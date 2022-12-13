from tkinter import *
from PIL import Image, ImageTk
from K_map_gui_tk import *

def makegraycode( n ):
    gray_code = ["0","1"]
    if(n<1):
        return {"0"}
    while(len(gray_code)<pow(2,n)):
        # print(len(gray_code))
        # if(len(gray_code)==pow(2,n)):
        #     break 
        l = len(gray_code)
        for i in range(l-1,-1,-1):
            gray_code.append(gray_code[i])
        # append 0 to the first half
        for j in range(l):
            gray_code[j] = "0" + gray_code[j]
 
        # append 1 to the second half
        for j in range(l, 2 * l):
            gray_code[j] = "1" + gray_code[j]
    
    # for i in range(len(gray_code)):
        # print(gray_code[i])
    return gray_code

def is_legal_region(kmap_function, term):
    root=kmap(kmap_function)
    n = len(term) #no of variables
   
    graycol = makegraycode(n-int(n/2))
    col=[]
    # print(graycol)
    # print(f"row  {int(n/2)}")
    grayrow = makegraycode(int(n/2))
    # print(grayrow)
    row=[]
    for i in range(len(graycol)):
        count = 0
        # print(f"colindex 0  {n-int(n/2)}")
        for j in range(0, n-int(n/2)):
            # print(f"colindex   {i}  {j}")
            if(term[j]== None):
                count+=1
            elif(term[j]==1):
                if(graycol[i][j]=='1'):
                    count+=1
            elif(term[j]==0):
                if(graycol[i][j]=='0'):
                    count+=1
        if(count==n-int(n/2)):
            col.append(i)


    for i in range(len(grayrow)):
        count = 0
        for j in range(n-int(n/2),n):
            # print(f"rowindex {i}  {j} ")
            if(term[j]== None):
                count+=1
            elif(term[j]==1):
                if(grayrow[i][j -(n-int(n/2)) ]=='1'):
                    count+=1
            elif(term[j]==0):
                if(grayrow[i][j - (n-int(n/2))]=='0'):
                    count+=1
        if(count==int(n/2)):
            row.append(i)

    # print("row")
    # print(row)
    # print("col")
    # print(col)   
    (y1,y2)= (col[0], col[-1])
    (x1,x2)= (row[0], row[-1])
    if(y2-y1+1 != len(col)):
        for i in range(1,len(col)):
            if(col[i]-1!=col[i-1]):
                (y2,y1)= (col[i-1], col[i])
                break
    if(x2-x1+1 != len(row)):
        for i in range(1,len(row)):
            if(row[i]-1!=row[i-1]):
                (x2,x1)= (row[i-1], row[i])
                break


    #     print("invalid number of variables")
    
    xdiff = x2-x1+1
    if(xdiff<0):
        xdiff+=4
    
    ydiff = y2-y1+1
    if(ydiff<0):
        ydiff+=4
    
    for i in range(x1, x1+xdiff):
        for j in range(y1, y1+ydiff):
            # print(f" :{kmap_function[i%4][j%4]}")
            if(kmap_function[i%4][j%4] ==0 ):
                # print(f"x1 {x1} y1 {y1} x2 {x2} y2 {y2}")
                # root.draw_region(x1,y1,x2,y2,'red')
                # root.mainloop()
                #display kmap
                return ((x1,y1), (x2,y2), False)
        # print("\n")
    # print(f"x1 {x1} y1 {y1} x2 {x2} y2 {y2}")
    # root.draw_region(x1,y1,x2,y2,'green')
    # root.mainloop()
    #display kmap
  
    return ((x1,y1), (x2,y2), True)

# print("start main")
# is_legal_region([[1,None],[1,1]],[None,1])

# # gray_code(3)
# # gray_code(4)
# print("main")

