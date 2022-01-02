# https://www.codewars.com/kata/52685f7382004e774f0001f7

# Human Readable Time

def make_readable(seconds):
    # Do something
    minutes = seconds // 60
    seconds %= 60    
    
    hours = minutes // 60
    minutes %= 60
    
    seconds = '0' + str(seconds) if seconds <= 9 else seconds
    minutes = '0' + str(minutes) if minutes <= 9 else minutes
    hours = '0' + str(hours) if hours < 9 else hours

    
#     return hours, minutes, seconds
    return f'{hours}:{minutes}:{seconds}'