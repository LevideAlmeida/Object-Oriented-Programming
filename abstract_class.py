# Abstract class - Abstract Base Class (ABC)
# Abstract classes are used to define new classes.
# Abstract class should not be used to create instances.

from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, mensage): ...

    def log_error(self, mensage):
        return self._log(f'Error: ({mensage}) in {self.__class__.__name__}')

    def log_success(self, mensage):
        return self._log(f'Success: ({mensage})')


class LogPrintMixin(Log):
    def _log(self, mensage):
        print(f'{mensage}' )

log = LogPrintMixin()
log.log_error('aaaaaaaa')
