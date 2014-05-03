from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from cobra_directory.models import UserProfile

# Register your models here.
class UserProfileChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = ['first_name', 'last_name', 'year']
    def save(self, commit=True):
        user = super(UserProfileChangeForm, self).save(commit=False)

class UserProfileAdmin(UserAdmin):
    form = UserProfileChangeForm

    fieldsets = (
        (None, {
                'fields': ('username', 'password', 'year', 'major', 'current_location', 'current_job', 'is_staff', 'is_superuser'),
                'classes': ('wide',)}),
       )
admin.site.register(UserProfile, UserProfileAdmin)
