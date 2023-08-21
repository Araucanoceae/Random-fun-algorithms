import numpy as np

import random

import string

#Creating all 5-bit words

binList = [[0],[1]]


for i in range(4):

    binoList = []

    for item in binList:

        binoList.append(item.copy())

    for item in binoList:

        item.append(0)
        
    for item in binList:

        item.append(1)
    binList = binList + binoList

#Dictionary of letter to 5-bit

alpha = string.ascii_lowercase

letterToString = {} 

for i in range(26):

    letterToString[alpha[i]] = binList[i]

#LFSR part

initialState = [1,1,0,1,1,0,1,1,1]
j=0
for i in range(200):

    newBit  = initialState[j]^initialState[j+1]^initialState[j+3]^initialState[j+4]^initialState[j+8]

    initialState.append(newBit)

    j = j+1

#Turning message into code
    
phrase = list("cryptographyismyfavouritesubject")
messageEncoded = []

for letter in phrase:

    messageEncoded.append(letterToString[letter])


#quickCheck = []

#for string in messageAsCode:

 #   for letter in letterToString:

  #      if letterToString[letter] == string:

   #         quickCheck.append(letter)

#Encrypt Encoded Message

messageEncrypted = []

i=0
for string in messageEncoded:

    j=0

    currentString = [None,None,None,None,None]

    while j <= 4:

        currentString[j] = string[j]^initialState[i+j]

        j = j + 1

    messageEncrypted.append(currentString)

    i = i + 5    

print(messageEncoded)
print(initialState)
print(messageEncrypted)

   

    
