from __future__ import print_function
# Create your views here.
import os

from django.shortcuts import render
from django.views.generic import TemplateView

from project.settings import BASE_DIR


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class ServiceWorkerView(TemplateView):
    def get(self, request, *args, **kwargs):
        service_url = os.path.join(BASE_DIR, 'templates/firebase-messaging-sw.js')
        return render(request, service_url, content_type="application/x-javascript")