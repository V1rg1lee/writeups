import binascii

hex_data = """
1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373
1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60
""".replace("\n", "").strip()


cipher_bytes = binascii.unhexlify(hex_data)
known_plaintext = b"ORDER:"
key = bytes([cipher_bytes[i] ^ known_plaintext[i] for i in range(len(known_plaintext))])

decrypted_message = bytes(
    [cipher_bytes[i] ^ key[i % len(key)] for i in range(len(cipher_bytes))]
)

decrypted_message.decode(errors="ignore")
print(decrypted_message)