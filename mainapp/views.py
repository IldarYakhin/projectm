from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from mainapp.models import License
from mainapp.my_test import generator, raspars
from tkinter import Tk
from mainapp.forms import LicenseCreationForm, Snippet
from django.contrib import messages
from .serializers import LicenseSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LicenseSerializer
# Create your views here.

def index(request):
    context = {'page_title': 'Index page',}
    return render(request, 'mainapp/index.html', context)

def bulk_creation_view(request):
    if request.method == 'POST':
        form = LicenseCreationForm(request.POST or None)
        if form.is_valid():
            qty = int(form['qty'].value())
            dur = int(form['dur'].value())
            # existed = License.objects.all()
            to_input = generator(qty, dur)
            for key, value in to_input.items():
                insert = License(code=key, duration=value)
                insert.save()
            messages.success(request, f'{qty} Licences duration {dur} days added and in your buffer.')
            data = License.objects.all().order_by('-idlicense')[:qty]
            # r = Tk()
            # r.withdraw()
            # r.clipboard_clear()
            # r.clipboard_append(to_input)
            # r.update() # now it stays on the clipboard after the window is closed
            # # r.destroy()

            context = {
                'data': to_input,
                'dur': dur,
            }
            return render(request, 'mainapp/succes.html', context)
    else:
        form = LicenseCreationForm()
    context = {
        'form': form
    }

    return render(request, 'mainapp/licence_create.html', context)

"""
ссылки create update в админку
"""
def update(request):
    if request.method == 'POST':
        form = Snippet(request.POST or None)
        if form.is_valid():
            data = form['body'].value()
            data = raspars(data)
            for key, value in data.items():
                change = License.objects.get(code=key)
                now = change.duration
                print(change)
                change.duration = int(now) + int(value)
                change.save()
                print(change)
            messages.success(request, f'{len(data)} Licences was updated.')
            form = Snippet(request.POST or None)
            context = {
                'form': form,
                'data': data,
            }
        return render(request, 'mainapp/succes.html', context)
    else:
            form = Snippet()
    context = {
        'form': form,
    }
    return render(request, 'mainapp/licence_update.html', context)


class LicenseView(APIView):
    def get(self, request):
        licences = License.objects.all()
        serializer = LicenseSerializer(licences, many=True)
        return Response({"License": serializer.data})

