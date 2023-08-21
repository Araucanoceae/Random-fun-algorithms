from PIL import Image

import numpy as np

import random

from scipy.linalg import hadamard

# Here are H32 and -H32

H = hadamard(32)

mH = np.empty([32,32])

for i in range(32):
    
    for j in range(32):
        
        mH[i][j] = int((-1)*H[i][j])
        

# Here is the code

largeH = np.vstack([H, mH])


code = {}

for i in range(64):
    
    code[i] = largeH[i] 


img = Image.open("Mariner.jpg")

img.show()

data = np.array(img)

for i in range(len(data)):
    
    for j in range(len(data[0])):
        
        data[i][j] = data[i][j]//4
        


## Here is the picture encoded with Hadamard matrix

print("Turning pic matrix into Hadamard code")

dataHad = np.empty([len(data),len(data[0])], dtype = object)


for i in range(len(data)):
    
    for j in range(len(data[0])):
        
        dataHad[i][j] = code[data[i][j]]
print(dataHad)

print("Done turning pic matrix into Hadamard code")

print("Sending info through noisy channel")


dataHadReceived = np.empty([len(data),len(data[0])], dtype = object)


for i in range(len(data)):
    
    for j in range(len(data[0])):

        pixel = []

        for k in range(32):

            if random.randint(1, 100) <= 5:

                pixel.append((-1)*dataHad[i][j][k])

            else:

                pixel.append(dataHad[i][j][k])

        dataHadReceived[i][j] = pixel

##        print(dataHadReceived[i][j] == dataHad[i][j])
        
print("Done sending info through noisy channel")
        
# Here we check for Hadamard distance


print("Decoding")




dataHadCorrected = np.empty([len(data),len(data[0])], dtype = object)

for i in range(len(data)):

##    print(i)

    for j in range(len(data[0])):

        closest = []

        minDist = 32
        
        for number in range(64):

            dist = 0

            match = dataHadReceived[i][j] == code[number]

            for item in match:

                if item == False:

                    dist = dist + 1
                    
##            print(dist)
            
            if dist == minDist:

                closest.append(code[number])

            elif dist < minDist:

                minDist = dist

                closest = [code[number]]

        dataHadCorrected[i][j] = closest[0]



print(dataHadCorrected)

dataHadDec = np.empty([len(data),len(data[0])])


for i in range(len(data)):
    
    for j in range(len(data[0])):

        for entry in code:
            
            check = (code[entry] == dataHadCorrected[i][j]).all()


            if check:

        
                dataHadDec[i][j] = entry*4

print(dataHadDec)
print(data)
imgR = Image.fromarray(dataHadDec)

imgR.show()
##print(dataHad)
