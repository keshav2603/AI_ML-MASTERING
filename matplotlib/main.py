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

# cr=plt.Circle(xy=(0,0),radius=1,facecolor="w")
# plt.gca().add_artist(cr)

# stem plot

x = [1, 2, 3, 4, 5]
y = [2, 5, -4, 7, -2]

# plt.stem(x, y, linefmt=":")
# plt.stem(x, y, linefmt="-")
# plt.stem(x, y, linefmt="-.")
# plt.stem(x, y, linefmt="-.", markerfmt="r*")
# plt.stem(x, y, linefmt="-.", markerfmt="r*", orientation="horizontal")

# plt.show()

# box plot

# x=[10,20,30,40, 50,60]
# x2=[10,20,30,40, 50,60,120]

# plt.boxplot(x)
# plt.boxplot(x, notch=True)
# plt.boxplot(x, vert=False)
# plt.boxplot(x, labels=["python"],patch_artist=True,showmeans=True)
# plt.boxplot(x2, labels=["python"],patch_artist=True,showmeans=True, whis=10)
# plt.boxplot(x, labels=["python"],patch_artist=True,showmeans=True,sym="g+",
#             boxprops={"color":"r" },
#             capprops={"color":"r"},
#             whiskerprops={"color":"r"}
#             )
# plt.show()

# x=[10,30,50,70]
# x2=[20, 40,60,80]
# y=[x, x2]
# plt.boxplot(y)
# plt.show()


# stack plot

# x=[10,20,30,40,50]
# y=[12,40,50,30,25]
# y1=[100,20,10,40,55]
# y2=[50,43,50,60,25]
# l=["area1","area2","area3"]
# # plt.stackplot(x,y,y1,y2,labels=l, colors=["r","b","y"], baseline="sym")
# # plt.stackplot(x,y,y1,y2,labels=l, colors=["r","b","y"], baseline="wiggle")
# plt.stackplot(x,y,y1,y2,labels=l, colors=["r","b","y"], baseline="weighted_wiggle")
# plt.legend(loc=2)
# plt.show()


# step plot

# x=[10,20,30,40,50]
# y=[12,40,50,30,25]

# plt.step(x,y, marker="o", ms=10, mfc="g")
# plt.grid()
# plt.show()
# can give more paremitter as in liner plot


# fill_between plot

x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.plot(x, y)
plt.fill_between(x,y)
plt.fill_between(x=[2,4],y1=[2,4])
plt.show()
