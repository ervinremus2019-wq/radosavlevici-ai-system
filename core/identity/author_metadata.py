# Immutable author metadata

AUTHOR_NAME = "Ervin Remus Radosavlevici"
DOB = "01/09/1987"
PRIMARY_EMAIL = "ervin210@icloud.com"
COPYRIGHT = "© 2026 Ervin Remus Radosavlevici"
IMMUTABLE = True


def verify_author(metadata):
    if metadata.get("AUTHOR_NAME") != AUTHOR_NAME:
        raise PermissionError("Unauthorized modification detected!")