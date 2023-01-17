from dataclasses import dataclass, field
import getpass


@dataclass
class Prerequisite:
    username: str = field(default="")
    password: str = field(default="")
    values: list = field(default_factory=list)
    number_of_posts: int = field(default=0)


def define_prerequisites() -> Prerequisite:

    username = input('Type username:')
    password = getpass.getpass(prompt='Enter password:')     #password = input('Type password:')

    state = False

    while(state == False):

        user_input = input('Define 3 search keywords for liking posts, separated by comma:')
        values = user_input.split(',')

        if len(values) == 3:

            print('You have defined 3 search keywords')
            state = True

        else:
            
            print('You have not defined 3 search keywords, Try again (Y) or exit the programm (Anything).')
            user_input = input()
            if user_input == 'Y':
                continue
            else:
                exit()

    number_of_posts = int(input('Define number of posts to like:'))

    return Prerequisite(username, password, values, number_of_posts)