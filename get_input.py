def get_input(prompt, type = 0, allow_empty = False):
    """
    handles getting input. 

    Args:
        prompt(_str_): the question the user sees during input
        type(int):    
                type = 0 (default) -> string
                type = 1 -> int
                type = 2 -> float
        allow_empty(bool):  Empty input is only allowed when type == 1

    Returns:
        str: the inputted value
    """
    s_input = input(prompt).strip()
    if allow_empty == True and type == 0:
        if len(s_input) == 0:
            return None
    if type == 0:  #output will be a string        
        if len(s_input) !=  0:
            return s_input
        return get_input(prompt)

    if type == 1:   #output will be an integer
        if len(s_input) !=  0:
            return make_input_int(s_input)
        return get_input(prompt)
        
    if type == 2:   #output will be a float value
        if len(s_input) !=  0:
            return make_input_float(s_input)
        return get_input(prompt)


def make_input_int(s_input : str)-> int:
    """converts an input value (str) into an integer. To be used in combination with get_input()

    Args:
        s_input (str): _description_

    Returns:
        int: integer of the input value
    """
    try:
        return int(s_input)
    except:
        print('input was geen integer...')
        return make_input_int(get_input('probeer opnieuw: '))


def make_input_float(s_input : str)-> float:
    """converts an input value (str) into an integer. To be used in combination with get_input()

    Args:
        s_input (str): _description_

    Returns:
        float: float of the input value
    """
    try:
        return float(s_input)
    except:
        print('input was geen getal...')
        return make_input_int(get_input('probeer opnieuw: '))


