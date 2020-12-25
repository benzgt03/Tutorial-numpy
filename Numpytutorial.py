import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Do this before importing pyplot!
import matplotlib.pyplot as plt
import pandas as pd
#a = [1,2,3,4]

#for i in a :
 #   print(i)

#filter

#b = [4,2,3,5,6]
#c = []

#for j in b :

 #print("start")
#for k in c:

 #   print(k)

#numpy

data = [1,2,5,7,8] #List data
print(np.std(data)) # SD
print(np.mean(data)) # mean
print(np.max(data))#max
print(np.min(data))#min
arraydata = np.array([data]) # นำList ไปสร้างเป็นARRAY
print(type(arraydata))

#create matrix
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arrmat = np.arange(1,26).reshape(5,5)
newarr = arr.reshape(4, 3)
print("maTrix4*5 = ",arrmat)
print("รูปร่าง4*3 = ",newarr)
x = [[1,2,3],[4,5,6],[7,8,9]]
arraymatrixx = np.array(x) # สร้าง Matrix ขนาด 3*3
print(arraymatrixx)
print("ขนาดmatrix = ", arraymatrixx.shape) # บอกขนาด เช่น(2, 2)
print(arraymatrixx[1,2]) # เลือกสักตัวจากในmatrixออกมาโดยIndex (x = row , y = column) เริ่มที่0
print(arraymatrixx[2,1])
matsum = arrmat.sum()
print("sum ค่าใน matrix 4*5 = ",matsum) # sum ค่าในmatrix 4*5

#Slice matrix
c = arraymatrixx[: , :-1] #ลบแค่ column - 1 เลยออกมาเพียงสอง column ส่วนrow มาครบเพราะเอาหมด
print("c = " , c)
c1 = arraymatrixx [: , -1 :] # เอาแค่ column สุดท้าย
print ("c1 =" , c1)
c2 = arraymatrixx [0:1,:] # เอาแค่rowแรก ทุก column
print ("c2 =" , c2)

#identity matrix
matrixiden = np.eye(3) # สร้างIdentity matrix 3*3

print("matrix เอกลักษณ์ขนาด 3*3 = " , matrixiden)


#random
random = np.random.rand(4) #ทำการสุ่ม 4 ตัวเลข
print(random)
random = random *10
print(random) # ทำการสุ่มเลข 0-10
random = np.random.rand(3,2)
print(random*10) # ทำการสุ่มแบบสร้าง3แถวสองคอลัมโดยเป็นเลข0-10

#show graph นิดหน่อย
xbar  = 3.5
sd = 0.8
randomnormal = np.random.normal(xbar ,sd ,1000) #สร้างเลขสุ่ม โดยสุ่มเลขที่มีการกระจายแบบnormal จำนวน1000ค่าที่มีmean = 3.5 ,sd =0.8
print("ค่าสุ่ม10ตัวแรก = ",randomnormal[:10])
plt.show(block=True) # สองบรรทัดนี้แก้ปัญหากรณี graph ไม่show ใน Pycharm
plt.interactive(False)
plt.hist(randomnormal,bins = 40)
#plt.show() เอาออกเพื่อ show graph

#สร้าง Series and DataFrame
datal = [20,155,52,'liew']
datab = [20,165,55,'benz'] # สร้าง List
benzs = np.array(datab) # แปลงเป็น Array
idx = ['age','height','weight','name']
benzserie = pd.Series(benzs,idx) # Arrayแปลงเป็น Serie
print(benzserie)

datasum =list(zip(datab,datal))
cols = ['benz_profile','liew_profile']
dataf = pd.DataFrame(datasum , columns=cols,index=idx) #สร้างData frame
print(dataf)



