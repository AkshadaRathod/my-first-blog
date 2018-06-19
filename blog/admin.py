from django.contrib import admin
#As you can see, we import (include) the Post model . 
#To make our model visible on the admin page, 
#we need to register the model with admin.site.register(Post).
# Register your models here.
from .models import Post

admin.site.register(Post)