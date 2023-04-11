# Abstration
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, mensage):
        raise NotImplementedError('Implement the log method')

    def log_error(self, mensage):
        return self._log(f'Error: ({mensage}) in {self.__class__.__name__}')

    def log_success(self, mensage):
        return self._log(f'Success: ({mensage})')



class LogFileMixin(Log):
    def _log(self, mensage):
        formated_mensage = f'{mensage}, {self.__class__.__name__}'
        with open(LOG_FILE, 'a') as file:
            file.write(formated_mensage)
            file.write('\n')



class LogPrintMixin(Log):
    def _log(self, mensage):
        print(f'{mensage}, {self.__class__.__name__}' )


if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print.log_error('LOG')
    log_print.log_success('11/04/2023')

    log_file = LogFileMixin()
    log_file.log_error('LOG')
    log_file.log_success('11/04/2023')
