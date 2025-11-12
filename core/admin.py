from django.contrib import admin
from core.models import Post,MyUser,Comments,Like,FriendRequest,Message
# Register your models here.

admin.site.register(Post)
admin.site.register(MyUser)
admin.site.register(Comments)
admin.site.register(FriendRequest)
admin.site.register(Like)
admin.site.register(Message)
