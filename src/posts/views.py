from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from posts.models import BlogPost

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts" #permet de spécifier un nom pour la variable que l'on va utiliser en HTML

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated : #si l'utilisateur de notre site est connecté 
            return queryset #retourne donc tous les artices si on est connecté
        return queryset.filter(published=True) #on retourne uniquement les articles publiés si on n'est pas connecté

@method_decorator(login_required, name="dispatch") #dispatch est déjà défini dans CreateView
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ["title", "content",]

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ["title", "content", "published",]

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("posts:home") #l'url à rediriger une fois l'article supprimé