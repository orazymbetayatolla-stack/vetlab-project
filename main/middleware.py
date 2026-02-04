from django.utils import translation

class DebugLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(">>> ACTIVE LANGUAGE:", translation.get_language())
        return response
