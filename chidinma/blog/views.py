from django.shortcuts import render_to_response
from blog.models import Article, Bio, Comment
from django.http import HttpResponseRedirect
from blog.forms import ArticleForm, CommentForm
from django.core.context_processors import csrf

def index(request):
	name = "Chidnma Mong"
	return render_to_response('index.html', {'name': name, 'bio': Bio.objects.get(id = 1)})

def all_articles(request):
	return render_to_response('all.html', {'articles': Article.objects.all()})

def get_article(request, article_id):
	c = {}
	c.update(csrf(request))
	c['form'] = CommentForm
	c['article'] = Article.objects.get(id = article_id)
	a = Article.objects.get(id = article_id)
	c['comment'] = Comment.objects.filter(article = a).order_by('-pub_date')
	return render_to_response('get_article.html', c)

def create(request):
	if request.method == "POST":
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/all')
	c = {}
	c.update(csrf(request))
	c['form'] = ArticleForm()
	return render_to_response('create.html', c)


def like(request,article_id):
	if article_id:
		element = Article.objects.get(id = article_id)
		c = element.likes
		element.likes = c + 1
		element.save()
		return HttpResponseRedirect('/get/%s/' % article_id)

	#if an invalid number is passed in, just render the page again.
	return HttpResponseRedirect('/all/')

def comment(request, article_id):
	a = Article.objects.get(id=article_id)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			c = form.save(commit = False)
			c.article = a
			c.save()


	return HttpResponseRedirect('/get/%s/' % article_id)


