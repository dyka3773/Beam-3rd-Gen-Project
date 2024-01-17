import asyncio
import numpy as np
import logging

from DataStorage import DataStorage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
)

logging.captureWarnings(True)


async def get_avg_temp_of_sensors() -> tuple[float, float]:
    """Returns the average temperature of the two temperature sensors.

    Returns:
        float: The average temperature of the two temperature sensors.
    """
    temp0_list, temp1_list = await asyncio.gather(*[DataStorage().get_temp_of_sensor_for_the_last_x_secs(i) for i in range(1, 3)])

    return np.average(temp0_list), np.average(temp1_list)
