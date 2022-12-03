from datetime import datetime
import requests

if __name__ == '__main__':
    # request 1 - GET
    hour = datetime.now().hour
    minute = datetime.now().minute
    param = "hour=" + str(hour) + "&" + "minute=" + str(minute)

    print("1 - GET")
    responseGet = requests.get('http://localhost:8989/test_get_method', params={'hour': hour, 'minute': minute})
    print("response: " + responseGet.text)

    # request 2 - POST
    bodyPost = {
        'hour': hour,
        'minute': minute,
        'requestId': responseGet.text}

    print("2 - POST")
    responsePost = requests.post('http://localhost:8989/test_post_method', data=bodyPost)
    print("response: " + responsePost.text)

    # request 3 - PUT
    print("3 - PUT")
    messagePost = responsePost.json()['message']
    hour = (hour + 21) % 24
    minute = (minute + 13) % 60
    bodyPut = {
        "hour": hour,
        "minute": minute}
    responsePut = requests.put('http://localhost:8989/test_put_method', params={"id": messagePost}, data=bodyPut)
    messagePut = responsePut.json()['message']
    print("response: " + messagePut)

    # request 4 - DELETE
    print("4 - DELETE")
    requests.delete('http://localhost:8989/test_delete_method', params={"id": messagePut})
