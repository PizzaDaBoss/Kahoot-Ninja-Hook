import random
import json
import time
import requests

code = input("Code: ")
url = "https://connect.kahoot.ninja/start/" + str(code)

while True:
        requests.post(url, allow_redirects=False)
        print("Sent 20 more bots to " + code)