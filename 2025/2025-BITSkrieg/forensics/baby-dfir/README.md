# Soluce

We have an .ad1 file, i.e. a file containing the image of a disk. 

If we do `strings <file> | grep “flag”`, we see that there's a “flag.txt”.

We'll now extract the files with `binwalk -e <file>`, then open the only .txt file, the flag is in.