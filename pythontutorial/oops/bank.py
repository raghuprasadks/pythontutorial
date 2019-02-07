class Bank:
    def __init__(self,name,headOffice,noOfBranches,roi):
        self.name = name
        self.headOffice = headOffice
        self.noOfBranches = noOfBranches
        self.roi = roi
    
    def info(self):
        print("Name : ",self.name, " Head Office : ",self.headOffice, " No of Branches ",self.noOfBranches, " Rate Of Interest ",self.roi)

    def showROI(self):
        print("Rate Of Interest : ",self.roi)

bk = Bank("RBI","Delhi",25,3.0)
bk.info()
bk.showROI()


class ICICI(Bank):
    def __init__(self,name,headOffice,noOfBranches,roi):
        super(ICICI,self).__init__(name,headOffice,noOfBranches,roi)
    def showROI(self):
        print("Rate Of Interest Of ICICI : ",self.roi)

bki = ICICI("ICICI","MUMBAI",2000,6.0)
bki.info()
bki.showROI()

class HDFC(Bank):
    def __init__(self,name,headOffice,noOfBranches,roi):
        super(HDFC,self).__init__(name,headOffice,noOfBranches,roi)
    def info(self):
        print("Name : ",self.name, " Head Office : ",self.headOffice, " No of Branches ",self.noOfBranches, " Rate Of Interest ",self.roi)

    def showROI(self):
        print("Rate Of Interest : ",self.roi)

bkh = HDFC("HDFC","MUMBAI",1500,7.0)
bkh.info()
bkh.showROI()



