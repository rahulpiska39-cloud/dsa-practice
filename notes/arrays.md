# Arrays

---

## Two Sum
Pattern: Hash Map

Idea:
Store visited numbers in dictionary.
Check if target - current exists.

Time: O(n)
Space: O(n)

---

## Remove Duplicates from Sorted Array
Pattern: Two Pointers

Idea:
Since array is sorted, duplicates are adjacent.
Move unique elements forward in-place.

Steps:
1. pos = 0
2. Loop from i = 1
3. If arr[i] != arr[pos]:
      pos += 1
      arr[pos] = arr[i]
4. Return pos + 1

Time: O(n)
Space: O(1)

Mistakes:
- Forgot self
- Wrong index assignment
- Returned None

---

## Move Zeroes
Pattern: Two Pointers

Idea:
Move non-zero elements forward.
Fill remaining with zeros.

Time: O(n)
Space: O(1)

Edge Cases:
- All zeros
- No zeros
- Single element

---

## Reverse String
Approach: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

---

## Product of Array Except Self
Approach: Prefix and Suffix Products

Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)

Key Idea: 
-Build left product in first pass, multiply by right product in second pass.

---

## Subarray Sum Equals K
Approach: Prefix Sum + Hashmap

Time Complexity: O(n)
Space Complexity: O(n)

Key Idea: 
-If current_sum - k exists in prefix_map, a valid subarray exists.

---

## Longest Substring Without Repeating Characters
Approach: Sliding Window with Set

Time Complexity: O(n)
Space Complexity: O(min(n, charset))

Key Idea: 
-Expand right pointer, shrink left pointer when duplicate found.

