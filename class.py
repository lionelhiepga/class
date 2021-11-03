


class sieunhan():
    sothutu = 1
    sucmanh = 50
    def __init__(self,t,mau,Vukhi) -> None:
        self.ten = t
        self.color = mau
        self.vukhi = Vukhi
        self.stt = sieunhan.sothutu
        sieunhan.sothutu += 1
    def xinchao(self):
        print('xin chao ta la sieu nhan',self.ten)
        print('ta o vi tri thu: ',self.stt)

sieunhanA = sieunhan('A', 'Đỏ', 'kiếm')
sieunhanB = sieunhan('B', 'vang','bua')

sieunhanA.xinchao()
