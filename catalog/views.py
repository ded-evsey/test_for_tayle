from django.shortcuts import render
from django.views import generic
from catalog.models import Product, Section, Characteristic
# Create your views here.


class SectionsListView(generic.ListView):
    model = Section
    template_name = 'section_list.html'


def section_detail_view(req, id_section):
    model = Product.objects.filter(sections=id_section)
    template_name = 'section_detail.html'
    return render(req, template_name, {'products': model, 'section_id': id_section})


def product_detail_view(req, id_section, id_product):
    model = Product.objects.get(id=id_product)
    template_name = 'product_detail.html'
    for item in model.characteristics.all():
        print(item.name)
    return render(req, template_name, {'product': model, 'section_id': id_section})
