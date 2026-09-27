def demo(a, /, b, *, c):
    print(a, b, c)

demo(1, 2, c=3)
