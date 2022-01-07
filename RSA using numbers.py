"""
------------------------------------------------------RSA Algorithm---------------------------------------------------
                                                 (Rivest–Shamir–Adleman)
RSA algorithm is asymmetric cryptography algorithm.
Asymmetric actually means that it works on two different keys
i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and Private key is kept private.
"""
import math
print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
print("_______________________________________________________\n")


# Prime Function
def prime_check(a):
    if a == 2:
        return True
    elif ((a < 2) or ((a % 2) == 0)):
        return False
    elif (a > 2):
        for i in range(2, a):
            if not (a % i):
                return False
    return True


check_p = prime_check(p)
check_q = prime_check(q)
while (check_p == False) or (check_q == False):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

# RSA Modulus
'''CALCULATION OF RSA MODULUS 'n'.'''
n = p * q
print("RSA Modulus(n) is:", n)

# Eulers Toitent
'''CALCULATION OF EULERS TOITENT 'r'.'''
phi = (p - 1) * (q - 1)
print("Eulers Toitent(phi) is:", phi)
print("_______________________________________________________\n")


def gcd(a, b):
    # Everything divides 0
    if (b == 0):
        return a
    return gcd(b, a % b)


# Function to check and print if
# two numbers are co-prime or not
def coprime(a, b):
    if (gcd(a, b) == 1):
        return a
    else:
        return 0


'''Choose e such than less than phi'''
for i in range(2, phi):
    if (coprime(i, phi)!=0):
        e = coprime(i, phi)
        break
# e=11

def mult_inv(e,phi):
    for i in range(1,1000):
        d=((phi*i)+1)/e
        frac, whole = math.modf(d)
        if(frac==0):
            d=int(d)
            return d


print("The value of e is:", e)
print("_______________________________________________________\n")

d = mult_inv(e, phi)
print("The value of d is:", d)
print("_______________________________________________________\n")
public = (e, n)
private = (d, n)
print("public key :(e,n) ",public)
print("private key :(d,n) ",private)
print("_______________________________________________________\n")

#Encryption
def encrypt(pub_key, i):
    e, n = pub_key
    i=int(i)
    c = (i ** e) % n
    return c

#Decryption
def decrypt(priv_key, i):
    d, n = priv_key
    i=int(i)
    m = (i ** d) % n
    return m

message = input("Would you like to Encrypt or Decrypt?\n(Separate numbers with ',' for decryption):")
print("Your message is:", message)

# Choose Encrypt or Decrypt and Print
choose = input("Type '1' for encryption and '2' for decrytion.")
if (choose == '1'):
    enc_msg = encrypt(public, message)
    print("Your encrypted message is:", enc_msg)
    print("Thank you for using the RSA. Goodbye!")
elif (choose == '2'):
    print("Your decrypted message is:", decrypt(private, message))
    print("Thank you for using the RSA. Goodbye!")
else:
    print("You entered the wrong option.")
    print("Thank you for using the RSA. Goodbye!")
