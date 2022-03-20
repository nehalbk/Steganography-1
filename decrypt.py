# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:58:47 2022

@author: Nehal Kankanawadi
"""

import cv2

msg=[]

print("Please place the encrypted image in current location as of this file with the name encrypted_image.png")

#Input of Keys
m=int(input("Enter first key : "))

n=int(input("Enter second key : "))

msg_len=int(input("Enter third key : "))

#Reading the image
x=cv2.imread('encrypted_image.png')

#Resizing to inital size
x=cv2.resize(x,[m,n])

#Converting ASCII value to chaareter
for i in x:
    for j in i:
        msg.append(chr(int(j[0])-msg_len))

#Converting list to string
msg=''.join(msg)

print("\nYour scecret message :")
print(msg)
