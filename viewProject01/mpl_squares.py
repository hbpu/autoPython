import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

ax.set_title("平方数", fontsize=12)

plt.show()
