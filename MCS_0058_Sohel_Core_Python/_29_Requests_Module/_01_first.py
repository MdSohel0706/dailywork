import requests
import json

#api_token = "9a7bc416c03922b3d72879ac65f58b68"

#response = requests.get("https://openweathermap.org/", auth=("sohel.fazal1995@gmail.com", api_token))

#print(response.content)
'''
header_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEyMjgiLCJuYmYiOjE2NDU0MzYwNDksImV4cCI6MTY0ODAyODA0OSwiaWF0IjoxNjQ1NDM2MDQ5fQ.QBo8FY6mqYCjqYtBFvzuOrNH1VTrWDHKb2fDbwUrfnY"

headers = {"Authorization" : "Bearer "+header_token}

url = "https://api.aniapi.com/v1/auth"

response = requests.post(url, headers=headers)
print(response.json())
'''
def login(email, password):
    s = requests.Session()
    payload = {
        'email' : email,
        'password' : password
    }
    response = s.post("https://api.aniapi.com/v1/auth", json=payload)
    return response.content

session = login('dhanuhv@gmail.com', 'Aniapitoken111')
print(session)
