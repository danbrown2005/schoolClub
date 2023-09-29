def accept_int(prompt_message=" ", error_message="Please input a valid integer", lower_bound=None, upper_bound=None):
    if not isinstance(prompt_message, str):
        raise TypeError("promptMessage should be of type <str>")
    if not isinstance(error_message, str):
        raise TypeError("errorMessage should be of type <str>")

    while True:
        user_input = input(prompt_message)
        try:
            output = int(user_input)
            if (lower_bound is None or output >= lower_bound) and (upper_bound is None or output <= upper_bound):
                return output
            else:
                print(error_message)
        except ValueError:
            print(error_message)


def accept_str(prompt_message="Input: ", error_message="Please input a valid alphabetical string"):
    if not isinstance(prompt_message, str):
        raise TypeError("promptMessage should be of type <str>")
    if not isinstance(error_message, str):
        raise TypeError("errorMessage should be of type <str>")

    while True:
        user_input = input(prompt_message)
        if user_input.isalpha():
            return user_input
        else:
            print(error_message)
