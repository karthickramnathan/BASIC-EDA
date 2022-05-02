import pandas as p
import matplotlib.pyplot as plt
file=p.read_csv("iris.data")
p.DataFrame(file)
file.columns=["petal length","petal width","sepal length","sepal width","specious"]
d=file.describe()
print(d)
# file.groupby(["specious"]).plot(kind="box")
# plt.show()

a=file.groupby(["specious"])["petal length"].median().plot(kind="bar")
a.set_ylabel("median petallength")
plt.show()
b=file.groupby(["specious"])["petal length"].mean().plot(kind="bar")
b.set_ylabel("mean petallength")
plt.show()
c=file.groupby(["specious"])["petal width"].median().plot(kind="bar")
c.set_ylabel("median petalwidth")
plt.show()
d=file.groupby(["specious"])["petal width"].mean().plot(kind="bar")
d.set_ylabel("median petalwidth")
plt.show()
e=file.groupby(["specious"])["sepal length"].median().plot(kind="bar")
e.set_ylabel("median psepallength")
plt.show()
f=file.groupby(["specious"])["sepal width"].mean().plot(kind="bar")
f.set_ylabel("median sepalwidth")
plt.show()
file.groupby(["specious"]).plot(kind="box")


