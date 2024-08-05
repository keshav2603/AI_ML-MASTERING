import matplotlib.pyplot as plt
import numpy as np
# bar plot 
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# name=["keshav","paras", "lovenish"]
# income= [1000000,450000,500000]
# plt.xlabel("Name")
# plt.ylabel("income")
# plt.title("income of three brother")
# # plt.bar(name,income)
# color = ["r", "y", "g"]
# # plt.bar(name,income, width=0.4, color=color)
# # plt.bar(name,income, width=0.4, color=color, align="edge")
# # plt.bar(name,income, width=0.4, color=color, edgecolor="m", linewidth=10, linestyle=":",alpha=0.2)
# # plt.bar(name,income, width=0.4, color=color,label ="income" )
# plt.legend()
# plt.show()

# name=["keshav", "paras", "ansh","lovnish"]
# y1=[20,40,60,80]
# y2=[15, 20,30,50]
# plt.bar(name, y1, color="r", width=0.5,  label ="math marks")
# plt.bar(name, y2, color="y", width=0.5, label= "sci marks" )
# plt.legend()
# plt.show()

# name=["keshav", "paras", "ansh","lovnish"]
# y1=[20,40,60,80]
# y2=[15, 20,30,50]
# width=0.2
# p=np.arange(len(name))
# p1=[j+width for j in p]
# plt.bar(p, y1, color="r", width=width,  label ="math marks")
# plt.bar(p1, y2, color="y", width=width, label= "sci marks" )
# plt.legend()
# plt.show()

# width = 0.2
# p = np.arange(len(name))
# p1 = [j + width for j in p]

# plt.bar(p, y1, color="r", width=width, label="Math Marks")
# plt.bar(p1, y2, color="y", width=width, label="Sci Marks")
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title("Marks Comparison")
# plt.xticks(p + width / 2, name, rotation=20)  # Center the x-ticks
# plt.legend()
# plt.show()


# scatter plot

# basic 
x=[1,2,3,4,5]
y=[2,4,6,8,10]
y1=[3,5,4,1,0]
size=[100,90,80,50,20]
# plt.scatter(x,y, color="r", s=size, marker="*")
plt.scatter(x,y, color="r", s=size)
plt.scatter(x,y1, color="y", s=size)
plt.show()