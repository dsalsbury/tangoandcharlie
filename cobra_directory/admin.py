from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from cobra_directory.models import UserProfile

# Register your models here.
class UserProfileChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile

class UserProfileAdmin(UserAdmin):
    form = UserProfileChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('current_location', 'current_job')}),
       )
admin.site.register(UserProfile, UserAdmin)
