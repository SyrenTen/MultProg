def validation(var_name, cast_typy):
    try:
        return cast_typy(input('Input {}: '.format(var_name)))
    except ValueError:
        return validation(var_name)