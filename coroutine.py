import asyncio


async def fetch_data(id, delay):
  print(f"Coroutine started for id: {id}")
  await asyncio.sleep(delay)
  return {"id": id, "title": f"Title for {id}"}


## coroutine function
async def main():
  results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

  for result in results:
    print(f"Result: {result}")







asyncio.run(main())