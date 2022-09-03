import asyncio
import multiprocessing
import threading
import airsim
from lib.Drone import Drone
from concurrent.futures import ProcessPoolExecutor


client = airsim.MultirotorClient()
client.confirmConnection()
# client.reset()
# client.confirmConnection()


async def show_message():
  while True:
    await asyncio.sleep(1)
    print('API call is in progress...')


sp = [
    [0, 0, -1],
    [-0.75, 0.75, -1],
    [0, 1.5, -1],
    [0.75, 2.25, -1],
    [1.5, 1.5, -1],
    [2.25, 0.75, -1],
    [1.5, 0, -1],
    [-0.75, 0.75, -1],
]

positions = []

for i in range(1, 5):
  positions += [
      [x, y, -i] for x, y, _ in sp
  ]


trajectories = {
    0: (positions)*10_000,
    1: (positions[1:]+positions[:1])*10_000,
    2: (positions[2:]+positions[:2])*10_000,
    3: (positions[3:]+positions[:3])*10_000,
}

# for position in trajectories[2]:
#   print(position)

# print(trajectories)
# trajectories = {
#     0: [[-10, -10, -10]],
#     1: [[10, 10, -10]],
#     2: [[-10, 10, -10]],
#     3: [[10, -10, -10]],
# }

drones = [
    Drone("SimpleFlight", client, (0, 0, 0)),
    Drone("Drone1", client, (1.5, 1.5, 0)),
    Drone("Drone2", client, (0, 1.5, 0)),
    Drone("Drone3", client, (1.5, 0, 0)),
]


# async def main():
# for drone
#
#  in drones:
#   # airsim.wait_key('Press any key to start drone %s' % drone.name)
#   drone.start()

# airsim.wait_key('Press any key to set Trajectories')
# for idx, drone in enumerate(drones):
#   drone.trajectory = trajectories[idx]

# # mainTask = asyncio.create_task(show_message())

# tasks = []
# # for drone in drones:
# #   # airsim.wait_key(
# #   #     'Press any key to start Trajectory for drone %s' % drone.name)
# #   tasks.append(asyncio.create_task(drone.startTrajectory()))
# # thread = threading.Thread(target=drone.flyThread)
# # thread.start()

# executor = ProcessPoolExecutor(len(drones))
# loop = asyncio.get_event_loop()

# for drone in drones:
#   # await task

#   tasks += [loop.run_in_executor(executor, drone.startTrajectory)]

# loop.run_forever()
# for drone in drones:
#   drone.join()

# for drone in drones:
#   drone.stop()

# await mainTask

# while True:
#   for drone in drones:
#     try:
#       position = map(float, input(
#           "enter a new point for %s to go to : " % drone.name).split())
#       drone.addNewPosition(*position)
#     except:
#       print("Invalid input")

# asyncio.run(main())


for drone in drones:
  # airsim.wait_key('Press any key to start drone %s' % drone.name)
  drone.start()


# mainTask = asyncio.create_task(show_message())

tasks = []
# for drone in drones:
#   # airsim.wait_key(
#   #     'Press any key to start Trajectory for drone %s' % drone.name)
#   tasks.append(asyncio.create_task(drone.startTrajectory()))
# thread = threading.Thread(target=drone.flyThread)
# thread.start()

# executor = ProcessPoolExecutor(len(drones))

loop = asyncio.get_event_loop()

for drone in drones:

  # asyncio.async(drone.flyThread())

  tasks += [loop.create_task(drone.flyThread())]

  # await task

  # tasks += [loop.run_in_executor(executor, )]


airsim.wait_key('Press any key to set Trajectories')
for idx, drone in enumerate(drones):
  drone.trajectory = trajectories[idx]

loop.run_forever()
