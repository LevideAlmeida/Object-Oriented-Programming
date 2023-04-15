class MyError(Exception):
    ...

class YourError(Exception):
    ...

def raise_my_error():
    exception_ = MyError('My', 'error', '😃')
    raise exception_

try:
    raise_my_error()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = YourError('Raise again 👍')
    raise exception_ from error
