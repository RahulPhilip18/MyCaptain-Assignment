# -*- coding: utf-8 -*-
"""
Created on Thu May  5 13:05:31 2022

@author: rahul
"""

#write a Python program to accept a filename from the user and print the
#extension of that

filename = input('Enter file name: ')
extension = filename.split('.')
print('The extension of file: ',extension)