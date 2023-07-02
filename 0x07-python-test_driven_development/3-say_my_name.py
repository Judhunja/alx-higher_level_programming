#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first name> <last name>

    Args:
        first_name(str): the person's first name
        last_name(str): the person's last name(optional)

    Raises:
        TypeError: if the arguments passed are not strings

    Returns:
        nothing
    """
    if type(first_name) != str or first_name == None:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
