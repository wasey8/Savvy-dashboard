from functions.database import db

def users():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december


#-------------------------------sellers-----------------------------------------------------------------#

def sellers():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december





#-------------------------------buyers-----------------------------------------------------------------#

def buyers():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december








#-------------------------------blockedjobs-----------------------------------------------------------------#

def blockedjobs():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december












#-------------------------------totalgigs-----------------------------------------------------------------#

def totalgigs():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december











#-------------------------------gigspurchased-----------------------------------------------------------------#

def gigspurchased():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december















#-------------------------------------active 1 day users-----------------------------------------------------------#

def activedayusers():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december







#-------------------------------unprocessed payments-----------------------------------------------------------------#

def unprocessedpayments():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december


#-------------------------------daily active users-----------------------------------------------------------------#

def dailyac():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december



#-----------------------------active jobs-----------------------------------------------------------------#

def activejobs():
    MonthJan=[]
    MonthFeb=[]
    MonthMar=[]
    MonthApr=[]
    MonthMay=[]
    MonthJun=[]
    MonthJul=[]
    MonthAug=[]
    MonthSep=[]
    MonthOct=[]
    MonthNov=[]
    MonthDec=[]
    jan=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":1}).fetchall()
    feb=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":2}).fetchall()
    mar=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":3}).fetchall()
    apr=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":4}).fetchall()
    may=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":5}).fetchall()
    jun=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":6}).fetchall()
    jul=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":7}).fetchall()
    aug=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":8}).fetchall()
    sep=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":9}).fetchall()
    oct=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":10}).fetchall()
    nov=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":11}).fetchall()
    dec=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":12}).fetchall()
    for i in jan:
        MonthJan.append(i[0])
    for i in feb:
        MonthFeb.append(i[0])
    for i in mar:
        MonthMar.append(i[0])
    for i in apr:
        MonthApr.append(i[0])
    for i in may:
        MonthMay.append(i[0])
    for i in jun:
        MonthJun.append(i[0])
    for i in jul:
        MonthJul.append(i[0])
    for i in aug:
        MonthAug.append(i[0])
    for i in sep:
        MonthSep.append(i[0])
    for i in oct:
        MonthOct.append(i[0])
    for i in nov:
        MonthNov.append(i[0])
    for i in dec:
        MonthDec.append(i[0])

    if not MonthJan:
        MonthJan=0
        january=MonthJan
    else: 
        january=MonthNov[-1]-MonthNov[0]


    if not MonthFeb:
        MonthFeb=0
        february=MonthFeb

    else:
        february=MonthFeb[-1]-MonthFeb[0]

    if not MonthMar:
        MonthMar=0
        march=MonthMar
    else: 
        march=MonthMar[-1]-MonthMar[0]


    if not MonthApr:
        MonthApr=0
        april=MonthApr

    else:
        april=MonthApr[-1]-MonthApr[0]

    if not MonthMay:
        MonthMay=0
        may=MonthMay
    else: 
        may=MonthMay[-1]-MonthMay[0]


    if not MonthJun:
        MonthJun=0
        june=MonthJun

    else:
        june=MonthJun[-1]-MonthJun[0]

    if not MonthJul:
        MonthJul=0
        july=MonthJul
    else: 
        july=MonthJul[-1]-MonthJul[0]


    if not MonthAug:
        MonthAug=0
        august=MonthAug

    else:
        august=MonthAug[-1]-MonthAug[0]

    if not MonthSep:
        MonthSep=0
        september=MonthSep
    else: 
        september=MonthSep[-1]-MonthSep[0]


    if not MonthOct:
        MonthOct=0
        october=MonthOct

    else:
        october=MonthOct[-1]-MonthOct[0]

    if not MonthDec:
        MonthDec=0
        december=MonthDec
    else: 
        december=MonthDec[-1]-MonthDec[0]


    if not MonthNov:
        MonthNov=0
        november=MonthNov

    else:
        november=MonthNov[-1]-MonthNov[0]

    return january,february,march,april,may,june,july,august,september,october,november,december
