# Challenge description

Hey, my son Timmy made his first website. He said he hid a 'secret' message within different parts of the website... can you find them all? I wanna make sure he isn't saying any swear words online.

The flag is broken up into 3 parts. The parts of the flag should be concatenated in the order they are numbered and then surrounded by the standard wrapper. For example: 'swampCTF{' + part1 + part2 + part3 + '}'

# Soluce

When we open the source code, we can see the first part of the flag in a comment:

```html
<!-- Part 1 of the flag: w3b_ -->
```

Then we can find a suspicious function by CTRL+F in js scripts in the `debugger` tab:

```js
var gs = class e {
  constructor(t) {
    this.cookieService = t;
    let n = 'flagPart2_3',
    r = 'U2FsdGVkX1/oCOrv2BF34XQbx7f34cYJ8aA71tr8cl8=',
    o = 'U2FsdGVkX197aFEtB5VUIBcswkWs4GiFPal6425rsTU=';
    this.cookieService.set(
      'flagPart2',
      $n.AES.decrypt(r, n).toString($n.enc.Utf8),
      {
        expires: 7,
        path: '/',
        secure: !0,
        sameSite: 'Strict'
      }
    );
    let i = new Headers;
    i.set('flagPart3', $n.AES.decrypt(o, n).toString($n.enc.Utf8)),
    fetch('/favicon.ico', {
      headers: i
    })
  }
  date = new Date;
  static ɵfac = function (n) {
    return new (n || e) (Wt(Ti))
  };
  static ɵcmp = si({
    type: e,
    selectors: [
      ['app-root']
    ],
    features: [
      ih([Ti])
    ],
    decls: 4,
    vars: 1,
    template: function (n, r) {
      n & 1 &&
      (
        Mn(0, 'p'),
        ai(1, 'Is it Tuesday?'),
        Tn(),
        hc(2, eE, 2, 0, 'p') (3, tE, 2, 0, 'p')
      ),
      n & 2 &&
      (bf(2), rh(r.date.getDay() == 3 ? 2 : 3))
    },
    styles: [
      'p[_ngcontent-%COMP%]{font-family:Comic Sans MS,cursive,sans-serif;font-size:24px;color:#ff69b4;text-shadow:2px 2px 5px yellow;background:repeating-linear-gradient(45deg,#0ff,#f0f 10%,#ff0 20%);padding:10px;border:5px dashed lime;transform:rotate(-5deg);animation:_ngcontent-%COMP%_wiggle .1s infinite alternate}@keyframes _ngcontent-%COMP%_wiggle{0%{transform:rotate(-5deg)}to{transform:rotate(5deg)}}'
    ]
  })
};
```

We can see that the flag is encrypted with AES. We can decrypt it with the key `flagPart2_3` with the following code: [decrypt.js](code/decrypt.js).

Here is the result: 

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ node decrypt.js                                                                                                                                         
Flag part 2: br0w53r5_4r3_
Flag part 3: c0mpl1c473d
```

So the flag is `swampCTF{w3b_br0w53r5_4r3_c0mpl1c473d}`.
