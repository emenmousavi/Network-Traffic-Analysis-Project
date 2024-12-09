# Network Traffic Analysis
Network Traffic Analysis and Anomaly Detection

## Introduction
This project focuses on the analysis and identification of anomalies in network traffic data collected with Wireshark. The goal is to identify network communication patterns and detect any anomalies or suspicious activities. The data represents network activity during a one-hour period, including source and destination IP addresses, protocols, and packet sizes. Using visualization techniques, this study delves into traffic patterns and highlights areas that may require extra monitoring.

You can access the dataset for this project from [Kaggle Network Traffic Dataset](https://www.kaggle.com/datasets/ravikumargattu/network-traffic-dataset).

## Technical Overview
This project was created using **Python**, **Pandas** for data manipulation, and **Matplotlib** for visualization. The code processes network traffic statistics, managing missing values and displaying protocol distributions, packet lengths, and source IP addresses. **Pandas** was used to clean and organize the data, while **Matplotlib** generated the charts required to examine traffic patterns and probable anomalies over time.

## GOALS
- Analyze the network traffic data and identify common traffic patterns.
- Visualize traffic behavior through protocol distributions, packet lengths, and source/destination IP addresses.
- Apply anomaly detection techniques to highlight potential irregularities or security concerns in the traffic flow.

## Methodology
The data was cleaned, and missing values were handled. Visualizations were created for:
- Protocol distribution
- Packet length distribution
- Frequency of source and destination IPs
- Anomaly detection techniques were applied to identify unusual traffic patterns.

## Results
- **Protocol Distribution**: The most common protocols include DNS and TCP.
  
From the graph, TCP dominates the traffic with over 300,000 packets, which is typical for network communications. TLSv1.3 follows with approximately 75,000 packets, indicating secure encrypted traffic. The low frequency of ICMP and DNS points to less reliance on these protocols, suggesting a focus on data transfer.

  ![Protocol Distribution](https://github.com/user-attachments/assets/b47561aa-f334-4acc-bd9b-63a948dae3fd)
  
- **Packet Length Distribution**: The majority of packets fall within a typical size range, with some outliers suggesting irregularities.

Most packets are small, concentrated in the 0-1000 unit range, typical of control or small data packets. Sparse large packets (over 10,000 units) may represent large data transfers or anomalies.

  ![Packet Length Distribution](https://github.com/user-attachments/assets/46fff15f-4da3-4765-903b-0a15cb23caa4)

- **Top 10 Source IPs**: A few source IPs dominate the traffic.

The IP 192.167.7.162 contributes a significant portion of the traffic, indicating a central server or high-activity device. The other IPs show less frequent but varied traffic.

  ![Top 10 Source IPs](https://github.com/user-attachments/assets/1fc3ce3b-843b-4109-a929-5ae0709961be)

- **Packet Distribution Over Time**: The distribution of packets over the time period.

Peaks at intervals like 400, 800, and 1200 suggest bursts of activity, possibly from network congestion or batch processing. These fluctuations point to potential anomalies or specific network events.

  ![Packet Distribution Over Time](https://github.com/user-attachments/assets/9e6db047-c8a6-4e0a-beb8-7967d86c8d5b)


## Analysis and Discussion
The protocol distribution shows common protocols like ARP and TCP, with few irregularities. However, the packet length distribution reveals high frequencies for lengths under 5000 bytes, which could suggest network traffic shaping. The concentration of specific source and destination IPs highlights key services or potential misconfigurations, pointing to areas for further investigation.

## Conclusion

The analysis shows mostly typical network behavior with some irregularities requiring further investigation. It is recommended to continuously monitor traffic patterns and investigate IPs with high activity to ensure the network’s optimal performance and security.
