from django.core.mail import mail_admins
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender="contact.ContactMessage")
def send_contactmessage_email(sender, instance, created, **kwargs):
    if created:
        body = """
            Name: {}
            Email: {}
            Body: {}
            """.format(instance.name, instance.email, instance.body)
        mail_admins("New Contact Message", body, fail_silently=False)
