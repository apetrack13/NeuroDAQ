# NeuroDAQ
<p> The NeuroDAQ is a quality control device for transcranial electrical stimulation (tES) generation devices.
The aim is to improve the outcomes of tES studies by verifying the fidelity of stimulation generation from
tES devices. </p>
<h2>Setting Up the NeuroDAQ</h2>
<p> The NeuroDAQ requires a connection to a local network. </p>

<h3>Setup Wireless Connection</h3>

1.)	Check if micro USB power cable is connected to NeuroDAQ located on the side.

2.)	Remove micro SD card from NeuroDAQ located on the side. 

3.)	Insert micro SD card into adaptor SD card adaptor provided with kit.

4.)	Plug the SD Card adaptor into computer. A new volume should appear in your finder/ file explorer.

5.)	Open the new volume and navigate to the boot directory /Volumes/boot.

6.)	Create a file called wpa_supplicant.conf in this directory and save it.

7.)	Open the file and add the following details:                                                					network={												ssid=”YOUR_NETWORK_NAME”									psk=”YOUR_PASSWORD”									key_mgmt=WPA-PSK

8.)	Eject the SD card and plug it back into the NeuroDAQ.

<h2>Using the NeuroDAQ via Terminal</h2>
<h3>Establish SSH Connection to NeuroDAQ</h3>
<p>
The NeuroDAQ can be controlled via a ssh connection. Once a ssh connection is established, data acquisition can be iniated.
</p>
1.)	First, be sure the micro USB power cable is connected to the NeuroDAQ.

2.)	Open terminal in the applications folder of Mac OS computer.

3.)	Type ssh pi@NeuroDAQ.local and press enter.

4.)	If prompted to answer a yes or no question, type yes and press enter. If not, skip to step 4.

5.)	You will be prompted to enter a password to connect to the device. The password is “GIZMO629” (obviously no quotes).

6.)	You are now connected to the device’s terminal from which you can execute scripts.

<h3>Retrieve Data File</h3>
1.)	In the Mac OS terminal connected to the device, type and enter:					scp pi@NeuroDAQ.local:~/Desktop/DATA_FILE_NAME.csv ~/Desktop		

Replace DATA_FILE_NAME with what you named the data file during data acquisition. 

2.)	The data file will be transferred to the desktop of your Mac OS computer. You now can process this data file with the MATLAB script provided.

<h3>Process Data File with MATLAB</h3>
1.)	Locate the MATLAB script file named “Process_Signal.m”. This script is available at github.com/NeuroModQC-WSU-Design/NeuroDAQ/.

2.)	Place the data file in the same directory as this script.

3.)	Open the script with MATLAB and run.

4.)	You will be prompted to answer questions about the stimulation paradigm recorded. Please, refer to the stimulation paradigm parameters used to record the data file.

5.)	Statistical analysis and graphs of stimulation paradigm will be presented.

