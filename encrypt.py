# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:04:00 2022

@author: Nehal Kankanawadi
"""

import numpy as np
import cv2

#Checking for prime
def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            return False
    return True

#getting list of factors
def factors(n):
    factors=[]
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors

#Input the message
msg=input("Enter your message: ")


msg=list(msg)

msg_len=len(msg)

#Checking if the length of message is a prime number
#If prime add '`' as last charecter so the image will not be only 1 row
if  isPrime(msg_len):
    msg_len+=1
    msg.append('`')

#Converting all the charecters into respective ASCII values
enc_msg=[ord(N) for N in msg]

#Getting factors
fact=factors(msg_len)

# Finding optimal row count
m=fact[int(len(fact)/2)]

#Optimal column count
n=int(msg_len/m)
print("First Key :",m)
print("Second Key : ",n)

#reshaping the vector to make it look like a 2D image
arr=np.array(enc_msg).reshape(n,m)

#Converting the array to uint8 to be compatable with CV2
arr=np.uint8(arr)

#Resizing to make it look proper
arr=cv2.resize(arr, [500,500],interpolation = cv2.INTER_NEAREST_EXACT)

#Saving the image
print("Image is saved in current location as encrypted_image.png. Please note down the keys as they will be required to decrypt the message")
cv2.imwrite('encrypted_image.png', arr)
cv2.waitKey(0)