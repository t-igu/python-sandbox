import functools
from loguru import logger

def accsess_log(app_name):
    def _wrapper(func):
        @functools.wraps(func)
        def __inner(*args, **kwargs):
            logger.info(app_name)
            v = func(*args, **kwargs)
            logger.info(app_name)
            return v
        return __inner
    return _wrapper

@accsess_log('aaa')
def test_func2():
    print("*** test_func2 executed ***")

test_func2()
# => *** wrapped ***
# = *** test_func ***