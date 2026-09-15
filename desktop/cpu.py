"""
FRIDAY AI
CPU Monitor Module

Responsibilities
----------------
- CPU usage
- Per-core usage
- CPU frequency
- Physical cores
- Logical threads
- CPU model
- Architecture

This module contains NO FastAPI logic.
It is only responsible for collecting CPU information.
"""

from __future__ import annotations

import logging
import platform
from typing import Any

import cpuinfo
import psutil

logger = logging.getLogger(__name__)


class CPUMonitor:
    """Collect CPU information."""

    def __init__(self) -> None:
        self._cpu_info = cpuinfo.get_cpu_info()

    def get_info(self) -> dict[str, Any]:
        """
        Return CPU information as a dictionary.
        Never raises exceptions to the caller.
        """

        try:
            frequency = psutil.cpu_freq()

            return {
                "name": self._cpu_info.get("brand_raw", "Unknown CPU"),
                "architecture": platform.machine(),
                "physical_cores": psutil.cpu_count(logical=False),
                "logical_threads": psutil.cpu_count(logical=True),

                "usage_percent": psutil.cpu_percent(interval=0.5),

                "per_core_usage": psutil.cpu_percent(
                    interval=0.5,
                    percpu=True,
                ),

                "frequency": {
                    "current": round(frequency.current, 2)
                    if frequency else None,

                    "min": round(frequency.min, 2)
                    if frequency else None,

                    "max": round(frequency.max, 2)
                    if frequency else None,
                },
            }

        except Exception as exc:

            logger.exception("CPU Monitor Error")

            return {
                "status": "error",
                "message": str(exc),
            }


cpu_monitor = CPUMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(cpu_monitor.get_info())