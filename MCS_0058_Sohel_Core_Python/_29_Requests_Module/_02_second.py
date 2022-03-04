from urllib import request
import requests

r = requests.get("http://www.google.com")

print(r.status_code)

print(r.ok) # returns true if we get anything other than 400 response.

print(r.headers)