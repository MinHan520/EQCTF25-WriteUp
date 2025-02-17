from gmpy2 import isqrt , next_prime
from Crypto.Util.number import long_to_bytes

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(e, phi_N):
    g, x, y = extended_gcd(e, phi_N)
    if g != 1:
        raise Exception('No modular inverse exists')
    return x % phi_N

N=10986069679740899320769487987259965136338163538313920951921558170716399011131571749355967327929782757252961432250665732844670832757630969990974354211674665217879301194915967815961901955331119097862220567741900953344002421010199387139438258915388299120537312319419560196095221842536034797857570594271497968571543268632342368822758109031157038270115475046299925831141039892806064466450571546834222025788616070408548026473179492912530200671560292851465500255213172920644302815477881129226831758156389887396481079039150256181152083078507883863985140189407376955776873853730599843478872399976242973508423433618152961348309
e=65537
C=2195468989281538327484120144714886786222108443822386213335264431639447179575013802497596322014889540032797783666693430103844035492180467143334243466603968944829680836129211979667061913058333561267630828758422011805278536599370681276716534375047691415305153173304117404635308274845621779917651565487097467077938208235595083835638297185421167329868537607503750906624903899336968072524704962983010525959106240384416922803445710408493786560172567404469778095227805268385869729463091111594408973206573286013513443234182105724723290297083787222131780636442462497223002541517291130831271935451970740180808267897428166746499
f=4203301120017181153512192371191327436380286582036247438379481982220240276670686609670968370331071343886281566516951351186472802979725501149166852576293749655990806367361286991990410689444889766967820170478115967009340001288791419622177173652

#Approcimately find a to assist to identify p and q
a_approx = f//2

# Find approx P
discriminant = pow(a_approx,2) + 4*N
p_approx = (-a_approx + isqrt(discriminant))//2

q_approx = N // p_approx

p = p_approx
while True : 
    q_approx = N // p
    if p*q_approx == N : 
        q = q_approx
        break
    p = next_prime(p)

#Find the private key
phi = (p-1)*(q-1)
d = mod_inverse(e, phi)

plaintext = pow(C, d, N)
print("This is the text : \n", plaintext)
flag = long_to_bytes(plaintext)
print("\n", flag)

