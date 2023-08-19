import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s', 
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

def stop_motor_at_the_edge_of_the_cell():
    """Stops the motor at the edge of the cell."""
    raise NotImplementedError('This function is not implemented yet.')