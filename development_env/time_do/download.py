import schedule
import time
import datetime
import os
#os.system('cd /usr/local')


date = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

year = date[2:4]

month =date[5:7]

day = date[8:10]

def job4():
    '''处理时间函数'''
    print("Job4:每天下午19:26执行一次，每次执行20秒")
    os.system('java -jar GDSJavaClient.jar 10.135.29.64 8080 samba ECMWF_HR/10_METER_WIND_GUST_IN_THE_LAST_3_HOURS'+' '+year+month+day+'20.000'+' '+year+month+day+'20.024'+' '+'diamond')
    time.sleep(20)
    print('job finshed------------------------------------------------------------------------')


if __name__ == '__main__':
    print("主程序")
    print(datetime.datetime.now())
    job4()
    #print(type(datetime.datetime.now()),datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)



    #schedule.every().day.at('19:26').do(job4)

    #while True:
    #    schedule.run_pending()