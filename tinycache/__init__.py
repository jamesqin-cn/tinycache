# encoding: utf-8
__author__ = 'jamesqin'

import os
import json
import time
import logging
import functools
import hashlib

def GenKey(method_name, args, kw):
    key_str = method_name + "("
    for arg in args:
        if str(type(arg)) == "<type 'instance'>" or ' object at 0x' in str(arg):
            key_str = "{}&class={}".format(key_str, arg.__class__)
            for name,val in vars(arg).items():
                key_str = "{}&self.{}={}".format(key_str, name, val)
        else:
            key_str = "{}&{}={}".format(key_str, str(type(arg)), arg)
    for (k,v) in kw.items():
        key_str = "{}&{}={}".format(key_str, k, v)
    key_str += ")"
    key = hashlib.md5(key_str.encode('utf8')).hexdigest()
    return (key, key_str)

# cache, use json to store cache
def WithCache(expired_sec=60*10, use_cache=True, cache_dir='cache/'):
    if cache_dir[-1] != '/':
        cache_dir = cache_dir + '/'
    is_exists = os.path.exists(cache_dir)
    if not is_exists:
        os.makedirs(cache_dir) 
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if not use_cache:
                return func(*args, **kw)

            (key,key_str) = GenKey(func.__name__, args, kw)
            file_name = cache_dir + key

            try:
                with open(file_name, 'r') as f:
                    cache = json.load(f)
            except IOError as err:
                logging.info("open cache file failed, file={}, error msg={}".format(file_name, err))
                cache = {}
            except ValueError as err:
                logging.info("cache file is not json format, file={}, error msg={}".format(file_name, err))
                cache = {}

            now = time.time()
            if 'value' in cache and 'expired_at' in cache:
                if cache['expired_at'] >= now:
                    logging.info("hit cache, cache filename = {}, key = {}".format(file_name,key_str))
                    return cache['value']
                else:
                    logging.info("cache found but expired {} seconds ago, filename = {}, key = {}".format(now-int(cache['expired_at']),file_name,key_str))

            cache['created_at'] = now
            cache['expired_at'] = now + expired_sec
            cache['key_str'] = key_str
            cache['key'] = key
            cache['value'] = func(*args, **kw)
            try:
                with open(file_name, 'w') as f:
                    json.dump(cache, f, indent=4, default=str)
            except IOError as err:
                logging.info("write cache file failed, file={}, error msg={}".format(file_name, err))
            else:
                logging.info("create cache, cache filename = {}, key = {}".format(file_name,key_str))
            return cache['value']
        return wrapper
    return decorator

