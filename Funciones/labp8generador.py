def miGenerador():
    print("primero")
    yield 10
    print("segundo")
    yield 20
    print("tercero")
    yield 30
gen = miGenerador()
val1 = next(gen)
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)