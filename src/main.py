import dataAcq
import cmd

def main():
    fileName = input("Enter the name of file in double quotes: ")
    fileName = fileName + ".csv"
    duration = input("Enter duration of test in seconds: ")
    numChannels = input("Enter active number of channels: ")
    
    dataAcq.beginAcq(numChannels, duration, fileName)

main()