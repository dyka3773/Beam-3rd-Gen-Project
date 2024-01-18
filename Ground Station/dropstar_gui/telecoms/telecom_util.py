import sqlite3 as sql
from typing import Any, Tuple


def coalesce_data(data: Tuple, previous_row_values: Tuple) -> Tuple:
    """Coalesces the data with the previous non-null values.

    Args:
        data (Tuple): The data to be coalesced.
        previous_row_values (Tuple): The previous non-null values.

    Returns:
        Tuple: The coalesced data.
    """
    def coalesce(x, y):
        return x if x is not None else y

    if len(previous_row_values) != len(data):
        raise ValueError(
            f"The length of the previous row values ({len(previous_row_values)}) is different from the length of the data ({len(data)}).")

    return tuple(map(coalesce, data, previous_row_values))


def get_previous_row_values(cursor: sql.Cursor) -> Tuple:
    """Gets values of the previous row.

    Args:
        cursor (sql.Cursor): The cursor to the database.

    Returns:
        Tuple: The values of the previous row.
    """
    cursor.execute('''
        SELECT * FROM GS_DATA
        ORDER BY time DESC
        LIMIT 1
    ''')
    previous_row = cursor.fetchone()

    if previous_row is None:
        return ()

    return previous_row
