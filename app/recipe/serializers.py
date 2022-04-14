from rest_framework import serializers

<<<<<<< HEAD
from core.models import Tag, Ingredient
=======
from core.models import Tag
>>>>>>> 6e0d92950f696a7a5584ef73b143bca4f440fdbe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ("id",)
<<<<<<< HEAD


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredient
        fields = ("id", "name")
        read_only_fields = ("id",)
=======
>>>>>>> 6e0d92950f696a7a5584ef73b143bca4f440fdbe
