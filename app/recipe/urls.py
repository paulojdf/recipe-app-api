from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register("tags", views.TagViewSet)
<<<<<<< HEAD
router.register("ingredients", views.IngredientViewSet)
=======
>>>>>>> 6e0d92950f696a7a5584ef73b143bca4f440fdbe

app_name = "recipe"

urlpatterns = [path("", include(router.urls))]
