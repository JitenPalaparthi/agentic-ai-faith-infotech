def loss(w): return (w-3)**2
def derivative(w): return 2*(w-3)
for w in [0,1,2,3,4]:
    print(f"w={w}, loss={loss(w)}, derivative={derivative(w)}")
