from django.contrib import admin
from .models import Document, Profile, Purchase

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'class_level', 'doc_type', 'price')
    list_filter = ('doc_type', 'class_level', 'subject')
    search_fields = ('title', 'subject')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'credits')
    search_fields = ('user__username', 'full_name')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'purchased_at')
    list_filter = ('purchased_at',)
