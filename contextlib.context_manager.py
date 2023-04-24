from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('OPEN FILE')
        file = open(file_path, mode)
        yield file
    except Exception as exception_:
        print('ERROR', exception_)
    finally:
        print('CLOSE FILE')
        file.close()


with my_open('file.txt', 'w') as file:
    file.write('LINE 1\n')
    file.write('LINE 2\n')
    file.write('LINE 3\n')
    print('WITH', file)
