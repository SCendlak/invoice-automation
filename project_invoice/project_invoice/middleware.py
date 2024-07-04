from django.shortcuts import redirect


class RedirectIfNotLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path == '/':
            return redirect('login')
        if request.user.is_authenticated and request.path == '/':
            return redirect('invoice:home')
        response = self.get_response(request)
        return response
