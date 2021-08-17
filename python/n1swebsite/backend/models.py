from django.db import models, connection
import os

# Create your models here.

'''
    @class: ImageSlideshowModel
        -> Slideshow table in database
'''
class SlideshowModel(models.Model):
    STATUS_OPTIONS = [
        ('In Use', 'In Use'),
        ('Not Use', 'Not Use')
    ]

    # Columns
    image = models.ImageField(upload_to = 'slideshow/', default='no-image.png', blank = False)
    title = models.CharField(max_length = 150, blank = True)
    description = models.CharField(max_length = 250, blank = False)
    status = models.CharField(max_length = 20, choices = STATUS_OPTIONS, default = 'In Use', blank = True)

    # Delete file when object deleted in database.
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        return super(SlideshowModel, self).delete(*args, **kwargs)

    # Class method
    # Delete all data in table.
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table};')

    # Class method
    # Set to un use all the images
    @classmethod
    def setUnuse(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'UPDATE {cls._meta.db_table} SET status="Not Use";')

    # Table name
    class Meta:
        db_table = 'slideshow'

'''
    @class: BranchModel
        -> Branch table in database.
'''
class BranchModel(models.Model):
    # Columns
    image = models.ImageField(upload_to = 'branch/', default='no-image.png', blank = False)
    title = models.CharField(max_length = 150, blank = False)
    content = models.TextField(blank = False)
    phonenumber = models.CharField(max_length = 20, default = 'N/A', blank = False)
    email = models.EmailField(default = 'N/A', blank = False)
    address = models.TextField(default = 'N/A', blank = False)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        return super(BranchModel, self).delete(*args, **kwargs)

    # Class method
    # Delete all data in tables.
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table};')

    # Table name
    class Meta:
        db_table = 'branch'

'''
    @class: NewsEventModel
        -> News and event table in database.
'''
class NewsEventModel(models.Model):
    # SELECTION OPTION
    CATEGORY = [
        ('News', 'News'),
        ('Event', 'Event')
    ]

    # Columns
    image = models.ImageField(upload_to='newsevent/', default='no-image.png', blank = False)
    title = models.CharField(max_length = 150, blank = False)
    date = models.DateField(blank = False)
    content = models.TextField(blank = False)
    category = models.CharField(max_length = 20, choices=CATEGORY, blank = False)

    # Delete file when object deleted in database.
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        return super(NewsEventModel, self).delete(*args, **kwargs)

    # Class method
    # Delete all data in table.
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table};')

    # Table name
    class Meta:
        db_table = 'newsevent'
        ordering = ['-date']

'''
    @class: AboutModel
        -> About table in database.
'''
class AboutModel(models.Model):
    # Columns
    header = models.CharField(max_length = 150, blank = False)
    content = models.TextField(blank = False)
    mission = models.TextField(blank = False)
    vision = models.TextField(blank = False)

    # Class method
    # Delete all data in table.
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table}')

    # Table name
    class Meta:
        db_table = 'about'


'''
    @class: MilestoneModel
        -> Milestone table in database.
'''
class MilestoneModel(models.Model):
    # Columns
    title = models.CharField(max_length = 150, blank = False)
    image = models.ImageField(upload_to = 'milestone', default = 'no-image.png', blank = False)
    date = models.DateField(blank = False)
    content = models.TextField(blank = False)

    # Delete file when object deleted in database.
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        return super(MilestoneModel, self).delete(*args, **kwargs)

    # Class method
    # Delete all data in database
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table};')

    # Table name
    class Meta:
        db_table = 'milestone'

'''
    @class: VideoModel
        -> Video model
'''
class VideoModel(models.Model):
    # Columns
    video = models.FileField(upload_to = 'videos/', blank = False)
    date = models.DateField(blank = False)
    title = models.CharField(max_length = 150, blank = False)

    # Delete file when object deleted in database.
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.video.path):
            os.remove(self.video.path)
        return super(VideoModel, self).delete(*args, **kwargs)

    # Table name
    class Meta:
        db_table = 'videos'

'''
    @class: SiteSettingsModel
        -> website settings configuration
'''
class SiteSettingsModel(models.Model):
    # Columns
    section = models.CharField(max_length = 150, blank = False)
    is_display = models.BooleanField()

    # Class method
    # Delete all data
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table};')

    # Class method
    # Update settings in false
    @classmethod
    def updateallsettings(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'UPDATE {cls._meta.db_table} SET is_display=false;')

    # Table name
    class Meta:
        db_table = 'sitesettings'

'''
    @class: CareersModel
        -> Careers model.
'''
class CareersModel(models.Model):
    image = models.ImageField(upload_to = 'careers/', default = 'no-image.png', blank = False)
    title = models.CharField(max_length = 150, blank = False)
    description = models.TextField(blank = False)
    vacants = models.IntegerField(blank = False)

    # Delete file when object deleted in database.
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        return super(CareersModel, self).delete(*args, **kwargs)

    # Delete all data records.
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table};')

    # Table settings
    class Meta:
        db_table = 'careers'
        ordering = ['-pk']

'''
    @class: ContactsModel
        -> Contacts model
'''
class ContactusModel(models.Model):
    OPTIONS = [
        ('Inquiry', 'Inquiry'),
        ('Feedback', 'Feedback'),
        ('Review', 'Review'),
    ]

    fullname = models.CharField(max_length = 150, blank = False)
    email = models.EmailField(blank = False)
    category = models.CharField(max_length = 20, choices = OPTIONS, blank = False)
    message = models.TextField(blank = False)

    # Delete all objects in table.
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM {cls._meta.db_table};')

    # Table settings.
    class Meta:
        db_table = 'contactus'
        ordering = ['-pk']
