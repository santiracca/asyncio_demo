import asyncio


async def fetch_data(id, delay):
  print(f"Coroutine started for id: {id}")
  await asyncio.sleep(delay)
  return {"id": id, "title": f"Title for {id}"}


## coroutine function
async def main():
  tasks = []

  async with asyncio.TaskGroup() as tg:
    for i, sleep_time in enumerate([2,1,3], start=1):
      task = tg.create_task(fetch_data(i, sleep_time))
      tasks.append(task)

  results = [task.result() for task in tasks]

  for result in results:
    print(f"Result: {result}")







asyncio.run(main())