from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

from base.services import image_size_validator
from event_app.managers import UserManager


class User(AbstractUser):
    """Custom user model. Credentials: email, password."""
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={'unique': _("A user with that email already exists.")})
    username = models.CharField(
        _('username'),
        max_length=150,
        null=True,
        blank=True,
        help_text=_('150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
    )
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL,
                                     related_name='users', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Organization(models.Model):
    """ Organization model """
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=6)

    def __str__(self):
        return self.title


class Event(models.Model):
    """ Event model """
    title = models.CharField(max_length=100)
    description = models.TextField()
    organization = models.ManyToManyField(Organization, related_name='events')
    date = models.DateField()
    image = models.ImageField(
        upload_to='event_images',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), image_size_validator]
    )

    def save(self, *args, **kwargs):
        """Delete old image when updating or delete"""
        try:
            this = Event.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except self.DoesNotExist:
            pass
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
