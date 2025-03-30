import string
from pwn import *
import sys
import time

context.log_level = 'error'

charset = string.ascii_letters + string.digits
BLOCK_SIZE = 16
PASSWORD_LEN = 20

def get_decrypt_output(r, user_input: str) -> bytes:
    r.sendline(b'')
    r.recvuntil(b'Choose your path')
    r.sendline(b'1')
    r.recvuntil(b'archives :: ')
    r.sendline(user_input.encode())
    line = r.recvline(timeout=2)
    if b'encrypted scrolls' not in line:
        raise ValueError(f'Unexpected response: {line}')
    return bytes.fromhex(line.decode().split(': ')[-1].strip())

def recover_password(host, port):
    password = bytearray()
    print(f'[+] Connecting to {host}:{port}...')
    r = remote(host, int(port))
    r.sendline(b'')
    r.recvuntil(b'Choose your path')
    print('[+] Connected.')

    for i in range(PASSWORD_LEN):
        block_index = (BLOCK_SIZE + i) // BLOCK_SIZE
        user_prefix = 'X' * 16
        pad_len = BLOCK_SIZE - (i % BLOCK_SIZE) - 1
        controlled_pad = 'A' * pad_len
        prefix = user_prefix + controlled_pad

        ref = get_decrypt_output(r, prefix)
        ref_block = ref[block_index * BLOCK_SIZE : (block_index + 1) * BLOCK_SIZE]

        found = False
        for c in charset:
            attempt = prefix + password.decode() + c
            out = get_decrypt_output(r, attempt)
            guess_block = out[block_index * BLOCK_SIZE : (block_index + 1) * BLOCK_SIZE]

            current_guess = password.decode() + c + "_" * (PASSWORD_LEN - len(password) - 1)
            sys.stdout.write(f"\r[+] Password: {current_guess}")
            sys.stdout.flush()

            if guess_block == ref_block:
                password.append(ord(c))
                current_done = password.decode() + "_" * (PASSWORD_LEN - len(password))
                sys.stdout.write(f"\r[+] Password: {current_done}")
                sys.stdout.flush()
                found = True
                break

        if not found:
            print(f"\n[-] Could not find byte {i+1:02}, stopping.")
            break

    print(f"\n[+] Final password: {password.decode()}")

    r.recvuntil(b'Choose your path')
    r.sendline(b'2')
    r.recvuntil(b'incantation')
    r.sendline(password)
    try:
        resp = r.recvall(timeout=3).decode()
        print("[+] Server response:\n")
        print(resp)
    except EOFError:
        print("[-] Connection closed unexpectedly.")
    r.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    recover_password(host, port)
