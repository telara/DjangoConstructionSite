from django.db import models
from django.conf import settings
from django.utils import timezone
from multiselectfield import MultiSelectField
from decimal import Decimal
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class BuildingProduct(models.Model):
    # CHOICES
    SCHOOL_CHOICES = [
        ('Praktijkonderwijs', 'Praktijkonderwijs'),
        ('MBO', 'MBO'),
        ('VMBO', 'VMBO'),
        ('HBO', 'HBO'),
        ('Opleidingsbedrijf', 'Opleidingsbedrijf'),
    ]

    CATEGORY_CHOICES = [
        ('MATERIALEN', 'Materialen'),
        ('CURSUS', 'Cursus'),
    ]

    # DATABASE FIELDS
    name = models.CharField(max_length=200)

    description = models.TextField()

    photo = ProcessedImageField(upload_to="product_photos",
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 200},
                                default="product_photos/default_photo.jpg")

    company_logo_thumbnail = ProcessedImageField(
        upload_to='company_logos',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 60},
        default="company_logos/default.jpg"
    )

    company_name = models.CharField(max_length=200)

    categories = MultiSelectField(choices=CATEGORY_CHOICES,
                                  default='CURSUS',
                                  null=False)

    school_type = models.CharField(max_length=20,
                                   choices=SCHOOL_CHOICES,
                                   default='MBO')

    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=Decimal('0.00'))

    expiration_date = models.DateTimeField(null=True)

    published_date = models.DateTimeField(default=timezone.now)

    # SAVE METHOD
    def create(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
