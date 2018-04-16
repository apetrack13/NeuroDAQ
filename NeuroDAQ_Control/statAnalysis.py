import numpy as np
import csv

def main(frequency):       
    collectedData = parseData()
    shape = np.shape(collectedData)
    numOfRows = shape[0] - 2 
    sortedLeastToGreatest = sortAscending(collectedData, numOfRows)
    minAverage = Average(sortedLeastToGreatest, frequency, numOfRows)
    sortedGreatestToLeast = np.flip(sortedLeastToGreatest, 1)
    maxAverage = Average(sortedGreatestToLeast, frequency, numOfRows)
    results = (maxAverage, minAverage, numOfRows)
    return results

def parseData():
    # Turns csv file into matrix named result.
    reader = csv.reader(open("data.csv", "r"), delimiter=",")
    x = list(reader)
    result = np.array(x).astype("float")
    # Transposes matrix so that columns are now the rows...
    result = np.transpose(result)
    return result
    
def sortAscending(data, numOfRows):
    sortedGreatestToLeast = []
    i = 0
    while i < numOfRows:
        sortedGreatestToLeast.append(data[i])
        i = i + 1
    sortedLeastToGreatest = np.sort(sortedGreatestToLeast)
    return sortedLeastToGreatest

def Average(data, frequency, numOfRows):
    averages = []
    i = 0
    while i < numOfRows:
        j = 0
        selectedValues = []
        while j < frequency/2:
            selectedValues.append(data[i][j])
            j = j + 1
        averages.append(np.mean(selectedValues))
        i = i + 1
    return averages
            
        