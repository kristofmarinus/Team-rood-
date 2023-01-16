def get_input_item(text: str, result_type:int = 0) -> any:
    """asks input and returns in correct type

    Args:
        text (str): text questions
        result_type (int, optional): 
            0 -> default -> str
            1 -> converts result to an int
            2 -> converts result to float

    Returns:
        any: returns result in type specified by result_type
    """
    result = input(f'{text}: ').strip()
    try:
        if result_type == 1:
            result = int(result)
        elif result_type == 2:
            result = float(result.replace(',', '.'))
    except Exception as e:
        result = 0

    return result

def get_int(text):
    """
    gets int , if not integer given it will keep asking without crashing
    :param text:
    :return:
    """
    n = 0
    while n == 0:
        inp = input(f'{text}')
        if inp.isdigit():
            n += 1
            return inp
        else:
            continue