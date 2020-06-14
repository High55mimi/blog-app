from django.shortcuts import render,redirect
from django.conf import settings
from django.db.models import Count,Q
from posts.models import post,category
from marketing.models import signup
from posts.models import post_author
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from .forms import register_user
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
	feautured_posts=post.objects.filter(feautured=True)
	latest_posts=post.objects.order_by('-timestamp')[0:3]
	if request.method=="POST":
		email_content=request.POST["email"]
		insert_email=signup.objects.create(email=email_content)
		return redirect('/')
	context={
	'blog_posts':feautured_posts,
	'latest_posts':latest_posts
	}
	return render(request,'blog/index.html',context)

	#counts number of categories for posts
def get_category_count():
	catcount=post.objects.values('categories__title').annotate(Count('categories__title'))
	return catcount

def blog(request):
	categories_count=get_category_count()
	blog_posts=post.objects.order_by('-timestamp')
	other_posts=post.objects.all()[0:4]
	post_categories=category.objects.all()
	paginator=Paginator(blog_posts,4)
	page_req_var='page'
	page=request.GET.get(page_req_var)
	try:
		paginated_queryset=paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset=paginator.page(1)
	except EmptyPage:
		paginated_queryset=paginator.page(paginator.num_pages)
	context={
	   'queryset':paginated_queryset,
	   'page_req_var':page_req_var,
	   'others':other_posts,
	   'categories':post_categories,
	   'categories_count':categories_count

	}
	return render(request,'blog/blog.html',context)


def search(request):
	other_posts=post.objects.all()[0:4]
	queryset=post.objects.all()
	query=request.GET.get('q')
	categories_count=get_category_count()
	post_categories=category.objects.all()

	if query:
		querset=queryset.filter(Q(title__icontains=query) | Q(overview__icontains=query)).distinct()
		number_of_search=querset.count()
    
   
	context={
	'others':other_posts,
	'queryset':querset,
	'categories':post_categories,
	'categories_count':categories_count,
	'count':number_of_search
	}

	return render(request,'blog/search_results.html',context)

#view for register page
def register_page(request):
	if request.method=="POST":
		form=register_user(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f"Account Created!You Can Login Now")
			return redirect('login-page')
	else:
		form=register_user()
		context={
		'form':form
		}
		return render(request,'blog/register.html',context)
	    

	


	

