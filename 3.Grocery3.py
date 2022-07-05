
import pickle
class User:
    def __init__(self) -> None:
        self.l=[]
        self.d={}
        self.c={}
        self.total=0.0
        self.pay=0.0
        self.final=0.0
        self.cash=0.0
        pass

    def loadData(self):
        with open('ProductList.txt', 'rb') as handle:
            data = handle.read()
            self.d = pickle.loads(data)
        with open('CouponCode.txt', 'rb') as handle:
            data = handle.read()
            self.c = pickle.loads(data)

    def inputItem(self):
        item='C'
        print("Enter: \'Item code\' \'Quantity\'")
        print("Enter: \'S\' to Stop")
        while(2>1):
            item=input("")
            if(item=='S'):
                break
            else:
                p=item.split(' ')
                n=float(p[1])
                self.bill(p[0],n)
        self.pay=self.total+int(0.18*self.total)
        print("Amount Payable is ",self.pay)
        cc=input("Enter Coupon Code if applicable else S: ")
        self.final=self.pay
        if(cc!='S'):
            for val in self.c:
                if(val==cc and self.pay>=self.c[cc]):
                    self.final=self.pay-self.c[cc]
        print("Final Amount is ",self.final)
        self.cash=float(input("Enter cash recieved: "))        

    def bill(self,pcode,qty):
        self.l.append(self.d.get(pcode)[0])
        self.l.append(self.d.get(pcode)[1])
        self.l.append(qty/self.d.get(pcode)[2])
        self.total=self.total+self.d.get(pcode)[1]*(qty/self.d.get(pcode)[2])

    def reciept(self):
        print("\n\n")
        print("BILL".center(40))
        print("")
        print("SOMAIYA STORE".center(40))
        print("Opp to K.J Somaiya College, Vidyavihar\n".center(40))
        print(F"{'Item Name':<10}{'MRP':^20}{'Qty':>10}")
        i=0
        while(i!=len(self.l)):
            print(f"{self.l[i]:<10}{self.l[i+1]:^20}{self.l[i+2]:>10}")
            i+=3
        print("--------------------------------------".center(40))
        print(f"{'Amount:':<10}{(self.total):>30}")
        print(f"{'GST:':<10}{'18.0%':>30}")
        print(f"{'Total Amount:':<10}{self.pay:>27}")
        print(f"{'Final Amount:':<10}{self.final:>27}")
        print(f"{'Cash Recieved:':<10}{self.cash:>26}")
        print(f"{'Change:':<10}{(self.cash-self.final):>30}")
        print("~~~~~~ THANK YOU ~~~~~~".center(40))
        print("\n\n")

class Admin:
    def __init__(self) -> None:
        self.edit=""
        self.dd={}
        self.cp={}
        pass

    def loadData(self):
        with open('ProductList.txt', 'rb') as handle:
            data = handle.read()
            self.dd = pickle.loads(data)
        with open('CouponCode.txt', 'rb') as handle:
            data = handle.read()
            self.cp = pickle.loads(data)

    def editor(self):
        print("ADMIN (EDIT PRODUCT LIST)".center(40))
        print("Enter:\n\'A\' To Append or Add\n\'D\' To Delete\n\'C\' To Add Coupon Code\n\'V\' To View Product List\n\'S\' To Stop")
        while(2>1):
            self.edit=input("")
            if(self.edit=='A'):
                self.append()
            elif(self.edit=='D'):
                self.delete()
            elif(self.edit=='C'):
                self.coupon()
            elif(self.edit=='V'):
                self.view()
            elif(self.edit=='S'):
                break

    def append(self):
        tt=int(input("Enter number of items to be added:"))
        for i in range (tt):
            cd1=input("Enter product code:")
            nm1=input("Enter product name:")
            pr1=float(input("Enter product price:"))
            q1=float(input("Enter product quantity:"))
            self.dd.update({cd1:[nm1,pr1,q1]})
            i+=1
        print("Item successfully updated")
        self.update()

    def delete(self):
        j=int(input("Enter number of items to be deleted:"))
        for i in range (j):
            cd2=input("Enter product code:")
            del self.dd[cd2]
            print("Item successfully deleted")
            i+=1
        self.update()
    
    def coupon(self):
        f=input("Enter coupon code to be appended:")
        cpc=input("Enter new coupon code:")
        cpp=input("Enter coupon value:")
        del self.cp[f]
        self.cp.update({cpc:float(cpp)})
        print("Coupon code successfuly updated")
        file = open("CouponCode.txt", "wb")
        pickle.dump(self.cp, file)
        file.close()

    def update(self):
        file = open("ProductList.txt", "wb")
        pickle.dump(self.dd, file)
        file.close()

    def view(self):
        print("Product List")
        print(self.dd)
        print("Coupon Code")
        print(self.cp)

class Grocery(User,Admin):
    def __init__(self) -> None:
        pass

    def prog(self):
        while(2>1):
            print("Enter\n\'U\' For User\n\'A\' For Admin\n\'S\' To Stop")
            ans=input("")
            if(ans=='U'):
                s1=User()
                s1.loadData()
                s1.inputItem()
                s1.reciept()
            elif(ans=='A'):
                s2=Admin()
                s2.loadData()
                s2.editor()
            elif(ans=='S'):
                break
        
s3=Grocery()        
s3.prog()


        



            




  

