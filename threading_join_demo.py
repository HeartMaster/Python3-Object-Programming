from threading import Thread
import json
from urllib.request import urlopen
import time

CITES = [
    'Edmonton','Victoria','Winnipeg''Fredericton',"St. John's",'Halifax','Toronto','Charlottetown','Quebec City','Regina'
]
class TempGetter(Thread):
    def __init__(self,city):
        super().__init__()
        self.city =city

    def run(self):
        url_template = ('http://www.baidu.com')
        self.response = urlopen(url_template.format(self.city))

threads = [TempGetter(c) for c in CITES]
start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print('it is{0.response}'.format(thread))

print(time.time()-start)

