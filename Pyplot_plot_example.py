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


plt.show()  #將結果秀在圖形視窗上
