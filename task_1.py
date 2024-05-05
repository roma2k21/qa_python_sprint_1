s = '1h 45m,360s,25m,30m 120s,2h 60s'
s = s.replace(',', ' ')
string = s.split()
res = 0
# replaced_sumbols = ['h', 'm', 's']
for time in string:
    if 'h' in time:
        time = time.replace('h', '')
        time = int(time) * 60
        res = res + time
    elif 'm' in time:
        time = time.replace('m', '')
        res = res + int(time)
    elif 's' in time:
        time = time.replace('s', '')
        time = int(time) // 60
        res = res + time
print(res)