import datetime

def get_moment():
    """returns a string that represents the moment of the day associated with an hour interval"""
    
    now = datetime.datetime.now()
    hour = int(now.strftime('%H'))

    if(hour >= 5 and hour <= 11):
        return "morning"
    elif(hour >= 12 and hour <= 17):
        return "afternoon"
    elif(hour > 17 and hour <= 21):
        return "evening"
    else:
        return "night"