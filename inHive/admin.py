from django.contrib import admin
from .models import User, Hive, Task, Membership

admin.site.register(User)
# admin.site.register(QueenBee)
admin.site.register(Hive)
admin.site.register(Task)
admin.site.register(Membership)
