# Composition is a specialization of aggregation.
# But in it, when the "parent" object is deleted,
# all references to child objects are also deleted.
class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def insert_address(self, road, number):
        self.addresses.append(Address(road, number))

    def list_address(self):
        for address in self.addresses:
            print(address.road, address.number)

class Address:
    def __init__(self, road, number):
        self.road = road
        self.number = number

client1 = Client('Levi')
client1.insert_address("422", 129)
client1.insert_address("uberlandia", 78)

client1.list_address()
