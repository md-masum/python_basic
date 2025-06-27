def do_stuff(number):
    try:
        return int(number) * 2
    except ValueError as error:
        return error
