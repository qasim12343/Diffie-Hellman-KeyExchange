class Person:

    CK = None
    key = None

    def __init__(self, private_key, g, n):
        self.private_key = private_key
        self.g = g
        self.n = n

    # to send and recieve the combination of private key with g and n
    def sendCK(self):
        return (self.g**self.private_key) % self.n

    def recieveCK(self, ck):
        self.CK = ck
        self.key = (ck**self.private_key) % self.n

    # Encrypt msg and send it
    def sendMsg(self, msg):
        encryptedMsg = ''
        for i in range(len(msg)):
            encrypted_ascii = ord(msg[i]) + self.key
            encryptedMsg = encryptedMsg + chr(encrypted_ascii)
        return encryptedMsg

    # Recieve msg and decrypt it
    def recieveMsg(self, msg):
        decryptedMsg = ''
        for i in range(len(msg)):
            decrypted_ascii = ord(msg[i]) - self.key
            decryptedMsg = decryptedMsg + chr(decrypted_ascii)
        return decryptedMsg


# main
p = int(input())
g = int(input())
p1_private_key = int(input())
p2_private_key = int(input())
msg = input()

# Initiate two person to exchange
p1 = Person(p1_private_key, g, p)
p2 = Person(p2_private_key, g, p)

# Sending and recieving common key
p2.recieveCK(p1.sendCK())
p1.recieveCK(p2.sendCK())

# sending and recieving encrypted and decrypted msg
p1_encryptedMsg = p1.sendMsg(msg)
p2_decryptedMsg = p2.recieveMsg(p1_encryptedMsg)

print(p2.CK)
print(p1.CK)
print(p1_encryptedMsg)
print(p2_decryptedMsg)
