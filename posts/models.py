from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.

class post_author(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic=models.ImageField()

	def __str__(self):
		return self.user.username

class category(models.Model):
	title=models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Tag(models.Model):
	tag_title=models.CharField(max_length=50)

	def __str__(self):
		return self.tag_title

class post(models.Model):
	title=models.CharField(max_length=100)
	overview=HTMLField()
	timestamp=models.DateTimeField(auto_now_add=True,null=False)
	comment_count=models.IntegerField(default=0)
	#view_count=models.IntegerField(default=0)
	thumb_nail=models.ImageField()
	author=models.ForeignKey(post_author,on_delete=models.CASCADE)
	categories=models.ManyToManyField(category)
	feautured=models.BooleanField(null=True)
	

	def __str__(self):
		return self.title

	class Meta:
		ordering=["timestamp","title"]
	@property
	def get_comments(self):
		return self.comments.order_by("-timestamp")

	

    
class comments(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	timestamp=models.DateTimeField(auto_now_add=True)
	content=models.TextField()
	post=models.ForeignKey(post,related_name='comments',on_delete=models.CASCADE)


	def __str__(self):
		return self.user.username
class Postview(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(post,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	@property
	def viewcount(self):
		return Postview.objects.filter(post=self).count()
	