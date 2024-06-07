"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'Student_name' : 'Pankaj Kesri',
        'Student_ID' : '10284560',
        'Toppings' : [
            'TOMATOES',
            'ONIONS',
            'GREEN PEPPERS'
        ],
        'movies': [
            {
                'title': 'Ghost Rider',
                'genre': 'sci-fi'
            },
            {
                'title': 'Iron-man 2',
                'genre': 'adventure'
            },
            {
                'title': 'Venom',
                'genre': 'Action'
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)
    
    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['mushroom', 'tofu'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'Hulk', 'Action')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    Student_name = my_info["Student_name"]
    Student_first_name = Student_name.split()[0]
    print(f' My name is {Student_name}, but you can call me Sir {Student_first_name}.\n My student ID is {my_info["Student_ID"]}.\n')

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    print(" My favourite pizza toppings are:")
    for topping in my_info["Toppings"]:
        print(f'- {topping}')
    print()

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    my_info['Toppings'].extend(toppings)
    my_info['Toppings'] = sorted({topping.lower() for topping in my_info["Toppings"]}, key=str.lower)

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    new_movie = {'title': title, 'genre': genre}
    my_info['movies'].append(new_movie)

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    genres = [movie["genre"] for movie in my_info["movies"]]
    genres = [genre for genre in genres if genre]
    if len(genres) > 1:
        genres_result = ', '.join(genres[:-1]) + ' and ' + genres[-1]
    else:
        genres_result = genres[0] if genres else 'no genres'
    print(" I like to watch " + genres_result + " movies.\n")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    titles = [movie["title"].title() for movie in movie_list]
    if len(titles) > 1:
        titles_result = ', '.join(titles[:-1]) + ' and ' + titles[-1]
    else:
        titles_result = titles[0]
    print(f"Some of my favourite movies are {titles_result}!\n")

if __name__ == '__main__':
    main()