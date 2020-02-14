# Tiny Cache

## What is TinyCache?
tinycache is a python modules base on local file for any python data struct

## Programming Language
- python 2.7
- python 3.7

## Install
```
pip install tinycache 
```

## Quick Start
use python decorators syntax to wrap the call target
```
from tinycache import WithCache

@WithCache(5)
def Add(a, b):
    return a + b

class Foo():
    @WithCache(5)
    def Bar(self, a, b):
        return a - b
```

## Cache File Format
cache file is json format, with filename look like './cache/`<md5_of_key_str>`'
```
{
    "created_at": 1581652043.872242,
    "expired_at": 1581652048.872242,
    "key_str": "Add(&<class 'int'>=1&<class 'int'>=2)",
    "key": "9d0aa1c9634aa575696710c7dfb9f018",
    "value": 3
}
```