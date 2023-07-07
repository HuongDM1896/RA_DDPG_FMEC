import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('F:\ANDA lab\Project 2\HuongCheck\Output.xlsx', sheet_name="LR")
x=df["Episode:"]
y1=df["first"]
y2=df["second"]
y3=df["ther"]
fix, ax = plt.subplots(figsize=(5, 4))
ax.plot(x,y2,':', label = 'LR = 0.0001')
ax.plot(x,y1, '-' , label = 'LR = 0.001')
ax.plot(x,y3,'--', label = 'LR = 0.01')

plt.xlabel('Episode')
plt.ylabel('Delay-energy cost')
plt.legend(loc='best')
plt.show()