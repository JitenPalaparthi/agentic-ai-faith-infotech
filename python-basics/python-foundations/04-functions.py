
def fib(n):
    fibs=[]
    a,b=0,1
    for _ in range(n):
        fibs.append(a)
        #print(a)
        a,b = b,a+b
    return tuple(fibs)

def exec():
    fiblist = fib(10)
    print(fiblist,type(fiblist))

if __name__=="__main__":
    exec()

    employees= [
        {"name":"A","skills":["Java","Python","Docker"]},
        {"name":"B","skills":["CSharp","Python","Devops"]},
        {"name":"C","skills":["CSharp","Java","Devops"]}
        ]
    print([e["name"] for e in employees if "Python" in e["skills"]])