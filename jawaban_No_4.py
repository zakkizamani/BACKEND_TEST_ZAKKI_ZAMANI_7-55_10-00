# 4. Buatlah function dengan Python untuk memeriksa suatu bilangan prima
def is_prima(x):
    for i in range(2, x):
        if x % i == 0:
            return "Bukan bilangan prima"

    return "Bilangan prima"
