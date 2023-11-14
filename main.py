import aiohttp
import asyncio 

class NGL():
    def __init__(self, username: str, question: str):
        self.url  = "https://ngl.link/api/submit"
        self.headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36"
        }
        
        self.body = {
            "username": username,
            "question": question,
            "deviceId": "534252"
        }

    async def start(self: "NGL"):
        while True:
            try:
                connector = aiohttp.TCPConnector(limit=1)
                async with aiohttp.ClientSession(connector=connector, headers=self.headers) as cs:
                    async with cs.post(self.url, json=self.body) as r:
                        print(r.status)
            except: 
                print("unknown")

async def main():
    username: str = input("username: ")
    question: str = input("question: ")
    s = NGL(username, question)
    await asyncio.gather(*[s.start() for _ in range(100)])

if __name__ == "__main__":
    asyncio.run(main())
