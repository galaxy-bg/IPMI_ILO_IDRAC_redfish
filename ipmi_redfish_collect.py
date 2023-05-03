import redfish
import sys
import os
import platform
import re
from urllib.parse import urlparse

base_url = sys.argv[1]



def ping_base_url(ip_address):

    parsed_base_url = urlparse(base_url)

    protocol = parsed_base_url.scheme
    ip_address = parsed_base_url.netloc

    ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    if not ip_pattern.match(ip_address):
        print("Error: Invalid IP address")
        return False

    if platform.system().lower() == 'windows':
        response = os.system(f"ping {ip_address} -n 1")
    else:
        response = os.system(f"ping {ip_address} -c 1")

    if response == 0:

        get_info(base_url)

    else:
        print("Error: ", base_url , "is not reachable!")

    return response == 0

def get_info(base_url):
    
    # Set up the Redfish client
    ilorest_client = redfish.redfish_client(base_url=base_url, username="<ilo_user>", password="<my-ILO-Password>")
    ilorest_client.login()
    # Retrieve the server information>
    response = ilorest_client.get("/redfish/v1/Systems/1")

    # Get the Manufactur, Model, Serial Number and Product Id from the response
    manufacturer = response.dict["Manufacturer"]
    model = response.dict["Model"]
    serial_number = response.dict["SerialNumber"]
    product_id = response.dict["SKU"]
    ilorest_client.logout()

    # Print the server information
    print("")
    print("Manufactur       : ", manufacturer)
    print("Model            : ", model)
    print("Serial Number    : ", serial_number)
    print("Product Id       : ", product_id)

ping_base_url(base_url)
