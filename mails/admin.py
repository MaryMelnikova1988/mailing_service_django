from django.contrib import admin

from mails.models import Client, Message, Mail


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk','email', 'last_name', 'first_name', 'father_name','comment',)
    list_filter = ('email','last_name',)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'body',)
    search_fields = ('title', 'body',)
    list_filter = ('title',)


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('pk','name','message','date_start', 'date_end','start_time','period', 'status','is_active', )
    search_fields = ( 'message',)
    list_filter = ('is_active',)



