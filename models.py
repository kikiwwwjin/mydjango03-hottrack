# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blog_post'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class HottrackSong(models.Model):
    id = models.BigAutoField(primary_key=True)
    melon_uid = models.CharField(unique=True, max_length=20)
    rank = models.PositiveSmallIntegerField()
    album_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    cover_url = models.CharField(max_length=200)
    lyrics = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    like_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'hottrack_song'


class MassFinalMdDataPo(models.Model):
    hashcode = models.CharField(primary_key=True, max_length=64)
    title = models.TextField(blank=True, null=True)
    option_name = models.TextField(blank=True, null=True)
    search_keyword = models.TextField(blank=True, null=True)
    result_target = models.TextField(blank=True, null=True)
    bon_malls = models.TextField(blank=True, null=True)
    mall_pid = models.TextField(blank=True, null=True)
    fixed_ctime = models.TextField(blank=True, null=True)
    reg_date = models.TextField(blank=True, null=True)
    reg_time = models.TextField(blank=True, null=True)
    oper_serialno = models.TextField(blank=True, null=True)
    refine_code = models.TextField(blank=True, null=True)
    deleted_keywords = models.TextField(blank=True, null=True)
    abs_model = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mass_final_md_data_po'


class RefineReportFinalmd(models.Model):
    id = models.BigAutoField(primary_key=True)
    hashcode = models.CharField(max_length=64)
    title = models.CharField(max_length=512)
    option_name = models.CharField(max_length=512)
    search_keyword = models.CharField(max_length=100)
    result_target = models.CharField(max_length=2058)
    bon_malls = models.CharField(max_length=64)
    mall_pid = models.CharField(max_length=128)
    fixed_ctime = models.CharField(max_length=128)
    reg_date = models.DateField()
    reg_time = models.DateTimeField()
    oper_serialno = models.CharField(max_length=64)
    refine_code = models.IntegerField()
    deleted_keywords = models.CharField(max_length=2058)
    abs_model = models.CharField(max_length=2058)

    class Meta:
        managed = False
        db_table = 'refine_report_finalmd'
