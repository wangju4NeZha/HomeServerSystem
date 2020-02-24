# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from common import md5_


class Contract(models.Model):
    t_contract_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    stop_time = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract'


class TBrowsingHistory(models.Model):
    browsing_history_id = models.AutoField(primary_key=True)
    usert = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    house = models.ForeignKey('THouse', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_browsing_history'


class TChatmsg(models.Model):
    chatmsg_id = models.AutoField(primary_key=True)
    msg = models.ForeignKey('TMessage', models.DO_NOTHING, blank=True, null=True)
    chatmsg_time = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_chatmsg'


class TComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    house = models.ForeignKey('THouse', models.DO_NOTHING, blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_comment'


class TComplaint(models.Model):
    fadeback_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('TOrder', models.DO_NOTHING, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_complaint'


class TFavorite(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    house = models.ForeignKey('THouse', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_favorite'


class TFeedback(models.Model):
    fadeback_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    house = models.ForeignKey('THouse', models.DO_NOTHING, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_feedback'


class THouse(models.Model):
    house_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    publish_time = models.DateField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sale_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_house'


class THouseVerify(models.Model):
    verify_id = models.AutoField(primary_key=True)
    house = models.ForeignKey(THouse, models.DO_NOTHING, blank=True, null=True)
    verify_status = models.IntegerField(blank=True, null=True)
    verify_recode = models.TextField(blank=True, null=True)
    verify_result = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_house_verify'


class TLuckyTicket(models.Model):
    lucky_ticket_id = models.AutoField(primary_key=True)
    u_lucky_ticketid = models.ForeignKey('TULuckyTicket', models.DO_NOTHING, db_column='u_lucky_ticketid', blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    begin_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    image = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lucky_ticket'


class TMessage(models.Model):
    msg_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    house = models.ForeignKey(THouse, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_message'


class TOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    house = models.ForeignKey(THouse, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    order_number = models.CharField(max_length=16, blank=True, null=True)
    enter_time = models.TimeField(blank=True, null=True)
    exit_time = models.TimeField(blank=True, null=True)
    hire_price = models.FloatField(blank=True, null=True)
    cash_price = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    order_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TPanda(models.Model):
    panda_id = models.AutoField(primary_key=True)
    detail_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_panda'


class TPublicNotice(models.Model):
    public_notice_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    link_url = models.CharField(max_length=100, blank=True, null=True)
    public_time = models.DateTimeField(auto_created=True, blank=True)
    note = models.TextField(blank=True, null=True)

    states = (
        (0, '待审核'),
        (1, '已通过'),
        (2, '未通过')
    )
    state = models.IntegerField(choices=states, default=0)

    class Meta:
        managed = False
        db_table = 't_public_notice'

    @property
    def state_label(self):
        return self.states[self.state][-1]


class TScore(models.Model):
    score_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_score'


class TService(models.Model):
    service_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    service_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_service'


class TSlidesshow(models.Model):
    slidesshow_id = models.AutoField(primary_key=True)
    house = models.ForeignKey(THouse, models.DO_NOTHING, blank=True, null=True)
    ord = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_slidesshow'


class TSysMenu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=20, blank=True, null=True)
    ord = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_menu'


class TSysRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=20)
    role_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_sys_role'


class TSysRoleMenu(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    sys_menu_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 't_sys_role_menu'


class TSysUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    head = models.ImageField(null=True, blank=True)
    # head = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    @property
    def role(self):
        return TSysRole.objects.get(role_id=self.role_id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if len(self.password) != 32:
            self.password = md5_.hash_encode(self.password)

        super(TSysUser, self).save()

    class Meta:
        managed = False
        db_table = 't_sys_user'


class TTradingrecord(models.Model):
    tradingrecord_id = models.AutoField(primary_key=True)
    house = models.ForeignKey(THouse, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tradingrecord'


class TULuckyTicket(models.Model):
    u_lucky_ticketid = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_u_lucky_ticket'


class TUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    identity_number = models.CharField(max_length=18, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    has_real_name = models.IntegerField(blank=True, null=True)
    is_member = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    dimension = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
