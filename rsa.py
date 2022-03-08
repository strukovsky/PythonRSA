from typing import List

from keys import PublicKey, PrivateKey


def encode(key: PublicKey, message: bytearray) -> List[int]:
    encoded = list()
    for byte in message:
        encoded_item = byte ** key.e % key.n
        encoded.append(encoded_item)
    return encoded


def decode(key: PrivateKey, message: bytearray) -> bytearray:
    encoded = bytearray()
    for byte in message:
        encoded_item = byte ** key.d % key.n
        encoded.append(encoded_item)
    return encoded
