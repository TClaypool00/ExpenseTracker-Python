from django.db import models
from bills import models as bill_models


class Post(models.Model):
    post_id = models.AutoField(db_column='postId', primary_key=True)
    title = models.CharField(max_length=50)
    post_body = models.CharField(db_column='postBody', max_length=255)
    date = models.DateField()
    user_id = models.ForeignKey(
        bill_models.Users, db_column='userId', on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'


class Comments(models.Model):
    comment_id = models.AutoField(db_column='commentId', primary_key=True)
    comment_body = models.CharField(max_length=200, db_column='commentBody')
    date = models.DateTimeField()
    post_id = models.ForeignKey(
        Post, db_column='postId', on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        bill_models.Users, db_column='userId', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'


class Reply(models.Model):
    reply_id = models.AutoField(db_column='replyId', primary_key=True)
    reply_body = models.CharField(db_column='replyBody', max_length=200)
    date = models.DateField()
    comment_id = models.ForeignKey(
        Comments, db_column='commentId', on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        bill_models.Users, db_column='userId', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reply'
