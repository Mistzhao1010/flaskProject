import jwt
from datetime import datetime, timedelta
from flask import current_app
from enums.config_key_enum import ConfigKeyEnum
from config import EnvConfig


def encode_token(payload):
    """
    获取token
    :return:
    """
    secret_key = EnvConfig.SECRET_KEY
    token_expire_days = int(EnvConfig.TOKEN_EXPIRE_DAYS)
    payload['exp'] = datetime.utcnow() + timedelta(days=token_expire_days)
    # print(jwt.encode(payload=payload, key=secret_key, algorithm='HS256'))
    return jwt.encode(payload=payload, key=secret_key, algorithm='HS256')
