"""
File with some utils
"""

def calculate_percent(wins: int, battles: int) -> float:
    """
    Calculate user's win percent

    :param wins: User's win count
    :param battles: User's total battles count

    :return: Percent win ratio
    """

    try:
        percent = wins/battles * 100
    except ZeroDivisionError:
        return 0.0

    return float(f'{percent:.2f}')


def separate(number: int) -> str:
    """
    Separate decimal places of a number

    :param number: Number
    :return: Separated number
    :example: 
        Input: 1000000
        Output: 1,000,000
    """

    return f'{number:,}'
