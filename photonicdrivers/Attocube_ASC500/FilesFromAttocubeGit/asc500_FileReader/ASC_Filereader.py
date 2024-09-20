# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 08:27:54 2022

@author: grundch
"""
import os
import numpy as np

def readHeaderFromASCFile(fileLoc):
    """
    Function to extract the header of a .asc file into a dictionary.

    Parameters
    ----------
    fileLoc : str
        Location of the .asc file.

    Returns
    -------
    header : dict
        Extracted header data.

    """
    with open(fileLoc, 'r') as f:
        lineCount = 0
        header = {}
        line = f.readline()
        line = f.readline()
        header['Date'] = line.split('T')[0][2:]
        header['Time'] = line.split('T')[1]
        while lineCount < 11:
            line = f.readline()
            line = line.split(':')
            try:
                header[line[0][2:]] = float(line[1])
            except:
                if 'unit' in line[0][2:]:
                    header[line[0][2:]] = str(line[1][4:-1])
                else:
                    header[line[0][2:]] = str(line[1][3:-1])
            lineCount += 1
        return header

def readDataFromASCFile(fileLoc):
    """
    Function to extract the data from a .asc file into a numpy array.

    Parameters
    ----------
    fileLoc : str
        Location of the .asc file.

    Returns
    -------
    data : array
        Extracted data.

    """
    with open(fileLoc, 'r') as f:
        lineCount = -1
        data = []
        for line in f:
            lineCount += 1
            if lineCount < 14:
                continue
            data.append(float(line[:-1]))
    return np.array(data)


DIR = os.getcwd()
for filename in os.listdir(DIR):
    if filename.endswith(".asc"):
        if 'adc6' in filename and 'fwd' in filename:
            header = readHeaderFromASCFile(filename)
            data = readDataFromASCFile(filename)

# Example for handling 2D data:
data2D = data.reshape(int(header['x-pixels']), int(header['y-pixels']))