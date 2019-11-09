import spider.spiderAio as sio
import urllib
url1 = 'http://www.douban.com/tag/' + urllib.request.quote("科技") + "/book?start=" + str(0)
url2 = 'http://www.douban.com/tag/' + urllib.request.quote("育儿") + "/book?start=" + str(0)


res1 = sio.getAllWebPage([url1])
res2 = sio.getAllWebPage([url2])

print(res1)
print(res2)

