from collections import deque

class RateLimiter:
    def __init__(self, max_requests: int, window_size_seconds: int):
        self.max_requests = max_requests
        self.window_size_seconds = window_size_seconds
        self.requests = deque() 

    def is_allowed(self, timestamp: int) -> bool:
        # 1. Remove expired requests
        while self.requests and self.requests[0] <= timestamp - self.window_size_seconds:
            self.requests.popleft()
            
        # 2. Check if we are under the limit
        if len(self.requests) < self.max_requests:
            self.requests.append(timestamp)
            return True
            
        # 3. Deny if limit is reached
        return False


def max_packets_in_window(packet_stream: list, window_size: int) -> int:
    """
    Calculates the maximum number of packets in any fixed-size time window.
    """
    if window_size <= 0 or not packet_stream or len(packet_stream) < window_size:
        return 0

    # 1. Initialize the first window
    current_window_sum = sum(packet_stream[:window_size])
    max_sum = current_window_sum
    
    # 2. Slide the window
    for i in range(window_size, len(packet_stream)):
        # Add the new packet entering the window, remove the one leaving
        current_window_sum += packet_stream[i] - packet_stream[i - window_size]
        
        # Update max
        max_sum = max(max_sum, current_window_sum)
        
    return max_sum


# ==========================================
# 🧪 TEST CASES
# ==========================================
if __name__ == "__main__":
    print("--- Testing Fixed Window (Max Packets) ---")
    # 1 means packet received, 0 means no packet
    stream = [1, 1, 0, 1, 1, 1, 0, 1]
    print(f"Max packets in window of size 3: {max_packets_in_window(stream, 3)}") 

    print("\n--- Testing Rate Limiter ---")
    # Allow max 3 requests every 10 seconds
    limiter = RateLimiter(max_requests=3, window_size_seconds=10)

    print(f"Time 1: {limiter.is_allowed(1)}")  # True (1 request)
    print(f"Time 2: {limiter.is_allowed(2)}")  # True (2 requests)
    print(f"Time 3: {limiter.is_allowed(3)}")  # True (3 requests)
    print(f"Time 4: {limiter.is_allowed(4)}")  # False (Limit reached!)
    print(f"Time 12: {limiter.is_allowed(12)}") # True (Time 1 has expired, window is now [2, 3, 12])