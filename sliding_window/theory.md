# 🪟 Sliding Window Technique

**Definition:** An algorithmic technique used to solve problems involving contiguous subarrays or substrings. It optimizes nested loop solutions from **O(n²) to O(n)** by reusing computations from the previous window.

## 🎯 How to Identify
Look for these keywords in the problem statement:
- Find the **longest/shortest** contiguous subarray/substring.
- Find a subarray/substring that **satisfies a specific condition** (e.g., sum > target, all unique characters).
- The problem explicitly gives a **fixed window size `k`**.

---

## 🛠️ 1. Fixed-Size Sliding Window
**Use when:** The window size `k` is explicitly given.

```python
def fixed_sliding_window(arr, k):
    # 1. Initialize the first window
    current_window_state = sum(arr[:k])
    best_result = current_window_state
    
    # 2. Slide the window from index k to the end
    for right in range(k, len(arr)):
        # Add the new element entering the window
        current_window_state += arr[right]
        # Remove the old element leaving the window
        current_window_state -= arr[right - k]
        
        # Update the result
        best_result = max(best_result, current_window_state)
        
    return best_result

---
## 🛠️ 2. Variable-Size Sliding Window
**Use when:** The window size is dynamic, and you need to expand/shrink based on a condition.

```python
def dynamic_sliding_window(arr, target_condition):
    left = 0
    # Pro-Tip: Use collections.Counter or defaultdict(int) for cleaner code!
    window_state = {} 
    best_result = 0  # Use float('inf') if finding minimum length
    
    # Expand window using the 'right' pointer
    for right in range(len(arr)):
        # Add arr[right] to window state
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1
        
        # Shrink window from the left until condition is valid
        while not is_condition_valid(window_state, target_condition):
            window_state[arr[left]] -= 1
            if window_state[arr[left]] == 0:
                del window_state[arr[left]]
            left += 1
            
        # Update result (window length is right - left + 1)
        best_result = max(best_result, right - left + 1)
        
    return best_result

