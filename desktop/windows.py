"""
FRIDAY AI
Windows Monitor Module

Responsibilities
----------------
- OS Information
- Hostname
- Username
- Machine Type
- Processor
- Boot Time
- Uptime

No FastAPI logic.
"""

from __future__ import annotations

import getpass
import logging
import platform
import socket
from datetime import datetime
from typing import Any

import psutil

logger = logging.getLogger(__name__)


class WindowsMonitor:
    """Collect Windows system information."""

    def get_info(self) -> dict[str, Any]:

        try:

            boot = datetime.fromtimestamp(psutil.boot_time())

            uptime = datetime.now() - boot

            return {

                "status": "ok",

                "source": "platform",

                "timestamp": datetime.now().isoformat(),

                "os": platform.system(),

                "release": platform.release(),

                "version": platform.version(),

                "machine": platform.machine(),

                "processor": platform.processor(),

                "hostname": socket.gethostname(),

                "username": getpass.getuser(),

                "boot_time": boot.strftime("%Y-%m-%d %H:%M:%S"),

                "uptime_hours": round(
                    uptime.total_seconds() / 3600,
                    2,
                ),

            }

        except Exception as exc:

            logger.exception("Windows Monitor Error")

            return {

                "status": "error",

                "source": "platform",

                "timestamp": datetime.now().isoformat(),

                "message": str(exc),

            }


windows_monitor = WindowsMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(windows_monitor.get_info())