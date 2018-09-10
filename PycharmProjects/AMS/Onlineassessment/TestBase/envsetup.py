import unittest
import MySQLdb
import mysql.connector
import xlrd
from selenium import webdriver
import datetime

class envSetup(unittest.TestCase):

    def __init__(self):
        conn = mysql.connector.connect(host='35.154.36.218',
                                       database='appserver_core',
                                       user='qauser',
                                       password='qauser')
        mycursor = conn.cursor()
        try:
            mycursor.execute(
                'delete from test_results where testuser_id in (select id from test_users where test_id = 6036 and login_time is not null);')
            conn.commit()
            print 'Test result deleted'
            mycursor.execute(
                'delete from candidate_scores where testuser_id in (select id from test_users where test_id = 6036 and login_time is not null);')
            conn.commit()
            print 'Candidate score deleted'
            mycursor.execute(
                'delete from test_user_login_infos where testuser_id in (select id from test_users where test_id = 6036 and login_time is not null);')
            conn.commit()
            print 'Test user login info deleted'
            mycursor.execute(
                'update test_users set login_time = NULL, log_out_time = NULL, status = 0, client_system_info = NULL, time_spent = NULL, is_password_disabled = 0,config = NULL, client_system_info = NULL, total_score = NULL, percentage = NULL where test_id = 6036 and login_time is not null;')
            conn.commit()
            print 'Test user login time reseted'
            mycursor.close()
            print 'Connection cl0sed'
        except Exception as e:
            print e
        print 'Executed'
        self.driver=webdriver.Chrome("D:\chromedriver.exe")
        print "Run started at :", str(datetime.datetime.now())
        print 'Chrome Env Setup'
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wb = xlrd.open_workbook('D:\Results_Final_Random_Evaluation_Check.xls')
        self.sh = self.wb.sheet_by_index(0)
        # print sh.row_values(0,0)
        n = 1
        rows =self.sh.nrows
        while n <rows:
            row_value = self.sh.row_values(n)
            # print row_value
            if row_value:
                self.Login_name = row_value[0]
                # print "Login Name =", self.Login_name
                self.Password = row_value[1]
                # print "Password = ", self.Password
                n+=1

    def tearDown(self):
        if (self.driver!=None):
            print('Test Env Destroyed')
            print('Run completed at:',str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

