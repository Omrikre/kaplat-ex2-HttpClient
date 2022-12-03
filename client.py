from datetime import datetime
import requests

url = "localhost:8989"

# request 1 - GET
hour = datetime.now().hour
minute = datetime.now().minute
param = "hour=" + str(hour) + "&" + "minute=" + str(minute)

print("1 - GET")
print("request: " + url + "/test_get_method?" + param)
responseGet = requests.get(url + "/test_get_method?" + param)
print("response: " + responseGet.text)

# request 2 - POST
bodyPost = {
    'hour': hour,
    'minute': minute,
    'requestId': responseGet.text}

print("2 - POST")
print("request: " + url + "/test_post_method")
print("data: " + str(bodyPost))
responsePost = requests.post(url + "/test_post_method", data=bodyPost)
print("response: " + responsePost.text)

# request 3 - PUT
messagePost = responsePost.json()['message']
hour = (hour + 21) % 24
minute = (minute + 13) % 60
bodyPut = {
    "hour": hour,
    "minute": minute
}
responsePut = requests.put(url+"/test_put_method", params={"id": messagePost}, data=bodyPut)
messagePut = responsePut.json()['message']

# request 4 - DELETE
requests.delete(url + "/test_delete_method", params={"id": messagePut})
