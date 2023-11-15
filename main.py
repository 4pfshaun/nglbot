import uuid
import aiohttp
import asyncio 

from typing import Optional

class NGL():
    def __init__(self, username: str, question: str, proxy: Optional[str]=None):
        self.url  = "https://ngl.link/api/submit"
        self.proxy = proxy

        self.headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36"
        }
        
        self.body = {
            "username": username,
            "question": question,
        }

    async def start(self: "NGL"):
        while True:
            try:
                self.body['deviceId'] = uuid.uuid4().__str__()
                connector = aiohttp.TCPConnector(limit=1)
                async with aiohttp.ClientSession(connector=connector, headers=self.headers) as cs:
                    async with cs.post(self.url, json=self.body, proxy=self.proxy) as r:
                        print(r.status)
            except Exception as e: 
                print(e.__str__())

async def main():
    username: str = input("username: ")
    question: str = input("question: ")
    s = NGL(username, question)
    await asyncio.gather(*[s.start() for _ in range(100)])

if __name__ == "__main__":
    asyncio.run(main())