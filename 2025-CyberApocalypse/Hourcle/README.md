# Challenge description

A powerful enchantment meant to obscure has been carelessly repurposed, revealing more than it conceals. A fool sought security, yet created an opening for those who dare to peer beyond the illusion. Can you exploit the very spell meant to guard its secrets and twist it to your will?

# Soluce

Here is the code of the challenge:

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os, string, random, re

KEY = os.urandom(32)

password = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])

def encrypt_creds(user):
    padded = pad((user + password).encode(), 16)
    IV = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv=IV)
    ciphertext = cipher.decrypt(padded)
    return ciphertext

def admin_login(pwd):
    return pwd == password


def show_menu():
    return input('''
=========================================
||                                     ||
||   🏰 Eldoria's Shadow Keep 🏰       ||
||                                     ||
||  [1] Seal Your Name in the Archives ||
||  [2] Enter the Forbidden Sanctum    ||
||  [3] Depart from the Realm          ||
||                                     ||
=========================================

Choose your path, traveler :: ''')

def main():
    while True:
        ch = show_menu()
        print()
        if ch == '1':
            username = input('[+] Speak thy name, so it may be sealed in the archives :: ')
            pattern = re.compile(r"^\w{16,}$")
            if not pattern.match(username):
                print('[-] The ancient scribes only accept proper names-no forbidden symbols allowed.')
                continue
            encrypted_creds = encrypt_creds(username)
            print(f'[+] Thy credentials have been sealed in the encrypted scrolls: {encrypted_creds.hex()}')
        elif ch == '2':
            pwd = input('[+] Whisper the sacred incantation to enter the Forbidden Sanctum :: ')
            if admin_login(pwd):
                print(f"[+] The gates open before you, Keeper of Secrets! {open('flag.txt').read()}")
                exit()
            else:
                print('[-] You salt not pass!')
        elif ch == '3':
            print('[+] Thou turnest away from the shadows and fade into the mist...')
            exit()
        else:
            print('[-] The oracle does not understand thy words.')

if __name__ == '__main__':
    main()
```

The vulnerability is in the encrypt_creds function. The function is intended to encrypt the user's credentials, but it mistakenly uses the decrypt() method instead of encrypt() from the AES object.

The code uses AES in CBC mode, and applies PKCS7 padding to the input (user + password) before passing it to decrypt(). However, the decrypt() function expects ciphertext, not plaintext. By applying decryption on a padded plaintext, the function exposes the internal behavior of the AES decryption process.

This essentially gives us a decryption oracle that reveals D_k(B_0) || D_k(B_1) || ..., where D_k is the AES decryption with the secret key k, and B_i are the 16-byte blocks of user + password + padding.

To exploit this, we use a classic byte-at-a-time attack:

    - We craft a username that aligns a specific byte of the unknown password at the end of a block.

    - We record the AES decrypt() output for that block.

    - Then we try appending all possible characters (a-zA-Z0-9) at the target position until we reproduce the same decrypted block.

    - When we find a match, we've discovered the correct character.

    - We repeat this process 20 times to recover the full password.

It is critical to keep the same TCP connection open during the entire attack because the password and key are randomly generated only once per process. A new connection would give a different password.

Once the password is recovered, we can access the second menu option and retrieve the flag.

Here is the exploit code: [hourcle.py](code/hourcle.py)

When you run the exploit code on the website, you will see this:

```sh
┌──(env)(virgile㉿localhost)-[~/Documents]
└─$ python hourcle.py 94.237.58.78 48642
[+] Connecting to 94.237.58.78:48642...
[+] Connected.
[+] Password: Rjzvn8DJNefc3wYE1KpQ
[+] Final password: Rjzvn8DJNefc3wYE1KpQ
[+] Server response:

 to enter the Forbidden Sanctum :: [+] The gates open before you, Keeper of Secrets! HTB{encrypting_with_CBC_decryption_is_as_insecure_as_ECB___they_also_both_fail_the_penguin_test_c6fd43206a0182cb8f290115e1bba936}
```

So the flag is `HTB{encrypting_with_CBC_decryption_is_as_insecure_as_ECB___they_also_both_fail_the_penguin_test_c6fd43206a0182cb8f290115e1bba936}`.