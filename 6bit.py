from PIL import Image

import numpy as np

import random

from scipy.linalg import hadamard

print(hadamard(32))



img = Image.open("Test64.png").crop((500,200,900,350))

img.show()

##img.save("Mariner.jpg")

data = np.array(img)

dataCoded = np.empty([len(data),len(data[0])], dtype = object)


for i in range(len(data)):
    for j in range(len(data[0])):
        
        dataCoded[i][j] = data[i][j]//4

##  Binary list


binList = [[-1],[1]]


for i in range(5):

    binoList = []

    for item in binList:

        binoList.append(item.copy())

    for item in binoList:

        item.append(-1)
        
    for item in binList:

        item.append(1)



    binList = binList + binoList
    
code = {}

for i in range(64):
    
    code[i] = binList[i]
    
## ENCODING

print('encoding')

for i in range(len(data)):
    
    for j in range(len(data[0])):
        
        dataCoded[i][j] = code[dataCoded[i][j]]


print('done encoding')

print('sending through noisy channel')

dataReceived = np.empty([len(data),len(data[0])], dtype = object)


for i in range(len(data)):
    
    for j in range(len(data[0])):

        pixel = []

        for k in range(6):

            if random.randint(1, 100) <= 5:

                pixel.append((-1)*dataCoded[i][j][k])

            else:

                pixel.append(dataCoded[i][j][k])

        dataReceived[i][j] = pixel

print('done sending through noisy channel')

print('decoding')        


dataDecoded = np.empty([len(data),len(data[0])])


for i in range(len(data)):
    
    for j in range(len(data[0])):

        for number in range(64):

            if dataReceived[i][j] == code[number]:

                dataDecoded[i][j] = number*4
                

imgR = Image.fromarray(dataDecoded)

imgR.show()
    
