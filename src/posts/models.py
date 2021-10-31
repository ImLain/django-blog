from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse 

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre") #unique à True pour ne pas avoir deux articles avec le même titre / verbose_name : ce sera le nom affiché à plusieurs endroits (dans les formulaires, interface d'administration)
    slug = models.SlugField(max_length=255, unique=True, blank=True) # blank à True permet de laisser ce champ libre
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) #SET_NULL permet de conserver l'article à la suppression de l'auteur et on doit ajouter le paramètre null=True
    last_updated = models.DateTimeField(auto_now=True) #champ qui est automatiquement mis à jour à chaque modification 
    created_on = models.DateField(blank=True, null=True) #permet d'indiquer la date que l'on veut, même si ce n'est pas celle du jour
    published = models.BooleanField(default=False, verbose_name="Publié") #par défaut, il ne sera pas publié
    content = models.TextField(blank=True, verbose_name="Contenu") #pas besoin de mettre null=True puisque c'est du texte
    thumbnail = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        ordering = ["-created_on"] #pour que les derniers articles publiés soient au début 
        verbose_name = "Article"

    def __str__(self):
        return self.title #permet un affichage avec le titre de l'article 

    def save(self, *args, **kwargs):
        if not self.slug : # si on n'a pas spécifié de slug à la modification/création d'un article, on en crée un automatiquement
            self.slug = slugify(self.title) #slugify permet de transformer notre titre en slug. Exemple title = "Harry Potter" / le slug devient "harry-potter"
        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        # if self.author: 
        #     return self.author.username
        # else: 
        #     return "Auteur inconnu"
        return self.author.username if self.author else "Auteur inconnu" #opérateur ternaire

    
    def get_absolute_url(self):
        return reverse("posts:home") #grâce à app_name d'urls, on va pouvoir récupérer notre url
