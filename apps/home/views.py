# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from apps.bot.models import LandLord


@login_required(login_url="/login/")
def index(request):
    latest_question_list = LandLord.objects.all
    context = {'segment': 'index','data':latest_question_list}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def order(request):
    shop = request.user.employee.shop
    company = request.user.employee.company
    print(shop)
    orders = OrderTable.objects.filter(shop_id=shop,company_id=company)
    context = {'orders':orders}
    html_template = loader.get_template('home/ui-tables.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def landlord_detail(request,landlord_id):
    landlord = LandLord.objects.get(pk=landlord_id)
    context = {'landlord':landlord}
    html_template = loader.get_template('home/order-detail.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
