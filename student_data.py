import numpy as np
import matplotlib.pyplot as plt
labels=["pass","fail","absent"]
students=[30,15,4]
plt.pie(
    students,
    labels=labels,
    autopct=("%.0f%%"),
    colors=("red","green","blue"),
    explode=(0,0.1,0),
)
plt.title("Students")
plt.savefig("piechart.png")
plt.show()