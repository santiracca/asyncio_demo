import asyncio


async def fetch_data(id, delay):
  print(f"Coroutine started for id: {id}")
  await asyncio.sleep(delay)
  return {"id": id, "title": f"Title for {id}"}


## coroutine function
async def main():
  task1 = asyncio.create_task(fetch_data(1, 2))
  task2 = asyncio.create_task(fetch_data(2, 1))
  task3 = asyncio.create_task(fetch_data(3, 3))

  result1 = await task1
  result2 = await task2
  result3 = await task3


  print(result1, result2, result3)





asyncio.run(main())