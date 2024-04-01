class Person:

    CK = None
    key = None

    def __init__(self, name, private_key, g, n):
        self.name = name
        self.private_key = private_key
        self.g = g
        self.n = n

    # to send and recieve the combination of private key with g and n
    def sendCK(self):
        return (self.g**self.private_key) % self.n

    def recieveCK(self, ck):
        self.CK = (ck**self.private_key) % self.n

    def sendMsg(self, msg):
        pass

    def recieveMsg(self, msg):
        pass


p1 = Person("Amir", 3, 7, 11)
p2 = Person("Reza", 5, 7, 11)

p2.recieveCK(p1.sendCK())
p1.recieveCK(p2.sendCK())

print(p1.CK)
print(p2.CK)
