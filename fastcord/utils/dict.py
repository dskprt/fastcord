def try_get_value(obj, key):
    try:
        return obj[key]
    except:
        return None