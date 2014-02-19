"""
Cryto assignment 1
Encrypting and decryting caesar cipher
"""

plain = 'Hello World'
cipher = 'Khoor Zruog'
sky = 'Greetings, Exalted One. Allow me to introduce myself. I am Luke Skywalker, Jedi Knight and friend to Captain Solo.'
gibber = 'L FDQ VHH LW LQ BRXU HBHV BRX KDYH WKH ORRN RI D PDQ ZKR DFFHSWV ZKDW KH VHHV EHFDXVH KH LV HASHFWLQJ WR ZDNH XS LURQLFDOOB WKLV LV QRW IDU IURP WKH WUXWK GR BRX EHOLHYH LQ IDWH QHR'

def builder(plain):
    text = ''
    for char in plain.upper():
        if char.isalpha():
            temp = ord(char) + 3
            if temp > ord('Z'):
                temp -= 26
            blah = chr(temp)
        else:
           blah = char
        text += blah
    return text

      
print (''.join(builder(plain)))
print (''.join(builder(sky)))

def breaker(cipher):
    text = ''
    for char in cipher.upper():
        if char.isalpha():
            temp = ord(char) - 3
            if temp < ord('A'):
                temp += 26
            blah = chr(temp)
        else:
           blah = char
        text += blah
    return text

print (''.join(breaker(cipher)))
print (''.join(breaker(gibber)))
