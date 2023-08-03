from enum import Enum
from django.urls import reverse
import requests
import json
from django.apps import apps
from django.views import View
from .settings import BASE_URL
# class ModulesModel(Enum):
#     CONFIG = ("config", 'config.models.)
#     IO = ("io", "http://localhost:8000/io_module/api/")


# def get_module(key):
#     for module in ModulesModel:
#         if module.name.lower() == key.lower():
#             print(f"Returning {module}")
#             return module.value
#     return None


MODULE_VIEWS_MAP = {
    # "config" : 'config:config-list',
    # "io" : 'io:io-list',
    "config" : 'config:config-list',
    "io" : 'io:io-list',
}

def get_module_view_name(key):
    # module = apps.get_model(key.lower())
    return MODULE_VIEWS_MAP.get(key.lower())

def get_module_url(module):
    print(f"Module received is : {module}")
    view_name = module.split(".")[-1]
    # url = reverse(view_name)
    # return reverse(module[1])
    return view_name

def save_module_step(url, step, user):
    # Submitting the data to the URL
    full_url = BASE_URL + url
    response = requests.post(full_url, data=json.dumps(step), headers={"Content-Type": "application/json"})
    
    if response.status_code > 200 and response.status_code < 300:
        # Successfully submitted the data, retrieve the response
        response_data = response.json()
        # Process the response data as needed
        print(f"Data Saved/Updated : {response.status_code}", response_data)
    else:
        # Failed to submit the data, handle the error
        print(f"Error: {response.status_code}")