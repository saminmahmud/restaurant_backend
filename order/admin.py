from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.status == "Pending":
            email_subject = "Your Order is Pending"
            email_body = render_to_string('order_pending.html', {'user' : obj.user})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.user.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

        if obj.status == "Completed":
            email_subject = "Your Order is Completed"
            email_body = render_to_string('order_completed.html', {'user' : obj.user})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.user.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()


admin.site.register(Order, OrderAdmin)
