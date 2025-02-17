# Neighbour-rsa-2

20 lines of codes, sure be easy right? Ask your neighbour to tweak a bit.

Author: pikaroot

## Solution
From the given code, we are able to analyse : 

-> a is a random long number

-> p is a long prime number

-> q is relation with a and p , [q = p+a]

-> N = p * q

-> f = q + a - p

Hence, we can try to use f to find the relationship between p,q,a

### Step 1 : Find the Approx (a)
f = q + a - p --(1)

q = next_prime(a+p)

q approx = a + p -- (2)

- Substitute (2) into (1)

f = (a+p) + a - p

f = 2a

a = f//2 --(3)

### Step 2 : Find the Approx (p)
N = p * q --(4)

- Substitute (2) into (4)

N = p * (p + a)

N = (p^2) + (ap)

Factorise the quadratic equation 

![image](https://github.com/user-attachments/assets/09a916e7-81bc-4299-8e5b-7b1be5f639de)

p = [(-a) + isqrt(a^2 + 4N)]//2 --(5)

### Step 3 : Find the Approx (q)
q = N // p

- After identifying the approx value for q, try to use while loop to identidy exact p and q value by <b>N == p*q</b>

### Step 4 : Find the private key and get the long plaintext
<img width="425" alt="image" src="https://github.com/user-attachments/assets/2457e8fe-4ac0-4fdb-9f51-318de5c641f9" />

- You after that convert the long plaintext into byte by using long_to_bytes(plaintext)

Flag : <b>EQCTF{if_y0u_c4nt_find_a_solution_brut3_f0rce_alw4ys_the_k3y}</b>




















