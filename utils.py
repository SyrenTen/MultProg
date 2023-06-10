
def validate_input(var_name, cast_typy):
    try:
        return cast_typy(input('Input {}: '.format(var_name)))
    except ValueError:
        return validate_input(var_name, cast_typy)
