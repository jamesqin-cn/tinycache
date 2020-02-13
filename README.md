# filecache

## What is filecache?
filecache is a python modules base on local file for any python data struct

## Example
use python decorators syntax to wrap the call target
```
from tinycache.tinycache import WithCache

@WithCache(3)
def Add(a, b):
    return a + b
```

## cache file format
cache file is json format, with filename look like './cache/`<md5_of_key_str>`'
```
{
    "created_at": 1581599989.43431, 
    "expired_at": 1581599992.43431
    "key_str": "Add(&1&2)", 
    "key": "9504ad0aba0f65472d5dad1e69a3bb21",
    "value": 3, 
}
```