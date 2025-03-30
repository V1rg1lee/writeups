# Challenge description

I took a few hours to create a simple HTML/CSS previewer system. Since there's no way to add JavaScript then my server should be safe, right?

Grab the flag from the http://chals.swampctf.com:47821/flag.txt file on the server to show that this isn't the case.

The flag is in the standard format. Good luck!

# Soluce

We know where is the flag, we just need to get it. We will open the `console` tab and we will try to read the file with the following code:

```js
await fetch("flag.txt").then(response=>response.text())
```

Then we can see the flag in the console: `swampCTF{c55_qu3r135_n07_j5}`.