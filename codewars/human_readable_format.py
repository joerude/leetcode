# https://www.codewars.com/kata/52742f58faf5485cae000b9a

# Human readable duration format


import codewars_test as test


def format_duration(seconds):
    d = {'years': seconds // (3600 * 24 * 365),
         'days': (seconds // (3600 * 24) % 365), 
         'hours': (seconds // 3600) % 24,
         'minutes': (seconds // 60) % 60,
         'seconds': seconds % 60}
    
    if seconds == 0: return 'now'
    
    data = []
    for k, v in d.items():
        if v > 0:
            if v == 1:
                data.append([str(v), k[:-1]])
            else:
                data.append([str(v), k])
    ans = ''
    for i in data:
        if len(data) == 1:
            ans += ' '.join(data.pop())
        elif len(data) == 2:
            continue
        else:
            ans += ' '.join(data.pop(0))+', '

    
    if data: 
        ans+= ' '.join(data.pop(0)) + ' and ' + ' '.join(data.pop())
    else: pass
    
    return ans 



test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")