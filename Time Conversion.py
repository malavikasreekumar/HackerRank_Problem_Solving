time = raw_input().strip()
hh = time[0:2]
period = time[-2:]

if period=='AM':
    if hh=='12':
        newtime='00'+time[2:len(time)-2]
    else:
        newtime=time[0:len(time)-2]
elif period=='PM':
    if hh=='12':
        newtime=time[0:len(time)-2]
    else:
        newtime=str(int(hh) + 12)+ time[2:len(time)-2]
        
else:
    print("go")
print(newtime)
