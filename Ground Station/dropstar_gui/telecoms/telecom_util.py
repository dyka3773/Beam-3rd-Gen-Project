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


def format_data(data: Tuple) -> Tuple:
    """Formats the data into their proper type.

    Args:
        data (Tuple): The data to be formatted.

    Returns:
        Tuple: The formatted data.
    """
    def format_signals(x):
        if x is None:
            return x
        if x == 0 or x == '0':
            return False
        if x == 1 or x == '1':
            return True
        return x

    return (
        data[0],
        int(data[1]),
        int(data[2]),
        int(data[3]),
        float(data[4]),
        float(data[5]),
        float(data[6]),
        format_signals(data[7]),
        format_signals(data[8]),
        format_signals(data[9]),
        int(data[10]),
        int(data[11]),
    )
