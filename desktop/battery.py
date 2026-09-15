"""
FRIDAY AI
Battery Monitor Module

Responsibilities
----------------
- Battery Percentage
- Charging Status
- Remaining Time
- Power Plugged

No FastAPI logic.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

import psutil

logger = logging.getLogger(__name__)


class BatteryMonitor:
    """Collect Battery information."""

    def get_info(self) -> dict[str, Any]:

        try:

            battery = psutil.sensors_battery()

            if battery is None:

                return {
                    "status": "unavailable",
                    "source": "psutil",
                    "timestamp": datetime.now().isoformat(),
                    "message": "Battery not detected."
                }

            secs = battery.secsleft

            if secs in (
                psutil.POWER_TIME_UNLIMITED,
                psutil.POWER_TIME_UNKNOWN,
            ):
                remaining = None
            else:
                hours = secs // 3600
                minutes = (secs % 3600) // 60
                remaining = f"{hours}h {minutes}m"

            return {

                "status": "ok",

                "source": "psutil",

                "timestamp": datetime.now().isoformat(),

                "percent": battery.percent,

                "charging": battery.power_plugged,

                "remaining": remaining,

            }

        except Exception as exc:

            logger.exception("Battery Monitor Error")

            return {

                "status": "error",

                "source": "psutil",

                "timestamp": datetime.now().isoformat(),

                "message": str(exc)

            }


battery_monitor = BatteryMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(battery_monitor.get_info())