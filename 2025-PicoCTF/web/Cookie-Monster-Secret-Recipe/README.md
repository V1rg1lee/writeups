# Challenge description

Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?

# Soluce

When we open the website, we can see this cookie in the storage page (`CTRL+SHIFT+I`):

```bash
cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0FDOEZDRDc1fQ%3D%3D
```

We can decode it with `base64` command. We can use the command:

```bash
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ echo "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0FDOEZDRDc1fQ==" | base64 -d                                                                                                                                                
picoCTF{c00k1e_m0nster_l0ves_c00kies_AC8FCD75}
```

So the flag is `picoCTF{c00k1e_m0nster_l0ves_c00kies_AC8FCD75}`.