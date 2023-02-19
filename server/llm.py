# GET CURRENT DATETIME

def get_current_datetime():
    from datetime import datetime
    import time
    current_timestamp = datetime.now()
    current_timestamp = int(time.mktime(current_timestamp.timetuple()))
    return current_timestamp