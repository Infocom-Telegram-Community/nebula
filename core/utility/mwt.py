import time
#CKASS MWT FOR AUTOMATIC ADMIN ONLY COMMAND
class MWT(object):
    _caches = {}
    _timeouts = {}

    def __init__(self,timeout=2):
        self.timeout = timeout

    def collect(self):
        for func in self._caches:
            cache = {}
            for key in self._caches[func]:
                if (time.time() - self._caches[func][key][1]) < self._timeouts[func]:
                    cache[key] = self._caches[func][key]
            self._caches[func] = cache

    def __call__(self, f):
        self.cache = self._caches[f] = {}
        self._timeouts[f] = self.timeout

        def func(*args, **kwargs):
            kw = sorted(kwargs.items())
            key = (args, tuple(kw))
            try:
                v = self.cache[key]
                print("cache=>user")
                if (time.time() - v[1]) > self.timeout:
                    raise KeyError
            except KeyError:
                print("new=>admin")
                v = self.cache[key] = f(*args,**kwargs),time.time()
            return v[0]
        func.func_name = f.__name__

        return func

@MWT(timeout=1*1)
def get_admin_ids(bot, chat_id):
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]