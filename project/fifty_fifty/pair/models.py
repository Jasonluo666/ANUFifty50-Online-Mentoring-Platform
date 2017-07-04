from django.db import models

# Create your models here.

class Pair(models.Model):
    """
    This class defines a mentor-mentee pair
    It contains mentor name matched with mentee name
    """
    mentor = models.ForeignKey('webcore.Profile', null=True, related_name="mentors")
    mentee = models.ForeignKey('webcore.Profile', null=True, related_name="mentees")

    class Meta:
        db_table = "pair"
