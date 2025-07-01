def verificar_multiplo(numero):
    if numero % 5 == 0 and numero % 7 == 0:
        return "FIZZBUZZ"
    elif numero % 5 == 0:
        return "FIZZ"
    elif numero % 7 == 0:
        return "BUZZ"
    else:
        return "MISS"
