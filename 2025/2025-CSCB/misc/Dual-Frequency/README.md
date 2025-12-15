# Challenge description

A simple research paper on parabolic antennas… or is it?
Dig deeper, and you may uncover the hidden signal.

# Soluce

We have a pdf file: [challenge.pdf](media/challenge.pdf)

Here is the content of the PDF:

```txt
Parabolic antennas are truly remarkable feats of engineering. Their elegant, dish-like
design isn't just aesthetically pleasing – it's the key to their incredible ability to
capture and focus signals. Think of them as the unsung heroes of modern
communication, silently ensuring we can stream high-definition videos, make crystal-
clear calls, and access the vast expanse of the internet. They're so ubiquitous, yet so
often overlooked, quietly shaping our connected world. It makes you wonder,
though, about the sheer power they wield. Are they *just* conduits for information,
or are they capable of something more? Something... hidden?
These antennas work by harnessing the power of a perfectly shaped curve. The
parabolic surface acts like a mirror for radio waves, collecting them from a wide area
and bouncing them all to a single point – the receiver. This concentration of signal is
what gives parabolic antennas their impressive strength and clarity. It's like focusing
sunlight with a magnifying glass, only instead of light, it's radio waves. And just like
a magnifying glass can start a fire, the focused power of these antennas raises
questions. What other information, what other signals, are being amplified and
directed? What secrets are being carried on those concentrated waves? Perhaps even
something like CSC{D0N7_ a message we're not meant to intercept.
But here's a little secret, and it's a secret that applies to all forms of communication:
signals can be sneaky. Sometimes, a strong signal might overpower a weaker one,
effectively hiding it in plain sight. It's like trying to hear a whisper in a crowded room
– the louder voices drown it out. This is where the precision engineering of a
parabolic antenna really shines. Beyond simply amplifying a signal, they can be fine-
tuned to discriminate between different frequencies, picking up even the faintest of
whispers, the most subtle of signals. They can isolate the quiet voices in the digital
crowd, potentially revealing hidden layers of information.
So, the next time you're enjoying your favorite online content, take a moment to
appreciate the parabolic antenna. It's a testament to human ingenuity, quietly working
to bring us closer together. But also, perhaps, a reminder that in the world of signals,
there's always more than meets the eye. There are always hidden messages, masked
frequencies, and secrets waiting to be uncovered. And maybe, just maybe, the
parabolic antenna is the key to unlocking some of them.
```

The text is a bit weird, and we can see that there is a flag hidden in the text: `CSC{D0N7_`. This is the first part of the flag. 

My first idea is to check the type of the file, to be sure that it is a PDF file. 

```sh
┌──(virgile㉿localhost)-[~/Téléchargements/CSCB]
└─$ file challenge.pdf                                                                                                                                      
challenge.pdf: data
```

The file is not a PDF file, but a binary file. It's a bit weird, because when we open it, we can see the content of the PDF. So let's check the content of the file by opening it with Visual Studio Code. 

We can see that in the beginning of the file:

```html
<div id='mypage'>
<h1>HTML page</h1>
<script language=javascript type="text/javascript">
document.documentElement.innerHTML =
document.getElementById('mypage').innerHTML;
document.title = 'HTML title';
alert("P0LY6L0T}");
console.log("P0LY6L0T}");
</script>
</div>
```

We can see the last part of the flag: `P0LY6L0T}`.

This gives us an hint: polyglot. This is a polyglot file, a file that can be interpreted in multiple ways. To be sure, I replace the extension of the file by `.html` and open it in a web browser. It works: [challenge.html](media/challenge.html).

So, after some tests with different extensions, I find that the file is a polyglot PDF/HTML/PNG: [challenge.png](media/challenge.png).

When we open the file, if we zoom on the antenna, we can see a part of the flag: 

![alt text](image.png)

The second part of the flag is: `YOU_1IK3`.

So the final flag is `CSC{D0N7_YOU_1IK3_P0LY6L0T}`.