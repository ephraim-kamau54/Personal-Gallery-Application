from django.contrib import admin
from .models import Editor,Article,tags,Location,Category,Images


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Images)






