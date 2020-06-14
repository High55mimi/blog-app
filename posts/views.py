from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import post,category,comments,post_author,Postview
from django.db.models import Count,Q
from blog.views import get_category_count,search
from .forms import commentform,create_post_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_detail(request,pk):
	Post=get_object_or_404(post,pk=pk)
	Postview.objects.get_or_create(user=request.user,post=Post)
	categories_count=get_category_count()
	post_categories=category.objects.all()
	others=post.objects.all()
	form=commentform(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.instance.user=request.user
			form.instance.post=Post
			form.save()
			return redirect(reverse('post-detail',kwargs={
				'pk':Post.pk
				}))
	context={
	'post':Post,
	'categories':post_categories,
	'categories_count':categories_count,
	'others':others,
	'form':form,
	}
	return render(request,'posts/post.html',context)

#to get author of the post

def get_post_author(user):
	qs=post_author.objects.filter(user=user)
	if qs.exists():
		return qs[0]
	return None
   
@login_required
def create_post(request):
	form=create_post_form(request.POST or None,request.FILES or None)
	author=get_post_author(request.user)
	if request.method=="POST":
		if form.is_valid():
			form.instance.author=author
			form.save()
			return redirect(reverse("post-detail",kwargs={
				"pk":form.instance.pk
				}))
	context={
	"form":form
	}

	return render(request,"posts/add_post.html",context)





 