def add(x, y):
    """Add x and y"""
    return x + y


def subtract(x, y):
    """subtract"""
    return x - y


def multiply(x, y):
    """multiply x and y"""
    return x * y


def divide(x, y):
    """divide x by y"""
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y
