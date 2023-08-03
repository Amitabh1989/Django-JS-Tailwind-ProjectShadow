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


# MODULE_VIEWS_MAP = {
#     # "config" : 'config:config-list',
#     # "io" : 'io:io-list',
#     "config" : 'config:config-list',
#     "io" : 'io:io-list',
# }

# def get_module_view_name(key):
#     # module = apps.get_model(key.lower())
#     return MODULE_VIEWS_MAP.get(key.lower())

# def get_module_url(module):
#     print(f"Module received is : {module}")
#     view_name = module.split(".")[-1]
#     # url = reverse(view_name)
#     # return reverse(module[1])
#     return view_name

# def user_to_dict(user):
#     return {
#         'email': user.email,
#         'name': user.name
#         # 'username': user.username,
#         # Add more relevant user information if needed
#     }

# # from django.contrib.auth.decorators import login_required

# # @login_required
# def save_module_step(url, step, request):
#     # Submitting the data to the URL
#     full_url = BASE_URL + url
#     # step["user"] = user_to_dict(request.user) #request.user #'root@root.com' #user_to_dict(request.user)
#     # print(f'Step user is : {step["user"]}')
#     headers = {
#         "Content-Type": "application/json",
#         "user": request.user.email,  # or any other relevant user information
#     }
#     response = requests.post(full_url, data=json.dumps(step), headers={"Content-Type": "application/json"})
#     # response = requests.post(full_url, data=json.dumps(step), headers={"Content-Type": "application/json"}, params={"user": request.user})
#     # response = requests.post(full_url, data=json.dumps(step), headers=headers)
    
#     if response.status_code > 200 and response.status_code < 300:
#         # Successfully submitted the data, retrieve the response
#         print(f"Response : {response}")
#         # response_data = response.json()
#         # Process the response data as needed
#         print(f"Data Saved/Updated : {response.status_code}") #, response_data)
#     else:
#         # Failed to submit the data, handle the error
#         print(f"Error: {response.status_code}")




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


def save_module_step(url, step, request):
    # Submitting the data to the URL
    full_url = BASE_URL + url
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer {request.user.token}"  # Assuming the user has an authentication token
        # "Cookie": f"sessionid={request.COOKIES.get('sessionid', '')}"
    }
    response = requests.post(full_url, data=json.dumps(step), headers=headers)
    
    if response.status_code > 200 and response.status_code < 300:
        # Successfully submitted the data, retrieve the response
        print(f"Response : {response}")
        # Process the response data as needed
        print(f"Data Saved/Updated : {response.status_code}") #, response_data)
    else:
        # Failed to submit the data, handle the error
        print(f"Error: {response.status_code}")

