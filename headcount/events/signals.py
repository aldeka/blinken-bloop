from django.contrib.sites.models import Site
from django.http import HttpRequest

from headcount.utils import generate_email


def event_creation(sender, instance, created, raw, **kwargs):
    if created:
        to_email = '{0.name} <{0.email}>'.format(instance.host)
        email = generate_email(
            'events/email/new_event',
            HttpRequest(),
            {
                'instance': instance,
                'domain': Site.objects.get_current().domain
            },
            to=(to_email,)
        )
        email.send(fail_silently=True)


def event_change(sender, instance, created, raw, **kwargs):
    if not created:
        to_emails = ['{0.name} <{0.email}>'.format(rsvp.user) for rsvp in
                     instance.rsvps.possible()]
        email = generate_email(
            'events/email/change_event',
            HttpRequest(),
            {
                'instance': instance,
                'domain': Site.objects.get_current().domain
            },
            to=to_emails
        )
        email.send(fail_silently=True)


def event_delete(sender, instance, **kwargs):
    to_emails = ['{0.name} <{0.email}>'.format(rsvp.user) for rsvp in
                 instance.rsvps.possible()]
    email = generate_email(
        'events/email/delete_event',
        HttpRequest(),
        {
            'instance': instance
        },
        to=to_emails
    )
    email.send(fail_silently=True)


def rsvp_creation(sender, instance, created, raw, **kwargs):
    if created and instance.response != instance.RESPONSE_CHOICES.no:
        to_email = '{0.name} <{0.email}>'.format(instance.user)
        email = generate_email(
            'events/email/new_rsvp',
            HttpRequest(),
            {
                'instance': instance,
                'domain': Site.objects.get_current().domain
            },
            to=(to_email,)
        )
        email.send(fail_silently=True)


def rsvp_delete(sender, instance, **kwargs):
    to_email = '{0.name} <{0.email}>'.format(instance.user)

    email = generate_email(
        'events/email/delete_rsvp',
        HttpRequest(),
        {
            'instance': instance
        },
        to=(to_email,)
    )
    email.send(fail_silently=True)


def rsvp_notification(sender, instance, created, raw, **kwargs):
    if instance.response == instance.RESPONSE_CHOICES.yes:
        to_email = '{0.name} <{0.email}>'.format(instance.event.host)
        email = generate_email(
            'events/email/notify_rsvp',
            HttpRequest(),
            {
                'instance': instance,
            },
            to=(to_email,)
        )
        email.send(fail_silently=True)
