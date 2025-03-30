# Challenge description

Somewhere on this message-board is a hidden flag. Nothing has worked so far but we have noticed a weird comment in the HTML. Maybe it's a clue?

# Soluce

When we open the `debugger` tab, we can see the following code:

```js
var printFlagSetup = document.getElementById("flagstuff");

[...]

if(printFlagSetup.getAttribute("code") === "G1v3M3Th3Fl@g!!!!"){
        const flag = await getFlag();
        setFlagValue("[flag]: " + flag);
      }
```

So we can change the `code` attribute to `G1v3M3Th3Fl@g!!!!` in the source code.

It will send the flag on the page.

So the flag is `swampCTF{Cr0ss_S1t3_Scr1pt1ng_0r_XSS_c4n_ch4ng3_w3bs1t3s}`.
