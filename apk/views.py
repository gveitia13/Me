from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from apk.models import Clothing


def Index(request):
    return redirect('/admin')


# @csrf_exempt
# def wash(request):
#     if 'wash' in request.POST:
#         print(request)


class Test(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'wash':

                print(request)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
