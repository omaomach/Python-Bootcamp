import time
from plyer import notification

while True:
    print("Take a glass of water!")
    notification.notify(
        title="Please drink some water",
        message="Its good for your health",
        timeout=10
    )
    time.sleep(3600)