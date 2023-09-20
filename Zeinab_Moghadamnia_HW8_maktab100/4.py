import requests

api_url = "https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies"

def get_movies_list():
    
    response = requests.get(api_url)
    if response.status_code == 200:
        movies = response.json()
        print("Movies list:")
        for movie in movies:
            return f"Title: {movie['title']} - Year: {movie['year']}"
    else:
        return "Failed!!!"

def add_movie():
    title = input("Enter the title of the movie: ")
    year = input("Enter the year of the movie: ")
    genre = input("Enter the genre of the movie: ")
    author = input("Enter the name of the author: ")

    new_movie = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
    }

    response = requests.post(api_url, json= new_movie)

    if response.status_code == 201:
            print("Added successfully!")
    else:
        print("Added failed!")

if __name__ == "__main__":
    print("1. List of movies")
    print("2. Add a new movie")
    choice = input("\nSelect a menu: ")

    if choice == "1":
        get_movies_list()
    elif choice == "2":
        add_movie()
    else:
        print("Please enter the correct number!")
