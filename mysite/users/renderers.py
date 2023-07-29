from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        print(f"Rendered Data : {data}")

        # ErrorDetail string comes in serializer.errors if any

        if 'ErrorDetail' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps(data)
        
        # return response 
        return response.encode(self.charset)