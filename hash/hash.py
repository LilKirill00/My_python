import hashlib

# Захешировать сообщение

input_hash = input('Input text: ')

hash_obj = hashlib.md5(input_hash.encode())
print("Hash:", hash_obj.hexdigest())
