from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.

class Users(AbstractUser):
    @receiver(post_save, sender = settings.AUTH_USER_MODEL)
    def create_token(sender, instance = None, created = False, **kwargs):
        if created:
            Token.objects.create(user = instance)

    class Meta:
        db_table = 'users'


def initializeControlNumber():
    get_last_id = Evaluation.objects.last()
    control_no  = 0
    control_no  = f'CDP-0000000{get_last_id.pk + 1}' if get_last_id is not None else 'CDP-00000001'
    return control_no


class Evaluation(models.Model):
    control_no                 = models.CharField(max_length = 250, default = initializeControlNumber, blank = True, null = True, unique = True, error_messages = {'unique': 'Control No. is already exists.'})
    date                       = models.DateField(auto_now = True)
    evaluated_person           = models.CharField(max_length = 250)
    line_manager               = models.CharField(max_length = 250)
    evaluator                  = models.CharField(max_length = 250)
    survey1_competency_level1  = models.CharField(max_length = 250)
    survey1_competency_level2  = models.CharField(max_length = 250)
    survey1_competency_level3  = models.CharField(max_length = 250)
    survey2_competency_level1  = models.CharField(max_length = 250)
    survey2_competency_level2  = models.CharField(max_length = 250)
    survey3_competency_level1  = models.CharField(max_length = 250)
    survey3_competency_level2  = models.CharField(max_length = 250)
    survey3_competency_level3  = models.CharField(max_length = 250)
    survey3_competency_level4  = models.CharField(max_length = 250)
    survey3_competency_level5  = models.CharField(max_length = 250)
    survey3_competency_level6  = models.CharField(max_length = 250)
    survey3_competency_level7  = models.CharField(max_length = 250)
    survey3_competency_level8  = models.CharField(max_length = 250)
    survey3_competency_level9  = models.CharField(max_length = 250)
    survey3_competency_level10 = models.CharField(max_length = 250)
    survey3_competency_level11 = models.CharField(max_length = 250)
    survey1_grade1             = models.CharField(max_length = 250)
    survey1_grade2             = models.CharField(max_length = 250)
    survey1_grade3             = models.CharField(max_length = 250)
    survey2_grade1             = models.CharField(max_length = 250)
    survey2_grade2             = models.CharField(max_length = 250)
    survey3_grade1             = models.CharField(max_length = 250)
    survey3_grade2             = models.CharField(max_length = 250)
    survey3_grade3             = models.CharField(max_length = 250)
    survey3_grade4             = models.CharField(max_length = 250)
    survey3_grade5             = models.CharField(max_length = 250)
    survey3_grade6             = models.CharField(max_length = 250)
    survey3_grade7             = models.CharField(max_length = 250)
    survey3_grade8             = models.CharField(max_length = 250)
    survey3_grade9             = models.CharField(max_length = 250)
    survey3_grade10            = models.CharField(max_length = 250)
    survey3_grade11            = models.CharField(max_length = 250)
    survey1_feedback1          = models.TextField()
    survey1_feedback2          = models.TextField()
    survey1_feedback3          = models.TextField()
    survey2_feedback1          = models.TextField()
    survey2_feedback2          = models.TextField()
    survey3_feedback1          = models.TextField()
    survey3_feedback2          = models.TextField()
    survey3_feedback3          = models.TextField()
    survey3_feedback4          = models.TextField()
    survey3_feedback5          = models.TextField()
    survey3_feedback6          = models.TextField()
    survey3_feedback7          = models.TextField()
    survey3_feedback8          = models.TextField()
    survey3_feedback9          = models.TextField()
    survey3_feedback10         = models.TextField()
    survey3_feedback11         = models.TextField()

    class Meta:
        db_table = 'evaluations'


def initializeControlNumberTrainingMemo():
    get_last_record = TrainingMemo.objects.last()
    control_no = 0
    control_no = f'TM-0000000{get_last_record.pk + 1}' if get_last_record is not None else 'TM-00000001'
    return control_no


class TrainingMemo(models.Model):
    control_no                 = models.CharField(max_length = 250, default = initializeControlNumberTrainingMemo, blank = True, null = True, unique = True, error_messages = {'unique': 'Traning memo control no. is already exists!'})
    date                       = models.CharField(max_length = 150, blank = True, null = True)
    dear                       = models.CharField(max_length = 250, blank = True, null = True)
    to1                        = models.CharField(max_length = 250, blank = True, null = True)
    to2                        = models.CharField(max_length = 250, blank = True, null = True)
    volume_objective           = models.CharField(max_length = 250, blank = True, null = True)
    volume_actual              = models.CharField(max_length = 250, blank = True, null = True)
    volume_percent             = models.CharField(max_length = 250, blank = True, null = True)
    callproductivity_objective = models.CharField(max_length = 250, blank = True, null = True)
    callproductivity_actual    = models.CharField(max_length = 250, blank = True, null = True)
    callproductivity_percent   = models.CharField(max_length = 250, blank = True, null = True)
    distribution_objective     = models.CharField(max_length = 250, blank = True, null = True)
    distribution_actual        = models.CharField(max_length = 250, blank = True, null = True)
    distribution_percent       = models.CharField(max_length = 250, blank = True, null = True)
    range_objective            = models.CharField(max_length = 250, blank = True, null = True)
    range_actual               = models.CharField(max_length = 250, blank = True, null = True)
    range_percent              = models.CharField(max_length = 250, blank = True, null = True)
    merchandising_objective    = models.CharField(max_length = 250, blank = True, null = True)
    merchandising_actual       = models.CharField(max_length = 250, blank = True, null = True)
    merchandising_percent      = models.CharField(max_length = 250, blank = True, null = True)
    cycle_objective            = models.CharField(max_length = 250, blank = True, null = True)
    cycle_actual               = models.CharField(max_length = 250, blank = True, null = True)
    cycle_percent              = models.CharField(max_length = 250, blank = True, null = True)
    strength                   = models.CharField(max_length = 250, blank = True, null = True)
    oppurtunities              = models.CharField(max_length = 250, blank = True, null = True)
    insights                   = models.CharField(max_length = 250, blank = True, null = True)
    actionplan                 = models.CharField(max_length = 250, blank = True, null = True)
    nextstep                   = models.CharField(max_length = 250, blank = True, null = True)

    class Meta:
        db_table = 'trainingmemos'
