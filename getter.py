class mail:
    def __init__(self, ho, ten) -> None:
        self.ho = ho
        self.ten = ten

    @property
    def hovanten(self):
        return '{}  {}'.format(self.ho, self.ten)
    
    @property
    def email(self):
        return self.ho + '_' + self.ten + '@gmail.com'

mail_A = mail("tran","long")

mail_A.ho = "nguyen"
mail_A.ten = "vui"
#khi thay họ tên, nhưng email ko đc thay đổi theo


print(mail_A.ho)
print(mail_A.email)
print(mail_A.hovanten)

#property giúp biến email từ phương thức thành thuộc tính, gọi email ko cần dấu ngoặc

        