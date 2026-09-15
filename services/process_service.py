import os
import subprocess
import shutil

import psutil


APP_ALIASES = {
    "chrome": "chrome",
    "google chrome": "chrome",
    "edge": "msedge",
    "microsoft edge": "msedge",
    "notepad": "notepad",
    "calculator": "calc",
    "calc": "calc",
    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",
    "cmd": "cmd",
    "command prompt": "cmd",
    "powershell": "powershell",
    "power shell": "powershell",
    "explorer": "explorer",
    "file explorer": "explorer",
    "paint": "mspaint",
    "settings": "settings",
    "task manager": "taskmgr",
    "control panel": "control",
}


COMMON_APP_PATHS = {
    "chrome": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ],

    "msedge": [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ],

    "code": [
        os.path.expandvars(
            r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
        ),
    ],

    "firefox": [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
    ],

    "steam": [
        r"C:\Program Files (x86)\Steam\steam.exe",
        r"C:\Program Files\Steam\steam.exe",
    ],
}


def normalize_app_name(app_name: str):

    name = str(app_name).strip().lower()

    return APP_ALIASES.get(
        name,
        name
    )


def get_start_menu_directories():

    directories = [

        os.path.expandvars(
            r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
        ),

        os.path.expandvars(
            r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs"
        ),

    ]

    return [

        directory
        for directory in directories
        if os.path.isdir(directory)
    ]


def find_start_menu_app(app_name: str):

    search_name = app_name.lower().strip()

    matches = []

    for base_directory in get_start_menu_directories():

        for root, _, files in os.walk(base_directory):

            for file_name in files:

                if not file_name.lower().endswith(".lnk"):

                    continue

                shortcut_name = os.path.splitext(
                    file_name
                )[0].lower()

                full_path = os.path.join(
                    root,
                    file_name
                )

                if shortcut_name == search_name:

                    return full_path

                if search_name in shortcut_name:

                    matches.append(
                        full_path
                    )

    if matches:

        matches.sort(
            key=lambda path: len(
                os.path.basename(path)
            )
        )

        return matches[0]

    return None


def find_executable(app_name: str):

    executable = shutil.which(app_name)

    if executable:

        return executable

    executable = shutil.which(
        f"{app_name}.exe"
    )

    if executable:

        return executable

    for path in COMMON_APP_PATHS.get(
        app_name,
        []
    ):

        expanded_path = os.path.expandvars(
            path
        )

        if os.path.exists(expanded_path):

            return expanded_path

    return None


def open_special_app(app_name: str):

    special_apps = {

        "notepad": "notepad.exe",
        "calc": "calc.exe",
        "cmd": "cmd.exe",
        "powershell": "powershell.exe",
        "explorer": "explorer.exe",
        "mspaint": "mspaint.exe",
        "taskmgr": "taskmgr.exe",
        "control": "control.exe",

    }

    executable = special_apps.get(
        app_name
    )

    if not executable:

        return None

    try:

        subprocess.Popen(
            executable
        )

        return {

            "success": True,

            "message": (
                f"Opened {app_name} successfully."
            ),

            "application": app_name

        }

    except Exception as error:

        return {

            "success": False,

            "message": str(error)

        }


def open_app(app_name: str):

    if not app_name:

        return {

            "success": False,

            "message": "Application name is missing."

        }

    original_name = str(
        app_name
    ).strip()

    normalized_name = normalize_app_name(
        original_name
    )

    if normalized_name == "settings":

        try:

            os.startfile(
                "ms-settings:"
            )

            return {

                "success": True,

                "message": (
                    "Opened Settings successfully."
                ),

                "application": original_name

            }

        except Exception as error:

            return {

                "success": False,

                "message": str(error)

            }

    special_result = open_special_app(
        normalized_name
    )

    if special_result is not None:

        return special_result

    executable = find_executable(
        normalized_name
    )

    if executable:

        try:

            command = [

                executable

            ]

            if normalized_name == "chrome":

                command.extend([
                    "--profile-directory=Default"
                ])

            subprocess.Popen(
                command
            )

            return {

                "success": True,

                "message": (
                    f"Opened {original_name} successfully."
                ),

                "application": original_name,

                "path": executable

            }

        except Exception as error:

            return {

                "success": False,

                "message": str(error)

            }

    shortcut = find_start_menu_app(
        original_name
    )

    if shortcut:

        try:

            os.startfile(
                shortcut
            )

            return {

                "success": True,

                "message": (
                    f"Opened {original_name} successfully."
                ),

                "application": original_name,

                "shortcut": shortcut

            }

        except Exception as error:

            return {

                "success": False,

                "message": str(error)

            }

    return {

        "success": False,

        "message": (
            f"Could not find an installed application "
            f"named '{original_name}'."
        )

    }


def find_matching_processes(app_name: str):

    normalized_name = normalize_app_name(
        app_name
    )

    search_terms = {

        normalized_name.lower(),

        f"{normalized_name.lower()}.exe"

    }

    matches = []

    for process in psutil.process_iter(

        [
            "pid",
            "name",
            "exe"
        ]

    ):

        try:

            process_name = (
                process.info["name"]
                or ""
            ).lower()

            process_path = (
                process.info["exe"]
                or ""
            ).lower()

            if any(

                term in process_name
                or term in process_path

                for term in search_terms

            ):

                matches.append(
                    process
                )

        except (

            psutil.NoSuchProcess,

            psutil.AccessDenied

        ):

            continue

    return matches


def close_app(app_name: str):

    if not app_name:

        return {

            "success": False,

            "message": (
                "Application name is missing."
            )

        }

    original_name = str(
        app_name
    ).strip()

    processes = find_matching_processes(
        original_name
    )

    if not processes:

        return {

            "success": False,

            "message": (
                f"{original_name} is not currently running."
            )

        }

    try:

        for process in processes:

            try:

                process.terminate()

            except (

                psutil.NoSuchProcess,

                psutil.AccessDenied

            ):

                continue

        _, alive = psutil.wait_procs(

            processes,

            timeout=3

        )

        for process in alive:

            try:

                process.kill()

            except (

                psutil.NoSuchProcess,

                psutil.AccessDenied

            ):

                continue

        return {

            "success": True,

            "message": (
                f"Closed {len(processes)} "
                f"process(es) for "
                f"{original_name}."
            ),

            "closed_processes": len(
                processes
            )

        }

    except Exception as error:

        return {

            "success": False,

            "message": str(error)

        }
