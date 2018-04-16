import dataAcq
import cmd

def main():
    print("Enter the name of file in double quotes.")
    fileName = input("Name: ")
    fileName = fileName + ".csv"
    print("\nType of Paradigm (0 = tDCS) (1 = tACS)")
    stimType = float(input("Stimulation Type: "))
    print("\nFrequency of Stimulation in Hz")
    frequency = float(input("Frequency: "))
    print("\nAmount of Current in mA?")
    current = float(input("Current: "))
    print("\nTest Impedance in Ohms")
    impedance = float(input("Impedance: "))
    print("\nNumber of Active Channels")
    numChannels = float(input("Number of Channels: "))
    print("\nTest Duration")
    duration = float(input("Duration: "))
    
    dataAcq.beginAcq(frequency, current, numChannels, impedance, duration, fileName)

main()