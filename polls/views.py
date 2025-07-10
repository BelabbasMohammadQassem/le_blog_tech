from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404, redirect



def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render (request, 'polls/index.html', {'articles' : articles})
    
def article_detail (request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'polls/article_detail.html', {'article' : article})


def about(request):
    return render(request, 'polls/about.html')

def search_articles(request):
    query = request.GET.get('q')
    if query and len(query) >= 3:
        results = Article.objects.filter(title__icontains=query)
        if results.count() == 1:
            return redirect('article_detail', article_id=results.first().id)
        else:
            return render(request, 'polls/search_results.html', {'results': results, 'query': query})
    else:
        # Message d'erreur facultatif
        return render(request, 'polls/search_results.html', {
            'results': [],
            'query': query,
            'error': "Veuillez entrer au moins 3 caractères pour effectuer une recherche."
        })

