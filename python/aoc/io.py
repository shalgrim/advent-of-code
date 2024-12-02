import sys
from functools import wraps
from pathlib import Path


def with_calling_file_context(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        frame = sys._getframe(1)
        filepath = frame.f_code.co_filename
        return func(filepath, *args, **kwargs)

    return wrapper


@with_calling_file_context
def this_year_day(filepath: str, pad_day: bool = False):
    p = Path(filepath)
    year = int(p.parts[-2][1:])
    day = int(p.parts[-1].split("_")[0][-2:])
    if pad_day:
        return year, f"{day:02d}"
    return year, day
