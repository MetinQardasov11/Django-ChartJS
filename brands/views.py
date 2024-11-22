from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Brand

class BrandChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context