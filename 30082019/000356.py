from matplotlib import pyplot as plt 

# defino dos listas
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x,dev_y) # GRAFICO LAS DOS LISTAS DEFINIDAS ANTERIORMENTE

plt.xlabel("Ages") # titulo eje x
plt.ylabel("Median Salary (USD)") # titulo eje y
plt.title("Median Salary (USD) by Age") # titulo del grafico
plt.show()


