# import time for wait and icm20948 for imu lib
import time
from icm20948 import ICM20948


# i2c at addr 69 --> used sudo i2cdetect -y 1 to find values
# if it is at 68 no change needs to be made
imu = ICM20948(i2c_addr=0x69)

# read imu data and store in params
while True:
    x, y, z = imu.read_magnetometer_data()
    ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()

    # display params
    print("""
Accel: {:05.2f} {:05.2f} {:05.2f}
Gyro:  {:05.2f} {:05.2f} {:05.2f}
Mag:   {:05.2f} {:05.2f} {:05.2f}""".format(
        ax, ay, az, gx, gy, gz, x, y, z
    ))

    # wait
    time.sleep(0.25)
