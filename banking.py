# lớp cha : user
# giữ, hiển thị thông tin về một người dùng
# có một hàm để chiếu thông tin người dùng

#lớp con: bank
#stores thông báo về số dư tài khoản
#stores thông báo về số lượng
#cho phép gửi tiền, rút tiền, xem số dư

#parent class
class user:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender 

    def thongtin(self):
        print("personal details")
        print('')
        print("name: ", self.name)
        print("age: ", self.age)
        print("gender: ", self.gender)

#hiep.user("hiep", 19, "nam")
#hiep.thongtin()

#child class
class bank(user):
    
    #kế thừa của class user 
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender) 
        self.balance = 0                  #số dư = 0
    
    def guitien(self, amount):
        self.balance = self.balance + amount
        print("The present balance: ", self.balance)

    def ruttien(self, amount_r):
        if amount_r > self.balance:
            print("vượt quá số dư, số dư hiện tại là: ", self.balance)
        else:
            self.balance = self.balance - amount_r
            print(" số dư hiện tại: ", self.balance)

    def show_detail(self):
        self.thongtin()
        print("Số dư hiện tại: ", self.balance)

hiep = bank("hiep", 19, "nam")   
#hiep.guitien(100)    
hiep.guitien(400)
hiep.ruttien(200)
hiep.ruttien(300)
hiep.show_detail()
