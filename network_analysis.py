# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv("Midterm_53_group.csv")

# Checking the first few rows and general information of the dataset
df.head()
df.info()

# Protocol distribution - Shows the most common protocols used in the network traffic
protocol_counts = df['Protocol'].value_counts()
protocol_counts.plot(kind='bar', color='skyblue')
plt.title('Protocol Distribution')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.show()

# Packet length distribution - Displays how packet sizes are distributed, helping to identify anomalies
plt.figure(figsize=(10,6))
plt.hist(df['Length'], bins=50, color='green', edgecolor='black')
plt.title('Packet Length Distribution')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()

# Source IP frequency - Highlights the top 10 source IPs in the traffic
top_sources = df['Source'].value_counts().head(10)
top_sources.plot(kind='bar', color='orange')
plt.title('Top 10 Source IPs')
plt.xlabel('Source IP')
plt.ylabel('Frequency')
plt.show()

# Packet distribution over time - Shows how the traffic varies over time
plt.figure(figsize=(10,6))
plt.hist(df['Time'], bins=50, color='blue', edgecolor='black')
plt.title('Packet Distribution Over Time')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
