#coding:utf-8
#�@�몺python
x = 1
y = x + 9
print(y)
#tensorflow 
import tensorflow as tf
x = tf.constant(1, name = 'x') #�إߤ@�Ӻ٬�x���`�ƭ�
y = tf.Variable(x+9, name = 'y') #�إߤ@���ܼ�y,�åB��y=x+9�w�q��
print(y) #���ɪ�y�å��Q����

