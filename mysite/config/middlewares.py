from typing import Any


class ConfigMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Config middleware initialized")
    
    def __call__(self, request, *args: Any, **kwargs: Any) -> Any:
        print(f"Config call pre-view called : {request.__dict__}")
        print(f"Config call user : {request.user}")
        response = self.get_response(request)
        print(f"Response after view : {response}")
        return response
