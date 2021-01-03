import sys
import os
sys.path.append(os.path.join('pypng-main','code'))
import png
import argparse
import binascii

def stringToBinary(str):
    '''(str) -> str
    >>> stringToBinary("hello world")
    0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100
    >>>stringToBinary("bonjour le monde")
    01100010011011110110111001101010011011110111010101110010001000000110110001100101001000000110110101101111011011100110010001100101
    >>>stringToBinary("hi !!!")
    011010000110100100100000001000010010000100100001
    '''
    return "".join(f"{ord(i):08b}" for i in str)



def binaryToString(string):
    '''(str) -> str
    >>> binaryToString("0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100")
    hello world
    >>>binaryToString("01100010011011110110111001101010011011110111010101110010001000000110110001100101001000000110110101101111011011100110010001100101")
    bonjour le monde
    >>>binaryToString("01101000 01101001 00100000 00100001 00100001 00100001")
    hi !!!
    '''
    out = [(string[i:i+8]) for i in range(0, len(string), 8)] 
    return "".join([chr(int(binary, 2)) for binary in out])




def pngToArray(filepath):
    
    data = png.Reader(filename=filepath).asRGBA8()
    
    width = data[0]
    height = data[1]
    rgbaList = list(data[2])
    
    rgbaArray = []

    for j in rgbaList:
        for color in range (0, len(j)):
            rgbaArray.append(j[color])
    return width, height , rgbaArray




def rgbaPair(array):
    for idx, val in enumerate(array):
        if val % 2 == 1:
            array[idx] = array[idx] - 1
    return array




def arrayToImage(w, h,array, newImage):
    image = png.Writer(w, h, greyscale=False, alpha=True)
    f = open(newImage, 'wb')
    List = arrayToList(w, array)
    image.write(f, List)
    f.close()




def arrayToList(w, array):
    List = [] 
    tmp = []
    reLoop = w * 4
    for j in array:
        tmp.append(j)
        if(len(tmp) == reLoop):
            List.append(tuple(tmp))
            tmp.clear()
    return List




def encode(image, text, newImage):
    w, h, array = pngToArray(image)
    BinText = stringToBinary(text)
    print(BinText)
    array = rgbaPair(array)

    lenTextB = len(BinText)
    lenArray = len(array)

    if lenArray > lenTextB + 8:
        for i in range(lenTextB):
            print(BinText[i])
            array[i] += int(BinText[i])
    else:
        print('text too long !!!!')
        exit()
    arrayToImage(w, h, array, newImage)


def testChar(array, idx):
    for x in range(idx, idx + 8):
        if array[x] % 2 == 1:
            return True
    return False



def getChar(array, idx):
    charBin = ''
    for x in range(idx, idx + 8):
        charBin = charBin + str(array[x] % 2)
    return charBin

def decode(image):
    w, h, array = pngToArray(image)
    BinText = ''
    for i in range(len(array)):
        if i % 8 == 0:
            if testChar(array, i):
                charBin = getChar(array, i)
                BinText = BinText + charBin
                i = i + 9
            else:
                break
    
    print(BinText)

    print(binaryToString(BinText))

encode('image.png', 'salut', 'newImage.png')
decode('newImage.png')