from django.db import models
from django.urls import reverse
from django.conf import settings


class Destinations(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='created')
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    charges = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.URLField(blank=True)
    src = models.URLField(blank=True)
    label = models.CharField(max_length=250, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tourism:detail', args=[self.id, self.slug])


class Expenses(models.Model):
    destination = models.ForeignKey(Destinations, related_name='destination_expense', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    tour_start_date = models.DateField(blank=False)
    tour_end_date = models.DateField(blank=False)
    number_of_people = models.IntegerField()
    activity = models.CharField(max_length=250, default='Sight seeing')
    amount_to_spend = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return 'Expenses for {}'.format(self.destination)





