import matplotlib.pyplot as plt

# bar plot 
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
name=["keshav","paras", "lovenish"]
income= [1000000,450000,500000]
plt.xlabel("Name")
plt.ylabel("income")
plt.title("income of three brother")
# plt.bar(name,income)
color = ["r", "y", "g"]
# plt.bar(name,income, width=0.4, color=color)
# plt.bar(name,income, width=0.4, color=color, align="edge")
# plt.bar(name,income, width=0.4, color=color, edgecolor="m", linewidth=10, linestyle=":",alpha=0.2)
plt.bar(name,income, width=0.4, color=color,label ="income" )
plt.legend()
plt.show()