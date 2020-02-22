class Chain(object):
    def __init__(self, path = ''):
        self.__path = path
    def __str__(self):
        return self.__path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))
    __repr__ = __str__

my_home = Chain('https://my_home.server')
print(my_home)
print(my_home.usr.video.info)
