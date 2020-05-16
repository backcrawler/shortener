from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import FormView

import json

from shorting.models import Link
from shorting.forms import LinkForm


def home(request):
    return render(request, 'shorting/test.html', {})


class HomeView(FormView):
    form_class = LinkForm
    #response_class = TemplateResponse

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        context = {'form': self.form}
        return render(request, 'shorting/index.html', context)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        if self.form.is_valid():
            url = self.form.cleaned_data['url']
            qs = Link.objects.filter(url=url)
            if qs.exists():
                link_obj = qs.first()  # if this url already exists
            else:
                link_obj = Link.objects.create(url=url)
                err = link_obj.save()
                if err:  # if save method suddenly returned the string, representing an error, instead of None
                    return render(request, 'shorting/creation_failure.html')
            context = {'form': self.form, 'link': link_obj}
            return render(request, 'shorting/index.html', context)
        else:
            return self.form_invalid(self.form)

    def form_invalid(self, form):
        context = {'form': self.form}
        return render(self.request, 'shorting/index.html', context)


class AjaxHomeView(FormView):
    form_class = LinkForm

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        context = {'form': self.form}
        return render(request, 'shorting/index.html', context)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        if self.form.is_valid():
            url = self.form.cleaned_data['url']
            link_txt = request.POST.get('link')
            qs = Link.objects.filter(url=url, active=True)
            if qs.exists():
                link_obj = qs.first()  # if this url already exists
            else:
                link_obj = Link.objects.create(url=url)
                err = link_obj.save()
                if err:  # if save method suddenly returned the string, representing an error, instead of None
                    return render(request, 'shorting/creation_failure.html')
            response_data = {}
            response_data['result'] = 'Create post successful!'
            response_data['pk'] = link_obj.pk  # TODO: no pk here
            response_data['short_url'] = link_obj.get_short_url()
            response_data['link'] = link_obj.url
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return self.form_invalid(self.form)

    def form_invalid(self, form):
        context = {'form': self.form}
        return render(self.request, 'shorting/index.html', context)


def redirect_view(request, shortcode):
    try:
        link_obj = Link.objects.get(short_url=shortcode)
    except:
        return render(request, 'shorting/wrong_shortcode.html', {'key': shortcode})
    redirect_url = link_obj.url
    return redirect(to=redirect_url)