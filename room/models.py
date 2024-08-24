from django.db import models
import uuid

class Room(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return self.name
