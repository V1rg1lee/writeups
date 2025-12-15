# Challenge description

ABC Bank's website has a loan calculator to help its clients calculate the amount they pay if they take a loan from the bank. Unfortunately, they are using an eval function to calculate the loan. Bypassing this will give you Remote Code Execution (RCE). Can you exploit the bank's calculator and read the flag?

# Soluce

This challenge involved exploiting a loan calculator that dangerously used eval() on user input. However, the server implemented a strict blacklist to block common RCE keywords such as os, cat, ls, shell, stdout, and even the use of quotes (" and '). This made traditional payloads unusable. To bypass the restrictions, I leveraged the `__import__()` function to dynamically load the subprocess module and used `getoutput()` to execute shell commands. Since direct command strings were blocked, I constructed them using `chr()` and `bytes()` to avoid literal blacklisted words like "cat" or "ls". By dynamically assembling the string "cat /flag.txt" using character codes, I successfully executed it without triggering the filters. This method worked because the blacklist was based on raw string matching, and did not detect reconstructed values or function calls built at runtime.

So the first step is this:

```python
__import__('subprocess').getoutput(
  ''.join([chr(x) for x in [108,115,32,47]])
)
```

This command will execute `ls /` and return the result. We can see that there is a `flag.txt` file. Then we can read the content of the flag.txt file. We can use the command:

```python
__import__('subprocess').getoutput(
  ''.join([chr(x) for x in [99,97,116,32,47,102,108,97,103,46,116,120,116]])
)
```

The result will be:

```bash
Result: picoCTF{D0nt_Use_Unsecure_f@nctions3ce5e79c}
```

So the flag is `picoCTF{D0nt_Use_Unsecure_f@nctions3ce5e79c}`.