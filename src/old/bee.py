import asyncio


class Drone:
  def __init__(self, name, x, y, z) -> None:
    self.name = name
    self.x = x
    self.y = y
    self.z = z
    self.wayPoints = []

  async def init(self):
    print(self.name, "Ready")
    await self.takeOff()

  async def takeOff(self):
    print(self.name, "Taking off")
    await asyncio.sleep(1)
    print(self.name, "Airborne")
    return

  def takeWayPoints(self, givenWayPoints):
    self.wayPoints += givenWayPoints

  async def flyToWayPoints(self):
    if not len(self.wayPoints):
      print("No more wayPoints")
      return

    wayPoint, *self.wayPoints = self.wayPoints

    print(self.name, "Flying to ", wayPoint)

    await asyncio.sleep(5)

    self.x, self.y, self.z = wayPoint

    print(self.name, "Got to ", *wayPoint)

    await self.flyToWayPoints()


async def main():
  print('run main')

  wayPoints = [
      [1, 1, 1],
      [2, 2, 2],
      [3, 3, 3],
  ]

  myDrone = Drone("drone1", 0, 0, 0)
  myDrone.takeWayPoints(wayPoints)

  await myDrone.init()
  # create a task (its like create the promise)
  # the task is to fly to way points
  task = asyncio.create_task(
      myDrone.flyToWayPoints()
  )
  await asyncio.sleep(1)
  myDrone.takeWayPoints([[4, 4, 4]])

  # dont finish execution of the main function
  # until the task is done (no more points to go to)
  await task


asyncio.run(main())

# pending = asyncio.all_tasks()
# asyncio.loop.run_until_complete(asyncio.gather(*pending))
