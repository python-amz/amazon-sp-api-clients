import json
import pickle
from typing import Dict, Tuple, Optional

import peewee
from requests import Response

db_proxy = peewee.Proxy()


class CacheModel(peewee.Model):
    class Meta:
        primary_key = peewee.CompositeKey(
            'endpoint',
            'marketplace_id',
            'refresh_token',
            'aws_access_key',
            'path',
            'data',
            'params',
            'method',
        )
        database = db_proxy

    endpoint = peewee.CharField(100)
    marketplace_id = peewee.CharField(100)
    refresh_token = peewee.CharField(500)
    aws_access_key = peewee.CharField(100)
    path = peewee.CharField(100)
    method = peewee.CharField(10)
    params = peewee.CharField(2000)
    data = peewee.CharField(2000)
    headers = peewee.CharField(2000)
    value = peewee.BlobField()


class RequestCache:
    def __init__(self,
                 endpoint: str,
                 marketplace_id: str,
                 refresh_token: str,
                 aws_access_key: str,
                 ):
        self.keys = {
            'endpoint': endpoint,
            'marketplace_id': marketplace_id,
            'refresh_token': refresh_token,
            'aws_access_key': aws_access_key,
        }
        self.db = peewee.SqliteDatabase('.sp-api.sqlite')
        db_proxy.initialize(self.db)
        self.db.create_tables([CacheModel])

    # path, method, params, data,headers
    KEYS_TYPE = Tuple[str, str, Dict, Dict, Dict]

    def __get_keys(self, keys: KEYS_TYPE):
        path, method, params, data, headers = keys
        keys = self.keys.copy()
        keys.update({
            'path': path,
            'method': method,
            'params': json.dumps(params),
            'data': json.dumps(data),
            'headers': json.dumps(headers),
        })
        return keys

    def __setitem__(self, keys: KEYS_TYPE, value: Response):
        keys = self.__get_keys(keys)
        keys['value'] = pickle.dumps(value)
        CacheModel.insert(**keys).execute()

    def __getitem__(self, keys: KEYS_TYPE) -> Optional[Response]:
        cache_model = CacheModel.get_or_none(**self.__get_keys(keys))
        if cache_model is not None:
            return pickle.loads(cache_model.value)
