from django.db import models

# Create your models here.

class Pair(models.Model):
    """
    This class defines a mentor-mentee pair
    It contains mentor name matched with mentee name
    """
    name = models.CharField(max_length=50, help_text='Enter a unique pair name',blank=True)
    mentor = models.ForeignKey('webcore.Profile', null=True, related_name="mentors")
    mentee = models.ForeignKey('webcore.Profile', null=True, related_name="mentees")

    class Meta:
        db_table = "pair"

    def __str__(self):
        return self.name
