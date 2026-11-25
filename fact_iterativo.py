def fact(n: int) -> int:
    def fact_iter(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return fact_iter(n - 1, acc * n)
    return fact_iter(n, 1)


def fact(n: int) -> int:
    def fact_iter(acc: int) -> int:
        nonlocal n
        if n == 0:
            return acc
        acc *= n
        n -= 1
        return fact_iter(acc)
    return fact_iter(1)


def fact(n: int) -> int:
    def fact_iter() -> int:
        nonlocal n, acc
        if n == 0:
            return acc
        acc *= n
        n -= 1
        return fact_iter()
    acc = 1
    return fact_iter()

    acc = 1


print(fact(5))


def f():
    x = 5
    def g():
        nonlocal x
        x = 3
        def h():
            nonlocal x
            x = 6
        h()
    g()
    print(x)

    