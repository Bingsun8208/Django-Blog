from django.db import models

# Create your models here.

from AccountApp.models import accounts
# Create your models here.

class boards(models.Model):
    boardId = models.IntegerField(primary_key=True)
    boardName = models.CharField(unique=True, max_length=200)


    def __unicode__(self):
        return self.boardName

class targets(models.Model):
    targetId = models.IntegerField(primary_key=True)
    targetName = models.CharField(unique=True, max_length=200)


    def __unicode__(self):
        return self.targetName

class articles(models.Model):
    articleId = models.IntegerField(primary_key=True)
    articleTitle = models.CharField(max_length=500)
    articleSubTitle = models.CharField(max_length=500)
    contents = models.TextField()
    targets = models.ManyToManyField(targets)
    boards = models.ForeignKey(boards, 'boardId')
    publishDate = models.DateTimeField()
    author = models.ForeignKey(accounts, 'accountId')

    def __unicode__(self):
        return self.articalTitle

class replies(models.Model):
    replyId = models.IntegerField(primary_key=True)
    article = models.ForeignKey(articles, 'articleId')
    author = models.ForeignKey(accounts, 'accountId')
    contents = models.TextField()
    publishDate = models.DateTimeField()