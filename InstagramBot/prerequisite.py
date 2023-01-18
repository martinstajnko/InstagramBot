"""
This file contains the function 'define_prerequisites()' which prompts the user to input their 
username, password, 3 search keywords, and number of posts to like. The function returns a 
Prerequisite object with the user's input.
"""


from dataclasses import dataclass, field
import getpass


@dataclass
class Prerequisite:
    username: str = field(default="")
    password: str = field(default="")
    values: list = field(default_factory=list)
    number_of_posts: int = field(default=0)


def define_prerequisites() -> Prerequisite:
    """
    Prompt the user to input their username, password, 3 search keywords, and number of posts to like.

    Returns:
        Prerequisite: A Prerequisite object with the user's input.
    """

    username = input('Type username:')
    password = getpass.getpass(prompt='Enter password:')

    while True:

        user_input = input('Define 3 search keywords for liking posts, separated by comma:')
        values = user_input.split(',')

        if len(values) == 3:
            print('You have defined 3 search keywords')
            break

        else:            
            print('You have not defined 3 search keywords, Try again (Y) or exit the programm (Anything).')
            user_input = input()

            if user_input != 'Y':
                exit()

    number_of_posts = int(input('Define number of posts to like:'))

    return Prerequisite(username, password, values, number_of_posts)