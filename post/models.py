import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

# Create a seperate directory for each user to upload his/her files
def get_user_directory(instance, file):
    return 'user-{0}/{1}'.format(instance.user.username, file)

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tag')
    slug = models.SlugField(max_length=75, unique=True, null=False)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags', arg=[self.slug])

    # Creating a unique slug for each product
    def _create_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    # Overriding save method to save the unique slug for the product
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._create_unique_slug()
        super().save(*args, **kwargs)


class Post(models.Model):
    # Creating our own id for the post
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tags')
    photo = models.ImageField(upload_to=get_user_directory, null=False, verbose_name='Picture')
    caption = models.TextField(max_length=1000, verbose_name='Caption')
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('postdetail', args=[str(self.id)])
