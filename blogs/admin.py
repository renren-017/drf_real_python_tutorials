from django.contrib import admin
from django import forms

from blogs.models import Category, Post, Comment, CategoryPost


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)


class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body')

    def save(self, commit=True):
        saved = super(PostForm, self).save(commit=commit)
        for category in self.cleaned_data['categories']:
            cp, created = CategoryPost.objects.get_or_create(category=category, post=saved)
            if not created:
                cp.save()
        return saved


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_on', 'last_modified', 'categories')
    search_fields = ('title',)
    ordering = ('-created_on',)
    form = PostForm


admin.site.register(Post, PostAdmin)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'body', 'created_on', 'post')
    list_filter = ('post', 'author')
    search_fields = ('post', 'author')
    ordering = ('-created_on',)


admin.site.register(Comment, PostCommentAdmin)