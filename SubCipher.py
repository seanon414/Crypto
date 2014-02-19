"""
Assignment 2 Monoalphabetic Subsitution Cipher
"""

plain = 'This is a mathematician named Dr. Gunter Janek. Works at a think tank called the Coolidge Institute. Specializes in large-number theory, prime numbers, factoring.'

temp = 'THEFINALCOUDWXYZBGJKMPQRSV'

def subs(plain, key):
    alpha = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}

    alpha_keys = sorted(alpha)

    plain = plain.upper()

    # Loops through each alpha char and gives the key a value based on the cipher key.
    num = 0
    for k in alpha_keys:
        alpha[k] = key[num]
        num += 1

    # Prints out the plain text given into encrypted text by looking up the value of 
    #  of each char in the alpha dictonary
    for char in plain:
        print (alpha[char], end="") if char.isalpha() else print (char, end='')

subs(plain, temp)

# KLCJ CJ T WTKLIWTKCECTX XTWIF FG. AMXKIG OTXIU. QYGUJ TK T KLCXU KTXU ETDDIF KLI EYYDCFAI CXJKCKMKI. JZIECTDCVIJ CX DTGAI-XMWHIG KLIYGS, ZGCWI XMWHIGJ, NTEKYGCXA.
