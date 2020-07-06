from datetime import datetime


def hello1():
    dt1 = datetime.now()
    dt2 = datetime.fromtimestamp(dt1.timestamp() / 1000)
    print(dt1)
    print(dt2)
    print(dt1.timestamp() * 1000)


EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000


def filetime_to_dt(ft):
    """Converts a Microsoft filetime number to a Python datetime. The new datetime object is time zone-naive but is equivalent to tzinfo=utc.

     >>> filetime_to_dt(116444736000000000)
     datetime.datetime(1970, 1, 1, 0, 0)
    """
    # Get seconds and remainder in terms of Unix epoch
    (s, ns100) = divmod(ft - EPOCH_AS_FILETIME, HUNDREDS_OF_NANOSECONDS)
    # Convert to datetime object
    dt = datetime.utcfromtimestamp(s)
    # Add remainder in as microseconds. Python 3.2 requires an integer
    dt = dt.replace(microsecond=(ns100 // 10))
    return dt


if __name__ == '__main__':
    hello1()
