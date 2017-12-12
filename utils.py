def logger(func):
    def wrapper(*argc, **kw):
        print("call method %s:"%func.__name__)
        return func(*argc, **kw)
    return wrapper
