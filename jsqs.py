



import tkinter
import math

root = tkinter.Tk()
root.minsize(240,280)
root.maxsize(240,280)
root.title('超级牛逼计算器')
root['bg']='#CCCCCC'

#菜单组件    
btn1 = tkinter.Button(root,text = '查看(V)',bd=5,bg='#CCCCCC')

btn1.place(x= 10,y = 0,width = 50,height =20)

btn2 = tkinter.Button(root,text = '编辑(E)',bd=5,bg='#CCCCCC')

btn2.place(x= 95,y = 0,width = 50,height =20)

btn3 = tkinter.Button(root,text = '帮助(H)',bd=5,bg='#CCCCCC')

btn3.place(x= 180,y = 0,width = 50,height =20)


#显示器

class Calc:
    


    #初始化魔术方法(界面布局)
    def __init__(self):
        


        #初始化共用属性
        #运算标志
        self.isys = False
        #运算列表
        self.yslists = []

        print(self.isys)

        #初始化界面
        self.initwindow()

    #界面布局方法
    def initwindow(self):


        #数字变量
        #创建变量
        self.num = tkinter.StringVar()
        
        self.num.set(0)

        #创建label显示运算结果
        label = tkinter.Label(root,textvariable = self.num,bg = '#999966',font = ('黑体',20),anchor = 'e')
        label.place(x = 10,y = 25,width = 220,height = 30)

        #设置按钮属性
        btn1 = tkinter.Button(root,text = 'MC',bd=5,bg='#CCCCCC',font=('宋体',13))
        btn1.place(x= 10,y = 60,width =40,height =30)

        btn2 = tkinter.Button(root,text = 'MR',bd=5,bg='#CCCCCC',font=('宋体',13))
        btn2.place(x= 55,y = 60,width = 40,height =30)

        btn3 = tkinter.Button(root,text = 'MS',bd=5,bg='#CCCCCC',font=('宋体',13))
        btn3.place(x= 100,y = 60,width = 40,height =30)

        btn4 = tkinter.Button(root,text = 'M+',bd=5,bg='#CCCCCC',font=('宋体',13))
        btn4.place(x= 145,y = 60,width = 40,height =30)

        btn5 = tkinter.Button(root,text = 'M-',bd=5,bg='#CCCCCC',font=('宋体',13))
        btn5.place(x= 190,y = 60,width = 40,height =30)


        btn6 = tkinter.Button(root,text = '←',bd=5,bg='#CCCCCC',font=('宋体',13),command=self.pressqk)
        btn6.place(x= 10,y = 95,width = 40,height =30)
        
        btn7 = tkinter.Button(root,text = 'CE',bd=5,bg='#CCCCCC',font=('宋体',13),command=self.pressca)
        btn7.place(x= 55,y = 95,width = 40,height =30)

        btn8 = tkinter.Button(root,text = 'C',bd=5,bg='#CCCCCC',font=('宋体',13),command = lambda : self.presscl())
        btn8.place(x= 100,y = 95,width = 40,height =30)

        btn9 = tkinter.Button(root,text = '±',bd=5,bg='#CCCCCC',font=('宋体',13),command=self.presszf)
        btn9.place(x= 145,y = 95,width = 40,height =30)

        btn10 = tkinter.Button(root,text = '√',bd=5,bg='#CCCCCC',font=('宋体',13),command=self.pressgh)
        btn10.place(x= 190,y = 95,width = 40,height =30)

        btn11 = tkinter.Button(root,text = '7',bd=5,bg='#CCCCCC',font=('宋体',13),command = lambda : self.pressno('7'))
        btn11.place(x= 10,y = 130,width = 40,height =30)

        btn12 = tkinter.Button(root,text = '8',bd=5,bg='#CCCCCC',font=('宋体',13),command = lambda : self.pressno('8'))
        btn12.place(x= 55,y = 130,width = 40,height =30)

        btn13 = tkinter.Button(root,text = '9',bd=5,bg='#CCCCCC',font=('宋体',13),command = lambda : self.pressno('9'))
        btn13.place(x= 100,y = 130,width = 40,height =30)

        btn14 = tkinter.Button(root,text = '/',bd=5,bg='#CCCCCC',font=('宋体',13),command = lambda : self.pressys('/'))
        btn14.place(x= 145,y = 130,width = 40,height =30)
         
        btn15 = tkinter.Button(root,text = ' % ',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressys('%'))
        btn15.place(x= 190,y = 130,width = 40,height =30)
        
        btn16 = tkinter.Button(root,text = '4',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressno('4'))
        btn16.place(x= 10,y = 165,width = 40,height =30)

        btn17 = tkinter.Button(root,text = '5',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressno('5'))
        btn17.place(x= 55,y = 165,width = 40,height =30)

        btn18 = tkinter.Button(root,text = '6',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressno('6'))
        btn18.place(x= 100,y = 165,width = 40,height =30)

        btn19 = tkinter.Button(root,text = '*',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressys('*'))
        btn19.place(x= 145,y = 165,width = 40,height =30)

        btn20 = tkinter.Button(root,text = '1/x',font=('宋体',13),bd=5,bg='#CCCCCC',command=self.pressfh)
        btn20.place(x= 190,y = 165,width = 40,height =30)

        btn21 = tkinter.Button(root,text = '1',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressno('1'))
        btn21.place(x= 10,y = 200,width = 40,height =30)

        btn22 = tkinter.Button(root,text = '2',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressno('2'))
        btn22.place(x= 55,y = 200,width = 40,height =30)

        btn23 = tkinter.Button(root,text = '3',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressno('3'))
        btn23.place(x= 100,y = 200,width = 40,height =30)

        btn24 = tkinter.Button(root,text = '-',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressys('-'))
        btn24.place(x= 145,y =200,width = 40,height =30)

        btn25 = tkinter.Button(root,text = '0',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressno('0'))
        btn25.place(x= 10,y = 235,width = 85,height =30)
        
        btn26 = tkinter.Button(root,text = '.',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressdi('.'))
        btn26.place(x= 100,y = 235,width = 40,height =30)

        btn27 = tkinter.Button(root,text = '+',font=('宋体',13),bd=5,bg='#CCCCCC',command = lambda : self.pressys('+'))
        btn27.place(x= 145,y =235,width = 40,height =30)


        btn28 = tkinter.Button(root,text = '=',bd=5,font=('宋体',13),bg='#CCCCCC',command = self.getresult)
        btn28.place(x= 190,y = 200,width = 40,height =65)


        root.mainloop()
        


    #添加功能方法
    #数字按钮操作
    def pressno(self,no):
        print(self.isys)
        print(no)
        #判断用户是否按下了运算按钮
        if self.isys == True:
           
            #按下了运算按钮
            self.num.set(no)
            #将运算标志复位
            self.isys = False

        
        else:
            #没有按下运算按钮
            #判断界面原始数字是否为0
            oldno = self.num.get()
            if oldno == '0':
                #如果界面为0，获取用户按下的数字，显示到界面中
                self.num.set(no)
            else:
                #如果界面不为0，其他数字链接进来
                self.num.set(self.num.get()+no)


    #运算按钮操作
    def pressys(self,ysflag):


        #设置运算被按下的标志
        self.isys =True  #此处多个'='出错！'=='不是附值！
        
            
        #将每次运算操作的信息计入一个列表 ['22','*','88'] -> result = eval(''.join(['22','*','88'] ))
        #按下按钮获取界面中已经输入的数字
        self.yslists.append(self.num.get())
        #记录当前运算符号
        self.yslists.append(ysflag)
        print(ysflag)
        
        

    #获取运算'='结果
    def getresult(self):
        
        
        #进行运算操作
        
        #或当前界面中的数字，并且加入运算列表
        self.yslists.append(self.num.get())
        
        #进行运算操作
        result = eval (''.join(self.yslists))#将每次运算操作的信息计入一个列表 ['22','*','88'] -> result = eval(''.join(['22','*','88'] ))
        lists1=self.yslists.append('=')
        print(lists1)
        print(self.yslists)
        print(result)
        
        #清空前面的过程
        self.yslists.clear()

        
        #将结果放入界面当中
        self.num.set(result)
       

    #设置清空'C'符号功能    
    def presscl(self):
        self.yslists.clear()
        self.num.set('0')

    
    #设置清空'←'符号功能
    def pressqk(self):
        if self.isys == True:
            #按下了按钮
            #self.num.set(no)
            #将按钮标志复位
            self.isys = False
        else:
            if self.num.get()=='0':
                self.num.set('0')
            else:
                lists=list(self.num.get())
                if len(lists)==1:
                    
                    lists.pop()
                    self.num.set('0')
                else:
                    lists.pop()
                    
                    print(self.num.get())
                    self.num.set(''.join(lists))
                    
                
    #设置'.'的处理功能
    def pressdi(self,di):
        if self.isys == True:
            #按下了按钮
            self.num.set(no)
            #将按钮标志复位
            self.isys = False
        else:
            if '.' not in self.num.get():
                self.num.set(self.num.get()+di)


    #设置'CE'符号功能
    def pressca(self):
        if self.isys == True:
            self.isys = False
        
        else:
            if self.num.get()=='0':
                self.num.set('0')
            
            else:
                self.num.set('0')
                

    #设置'±'符号功能
    def presszf(self):
        if self.isys == True:
            self.isys = False
        else:
            if '-' not in self.num.get():
                strs='-'+self.num.get()
                self.num.set(strs)
            else:
                strs2=self.num.get().lstrip('-')
                self.num.set(strs2)
                
                
    #设置'√'符号功能
    def pressgh(self):
        if self.isys == True:
            self.isys = False
        else:
            ghs=math.sqrt(float(self.num.get()))
            print(ghs)
            result='{:.6f}'.format(ghs)
            self.num.set(result)
            
            

    #设置'1/x'符号功能
    def pressfh(self):
        if self.isys == True:
            self.isys = False
        else:
            result=eval('1'+'/'+self.num.get())
            print(result)
            self.num.set(result)
        
        
    
#实例化对象
c = Calc()













