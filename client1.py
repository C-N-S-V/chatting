import requests
import time

url = "http://192.168.185.24:5001/data"

while True:
    data = {"sensor": "temperature", "value": 22.5}
    try:
        response = requests.post(url, json=data)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    time.sleep(1)