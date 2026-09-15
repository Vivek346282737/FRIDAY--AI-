"""
FRIDAY AI
System Monitor

Master collector for all desktop monitoring modules.
"""

from __future__ import annotations

from datetime import datetime

from desktop.cpu import cpu_monitor
from desktop.memory import memory_monitor
from desktop.gpu import gpu_monitor
from desktop.battery import battery_monitor
from desktop.network import network_monitor
from desktop.windows import windows_monitor
from desktop.processes import process_monitor


class SystemMonitor:
    """Collect complete system information."""

    def get_info(self):

        return {

            "status": "ok",

            "timestamp": datetime.now().isoformat(),

            "cpu": cpu_monitor.get_info(),

            "memory": memory_monitor.get_info(),

            "gpu": gpu_monitor.get_info(),

            "battery": battery_monitor.get_info(),

            "network": network_monitor.get_info(),

            "windows": windows_monitor.get_info(),

            "processes": process_monitor.get_info(),

        }


system_monitor = SystemMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(system_monitor.get_info())