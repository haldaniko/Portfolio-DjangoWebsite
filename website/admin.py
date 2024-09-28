from django.contrib import admin
from .models import (Certificate, Language, PortfolioExample, Skill, StudyExperience, WorkExperience, Document,
                     CertificateTag, PortfolioTag)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name", "lvl",)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    search_fields = ("position_name", "company_name", "location",)
    list_filter = ("company_name", "start_date", "end_date", "location",)


@admin.register(StudyExperience)
class StudyExperienceAdmin(admin.ModelAdmin):
    search_fields = ("school_name", "location",)
    list_filter = ("school_name", "start_date", "end_date", "location",)


@admin.register(PortfolioExample)
class PortfolioExampleAdmin(admin.ModelAdmin):
    search_fields = ("name", "description_small", "about",)
    list_filter = ("name",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(CertificateTag)
class CertificateTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(PortfolioTag)
class PortfolioTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)
