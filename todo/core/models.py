# coding: utf-8
from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField('título', max_length=255)
    description = models.TextField('descrição', blank=True)
    done = models.BooleanField('concluído', default=False)
    created_at = models.DateTimeField('criado em', default=timezone.now)
    owner = models.ForeignKey('auth.User', related_name='task_owner')
    tags = models.ManyToManyField('Tag')

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ('created_at',)


class Tag(models.Model):
    name = models.CharField('nome', max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
