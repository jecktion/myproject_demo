import tkinter
import tkinter.filedialog
import tkinter.messagebox
import zipfile
import os

root=tkinter.Tk()

 
root.minsize(300,400)
root.maxsize(300,400)

#设置全局变量 存放压缩文件内容
filelists = []


#文件选取函数
def selectfiles():
    #全局化操作
    global filelists

    #打开文件选择窗口，选择文件并且记录
    
    filepaths= tkinter.filedialog.askopenfilenames(title = '请选择要压缩文件')
    filelists=list(filepaths)

    #将信息写入label用于显示（字符串，一个路径一行）
    filestr = '\n'.join(filelists)
    files.set(filestr)

    
#文件压缩操作
def pressfile():
    #全局化操作
    global filelists

    #请求用户选择文件压缩路径
    dirname = tkinter.filedialog.askdirectory(title = '请选择文件保存路径')

    #创建文件名
    basename = os.path.basename(dirname)+'.zip'

    #组合完整名称
    zippath = os.path.join(dirname,basename)

    #创建压缩文件
    zp = zipfile.ZipFile(zippath,'w',zipfile.ZIP_DEFLATED)

    #将文件压缩进来
    for path in filelists:
        #检测文件是否存在
        if os.path.exists(path):
            #向压缩文件中写入文件
            zp.write(path,os.path.basename(path))

            
    #关闭压缩文件
    zp.close()

    #提示操作成功
    tkinter.messagebox.showinfo('操作完成','文件压缩成功，路径为：'+zippath)




#解压文件函数
def unpressfile():
    #选择压缩文件
    zippath = tkinter.filedialog.askopenfilename(title = '请选择解压文件',filetypes= [('zip文件','*.zip')])

    #选择解压路径
    dirpath = tkinter.filedialog.askdirectory(title= '选择解压路径')

    #解压操作
    zp = zipfile.ZipFile(zippath,'r',zipfile.ZIP_DEFLATED)

    zp.extractall(dirpath)

    zp.close()
    

    #提示解压结果
    tkinter.messagebox.showinfo('结果','文件解压成功，路径为：'+dirpath)



    
#三个按钮并且布局
btn1 = tkinter.Button(root,text = '选择文件',command = selectfiles)
btn1.grid(row = 0,column = 0,padx = 20,pady = 20)

btn2 = tkinter.Button(root,text = '压缩文件',command = pressfile)
btn2.grid(row = 0,column = 1,padx = 20,pady = 20)

btn3 = tkinter.Button(root,text = '解压文件',command = unpressfile)
btn3.grid(row = 0,column = 2,padx = 20,pady = 20)


    

#一个label用于显示文件信息

#声明一个变量用于存放文件信息


files = tkinter.StringVar()
files.set('没有任何文件被选中')

label = tkinter.Label(root,textvariable = files,bg = 'blue',width = 50,height = 20,justify ='left',anchor = 'nw')
label.grid(row = 1,column=0,columnspan = 3)


root.mainloop()






