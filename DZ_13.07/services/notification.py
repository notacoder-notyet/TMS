from datetime import time


def write_notification(email: str, message=""):
    time.sleep(5)
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)