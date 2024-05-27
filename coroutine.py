import asyncio


async def fetch_data(delay):
  print(f'Starting fetching data with a delay of {delay} seconds')
  await asyncio.sleep(delay)
  print(f'Finished fetching data with a delay of {delay} seconds')
  return {'data': 100}


## coroutine function
async def main():
  print('Start of main coroutine')
  task = fetch_data(2);
  result = await task
  print(f'Result: {result}')
  print('End of main coroutine')




asyncio.run(main())