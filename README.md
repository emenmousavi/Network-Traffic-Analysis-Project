# Network Traffic Analysis
Network Traffic Analysis and Anomaly Detection

## Introduction
This project analyzes network traffic data captured via Wireshark on October 9th, 2023. The dataset includes network traffic from a one-hour period, featuring source/destination IPs, protocols, and packet lengths. This dataset is valuable for understanding typical and unusual network patterns, which is crucial for identifying anomalies and enhancing network security.

You can access the dataset for this project from [Kaggle Network Traffic Dataset](https://www.kaggle.com/datasets/ravikumargattu/network-traffic-dataset).

## Technical Overview

This project was developed using **Python** with **Pandas** for data manipulation and **Matplotlib** for visualizations. The code processes network traffic data, handling missing values and visualizing protocol distributions, packet lengths, and source IPs. **Pandas** was used for data cleaning and organization, while **Matplotlib** created the necessary plots to analyze traffic patterns and potential anomalies over time.

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
