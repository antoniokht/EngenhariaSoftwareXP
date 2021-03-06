from django.db import models
from django.contrib.auth.models import User
#from PIL import Image


class Profile(models.Model):
    description = models.TextField(null=True, blank=True,
                                   default="", verbose_name="Breve descrição")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.png', upload_to='profile_pics', verbose_name="Imagem de perfil")

    def __str__(self):
        return f'{self.user.username} Profile'

    # Shrink image size. Will not be used in S3
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
