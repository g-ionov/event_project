from django.contrib import admin
from base.services import get_image_html
from event_app.models import User, Organization, Event


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'organization', 'username', 'is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('date_joined', 'last_login')
    list_display_links = ('id', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'organization')
    search_fields = ('email', 'username', 'organization__title')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'address', 'postcode')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'address', 'postcode')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'get_image')
    readonly_fields = ('get_image',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'date')
    list_filter = ('date',)

    @staticmethod
    def get_image(obj):
        return get_image_html(obj.image, 300)
