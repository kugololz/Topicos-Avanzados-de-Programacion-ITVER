import hashlib

h = hash("qwerty".encode())
print(h)
hl = hashlib.md5("qwerty".encode()).hexdigest()
print(hl)
hl2 = hashlib.sha512("qwerty".encode()).hexdigest()
print(hl2)
hl3 = hashlib.sha3_512("qwerty".encode()).hexdigest()
print(hl3)