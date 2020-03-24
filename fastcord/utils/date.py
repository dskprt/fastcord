from datetime import datetime

def from_iso8601(date):
    return datetime.fromisoformat(date)

def to_iso8601(year, month, day, hour, minute, second):
    return datetime(year, month, day, hour,
        minute, second, 0).isoformat()
