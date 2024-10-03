from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagget_pets')

    @staticmethod
    def get_tagget_pets(obj):
        return ', '.join(str(pet) for pet in obj.tagget.pets.all())
