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
    print("(%d - %d)mod 26 = "%(shifted,-1*keyOffset),end='')
    shifted += keyOffset
    print("(%d)mod 26 = "%(shifted),end='')
    shifted %= 26
    print("%d = "%(shifted),end='')
    shifted += offset
    print(chr(shifted))
    # shifted = ((ord(x)-offset)+keyOffset)%26 + offset
    return chr(shifted)

# def encrypt(pt,key): #Vigneere
#     ptLen = len(pt)
#     keyLen = len(key)
#     keyIndex = 0
#     ct = ""
#     for ptIndex in range(ptLen):
#         if(pt[ptIndex]==" "):
#             ct+=" "
#             continue
#         ct += shiftChr(pt[ptIndex],key[keyIndex])
#         keyIndex += 1
#         if(keyIndex >= keyLen):
#             keyIndex = 0
#     return ct

def encrypt(pt:str,iKey:str): #Autokey
    key = iKey
    ptLen = len(pt)
    keyLen = len(key)
    keyIndex = 0
    ct = ""
    for ptIndex in range(ptLen):
        if(pt[ptIndex]==" "):
            ct+=" "
            continue
        if(keyIndex == keyLen):
            key = pt.replace(' ','')
            keyIndex=0
            keyLen=-1
        ct += shiftChr(pt[ptIndex],key[keyIndex])
        keyIndex += 1
    return ct

def decrypt(ct,key):
    plusKey = ''
    ctLen = len(ct)
    keyLen = len(key)
    keyIndex = 0
    pt = ""
    for ctIndex in range(ctLen):
        if(ct[ctIndex]==" "):
            pt+=" "
            continue   
        if(keyIndex>=keyLen):
            buffer = shiftChr(ct[ctIndex],plusKey[keyIndex-keyLen],-1)
        else:
            buffer = shiftChr(ct[ctIndex],key[keyIndex],-1)
        plusKey += buffer
        pt += buffer
        keyIndex += 1
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

test()
# main()