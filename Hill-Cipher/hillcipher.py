#   140810200011 Faiq Muhammad
#   140810200017 M. Keenan Febriansyah
#   140810200021 Rifqi Akmal Fauzi
#   140810200029 Adnan Rafiyansyah Majid
#   140810200031 Ahmad Yahya Salim

#   --- HILL Cipher ---


#>input n
#>input cipher or decipher or key or input
#>if output input save or no
#number size selection
#string plaintext ciphertext
#matrix key invkey cryptbuffer keybuffer

from operator import mod
import numpy as np
import sys

nSize=3

sCipherText = ''
sPlainText = ''
pad = 25

# mKey = np.array([[3,2],[2,9]])
mKey = np.array([[3,4,-1],[2,0,1],[1,3,-2]])

mInvkey = np.zeros(1,dtype=int)

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=np.array(A,dtype=int)
  adj=np.zeros(shape=(n,n),dtype=int)
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(np.linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(np.linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=np.array(A)
  minor=np.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def toc(n):
    n = int(n)
    return chr(mod(n,26)+97) 
def ton(c):
    return ord(c)-97
    
def cipher():
    sCipherText=''
    length = len(sPlainText)
    for i in range(0,length,nSize):
        mCryptbuffer = np.zeros(nSize)
        for j in range(i,i+nSize,1):
            if(j>=length):
                nPlainChr = pad
            else:
                nPlainChr = ton(sPlainText[j])
            mCryptbuffer[j-i]=nPlainChr
        # print(mCryptbuffer)
        mCryptbuffer = np.matmul(mKey,mCryptbuffer)
        # print(mCryptbuffer)
        for j in range(nSize):
            sCipherText += toc(mCryptbuffer[j])
    return (sCipherText)

def decipher():
    sPlainText=''
    length = len(sCipherText)
    for i in range(0,length,nSize):
        mCryptbuffer = np.zeros(nSize)
        for j in range(i,i+nSize,1):

            nCipherChr = ton(sCipherText[j])
            mCryptbuffer[j-i]=nCipherChr
        # print(mCryptbuffer)
        mCryptbuffer = np.matmul(mInvKey,mCryptbuffer)
        # print(mCryptbuffer)
        for j in range(nSize):
            sPlainText += toc(mCryptbuffer[j])
        print(sPlainText)
    return sPlainText[0:length]

def setPlainText(text):
    length = len(text)
    buffer = str(text)
    padCount = nSize-(length%nSize)
    for i in range(padCount):
        buffer += toc(pad)
    if(padCount > 0):
        print('Added '+str(padCount)+' padding(s)')
    global sPlainText
    sPlainText = str(buffer)
    print('New Plain Text set')
    return 1

def setCipherext(text):
    ret = 1
    length = len(text)
    buffer = str(text)
    if(length%nSize!=0):
        print('!!!!!!! - CIPHER TEXT BUKAN KELIPATAN '+str(nSize))
        ret = 2
    global sCipherText
    sCipherText = buffer
    print('New Cipher Text set')
    return ret

def setKey():
    mBuffer = np.zeros((nSize,nSize),dtype=int)
    textBuffer = ''
    nBuffer = ''
    print('Masukkan matriks Key : \n')
    for i in range(nSize):
        for j in range(nSize):
            nBuffer = input("\033[F"+textBuffer)
            mBuffer[i,j] = int(nBuffer)
            textBuffer += nBuffer + ' '
        print()
        textBuffer = ''
    try:
        modMatInv(mBuffer,26)
    except:
        print('Tidak ada Mod inverse nya')
        return 0
    global mKey
    mKey = mBuffer
    return 1

def setSize():
    print()
    select = input('Key akan direset, lanjut ?(y/n)')
    select = select.lower()
    if(select == 'n'):
        return 0
    global nSize
    global mKey
    global mInvKey
    nSize = int(input('New size : '))
    mKey = np.identity(nSize,dtype=int)
    mInvKey = modMatInv(mKey,26)
    print('Size berhasil di set dan key di reset')
    return 1

# nSize = int(input("n = "))
# initMatrices(nSize)
ret = 0
buffer = ''
while(ret != -1):
    mInvKey = modMatInv(mKey,26)
    buffer = ''
    print('--------------------------------------------------------------------------------')
    print('\n[Plaintext]\n'+sPlainText)
    print('\n[Ciphertext]\n'+sCipherText)
    print('\n[Key]')
    print(mKey)
    print('\n[Mod Inverse Key]')
    print(mInvKey)
    print('\n[Menu Selection]')
    print('11.set plaintext')
    print('12.cipher plaintext')
    print('21.set ciphertext')
    print('22.decipher ciphertext')
    print('3.set key')
    print('4.set size')
    print('5.exit')
    selection = int(input('\nPilihan : '))
    if(selection == 11):
        buffer = input('masukkan plain text baru : ')
        ret = setPlainText(buffer)
    elif(selection == 12):
        print('[Chiper Text]')
        buffer = cipher()
        print(buffer)
        saveno = input('save ? (y/n) : ').lower()
        if(saveno == 'y'):
            setCipherext(buffer)
    elif(selection == 21):
        buffer = input('masukkan plain text baru : ')
        ret = setCipherext(buffer)
    elif(selection == 22):
        print('[Dechipered Text]')
        buffer = decipher()
        print(buffer)
        saveno = input('save ? (y/n) : ').lower()
        if(saveno == 'y'):
            setPlainText(buffer)
    elif(selection == 3):
        ret = setKey()
    elif(selection == 4):
        ret = setSize()
    elif(selection == 5):
        sys.exit('PROGRAM DIHENTIKAN OLEH USER')
    input('(tekan enter)')
    
# sCipherText = cipher()
# print(sCipherText)
# print('ddddddddddd')
# print(decipher())
