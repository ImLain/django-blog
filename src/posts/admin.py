from django.contrib import admin

from posts.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display =("title", "published", "created_on", "last_updated",) #indique ce que l'on veut afficher
    list_editable = ("published", )#pour éditer certains champs dans notre interface

admin.site.register(BlogPost, BlogPostAdmin) #pour indiquer à django que l'on souhaite afficher la classe BlogPost à l'intérieur de notre interface d'administration