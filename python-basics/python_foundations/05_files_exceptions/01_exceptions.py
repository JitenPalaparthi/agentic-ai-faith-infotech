try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("handled:", e)
finally:
    print("cleanup")
