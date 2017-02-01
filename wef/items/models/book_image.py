from django.db import models

from .item_post import ItemPost

from versatileimagefield.fields import VersatileImageField


# image 업로드 경로 지정
def image_upload_to(instance, imagename):
    return 'posts_images/%s/%s/%s' % (instance.post.user.username, instance.post.id, imagename)


class BookImage(models.Model):

    post = models.ForeignKey(
            "ItemPost",
            )

    image = VersatileImageField(
            upload_to=image_upload_to,
            height_field="height",
            width_field="width",
            blank=True,
            null=True,
            )

    height = models.PositiveIntegerField(
            blank=True,
            null=True,
            )

    width = models.PositiveIntegerField(
            blank=True,
            null=True,
            )
