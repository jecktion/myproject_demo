



import tkinter
import time
#导入多线程高级模块
import threading



#定义抽奖器的类
class Cjq:
    #初始化对象
    def __init__(self):
        
        #将所有抽奖选项添加到列表中
        self.allfruits = []
        self.allfruits1 = []
        self.allfruits2 = []
        #获取抽奖列表的最大索引值
        self.maxindex = len(self.allfruits) - 1   #self.maxindex==11
        self.maxindex1 = len(self.allfruits1) - 1
        self.maxindex2 = len(self.allfruits2) - 1
        #设置起始索引值
        self.startindex = 0
        self.startindex1 = 0
        self.startindex2 = 0
        #是否停止标志
        self.stopflag = False
        self.stopflag1 = False
        self.stopflag2 = False

        #点击次数初始值
        self.num=0
        self.num1=0
        self.num2=0

        
        #初始化界面
        self.initwindow()
        
    #界面布局方法
    def initwindow(self):
        
        #界面布局
        root=tkinter.Tk()
        root.minsize(370,430)
        root.maxsize(370,430)
        root['bg']='#999999'
        #小标签
        root.title('天地玄黄，宇宙洪荒')


        #用于抽奖的label标签


        apple = tkinter.Label(root,text = '鼠',bg = '#669933',font=('黑体',15))
        apple.place(x = 70,y = 70,width = 50,height = 50)

        pear = tkinter.Label(root,text = '牛',bg = '#336633',font=('黑体',15))
        pear.place(x = 130,y = 70,width = 50,height = 50)

        orange = tkinter.Label(root,text = '虎',bg = '#336633',font=('黑体',15))
        orange.place(x = 190,y = 70,width = 50,height = 50)

        banana = tkinter.Label(root,text = '兔',bg = '#669933',font=('黑体',15))
        banana.place(x = 250,y = 70,width = 50,height = 50)

        cherry = tkinter.Label(root,text = '龙',bg = '#336633',font=('黑体',15))
        cherry.place(x = 250,y = 130,width = 50,height = 50)


        ananas = tkinter.Label(root,text = '蛇',bg = '#336633',font=('黑体',15))
        ananas.place(x = 250,y = 190,width = 50,height = 50)


        peach = tkinter.Label(root,text = '马',bg = '#669933',font=('黑体',15))
        peach.place(x = 250,y = 250,width = 50,height = 50)


        watermelon = tkinter.Label(root,text = '羊',bg = '#336633',font=('黑体',15))
        watermelon.place(x = 190,y = 250,width = 50,height = 50)

        lemon = tkinter.Label(root,text = '猴',bg = '#336633',font=('黑体',15))
        lemon.place(x = 130,y = 250,width = 50,height = 50)

        jackfruit =  tkinter.Label(root,text = '鸡',bg = '#669933',font=('黑体',15))
        jackfruit.place(x = 70,y = 250,width = 50,height = 50)

        coco =  tkinter.Label(root,text = '猪',bg = '#336633',font=('黑体',15))
        coco.place(x = 70,y = 190,width = 50,height = 50)

        longan =  tkinter.Label(root,text = '狗',bg = '#336633',font=('黑体',15))
        longan.place(x = 70,y = 130,width = 50,height = 50)

        west=tkinter.Label(root,text = '西',bg = '#336633',font=('黑体',15))
        west.place(x = 10,y = 160,width = 50,height = 50)

        east=tkinter.Label(root,text = '东',bg = '#336633',font=('黑体',15))
        east.place(x = 310,y = 160,width = 50,height = 50)

        north=tkinter.Label(root,text = '北',bg = '#336633',font=('黑体',15))
        north.place(x = 160,y = 10,width = 50,height = 50)

        south=tkinter.Label(root,text = '南',bg = '#336633',font=('黑体',15))
        south.place(x = 160,y = 310,width = 50,height = 50)

        bun1=tkinter.Label(root,text = '乾',bg = '#336633',font=('黑体',15))
        bun1.place(x = 10,y = 370,width = 50,height = 50)

        bun2=tkinter.Label(root,text = '坤',bg = '#336633',font=('黑体',15))
        bun2.place(x = 310,y = 370,width = 50,height = 50)



        
        
        #将所有抽奖选项添加到列表中
        self.allfruits = [apple,pear,orange,banana,cherry,ananas,peach,watermelon,lemon,jackfruit,coco,longan]
        print(self.allfruits)
        
        self.allfruits1=[west,south,east,north]
        print(self.allfruits1)

        self.allfruits2=[bun1,bun2]
        print(self.allfruits2)


        
        #设置按钮属性
        
        
        #按钮开始
        startbtn = tkinter.Button(root,text = '开始',bg='#CCCCCC',font=('宋体',11),bd=10,command=self.start)
        startbtn.place(x = 130,y = 160,width = 50,height = 50)
        

        #按钮结束
        stopbtn = tkinter.Button(root,text = '停止',bg='#CCCCCC',font=('宋体',11),bd=10,command=self.stop)
        stopbtn.place(x = 190,y = 160,width = 50,height = 50)
        
        #标题
        headline=tkinter.Label(root,text='卐  生命轮回  卐',bg='#CCCC00',font=('宋体',18))
        headline.place(x=70,y=370,width=230,height=50)

        
        
        root.mainloop()

        
    #设置按钮方法
    def start(self):
        
        #开启一个新的线程用于循环操作
        self.num += 1
        t = threading.Thread(target = self.roll)
        if self.num == 1:
            t.start()

        self.num1 += 1   
        t1 = threading.Thread(target = self.roll1)
        if self.num1 == 1:
            t1.start()

        self.num2 += 1    
        t2 = threading.Thread(target = self.roll2)
        if self.num2 == 1:
            t2.start()

    #定义一个用于旋转选项的函数
    def roll(self):
        
        while True:
            #检测是否按下了停止按钮，按下了就终止循环
            if self.stopflag == True:
                #复位终止按钮设置
                self.stopflag=False
                self.num = 0
                return self.startindex
            

                
                
            #获取抽奖列表的最大索引值
            self.maxindex = len(self.allfruits) - 1
            #判断索引值是否超过上限，超过就归0
        
            #将其他所有选项变回白色
            for i in self.allfruits:
                i['bg']='#669933'
                
            #将当前的索引对应的选项变色
            self.allfruits[self.startindex]['bg']='red'
            
            #设置停动时间
            time.sleep(0.08)
            
            #索引+1准备下次变色
            self.startindex += 1 
            
            
            if self.startindex > self.maxindex:
                self.startindex = 0
                
        


        
    #定义一个用于旋转选项的函数
    def roll1(self):
        
        while True:
            #检测是否按下了停止按钮，按下了就终止循环
            if self.stopflag1 == True:
                #复位终止按钮设置
                self.stopflag1=False
                self.num1 = 0
                return self.startindex1
            

                
                
            #获取抽奖列表的最大索引值
            self.maxindex1 = len(self.allfruits1) - 1
            #判断索引值是否超过上限，超过就归0
        
            #将其他所有选项变回白色
            for j in self.allfruits1:
                j['bg']='#669933'
                
            #将当前的索引对应的选项变色
            self.allfruits1[self.startindex1]['bg']='#FFFF00'
            
            
            #设置停动时间
            time.sleep(0.3)
            
            #索引+1准备下次变色
            self.startindex1 += 1 
            
            
            if self.startindex1 > self.maxindex1:
                self.startindex1 = 0
                
        


    #定义一个用于旋转选项的函数
    def roll2(self):
        
        while True:
            #检测是否按下了停止按钮，按下了就终止循环
            if self.stopflag2 == True:
                #复位终止按钮设置
                self.stopflag2=False
                self.num2 = 0
                return self.startindex2
            

                
                
            #获取抽奖列表的最大索引值
            self.maxindex2 = len(self.allfruits2) - 1
            #判断索引值是否超过上限，超过就归0
        
            #将其他所有选项变回白色
            for k in self.allfruits2:
                k['bg']='#669933'
                
            #将当前的索引对应的选项变色
            self.allfruits2[self.startindex2]['bg']='#003399'
            
            
            #设置停动时间
            time.sleep(0.1)
            
            #索引+1准备下次变色
            self.startindex2 += 1 
            
            
            if self.startindex2 > self.maxindex2:
                self.startindex2 = 0
                
        
              
        
            

    #定义结束抽奖函数
    def stop(self):
        
        #设置停止标志
        self.stopflag = True
        self.stopflag1 = True
        self.stopflag2 = True
        

        
        
#实例化对象
c=Cjq()
        
