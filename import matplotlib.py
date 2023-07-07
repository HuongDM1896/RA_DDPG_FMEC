import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('F:\ANDA lab\Project 2\HuongCheck\Output.xlsx', sheet_name="Ori 10")
x=df["Episode:"]
y1=df["Ori"]
y2=df["RRA"]
y3=df["URA"]
y4=df["PER"]
fix, ax = plt.subplots(figsize=(5, 4))
ax.plot(x,y2,':', label = 'RRA')
ax.plot(x,y3,'--', label = 'URA')
ax.plot(x,y1, '-' , label = 'DDPG')
ax.plot(x,y4, label = 'DDPG-PER')
plt.xlabel('Episode')
plt.ylabel('Delay-energy cost')
plt.legend(loc='best')
plt.show()