# with open('FILE PATH', 'w') as file:
#    ...

class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('OPEN FILE')
        self._file = open(self.file_path, self.mode)
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('CLOSE FILE')
        self._file.close()

        # raise class_exception("FUCK")
        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        return True # Handle Exception

with MyOpen('file.txt', 'w') as file:
    file.write('LINE 1\n')
    file.write('LINE 2\n', 1234)
    file.write('LINE 3\n')
    print('WITH', file)
