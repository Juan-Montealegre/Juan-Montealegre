def validate_username(username):
    if not username or len(username) < 3:
        return False
    return True

def validate_password(password):
    if not password or len(password) < 6:
        return False
    return True

def format_date(date):
    return date.strftime("%Y-%m-%d")

def format_time(time):
    return time.strftime("%H:%M:%S")