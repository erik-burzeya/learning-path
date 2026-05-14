from matplotlib import pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
hours_spent = [4, 4.66, 3, 8.4, 2.12, 4, 4.9]

plt.plot(days, hours_spent, color='red', marker='o', linestyle='solid')

plt.title("Hours/Day spent studying")

plt.ylabel("t in h")

plt.xlabel("Days")
plt.show()
