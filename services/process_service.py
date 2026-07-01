import os
import subprocess
import psutil


APP_PATHS = {

    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

    "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",

    "notepad": "notepad.exe",

    "calculator": "calc.exe",

    "cmd": "cmd.exe",

    "powershell": "powershell.exe",

    "explorer": "explorer.exe",

    "settings": "ms-settings:",

}


def open_app(app_name: str):

    app_name = app_name.lower()

    if app_name not in APP_PATHS:
        return {
            "success": False,
            "message": "App not supported"
        }

    path = os.path.expandvars(APP_PATHS[app_name])

    try:

        if app_name == "settings":
            os.startfile(path)

        elif path.endswith(".exe"):
            subprocess.Popen(path)

        else:
            subprocess.Popen(path)

        return {
            "success": True,
            "message": f"{app_name} opened successfully"
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }


def close_app(app_name: str):

    app_name = app_name.lower()

    process_names = {

        "chrome": "chrome.exe",
        "edge": "msedge.exe",
        "vscode": "Code.exe",
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe",
        "cmd": "cmd.exe",
        "powershell": "powershell.exe",
        "explorer": "explorer.exe"

    }

    if app_name not in process_names:

        return {
            "success": False,
            "message": "Unsupported App"
        }

    killed = False

    for proc in psutil.process_iter():

        try:

            if proc.name().lower() == process_names[app_name].lower():

                proc.kill()
                killed = True

        except:

            pass

    return {
        "success": killed,
        "message": "Closed" if killed else "Not Running"
    }