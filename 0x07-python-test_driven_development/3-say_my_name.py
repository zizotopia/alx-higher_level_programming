#!/usr/bin/python3
"""say_my_name

"""


def say_my_name(first_name, last_name=""):
    """say_my_name
    arg:
        first_name: first name
        last_name: last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
