import os
import shutil
import subprocess
import time
import webbrowser
from urllib.parse import quote_plus


class ApplicationService:

    def __init__(self):

        self.websites = {

            # ==========================================
            # SEARCH
            # ==========================================

            "google": "https://www.google.com",
            "bing": "https://www.bing.com",
            "duckduckgo": "https://duckduckgo.com",

            # ==========================================
            # AI
            # ==========================================

            "chatgpt": "https://chatgpt.com",
            "openai": "https://openai.com",
            "claude": "https://claude.ai",
            "gemini": "https://gemini.google.com",

            # ==========================================
            # VIDEO / MUSIC
            # ==========================================

            "youtube": "https://www.youtube.com",
            "spotify": "https://open.spotify.com",
            "netflix": "https://www.netflix.com",

            # ==========================================
            # SOCIAL
            # ==========================================

            "instagram": "https://www.instagram.com",
            "facebook": "https://www.facebook.com",
            "x": "https://x.com",
            "twitter": "https://x.com",
            "linkedin": "https://www.linkedin.com",
            "reddit": "https://www.reddit.com",

            # ==========================================
            # COMMUNICATION
            # ==========================================

            "gmail": "https://mail.google.com",
            "google mail": "https://mail.google.com",
            "whatsapp": "https://web.whatsapp.com",
            "discord": "https://discord.com/app",

            # ==========================================
            # DEVELOPMENT
            # ==========================================

            "github": "https://github.com",
            "gitlab": "https://gitlab.com",
            "stackoverflow": "https://stackoverflow.com",

            # ==========================================
            # SHOPPING
            # ==========================================

            "amazon": "https://www.amazon.in",
            "flipkart": "https://www.flipkart.com",

            # ==========================================
            # PRODUCTIVITY
            # ==========================================

            "google drive": "https://drive.google.com",
            "google docs": "https://docs.google.com",
            "google sheets": "https://sheets.google.com",
            "google calendar": "https://calendar.google.com",

        }

        self.desktop_apps = {

            # ==========================================
            # WINDOWS APPS
            # ==========================================

            "notepad": ["notepad.exe"],
            "calculator": ["calc.exe"],
            "paint": ["mspaint.exe"],
            "task manager": ["taskmgr.exe"],
            "explorer": ["explorer.exe"],
            "file explorer": ["explorer.exe"],
            "cmd": ["cmd.exe"],
            "command prompt": ["cmd.exe"],
            "powershell": ["powershell.exe"],

            # ==========================================
            # BROWSERS
            # ==========================================

            "chrome": [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            ],

            "google chrome": [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            ],

            "edge": [
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            ],

            "microsoft edge": [
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            ],

            # ==========================================
            # DEVELOPMENT
            # ==========================================

            "vscode": ["code"],
            "vs code": ["code"],
            "visual studio code": ["code"],

            # ==========================================
            # MUSIC
            # ==========================================

            "spotify": [
                os.path.expandvars(
                    r"%APPDATA%\Spotify\Spotify.exe"
                )
            ],

        }

    # =====================================================
    # NORMALIZE
    # =====================================================

    def normalize(self, name):

        return (
            str(name)
            .lower()
            .strip()
        )

    # =====================================================
    # WEBSITE CHECK
    # =====================================================

    def is_website(self, target):

        target = self.normalize(target)

        return target in self.websites

    # =====================================================
    # APP CHECK
    # =====================================================

    def is_desktop_app(self, target):

        target = self.normalize(target)

        return target in self.desktop_apps

    # =====================================================
    # OPEN WEBSITE
    # =====================================================

    def open_website(self, target):

        target = self.normalize(target)

        if target not in self.websites:

            return {

                "success": False,

                "message": (
                    f"Unknown website: {target}"
                )

            }

        url = self.websites[target]

        try:

            webbrowser.open(
                url,
                new=2
            )

            return {

                "success": True,

                "type": "website",

                "target": target,

                "url": url,

                "message": (
                    f"Opened {target}."
                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # OPEN DESKTOP APPLICATION
    # =====================================================

    def open_desktop_app(self, target):

        target = self.normalize(target)

        commands = self.desktop_apps.get(
            target
        )

        if not commands:

            return {

                "success": False,

                "message": (
                    f"Unknown desktop application: {target}"
                )

            }

        for command in commands:

            try:

                if os.path.exists(command):

                    subprocess.Popen(
                        [command],
                        shell=False
                    )

                    return {

                        "success": True,

                        "type": "desktop_app",

                        "application": target,

                        "message": (
                            f"Opened {target} successfully."
                        )

                    }

                if shutil.which(command):

                    subprocess.Popen(
                        command,
                        shell=True
                    )

                    return {

                        "success": True,

                        "type": "desktop_app",

                        "application": target,

                        "message": (
                            f"Opened {target} successfully."
                        )

                    }

                if command.endswith(".exe"):

                    subprocess.Popen(
                        command,
                        shell=True
                    )

                    return {

                        "success": True,

                        "type": "desktop_app",

                        "application": target,

                        "message": (
                            f"Opened {target} successfully."
                        )

                    }

            except Exception:

                continue

        return {

            "success": False,

            "message": (
                f"Could not open {target}."
            )

        }

    # =====================================================
    # OPEN ANYTHING
    # =====================================================

    def open(self, target):

        target = self.normalize(target)

        # -----------------------------------------------
        # WEBSITE
        # -----------------------------------------------

        if self.is_website(target):

            return self.open_website(
                target
            )

        # -----------------------------------------------
        # DESKTOP APP
        # -----------------------------------------------

        if self.is_desktop_app(target):

            return self.open_desktop_app(
                target
            )

        # -----------------------------------------------
        # TRY WINDOWS START COMMAND
        # -----------------------------------------------

        try:

            subprocess.Popen(
                f'start "" "{target}"',
                shell=True
            )

            return {

                "success": True,

                "type": "generic_application",

                "application": target,

                "message": (
                    f"Attempted to open {target}."
                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # GOOGLE SEARCH
    # =====================================================

    def google_search(self, query):

        query = str(query).strip()

        if not query:

            return {

                "success": False,

                "message": "Search query is empty."

            }

        url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        try:

            webbrowser.open(
                url,
                new=2
            )

            return {

                "success": True,

                "type": "google_search",

                "query": query,

                "url": url,

                "message": (
                    f"Searched Google for {query}."
                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # YOUTUBE SEARCH
    # =====================================================

    def youtube_search(self, query):

        query = str(query).strip()

        if not query:

            return {

                "success": False,

                "message": "YouTube search query is empty."

            }

        url = (
            "https://www.youtube.com/results?search_query="
            + quote_plus(query)
        )

        try:

            webbrowser.open(
                url,
                new=2
            )

            return {

                "success": True,

                "type": "youtube_search",

                "query": query,

                "url": url,

                "message": (
                    f"Searched YouTube for {query}."
                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # SPOTIFY SEARCH
    # =====================================================

    def spotify_search(self, query):

        query = str(query).strip()

        if not query:

            return {

                "success": False,

                "message": "Spotify search query is empty."

            }

        url = (
            "https://open.spotify.com/search/"
            + quote_plus(query)
        )

        try:

            webbrowser.open(
                url,
                new=2
            )

            return {

                "success": True,

                "type": "spotify_search",

                "query": query,

                "url": url,

                "message": (
                    f"Searched Spotify for {query}."
                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # GENERIC WEB SEARCH
    # =====================================================

    def search(self, platform, query):

        platform = self.normalize(platform)

        if platform == "google":

            return self.google_search(
                query
            )

        if platform == "youtube":

            return self.youtube_search(
                query
            )

        if platform == "spotify":

            return self.spotify_search(
                query
            )

        return {

            "success": False,

            "message": (
                f"Search is not yet supported "
                f"for {platform}."
            )

        }


application_service = ApplicationService()