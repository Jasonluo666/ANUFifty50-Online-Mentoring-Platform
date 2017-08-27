from django.db import models
from webcore.models import Profile
# Create your models here.

class Pair(models.Model):
    """
    This class defines a mentor-mentee pair
    It contains mentor name matched with mentee name
    """
    name = models.CharField(max_length=50, help_text='Enter a unique pair name',blank=True)
    mentor = models.ForeignKey('webcore.Profile', null=True, related_name="mentors", limit_choices_to={'role': 'Mentor'})
    mentee = models.ForeignKey('webcore.Profile', null=True, related_name="mentees", limit_choices_to={'role':'Mentee'})


    class Meta:
        db_table = "pair"

    def __str__(self):
        return self.name
