

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("data2.xlsx")
print(data)

fig, axs = plt.subplots(3, 1)

axs[0].plot(data.index, data["score"])
axs[0].set_title("score stats")
axs[0].set_xlabel("frequency")
axs[0].set_ylabel("score")

axs[1].plot(data.index, data["wrong"])
axs[1].set_title("wrong stats")
axs[1].set_xlabel("frequency")
axs[1].set_ylabel("wrong")

print(data.corr())
sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")

axs[2].plot(data.index, data["total"])
axs[2].set_title("total stats")
axs[2].set_xlabel("frequency")
axs[2].set_ylabel("total")

plt.tight_layout()

# Set the size of the graph to match the tkinter application
fig.set_size_inches(9.9, 6.0)  # 990x660 pixels

# Set the window position
plt.get_current_fig_manager().window.wm_geometry("+130+30")

plt.show()
