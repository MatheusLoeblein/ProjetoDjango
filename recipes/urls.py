from django.urls import path

from recipes import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<id>/', views.recipe, name="recipe"),
    path('recipes/search/', views.search, name="search"),

]
