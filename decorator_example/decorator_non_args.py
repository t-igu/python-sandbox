from functools import wraps

class DecoratorClass(object):
    def deco(self):
        def _deco(function):
            @wraps(function)
            def __deco(*args, **kwargs):
                print ('before')
                result = function(*args, **kwargs)
                print ('after')
                return result
            return __deco
        return _deco

decoobj = DecoratorClass()

@decoobj.deco()
def hello():
    print ('Hello, World!')


if __name__ == '__main__':
    hello()