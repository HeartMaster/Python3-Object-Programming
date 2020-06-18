class Color:
    def __init__(self,rgb_value,name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self,name):
        if not name:
            raise Exception('Invalid Name')
        self._name = name

    def _get_name(self):
        return self._name

    name1 = property(_get_name,_set_name)


class Silly:
    def _get_silly(self):
        print('You are getting silly')
        return self._silly

    def _set_silly(self,value):
        print('You are making silly {}'.format(value))
        self._silly = value

    def _del_silly(self):
        print('Whoah,you killed silly')
        del self._silly

    silly = property(_get_silly,_set_silly,_del_silly,'This is a silly property')


class Silly:
    @property
    def silly(self):
        return self._silly

    @silly.setter
    def silly(self,value):
        self._silly = value

    @silly.deleter
    def silly(self):
        del self._silly


from urllib.request import urlopen


class WebPage:
    def __init__(self,url):
        self.url =url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print('Retrieving New Page...')
            self._content = urlopen(self.url).read()
        return self._content


class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)
