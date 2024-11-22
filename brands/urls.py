from django.urls import path
from .views import BrandChartView

app_name = 'brands'

urlpatterns = [
    path('', BrandChartView.as_view(), name='chart'),
]