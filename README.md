# Server Information Retrieval Script

This Python script uses the Redfish API to retrieve information about a server, including the manufactur, model, serial number, and product ID. 

## Requirements

To use this script, you need to have Python 3 installed and the `redfish` library. You can install the library using pip:

$ pip3 install redfish

## Usage

To use the script, run the following command in your terminal, replacing `IP_ADDRESS` with the IP address of your server:

$ python server_info.py https://<IPMI/ILO IP address>

NOTE: Make sure to provide the correct username and password for the server in the script. 

The script will first check if the IP address is reachable using the `ping` command. If the IP address is reachable, the script will log in to the server using the Redfish client and retrieve the server information. The script will then print this information to the console.
