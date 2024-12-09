# Network Traffic Analysis
Network Traffic Analysis and Anomaly Detection

## Introduction
This project analyzes network traffic data captured via Wireshark on October 9th, 2023. The dataset includes network traffic from a one-hour period with key features such as source/destination IPs, protocols, and packet lengths. The goal is to visualize traffic patterns and identify potential anomalies.

You can access the dataset for this project from [Kaggle Network Traffic Dataset](https://www.kaggle.com/datasets/ravikumargattu/network-traffic-dataset).

## Methodology
The data was cleaned and missing values were handled. Visualizations were created for:
- Protocol distribution
- Packet length distribution
- Frequency of source and destination IPs  
Anomaly detection techniques were applied to identify unusual traffic patterns.

## Results
- **Protocol Distribution**: The most common protocols include DNS and TCP.
  
  From the graph, we can see that TCP dominates the traffic, with over 300,000 packets, which is typical for most network communications. TLSv1.3 also stands out with around 75,000 packets, indicating secure     encrypted traffic. The near-zero occurrences of ICMP and DNS suggest these protocols aren't being used much, possibly pointing to a focus on data transfer rather than diagnostic or name resolution operations. This might indicate the network is handling mainly secure, application-level traffic.
  ![Protocol Distribution](https://github.com/user-attachments/assets/b47561aa-f334-4acc-bd9b-63a948dae3fd)
- **Packet Length Distribution**: The majority of packets fall within a typical size range, with some outliers suggesting irregularities.
  ![Packet Length Distribution](https://github.com/user-attachments/assets/46fff15f-4da3-4765-903b-0a15cb23caa4)

- **Top 10 Source IPs**: A few source IPs dominate the traffic.
  ![Top 10 Source IPs](https://github.com/user-attachments/assets/1fc3ce3b-843b-4109-a929-5ae0709961be)

- **Packet Distribution Over Time**: The distribution of packets over the time period.
  ![Packet Distribution Over Time](https://github.com/user-attachments/assets/9e6db047-c8a6-4e0a-beb8-7967d86c8d5b)


## Analysis and Discussion
The protocol distribution appears typical, but irregular packet lengths indicate possible misconfigurations or traffic shaping. Dominant source IPs suggest centralized services or network anomalies.

## Conclusion
The analysis reveals normal traffic patterns with some irregularities that need further investigation. Ongoing monitoring and deeper inspection of IP traffic are recommended for improved security and performance.
