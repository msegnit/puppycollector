from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('puppies/', views.puppies_index, name='index'),
  path('puppies/<int:puppy_id>/', views.puppy_detail, name='detail'),
  path('puppies/create/', views.PuppyCreate.as_view(), name='puppies_create'),
  path('puppies/<int:pk>/update/', views.PuppyUpdate.as_view(), name='puppies_update'),
  path('puppies/<int:pk>/delete/', views.PuppyDelete.as_view(), name='puppies_delete'),
  path('puppies/<int:puppy_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('puppies/<int:puppy_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('puppies/<int:puppy_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]