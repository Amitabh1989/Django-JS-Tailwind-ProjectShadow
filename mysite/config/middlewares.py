from typing import Any
import json

# Not used currently

class ConfigMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Config middleware initialized")
    
    def __call__(self, request, *args: Any, **kwargs: Any) -> Any:
        print(f"Config call pre-view called : {request.__dict__}") 
        print(f"Config call pre-view POST : {request.body}")
        print(f"Config call pre-view POST : {request.POST}")
        print(f"Config call pre-view USER : {request.user}")
        print(f"Config call pre-view META : {request.META}")
        print(f"Config call pre-view ARGS : {args}")
        print(f"Config call pre-view KWARGS : {kwargs}")
        # json_data = json.loads(request.body.decode('utf-8'))
        # print(f"JSON data = {json_data}")
        # request.user = json_data["user"]
        # print(f"Config call user : {request.POST['user']}")
        response = self.get_response(request)
        print(f"Response after view : {response}\n\n\n=====================\n\n")
        return response
