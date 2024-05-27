import asyncio


async def fetch_data(delay):
  print(f'Starting fetching data with a delay of {delay} seconds')
  await asyncio.sleep(delay)
  print(f'Finished fetching data with a delay of {delay} seconds')
  return {'data': 100}


## coroutine function
async def main():
  task1 = fetch_data(2)
  task2 = fetch_data(3)
  result1 = await task1
  print(f"Task 1 result: {result1}")
  result2 = await task2
  print(f"Task 2 result: {result2}")
  




asyncio.run(main())