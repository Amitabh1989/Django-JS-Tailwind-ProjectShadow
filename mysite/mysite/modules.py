from enum import Enum
from django.urls import reverse
import requests
import json

class Modules(Enum):
    CONFIG = ("config", "http://localhost:8000/config/api/")
    IO = ("io", "http://localhost:8000/io_module/api/")


def get_module(key):
    for module in Modules:
        if module.name.lower() == key.lower():
            print(f"Returning {module}")
            return module.value
    return None

def get_url(module):
    print(f"Module received is : {module}")
    # return reverse(module[1])
    return module[1]

def data_request(url, step):
    # Submitting the data to the URL
    response = requests.post(url, data=json.dumps(step), headers={"Content-Type": "application/json"})
    
    if response.status_code > 200 and response.status_code < 300:
        # Successfully submitted the data, retrieve the response
        response_data = response.json()
        # Process the response data as needed
        print(f"Data Saved/Updated : {response.status_code}", response_data)
    else:
        # Failed to submit the data, handle the error
        print(f"Error: {response.status_code}")