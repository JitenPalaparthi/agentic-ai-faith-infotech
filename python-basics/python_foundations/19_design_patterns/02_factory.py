class Email: pass
class SMS: pass

def notifier(kind):
    if kind == "email": return Email()
    if kind == "sms": return SMS()
    raise ValueError(kind)

print(type(notifier("email")).__name__)
