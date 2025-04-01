# Challenge description

Can you win in a convincing manner against this chess bot? He won't go easy on you!

# Soluce

This challenge involves a chess game where the goal is to beat the bot convincingly. The frontend uses WebSocket to communicate with the backend, sending move evaluations (like eval X for scores or mate Y for checkmate). By analyzing the code, we see the bot relies on Stockfish's evaluation, and the flag is likely sent when the server detects a winning condition. Instead of legitimately checkmating, we found that sending an artificially extreme negative evaluation (eval -100000) tricks the server into thinking the bot is in a hopelessly losing position (equivalent to forced mate), triggering the flag. This was deduced by:

    1. Observing WebSocket message formats (eval/mate),

    2. Testing how the server validates wins (it accepted unrealistic scores),

    3. Exploiting the lack of sanity checks on evaluation thresholds. The key insight was that the server trusted client-submitted evaluations without verifying board state.

So we can use this command to send the message on the console page (`CTRL+SHIFT+I`):

```javascript
sendMessage("eval -100000");
```

Then we can see the flag in the page: `Huh???? How can I be losing this badly... I resign... here's your flag: picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_b820bcc2}`.

So the flag is `picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_b820bcc2}`.