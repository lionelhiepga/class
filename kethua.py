class dagiac:
    def __init__(self,n) -> None:
        self.socanh = n

    def nhapcanh(self):
        self.nhapcanh = [float(input('Bạn hãy nhập giá trị cạnh: ' + str(i+1) + ' : ')) for i in range(self.socanh)]
        
    
    def hienthicanh(self):
        for i in range(self.socanh):
            print('Giá trị cạnh ',i + 1,'là', self.nhapcanh[i])

class TamGiac(dagiac):
     def __init__(self):
        dagiac.__init__(self,3)

     def dientich(self):
        a, b, c = self.nhapcanh
        # Tính nửa chu vi
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('Diện tích của hình tam giác là %0.2f' %area)

t = TamGiac()
t.nhapcanh()
t.hienthicanh()
t.dientich()
    
    
