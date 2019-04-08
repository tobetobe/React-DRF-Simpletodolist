# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class todoModel(models.Model):
    todoContent = models.TextField()
    isDone = models.BooleanField()
    expireDate = models.TextField()
    priority = models.IntegerField()  # 3->top 2->mid 1->low

    def __str__(self):
        return "{} {}".format(self.todoContent, self.isDone)

    class Meta:
        ordering = ('priority',)  # Ordered by priority
