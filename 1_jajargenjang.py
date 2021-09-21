class jajarGenjang:
    def __init__(self,tinggi):
        self.tinggi=tinggi
    def gambarjajarGenjang(self):
        t=self.tinggi
        a=""
        i=0
        while(i<t):
            j=t
            u=0
            while(j>i):
                a+=' '
                j-=1
            while(u<=i):
                a+='*'
                u+=1
            j=t-1
            while(j>i):
                a+='*'
                j-=1
            i+=1
            a+= '\n'
        print(a)
    
a=jajarGenjang(5)
a.gambarjajarGenjang()