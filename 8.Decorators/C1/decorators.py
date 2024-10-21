def configure_plugin_decorator(func):
    def wrapper(*args):
        dic = dict(args)
        return func(**dic)
    return wrapper