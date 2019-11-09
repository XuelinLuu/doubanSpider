'''
通过aiohttp和asyncio进行数据爬取
'''


import aiohttp
import asyncio
import json
import numpy as np
import os

with open("hds.json", "r") as fp:
    hds = json.load(fp)


async def getWebPage(url):
    async with aiohttp.ClientSession() as session:
        try_loop = 0
        while True:
            if try_loop == 10:
                return ""
            try_loop += 1
            try:
                async with session.get(url, headers = hds[np.random.randint(3)]) as response:
                    result = await response.read()
                    #print(result.decode("utf-8"))
                    return result.decode("utf-8")
            except:
                print("get page False, time {0}, loading....".format(try_loop))
                continue


def getAllWebPage(urls):
    tasks = []
    loop = asyncio.get_event_loop()
    for i in range(len(urls)):
        task = asyncio.ensure_future(getWebPage(urls[i]))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    return result

if __name__ == '__main__':
    res = getAllWebPage(["https://www.baidu.com"])
    #res = getWebPage("http://www.baidu.com")
    print(res[0])
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" * 10)

