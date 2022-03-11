from django.db import models
from account.models import DateAbstractModel, PersonalArea


class Organization(DateAbstractModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    structure = models.CharField(max_length=10, blank=True, null=True, help_text='ИП, ООО, ЗАО или др')
    personal_area = models.OneToOneField(PersonalArea, on_delete=models.CASCADE)


