import airsim
from typing import List
import asyncio
# import multiprocessing
import time

# multiprocessing.set_start_method('spawn')


class Drone:
  def __init__(
      self,
      name,
      initialPosition: List[float],
      trajectory: List[List[float]] = [],
  ) -> None:
    self.name = name

    self.client = airsim.MultirotorClient()
    self.client.confirmConnection()

    self.trajectory = trajectory
    self.velocity = 4

    if self.name not in self.client.listVehicles():
      self.client.simAddVehicle(
          self.name,
          "simpleflight",
          airsim.Pose(airsim.Vector3r(*initialPosition))
      )

    self.flyingThread = None
    self.stopThread = False
    self.hovering = True

    self.client.enableApiControl(True, vehicle_name=self.name)
    self.client.armDisarm(True, vehicle_name=self.name)
    self.takeOff()

  def start(self):
    print("Starting drone %s" % self.name)
    self.flyThread()

  # async def startTrajectory(self):

  #   print("Starting trajectory for drone %s" % self.name)
  #   await self.flyThread()
    # self.flyThread = multiprocessing.Process(target=self.flyThread)
    # self.flyThread.start()

    # self.flyingThread = threading.Thread(target=self.flyThread)
    # self.flyingThread.start()
    # process = multiprocessing.Process(target=self.flyThread)
    # process.start()

  def stop(self):
    self.stopThread = True
    self.client.armDisarm(False, vehicle_name=self.name)
    self.client.reset()
    self.client.enableApiControl(False, vehicle_name=self.name)

  def join(self):
    if self.flyingThread:
      self.flyingThread.join()

  def flyThread(self):

    while not self.stopThread:
      if len(self.trajectory):
        self.flyToNextPoint()
      else:
        self.hover()
      time.sleep(0.1)
    # if len(self.trajectory) > 0:
    #   self.hovering = False
    #   self.flyToNextPoint()
    # self.client.hoverAsync(vehicle_name=self.name).join()
    # if len(self.trajectory) > 0:
    #   await self.flyThread()
    # else:
    #   self.hovering = True

  def addNewPosition(self, x, y, z):
    self.trajectory.append((x, y, z))
    # if self.hovering:
    #   asyncio.run(
    #       self.flyThread()
    #   )

  def updateVelocity(self, newVelocity: float):
    self.velocity = newVelocity

  def takeOff(self):
    self.client.takeoffAsync(vehicle_name=self.name)

  def flyToNextPoint(self):
    if not len(self.trajectory):
      return
    position = self.trajectory.pop(0)
    print("Flying %s to %s" % (self.name, position))
    self.client.moveToPositionAsync(
        *position,
        self.velocity,
        vehicle_name=self.name
    ).join()
