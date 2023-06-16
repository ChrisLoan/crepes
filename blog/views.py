from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from blog.models import Article
from blog.forms import ContactForm

def date_actuelle(request):
    return render(request, 'blog/date.html', {'dates':
    datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
    <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)
def caca(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon  !</h1>
    <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)
def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    text = "Vous avez demandé l'article #{0} !".format(id_article)
    return HttpResponse(text)
def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos
    articles
    return render(request, 'blog/accueil.html',
    {'derniers_articles':articles})
    
def lire(request, id):
    """ Afficher un article complet """
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/lire.html', {'article': article})



def contact(request):
    if request.method == 'POST': # S'il s'agit d'une requête POST
        form = ContactForm(request.POST) # Nous reprenons les
        if form.is_valid(): # Nous vérifions que les données
        # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']
            envoi = True
    else: # Si ce n'est pas du POST, c'est probablement une requête
        form = ContactForm() # Nous créons un formulaire vide
    return render(request, 'blog/contact.html', locals())

