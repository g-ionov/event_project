from django.db.models import Prefetch

from event_app.models import Event, Organization, User


def get_events_with_organizations():
    """Get all events with organizations"""
    return Event.objects.prefetch_related('organization').all()


def get_event_detail(event_id):
    """Get event detail with organizations and users of organizations"""
    return Event.objects.prefetch_related(
        Prefetch(
            'organization',
            queryset=Organization.objects.prefetch_related('users').all()
        )
    ).filter(id=event_id)