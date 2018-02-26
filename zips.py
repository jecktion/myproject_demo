import tkinter
import tkinter.filedialog
import os
import zipfile
import tkinter.messagebox



class Zips:
    #初始化对象
    def __init__(self):
        #存放压缩文件内容
        self.filelists=[]

        #用于判断添加按钮是否被按下
        self.isadd=False
        
        #创建窗口
        root=tkinter.Tk()
        root.minsize(300,400)
        root.maxsize(300,400)

        #三个按钮并且布局
        btn1 = tkinter.Button(root,text = '选择文件',command = self.selectfiles)
        btn1.grid(row = 0,column = 0,padx = 20,pady = 20)

        btn2 = tkinter.Button(root,text = '压缩文件',command = self.pressfile)
        btn2.grid(row = 0,column = 1,padx = 20,pady = 20)

        btn3 = tkinter.Button(root,text = '解压文件',command = self.unpressfile)
        btn3.grid(row = 0,column = 2,padx = 20,pady = 20)



        #一个label用于显示文件信息
        #声明一个变量用于存放文件信息

        self.files = tkinter.StringVar()
        
        self.files.set('没有任何文件被选中')

        label = tkinter.Label(root,textvariable = self.files,bg = 'blue',width = 40,height = 20,justify ='left',anchor = 'nw')
        label.grid(row = 1,column=0,columnspan = 3)


        root.mainloop()


    #文件选取函数
    def selectfiles(self):
        #按钮被按下时
        self.isadd=True
        
        
        if self.isadd==True:
            if len(self.filelists)==0:
                #如果长度为0,打开文件选择窗口，选择文件并且记录
                filepaths=tkinter.filedialog.askopenfilenames(title = '请选择要压缩文件')
                self.filelists=list(filepaths)
            
                #将信息写入label用于显示（字符串，一个路径一行）
                filestr = '\n'.join(self.filelists)
                self.files.set(filestr)
                #让按下按钮复位
                self.isadd=False
            else:
                filepaths1=tkinter.filedialog.askopenfilenames(title = '请选择要压缩文件')
                for i in filepaths1:
                    if i not in self.filelists:
                        self.files.append(i)
                #将路径换行显示
                filestr = '\n'.join(self.filelists)
                self.files.set(filestr)
                #让按下按钮复位
                self.isadd=False                                               
                                                               
                                                           
                                                           
    #压缩文件函数
    def pressfile(self):
        
        #请求用户选择文件压缩路径
        dirname1 = tkinter.filedialog.askdirectory(title = '请选择文件保存路径')
        #创建文件名
        basename1=os.path.basename(dirname1)+'zip'
        #组合完整名称
        zippath=os.path.join(dirname1,basename1)
        

        #判断是否压缩
        var=tkinter.messagebox.askokcancel('是否压缩','是否进行压缩')
        if var==True:
            #文件压缩
            #创建压缩文件
            zp=zipfile.ZipFile(zippath,'w',zipfile.ZIP_DEFLATED)                                               
                                                           
            #将文件压缩进来
            for path in self.filelists:
                #检测文件是否存在
                if os.path.exists(path)==True:
                    if os.path.isfile(path):
                        zp.write(path,os.path.basename(path))
                    elif os.path.isdir(path):                                      
                        zp.write(os.path.basename(path))

        
        #关闭压缩文件
        zp.close()

        #提示操作成功
        tkinter.messagebox.showinfo('操作完成','文件压缩成功，路径为：'+zippath)
        

    #解压文件函数
    def unpressfile(self):
        #选择压缩文件
        zippath = tkinter.filedialog.askopenfilename(title = '请选择解压文件',filetypes= [('zip文件','*.zip')])
    
        #选择解压路径
        dirpath = tkinter.filedialog.askdirectory(title= '选择解压路径')

        #解压操作
        #判断是否解压
        var=tkinter.messagebox.askokcancel('是否解压','是否进行解压')
        if var==True:                                                  
            zp = zipfile.ZipFile(zippath,'r',zipfile.ZIP_DEFLATED)
            
            zp.extractall(dirpath)

            zp.close()

            #提示解压结果
            tkinter.messagebox.showinfo('结果','文件解压成功，路径为：'+dirpath)
            
        
#实例化对象
zips=Zips()
        





















        

        





























        

   
    
