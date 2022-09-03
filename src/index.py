import airsim

import numpy as np
import os
import tempfile
import pprint
import cv2

# connect to the AirSim simulator
client = airsim.MultirotorClient()
# client.reset()
pose = airsim.Pose(airsim.Vector3r(1, 0, 0))

client.confirmConnection()
client.simAddVehicle("SimpleFlight2",
                     "simpleflight",
                     pose)


client.enableApiControl(True, vehicle_name="SimpleFlight2")

state = client.getMultirotorState(vehicle_name="SimpleFlight2")

# s = pprint.pformat(state)
# print("state: %s" % s)


vehicles = client.listVehicles()
print("vehicles: %s" % vehicles)

# imu_data = client.getImuData()
# s = pprint.pformat(imu_data)
# print("imu_data: %s" % s)

# barometer_data = client.getBarometerData()
# s = pprint.pformat(barometer_data)
# print("barometer_data: %s" % s)

# magnetometer_data = client.getMagnetometerData()
# s = pprint.pformat(magnetometer_data)
# print("magnetometer_data: %s" % s)

# gps_data = client.getGpsData()
# s = pprint.pformat(gps_data)
# print("gps_data: %s" % s)

airsim.wait_key('Press any key to takeoff')
print("Taking off...")
client.armDisarm(True, vehicle_name="SimpleFlight2")
client.takeoffAsync(vehicle_name="SimpleFlight2").join()

state = client.getMultirotorState(vehicle_name="SimpleFlight2")
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to move vehicle to (-10, 10, -10) at 5 m/s')
client.moveToPositionAsync(-10, 10, -10, 5,
                           vehicle_name="SimpleFlight2").join()

airsim.wait_key('Press any key to hover')
client.hoverAsync(vehicle_name="SimpleFlight2").join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to reset to original state')

client.reset()
client.armDisarm(False, vehicle_name="SimpleFlight2")

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False, vehicle_name="SimpleFlight2")
