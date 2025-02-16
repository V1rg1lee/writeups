# Challenge description

Our network intern is clearly going through something. Here’s his summer project—a protocol that does nothing but leave you on seen.

Psst... there might be a FLAG hidden in there somewhere. If you can break through the silence. 

The server is hosted at 20.244.40.210 Port : 5002

# Ghosting protocol code

```python
import struct
from enum import IntEnum

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
    

class GhostingPacket:
    """
    Packet structure:
    - version (1 byte)
    - type (1 byte)
    - flags (1 byte)
    - rsv (4 bytes string)
    - payload_length (1 byte)
    - payload (variable length)
    """
    def __init__(self, version=1, packet_type=PacketType.DATA, flags=0, rsv=b'xxxx',payload_length = 0, payload=b''):
        if not isinstance(rsv, bytes) or len(rsv) != 4:
            raise ValueError("RSV must be exactly 4 bytes")
        
        self.version = version
        self.packet_type = packet_type
        self.flags = flags
        self.rsv = rsv
        self.payload = payload
        self.payload_length = len(payload)

    def pack(self):
        """Pack the packet into bytes"""
        if len(self.payload) > 255:
            raise ValueError("Payload too large (max 255 bytes)")
            
        header = struct.pack('!BBB4sB', 
            self.version,
            int(self.packet_type),  
            self.flags,
            self.rsv,
            self.payload_length
        )
        return header + self.payload

    @classmethod
    def unpack(cls, data):
        """Unpack bytes into a packet"""
        if len(data) < 8:
            raise ValueError("Packet too short (minimum 8 bytes)")
            
        
        version, packet_type, flags, rsv, payload_length = struct.unpack('!BBB4sB', data[:8])
        
        if len(data) < 8 + payload_length:
            raise ValueError(f"Packet payload incomplete. Expected {payload_length} bytes")
            
        payload = data[8:8+payload_length]
        
        try:
            packet_type = PacketType(packet_type)
        except ValueError:
            raise ValueError(f"Invalid packet type: {packet_type}")
            
        return cls(version, packet_type, flags, rsv,payload_length, payload)

    def __str__(self):
        """String representation for debugging"""
        flags_str = []
        if self.flags & Flags.DEV: flags_str.append("DEV")
        if self.flags & Flags.SYN: flags_str.append("SYN")
        if self.flags & Flags.ACK: flags_str.append("ACK")
        if self.flags & Flags.ERROR: flags_str.append("ERROR")
        if self.flags & Flags.FIN: flags_str.append("FIN")
        
        return (f"GhostingPacket(version={self.version}, "
                f"type={self.packet_type.name}, "
                f"flags=[{' | '.join(flags_str)}], "
                f"rsv={self.rsv}, "
                f"payload_length={self.payload_length}, "
                f"payload={self.payload})")

    def validate(self):
        
        if self.version != 1:
            raise ValueError("Unsupported version")
            
        if not isinstance(self.packet_type, PacketType):
            raise ValueError("Invalid packet type")
            
        if len(self.rsv) != 4:
            raise ValueError("RSV must be exactly 4 bytes")
            
        if len(self.payload) > 255:
            raise ValueError("Payload too large")
```

# Protocol documentation

## Overview
Just like that person who left your texts on 'seen' for days, the Ghosting Protocol is a custom peer-to-peer messaging protocol that acknowledges received messages with nothing but a cold, emotionless "seen" response. No explanations, no closure, just the void staring back at you. 

## Packet Structure
Each Ghosting Packet consists of the following fields, like the desperate attempts to reach out before the inevitable silence:

| Field           | Size  | Description                                    |
|---------------|------|------------------------------------------------|
| Version       | 1B   | Protocol version (default: 1)                  |
| Type          | 1B   | Packet type (DATA, SEEN, ERROR)                |
| Flags         | 1B   | Control flags (DEV, SYN, ACK, ERROR, FIN, PSH) |
| RSV           | 4B   | Reserved field (default: `xxxx`)               |
| Payload Length | 1B   | Length of the payload (0-255 bytes)            |
| Payload       | Variable | Optional message data                        |

## Packet Types

Because sometimes, the only thing you get back is silence.

| Type  | Value | Description                                      |
|-------|-------|--------------------------------------------------|
| DATA  | 0x01  | Contains actual message data—your heartfelt text.|
| SEEN  | 0x02  | The equivalent of "k." It hurts.                 |
| ERROR | 0x03  | Signals that something went wrong. Like your relationship.|

## Flags
Flags control packet behavior, much like the mixed signals you keep receiving.

| Flag  | Value    | Description                         |
|------|---------|---------------------------------|
| DEV  | 0b10000000 | Developer access flag—because some get special treatment.|
| SYN  | 0b01000000 | Synchronization request to establish connection. No proper handshake, no talk. |
| ACK  | 0b00100000 | Acknowledgment—"Yeah, I got it, whatever."|
| ERROR| 0b00010000 | Signals a mistake, like trusting them.|
| FIN  | 0b00001000 | Indicates termination, as sudden as that last message.|
| PSH  | 0b00000100 | Urges immediate delivery. Too bad they won’t reply.|

## Connection Establishment (Handshake First, Always)
Before you can start sending messages (and getting ignored), you must establish a connection properly. The client must initiate with a **SYN** packet. The server, if willing to acknowledge your existence, will respond with **ACK**. Only after this tragic formality is complete can real communication begin.

Failure to follow this sequence? Well, expect radio silence. Again.

### Handshake Example:
1. **Client:** Sends a packet with `SYN` flag set.
2. **Server:** Replies with `ACK` if it's open to a connection.
3. **Client:** Finally sends actual data (DATA packet).
4. **Server:** Replies with a SEEN packet, leaving you questioning your life choices.

## Implementation

### GhostingPacket Class
The `GhostingPacket` class lets you experience what it's like to be ignored programmatically. 

#### Constructor
```python
GhostingPacket(version=1, packet_type=PacketType.DATA, flags=0, rsv=b'xxxx', payload=b'')
```
- **version**: Protocol version (default: 1)
- **packet_type**: Type of packet (DATA, SEEN, ERROR)
- **flags**: Bitwise flags for control information
- **rsv**: Reserved 4-byte field (default: `xxxx`)
- **payload**: Variable-length message data

#### Methods
- **`pack()`**: Serializes the packet into bytes, like you packing up your dignity.
- **`unpack(data)`**: Deserializes bytes into a `GhostingPacket` object, if only you could unpack the truth.
- **`validate()`**: Ensures compliance with protocol constraints. Unlike people.
- **`__str__()`**: Returns a string representation for debugging your heartbreak.

### Example Usage

#### Sending a Message (Foolishly Hoping for a Reply)
```python
packet = GhostingPacket(packet_type=PacketType.DATA, flags=Flags.DEV, payload=b'Hello?')
packed_data = packet.pack()
print(packed_data)
```

#### Receiving a Response (Or Lack Thereof)
```python
received_packet = GhostingPacket.unpack(packed_data)
print(received_packet)
```

## Error Handling
Because mistakes were made.
- Invalid packet types result in a `ValueError`, just like choosing to text first.
- Payload exceeding 255 bytes throws an exception—much like an overlong paragraph that gets ignored.
- Incorrect `rsv` field length is rejected. Just like you.

## Future Extensions
- Support for encrypted payloads (because some things should remain unsaid).
- Additional handshake mechanisms (but let's be honest, they're not reaching out).
- More sophisticated error handling (like handling rejection with grace).
- To limit the powers of dev and make sure that reserved things stayed reserved.
---
**Author:** A Heartbroken Developer   
**Version:** 1.0  
**Last Updated:** February 2025  

# Soluce

The first trap is that you try to connect the given address via TCP (with netcat for example), but you see that the port is closed. You have to connect in UDP. 

As explained in the protocol, you can send a message and different flags. In the doc they talk about the "DEV" flag, and in the description they say that you have to find the "FLAG", so you have to combine these two pieces of information after passing the handshake for the server to return the flag. 

The program is [here](ghosting_protocol.py)