def triangle(a, b, c: int):
    if a + b > c and c + b > a and c + a > b:
        print("Это треугольник")
    else:
        print("Это не треугольник")

triangle(a=7, b=6, c=10)