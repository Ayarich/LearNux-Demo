# serverconsole/consumers.py

import os
import pty
import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TerminalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope.get("user")

        if not user or not user.is_authenticated:
            await self.close()
            return

        await self.accept()

        # ---------------------------
        # REAL SHELL VIA PTY
        # ---------------------------
        self.master_fd, self.slave_fd = pty.openpty()

        self.process = await asyncio.create_subprocess_exec(
            "/bin/bash",
            "-i",
            stdin=self.slave_fd,
            stdout=self.slave_fd,
            stderr=self.slave_fd,
            env={**os.environ, "TERM": "xterm-256color"},
        )

        # Start background reader
        self.loop = asyncio.get_event_loop()
        self.loop.add_reader(self.master_fd, self._read_from_pty)

    async def disconnect(self, close_code):
        try:
            os.close(self.master_fd)
        except:
            pass

        if self.process:
            self.process.terminate()

    async def receive(self, text_data):
        data = json.loads(text_data).get("data", "")
        if data:
            os.write(self.master_fd, data.encode())

    def _read_from_pty(self):
        try:
            data = os.read(self.master_fd, 1024)
            asyncio.create_task(
                self.send(text_data=data.decode(errors="ignore"))
            )
        except:
            pass
