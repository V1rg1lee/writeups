#!/usr/bin/env python3
import base64

def powershell_a12Vc(b64_str):
    """
    Équivalent de la fonction a12Vc :
    - base64 decode (donne des octets bruts)
    - .GetString(…, UTF-8) (convertit ces octets en une chaîne de caractères)
    """
    raw_bytes = base64.b64decode(b64_str)
    return raw_bytes.decode('utf-8', errors='replace')

def xor_with_two_keys(data, key1_bytes, key2_bytes):
    """XOR chaque octet avec key1 et key2 en boucle."""
    out = bytearray(len(data))
    for i in range(len(data)):
        out[i] = data[i] ^ key1_bytes[i % len(key1_bytes)] ^ key2_bytes[i % len(key2_bytes)]
    return out

def main():
    a53Va = "NXhzR09iakhRaVBBR2R6TGdCRWVJOHUwWVNKcTc2RWl5dWY4d0FSUzdxYnRQNG50UVk1MHlIOGR6S1plQ0FzWg=="
    b64Vb = "n2mmXaWy5pL4kpNWr7bcgEKxMeUx50MJ"

    c56Ve = powershell_a12Vc(a53Va)
    d78Vf = powershell_a12Vc(b64Vb)

    key1_bytes = c56Ve.encode('utf-8')
    key2_bytes = d78Vf.encode('utf-8')

    with open("map.pdf.secured", "r") as f:
        secured_b64 = f.read().strip()

    encrypted_data = base64.b64decode(secured_b64)

    decrypted_data = xor_with_two_keys(encrypted_data, key1_bytes, key2_bytes)

    with open("map_decrypted.pdf", "wb") as f:
        f.write(decrypted_data)

    print("Unciphering done. Check the file type:")
    print("  file map_decrypted.pdf")

if __name__ == "__main__":
    main()
