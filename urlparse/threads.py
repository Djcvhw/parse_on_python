#!/usr/bin/env python
import asyncio
import websockets
import datetime
import time
import requests
from bs4 import BeautifulSoup
from urlparse.models import Url, Info

@asyncio.coroutine
def parse():
    websocket = yield from websockets.connect('ws://localhost:5237/parse/')

    def seconds(s):
        l = s.split(':')
        return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

    urls = Url.objects.all().values_list('url', flat=True)

    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
        }

    def html_escape(text):
        """Produce entities within text."""
        return "".join(html_escape_table.get(c,c) for c in text)

    for url in urls:
        sleep = Url.objects.get(url=url)
        sec = seconds(str(sleep.timeshift))
        time.sleep( sec )
        html = requests.get('http://'+url)
        soup = BeautifulSoup(html.text, 'html.parser')
        if soup.h1:
            h = html_escape(soup.h1)
        else:
            h = ""

        if html.ok:
            result = '{"url" : "'+url+'","title" : "'+soup.title.string+'", "encoding" : "'+html.encoding+'", "h1" : "'+str(h)+'", "time" : "'+str(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time())))+'", "status": "ok"}'
        else:
            result = '{"url" : "'+url+'", "time" : "'+str(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time())))+'", "status": "fail"}'

        q = Info(url=url, title=soup.title.string, encoding=html.encoding, h1=h)
        q.save()
        yield from websocket.send(result)

    yield from websocket.close()

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop_main = asyncio.get_event_loop()
    loop_main.run_until_complete(parse())

if __name__ == '__main__':
    main()