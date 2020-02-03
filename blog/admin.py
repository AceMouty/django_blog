from django.contrib import admin
from .models import Post
# Models registered will show up in the admin page


admin.site.register(Post)
