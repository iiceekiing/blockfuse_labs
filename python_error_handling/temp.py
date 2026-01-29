

def change_case(func):
    def wrapper(*args, **kwargs):
        result = func().upper()
        return result
    return wrapper


@change_case
def text():
    return "Hello World"

result = text()

print(result)