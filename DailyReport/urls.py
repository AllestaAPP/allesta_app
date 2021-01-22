from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
from .views import csvdownload, tmpsave, default, _base, totalup

urlpatterns = [
    path('',  default, name='index'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('csvdownload/', csvdownload, name='csvdownload'),
    path('tmpsave/', tmpsave, name='tmpsave'),
    # path('default/', default, name='default'),
    path('_base/', _base, name='base'),
    path('registered/',  ItemFilterView.as_view(), name='registered'),
    path('totalup/',  totalup, name='totalup'),
]
