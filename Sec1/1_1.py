#coding:utf-8
#一般的python
x = 1
y = x + 9
print(y)
#tensorflow 
import tensorflow as tf
x = tf.constant(1, name = 'x') #建立一個稱為x的常數值
y = tf.Variable(x+9, name = 'y') #建立一個變數y,並且用y=x+9定義它
print(y) #此時的y並未被執行

