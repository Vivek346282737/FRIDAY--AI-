"""
System tools — time and system monitoring.
"""

import datetime
import platform
import psutil


def register(mcp):

    @mcp.tool()
    def get_current_time() -> str:
        """Return the current date and time in ISO 8601 format."""
        return datetime.datetime.now().isoformat()

    @mcp.tool()
    def get_system_info() -> dict:
        """Return detailed information about the host system."""

        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        battery = psutil.sensors_battery()

        if battery:
            battery_percent = battery.percent
            charging = battery.power_plugged
        else:
            battery_percent = None
            charging = None

        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "python_version": platform.python_version(),

            "cpu_percent": psutil.cpu_percent(interval=1),

            "ram_percent": memory.percent,
            "ram_used_gb": round(memory.used / (1024 ** 3), 2),
            "ram_total_gb": round(memory.total / (1024 ** 3), 2),

            "disk_percent": disk.percent,
            "disk_used_gb": round(disk.used / (1024 ** 3), 2),
            "disk_total_gb": round(disk.total / (1024 ** 3), 2),

            "battery_percent": battery_percent,
            "charging": charging,
        }