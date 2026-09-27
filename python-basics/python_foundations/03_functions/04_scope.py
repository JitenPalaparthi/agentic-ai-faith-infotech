x = "global"

def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "changed"
    inner()
    print(x)

outer()
print(x)
