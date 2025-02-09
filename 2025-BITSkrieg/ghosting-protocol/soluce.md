# Soluce

The first trap is that you try to connect the given address via TCP (with netcat for example), but you see that the port is closed. You have to connect in UDP. 

As explained in the protocol, you can send a message and different flags. In the doc they talk about the "DEV" flag, and in the description they say that you have to find the "FLAG", so you have to combine these two pieces of information after passing the handshake for the server to return the flag. 

The program is in./ghosting_protocol.py