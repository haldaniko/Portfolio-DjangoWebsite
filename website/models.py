import os
import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


def certif_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join(f"certificates/", filename)


def portfolio_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join(f"portfolio-content/", filename)


def decument_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join(f"document/", filename)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    percentage = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)]
    )

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
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.position_name} in {self.company_name}"


class StudyExperience(models.Model):
    school_name = models.CharField(max_length=255)
    school_link = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255)
    descritpion = models.TextField()

    def __str__(self):
        return f"{self.school_name}"


class PortfolioTag(models.Model):
    name = models.CharField(max_length=86)

    def __str__(self):
        return self.name


class PortfolioExample(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=portfolio_file_path)
    tag = models.ManyToManyField(PortfolioTag)
    github_source = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to=decument_file_path)

    def __str__(self):
        return self.name


class CertificateTag(models.Model):
    name = models.CharField(max_length=86)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    tag = models.ManyToManyField(CertificateTag)
    credential_link = models.CharField(max_length=255, null=True, blank=True)
    pdf_link = models.OneToOneField(Document, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to=certif_file_path)

    def __str__(self):
        return self.name

