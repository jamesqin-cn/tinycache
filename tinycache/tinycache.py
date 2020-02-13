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
        if str(type(arg)) == "<type 'instance'>":
            key_str = "{}&{}".format(key_str, arg.__class__)
        else:
            key_str = "{}&{}".format(key_str, arg)
    for (k,v) in kw.items():
        key_str = "{}&{}={}".format(key_str, k, v)
    key_str += ")"
    key = hashlib.md5(key_str).hexdigest()
    return (key, key_str)

# cache, use json to store cache
def WithCache(expired_sec=20, use_cache=True, cache_dir='cache/'):
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
                cache = json.load(open(file_name, 'r'))
            except (IOError, ValueError), err:
                logging.info("read cache error, msg = %s" % err)
                cache = {}

            now = time.time()
            if 'value' not in cache or 'expired_at' not in cache or now>cache['expired_at']:
                cache['created_at'] = now
                cache['expired_at'] = now + expired_sec
                cache['key_str'] = key_str
                cache['key'] = key
                cache['value'] = func(*args, **kw)
                json.dump(cache, open(file_name, 'w'), indent=4, default=str)
                logging.info("create cache, cache filename = {}, key = {}".format(file_name,key_str))
            else:
                logging.info("hit cache, cache filename = {}, key = {}".format(file_name,key_str))
            return cache['value']
        return wrapper
    return decorator

