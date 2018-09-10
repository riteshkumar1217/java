# import xlrd
# import xlwt
#
# class IoClass():
#     def __init__(self, driver):
#         self.driver = driver
#     def inputdata(self):
#         self.wb = xlrd.open_workbook('D:\Results_Final_Random_Evaluation_Check.xls')
#         self.sh = self.wb.sheet_by_index(0)
#         # print sh.row_values(0,0)
#         n = 1
#         rows =self.sh.nrows
#         while n <rows:
#             row_value = self.sh.row_values(n)
#             # print row_value
#             self.Login_name = row_value[0]
#             print "Login Name =", self.Login_name
#             self.Password = row_value[1]
#             print "Password = ", self.Password
#             n+=1

#
# class area():
#     def __init__(self,l,b):
#         # self.area()
#         self.l = l
#         self.b = b
#     def area(self):
#         print 'area of rectangle:', self.l * self.b
#     def perimeter(self):
#
#         print 'Permeter of rectangle:', 2 * (self.l+self.b)
#
# #
# a = area(3,2)
# a.area()
# a.perimeter()