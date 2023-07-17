from django.contrib import admin
from users.models import User, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserProfileInline(admin.StackedInline):
    model = UserProfile

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    def profile_link(self, obj):
        # Assuming your UserProfile model has a 'user' OneToOneField
        print(f"Profile obj as been called : {obj}")
        profile = obj.userprofile  # Access the UserProfile instance
        print(f"Profile link as been called : {profile}")
        return profile  # Return the UserProfile instance
    profile_link.short_description = 'Profile Link'

    inlines = [UserProfileInline]

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email", "name", "is_admin", "profile_link"]
    list_display_links = ["id", "email", "profile_link"]  # Make the ID and email clickable in the admin panel
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin"]})
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []

# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)