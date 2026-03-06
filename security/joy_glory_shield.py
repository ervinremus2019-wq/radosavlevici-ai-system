# Prevent unauthorized execution
from core.identity.author_metadata import AUTHOR_NAME, verify_author


def shield(metadata):
    try:
        verify_author(metadata)
        print("System verified: Authorized user.")
    except PermissionError as e:
        print(str(e))
        print("Disabling system due to unauthorized modification.")
        exit(1)


# Example usage
if __name__ == "__main__":
    user_metadata = {"AUTHOR_NAME": "Ervin Remus Radosavlevici"}
    shield(user_metadata)