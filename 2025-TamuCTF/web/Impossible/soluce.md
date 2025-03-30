# Challenge description

My friends and I used to play this game all the time as kids! I never managed to win though, can you?

# Soluce

When you open the website, you can open the source code, there is this:

```html
<param name="movie" value="impossible_ctf.swf">
<param name="allowScriptAccess" value="always">
<param name="allowFullScreen" value="true">
<p class="notice">Flash is no longer supported.</p>
```

So I downloaded the `impossible_ctf.swf` file and I opened it with `ffdec` (a Flash decompiler). 

When I looked in the `Images` folder, there is two interesting files:

![alt text](media/image.png)

and

![alt text](media/image-1.png)

So the flag is `gigem{f1v3_m1nu73_b1nw41k}` or `gigem{1m_4_w1nn4r}`.