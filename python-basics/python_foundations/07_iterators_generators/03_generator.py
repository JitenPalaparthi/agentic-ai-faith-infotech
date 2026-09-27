def squares(n):
    for i in range(n):
        yield i*i

print(list(squares(5)))
