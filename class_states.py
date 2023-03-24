class Camera:
    def __init__(self, name, is_filming=False):
        self.name = name
        self.is_filming = is_filming

    def filming(self):
        if self.is_filming:
            return f'{self.name} is already filming...'

        self.is_filming = True
        return f'{self.name} is filming...'

    def stop_filming(self):
        if not self.is_filming:
            return f"{self.name} already not film..."

        self.is_filming = False
        return f"{self.name} stop film..."

    def photograph(self):
        if self.is_filming:
            return f"{self.name} can't photograph while filming..."

        return f"{self.name} Photographed"


canon = Camera('Canon')
print(canon.filming())
print()

sony = Camera('Sony')

print(sony.filming())
print(sony.filming())
print(sony.photograph())
print(sony.stop_filming())
print(sony.photograph())

print()

print(canon.filming())
print(canon.photograph())
print(canon.stop_filming())
print(canon.photograph())
print(canon.filming())
