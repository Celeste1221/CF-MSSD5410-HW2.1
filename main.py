from SortFunctions import quick_sort
import random
import csv


def main():
    movies_by_genre = []
    # read file into the movies_by_genre list
    with open('movies.csv', encoding="utf8", newline='\n') as csvfile:  # added utf8 encoding to fix UnicodeDecodeError
        movie_reader = csv.reader(csvfile, delimiter=',')
        for row in movie_reader:
            movies_by_genre.append((row[2].split('|')[0], row[1]))

    # quicksort the movies_by_genre list
    quick_sort(0, len(movies_by_genre) - 1, movies_by_genre)

    # Accept input from the user asking how many movie recommendations they want (3-7)
    choice = input("How many movie recommendations would you like? Choose a number 3-7: ")

    # Choose a random index from the list of sorted movies and use the user's choice number to give that many
    # recommendations in the same genre
    x = random.randint(0, len(movies_by_genre) - 1)

    # match case statement for user input
    match choice:
        case '3':
            s = slice(x - 1, x + 2)
            print(movies_by_genre[s])
        case '4':
            s = slice(x - 2, x + 2)
            print(movies_by_genre[s])
        case '5':
            s = slice(x - 2, x + 3)
            print(movies_by_genre[s])
        case '6':
            s = slice(x - 3, x + 3)
            print(movies_by_genre[s])
        case '7':
            s = slice(x - 3, x + 4)
            print(movies_by_genre[s])
        case _:  # default case if the user input doesn't match any of the other cases, give 3 recommendations
            s = slice(x - 1, x + 2)
            print("Invalid entry. Here are 3 recommendations: ")
            print(movies_by_genre[s])


if __name__ == "__main__":
    main()
