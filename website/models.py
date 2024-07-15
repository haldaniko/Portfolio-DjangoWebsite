from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255, unique=True)
    lvl = models.IntegerField()

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    position_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_link = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.position_name} in {self.company_name}"


class StudyExperience(models.Model):
    school_name = models.CharField(max_length=255)
    school_link = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    descritpion = models.TextField()

    def __str__(self):
        return f"{self.school_name}"


class PortfolioExample(models.Model):
    name = models.CharField(max_length=255)
    description_small = models.CharField(max_length=255)
    description_photo = models.ImageField()
    project_photo = models.ImageField()
    about = models.TextField()
    github_source = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    credential_link = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.name
