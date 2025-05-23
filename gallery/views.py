from datetime import datetime

from django.http import HttpResponseRedirect

from gallery.forms import ExhibitionForm
from django.shortcuts import render
from gallery.models import *
# Create your views here.
def index(request):
    exhibitions = Exhibition.objects.filter(start_date__gte=datetime.now())
    aws = ArtPiece.objects.all()

    e = []

    for exh in exhibitions:
        a = aws.filter(exhibition=exh)
        e.append((exh, a.first()))

    return render(request, 'index.html', { 'exhibitions': e, 'aws': aws })


def add(request):
    form = ExhibitionForm()

    if request.method == 'POST':
        e_form = ExhibitionForm(request.POST, files=request.FILES)
        if e_form.is_valid():
            e_form.save()
            return HttpResponseRedirect("/index")

    return render(request, 'add.html', {"form": form})
