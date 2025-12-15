import hashlib
import sys

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def md5_hash(s):
    return hashlib.md5(s.encode()).hexdigest()

# Hash for "Dress1"
expected = "4d59a442b89b87717aaf15d08a38a4b1"

# Different concatenation variants to test
def variants(item, qty, secret):
    return [
        item + qty + secret,
        item + secret + qty,
        qty + item + secret,
        secret + item + qty,
        item + ":" + qty + ":" + secret,
        secret + ":" + item + ":" + qty
    ]

if len(sys.argv) < 2:
    print("Usage: {} <path_of_dict>".format(sys.argv[0]))
    sys.exit(1)

dict_path = sys.argv[1]
found = False

print(f"{YELLOW}Searching for the secret for MD5 hash: {expected}{RESET}")
print(f"{GREEN}Using dictionary file: {dict_path}{RESET}")
print("-" * 60)

try:  
   with open(dict_path, "r", encoding="utf-8", errors="ignore") as f:
        for candidate_secret in f:
            candidate_secret = candidate_secret.strip()
            for variant in variants("Dress", "1", candidate_secret):
                if md5_hash(variant) == expected:
                    print(f"{GREEN}Secret found: {candidate_secret}{RESET}")
                    print(f"{GREEN}Concatenation used: {variant}{RESET}")
                    found = True
                    break
            if found:
                break
except FileNotFoundError:
    print(f"{RED}File not found: {dict_path}{RESET}")
    sys.exit(1)

if not found:
    print(f"{RED}No secret found with the current dictionary and these variants.{RESET}")
    sys.exit(1)