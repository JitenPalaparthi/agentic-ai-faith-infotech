status = 404
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Other")
