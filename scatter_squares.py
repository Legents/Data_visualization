import matplotlib.pyplot as plt


x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,edgecolor = 'none', s=40)
#设置图标 坐标的标签
plt.title("Square Numers", fontsize = 14)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)
#设置标记刻度
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.axis([0, 1100, 1, 1100000])
plt.show()
