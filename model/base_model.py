from peewee import Model
from playhouse.db_url import connect
from config import EnvConfig
# 多线程写入方式，会造成读取不到刚写入的数据
db = connect(url=EnvConfig.DB_CONNECT_URL)


class BaseModel(Model):
    class Meta:
        database = db