def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError(f"No se puede dividir {a} entre cero.")
    return a / b
