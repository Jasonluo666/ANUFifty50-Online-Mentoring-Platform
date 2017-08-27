from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

YEAR_OF_STUDY = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5+','5+'),
)

BACHELOR_DEGREE_PROGRAMME = (
    ('','-'),
    ('AACOM','Advanced Computing (Honours)'),
    ('AACRD','Advanced Computing (R&D) (Honours)'),
    ('BADAN','Applied Data Analytics'),
    ('HADAN','Applied Data Analytics (Honours)'),
    ('BBIOT','Biotechnology'),
    ('HBIOT','Biotechnology (Honours)'),
    ('AENGI','Engineering (Honours)'),
    ('AENRD','Engineering (R&D) (Honours)'),
    ('BENSU','Environment and Sustainability'),
    ('HENSU','Environment and Sustainability (Honours)'),
    ('AENSU','Environment and Sustainability Advanced (Honours)'),
    ('HENVS','Environemntal Studies'),
    ('BGENE','Genetics'),
    ('HGENE','Genetics (Honours)'),
    ('BHLTH','Health Science (Honours)'),
    ('BIT','Information Technology'),
    ('HIT','Information Technology (Honours)'),
    ('BMASC','Mathematical Sciences'),
    ('HMASC','Mathematical Sciences (Honours)'),
    ('BMEDS','Medical Science'),
    ('HMEDS/HMDSA','Medical Science (Honours)'),
    ('PHBSCIENCE', 'PhB / Bachelor of Philosophy (Honours) in Science'),
    ('APSYC','Psychology (Honours)'),
    ('BSC','Science'),
    ('HSC','Science (Honours)'),
    ('ASCAD','Science (Advanced) (Honours)'),
    ('BSPSY','Science (Psychology)'),
    ('HSPSY','Science (Psychology) (Honours)'),
    ('ASENG','Software Engineering (Honours)'),
    ('ESCIE','Diploma of Science'),
    ('ECOMP','Diploma of Computing'),
)

ROLES = (
    ('Mentee', 'Mentee'),
    ('Mentor', 'Mentor'),
)

GENDER = (
    ('','-'), #error-checking st. "-" isn't a valid answer
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Rather not say', 'Rather not say'),
)


MENTOR_GENDER = (
    ('Definitely', 'Definitely'),
    ('If possible', 'If possible'),
    ('Unconcerned', 'Unconcerned'),
)



class Profile(models.Model):
    role = models.CharField(max_length=15, null = True ,choices=ROLES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uniId = models.CharField(max_length=100)
    study_year = models.CharField(max_length=100,choices=YEAR_OF_STUDY, blank=False)
    degree_programme = models.CharField(max_length=50, null = True ,blank=False,choices=BACHELOR_DEGREE_PROGRAMME)
    degree_programme_2 = models.CharField(max_length=50, null = True ,choices=BACHELOR_DEGREE_PROGRAMME)
    degree_major = models.CharField(max_length=15, null = True)
    gender = models.CharField(max_length=15, null = True ,choices=GENDER)
    mentor_gender = models.CharField(max_length=15, null = True ,choices=MENTOR_GENDER)
    why_mentor = models.CharField(max_length=150, null = True)
    why_div_equ_inc = models.CharField(max_length=150, null = True)
    mentee_number = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    hear_about = models.CharField(max_length=150, null = True)
    paired_with = models.CharField(max_length=50, null = True)


    def __str__(self):
       return str(self.role)+ " "+ str(self.uniId)

class Xpairs(models.Model):
    mentee = models.ForeignKey(Profile, related_name="Xmentees", limit_choices_to={'role': 'Mentee'},)
    mentor = models.ForeignKey(Profile, related_name="Xmentors", limit_choices_to={'role': 'Mentor'})
    name = models.CharField(max_length=50, help_text='Enter a unique pair name',blank=True, null = True)

    def save(self, *args, **kwargs): ## Overiding the save function of Xpairs
        self.name = str(self.mentee) +" -> "+ str(self.mentor)  ## Changing name of pair as mentee -> mentor
        self.shortcode = transfer(str(self.mentee),str(self.mentor)) ## trimming mentee and mentor, and transfering them to Profile.paired_with
        super(Xpairs, self).save(*args, **kwargs)

    def __str__(self):
       return str(self.mentee) +" -> "+ str(self.mentor)



def transfer(tee,tor):
    menteeId = tee.split(' ', 1)[1]
    mentorId = tor.split(' ', 1)[1]
    print(Profile.objects.all())
    Profile.objects.filter(uniId__contains=menteeId).update(paired_with=mentorId)
    Profile.objects.filter(uniId__contains=mentorId).update(paired_with=menteeId)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
