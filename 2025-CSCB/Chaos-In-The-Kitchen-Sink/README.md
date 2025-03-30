# Challenge description

Imagine diving into a kitchen sink that's a chaotic wonderland of dirty dishes, rogue utensils, and mysterious leftovers.
Your mission? To find a hidden flag amidst this culinary catastrophe.
It's like playing hide-and-seek with a ninja spoon!
In this scenario, CHAOS is not just a state—it's a class !
To make your search easier, use the DNS (Domain Name System) protocol.
Just as DNS helps you find the exact address of a website among billions of possibilities, it will guide you to locate the flag in this mess.
Ready to tackle the CHAOS class and find that elusive flag in the SINK (DNS TYPE 40) ?

Let's get scrubbing and let DNS lead the way!

Start with the following info:
- domain name : dishes.be
- hints : hints.dishes.be
- server IP address : See below

The server is listening on
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053

# Soluce

We will begin by accessing hints:

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hints.dishes.be TXT


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hints.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44623
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hints.dishes.be.               IN      TXT

;; ANSWER SECTION:
hints.dishes.be.        300     IN      TXT     "follow the DNS hint{1..7}.dishes.be"

;; Query time: 36 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:08:18 EDT 2025
;; MSG SIZE  rcvd: 81
```

We can see that we need to follow the DNS hints from 1 to 7.

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint1.dishes.be TXT
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint2.dishes.be TXT
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint3.dishes.be TXT
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint4.dishes.be TXT
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint5.dishes.be TXT
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint6.dishes.be TXT
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint7.dishes.be TXT


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint1.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54665
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hint1.dishes.be.               IN      TXT

;; ANSWER SECTION:
hint1.dishes.be.        300     IN      TXT     "https://datatracker.ietf.org/doc/html/draft-eastlake-kitchen-sink-02"

;; Query time: 32 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:09:34 EDT 2025
;; MSG SIZE  rcvd: 114


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint2.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52764
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hint2.dishes.be.               IN      TXT

;; ANSWER SECTION:
hint2.dishes.be.        300     IN      TXT     "DNS query for the DNS server <IP address>"

;; Query time: 36 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:09:34 EDT 2025
;; MSG SIZE  rcvd: 87


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint3.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 58814
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hint3.dishes.be.               IN      TXT

;; ANSWER SECTION:
hint3.dishes.be.        300     IN      TXT     "DNS query for the DNS server port 5053"

;; Query time: 36 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:09:34 EDT 2025
;; MSG SIZE  rcvd: 84


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint4.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 36424
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hint4.dishes.be.               IN      TXT

;; ANSWER SECTION:
hint4.dishes.be.        300     IN      TXT     "DNS query for the domain dishes.be"

;; Query time: 36 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:09:34 EDT 2025
;; MSG SIZE  rcvd: 80


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint5.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 46807
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hint5.dishes.be.               IN      TXT

;; ANSWER SECTION:
hint5.dishes.be.        300     IN      TXT     "DNS query for the record dirty.dishes.be"

;; Query time: 32 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:09:34 EDT 2025
;; MSG SIZE  rcvd: 86


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint6.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 18003
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hint6.dishes.be.               IN      TXT

;; ANSWER SECTION:
hint6.dishes.be.        300     IN      TXT     "DNS query for the CHAOS class"

;; Query time: 28 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:09:34 EDT 2025
;; MSG SIZE  rcvd: 75


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 hint7.dishes.be TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28196
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hint7.dishes.be.               IN      TXT

;; ANSWER SECTION:
hint7.dishes.be.        300     IN      TXT     "DNS query for the SINK record type"

;; Query time: 32 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:09:34 EDT 2025
;; MSG SIZE  rcvd: 80
```

So here is a table of the hints:

| Hint | Content |
|------|---------|
| hint1.dishes.be | [https://datatracker.ietf.org/doc/html/draft-eastlake-kitchen-sink-02](https://datatracker.ietf.org/doc/html/draft-eastlake-kitchen-sink-02) |
| hint2.dishes.be | DNS query for the DNS server <IP address> |
| hint3.dishes.be | DNS query for the DNS server port 5053 |
| hint4.dishes.be | DNS query for the domain dishes.be |
| hint5.dishes.be | DNS query for the record dirty.dishes.be |
| hint6.dishes.be | DNS query for the CHAOS class |
| hint7.dishes.be | DNS query for the SINK record type |

We will do this, according to hints:

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 dirty.dishes.be TYPE40 -c CH


; <<>> DiG 9.20.2-1-Debian <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 dirty.dishes.be TYPE40 -c CH
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 420
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;dirty.dishes.be.               CH      SINK

;; ANSWER SECTION:
dirty.dishes.be.        300     CH      SINK    40 0 0 Q1NDe05vTW9yZURpcnR5RGlzaGVzSW5UaGVLaXRjaGVuU0lOS30=

;; Query time: 40 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 07:10:24 EDT 2025
;; MSG SIZE  rcvd: 86
```

We can see that there is a base64 encoded string. We will decode it:

```sh
echo 'Q1NDe05vTW9yZURpcnR5RGlzaGVzSW5UaGVLaXRjaGVuU0lOS30=' | base64 -d
```

So the flag is `CSC{NoMoreDirtyDishesInTheKitchenSINK}`.