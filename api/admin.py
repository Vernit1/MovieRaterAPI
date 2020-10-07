from django.contrib import admin
from .models import Movie, Rating

admin.site.register(Movie)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display=('movie', 'user', 'stars')
    list_per_page = 10
