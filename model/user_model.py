from datetime import datetime

from peewee import CharField, DateTimeField, BooleanField, AutoField, IntegerField
from model.base_model import BaseModel
from enums.role_enum import RoleEnum
from config import EnvConfig
from utils import datetime_util, bcrypt_util


class UserModel(BaseModel):
    """用户"""
    id = AutoField(primary_key=True)

    # 用户名
    username = CharField(unique=True, null=None)

    # 密码
    password = CharField()

    # 头像
    avatar_url = CharField(null=None, default='')

    # 用户角色
    role = IntegerField(null=False, default=RoleEnum.USER)

    # 账号状态
    status = BooleanField(default=True)

    # 创建时间
    create_time = DateTimeField(default=datetime.now)

    # 更新时间
    update_time = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'tb_user'

    @property
    def is_default_password(self):
        """
        管理员是否使用系统给定的默认密码
        :return:
        """
        if self.username != EnvConfig.DEFAULT_ADMIN_USERNAME:
            return False
        else:
            return bcrypt_util.check_password(EnvConfig.DEFAULT_ADMIN_PASSWORD, self.password)

    @property
    def create_time_label(self):
        return datetime_util.time_for_human(self.create_time)


def init_table_data():
    data = [
        {
            'username': EnvConfig.ADMIN_USERNAME,
            'password': bcrypt_util.encode_password(EnvConfig.DMIN_PASSWORD),
            'role': RoleEnum.ADMIN
        }
    ]

    UserModel.insert_many(data).execute()
