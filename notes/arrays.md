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
