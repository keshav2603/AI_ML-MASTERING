import matplotlib.pyplot as plt
import numpy as np
import random
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

# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# y1=[3,5,4,1,0]
# size=[100,90,80,50,20]
# # plt.scatter(x,y, color="r", s=size, marker="*")
# plt.scatter(x,y, color="r", s=size)
# plt.scatter(x,y1, color="y", s=size)
# plt.show()

# histogram plot

# l=[20,40,60,80]
# no = [42, 74, 73, 72, 27, 79, 42, 33, 62, 34, 14, 66, 63, 56, 65, 41, 30, 85, 42, 37, 36, 22, 87, 48, 49, 40, 64, 90, 53, 79, 69, 34, 49, 57, 45, 53, 61, 72, 57, 27, 70, 41, 59, 45, 32, 56, 25, 27, 80, 63]
# plt.hist(no, color="b", edgecolor="black", bins=l)
# plt.hist(no, color="b", edgecolor="black", bins="auto", range=(0,200),cumulative=1)
# plt.hist(no, color="b", edgecolor="black",bottom=20)
# plt.hist(no, color="b", edgecolor="black",histtype="step")
# plt.hist(no, color="b", edgecolor="black",histtype="stepfilled")
# plt.hist(no, color="b", edgecolor="black",histtype="bar")
# plt.hist(no, color="b", edgecolor="black",histtype="barstacked")
# plt.hist(no, color="b", edgecolor="black",orientation="horizontal")
# plt.hist(no, color="b", edgecolor="black",rwidth=0.6)
# plt.hist(no, color="b", edgecolor="black")
# plt.axvline(45,color="r")
# plt.show()

# pie plot 

# x=[10,20,30,40]
# ex=[0.2,0.0,0.0,0.0]
# y=["ansh","aryan","paras","love"]
# plt.pie(x,labels=y, explode=ex, autopct="%0.1f%%", shadow=True,startangle=90,textprops={"fontsize":15},counterclock=False, wedgeprops={"linewidth":2},rotatelabels=True)
# plt.show()

# x=[10,20,30,40]
# y=["ansh","aryan","paras","love"]
# plt.pie(x,labels=y,radius=1)
# plt.pie([1],colors="white",radius=0.5)
# plt.show()

cr=plt.Circle(xy=(0,0),radius=1,facecolor="w")
plt.gca().add_artist(cr)