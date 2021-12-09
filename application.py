from flask import  Flask,render_template,flash,session,Response,send_file,stream_with_context
from flask.globals import request
from flask.helpers import flash, url_for
import asyncio
import csv
import requests
import os
from datetime import datetime
from werkzeug.utils import redirect
from flask_session import Session
from datetime import datetime
from functions.calender import check
from functions.Savvyapis import get_all_urls
from functions.website import get_all_urls_web
from functions.database import db
import pytz
from functions.History import SevenDays, SevenDaysPurchasedGigs,thirtyDays,SevenDaysSellers, thirtyDaysPurchasedGigs,thirtyDaysSellers,SevenDaysBuyers,thirtyDaysBuyers,SevenDaysActiveJobs,thirtyDaysActiveJobs,SevenDaysBlockedJobs,thirtyDaysBlockedJobs,SevenDaysTotalGigs,thirtyDaysTotalGigs,SevenDaysactiveusers,thirtyDaysactiveusers,SevenDaysCrashFreeUsers,thirtyDaysCrashFreeUsers,SevenDaysAverageValue,thirtyDaysAverageValue,SevenDaysUnprocessedPayments,thirtyDaysUnprocessedPayments,SevenDaysDau,thirtyDaysDau
from functions.googleA import sample_run_report,sample_run_report_crash,sample_run_report_lastDay




# # -------------------GA credentials---------------------------------#
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="GA_file/savvyapi-10ebd6df9ae1.json"
# -------------Initializing-------------------------------------------#

app=Flask(__name__)
app.secret_key="wasey1238883jchsd"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



#------------Today's date--------------------------------------------#
date=datetime.date(datetime.now(pytz.timezone("Asia/Karachi")))


#-----------------Real time--------------------------------#
@app.route('/time_feed')
def time_feed():
    def generate():
        yield datetime.now().strftime("%d.%m.%Y %H:%M:%S") 
    return Response(generate(), mimetype='text') 


#----------------Real time active app users----------------#
@app.route('/active_users')
def active_users():
    def generate():
        a=sample_run_report(294104009)
        yield a
    return Response(generate()) 



#----------------Getting dau's----------------#
@app.route('/dau')
def dau():
    def generate():
        dbDAte=[]
        try:
            a=requests.get("http://127.0.0.1:5001/firebase")
            a=a.json()
            a=a['dau']
            dateCheck=db.execute("SELECT * FROM dau").fetchall()
            for i in dateCheck:
                dbDAte.append(i[0])

            if date not in dbDAte :
                db.execute("INSERT INTO dau(date,count) VALUES (:date,:count)",{"date":date,"count":a})
                db.commit()

            elif date in dbDAte:
                db.execute("UPDATE dau set count=:count where date=:date",{"count":a,"date":date})
                db.commit()

        except Exception:
            a=db.execute("SELECT count FROM dau  order by date desc limit 1").fetchone()        
        yield str(a[0])
    return Response(generate()) 


#-----------------Update data--------------------------------#
@app.route('/update_data')
def updata_data():
    def generate():
        dbDAte=[]
        urls = asyncio.run(get_all_urls())
        users=urls[0]
        buyers=urls[1]
        sellers=urls[2]
        activejobs=urls[3]
        blockedjobs=urls[4]
        totalGigs=urls[5]
        purchasedGigs=urls[6]

        #------Website data--------#
        data=asyncio.run(get_all_urls_web())
        countTranscation=data[0]
        sumTranscation=data[1]
        averageTransaction=float(sumTranscation)/int(countTranscation)
        averageTransaction="{:.2f}".format(averageTransaction)

        #------App data-------------#
        crash=sample_run_report_crash(294104009)
        app_users=sample_run_report(294104009)
        last_day=sample_run_report_lastDay(294104009)
        crash=(crash/1)*100




        dateCheck=db.execute("SELECT * FROM users").fetchall()
       

        for i in dateCheck:
            dbDAte.append(i[0])
            
        print(date)

        if date not in dbDAte :
            db.execute("INSERT INTO users(date,count) VALUES (:date,:count)",{"date":date,"count":users})
            db.commit()
            db.execute("INSERT INTO sellers(date,count) VALUES (:date,:count)",{"date":date,"count":sellers})
            db.commit() 
            db.execute("INSERT INTO buyers(date,count) VALUES (:date,:count)",{"date":date,"count":buyers})
            db.commit()
            db.execute("INSERT INTO activejobs(date,count) VALUES (:date,:count)",{"date":date,"count":activejobs})
            db.commit()
            db.execute("INSERT INTO blockedjobs(date,count) VALUES (:date,:count)",{"date":date,"count":blockedjobs})
            db.commit()
            db.execute("INSERT INTO totalgigs(date,count) VALUES (:date,:count)",{"date":date,"count":totalGigs})
            db.commit()
            db.execute("INSERT INTO gigspurchased(date,count) VALUES (:date,:count)",{"date":date,"count":purchasedGigs})
            db.commit()
            db.execute("INSERT INTO activedayusers(date,count) VALUES (:date,:count)",{"date":date,"count":last_day})
            db.commit()
            db.execute("INSERT INTO crashfree(date,count) VALUES (:date,:count)",{"date":date,"count":crash})
            db.commit()
            db.execute("INSERT INTO averagevalue(date,count) VALUES (:date,:count)",{"date":date,"count":float(averageTransaction)})
            db.commit()
            db.execute("INSERT INTO unprocessedpayments(date,count) VALUES (:date,:count)",{"date":date,"count":countTranscation})
            db.commit()
        
        elif date in dbDAte:
            db.execute("UPDATE users set count=:count where date=:date",{"count":users,"date":date})
            db.commit()
            db.execute("UPDATE sellers set count=:count where date=:date",{"count":sellers,"date":date})
            db.commit()
            db.execute("UPDATE buyers set count=:count where date=:date",{"count":buyers,"date":date})
            db.commit()
            db.execute("UPDATE activejobs set count=:count where date=:date",{"count":activejobs,"date":date})
            db.commit()
            db.execute("UPDATE blockedjobs set count=:count where date=:date",{"count":blockedjobs,"date":date})
            db.commit()
            db.execute("UPDATE totalgigs set count=:count where date=:date",{"count":totalGigs,"date":date})
            db.commit()
            db.execute("UPDATE gigspurchased set count=:count where date=:date",{"count":purchasedGigs,"date":date})
            db.commit()
            db.execute("UPDATE activedayusers set count=:count where date=:date",{"date":date,"count":last_day})
            db.commit()
            db.execute("UPDATE crashfree set count=:count where date=:date",{"date":date,"count":crash})
            db.commit()
            db.execute("UPDATE averagevalue set count=:count where date=:date",{"date":date,"count":float(averageTransaction)})
            db.commit()
            db.execute("UPDATE unprocessedpayments set count=:count where date=:date",{"date":date,"count":countTranscation})
            db.commit()

        else:
            pass

        yield app_users
    response = Response(stream_with_context((generate())),
                        mimetype='text/plain')
    return response




#-----------------Homepage-----------------------#
@app.route('/', methods=['POST','GET'])
def homepage():
    return render_template("login.html")




#------------------Main dashboard-----------------#
@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    username=session.get('username')
    if  username:
        app_users=sample_run_report(294104009)
        dau=db.execute("SELECT count FROM dau order by date desc limit 1").fetchone()

        urls = asyncio.run(get_all_urls())
        #------Website data--------#
        data=asyncio.run(get_all_urls_web())
        countTranscation=data[0]
        sumTranscation=data[1]
        averageTransaction=float(sumTranscation)/int(countTranscation)
        averageTransaction="{:.2f}".format(averageTransaction)

        #------App data-------------#
        crash=sample_run_report_crash(294104009)
        last_day=sample_run_report_lastDay(294104009)
        crash=(crash/1)*100
        return render_template("index.html",username=username,dau=dau[0],users=urls[0],buyers=urls[1],sellers=urls[2],active=urls[3],block=urls[4],totalGigs=urls[5],purchasedGigs=urls[6],app_users=app_users,UnprocessedPayments=countTranscation,averageTransaction=averageTransaction,crash_free=crash,last_day=last_day)

        
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))






#-----------------Login---------------------------#
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        #---------Session veriable----------#
        session['username']=username

        if session['username']=="savvyadmin" and password=="9NZteL9vht":
            return redirect(url_for('dashboard'))
        else:
            flash("Wrong credentials!")
            return redirect(url_for('homepage'))
    return redirect(url_for('homepage'))




#-----------------redirect to main page----------------------------------------#
@app.route('/home')
def homedirect():
    if session['username']:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('homepage'))


#-----------------For website data-------------------------------#'
@app.route('/website')
def websiteFunc():
    username=session.get('username')
    if  username:
        data=asyncio.run(get_all_urls_web())
        countTranscation=data[0]
        sumTranscation=data[1]
        averageTransaction=float(sumTranscation)/int(countTranscation)
        averageTransaction="{:.2f}".format(averageTransaction)
        return render_template("website.html",username=username,UnprocessedPayments=countTranscation,averageTransaction=averageTransaction)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))


#-----------------For App data-------------------------------#'
@app.route('/app')
def appFunc():
    username=session.get('username')
    if  username:
        crash=sample_run_report_crash(294104009)
        dau=db.execute("SELECT count FROM dau  order by date desc limit 1").fetchone()
        app_users=sample_run_report(294104009)
        crash=(crash/1)*100
        last_day=sample_run_report_lastDay(294104009)
        return render_template("app.html",username=username,crash_free=crash,last_day=last_day,app_users=app_users,dau=dau[0])
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))



# #-----------------For Facebook data-------------------------------#
# @app.route('/facebook')
# def facebookFunc():
#     username=session.get('username')
#     if  username:
#         return render_template("facebook.html",username=username)
#     else:
#         flash("You need to log in first!")
#         return redirect(url_for('homepage'))
        

# #-----------------For firebase data-------------------------------#'
# @app.route('/firebase')
# def firebaseFunc():
#     username=session.get('username')
#     if  username:
#         return render_template("firebase.html",username=username)
#     else:
#         flash("You need to log in first!")
#         return redirect(url_for('homepage'))



#----------------Users_inner_page----------------------------------#
@app.route('/UserHistory')
def UserHistory():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM users order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDays()
        Thirty=thirtyDays()
        var="Users"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))

#--------------------Search Users-----------------------------#
@app.route('/search/<var>',methods=['POST','GET'])
def search(var):
    username=session.get('username')
    if  username:
        if var=='Users':
            Seven=SevenDays()
            Thirty=thirtyDays()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM users where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM users where extract(Month from date)=:date order by date",{"date":Date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM users where date=:date order by date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)

        elif var=='Sellers':
            Seven=SevenDaysSellers()
            Thirty=thirtyDaysSellers()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM sellers where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM sellers where extract(Month from date)=:date order by date",{"date":Date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM sellers where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)

        elif var=='Buyers':
            Seven=SevenDaysBuyers()
            Thirty=thirtyDaysBuyers()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date

                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM buyers where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM buyers where extract(Month from date)=:date order by date",{"date":Date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM buyers where date=:date",{"date":date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)
        
        elif var=='Active Jobs':
            Seven=SevenDaysActiveJobs()
            Thirty=thirtyDaysActiveJobs()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM activejobs where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM activejobs where extract(Month from date)=:date order by date",{"date":Date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM activejobs where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)
        
          
        elif var=='Blocked Jobs':
            Seven=SevenDaysBlockedJobs()
            Thirty=thirtyDaysBlockedJobs()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM blockedjobs where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM blockedjobs where extract(Month from date)=:date order by date",{"date":Date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM blockedjobs where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)
        


        elif var=='Total Gigs':
            Seven=SevenDaysTotalGigs()
            Thirty=thirtyDaysTotalGigs()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM totalgigs where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM totalgigs where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM totalgigs where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)


        elif var=='Purchased Gigs':
            Seven=SevenDaysPurchasedGigs()
            Thirty=thirtyDaysPurchasedGigs()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM gigspurchased where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM gigspurchased where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM gigspurchased where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)

        elif var=='Average Transaction Value':
            Seven=SevenDaysAverageValue()
            Thirty=thirtyDaysAverageValue()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM averagevalue where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM averagevalue where extract(Month from date)=:date order by date",{"date":Date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM averagevalue where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)

        elif var=='Unprocessed Payments':
            Seven=SevenDaysUnprocessedPayments()
            Thirty=thirtyDaysUnprocessedPayments()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM unprocessedpayments where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM unprocessedpayments where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)

        elif var=='Crash Free users':
            Seven=SevenDaysCrashFreeUsers()
            Thirty=thirtyDaysCrashFreeUsers()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM crashfree where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM crashfree where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)

        elif var=='Active 1 day users':
            Seven=SevenDaysactiveusers()
            Thirty=thirtyDaysactiveusers()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM activedayusers where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM activedayusers where extract(Month from date)=:date order by date",{"date":Date}).fetchall()

                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM activedayusers where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)

        elif var=='Daily Active Users':
            Seven=SevenDaysDau()
            Thirty=thirtyDaysDau()
            usersData=[]
            date=request.form.get('input')
            try:
                date=date.lower()
                MonthCheck=date
                if date== 'january' or date=='february' or date=='march' or date== 'april' or date=='may' or date=='june' or date== 'july' or date=='august' or date=='september' or date== 'october' or date=='november' or date=='december':
                    Date=check(date)
                    usersData=[]
                    search=db.execute("SELECT * FROM dau where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    Month=db.execute("SELECT count FROM dau where extract(Month from date)=:date order by date",{"date":Date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)
                    else:
                        AllMonth=[]
                        for i in Month:
                            AllMonth.append(i[0])           
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        ThisMonth=AllMonth[-1]-AllMonth[0]
                        return render_template("search.html",Month=MonthCheck,ThisMonth=ThisMonth,username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty,var1=Date)
                else:
                    search=db.execute("SELECT date,count FROM dau where date=:date",{"date":date}).fetchall()
                    if not search:
                        error="No Records Found!"
                        return render_template("error.html",username=username,error=error,var=var)

                    else:
                        for i in search:
                            date=i[0]
                            count=i[1]
                            all_data={
                                "date":date,
                                "count":count
                            }
                            usersData.append(all_data)
                        return render_template("History.html",username=username,usersData=usersData,var=var,Seven=Seven,Thirty=Thirty)
            except:
                error="Invalid entry!"
                return render_template("error.html",username=username,error=error,var=var)


    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))


#----------------Seller_inner_page----------------------------------#
@app.route('/SellerHistory')
def SellerHistory():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM sellers order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysSellers()
        Thirty=thirtyDaysSellers()
        var="Sellers"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))


#----------------Buyers_inner_page----------------------------------#
@app.route('/BuyerHistory')
def BuyerHistory():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM buyers order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysBuyers()
        Thirty=thirtyDaysBuyers()
        var="Buyers"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))


#----------------ActiveJobs inner page----------------------------------#
@app.route('/ActiveJobsHistory')
def ActiveJobs():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM activejobs order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysActiveJobs()
        Thirty=thirtyDaysActiveJobs()
        var="Active Jobs"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))



#----------------Blocked jobs inner page----------------------------------#
@app.route('/BlockedJobsHistory')
def BlockedJobs():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM blockedjobs order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysBlockedJobs()
        Thirty=thirtyDaysBlockedJobs()
        var="Blocked Jobs"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))




#----------------Blocked jobs inner page----------------------------------#
@app.route('/TotalGigsHistory')
def TotalGigs():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM totalgigs order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysTotalGigs()
        Thirty=thirtyDaysTotalGigs()
        var="Total Gigs"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))



#----------------Purchased GIgs inner page----------------------------------#
@app.route('/PurchasedGigsHistory')
def PurchasedGigs():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM gigspurchased order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysPurchasedGigs()
        Thirty=thirtyDaysPurchasedGigs()
        var="Purchased Gigs"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))





#----------------Active Day Users inner page----------------------------------#
@app.route('/ActiveDayUsers')
def ActiveDayUsers():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM activedayusers order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysactiveusers()
        Thirty=thirtyDaysactiveusers()
        var="Active 1 day users"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))



#----------------Crash free Users inner page----------------------------------#
@app.route('/CrashFree')
def CrashFree():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM crashfree order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysCrashFreeUsers()
        Thirty=thirtyDaysCrashFreeUsers()
        var="Crash Free users"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))


#----------------average trasaction value inner page inner page----------------------------------#
@app.route('/AverageTransaction')
def AverageTransaction():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM averagevalue order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysAverageValue()
        Thirty=thirtyDaysAverageValue()
        var="Average Transaction Value"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))


#----------------Unprocessed payments inner page----------------------------------#
@app.route('/UnprocessedPayments')
def UnprocessedPayments():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM unprocessedpayments order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysUnprocessedPayments()
        Thirty=thirtyDaysUnprocessedPayments()
        var="Unprocessed Payments"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))



#----------------dau inner page----------------------------------#
@app.route('/DauInner')
def DauInner():
    username=session.get('username')
    if  username:
        usersData=[]
        all_users=db.execute("SELECT * FROM dau order by date asc").fetchall()
        for i in all_users:
            date=i[0]
            count=i[1]
            all_data={
                "date":date,
                "count":count
            }
            usersData.append(all_data)
        Seven=SevenDaysDau()
        Thirty=thirtyDaysDau()
        var="Daily Active Users"
        return render_template("History.html",username=username,usersData=usersData,Seven=Seven,Thirty=Thirty,var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))
#--------------------Download csv for user custom query-----------------------#

@app.route("/getPlotCV/<var>,<var1>")
def getPlotCSV(var,var1):
    if var=='Users':
        file=[]
        search=db.execute("SELECT date,count FROM users where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Buyers':
        file=[]
        search=db.execute("SELECT date,count FROM buyers where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Sellers':
        file=[]
        search=db.execute("SELECT date,count FROM sellers where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Active Jobs':
        file=[]
        search=db.execute("SELECT date,count FROM activejobs where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Blocked Jobs':
        file=[]
        search=db.execute("SELECT date,count FROM blockedjobs where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Total Gigs':
        file=[]
        search=db.execute("SELECT date,count FROM totalgigs where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Purchased Gigs':
        file=[]
        search=db.execute("SELECT date,count FROM gigspurchased where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)
    
    elif var=='Active 1 day users':
        file=[]
        search=db.execute("SELECT date,count FROM activedayusers where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Crash Free users':
        file=[]
        search=db.execute("SELECT date,count FROM crashfree where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Average Transaction Values':
        file=[]
        search=db.execute("SELECT date,count FROM averagevalue where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Unprocessed Payments':
        file=[]
        search=db.execute("SELECT date,count FROM unprocessedpayments where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Daily Active Users':
        file=[]
        search=db.execute("SELECT date,count FROM dau where extract(Month from date)=:var1 order by date",{"var1":var1}).fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)


#--------------------Download csv for all query-----------------------#

@app.route("/getPlotCV1/<var>")
def getPlotCSV1(var):
    if var=='Users':
        file=[]
        search=db.execute("SELECT date,count FROM users order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Sellers':
        file=[]
        search=db.execute("SELECT date,count FROM sellers order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
            path = "Data.csv"
            return send_file(path, as_attachment=True)

    elif var=='Buyers':
        file=[]
        search=db.execute("SELECT date,count FROM buyers order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

    elif var=='Active Jobs':
            file=[]
            search=db.execute("SELECT date,count FROM activejobs order by date").fetchall()
            for i in search:
                data=i['date']
                count=i['count']
                was={
                    "date":data,
                    "count":count
                }

                file.append(was)
            csv_columns=['date','count']

            with open('Data.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in file:
                    writer.writerow(data)
            path = "Data.csv"
            return send_file(path, as_attachment=True)

    elif var=='Blocked Jobs':
            file=[]
            search=db.execute("SELECT date,count FROM blockedjobs order by date").fetchall()
            for i in search:
                data=i['date']
                count=i['count']
                was={
                    "date":data,
                    "count":count
                }

                file.append(was)
            csv_columns=['date','count']

            with open('Data.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in file:
                    writer.writerow(data)
            path = "Data.csv"
            return send_file(path, as_attachment=True)

    elif var=='Total Gigs':
            file=[]
            search=db.execute("SELECT date,count FROM totalgigs order by date").fetchall()
            for i in search:
                data=i['date']
                count=i['count']
                was={
                    "date":data,
                    "count":count
                }

                file.append(was)
            csv_columns=['date','count']

            with open('Data.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in file:
                    writer.writerow(data)
            path = "Data.csv"
            return send_file(path, as_attachment=True)

    elif var=='Purchased Gigs':
            file=[]
            search=db.execute("SELECT date,count FROM gigspurchased order by date").fetchall()
            for i in search:
                data=i['date']
                count=i['count']
                was={
                    "date":data,
                    "count":count
                }

                file.append(was)
            csv_columns=['date','count']

            with open('Data.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in file:
                    writer.writerow(data)
            path = "Data.csv"
            return send_file(path, as_attachment=True)
        
     
    elif var=='Active 1 day users':
        file=[]
        search=db.execute("SELECT date,count FROM activedayusers order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)


       
    elif var=='Average Transaction Value':
        file=[]
        search=db.execute("SELECT date,count FROM averagevalue order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)


       
    elif var=='Crash Free users':
        file=[]
        search=db.execute("SELECT date,count FROM crashfree order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

       
    elif var=='Unprocessed Payments':
        file=[]
        search=db.execute("SELECT date,count FROM unprocessedpayments order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)

      
    elif var=='Daily Active Users':
        file=[]
        search=db.execute("SELECT date,count FROM dau order by date").fetchall()
        for i in search:
            data=i['date']
            count=i['count']
            was={
                "date":data,
                "count":count
            }

            file.append(was)
        csv_columns=['date','count']

        with open('Data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in file:
                writer.writerow(data)
        path = "Data.csv"
        return send_file(path, as_attachment=True)


#--------------------For Overview page csv-------------------------#
@app.route('/getPlotCSV2/<users>,<dau>,<buyers>,<sellers>,<active>,<block>,<totalGigs>,<purchasedGigs>,<app_users>,<UnprocessedPayments>,,<averageTransaction>,<crash_free>,<last_day>',methods=[ 'GET'])
def getPlotCSV2(users,dau,buyers,sellers,active,block,totalGigs,purchasedGigs,app_users,UnprocessedPayments,averageTransaction,crash_free,last_day):
    username=session.get('username')
    file=[]
    if  username:
        was={
            "users":users,
            "sellers":sellers,
            "buyers":buyers,
            "active jobs":active,
            "blocked jobs":block,
            "total gigs": totalGigs,
            "purchased gigs": purchasedGigs,
            "Unprocessed payments":UnprocessedPayments,
            "Average transaction value": averageTransaction,
            "Crash free users":crash_free,
            "Active 1 day users":last_day,
            "Active app users (currently)":int(app_users),
            "dau":dau
        }
        file.append(was)
       

    csv_columns=['users','sellers','buyers','active jobs','blocked jobs','total gigs','purchased gigs','Unprocessed payments','Average transaction value','Crash free users','Active 1 day users','Active app users (currently)','dau']

    file_name='Overview data on date:{date}.csv'.format(date=date)
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in file:
            writer.writerow(data)
    path = file_name
    return send_file(path, as_attachment=True)

#--------------------stats page-----------------------------#
@app.route("/stats/<var>")
def stats(var):
    username=session.get('username')
    if  username:
        if var=="Users":
            AllMonths=users()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Sellers":
            AllMonths=sellers()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Buyers":
            AllMonths=buyers()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Blocked Jobs":
            AllMonths=blockedjobs()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Total Gigs":
            AllMonths=totalgigs()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Purchased Gigs":
            AllMonths=gigspurchased()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Active 1 day users":
            AllMonths=activedayusers()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Daily Active Users":
            AllMonths=dailyac()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Unprocessed Payments":
            AllMonths=unprocessedpayments()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
        elif var=="Active Jobs":
            AllMonths=activejobs()
            return render_template('stats.html',date=date,username=username,january=AllMonths[0],february=AllMonths[1],march=AllMonths[2],april=AllMonths[3],may=AllMonths[4],june=AllMonths[5],july=AllMonths[6],august=AllMonths[7],september=AllMonths[8],october=AllMonths[9],november=AllMonths[10],december=AllMonths[11],var=var)
    else:
        flash("You need to log in first!")
        return redirect(url_for('homepage'))



#--------------------Logout-----------------------------#
@app.route("/logout")
def logout():
    session.pop('username',None)
    flash("logout successfull!")
    return redirect(url_for('homepage'))



if __name__=="__main__":
    app.run(debug=True,threaded=True,port=5000)
