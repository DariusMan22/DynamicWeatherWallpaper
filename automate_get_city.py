import requests
import socket

hostname = socket.gethostname()
IPaddr = socket.gethostbyname(hostname)  
response = requests.get(f"https://geolocation-db.com/json/{IPaddr}&position=true").json()

print (response)