import requests

base_url = "https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api"

def get_movie_list():
    '''check if get is successfull print list of movies'''
    endpoint = f"{base_url}/movies"
    response = requests.get(endpoint)

    if response.status_code == 200:
        movies = response.json()
        for movie in movies:
            print(movie)

    else:
        print(f"Error! Status code: {response.status_code}")

def add_movie():
    '''get the information of movies from user and write them in a dict
    post the dict in base url and check it's successfull or not'''
    title = input("Enter the movie title: ")
    year = input("Enter the movie year: ")
    runtime = input("Enter the movie runtime: ")
    poster = input("Enter the movie poster: ")

    endpoint = f"{base_url}/movies"
    new_movie = {
        "Title": title,
        "Year": year,
        "Runtime": runtime,
        "Poster": poster
    }

    response = requests.post(endpoint, json=new_movie)

    if response.status_code == 201:
        print("Movie added successfully.")
    else:
        print(f"Failed to add the movie. Status code: {response.status_code}")

def main():
    '''show options of menu and get an input and call each method that user choosed'''
    while True:
        print("\n1. Get Movie List")
        print("2. Add New Movie")
        print("3. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            get_movie_list()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            break
        else:
            print("Enter a correct number:")

if __name__ == "__main__":
    main()