## 安裝 Python 套件 與  Tensorflow 方法


以下指令都在 **ubuntu 16.04 LTS** 64bit 作業系統下執行

#### 1. 安裝python 科學計算、繪圖的相關套件

安裝科學計算相關套件的順序

**python-numpy -> python-scipy -> python-matplotlib**

##### (1) 安裝 numpy

```shell
sudo apt-get install python-numpy
```

##### (2) 安裝 scipy

```shell
sudo apt-get install python-scipy
```

##### (3) 安裝 matplotlib

```shell
sudo apt-get install python-matplotlib
```

測試科學計算、繪圖相關套件是否安裝成功，建立以下 **Plot2D.py**

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3.5, 0.5)
y = [var1**2 for var1 in x]
z = [var2 *2 for var2 in x]

fig = plt.figure(1)

ax = fig.add_subplot(211)
line1 = ax.plot(x, y, 'ro-')

ax = fig.add_subplot(212)
line2 = ax.plot(x, z, 'g-')

plt.show()
```

執行 **Plot2D.py**

```shell
python Plot2D.py
```

若是安裝成功，執行後會出現以下畫面

![image](https://github.com/elevenkbc/Python_MachineLearning/blob/master/image/Plot2D.png)

#### 2.安裝 pip (Python 套件管理工具) 

在 *Terminal* 輸入 

```shell
sudo apt-get install python-pip
```

#### 3. Virtualenv (虛擬環境，可以避免python 套件間的干擾)

```shell
sudo apt-get install python-dev python-virtualenv
```

#### 4. 建立一個 Virtualenv 虛擬環境，用來安裝tensorflow 套件

```shell
virtualenv --system-site-packages ~/tensorflow
```

執行指令之後，會在根目錄下建立一個 **tensorflow** 資料夾，存放虛擬環境

#### 5. 啟動剛剛建立的 tensorflow 虛擬環境

```shell
source ~/tensorflow/bin/activate
```

執行後，終端機的每一行前面會出現 **(tenforflow) ** ，代表已經在剛剛新建的虛擬環境 (名為 tensorflow)中

此後在 *Terminal* 執行的所有指令、安裝的套件，都是在名為 **tensorflow** 中的虛擬環境中安裝，並不會與其他環境互相干擾



#### 6. 安裝 tensorflow 套件

```shell
pip install --upgrade tensorflow
```

#### 7. 測試 tensorflow 是否安裝成功

建立以下python 程式，並儲存為 **HelloTensorflow.py**

````python
import tensorflow as tf
hello = tf.constant("Hello! Tensorflow!")
sess = tf.Session()
print(sess.run(hello))
````

執行 **HelloTensorflow.py**

```shell
python HelloTensorflow.py
```

如果安裝成功會出現 **Hello! Tensorflow!**

#### 8.輸入以下指令，離開 **virtualenv** 虛擬環境

``` shell
deactivate
```

使用者名稱前的 **(tensorflow)** 便會消失
