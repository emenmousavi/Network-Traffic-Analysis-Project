import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Midterm_53_group.csv')

df.head()
df.info()

protocol_counts = df['Protocol'].value_counts()
protocol_counts.plot(kind='bar', color='skyblue')
plt.title('Protocol Distribution')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['Length'], bins=50, color='green', edgecolor='black')
plt.title('Packet Length Distribution')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()

top_sources = df['Source'].value_counts().head(10)
top_sources.plot(kind='bar', color='orange')
plt.title('Top 10 Source IPs')
plt.xlabel('Source IP')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['Time'], bins=50, color='blue', edgecolor='black')
plt.title('Packet Distribution Over Time')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
