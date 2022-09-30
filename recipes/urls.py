from django.urls import path

from recipes import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<id>/', views.recipe, name="recipe")
]
