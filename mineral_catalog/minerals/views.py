from django.shortcuts import render
from django.utils.safestring import mark_safe

# Create your views here.

from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    fields = [field.name for field in Mineral._meta.get_fields()]
    fields = [e for e in fields if e not in ('id', 'name', 'image_filename',
                                             'image_caption')]
    return render(request, 'minerals/detail.html', {
                  'mineral': mineral,
                  'fields': fields,
                  })