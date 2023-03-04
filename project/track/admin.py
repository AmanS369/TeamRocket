from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import Ngodetails,blog_model,achievement

admin.site.register(Ngodetails)
admin.site.register(blog_model)
admin.site.register(achievement)

