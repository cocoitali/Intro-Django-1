from django.contrib import admin

# Register your models here.
from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register(Note, NoteAdmin)

# If you want to register more models, you can do so with additional register() calls:
# admin.site.register(Note)
# admin.site.register(PersonalNote)   # etc.