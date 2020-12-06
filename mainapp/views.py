from django.shortcuts import render
from django.shortcuts import get_object_or_404
from mainapp.models import License
from mainapp.my_func import generator, raspars
from mainapp.forms import LicenseCreationForm, Snippet
from django.contrib import messages

from rest_framework.views import APIView
from .serializers import GetLicenseSerializer, PostLicenseSerializer

from rest_framework.response import Response

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
            messages.success(request, f'{qty} Licences duration {dur} days added.')
            data = License.objects.all().order_by('-idlicense')[:qty]

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

    return render(request, 'mainapp/license_create.html', context)


def update(request):
    if request.method == 'POST':
        form = Snippet(request.POST or None)
        if form.is_valid():
            data = form['body'].value()
            data = raspars(data)
            for key in data.keys():
                obj = get_object_or_404(License, code=key)
            for key, value in data.items():
                change = License.objects.get(code=key)
                now = change.duration
                change.duration = int(now) + int(value)
                change.save()
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
    return render(request, 'mainapp/license_update.html', context)


class LicenseView(APIView):
    def get(self, request):
        licences = License.objects.all()
        serializer = GetLicenseSerializer(licences, many=True)
        return Response({"License": serializer.data})

    def post(self, request):
        license = request.data.get('license')
        # Create a License from the above data
        serializer = PostLicenseSerializer(data=license, many=False) #забраем данные
        if serializer.is_valid(raise_exception=True):
            license_saved = serializer.save()
            resp_license = License.objects.get(code=license_saved.code) #получаем сохраненные данные для обратного вывода
            serializer = GetLicenseSerializer(resp_license, many=False) #выводим даннные обратно
        return Response(serializer.data)



