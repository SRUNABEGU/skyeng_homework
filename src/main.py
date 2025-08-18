from typing import Union


def gans(arg1: Union[int, float], arg2: Union[int, float]) -> float:
    """
    Делит 'arg1' на 'arg2'
    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """
    return arg1 / arg2


print(gans(10, 5))

def HelloWorld(print: str):
    print = "print"
    return print


HelloWorld("print")
