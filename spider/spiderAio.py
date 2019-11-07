import aiohttp
import asyncio
import json
import numpy as np

with open("hds.json", "r") as fp:
    hds = json.load(fp)

tasks = []
async def getWebPage(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers = hds[np.random.randint(3)]) as response:
            result = await response.read()
            #print(result.decode("utf-8"))
            return result

def getAllWebPage(urls):
    loop = asyncio.get_event_loop()
    for i in range(len(urls)):
        task = asyncio.ensure_future(getWebPage(urls[i]))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    return result

if __name__ == '__main__':
    res = getAllWebPage(["https://www.baidu.com"])
    #res = getWebPage("http://www.baidu.com")
    print(res[0].decode('utf-8'))

