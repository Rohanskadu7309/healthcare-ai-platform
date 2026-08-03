from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailService:
    
    @staticmethod
    def send_email(recipient, subject, template, context):
        """
        Send an email using a specified template and context.
        """

        html_message = render_to_string(template, context)
        
        email = EmailMultiAlternatives(
            subject=subject,
            body="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient],
        )
        email.attach_alternative(html_message, "text/html")
        email.send()
