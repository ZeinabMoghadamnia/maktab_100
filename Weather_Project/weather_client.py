import socket

def client_(city_name):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(("127.0.0.53", 5555))
    client.send(city_name.encode("utf-8"))
    data = client.recv(1024).decode("utf-8")
    return data


city_name = input("Enter a name city: ")
result = client_(city_name)
while True:
    if result == "No matching location found!\n":
        print(result+"Enter a valid name!")
        city_name2 = input("\nEnter a name city: ")
        result = client_(city_name2)
    else:
        print(result)
        break
