from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.db.models import Q

# Create your views here.
import string
from .models import Mineral

groups = ['Silicates', 'Oxides', 'Sulfates', 'Carbonates', 'Halides',
              'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
              'Arsenates', 'Native Elements', 'Other']

alphabet = [x for x in list(string.ascii_uppercase) if
            x not in ['Q', 'Y']]

def mineral_list(request, letter=None):
    if not letter:
        letter = "A"
    minerals = Mineral.objects.filter(name__istartswith=letter).values('id', 'name')
    return render(request, 'minerals/list.html',
                  {'minerals': minerals,
                   'letter': letter,
                   'alphabet': alphabet,
                   'groups': groups,
                   'group_name': None})

def mineral_group_list(request, group_name):
    minerals = Mineral.objects.filter(group__icontains=group_name)
    print('queryset length: ', len(minerals))
    return render(request, 'minerals/list.html',
                  {'minerals': minerals,
                   'letter': 'ZZ',
                   'alphabet': alphabet,
                   'groups': groups,
                   'group_name': group_name})


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    fields = [field.name for field in Mineral._meta.get_fields()]
    fields = [e for e in fields if e not in ('id', 'name', 'image_filename',
                                             'image_caption')]
    return render(request, 'minerals/detail.html', {
                  'mineral': mineral,
                  'fields': fields,
                  'alphabet': alphabet,
                  'letter': 'ZZ',
                  'groups': groups
                  })

def search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(
        Q(name__icontains=term)|
        Q(image_caption__icontains=term)|
        Q(category__icontains=term)|
        Q(formula__icontains=term)|
        Q(strunz_classification__icontains=term)|
        Q(color__icontains=term)|
        Q(crystal_system__icontains=term)|
        Q(unit_cell__icontains=term)|
        Q(crystal_symmetry__icontains=term)|
        Q(cleavage__icontains=term)|
        Q(mohs_scale_hardness__icontains=term)|
        Q(luster__icontains=term)|
        Q(streak__icontains=term)|
        Q(diaphaneity__icontains=term)|
        Q(optical_properties__icontains=term)|
        Q(refractive_index__icontains=term)|
        Q(crystal_habit__icontains=term)|
        Q(specific_gravity__icontains=term)|
        Q(group__icontains=term)
    )
    return render(request, 'minerals/list.html', {
                  'minerals': minerals,
                  'letter': 'ZZ',
                  'alphabet': alphabet,
                  'groups': groups,
                  'group_name': None
                  })
