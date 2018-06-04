from selenium import webdriver
import time
import xlrd
import xlwt
excel = xlwt.Workbook()  # 创建一个excel表
sheet = excel.add_sheet("test")  # 创建一个sheet
sheet.write(0, 0, 'username')
sheet.write(0, 1, 'password')
list1 = ['15902127951', '15902127952', '15902127954', '15902127955', '15902127956', '15902127953']
list2 = ['12345678', '123456789', '123456', '1234567', '1234', '123456']
for i in range(len(list1)):
    sheet.write(i + 1, 0, list1[i])
for i in range(len(list2)):
    sheet.write(i + 1, 1, list2[i])
excel.save('0527.xlsx')  # 保存上面写入的数据
# 读取数据
excel = xlrd.open_workbook('0527.xlsx')
sheet = excel.sheet_by_index(0)
class mylogintest:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:5000/')
        driver.find_element_by_xpath("//*[text()='登录']").click()
        name = driver.find_element_by_xpath("/html/body/form/p[1]/input")
        name.send_keys(self.username)
        time.sleep(3)
        pwd = driver.find_element_by_xpath("/html/body/form/p[2]/input")
        pwd.send_keys(self.password)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/form/p[3]/button").click()
        driver.close()
    # def excute_case(self):

for i in range(sheet.nrows):
    case = mylogintest(sheet.row_values(i + 1)[0], sheet.row_values(i + 1)[1]).login()










#

















