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
        data[0] if data[0] is not None else None,
        int(data[1]) if data[1] is not None else None,
        int(data[2]) if data[2] is not None else None,
        int(data[3]) if data[3] is not None else None,
        float(data[4]) if data[4] is not None else None,
        float(data[5]) if data[5] is not None else None,
        float(data[6]) if data[6] is not None else None,
        format_signals(data[7]) if data[7] is not None else None,
        format_signals(data[8]) if data[8] is not None else None,
        format_signals(data[9]) if data[9] is not None else None,
        int(data[10]) if data[10] is not None else None,
        int(data[11]) if data[11] is not None else None,
    )
