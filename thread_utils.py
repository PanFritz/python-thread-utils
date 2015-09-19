import threading
"""
Quick implementation of a @synchronized and @asynchronized decorators
"""

def synchronized(lock=None):
    def decorator(wrapped):
        def wrapper(*args, **kwargs):
            with lock:
                return wrapped(*args, **kwargs)
        return wrapper
    return decorator 

def asynchronized(daemon = True):
    def decorator(function):
        def wrapper(*args,**kwargs):
            thread = threading.Thread(target=function,args=args,kwargs=kwargs)
            thread.daemon = daemon
            thread.start()
        return wrapper
    return decorator