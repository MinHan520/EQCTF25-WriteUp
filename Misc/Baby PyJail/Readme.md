# Baby PyJail

The author is too lazy to write his own challenges from scratch, so he modified some of the past CTF challenge. See if you can escape the jail!

Flag is at `/flag.txt`

Author: vicevirus

## Solutions

### 1. Converting the .pyc file into .py file

When I see .pyc file which is a low-level-langauge file. 

I can get my python code by decompiling it using <b>uncompyle6</b>

<b>Install uncompyle6</b>

pip install uncompyle6

Type this to decompile the .pyc file into .py file

uncompyle6 -o . babypyjail.pyc

<img width="580" alt="image" src="https://github.com/user-attachments/assets/45d63ed2-cefc-4ec1-9c0a-4312c6fcc07f" />

### 2. Understanding the code
The code mentioned a list of Strings that cannot be input. 

The flag is in answer of the execution python file.

Hence, I need to run the flag.txt file without using the "flag" word.


### 3. Escaping the jail

fn = o.sep + 'fl' + 'ag.txt' 
f = getattr(o, 'o' + 'pen')(fn, 0)  --> f = os.open(./flag.txt, 0) which will read flag.txt with read only access
d = getattr(o, 're' + 'ad')(f, 100)  --> d = os.read(f,100)
getattr(o, 'wr' + 'ite')(2, d)  --> os.write(2,d)
EOF

Rasional : 

<b>f = os.open(./flag.txt, 0)</b> which will open the flag.txt with read only access

<b>d = os.read(f,100)</b> read the file data up to 100 bytes

<b>os.write(2,d)</b> takes the bytes in d and sends them to the standard error stream
