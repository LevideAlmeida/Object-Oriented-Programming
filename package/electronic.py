from log import LogFileMixin

class Electronic:
    def __init__(self, name):
        self._name = name
        self._on = False

    def turn_on(self):
        if not self._on:
            self._on = True

    def turn_off(self):
        if self._on:
            self._on = True


class Smartphone(Electronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()

        if self._on:
            mensage = f'{self._name} is on'
            self.log_success(mensage)

    def turn_off(self):
        super().turn_off()

        if not self._on:
            mensage = f'{self._name} is off'
            self.log_error(mensage)
