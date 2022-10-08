# nama Adnan Rafiyansyah Majid
# npm 140810200029
# VIGNERE CIPHER


def shiftChr(x,key,modifier=1):
    offset = 97 if str(x).islower() else 65

    keyOffset = ord(key)
    keyOffset -= (97 if str(x).islower() else 65)
    keyOffset *= modifier

    shifted = ord(x)
    shifted -= offset
    # print("(%d - %d)mod 26 = "%(shifted,-1*keyOffset),end='')
    shifted += keyOffset
    # print("(%d)mod 26 = "%(shifted),end='')
    shifted %= 26
    # print("%d = "%(shifted),end='')
    shifted += offset
    # print(chr(shifted))
    # shifted = ((ord(x)-offset)+keyOffset)%26 + offset
    return chr(shifted)

def encrypt(pt,key): #Vigneere
    ptLen = len(pt)
    keyLen = len(key)
    keyIndex = 0
    ct = ""
    for ptIndex in range(ptLen):
        if(pt[ptIndex]==" "):
            ct+=" "
            continue
        ct += shiftChr(pt[ptIndex],key[keyIndex])
        keyIndex += 1
        if(keyIndex >= keyLen):
            keyIndex = 0
    return ct


def decrypt(ct,key):
    ctLen = len(ct)
    keyLen = len(key)
    keyIndex = 0
    pt = ""
    for ctIndex in range(ctLen):
        if(ct[ctIndex]==" "):
            pt+=" "
            continue
        pt += shiftChr(ct[ctIndex],key[keyIndex],-1)
        keyIndex += 1
        if(keyIndex >= keyLen):
            keyIndex = 0
    return pt


def test():
    pt = "adnan rafiyansyah majid"
    key = "adnan"
    ct = encrypt(pt,key)
    print(ct)
    print(decrypt(ct,key))

def main():
    pt = input("Plain teks : ")
    key = input("Key : ")
    ct = encrypt(pt,key)
    print("Cipher Teks : "+ct)
    print("Deciphered Teks : "+decrypt(ct,key))

# test()
main()