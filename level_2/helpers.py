# calcula o fatorial de n
def fatorial_calc(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_calc(n - 1)    
