from django.contrib import admin
from .models import *
import admin_thumbnails
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

# Register your models here.
admin.site.register(Japan_clothes),
admin.site.register(Japan_foods),
admin.site.register(Japan_others),

admin.site.register(USA_clothes),
admin.site.register(USA_foods),
admin.site.register(USA_others),

admin.site.register(Vietnam_clothes),
admin.site.register(Vietnam_foods),
admin.site.register(Vietnam_others),


#커뮤니티 기능
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail("photo")
class PostImageInLine(admin.TabularInline):
    model = PostImage
    extra = 1
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "thumbnail",
    ]
    inlines = [
        CommentInLine,
        PostImageInLine,
    ]
    formfield_overrides = {
        ManyToManyField: {"widget":CheckboxSelectMultiple},
    }

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass