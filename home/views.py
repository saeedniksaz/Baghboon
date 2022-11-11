from django.shortcuts import render
from django.views import View


class Home(View):
    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers['host'] = 'localhost'
        response.headers['user'] = request.user
        return response

    def get(self, request):
        return render(request, 'home/home.html')