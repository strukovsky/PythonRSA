from keys import gen_keys
from rsa import encode, decode

pub, pri = gen_keys(1000)
initial_string = bytearray('Test', encoding='utf-8')
encoded = encode(pub, initial_string)
decoded = decode(pri, encoded)
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
