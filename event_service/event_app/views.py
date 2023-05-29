from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from event_app.serializers import OrganizationSerializer, EventSerializer, EventDetailSerializer, EventCreateSerializer
from event_app.services import get_events_with_organizations, get_event_detail


class OrganizationCreateView(generics.CreateAPIView):
    """ Create organization """
    serializer_class = OrganizationSerializer


class EventViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """ Create, retrieve, list events """
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ordering_fields = ['date']
    search_fields = ['title']

    def get_queryset(self):
        if self.action == 'retrieve':
            return get_event_detail(self.kwargs['pk'])
        return get_events_with_organizations()

    def get_serializer_class(self):
        if self.action == 'create':
            return EventCreateSerializer
        elif self.action == 'retrieve':
            return EventDetailSerializer
        return EventSerializer
