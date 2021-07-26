import os
from django.db import models
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='files/images', blank=True, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Product` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Product` object is updated
    with new file.
    """

    # pk means primary key. pk of current object/instance
    if not instance.pk:
        return False

    if instance.image:
        try:
            old_file = Product.objects.get(pk=instance.pk).image
        except Product.DoesNotExist:
            return False

        if not old_file == instance.image:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
