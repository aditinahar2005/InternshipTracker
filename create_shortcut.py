import os
import winshell
from win32com.client import Dispatch

def create_shortcut():
    # Get the path to the desktop
    desktop = winshell.desktop()

    # Define the path for the shortcut
    path = os.path.join(desktop, "Internship Tracker.lnk")

    # Get the absolute path to the target script
    target = os.path.abspath(os.path.join(os.path.dirname(__file__), "Internship_tracker.py"))

    # Define the working directory and icon path
    wDir = os.path.dirname(target)
    icon = target

    # Create a shell object
    shell = Dispatch('WScript.Shell')

    # Create a shortcut object
    shortcut = shell.CreateShortCut(path)

    # Set shortcut properties
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon

    # Save the shortcut
    shortcut.save()

# Run the script to create the shortcut if this file is executed directly
if __name__ == '__main__':
    create_shortcut()
