import os
import platform

def bring_to_front():
    """
    Pokus o prepnutie okna do popredia pomocou AppleScript.
    Nefunguje spoľahlivo vo VSCode kvôli sandboxu.
    """
    if platform.system() == "Darwin":
        os.system(
            '''osascript -e 'tell application "System Events"
            to set frontmost of the first process whose unix id is (do shell script "echo $PPID") to true' '''
        )
