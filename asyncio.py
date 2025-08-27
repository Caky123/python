import time
import asyncio

async def stahni_data(url):
    print(f"Stahuji: {url}")
    await asyncio.sleep(2)
    print(f"Hotovo: {url}")

async def main():
    await asyncio.gather(
        stahni_data("https://example.com/1"),
        stahni_data("https://example.com/2")
    )
    

start_time = time.time()

asyncio.run(main())

end_time = time.time()

print(f"Run time: {end_time - start_time} sec")
