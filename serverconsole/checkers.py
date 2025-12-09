# serverconsole/checkers.py
import os
import subprocess
from typing import Tuple, Any, Dict

# Base path where you expect learners to work.
# For now, assume /app; you can change to /workspace or /home/student.
SANDBOX_BASE = "/app"


def _abs_path(relative: str) -> str:
    if os.path.isabs(relative):
        return relative
    return os.path.join(SANDBOX_BASE, relative)


def check_dir_exists(params: Dict[str, Any]) -> Tuple[bool, str]:
    rel_path = params.get("path", "")
    target = _abs_path(rel_path)
    exists = os.path.isdir(target)
    return exists, f"Directory exists={exists} at {target}"


def check_file_exists(params: Dict[str, Any]) -> Tuple[bool, str]:
    rel_path = params.get("path", "")
    target = _abs_path(rel_path)
    exists = os.path.isfile(target)
    return exists, f"File exists={exists} at {target}"


def check_file_contains(params: Dict[str, Any]) -> Tuple[bool, str]:
    rel_path = params.get("path", "")
    expected = params.get("contains", "")
    target = _abs_path(rel_path)

    if not os.path.isfile(target):
        return False, f"File {target} not found."

    try:
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return False, f"Could not read file: {e}"

    ok = expected in content
    return ok, f"Expected text found={ok} in {target}"


def check_pwd_equals(params: Dict[str, Any]) -> Tuple[bool, str]:
    expected = params.get("expect", SANDBOX_BASE)

    try:
        result = subprocess.run(
            ["pwd"],
            cwd=SANDBOX_BASE,
            capture_output=True,
            text=True,
            timeout=5,
        )
        actual = (result.stdout or "").strip()
    except Exception as e:
        return False, f"Error running pwd: {e}"

    ok = (actual == expected)
    return ok, f"pwd={actual}, expected={expected}"


CHECKERS = {
    "dir_exists": check_dir_exists,
    "file_exists": check_file_exists,
    "file_contains": check_file_contains,
    "pwd_equals": check_pwd_equals,
    # "manual" means: always false, learner just does it – we don't auto-check
}
