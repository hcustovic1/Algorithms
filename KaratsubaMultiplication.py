def karatsuba_multiplication(x, y):

    str_x, str_y = str(x), str(y)

    if len(str_x) == 1 or len(str_y) == 1:
        return x * y

    max_len = max(len(str_x), len(str_y))
    max_half_len = max_len // 2

    a = x // (10**max_half_len)
    b = x % (10**max_half_len)
    c = y // (10**max_half_len)
    d = y % (10**max_half_len)

    bd = karatsuba_multiplication(b, d)
    adbc = karatsuba_multiplication(a + b, c + d)
    ac = karatsuba_multiplication(a, c)

    multiplication = 10**(max_half_len * 2) * ac + 10**max_half_len * (adbc - ac - bd) + bd

    return multiplication


def main():
    x = int(input("Please input the first number: "))
    y = int(input("Please input the second number "))

    result = karatsuba_multiplication(x, y)
    print("The result of the multiplication x * y is", result)

if __name__ == '__main__':
    main()
