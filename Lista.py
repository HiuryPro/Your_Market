from tkinter import *
  
  

      
def Lista(root, vezes): 
        largura = 500
        altura = 0
        i = 1
        j = 0
        new = 4
        while i <= c :
            while j < new:
                e = Label(root,text="", width=20, fg='blue', font=('Arial',16,'bold'),
                borderwidth = 2,
                relief="ridge") 
                e.place(x= largura, y = altura, width = 250, height = 30) 
                e["text"]= lst[j]
                largura += 250
                j += 1
            
            new += 4
            i += 1  
            altura += 30
            largura = 500
        
        i = 0
        if vezes != 0:
             while i < vezes :
                e = Label(root,text="", width=20, fg='blue', font=('Arial',16,'bold'),
                borderwidth = 2,
                relief="ridge") 
                e.place(x= largura, y = altura, width = 250, height = 30) 
                e["text"]= lst[j]
                largura += 250
                j += 1
                i += 1  
               
            


        
      
            
lst = ["1", "2", "3", "4", "5", "6", "7", "8"]


total_rows = len(lst)
vezes = len(lst) % 4
c = len(lst) / 4

print(total_rows)
print(vezes)




root = Tk()
root.state('zoomed')
t = Lista(root, vezes) 
root.mainloop() 
