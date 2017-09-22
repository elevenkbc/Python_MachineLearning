#encodgin: utf8

import matplotlib.pyplot as plt
def bar_chart_generator():
	l = [1, 2, 3, 4, 5]
	h = [20, 14, 38, 27, 9]
	w = [0.1, 0.2, 0.3, 0.4, 0.5]
	b = [5, 2, 3, 4, 5]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	rects = ax.bar(l, h, w, b)
	plt.show()

bar_chart_generator()
 
