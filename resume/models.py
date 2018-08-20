from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    skills = models.ManyToManyField(
        'Skill',
        through='UserSkill'
    )


class Skill(models.Model):
    PROGRAMMING_LANGUAGE = 'PL'
    LEADERSHIP = 'LS'
    SOFTWARE = 'SW'
    FRAMEWORK = 'FW'

    TYPE_CHOICES = (
        (PROGRAMMING_LANGUAGE, 'Programming Language'),
        (LEADERSHIP, 'Leadership'),
        (SOFTWARE, 'Software'),
        (FRAMEWORK, 'Framework'),
    )

    name = models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)


class UserSkill(models.Model):
    BEGINNER = 1
    INTERMEDIATE = 2
    EXPERIENCED = 3
    EXPERT = 3
g
    SKILL_LEVELS = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (EXPERIENCED, 'Experienced'),
        (EXPERT, 'Expert')
    )

    user = models.ForeignKey(User, models.CASCADE)
    skill = models.ForeignKey(Skill, models.CASCADE)
    proficiency = models.IntegerField(choices=SKILL_LEVELS)


class Project(models.Model):
    user = models.ForeignKey('User', models.CASCADE)
    job = models.ForeignKey(
        'Job',
        models.CASCADE,
        null=True,
        blank=True
    )


class Job(models.Model):
    user = models.ForeignKey('User', models.CASCADE)
    job_title = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    start_date = models.DateField
    end_date = models.DateField


class Education(models.Model):
    ASSOCIATE_ARTS = 'AA'
    ASSOCIATE_SCIENCE = 'AS'
    ASSOCIATE_APPLIED_SCIENCE = 'AAS'
    ASSOCIATE_ENGINEERING = 'AE'
    ASSOCIATE_APPLIED_ARTS = 'AAA'
    ASSOCIATE_POLITICAL_SCIENCE = 'APS'
    BACHELOR_ARTS = 'BA'
    BACHELOR_SCIENCE = 'BS'
    # TODO rest of the degree types

    DEGREES = (
        (ASSOCIATE_ARTS, 'Associate of Arts'),
        (ASSOCIATE_SCIENCE, 'Associate of Science'),
        (BACHELOR_ARTS, 'Bachelor of Arts'),
        (BACHELOR_SCIENCE, 'Bachelor of Arts')
    )

    degree = models.CharField(max_length=2, choices=DEGREES)
    major = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    graduation_date = models.DateField
    gpa = models.DecimalField


class Detail(models.Model):
    text = models.CharField(max_length=100)
    job = models.ForeignKey(
        'Job',
        on_delete=models.CASCADE,
        null=True
    )
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        null=True
    )
    education = models.ForeignKey(
        'Education',
        on_delete=models.CASCADE,
        null=True
    )