import string


def handle_string(value):
    count_int = 0
    count_str = 0
    for x in tuple(value):
        if x in string.digits:
            count_int += 1
        elif x in string.ascii_letters:
            count_str += 1
    return 'Letters - {} \nDigits - {}'.format(count_str, count_int)

print(handle_string("Hello world! 123!"))

