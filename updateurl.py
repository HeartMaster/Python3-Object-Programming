from threading import Timer
import datetime
from urllib.request import urlopen

class UpdateURL:
    def __init__(self,url):
        self.contents =''
        self.url = url
        self.last_updated =None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600,self.update())
        # 设置守护线程
        self.timer.setDaemon(True)
        self.timer.start()

u  = UpdateURL("http://news.yahoo.com/")