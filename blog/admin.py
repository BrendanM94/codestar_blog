from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'status', 'created_on', 'updated_on')
	list_filter = ('status', 'created_on', 'author')
	search_fields = ('title', 'content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'author', 'post', 'approved', 'created_on')
	list_filter = ('approved', 'created_on', 'author')
	search_fields = ('body', 'author__username', 'post__title')
	actions = ['approve_comments']

	def approve_comments(self, request, queryset):
		queryset.update(approved=True)

	approve_comments.short_description = "Mark selected comments as approved"
