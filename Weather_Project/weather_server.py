import socket
import requests
import datetime


def get_weather(city):
    try:
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1d23b5fc6043031715d16d21264a529a"
        json_data = requests.get(api).json()
        temp = int(json_data["main"]["temp"] - 273.15)
        feels_like = int(json_data["main"]["feels_like"] - 273.15)
        update = datetime.datetime.now()
        return (
            f"Temperature:{temp}°C\nFeels Like: {feels_like}°C\nLast Update: {update}"
        )
    except KeyError:
        return "No matching location found!"

def server_():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.53", 5555))
    server.listen()

    while True:
        client, adress = server.accept()
        data = client.recv(1024).decode("utf-8")
        result = get_weather(data)
        client.send(result.encode("utf-8"))
        print(data, ":", result)
        client.close()

server_()