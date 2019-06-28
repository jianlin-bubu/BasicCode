def f(level):
    if level == 0:
        return
    print(level)
    f(level-1)
    print(level)

f(10)
