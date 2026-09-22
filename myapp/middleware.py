class LogRequestMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        # process Before 
        print(f"[Middleware] Request Path {request.path}")
        response = self.get_response(request)
        # Process after view  
        print(f"[Middleware] Response Status: {response.status_code}")
        return response 





# Browser --> MiddlewareStack --> view --> MiddlewareStack --> Response 