# Neighbor-RSA 
My neighbour has similar wealth with me, maybe a 5000 times richer than me??

Author: pikaroot
## Notes for RSA
p , q = large prime number

n = p * q

e = 3,5,17,65537

r = (p-1)(q-1)

d = inverse(e) * mod(r)

Public Key = (e,n) / Private Key = (d)

Encryption = pow(m,e,n)
Decryption = pow(c,d,n)

## Solutions
### Analysis
From the given code, we can understand

-> The given flag is encrypted at line 18 using <b>C = pow(bytes_to_long(flag),e,n)</b>

-> Info given C [encrypted flag], (e,n) [public key] , P/Q [prime numbers] are not given 

-> We has to find the private key (d) 

### 1. Find the prime numbers by factorising 
Implementing the <b>factorint</b> libraries 

![image](https://github.com/user-attachments/assets/81fa98c5-8de9-41d3-9c06-beb4214b0948)

You will be getting 2 long prime numbers 

![image](https://github.com/user-attachments/assets/a4b1f5df-064a-45b7-aafb-535cdb32dac1)

### 2. Find the private key
using <b>
r = (p-1)(q-1)

d = mod_inverse(e, r)
</b>

![image](https://github.com/user-attachments/assets/354017c0-ff91-4e94-a1c7-f9ae650695a9)

### 3. Decrypt the plaintext into bytes
You will receive a long number, hence convert the long into bytes

<b>from Crypto.Util.number import long_to_bytes</b>

![image](https://github.com/user-attachments/assets/c694e83b-135b-43f2-b010-d48a0c676318)


### Output 
Plain Text : 10668929487112715015386141655863628827435466429705069713350312606858982395048045960372953266097502354984793049997693
Flag : <b>b'EQCTF{cla554ic_ferm4t_fact0rization_ch4llenge!!}'</b>
