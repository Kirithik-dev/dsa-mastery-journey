#  Network Packet Rate Limiter

A backend utility built using the **Fixed-Size Sliding Window** technique to simulate network traffic monitoring and request rate limiting.

## 📌 Project Overview
1. **Max Packets in Window:** Calculates the maximum number of network packets received in any given fixed time window.
2. **Rate Limiter:** A class-based implementation that allows or denies API requests based on a maximum threshold within a specific time frame.

##  Key DSA Concepts Applied
- **Algorithm:** Fixed-Size Sliding Window.
- **Time Complexity:** $O(N)$ for packet stream analysis; $O(1)$ amortized for rate limiting.
- **Space Complexity:** $O(K)$ where $K$ is the maximum number of allowed requests.