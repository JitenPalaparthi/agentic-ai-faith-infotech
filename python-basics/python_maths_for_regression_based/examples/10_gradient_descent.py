w=0.0; alpha=0.1
for step in range(10):
    loss=(w-3)**2
    grad=2*(w-3)
    print(step, "w=",round(w,4),"loss=",round(loss,4),"gradient=",round(grad,4))
    w = w-alpha*grad
