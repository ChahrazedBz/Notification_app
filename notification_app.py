import time

from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Simple Notification",
        message="Everything is gonna be alright Dont worry ",
        timeout=10,
    )
    time.sleep(7)
