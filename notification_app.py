import time

from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Simple Notification",
        message="Hello ,Have some coffe  ",
        timeout=10,
    )
    time.sleep(7)
