import os

# We’ll define different commands depending on the OS
if os.name == "nt":  # Windows
    ALLOWED_COMMANDS = {
        "list_c": {
            "label": "List C:\\ directory",
            "cmd": ["cmd", "/c", "dir C:\\"],
        },
        "system_info": {
            "label": "Show system info (systeminfo)",
            "cmd": ["cmd", "/c", "systeminfo"],
        },
        "ip_config": {
            "label": "Show network config (ipconfig)",
            "cmd": ["cmd", "/c", "ipconfig /all"],
        },
        "processes": {
            "label": "List running processes (tasklist)",
            "cmd": ["cmd", "/c", "tasklist"],
        },
    }
else:  # Linux / macOS (posix)
    ALLOWED_COMMANDS = {
        "disk_usage": {
            "label": "Show disk usage (df -h)",
            "cmd": ["df", "-h"],
        },
        "list_root": {
            "label": "List root directory (ls -la /)",
            "cmd": ["ls", "-la", "/"],
        },
        "uptime": {
            "label": "Show system uptime",
            "cmd": ["uptime"],
        },
        "top_processes": {
            "label": "Top 10 processes by memory",
            "cmd": ["ps", "aux", "--sort=-%mem", "--head=10"],
        },
    }
