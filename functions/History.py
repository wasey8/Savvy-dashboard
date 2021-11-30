from functions.database import db

#--------------------Last 30 days data users--------------------------------#
def SevenDays():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM users ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    sevenDays=data[-1]-data[0]
    return sevenDays

def thirtyDays():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM users ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    thirtyDays=data[-1]-data[0]
    return thirtyDays

#--------------------Last 30 days data sellers--------------------------------#


def SevenDaysSellers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM sellers ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    sevenDays=data[-1]-data[0]
    return sevenDays

def thirtyDaysSellers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM sellers ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    thirtyDays=data[-1]-data[0]
    return thirtyDays


#--------------------Last 30 days data buyers--------------------------------#

def SevenDaysBuyers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM buyers ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    sevenDays=data[-1]-data[0]
    return sevenDays

def thirtyDaysBuyers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM buyers ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    thirtyDays=data[-1]-data[0]
    return thirtyDays


#--------------------Last 30 days data active jobs--------------------------------#

def SevenDaysActiveJobs():
    data=[]
    countCheck=db.execute("SELECT count FROM activejobs ORDER BY date asc LIMIT 7").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[1]-data[0]
        if sevenDays<0:
            sevenDays=0
            return sevenDays


    except IndexError:
        sevenDays=0
    return sevenDays

def thirtyDaysActiveJobs():
    data=[]
    countCheck=db.execute("SELECT count FROM activejobs ORDER BY date asc LIMIT 30").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
        if thirtyDays<0:
            thirtyDays=0
        return thirtyDays

    except IndexError:
        thirtyDays=0
    return thirtyDays


#--------------------Last 30 days data blocked jobs--------------------------------#

def SevenDaysBlockedJobs():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM blockedjobs ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysBlockedJobs():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM blockedjobs ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays

#--------------------Last 30,7 days data total gigs--------------------------------#

def SevenDaysTotalGigs():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM totalgigs ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysTotalGigs():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM totalgigs ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays

#--------------------Last 30,7 days data purchased gigs--------------------------------#

def SevenDaysPurchasedGigs():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM gigspurchased ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysPurchasedGigs():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM gigspurchased ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays

#--------------------Last 30,7 days data active day users gigs--------------------------------#

def SevenDaysactiveusers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM activedayusers ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysactiveusers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM activedayusers ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays

#--------------------Last 30,7 days data active day users gigs--------------------------------#

def SevenDaysUnprocessedPayments():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM unprocessedpayments ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysUnprocessedPayments():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM unprocessedpayments ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays


#--------------------Last 30,7 days data crash free users gigs--------------------------------#

def SevenDaysCrashFreeUsers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM crashfree ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysCrashFreeUsers():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM crashfree ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays


#--------------------Last 30,7 days data average transaction value  gigs--------------------------------#

def SevenDaysAverageValue():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM averagevalue ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysAverageValue():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM averagevalue ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays

#--------------------Last 30,7 days data of dau--------------------------------#


def SevenDaysDau():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM dau ORDER BY date DESC LIMIT 7) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        sevenDays=data[-1]-data[0]
    except IndexError:
        sevenDays=0    
    return sevenDays

def thirtyDaysDau():
    data=[]
    countCheck=db.execute("SELECT count FROM (SELECT count FROM dau ORDER BY date DESC LIMIT 30) sub ORDER BY count ASC").fetchall()
    for i in countCheck:
        data.append(i[0])
    try:
        thirtyDays=data[-1]-data[0]
    except IndexError:
        thirtyDays=0
    return thirtyDays