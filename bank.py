class Bank:
    bank_name='SBI'
    bank_roi=7
    bank_branch='kizikistan'
    def __init__(self,cn,ca,cac,cb):
        self.cname=cn
        self.cage=ca
        self.caccount=cac
        self.cbalance=cb
    @classmethod
    def bank_details(cls):
        print(f'Name of the bank is {cls.bank_name}')
        print(f'ROI of the bank is {cls.bank_roi}')
        print(f'Branch of thr bank is {cls.bank_branch}')

    def customer_details(self):
        print(f'Name of the customer is {self.cname}')
        print(f'Age of the customer is {self.cage}')
        print(f'Account of the customer is {self.caccount}')
        print(f'Balance of the customer is {self.cbalance}')
    @staticmethod
    def get_int_value():
        iv=int(input('enter the value'))
        return iv
    @staticmethod
    def get_str_value():
        sv=input()
        return sv
    
    def withdraw(self):
        amount=self.get_int_value()
        if amount<=self.cbalance:
            self.cbalance-=amount
            print('withdrawal is successfull')
            print(f'balance is {self.cbalance}')
        else:
            print('insufficient balance')

    def deposit(self):
        amount=self.get_int_value()
        if amount>0:
            self.cbalance+=amount
            print('deposited successfully')
        else:
            print('enter valid amount')

    def balance_enquiry(self):
        print(f'Balance is {self.cbalance}')
    
    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_value()
        cls.bank_roi=newroi
        print('ROI is modified')

    @classmethod
    def change_branch(cls):
        bn=cls.get_str_value()
        cls.bank_branch=bn
        print('Branch is modified')

govinda=Bank('Govinda Govindaa',22,98765,563214)
malik=Bank('Malik Basha',23,54321,635241)
#govinda.customer_details()
malik.customer_details()
#malik.withdraw()
malik.deposit()
malik.balance_enquiry()



    