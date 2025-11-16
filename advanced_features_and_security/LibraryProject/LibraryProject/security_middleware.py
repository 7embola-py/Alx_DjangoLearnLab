class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Basic CSP: allow scripts only from your own site
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        return response
