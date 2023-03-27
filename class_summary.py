# method vs @classmethod vs @staticmethods
# method => self, instance method
# @classmethod => cls, class method
# @staticmethod => (❌self, ❌cls)

#Exemple:
class ConnectionHost:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(log_mensage):
        return log_mensage


separator = '------------------------------------'

host = ConnectionHost()
print(host.host)

host.set_user('Levi')
print(host.user)

host.set_password("**************")
print(host.password)

print(separator)

host2 = ConnectionHost.create_with_auth('Vitoria', 277353)
print(host2.host)
print(host2.user)
print(host2.password)

print(separator)

print(ConnectionHost.log('This is a log mensage'))
