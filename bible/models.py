from django.db import models

# Create your models here.


class BibleModel(models.Model):
    book = models.CharField(max_length=3)
    chapter = models.PositiveSmallIntegerField()
    verse = models.PositiveSmallIntegerField()
    contents = models.TextField()

    def __str__(self):
        return f"{self.book} {self.chapter}:{self.verse} {self.contents}"


class BibleMetaModel(models.Model):
    book = models.CharField(max_length=3)
    full_name = models.CharField(max_length=15)
    testament = models.CharField(max_length=3)
    chapter_length = models.PositiveSmallIntegerField()
    verse_length = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.full_name}"


class McheyneModel(models.Model):
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    order = models.PositiveIntegerField()
    part1 = models.CharField(max_length=30)
    part2 = models.CharField(max_length=30)
    part3 = models.CharField(max_length=30)
    part4 = models.CharField(max_length=30)
    part1_start_book = models.CharField(max_length=3)
    part1_start_chapter = models.PositiveIntegerField()
    part1_start_verse = models.PositiveIntegerField()
    part1_end_book = models.CharField(max_length=3)
    part1_end_chapter = models.PositiveIntegerField()
    part1_end_verse = models.PositiveIntegerField()
    part2_start_book = models.CharField(max_length=3)
    part2_start_chapter = models.PositiveIntegerField()
    part2_start_verse = models.PositiveIntegerField()
    part2_end_book = models.CharField(max_length=3)
    part2_end_chapter = models.PositiveIntegerField()
    part2_end_verse = models.PositiveIntegerField()
    part3_start_book = models.CharField(max_length=3)
    part3_start_chapter = models.PositiveIntegerField()
    part3_start_verse = models.PositiveIntegerField()
    part3_end_book = models.CharField(max_length=3)
    part3_end_chapter = models.PositiveIntegerField()
    part3_end_verse = models.PositiveIntegerField()
    part4_start_book = models.CharField(max_length=3)
    part4_start_chapter = models.PositiveIntegerField()
    part4_start_verse = models.PositiveIntegerField()
    part4_end_book = models.CharField(max_length=3)
    part4_end_chapter = models.PositiveIntegerField()
    part4_end_verse = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order}일차, {self.month}/{self.day} {self.part1} / {self.part2} / {self.part3} / {self.part4}"
