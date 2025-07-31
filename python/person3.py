from person1 import person
from person2 import driver

class rapidodriver(person,driver):

    def __init__(self, p_name,mobile_no,p_location,d_name,d_location,lisenc_number,reting):
        person.__init__(self,p_name,mobile_no,p_location)
        driver.__init__(self,d_name,d_location,lisenc_number)
        self.reting=reting

    def detail(self):
        print(f"p_name:{self.p_name}\nmobile_no:{self.mobile_no}\np_location:{self.p_location}\nd_name:{self.d_name}\nd_location:{self.d_location}\nlisenc_number:{self.licence_number}\nreting:{self.reting}")

driver=rapidodriver("suraj",132444445,"basavangudi","ramesh","rajajinagar","gbl1223",5)
driver.detail()    