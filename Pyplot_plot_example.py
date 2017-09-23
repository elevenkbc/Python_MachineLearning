# -*- coding: utf-8 -*-
# 若未在文檔開頭加入以上敘述,則無法使用中文註解
import numpy as np
import matplotlib.pyplot as plt #引入 matplotlib 模組中的 pyplot 並且簡寫為 plt
plt.figure(1) #第一個圖形視窗
plt.plot([1,2,3,4]) #使用在 pyplot 的類別下的函數 plot 來繪製圖片
plt.ylabel("This is y label discription") #用 ylabel 函數來對y座標作註釋

plt.figure(2)
plt.plot([1,2,3,4,5], [1,3,5,3,1], 'ro') #'ro' 為用紅色圓圈畫圖
plt.xlabel("red circle plot")

plt.figure(3)
plt.plot([1,2,3,4,5], [1,3,5,3,1], 'y-') #'y' 為用黃色線連接
plt.axis([0,6,-2,15]) #axis([左邊界, 右邊界,下邊界, 上邊界]) axis 用來指定圖形範圍

plt.figure(4)
t = np.arange(0., 5., 0.2) #產生從 0 到5 間隔為 0.2 的浮點數陣列

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**(.5), 'g^')


plt.figure(5)
# 繪圖的參數設定
line1 = plt.plot([1,2,3,4,5], [1,4,9,16,25]) # line1 為物件
plt.setp(line1, color = 'r', linewidth = 2.5) #用類似matlab的方式來指定繪圖方法
#以上也能改寫成 plt.setp(line1, 'color', 'r', 'linewidth', 2,5)


#多張圖片繪在同一個figure上
plt.figure(6)
#定義函數 f(t) = exp(-t)cos(2 pi t)
def f(t):
	return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0., 5., .1)
t2 = np.arange(0., 5., .02)

plt.subplot(211) #指定 2個row 1個column 的第一個
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'g')

plt.subplot(212)
plt.plot(t2, np.sin(t2), 'm--')

plt.show()  #將結果秀在圖形視窗上
