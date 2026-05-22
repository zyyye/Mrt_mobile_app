import time

cache = {}

def set_cache(key, value, ttl=300):
    cache[key] = {
        "value": value,
        "expire": time.time() + ttl
    }

def get_cache(key):
    if key not in cache:
        return None

    if time.time() > cache[key]["expire"]:
        del cache[key]
        return None

    return cache[key]["value"]