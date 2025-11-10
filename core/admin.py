from django.contrib import admin

from core.models import (
    NewsletterSubscriber,
    Testimony,
    Experience,
    ContactOption,
)

admin.site.register(NewsletterSubscriber)
admin.site.register(Testimony)
admin.site.register(Experience)
admin.site.register(ContactOption)
