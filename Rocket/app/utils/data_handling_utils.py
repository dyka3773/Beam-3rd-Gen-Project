import asyncio

from DataStorage import DataStorage

async def get_avg_temp() -> float | None:
    """Returns the average temperature of the two temperature sensors.
    
    Returns:
        float: The average temperature of the two temperature sensors.
    """    
    temp_list = await asyncio.gather(*[DataStorage().get_temperature_of_sensor(i) for i in range(1, 3)])
    
    if None in temp_list:
        return None
    
    return sum(temp_list) / len(temp_list) # type: ignore


async def get_avg_pressure() -> float | None:
    """Returns the average pressure of the two pressure sensors.
    
    Returns:
        float: The average pressure of the two pressure sensors.
    """
    pressure_list = await asyncio.gather(*[DataStorage().get_pressure_of_sensor(i) for i in range(1, 3)])
    
    if None in pressure_list:
        return None
    
    return sum(pressure_list) / len(pressure_list) # type: ignore