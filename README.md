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
- **Protocol Distribution**: The most common protocols include ARP and NBNS.
- **Packet Length Distribution**: The majority of packets fall within a typical size range, with some outliers suggesting irregularities.
- **Source and Destination IPs**: A few source IPs dominate the traffic, with some destination IPs showing concentrated communication.

## Analysis and Discussion
The protocol distribution appears typical, but irregular packet lengths indicate possible misconfigurations or traffic shaping. Dominant source IPs suggest centralized services or network anomalies.

## Conclusion
The analysis reveals normal traffic patterns with some irregularities that need further investigation. Ongoing monitoring and deeper inspection of IP traffic are recommended for improved security and performance.
