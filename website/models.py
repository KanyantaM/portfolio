from django.db import models

IMAGE_URL = 'static/images/'

########################################### HOME ####################################################################
class Owner(models.Model):
    name = models.CharField(max_length=80)
    profile = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    profile_image = models.ImageField(upload_to=f'{IMAGE_URL}profile_images/')
    bio = models.TextField()
    address = models.CharField(max_length=64)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    final_remarks = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.proficiency}%)"

class Service(models.Model):
    ICON_CHOICES = [
        ('bi bi-sun', 'Sun'),
        ('bi bi-code', 'Code'),
        ('bi bi-bar-chart', 'Bar Chart'),
        # Add more icon choices here
    ]

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)

    def __str__(self):
        return self.title

class Counter(models.Model):
    ICON_CHOICES = [
        ('bi bi-check', 'Check'),
        ('bi bi-journal-richtext', 'Journal'),
        ('bi bi-people', 'People'),
        ('bi bi-award', 'Award'),
        # Add more icon choices here
    ]

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='counters')
    title = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)

    def __str__(self):
        return self.title
 

class Testimonial(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='testimonials')
    auther_name = models.CharField(max_length=100)
    review = models.CharField(max_length=64)
    author_image = models.ImageField(upload_to=f"{IMAGE_URL}projects/testimonials/")   
    
    def __str__(self):
        return self.auther_name


 ########################################BLOG###############################################################   
class Blog(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='blog_ads')
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=64)
    cover_image = models.ImageField(upload_to=f"{IMAGE_URL}blogs/covers/")
    reading_time = models.PositiveSmallIntegerField()
    author_name = models.CharField(max_length=64)
    summary = models.TextField()
    author_image = models.ImageField(upload_to=f"{IMAGE_URL}blogs/authors/")
    content = models.TextField() #in html to keep your formating
    highlights = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    blog = models.ForeignKey(Blog, related_name='tags', on_delete=models.CASCADE)
    def __str__(self):
        return self.tag

class BlogComment(models.Model):
    author_name = models.CharField(max_length=64)
    author_image = models.URLField()
    author_email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    # replies = models.ManyToOneRel(to='self', on_delete=models.CASCADE, related_name='replies', field_name='replies')

    def __str__(self):
        return self.comment
        
    
########################################## PROJECT ##################################################################
class ProjectDetails(models.Model):
    #todo: make this be able to get a lot of photos and not just one
    gallery = models.ImageField(upload_to=f"{IMAGE_URL}projects/gallery/")
    category = models.CharField(max_length=64)
    client = models.CharField(max_length=100)
    project_date = models.DateField()
    project_url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='portfolio_ads')
    cover_image = models.ImageField(upload_to=f"{IMAGE_URL}projects/covers/")
    
    def __str__(self):
        return self.title

