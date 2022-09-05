import asyncio
import multiprocessing
from multiprocessing.dummy import Process
import threading
import airsim
from lib.Drone import Drone


# client = airsim.MultirotorClient()
# client.confirmConnection()
# client.reset()
# client.confirmConnection()

# sp = [
#     [0, 0, -1],
#     [-0.75, 0.75, -1],
#     [0, 1.5, -1],
#     [0.75, 2.25, -1],
#     [1.5, 1.5, -1],
#     [2.25, 0.75, -1],
#     [1.5, 0, -1],
#     [-0.75, 0.75, -1],
# ]

# positions = []

# for i in range(1, 5):
#   positions += [
#       [x, y, -i] for x, y, _ in sp
#   ]


# trajectories = {
#     0: (positions)*10_000,
#     1: (positions[1:]+positions[:1])*10_000,
#     2: (positions[2:]+positions[:2])*10_000,
#     3: (positions[3:]+positions[:3])*10_000,
#     4: (positions[4:]+positions[:4])*10_000,
#     5: (positions[5:]+positions[:5])*10_000,
#     6: (positions[6:]+positions[:6])*10_000,
#     7: (positions[7:]+positions[:7])*10_000,
#     8: (positions[8:]+positions[:8])*10_000,
# }

trajectories = [
    [
        (0, 0, -1),
        (0, 0, -1),
        (0, 0, -2),
        (0, 0, -3),
        (0, 0, -4),
        (0, 0, -3),
        (0, 0, -2),
        (0, 0, -1),
        (0, 0, -1),
    ]*10_000,
    [
        (0, 1.5, -1),
        (0, 2,  -1),
        (0, 3,  -1),
        (0, 4,  -1),
        (0, 5,  -1),
        (0, 6,  -1),
        (0, 5,  -1),
        (0, 4,  -1),
        (0, 3,  -1),
        (0, 2,  -1),
        (0, 1.5, -1),
    ]*10_000,
    [
        (1.5, 0, -1),
        (2, 0, -1),
        (3, 0, -1),
        (4, 0, -1),
        (5, 0, -1),
        (6, 0, -1),
        (5, 0, -1),
        (4, 0, -1),
        (3, 0, -1),
        (2, 0, -1),
        (1.5, 0, -1),
    ]*10_000,
    [
        (-1.5, 0, -1),
        (-2, 0, -1),
        (-3, 0, -1),
        (-4, 0, -1),
        (-5, 0, -1),
        (-6, 0, -1),
        (-5, 0, -1),
        (-4, 0, -1),
        (-3, 0, -1),
        (-2, 0, -1),
        (-1.5, 0, -1),
    ]*10_000,
    [
        (0, -1.5, -1),
        (0, -2, -1),
        (0, -3, -1),
        (0, -4, -1),
        (0, -5, -1),
        (0, -6, -1),
        (0, -5, -1),
        (0, -4, -1),
        (0, -3, -1),
        (0, -2, -1),
        (0, -1.5, -1),
    ]*10_000,
    [
        (1.5, 1.5, -1),
        (2, 2, -1),
        (3, 3, -1),
        (4, 4, -1),
        (5, 5, -1),
        (6, 6, -1),
        (5, 5, -1),
        (4, 4, -1),
        (3, 3, -1),
        (2, 2, -1),
        (1.5, 1.5, -1),
    ]*10_000,
    [
        (1.5, -1.5, -1),
        (2, -2, -1),
        (3, -3, -1),
        (4, -4, -1),
        (5, -5, -1),
        (6, -6, -1),
        (5, -5, -1),
        (4, -4, -1),
        (3, -3, -1),
        (2, -2, -1),
        (1.5, -1.5, -1),
    ]*10_000,
    [
        (-1.5, 1.5, -1),
        (-2, 2,  -1),
        (-3, 3,  -1),
        (-4, 4,  -1),
        (-5, 5,  -1),
        (-6, 6,  -1),
        (-5, 5,  -1),
        (-4, 4,  -1),
        (-3, 3,  -1),
        (-2, 2,  -1),
        (-1.5, 1.5, -1),
    ]*10_000,
    [
        (-1.5, -1.5, -1),
        (-2, -2,  -1),
        (-3, -3,  -1),
        (-4, -4,  -1),
        (-5, -5,  -1),
        (-6, -6,  -1),
        (-5, -5,  -1),
        (-4, -4,  -1),
        (-3, -3,  -1),
        (-2, -2,  -1),
        (-1.5, -1.5, -1),
    ]*10_000,
]
# }

drones = [
    Drone("SimpleFlight", (0, 0, -1), trajectories[0]),
    Drone("Drone1", (0, 1.5, -1), trajectories[1]),
    Drone("Drone2", (1.5, 0, -1), trajectories[2]),
    Drone("Drone3", (-1.5, 0, -1), trajectories[3]),
    Drone("Drone4", (0, -1.5, -1), trajectories[4]),
    # Drone("Drone5", (1.5, 1.5, -1), trajectories[5]),
    # Drone("Drone6", (1.5, -1.5, -1), trajectories[6]),
    # Drone("Drone7", (-1.5, 1.5, -1), trajectories[7]),
    # Drone("Drone8", (-1.5, -1.5, -1), trajectories[8]),
]


# processes = [
#     Process(target=drone.start) for drone in drones
# ]
# airsim.wait_key('Press any key to start the dance')

# for process in processes:
#   process.start()

# for process in processes:
#   process.join()

threads = [
    threading.Thread(target=drone.start) for drone in drones
]
airsim.wait_key('Press any key to start the dance')

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()
