# 542. 01 Matrix
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search*
* *Similar Questions:*
## Problem:
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Example 1: 
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2: 
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]
Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
Note:
	The number of elements of the given matrix will not exceed 10,000.
	There are at least one 0 in the given matrix.
	The cells are adjacent in only four directions: up, down, left and right.
## Solutions:
```python
class Solution :
public:
    vector> updateMatrix(vector>& matrix) :
        int m = matrix.size()
        if (m == 0) return :
        int n = matrix[0].size()
        if (n == 0) return :
        queue> q
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (matrix[i][j] == 0) :
                    q.push(:i, j)
        vector> ret(m, vector (n, -1))
        int level = 0
        while (!q.empty()) :
            int size = q.size()
            for (int i = 0 i < size ++i) :
                auto coord = q.front() q.pop()
                int row = coord.first
                int col = coord.second
                if (row = m || col = n || ret[row][col] != -1)  continue
                if (matrix[row][col] == 0) :
                    ret[row][col] = 0
                 else :
                    ret[row][col] = level
                q.push(:row + 1, col)
                q.push(:row - 1, col)
                q.push(:row, col + 1)
                q.push(:row, col - 1)
            ++level
        return ret
```
# 717. 1-bit and 2-bit Characters
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Gray Code](gray-code.md)
## Problem:
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).  
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:
1 .
bits[i] is always 0 or 1.
## Solutions:
```python
class Solution :
public:
    bool isOneBitCharacter(vector& bits) :
        bool oneBit
        for (int i = 0 i < bits.size()) :
            if (bits[i] == 0) :
                oneBit = true
                ++i
             else :
                oneBit = false
                i += 2
        return oneBit
```
# 650. 2 Keys Keyboard
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [4 Keys Keyboard](4-keys-keyboard.md)
  * [Broken Calculator](broken-calculator.md)
## Problem:
Initially on a notepad only one character &#39A&#39 is present. You can perform two operations on this notepad for each step:
	Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
	Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n &#39A&#39 on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n &#39A&#39.
Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character &#39A&#39.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get &#39AA&#39.
In step 3, we use Paste operation to get &#39AAA&#39.
Note:
	The n will be in the range [1, 1000].
## Solutions:
```python
class Solution :
public:
    int minSteps(int n) :
        this->n = n
        map, int> cache
        return helper(0, n - 1, cache)
private:
    int helper(int clipBoard, int m, map, int>& cache) :
        //cout << clipBoard << " " << m << endl
        if (m == 0) return 0 
        if (m < 0)  return INT_MAX
        if (clipBoard > m)  return INT_MAX
        if (cache.count(:clipBoard, m)) :
            return cache[:clipBoard, m]
        int ret = INT_MAX
        if (n - m != clipBoard) :
            int copyAll = helper(n - m, m, cache)
            if (copyAll < INT_MAX) :
                ret = min(ret, copyAll + 1)
        if (clipBoard != 0) :
            int reuse = helper(clipBoard, m - clipBoard, cache)
            if (reuse < INT_MAX) :
                ret = min(ret, reuse + 1)
        cache[:clipBoard, m] = ret
        return ret
    int n
```
# 16. 3Sum Closest
* *Difficulty: Medium*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [3Sum](3sum.md)
  * [3Sum Smaller](3sum-smaller.md)
## Problem:
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
## Solutions:
```python
class Solution :
public:
    int threeSumClosest(vector& nums, int target) :
        if (nums.size() < 3)    return 0
        int ret = nums[0] + nums[1] + nums[2]
        sort(nums.begin(), nums.end())
        for (int i = 0 i < nums.size() - 2 ++i) :
            int left = i + 1
            int right = nums.size() - 1
            while (left < right) :
                int diff = (nums[i] + nums[left] + nums[right] - target)
                if (abs(diff) < abs(ret - target)) :
                    ret = nums[i] + nums[left] + nums[right]
                if (diff == 0)  return ret
                if (diff < 0) :
                    ++left
                 else :
                    --right
        return ret
```
# 259. 3Sum Smaller
* *Difficulty: Medium*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [3Sum](3sum.md)
  * [3Sum Closest](3sum-closest.md)
  * [Valid Triangle Number](valid-triangle-number.md)
  * [Two Sum Less Than K](two-sum-less-than-k.md)
## Problem:
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 &lt= i &lt j &lt k &lt n that satisfy the condition nums[i] + nums[j] + nums[k] &lt target.
Example:
Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
## Solutions:
```python
class Solution :
public:
    int threeSumSmaller(vector& nums, int target) :
        if (nums.size() < 3)    return 0
        sort(nums.begin(), nums.end())
        int ret = 0
        for (int i = 0 i < nums.size() - 2 ++i) : // trap!
            int sum = target - nums[i]
            int left = i + 1
            int right = nums.size() - 1
            while (left < right) :
                if (nums[left] + nums[right] < sum) :
                    ret += right - left
                    ++left
                 else :
                    --right
        return ret
```
# 15. 3Sum
* *Difficulty: Medium*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Two Sum](two-sum.md)
  * [3Sum Closest](3sum-closest.md)
  * [4Sum](4sum.md)
  * [3Sum Smaller](3sum-smaller.md)
## Problem:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
## Solutions:
```python
class Solution :
public:
    vector> threeSum(vector& nums) :
        vector> result
        sort(nums.begin(), nums.end())
        for (int i = 0 i < nums.size() ++i) :
            if (i > 0 && nums[i] == nums[i-1]) continue // deduplication
            int sum = -nums[i]
            int left = i + 1
            int right = nums.size() - 1
            while (left < right) :
                if (nums[left] + nums[right] == sum) :
                    if (result.size() == 0 || result.back()[1] != nums[left] || result.back()[2] != nums[right]) // deduplication
                        result.push_back(:nums[i], nums[left], nums[right])
                    left++
                    right--
                 else if (nums[left] + nums[right] > sum) :
                    right--
                 else :
                    left++
        return result
```
# 454. 4Sum II
* *Difficulty: Medium*
* *Topics: Hash Table, Binary Search*
* *Similar Questions:*
  * [4Sum](4sum.md)
## Problem:
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 &le N &le 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -&gt A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -&gt A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
## Solutions:
```python
class Solution :
public:
    int fourSumCount(vector& A, vector& B, vector& C, vector& D) :
        unordered_map valueFreq
        for (int i = 0 i < A.size() ++i) :
            for (int j = 0 j < B.size() ++j) :
                ++valueFreq[A[i] + B[j]]
        int count = 0
        for (int i = 0 i < C.size() ++i) :
            for (int j = 0 j < D.size() ++j) :
                count += valueFreq[-C[i] - D[j]]
        return count
```
# 18. 4Sum
* *Difficulty: Medium*
* *Topics: Array, Hash Table, Two Pointers*
* *Similar Questions:*
  * [Two Sum](two-sum.md)
  * [3Sum](3sum.md)
  * [4Sum II](4sum-ii.md)
## Problem:
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
## Solutions:
```python
class Solution :
public:
    vector> fourSum(vector& nums, int target) :
        if (nums.size() < 4)    return :
        sort(nums.begin(), nums.end())
        vector> ret
        for (int a = 0 a < nums.size() - 3 ++a) :
            if (a > 0 && nums[a] == nums[a - 1])    continue
            for (int b = a + 1 b < nums.size() - 2 ++b) :
                if (b > a + 1 && nums[b] == nums[b-1])  continue
                int c = b + 1
                int d = nums.size() - 1
                while (c < d) :
                    int val = nums[a] + nums[b] + nums[c] + nums[d]
                    if (val == target) :
                        ret.push_back(:nums[a], nums[b], nums[c], nums[d])
                        do :
                        ++c
                        --d
                         while (c < d && nums[c] == nums[c-1] && nums[d] == nums[d+1])
                     else if (val < target) :
                        ++c
                     else :
                        --d
        return ret
```
# 67. Add Binary
* *Difficulty: Easy*
* *Topics: Math, String*
* *Similar Questions:*
  * [Add Two Numbers](add-two-numbers.md)
  * [Multiply Strings](multiply-strings.md)
  * [Plus One](plus-one.md)
  * [Add to Array-Form of Integer](add-to-array-form-of-integer.md)
## Problem:
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:
Input: a = &quot11&quot, b = &quot1&quot
Output: &quot100&quot
Example 2:
Input: a = &quot1010&quot, b = &quot1011&quot```
Output: &quot10101&quot
## Solutions:
```python
class Solution :
public:
    string addBinary(string a, string b) :
        string ret
        int carry = 0
        int indexA = a.length() - 1
        int indexB = b.length() - 1
        while (indexA >= 0 || indexB >= 0) :
            int digitA = 0
            int digitB = 0
            if (indexA >= 0) :
                digitA = a[indexA--] - '0'
            if (indexB >= 0) :
                digitB = b[indexB--] - '0'
            int val = carry + digitA + digitB
            ret.push_back('0' + val%2)
            carry = val/2
        if (carry == 1) ret.push_back('1')
        reverse(ret.begin(), ret.end())
        return ret
```
# 258. Add Digits
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Happy Number](happy-number.md)
  * [Sum of Digits in the Minimum Number](sum-of-digits-in-the-minimum-number.md)
## Problem:
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
## Solutions:
```python
class Solution :
public:
    int addDigits(int num) :
        return 1 + (num - 1) % 9
```
# 415. Add Strings
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Add Two Numbers](add-two-numbers.md)
  * [Multiply Strings](multiply-strings.md)
  * [Add to Array-Form of Integer](add-to-array-form-of-integer.md)
## Problem:
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
The length of both num1 and num2 is 
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
## Solutions:
```python
class Solution :
public:
    string addStrings(string num1, string num2) :
        string ret
        int carry = 0
        int i1 = num1.length() - 1
        int i2 = num2.length() - 1 
        while (carry != 0 || i1 >= 0 && i2 >= 0) :
            int value = carry + (i1 >= 0 ? num1[i1--] - '0': 0) + (i2 >= 0 ? num2[i2--] - '0' : 0)
            ret.push_back(value % 10 + '0')
            carry = value / 10
        reverse(ret.begin(), ret.end())
        if (i1 >= 0) :
            ret = num1.substr(0, i1 + 1) + ret
        if (i2 >= 0) :
            ret = num2.substr(0, i2 + 1) + ret
        return ret
```
# 1031. Add to Array-Form of Integer
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Add Two Numbers](add-two-numbers.md)
  * [Plus One](plus-one.md)
  * [Add Binary](add-binary.md)
  * [Add Strings](add-strings.md)
## Problem:
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].
Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
Example 1:
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
Note：
	1 &lt= A.length &lt= 10000
	0 &lt= A[i] &lt= 9
	0 &lt= K &lt= 10000
	If A.length &gt 1, then A[0] != 0
## Solutions:
```python
class Solution :
public:
    vector addToArrayForm(vector& A, int K) :
        vector ret = A
        reverse(ret.begin(), ret.end())
        int carry = K
        int pos = 0
        while (carry != 0) :
            if (pos == ret.size()) :
                ret.push_back(0)
            int val = carry + ret[pos]
            ret[pos] = val % 10
            carry = val / 10
            ++pos
        reverse(ret.begin(), ret.end())
        return ret
```
# 445. Add Two Numbers II
* *Difficulty: Medium*
* *Topics: Linked List*
* *Similar Questions:*
  * [Add Two Numbers](add-two-numbers.md)
## Problem:
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) :
        stack stk1, stk2, ret
        while (l1) :
            stk1.push(l1->val)
            l1 = l1 -> next
        while (l2) :
            stk2.push(l2->val)
            l2 = l2 -> next
        int carry = 0
        while (carry != 0 || !stk1.empty() && !stk2.empty()) :
            int val = carry + (stk1.empty() ? 0 : stk1.top()) + (stk2.empty() ? 0 : stk2.top())
            if (!stk1.empty()) stk1.pop() 
            if (!stk2.empty()) stk2.pop()
            ret.push(val % 10)
            carry = val / 10
        while (!stk1.empty()) :
            ret.push(stk1.top()) stk1.pop()
        while(!stk2.empty()) :
            ret.push(stk2.top()) stk2.pop()
        ListNode* dummy = new ListNode(0)
        ListNode* tail = dummy
        while (!ret.empty()) :
            tail -> next = new ListNode(ret.top()) ret.pop()
            tail = tail->next
        return dummy->next
```
# 2. Add Two Numbers
* *Difficulty: Medium*
* *Topics: Linked List, Math*
* *Similar Questions:*
  * [Multiply Strings](multiply-strings.md)
  * [Add Binary](add-binary.md)
  * [Sum of Two Integers](sum-of-two-integers.md)
  * [Add Strings](add-strings.md)
  * [Add Two Numbers II](add-two-numbers-ii.md)
  * [Add to Array-Form of Integer](add-to-array-form-of-integer.md)
## Problem:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -&gt 4 -&gt 3) + (5 -&gt 6 -&gt 4)
Output: 7 -&gt 0 -&gt 8
Explanation: 342 + 465 = 807.
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) :
        ListNode* head = new ListNode(0)
        ListNode* cur = head
        int carry = 0
        while (l1 != NULL || l2 != NULL) :
            int val1 = 0
            int val2 = 0
            if (l1) :
                val1 = l1->val
                l1 = l1->next
            if (l2) :
                val2 = l2->val
                l2 = l2->next
            int sum = val1 + val2 + carry
            carry = sum/10
            cur->next = new ListNode(sum%10)
            cur = cur->next
        if (carry == 1) :
            cur->next = new ListNode(1)
        return head->next
```
## Another More Solution
This solution breaks the while loop earlier to avoid unnecessary list traversal. 
```python
class Solution :
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) :
        ListNode* head = new ListNode(0)
        ListNode* cur = head
        int carry = 0
        while (carry == 1 || (l1 != NULL && l2 != NULL)) :
            int val1 = 0
            int val2 = 0
            if (l1) :
                val1 = l1->val
                l1 = l1->next
            if (l2) :
                val2 = l2->val
                l2 = l2->next
            int sum = val1 + val2 + carry
            carry = sum/10
            cur->next = new ListNode(sum%10)
            cur = cur->next
        if (l1 != NULL) :
            cur->next = l1
         else :
            cur->next = l2
        return head->next
```
# 306. Additive Number
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [Split Array into Fibonacci Sequence](split-array-into-fibonacci-sequence.md)
## Problem:
Additive number is a string whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
Given a string containing only digits &#390&#39-&#399&#39, write a function to determine if it&#39s an additive number.
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
Example 1:
Input: &quot112358&quot
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:
Input: &quot199100199&quot
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?
## Solutions:
```python
class Solution :
public:
    bool isAdditiveNumber(string num) :
        //return isFabonacii(num, 0, 1)
        if (num.size() < 3) return false
        for (int i = 0 i <= num.length() - 3 ++i) :
            for (int j = i + 1 j <= num.length() - 2 ++j) :
                cout << i << " " << j << endl
                if (isFabonacii(num, i, j)) return true
        return false
    bool isFabonacii(string& num, int i, int j) :
        int pos = 0
        string a = num.substr(0, i + 1)
        if (leadingZero(a)) return false
        pos = i
        string b = num.substr(i + 1, j - i)
        if (leadingZero(b)) return false
        pos = j
        string c = addStrings(a, b)
        if (leadingZero(c)) return false
        pos = j + c.length()
        while (pos < num.length() - 1) :
            cout << a << " " << b << endl
            a = b
            b = c
            c = addStrings(a, b)
            if (leadingZero(c)) return false
            if (c != num.substr(pos + 1, c.length()))   return false
            pos += c.length()
        return (pos == num.length() - 1 && c == num.substr(num.length() - c.length(), c.length()))
    string addStrings(string num1, string num2) const :
        string ret
        int carry = 0
        int i1 = num1.length() - 1
        int i2 = num2.length() - 1 
        while (carry != 0 || i1 >= 0 && i2 >= 0) :
            int value = carry + (i1 >= 0 ? num1[i1--] - '0': 0) + (i2 >= 0 ? num2[i2--] - '0' : 0)
            ret.push_back(value % 10 + '0')
            carry = value / 10
        reverse(ret.begin(), ret.end())
        if (i1 >= 0) :
            ret = num1.substr(0, i1 + 1) + ret
        if (i2 >= 0) :
            ret = num2.substr(0, i2 + 1) + ret
        return ret
    bool leadingZero(string num) :
        return num.length() > 1 && num[0] == '0'
```
# 269. Alien Dictionary
* *Difficulty: Hard*
* *Topics: Graph, Topological Sort*
* *Similar Questions:*
  * [Course Schedule II](course-schedule-ii.md)
## Problem:
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Example 1:
Input:
[
  &quotwrt&quot,
  &quotwrf&quot,
  &quoter&quot,
  &quotett&quot,
  &quotrftt&quot
]
Output: &quotwertf&quot
Example 2:
Input:
[
  &quotz&quot,
  &quotx&quot
]
Output: &quotzx&quot
Example 3:
Input:
[
  &quotz&quot,
  &quotx&quot,
  &quotz&quot
] 
Output: &quot&quot 
Explanation: The order is invalid, so return &quot&quot.
Note:
	You may assume all letters are in lowercase.
	You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
	If the order is invalid, return an empty string.
	There may be multiple valid order of letters, return any one of them is fine.
## Solutions:
```python
class Solution :
public:
    string alienOrder(vector& words) :
        unordered_map> graph
        unordered_map inDegree
        for (int i = 0 i < words.size() ++i) :
            for (auto c: words[i]) :
                graph[c]
        for (int i = 0 i < words.size() - 1 ++i) :
            vector partialOrder = getPartialOrder(words[i], words[i+1])
            if (partialOrder.size() == 0)   continue
            graph[partialOrder[0]].push_back(partialOrder[1])
            ++inDegree[partialOrder[1]]
        string ret
        queue q
        for (auto& node : graph) :
            if (inDegree.count(node.first) == 0) : // it is wrong to iterate inDegree directly, becaues for those free chars, it is not in inDegree. 
                q.push(node.first)
        while (!q.empty()) :
            char c = q.front() q.pop()
            ret.push_back(c)
            for (auto& neighbor : graph[c]) :
                if(--inDegree[neighbor] == 0) :
                    q.push(neighbor)
        for (auto& node : inDegree) :
            if (node.second != 0)   return ""
        return ret
    vector getPartialOrder(string& smaller, string& larger) :
        for (int i = 0 i < min(smaller.length(), larger.length()) ++i) :
            if (smaller[i] != larger[i]) :
                return :smaller[i], larger[i]
        return : 
```
# 413. Arithmetic Slices
* *Difficulty: Medium*
* *Topics: Math, Dynamic Programming*
* *Similar Questions:*
  * [Arithmetic Slices II - Subsequence](arithmetic-slices-ii-subsequence.md)
## Problem:
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic. 1, 1, 2, 5, 7 
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 
A slice (P, Q) of array A is called arithmetic if the sequence:
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 
The function should return the number of arithmetic slices in the array A. 
Example:
A = [1, 2, 3, 4]
return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
## Solutions:
```python
class Solution :
public:
    int numberOfArithmeticSlices(vector& A) :
        int count = 0
        int right = 1
        for (int i = 0 i < (int) A.size() - 2 ++i) : // minus!
            if (i + 1 == right) :
                while (right + 1 < A.size() && A[right + 1] - A[right] == A[right] - A[right - 1]) ++right
            count += (right - i - 1)
            if (i + 1 == right) : // push right
                ++right
        return count
```
# 441. Arranging Coins
* *Difficulty: Easy*
* *Topics: Math, Binary Search*
* *Similar Questions:*
## Problem:
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.
Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.
Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
## Solutions:
```python
class Solution :
public:
    int arrangeCoins(int n) :
        long left = 0
        long right = INT_MAX / 4
        while (left < right) :
            long mid = right - (right - left) / 2
            if ( (mid + 1) * mid / 2 > n)  :
                right = mid - 1
             else :
                left = mid
        return left
```
# 561. Array Partition I
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
## Solutions:
```python
class Solution :
public:
    int arrayPairSum(vector& nums) :
        sort(nums.begin(), nums.end())
        int sum = 0
        for (int i = 0 i < nums.size() i = i + 2) :
            sum += nums[i]
        return sum
```
# 1117. As Far from Land as Possible
* *Difficulty: Medium*
* *Topics: Breadth-first Search, Graph*
* *Similar Questions:*
  * [Shortest Distance from All Buildings](shortest-distance-from-all-buildings.md)
## Problem:
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.
The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
If no land or water exists in the grid, return -1.
Example 1:
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
Note:
	1 &lt= grid.length == grid[0].length &lt= 100
	grid[i][j] is 0 or 1
## Solutions:
```python
class Solution :
public:
    int maxDistance(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        queue> q
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] == 1) :
                    q.push(:i, j)
        int distance = -1
        while (!q.empty()) :
            int size = q.size()
            for (int i = 0 i < size ++i) :
                auto coord = q.front() q.pop()
                for (int d = 0 d < 4 ++d) :
                    int row = coord.first + directions[d][0]
                    int col = coord.second + directions[d][1]
                    if (row >= 0 && row = 0 && col < n && grid[row][col] == 0) :
                        q.push(:row, col)
                        grid[row][col] = 1
            ++distance
        return distance <= 0 ? -1 : distance
private:
    int directions[4][2] = :
        :1, 0,
        :-1, 0,
        :0, 1,
        :0, -1
```
# 455. Assign Cookies
* *Difficulty: Easy*
* *Topics: Greedy*
* *Similar Questions:*
## Problem:
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.
Example 1:
Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:
Input: [1,2], [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
## Solutions:
```python
class Solution :
public:
    int findContentChildren(vector& g, vector& s) :
        sort(g.begin(), g.end())
        sort(s.begin(), s.end())
        int ret = 0
        int idx1 = 0
        int idx2 = 0
        while (idx1 < g.size() && idx2 < s.size()) :
            if (g[idx1] <= s[idx2]) :
                ++ret
                ++idx1
                ++idx2
             else :
                ++idx2
        return ret
```
# 735. Asteroid Collision
* *Difficulty: Medium*
* *Topics: Stack*
* *Similar Questions:*
  * [Can Place Flowers](can-place-flowers.md)
## Problem:
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).  Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions.  If two asteroids meet, the smaller one will explode.  If both are the same size, both will explode.  Two asteroids moving in the same direction will never meet.
Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:
The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
## Solutions:
```python
class Solution :
public:
    vector asteroidCollision(vector& asteroids) :
        vector stack
        vector ret
        for (auto asteroid : asteroids) :
            if (asteroid < 0) :
                while (!stack.empty() && stack.back() + asteroid < 0)   stack.pop_back()
                if (stack.empty()) :
                    ret.push_back(asteroid)
                 else if (stack.back() + asteroid == 0) :
                    stack.pop_back()
             else :
                stack.push_back(asteroid)
        ret.insert(ret.end(), stack.begin(), stack.end())
        return ret
```
# 110. Balanced Binary Tree
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md)
## Problem:
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.
Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isBalanced(TreeNode* root) :
        int height
        return isBalanced(root, height)
    bool isBalanced(TreeNode* root, int& height) :
        if (root == nullptr) :
            height = 0
            return true
        int leftHeight
        int rightHeight
        if (isBalanced(root->left, leftHeight) && isBalanced(root->right, rightHeight) && abs(leftHeight - rightHeight) <= 1) :
            height = 1 + max(leftHeight, rightHeight)
            return true
         else :
            return false
```
# 504. Base 7
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Given an integer, return its base 7 string representation.
Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note:
The input will be in range of [-1e7, 1e7].
## Solutions:
```python
class Solution :
public:
    string convertToBase7(int num) :
        if (num == 0)   return "0"
        int sign = 1
        if (num < 0) :
            sign = -1
            num = -num
        string ret
        while (num > 0) :
            ret.push_back('0' + num % 7)
            num /= 7
        if (sign == -1) :
            ret.push_back('-')
        reverse(ret.begin(), ret.end())
        return ret
```
# 227. Basic Calculator II
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
  * [Basic Calculator](basic-calculator.md)
  * [Expression Add Operators](expression-add-operators.md)
  * [Basic Calculator III](basic-calculator-iii.md)
## Problem:
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
Example 1:
Input: &quot3+2*2&quot
Output: 7
Example 2:
Input: &quot 3/2 &quot
Output: 1
Example 3:
Input: &quot 3+5 / 2 &quot
Output: 5
Note:
	You may assume that the given expression is always valid.
	Do not use the eval built-in library function.
## Solutions:
```python
class Solution :
public:
    int calculate(string s) :
        int sum = 0
        int val = 0
        char lastChar = '+'
        vector v
        for (int i = 0 i <= s.length() ++i) :
            if (i != s.length()) :
                if (s[i] == ' ') :
                    continue
                if (isdigit(s[i])) :
                    val = val * 10 + (s[i] - '0')
                    continue
            switch(lastChar) :
                case '+': 
                    v.push_back(val)
                    break
                case '-': 
                    v.push_back(-val)
                    break
                case '*': 
                    v.back() *= val
                    break
                case '/': 
                    v.back() /= val
                    break
            val = 0
            if (i != s.length()) :
                lastChar = s[i]
        for (auto val : v) :
            sum += val
        return sum
```
# 224. Basic Calculator
* *Difficulty: Hard*
* *Topics: Math, Stack*
* *Similar Questions:*
  * [Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation.md)
  * [Basic Calculator II](basic-calculator-ii.md)
  * [Different Ways to Add Parentheses](different-ways-to-add-parentheses.md)
  * [Expression Add Operators](expression-add-operators.md)
  * [Basic Calculator III](basic-calculator-iii.md)
## Problem:
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
Example 1:
Input: &quot1 + 1&quot
Output: 2
Example 2:
Input: &quot 2-1 + 2 &quot
Output: 3
Example 3:
Input: &quot(1+(4+5+2)-3)+(6+8)&quot
Output: 23
Note:
	You may assume that the given expression is always valid.
	Do not use the eval built-in library function.
## Solutions:
```python
class Solution :
public:
    int calculate(string s) :
        stack stk
        int sign = 1
        int val = 0
        stk.push(0)
        for (int i = 0 i < s.length() ++i) :
            switch(s[i]) :
                case '+': :
                    stk.top() = stk.top() + sign * val
                    sign = 1 // reset
                    val = 0
                    break
                case '-': :
                    stk.top() = stk.top() + sign * val
                    sign = -1 // reset
                    val = 0
                    break
                case ' ': :
                    break
                case '(': :
                    stk.push(sign)
                    sign = 1 // reset
                    val = 0
                    stk.push(0)
                    break
                case ')': :
                    stk.top() = stk.top() + sign * val
                    int expVal = stk.top()
                    stk.pop()
                    expVal = expVal * stk.top()
                    stk.pop()
                    stk.top() += expVal
                    val = 0 // reset
                    sign = 1
                    break
                default: :
                    val = val * 10 - '0' + s[i] 
                    break
        return stk.top() + val * sign // including all
```
# 419. Battleships in a Board
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
## Solutions:
```python
class Solution :
public:
    int countBattleships(vector>& board) :
        int count = 0
        int m = board.size()
        if (m == 0) return 0
        int n = board[0].size()
        if (n == 0) return 0
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (board[i][j] == 'X' && (j - 1 < 0 || board[i][j-1] != 'X') && ( i - 1 < 0 || board[i-1][j] != 'X'))  ++count
        return count
```
# 1132. Before and After Puzzle
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
## Problem:
Given a list of phrases, generate a list of Before and After puzzles.
A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.
Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.
Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.
You should return a list of distinct strings sorted lexicographically.
Example 1:
Input: phrases = [&quotwriting code&quot,&quotcode rocks&quot]
Output: [&quotwriting code rocks&quot]
Example 2:
Input: phrases = [&quotmission statement&quot,
                  &quota quick bite to eat&quot,
                  &quota chip off the old block&quot,
                  &quotchocolate bar&quot,
                  &quotmission impossible&quot,
                  &quota man on a mission&quot,
                  &quotblock party&quot,
                  &quoteat my words&quot,
                  &quotbar of soap&quot]
Output: [&quota chip off the old block party&quot,
         &quota man on a mission impossible&quot,
         &quota man on a mission statement&quot,
         &quota quick bite to eat my words&quot,
         &quotchocolate bar of soap&quot]
Example 3:
Input: phrases = [&quota&quot,&quotb&quot,&quota&quot]
Output: [&quota&quot]
Constraints:
	1 &lt= phrases.length &lt= 100
	1 &lt= phrases[i].length &lt= 100
## Solutions:
```python
class Solution :
public:
    vector beforeAndAfterPuzzles(vector& phrases) :
        unordered_map> firstWordToPhase
        for (int i = 0 i < phrases.size() ++i) :
            string firstWord = getFirstWord(phrases[i])
            firstWordToPhase[firstWord].push_back(i)
        set ret
        for (int i = 0 i < phrases.size() ++i) :
            int lastWordIndex = getLastWordIndex(phrases[i])
            string lastWord = phrases[i].substr(lastWordIndex)
            if (firstWordToPhase.count(lastWord) > 0) :
                string prefix = phrases[i].substr(0, lastWordIndex)
                for (auto& j : firstWordToPhase[lastWord]) :
                    if (j == i) continue
                    ret.insert(prefix + phrases[j])
        return :ret.begin(), ret.end()
private:
    string getFirstWord(const string& str) :
        int pos = 0
        while (pos < str.length() && str[pos] != ' ') :
            ++pos
        return str.substr(0, pos)
    int getLastWordIndex(const string& str) :
        int pos = str.length() - 1
        while (pos >= 0 && str[pos] != ' ') :
            --pos
        return pos + 1
```
# 296. Best Meeting Point
* *Difficulty: Hard*
* *Topics: Math, Sort*
* *Similar Questions:*
  * [Shortest Distance from All Buildings](shortest-distance-from-all-buildings.md)
  * [Minimum Moves to Equal Array Elements II](minimum-moves-to-equal-array-elements-ii.md)
## Problem:
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
Example:
Input: 
1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
Output: 6 
Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
## Solutions:
```python
class Solution :
public:
    int minTotalDistance(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        vector x, y
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] == 1) :
                    x.push_back(i)
                    y.push_back(j)
        sort(y.begin(), y.end()) // sorting!!!!!!!
        return minTotalDistanceAtOneDimension(x) + minTotalDistanceAtOneDimension(y)
private:
    int minTotalDistanceAtOneDimension(vector& points) : // it is median!!! not average!!!
        int distance = 0
        int i = 0
        int j = points.size() - 1
        while (i < j) :
            distance += points[j] - points[i]
            i++
            j--
        cout << distance << endl
        return distance
```
# 122. Best Time to Buy and Sell Stock II
* *Difficulty: Easy*
* *Topics: Array, Greedy*
* *Similar Questions:*
  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)
  * [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii.md)
  * [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv.md)
  * [Best Time to Buy and Sell Stock with Cooldown](best-time-to-buy-and-sell-stock-with-cooldown.md)
  * [Best Time to Buy and Sell Stock with Transaction Fee](best-time-to-buy-and-sell-stock-with-transaction-fee.md)
## Problem:
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
## Solutions:
```python
class Solution :
public:
    int maxProfit(vector& prices) :
        int profit = 0
        for (int i = 1 i < prices.size() ++i) :
            profit += max(0, prices[i] - prices[i-1]) 
        return profit
```
# 123. Best Time to Buy and Sell Stock III
* *Difficulty: Hard*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)
  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)
  * [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv.md)
  * [Maximum Sum of 3 Non-Overlapping Subarrays](maximum-sum-of-3-non-overlapping-subarrays.md)
## Problem:
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
## Solutions:
```python
class Solution :
public:
    int maxProfit(vector& prices) :
        int n = prices.size()
        if (n == 0) return 0
        vector forward(n, 0)
        vector backward(n, 0)
        int minVal = prices[0]
        for (int i = 1 i < n ++i) :
            forward[i] = max(forward[i - 1], prices[i] - minVal)
            minVal = min(minVal, prices[i])
        int maxVal = prices[n-1]
        for (int i = n - 2 i >= 0 --i) :
            backward[i] = max(backward[i + 1], maxVal - prices[i])
            maxVal = max(maxVal, prices[i])
        int ret = 0
        for (int i = 0 i < n ++i) :
            ret = max(ret, forward[i] + backward[i])
        return ret
```
# 188. Best Time to Buy and Sell Stock IV
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)
  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)
  * [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii.md)
## Problem:
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
## Solutions:
```python
class Solution :
public:
    int maxProfit(int k, vector& prices) :
        int n = prices.size()
        if (k == 0 || n == 0) return 0
        k = min(k, n/2)
        vector> hold (n , vector (2, 0))
        vector> empty(n , vector (2, 0))
        for (int i = 0 i < n ++i) :
            empty[i][0] = 0
        for (int j = 1 j <= k ++j) :
            hold[0][j%2] = -prices[0]
            empty[0][j%2] = 0
        for (int j = 1 j <= k ++j) :
            for (int i = 1 i < n ++i) :
                hold[i][j%2] = max(hold[i-1][j%2], empty[i-1][(j-1)%2] - prices[i])
                empty[i][j%2] = max(empty[i-1][j%2], hold[i-1][j%2] + prices[i])        
        return empty[n-1][k%2]
```
# 309. Best Time to Buy and Sell Stock with Cooldown
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)
  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)
## Problem:
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
	You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
	After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
## Solutions:
```python
class Solution :
public:
    int maxProfit(vector& prices) :
        int n = prices.size()
        if (n == 0) return 0
        vector sell(n, 0)
        vector hold(n, 0)
        for (int i = 0 i < n ++i) :
            hold[i] = max(i - 1 >= 0 ? hold[i-1] : INT_MIN, i - 2 >= 0 ? -prices[i] + sell[i-2] : -prices[i])
            sell[i] = (i - 1 >= 0 ? max(hold[i-1] + prices[i], sell[i-1]) : 0)
        return sell[n-1]
```
# 121. Best Time to Buy and Sell Stock
* *Difficulty: Easy*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
  * [Maximum Subarray](maximum-subarray.md)
  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)
  * [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii.md)
  * [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv.md)
  * [Best Time to Buy and Sell Stock with Cooldown](best-time-to-buy-and-sell-stock-with-cooldown.md)
## Problem:
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
## Solutions:
```python
class Solution :
public:
    int maxProfit(vector& prices) :
        int buy = INT_MAX
        int profit = 0
        for (auto price : prices) :
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
```
# 595. Big Countries
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
There is a table World
+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+
A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.
Write a SQL solution to output big countries&#39 name, population and area.
For example, according to the above table, we should output:
+--------------+-------------+--------------+
| name         | population  | area         |
+--------------+-------------+--------------+
| Afghanistan  | 25500100    | 652230       |
| Algeria      | 37100000    | 2381741      |
+--------------+-------------+--------------+
## Solutions:
```python
# Write your MySQL query statement below
SELECT name, population, area 
FROM World 
WHERE
area > 3000000 OR population > 25000000
```
# 173. Binary Search Tree Iterator
* *Difficulty: Medium*
* *Topics: Stack, Tree, Design*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
  * [Flatten 2D Vector](flatten-2d-vector.md)
  * [Zigzag Iterator](zigzag-iterator.md)
  * [Peeking Iterator](peeking-iterator.md)
  * [Inorder Successor in BST](inorder-successor-in-bst.md)
## Problem:
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
Example:
BSTIterator iterator = new BSTIterator(root)
iterator.next()    // return 3
iterator.next()    // return 7
iterator.hasNext() // return true
iterator.next()    // return 9
iterator.hasNext() // return true
iterator.next()    // return 15
iterator.hasNext() // return true
iterator.next()    // return 20
iterator.hasNext() // return false
Note:
	next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
	You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class BSTIterator :
public:
    BSTIterator(TreeNode* root) :
        while (root) :
            stk.push(root)
            root = root->left
    /** @return the next smallest number */
    int next() :
        TreeNode* node = stk.top() stk.pop()
        int ret = node->val
        node = node->right
        while (node) :
            stk.push(node)
            node = node->left
        return ret
    /** @return whether we have a next smallest number */
    bool hasNext() :
        return !stk.empty()
private:
    stack stk
/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root)
 * int param_1 = obj->next()
 * bool param_2 = obj->hasNext()
 */
```
# 94. Binary Tree Inorder Traversal
* *Difficulty: Medium*
* *Topics: Hash Table, Stack, Tree*
* *Similar Questions:*
  * [Validate Binary Search Tree](validate-binary-search-tree.md)
  * [Binary Tree Preorder Traversal](binary-tree-preorder-traversal.md)
  * [Binary Tree Postorder Traversal](binary-tree-postorder-traversal.md)
  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)
  * [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst.md)
  * [Closest Binary Search Tree Value II](closest-binary-search-tree-value-ii.md)
  * [Inorder Successor in BST](inorder-successor-in-bst.md)
  * [Convert Binary Search Tree to Sorted Doubly Linked List](convert-binary-search-tree-to-sorted-doubly-linked-list.md)
  * [Minimum Distance Between BST Nodes](minimum-distance-between-bst-nodes.md)
## Problem:
Given a binary tree, return the inorder traversal of its nodes&#39 values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector inorderTraversal(TreeNode* root) :
        vector ret
        TreeNode* cur = root
        while (cur) :
            TreeNode* pre = cur->left
            if (pre == nullptr) :
                ret.push_back(cur->val) // visit
                cur = cur->right
                continue
            while (pre->right != nullptr && pre->right != cur) :
                pre = pre->right
            if (pre->right == nullptr) :
                pre->right = cur
                cur = cur->left
             else :
                pre->right = nullptr
                ret.push_back(cur->val) // visit
                cur = cur->right
        return ret
```
# 107. Binary Tree Level Order Traversal II
* *Difficulty: Easy*
* *Topics: Tree, Breadth-first Search*
* *Similar Questions:*
  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)
  * [Average of Levels in Binary Tree](average-of-levels-in-binary-tree.md)
## Problem:
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector> levelOrderBottom(TreeNode* root) :
        vector> ret
        queue q
        if (root != NULL)   q.push(root)
        while (!q.empty()) :
            int size = q.size()
            vector level
            for (int i = 0 i < size ++i) :
                TreeNode* node = q.front() q.pop()
                level.push_back(node->val)
                if (node->left) q.push(node->left)
                if (node->right) q.push(node->right)
            ret.push_back(level)
        reverse(ret.begin(), ret.end())
        return ret
```
# 102. Binary Tree Level Order Traversal
* *Difficulty: Medium*
* *Topics: Tree, Breadth-first Search*
* *Similar Questions:*
  * [Binary Tree Zigzag Level Order Traversal](binary-tree-zigzag-level-order-traversal.md)
  * [Binary Tree Level Order Traversal II](binary-tree-level-order-traversal-ii.md)
  * [Minimum Depth of Binary Tree](minimum-depth-of-binary-tree.md)
  * [Binary Tree Vertical Order Traversal](binary-tree-vertical-order-traversal.md)
  * [Average of Levels in Binary Tree](average-of-levels-in-binary-tree.md)
  * [N-ary Tree Level Order Traversal](n-ary-tree-level-order-traversal.md)
  * [Cousins in Binary Tree](cousins-in-binary-tree.md)
## Problem:
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector> levelOrder(TreeNode* root) :
        vector> ret
        if (root == NULL)   return ret
        queue q
        q.push(root)
        while (!q.empty()) :
            int count = 0
            vector level
            for (int i = q.size() - 1 i >= 0 --i) :  // starting from 0 is wrong because q.size() keeps on changing. 
                auto node = q.front() q.pop()
                level.push_back(node->val)
                if (node->left) :
                    q.push(node->left)
                if (node->right) :
                    q.push(node->right)
            ret.push_back(level)
        return ret
```
# 298. Binary Tree Longest Consecutive Sequence
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Longest Consecutive Sequence](longest-consecutive-sequence.md)
  * [Binary Tree Longest Consecutive Sequence II](binary-tree-longest-consecutive-sequence-ii.md)
## Problem:
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
Example 1:
Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:
Input:
   2
    \
     3
    / 
   2    
  / 
 1
Output: 2 
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int longestConsecutive(TreeNode* root) :
        if (root == nullptr)    return 0
        int consecutiveLen = 1
        return helper(root, consecutiveLen)
private:
    int helper(TreeNode* root, int& consecutiveLen) :
        int ret = 0
        if (root->left) :
            int leftConsecutive = 1
            ret = max(ret, helper(root->left, leftConsecutive))
            if (root->val + 1 == root->left->val) :
                consecutiveLen = max(consecutiveLen, 1 + leftConsecutive)
        if (root->right) :
            int rightConsecutive = 1
            ret = max(ret, helper(root->right, rightConsecutive))
            if (root->val + 1 == root->right->val) :
                consecutiveLen = max(consecutiveLen, 1 + rightConsecutive)
        ret = max(ret, consecutiveLen)
        return ret
```
# 124. Binary Tree Maximum Path Sum
* *Difficulty: Hard*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Path Sum](path-sum.md)
  * [Sum Root to Leaf Numbers](sum-root-to-leaf-numbers.md)
  * [Path Sum IV](path-sum-iv.md)
  * [Longest Univalue Path](longest-univalue-path.md)
## Problem:
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6
Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int maxPathSum(TreeNode* root) :
        int maxPathToRoot
        return helper(root, maxPathToRoot)
    int helper(TreeNode* root, int& maxPathToRoot) :
        if (root == nullptr) :
            maxPathToRoot = 0
            return 0
        int ret = INT_MIN
        int leftMaxPathToRoot = 0
        int rightMaxPathToRoot = 0
        if (root->left) :
            ret = max(ret, helper(root->left, leftMaxPathToRoot))
        if (root->right) :
            ret = max(ret, helper(root->right, rightMaxPathToRoot))
        maxPathToRoot = root->val + max(0, max(leftMaxPathToRoot, rightMaxPathToRoot))
        return max(ret, root->val + max(0, leftMaxPathToRoot) + max(0, rightMaxPathToRoot))
```
# 257. Binary Tree Paths
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Path Sum II](path-sum-ii.md)
  * [Smallest String Starting From Leaf](smallest-string-starting-from-leaf.md)
## Problem:
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
Example:
Input:
   1
 /   \
2     3
 \
  5
Output: [&quot1-&gt2-&gt5&quot, &quot1-&gt3&quot]
Explanation: All root-to-leaf paths are: 1-&gt2-&gt5, 1-&gt3
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector binaryTreePaths(TreeNode* root) :
        if (root == NULL)   return :
        vector> ret
        vector path
        helper(root, path, ret)
        vector strRet
        for (auto& intPath : ret) :
            strRet.push_back(join(intPath))
        return strRet
    void helper(TreeNode* root, vector& path, vector>& ret) :
        path.push_back(root->val)
        if (root->left == NULL && root->right == NULL) :
            ret.push_back(path)
            path.pop_back()
            return
        if (root->left) helper(root->left, path, ret)
        if (root->right) helper(root->right, path, ret)
        path.pop_back()
    string join(vector& nums) :
        stringstream ss
        for (int i = 0 i < nums.size() ++i) :
            if (i != 0) :
                ss "
            ss << nums[i]
        return ss.str()
```
# 145. Binary Tree Postorder Traversal
* *Difficulty: Hard*
* *Topics: Stack, Tree*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
  * [N-ary Tree Postorder Traversal](n-ary-tree-postorder-traversal.md)
## Problem:
Given a binary tree, return the postorder traversal of its nodes&#39 values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* reverse(TreeNode* head) :
        TreeNode* dummy = new TreeNode(0)
        TreeNode* next
        while (head) :
            next = head->right
            head->right = dummy->right
            dummy->right = head
            head = next
        return dummy->right
    void visit(TreeNode* from, TreeNode* to, vector& ret) :
        TreeNode* newHead = reverse(from)
        TreeNode* cur = newHead
        while (cur != nullptr) :
            ret.push_back(cur->val)
            cur = cur->right
        reverse(newHead)
    vector postorderTraversal(TreeNode* root) :
        vector ret
        TreeNode* dummy = new TreeNode(0)
        dummy->left = root
        TreeNode* cur = dummy
        while (cur) :
            if (cur->left == nullptr) :
                cur = cur->right
             else :
                TreeNode* pre = cur->left
                while (pre->right != nullptr && pre->right != cur) :
                    pre = pre->right
                if (pre->right == nullptr) :
                    pre->right = cur
                    cur = cur->left
                 else :
                    pre->right = nullptr
                    visit(cur->left, pre, ret)
                    cur = cur->right
        return ret
```
# 144. Binary Tree Preorder Traversal
* *Difficulty: Medium*
* *Topics: Stack, Tree*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
  * [Verify Preorder Sequence in Binary Search Tree](verify-preorder-sequence-in-binary-search-tree.md)
  * [N-ary Tree Preorder Traversal](n-ary-tree-preorder-traversal.md)
## Problem:
Given a binary tree, return the preorder traversal of its nodes&#39 values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector preorderTraversal(TreeNode* root) :
        vector ret
        TreeNode* cur = root
        while (cur) :
            TreeNode* pre = cur->left
            if (pre == nullptr) :
                ret.push_back(cur->val) // visit
                cur = cur->right
                continue
            while (pre->right != nullptr && pre->right != cur) :
                pre = pre->right
            if (pre->right == nullptr) :
                pre->right = cur
                ret.push_back(cur->val) // visit
                cur = cur->left
             else :
                pre->right = nullptr
                cur = cur->right
        return ret
```
# 199. Binary Tree Right Side View
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search, Breadth-first Search*
* *Similar Questions:*
  * [Populating Next Right Pointers in Each Node](populating-next-right-pointers-in-each-node.md)
  * [Boundary of Binary Tree](boundary-of-binary-tree.md)
## Problem:
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            &lt---
 /   \
2     3         &lt---
 \     \
  5     4       &lt---
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector rightSideView(TreeNode* root) :
        vector ret
        helper(root, 0, ret)
        return ret
    void helper(TreeNode* root, int level, vector& ret) :
        if (root == nullptr)    return
        if (ret.size() == level)    ret.push_back(root->val)
        helper(root->right, level + 1, ret)
        helper(root->left, level + 1, ret)
```
# 563. Binary Tree Tilt
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Given a binary tree, return the tilt of the whole tree.
The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
The tilt of the whole tree is defined as the sum of all nodes' tilt.
Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:
The sum of node values in any subtree won't exceed the range of 32-bit integer. 
All the tilt values won't exceed the range of 32-bit integer.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int findTilt(TreeNode* root) :
        int tilt = 0
        helper(root, tilt)
        return tilt
private:
    int helper(TreeNode* root, int& tilt) :
        if (root == nullptr) :
            return 0
        int left = helper(root->left, tilt)
        int right = helper(root->right, tilt)
        tilt += abs(left - right)
        return root->val + left + right
```
# 156. Binary Tree Upside Down
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Reverse Linked List](reverse-linked-list.md)
## Problem:
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
Example:
Input: [1,2,3,4,5]
    1
   / \
  2   3
 / \
4   5
Output: return the root of the binary tree [4,5,2,#,#,3,1]
   4
  / \
 5   2
    / \
   3   1  
Clarification:
Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.
The serialization of a binary tree follows a level order traversal, where &#39#&#39 signifies a path terminator where no node exists below.
Here&#39s an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* upsideDownBinaryTree(TreeNode* root) :
        if (root == nullptr)    return nullptr
        if (root->left == nullptr && root->right == nullptr)    return root
        TreeNode* leftNode = root->left
        TreeNode* rightNode = root->right
        TreeNode* leftSubUpsideDown = upsideDownBinaryTree(leftNode)
        TreeNode* rightSubUpsideDown = upsideDownBinaryTree(rightNode)
        leftNode->left = rightSubUpsideDown
        leftNode->right = root
        root->left = nullptr // set nullptr
        root->right = nullptr // set nullptr
        return leftSubUpsideDown
```
# 314. Binary Tree Vertical Order Traversal
* *Difficulty: Medium*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)
## Problem:
Given a binary tree, return the vertical order traversal of its nodes&#39 values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
Examples 1:
Input: [3,9,20,null,null,15,7]
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 
Output:
[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:
Input: [3,9,8,4,0,1,7]
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 
Output:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0&#39s right child is 2 and 1&#39s left child is 5)
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
Output:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector> verticalOrder(TreeNode* root) :
        queue> q
        map> verticals
        q.push(:root,0)
        while(!q.empty()) :
            auto node = q.front() q.pop()
            if (node.first == nullptr) continue
            verticals[node.second].push_back(node.first->val)
            q.push(:node.first->left, node.second - 1)
            q.push(:node.first->right, node.second + 1)
        vector> ret
        for (auto it = verticals.begin() it != verticals.end() ++it) :
            ret.push_back(it->second)
        return ret
```
# 103. Binary Tree Zigzag Level Order Traversal
* *Difficulty: Medium*
* *Topics: Stack, Tree, Breadth-first Search*
* *Similar Questions:*
  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)
## Problem:
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector> zigzagLevelOrder(TreeNode* root) :
        vector> ret
        if (root == NULL)   return ret
        bool forward = true
        queue q
        q.push(root)
        while (!q.empty()) :
            int n = q.size()
            vector level(n)
            for (int i = 0 i < n ++i) :
                TreeNode* node = q.front() q.pop()
                if (node->left) q.push(node->left)
                if (node->right) q.push(node->right)
                if (forward) :
                    level[i] = node->val
                 else :
                    level[n - 1 - i] = node->val
            ret.push_back(level)
            forward = !forward
        return ret
```
# 843. Binary Trees With Factors
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
Given an array of unique integers, each integer is strictly greater than 1.
We make a binary tree using these integers and each number may be used for any number of times.
Each non-leaf node&#39s value should be equal to the product of the values of it&#39s children.
How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.
Example 1:
Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:
Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
Note:
	1 &lt= A.length &lt= 1000.
	2 &lt= A[i] &lt= 10 ^ 9.
## Solutions:
```python
class Solution :
public:
    int numFactoredBinaryTrees(vector& A) :
        sort(A.begin(), A.end())
        map dp
        long ret = 0
        for (int i = 0 i < A.size() ++i) :
            dp[A[i]] = 1
            for (auto it = dp.begin() it != dp.end() ++it) :
                if (A[i] % it->first == 0 && dp.count(A[i]/it->first)) :
                    dp[A[i]] = (dp[A[i]] + it->second * dp[A[i]/it->first]) % MOD
            ret = (ret + dp[A[i]]) % MOD
        return ret
private:
    int MOD = 1e9 + 7
```
# 401. Binary Watch
* *Difficulty: Easy*
* *Topics: Backtracking, Bit Manipulation*
* *Similar Questions:*
  * [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number.md)
  * [Number of 1 Bits](number-of-1-bits.md)
## Problem:
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
Example:
Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
## Solutions:
```python
class Solution :
public:
    vector readBinaryWatch(int num) :
        vector ret
        for (int i = 0 i <= num ++i) :
            auto miniteRet = minite(i)
            auto secondRet = second(num - i)
            for (int j = 0  j < miniteRet.size() ++j) :
                for (int k = 0 k < secondRet.size() ++k) :
                    ret.push_back(miniteRet[j] + ":" + secondRet[k])
        return ret
private:
    vector minite(int num) :
        vector ret
        for (int i = 0 i < 12 ++i) :
            if (countBit(i) == num) :
                ret.push_back(to_string(i))
        return ret
    vector second(int num) :
        vector ret
        for (int i = 0 i < 60 ++i)  :
            if (countBit(i) == num) :
                if (i < 10) : 
                    ret.push_back("0" + string(1, '0' + i))
                 else :
                    ret.push_back(to_string(i))
        return ret
    int countBit(int num) :
        int ret = 0
        while (num > 0) :
            ++ret
            num = num & (num - 1)
        return ret
```
#### More concise solution
From [Huahua](https://zxi.mytechroad.com/blog/bit/leetcode-401-binary-watch/)
```python
// Author: Huahua
// Running time: 2 ms (beats 100%)
class Solution :
public:
  vector readBinaryWatch(int num) :
    vector ans
    for (int i = 0 i <= num ++i)
      for (int h : nums(i, 12))
        for (int m : nums(num - i, 60))
          ans.push_back(to_string(h) + (m < 10 ? ":0" : ":") + to_string(m))
    return ans
private:
  // Return numbers in [0,r) that has b 1s in their binary format.
  vector nums(int b, int r) :    
    vector ans
    for (int n = 0 n < r ++n)
      if (__builtin_popcount(n) == b) ans.push_back(n)
    return ans
```
# 201. Bitwise AND of Numbers Range
* *Difficulty: Medium*
* *Topics: Bit Manipulation*
* *Similar Questions:*
## Problem:
Given a range [m, n] where 0 &lt= m &lt= n &lt= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
Example 1:
Input: [5,7]
Output: 4
Example 2:
Input: [0,1]
Output: 0
## Solutions:
```python
class Solution :
public:
    int rangeBitwiseAnd(int m, int n) :
        int ret = 0
        stack mBitValues
        stack nBitValues
        while (m > 0) :
            mBitValues.push(m&(-m))
            m -= m&(-m)
        while (n > 0) :
            nBitValues.push(n&(-n))
            n -= n&(-n)
        while (!mBitValues.empty() && !nBitValues.empty() && mBitValues.top() == nBitValues.top()) :
            ret += nBitValues.top()
            mBitValues.pop()
            nBitValues.pop()
        return ret
```
# 361. Bomb Enemy
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a 2D grid, each cell is either a wall &#39W&#39, an enemy &#39E&#39 or empty &#390&#39 (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.
Example:
Input: [[&quot0&quot,&quotE&quot,&quot0&quot,&quot0&quot],[&quotE&quot,&quot0&quot,&quotW&quot,&quotE&quot],[&quot0&quot,&quotE&quot,&quot0&quot,&quot0&quot]]
Output: 3 
Explanation: For the given grid,
0 E 0 0 
E 0 W E 
0 E 0 0
Placing a bomb at (1,1) kills 3 enemies.
## Solutions:
```python
class Solution :
public:
    int maxKilledEnemies(vector>& grid) :
        if (grid.empty() || grid[0].empty()) return 0
        int m = grid.size(), n = grid[0].size(), res = 0
        vector> v1(m, vector(n, 0)), v2 = v1, v3 = v1, v4 = v1
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                int t = (j == 0 || grid[i][j] == 'W') ? 0 : v1[i][j - 1]
                v1[i][j] = grid[i][j] == 'E' ? t + 1 : t
            for (int j = n - 1 j >= 0 --j) :
                int t = (j == n - 1 || grid[i][j] == 'W') ? 0 : v2[i][j + 1]
                v2[i][j] = grid[i][j] == 'E' ? t + 1 : t
        for (int j = 0 j < n ++j) :
            for (int i = 0 i < m ++i) :
                int t = (i == 0 || grid[i][j] == 'W') ? 0 : v3[i - 1][j]
                v3[i][j] = grid[i][j] == 'E' ? t + 1 : t
            for (int i = m - 1 i >= 0 --i) :
                int t = (i == m - 1 || grid[i][j] == 'W') ? 0 : v4[i + 1][j]
                v4[i][j] = grid[i][j] == 'E' ? t + 1 : t
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] == '0') :
                    res = max(res, v1[i][j] + v2[i][j] + v3[i][j] + v4[i][j])
        return res
```
# 1076. Brace Expansion
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [Decode String](decode-string.md)
  * [Letter Case Permutation](letter-case-permutation.md)
  * [Brace Expansion II](brace-expansion-ii.md)
## Problem:
A string S represents a list of words.
Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, &quot:a,b,c&quot represents options [&quota&quot, &quotb&quot, &quotc&quot].
For example, &quot:a,b,cd:e,f&quot represents the list [&quotade&quot, &quotadf&quot, &quotbde&quot, &quotbdf&quot, &quotcde&quot, &quotcdf&quot].
Return all words that can be formed in this manner, in lexicographical order.
Example 1:
Input: &quot:a,bc:d,ef&quot
Output: [&quotacdf&quot,&quotacef&quot,&quotbcdf&quot,&quotbcef&quot]
Example 2:
Input: &quotabcd&quot
Output: [&quotabcd&quot]
Note:
	1 &lt= S.length &lt= 50
	There are no nested curly brackets.
	All characters inside a pair of consecutive opening and ending curly brackets are different.
## Solutions:
```python
class Solution :
public:
    vector expand(string S) :
        set ret
        string path
        helper(S, 0, path, ret)
        return :ret.begin(), ret.end()
private:
    void helper(const string& S, int pos, string& path, set& ret) :
        if (pos == S.length()) :
            ret.insert(path)
            return
        string origin = path
        while (pos < S.length() && S[pos] != ':') :
            path.push_back(S[pos++])
        if (S[pos] == ':') :
            ++pos 
            vector letters
            while (S[pos] != '') :
                if (S[pos] == ',') :
                    ++pos
                 else :
                    letters.push_back(S[pos++])
            for (char& c : letters) :
                path.push_back(c)
                helper(S, pos + 1, path, ret)
                path.pop_back()
            path = origin
            return
        ret.insert(path)
        path = origin
        return
```
# 1033. Broken Calculator
* *Difficulty: Medium*
* *Topics: Math, Greedy*
* *Similar Questions:*
  * [2 Keys Keyboard](2-keys-keyboard.md)
## Problem:
On a broken calculator that has a number showing on its display, we can perform two operations:
	Double: Multiply the number on the display by 2, or
	Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.
Return the minimum number of operations needed to display the number Y.
Example 1:
Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation :2 -&gt 4 -&gt 3.
Example 2:
Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double :5 -&gt 4 -&gt 8.
Example 3:
Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double :3 -&gt 6 -&gt 5 -&gt 10.
Example 4:
Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.
Note:
	1 &lt= X &lt= 10^9
	1 &lt= Y &lt= 10^9
## Solutions:
```python
class Solution :
public:
    int brokenCalc(int X, int Y) :
        int ret = 0
        while (Y > X) :
            if (Y % 2 == 0) :
                Y /= 2
                ++ret
             else :
                ++Y
                Y /= 2
                ret += 2
        ret += (X - Y)
        return ret
```
# 319. Bulb Switcher
* *Difficulty: Medium*
* *Topics: Math, Brainteaser*
* *Similar Questions:*
  * [Bulb Switcher II](bulb-switcher-ii.md)
  * [Minimum Number of K Consecutive Bit Flips](minimum-number-of-k-consecutive-bit-flips.md)
## Problem:
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it&#39s off or turning off if it&#39s on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.
Example:
Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 
So you should return 1, because there is only one bulb is on.
## Solutions:
```python
class Solution :
public:
    int bulbSwitch(int n) :
        return sqrt(n)
```
# 299. Bulls and Cows
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called &quotbulls&quot) and how many digits match the secret number but locate in the wrong position (called &quotcows&quot). Your friend will use successive guesses and hints to eventually derive the secret number.
Write a function to return a hint according to the secret number and friend&#39s guess, use A to indicate the bulls and B to indicate the cows. 
Please note that both secret number and friend&#39s guess may contain duplicate digits.
Example 1:
Input: secret = &quot1807&quot, guess = &quot7810&quot
Output: &quot1A3B&quot
Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:
Input: secret = &quot1123&quot, guess = &quot0111&quot
Output: &quot1A1B&quot
Explanation: The 1st 1 in friend&#39s guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend&#39s guess only contain digits, and their lengths are always equal.
## Solutions:
```python
class Solution :
public:
    string getHint(string secret, string guess) :
        int m[256] = :0, bulls = 0, cows = 0
        for (int i = 0 i < secret.size() ++i) :
            if (secret[i] == guess[i]) ++bulls
            else ++m[secret[i]]
        for (int i = 0 i < secret.size() ++i) :
            if (secret[i] != guess[i] && m[guess[i]]) :
                ++cows
                --m[guess[i]]
        return to_string(bulls) + "A" + to_string(cows) + "B"
```
# 312. Burst Balloons
* *Difficulty: Hard*
* *Topics: Divide and Conquer, Dynamic Programming*
* *Similar Questions:*
  * [Minimum Cost to Merge Stones](minimum-cost-to-merge-stones.md)
## Problem:
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
Find the maximum coins you can collect by bursting the balloons wisely.
Note:
	You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
	0 &le n &le 500, 0 &le nums[i] &le 100
Example:
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --&gt [3,5,8] --&gt   [3,8]   --&gt  [8]  --&gt []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
## Solutions:
```python
class Solution :
public:
    int maxCoins(vector& nums) :
        int n = nums.size()
        if (n == 0) return 0
        if (n == 1) return nums[0]
        vector> dp(n, vector(n, 0))
        for (int i = 1 i < n - 1 ++i) :
            dp[i][i] = nums[i] * nums[i-1] * nums[i+1]
        dp[0][0] = nums[0] * nums[1]
        dp[n-1][n-1] = nums[n-2] * nums[n-1]
        for (int l = 2 l <= n ++l) :
            for (int i = 0 i < n ++i) :
                 if (i + l - 1 >= n) break
                for (int mid = i mid <= i + l - 1 ++mid) :
                    dp[i][i + l - 1] = max(dp[i][i + l - 1], nums[mid] * (i - 1 >= 0 ? nums[i-1] : 1) * (i + l < n ? nums[i + l] : 1) 
                                           + (mid - 1 >= i ? dp[i][mid - 1] : 0) + (mid + 1 <= i + l - 1 ? dp[mid + 1][i + l - 1] : 0))
        return dp[0][n-1]
```
# 833. Bus Routes
* *Difficulty: Hard*
* *Topics: Breadth-first Search*
* *Similar Questions:*
## Problem:
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1-&gt5-&gt7-&gt1-&gt5-&gt7-&gt1-&gt... forever.
We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.
Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note: 
	1 &lt= routes.length &lt= 500.
	1 &lt= routes[i].length &lt= 500.
	0 &lt= routes[i][j] &lt 10 ^ 6.
## Solutions:
```python
class Solution :
public:
    int numBusesToDestination(vector>& routes, int S, int T) :
        if (S == T) return 0
        map> stopToRoutes
        for (int i = 0 i < routes.size() ++i) :
            for (int j = 0 j < routes[i].size() ++j) :
                stopToRoutes[routes[i][j]].push_back(i)
        unordered_set visitedStops
        unordered_set visitedRoutes
        queue q
        q.push(S)
        int ret = 0
        while (!q.empty()) :
            int size = q.size()
            for (int i = 0 i < size ++i) :
                int stop = q.front() q.pop()
                if (stop == T)  return ret
                for (auto& route : stopToRoutes[stop]) :
                    if (visitedRoutes.count(route)) continue
                    visitedRoutes.insert(route)
                    for (auto& neighbor : routes[route]) :
                        if (visitedStops.count(neighbor))   continue
                        visitedStops.insert(neighbor)
                        q.push(neighbor)
            ++ret
        return -1
```
# 464. Can I Win
* *Difficulty: Medium*
* *Topics: Dynamic Programming, Minimax*
* *Similar Questions:*
  * [Flip Game II](flip-game-ii.md)
  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)
  * [Predict the Winner](predict-the-winner.md)
## Problem:
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins. 
What if we change the game so that players cannot re-use integers? 
For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally. 
You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
Example
Input:
maxChoosableInteger = 10
desiredTotal = 11
Output:
false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
## Solutions:
```python
class Solution :
public:
    bool canIWin(int maxChoosableInteger, int desireTotal) :
        int pool = 0
        for (int i = 1 i <= maxChoosableInteger ++i) :
            pool = pool | (1 << i)
        if ((maxChoosableInteger + 1) * maxChoosableInteger / 2 < desireTotal)  return false
        map, bool> cache
        return helper(pool, desireTotal, maxChoosableInteger, cache)
private:
    bool helper(int pool, int desireTotal, int maxChoosableInteger, map, bool>& cache) :
        if (cache.count(:pool, desireTotal) > 0)   return cache[:pool, desireTotal]
        bool ret = false
        for (int i = 1 i <= maxChoosableInteger ++i) :
            if ((pool >> i) & (0x1)) :
                int newPool = pool & (~(1 << i))
                if (desireTotal - i <= 0) :
                    ret = true
                    break
                bool enemy = helper(newPool, desireTotal - i, maxChoosableInteger, cache)
                if (!enemy) :
                    ret = true
                    break
        cache[:pool, desireTotal] = ret
        return ret
```
# 605. Can Place Flowers
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Teemo Attacking](teemo-attacking.md)
  * [Asteroid Collision](asteroid-collision.md)
## Problem:
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
## Solutions:
```python
class Solution :
public:
    bool canPlaceFlowers(vector& flowerbed, int n) :
        int count = 0
        for (int i = 0 i < flowerbed.size()) :
            if ((i - 1 >= 0 ? flowerbed[i-1] == 0 : true) && (flowerbed[i] == 0) && (i+1 < flowerbed.size() ? flowerbed[i+1] == 0 : true)) :
                if (++count == n)   return true
                ++i
            ++i
        return count >= n
```
# 135. Candy
* *Difficulty: Hard*
* *Topics: Greedy*
* *Similar Questions:*
## Problem:
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
	Each child must have at least one candy.
	Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
Example 1:
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
## Solutions:
```python
class Solution :
public:
    int candy(vector& ratings) : // pay attention to the condition that two adjecent ratings are equal
        int n = ratings.size()
        vector candyCount (n, 0)
        vector> ratingWithIndex
        for (int i = 0 i < n ++i) :
            ratingWithIndex.push_back(:ratings[i], i)
        sort(ratingWithIndex.begin(), ratingWithIndex.end())
        int sum = 0
        for (int i = 0 i < n ++i) :
            int index = ratingWithIndex[i].second
            candyCount[index] = 1
            if (index - 1 >= 0 && ratings[index] > ratings[index - 1]) :
                candyCount[index] = max(candyCount[index], candyCount[index - 1] + 1)
            if (index + 1  ratings[index + 1]) :
                candyCount[index] = max(candyCount[index], candyCount[index + 1] + 1)
            sum += candyCount[index]
        return sum
```
# 1056. Capacity To Ship Packages Within D Days
* *Difficulty: Medium*
* *Topics: Array, Binary Search*
* *Similar Questions:*
## Problem:
A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
Example 2:
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
Note:
	1 &lt= D &lt= weights.length &lt= 50000
	1 &lt= weights[i] &lt= 500
## Solutions:
```python
class Solution :
public:
    int shipWithinDays(vector& weights, int D) :
        if (weights.size() == 0)    return 0
        int maxWeight = 0
        int totalWeight = 0
        for (int i = 0 i < weights.size() ++i) :
            maxWeight = max(maxWeight, weights[i])
            totalWeight += weights[i]
        int left = maxWeight
        int right = totalWeight
        while (left < right) :
            int mid = left + (right - left) / 2
            if (minShipDay(weights, mid) <= D) :
                right = mid
             else :
                left = mid + 1
        return left
private:
    int minShipDay(vector& weights, int capacity) :
        int day = 1
        int remaining = capacity
        for (int i = 0 i < weights.size() ++i) :
            int weight = weights[i]
            if (remaining - weight < 0) :
                ++day
                remaining = capacity
            remaining -= weight
        return day
```
# 883. Car Fleet
* *Difficulty: Medium*
* *Topics: Sort*
* *Similar Questions:*
## Problem:
N cars are going to the same destination along a one lane road.  The destination is target miles away.
Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.
A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.
The distance between these two cars is ignored - they are assumed to have the same position.
A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
How many car fleets will arrive at the destination?
Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn&#39t catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Note:
	0 &lt= N &lt= 10 ^ 4
	0 &lt target &lt= 10 ^ 6
	0 &lt speed[i] &lt= 10 ^ 6
	0 &lt= position[i] &lt target
	All initial positions are different.
## Solutions:
```python
class Solution :
public:
    int carFleet(int target, vector& position, vector& speed) :
        vector> cars
        for (int i = 0 i < position.size() ++i) :
            cars.push_back(:position[i], speed[i])
        sort(cars.begin(), cars.end())
        stack stk
        for (int i = 0 i < cars.size() ++i) :
            double duration = (target - cars[i].first) / (double) cars[i].second
            while(!stk.empty() && stk.top() <= duration) :
                stk.pop()
            stk.push(duration)
        return stk.size()
```
# 828. Chalkboard XOR Game
* *Difficulty: Hard*
* *Topics: Math*
* *Similar Questions:*
## Problem:
We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we&#39ll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)
Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.
Return True if and only if Alice wins the game, assuming both players play optimally.
Example:
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
Notes: 
	1 &lt= N &lt= 1000. 
	0 &lt= nums[i] &lt= 2^16.
## Solutions:
```python
class Solution :
public:
    bool xorGame(vector& nums) :
        int sum = 0
        for (auto& val : nums) :
            sum ^= val
        return sum == 0 || nums.size() % 2 == 0
```
# 998. Check Completeness of a Binary Tree
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Given a binary tree, determine if it is a complete binary tree.
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values :1 and :2, 3), and all nodes in the last level (:4, 5, 6) are as far left as possible.
Example 2:
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn&#39t as far left as possible.
Note:
	The tree will have between 1 and 100 nodes.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isCompleteTree(TreeNode* root) :
        if (root == nullptr)    return true
        queue q
        q.push(root)
        int level = 0
        bool lastLevel = false
        while (!q.empty()) :
            int n = q.size()
            if ((1 << level) != n) :
                lastLevel = true
            for (int i = 0 i < n ++i) :
                TreeNode* node = q.front() q.pop()
                if (!node->left && node->right) return false
                if (node->left) :
                    if (lastLevel)  return false
                    q.push(node->left)
                 else :
                    lastLevel = true
                if (node->right) :
                    if (lastLevel)  return false
                    q.push(node->right)
                 else :
                    lastLevel = true
            ++level
        return true
```
# 1102. Check If a Number Is Majority Element in a Sorted Array
* *Difficulty: Easy*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [Majority Element](majority-element.md)
  * [Majority Element II](majority-element-ii.md)
## Problem:
Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.
A majority element is an element that appears more than N/2 times in an array of length N.
Example 1:
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: 
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 &gt 9/2 is true.
Example 2:
Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: 
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 &gt 4/2 is false.
Note:
	1 &lt= nums.length &lt= 1000
	1 &lt= nums[i] &lt= 10^9
	1 &lt= target &lt= 10^9
## Solutions:
```python
class Solution :
public:
    bool isMajorityElement(vector& nums, int target) :
        if (nums.size() == 0)   return false
        int l1 = 0
        int l2 = 0
        int r1 = nums.size() - 1
        int r2 = nums.size() - 1
        while (true) :   
            if (l1 <= r1) :
                int mid = l1 + (r1 - l1) / 2
                if (nums[mid] >= target) :
                    r1 = mid
                 else :
                    l1 = mid + 1
            if (l1 > r1)    return false
            if (l2 <= r2) :
                int mid = r2 - (r2 - l2) / 2
                if (nums[mid] <= target) :
                    l2 = mid
                 else :
                    r2 = mid - 1
            if (l2 > r2)    return false
            if (l2 - r1 + 1 > int(nums.size() / 2)) : // trap! 
                return true
            if (r2 - l1 + 1 <= int(nums.size() / 2)) : // trap!
                return false
```
# 741. Cherry Pickup
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Minimum Path Sum](minimum-path-sum.md)
  * [Dungeon Game](dungeon-game.md)
## Problem:
In a N x N grid representing a field of cherries, each cell is one of three possible integers.
	0 means the cell is empty, so you can pass through
	1 means the cell contains a cherry, that you can pick up and pass through
	-1 means the cell contains a thorn that blocks your way.
Your task is to collect maximum number of cherries possible by following the rules below:
	Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1)
	After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells
	When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0)
	If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Note:
	grid is an N by N 2D array, with 1 &lt= N &lt= 50.
	Each grid[i][j] is an integer in the set :-1, 0, 1.
	It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
## Solutions:
```python
class Solution :
public:
    int cherryPickup(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        unordered_map cache
        int ret = helper(grid, m, n, m - 1, n - 1, m - 1, n - 1, cache)
        return ret == -1 ? 0 : ret
private:
    int helper(const vector>& grid, int m, int n, int x1, int y1, int x2, int y2, unordered_map& cache) :
        if (x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)   return grid[x1][y1]
        int digest = positionDigest(m, n, x1, y1, x2, y2)
        if (cache.count(digest) > 0)    return cache[digest]
        int ret = 0
        if (grid[x1][y1] == 1) ++ret
        if (grid[x2][y2] == 1) ++ret
        if (x1 == x2 && y1 == y2 && grid[x1][y1] == 1) :
            ret -= 1
        int lastValue = -1
        for (int i = 0 i < 2 ++i) :
            for (int j = 0j < 2 ++j) :
                int prevX1 = x1 + direction[i][0]
                int prevY1 = y1 + direction[i][1]
                int prevX2 = x2 + direction[j][0]
                int prevY2 = y2 + direction[j][1]
                if (prevX1 >= 0 && prevY1 >= 0 && grid[prevX1][prevY1] != -1 && prevX2 >= 0 && prevY2 >= 0 && grid[prevX2][prevY2] != -1) :
                    lastValue = max(lastValue, helper(grid, m, n, prevX1, prevY1, prevX2, prevY2, cache))
        if (lastValue == -1)    ret = -1
        else :
            ret += lastValue
        cache[digest] = ret
        return ret
    int positionDigest(int m, int n, int x1, int y1, int x2, int y2) :
        int gridNum = m * n
        int position1 = x1 * n + y1
        int position2 = x2 * n + y2
        return position1 * gridNum + position2
    int direction[2][2] = :
        :-1, 0,
        :0, -1
```
# 70. Climbing Stairs
* *Difficulty: Easy*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Min Cost Climbing Stairs](min-cost-climbing-stairs.md)
  * [Fibonacci Number](fibonacci-number.md)
  * [N-th Tribonacci Number](n-th-tribonacci-number.md)
## Problem:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
## Solutions:
```python
class Solution :
public:
    int climbStairs(int n) :
        int prev = 0
        int ret = 1
        for (int i = 1 i <= n ++i) :
            int temp = ret
            ret = ret + prev
            prev = temp
        return ret
```
# 133. Clone Graph
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search, Graph*
* *Similar Questions:*
  * [Copy List with Random Pointer](copy-list-with-random-pointer.md)
## Problem:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
Example:
Input:
:&quot$id&quot:&quot1&quot,&quotneighbors&quot:[:&quot$id&quot:&quot2&quot,&quotneighbors&quot:[:&quot$ref&quot:&quot1&quot,:&quot$id&quot:&quot3&quot,&quotneighbors&quot:[:&quot$ref&quot:&quot2&quot,:&quot$id&quot:&quot4&quot,&quotneighbors&quot:[:&quot$ref&quot:&quot3&quot,:&quot$ref&quot:&quot1&quot],&quotval&quot:4],&quotval&quot:3],&quotval&quot:2,:&quot$ref&quot:&quot4&quot],&quotval&quot:1
Explanation:
Node 1&#39s value is 1, and it has two neighbors: Node 2 and 4.
Node 2&#39s value is 2, and it has two neighbors: Node 1 and 3.
Node 3&#39s value is 3, and it has two neighbors: Node 2 and 4.
Node 4&#39s value is 4, and it has two neighbors: Node 1 and 3.
Note:
	The number of nodes will be between 1 and 100.
	The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
	Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
	You must return the copy of the given node as a reference to the cloned graph.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    vector neighbors
    Node() :
    Node(int _val, vector _neighbors) :
        val = _val
        neighbors = _neighbors
*/
class Solution :
public:
    Node* cloneGraph(Node* node) :
        unordered_map oldToNew
        return helper(node, oldToNew)
    Node* helper(Node* node, unordered_map& oldToNew) :
        if (node == NULL)   return NULL
        if (oldToNew.count(node) > 0)   return oldToNew[node]
        Node* newNode = new Node(node->val, :)
        oldToNew[node] = newNode
        for (auto& neighbor : node->neighbors) :
            newNode->neighbors.push_back(helper(neighbor, oldToNew))
        return newNode
```
# 272. Closest Binary Search Tree Value II
* *Difficulty: Hard*
* *Topics: Stack, Tree*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
  * [Closest Binary Search Tree Value](closest-binary-search-tree-value.md)
## Problem:
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
Note:
	Given target value is a floating point.
	You may assume k is always valid, that is: k &le total nodes.
	You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
    4
   / \
  2   5
 / \
1   3
Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Iterator:
    public:
    Iterator(stack stk, bool forward): stk_(stk), forward_(forward) :
    int next() :
        TreeNode* node = stk_.top() stk_.pop()
        int ret = node->val
        node = forward_ ? node->right : node->left
        while (node) :
            stk_.push(node)
            node = forward_ ? node->left : node->right
        return ret
    // remember to has peek()
    int peek() :
        return stk_.top()->val
    bool hasNext() :
        return !stk_.empty()
    private:
        bool forward_
        stack stk_
class Solution :
public:
    vector closestKValues(TreeNode* root, double target, int k) :
        if (k == 0) return :
        if (root == NULL)   return :
        stack fstk
        stack bstk
        findHelper(root, target, fstk, bstk)
        Iterator forwardIter = Iterator(fstk, true)
        Iterator backIter = Iterator(bstk, false)
        if (forwardIter.peek() <= target) :
            forwardIter.next()
         else :
            backIter.next()
        vector ret
        for (int i = 0 i < k ++i) :
            if (!forwardIter.hasNext()) :
                ret.push_back(backIter.next())
                continue
            if (!backIter.hasNext()) :
                ret.push_back(forwardIter.next())
                continue
            int forwardVal = forwardIter.peek()
            int backVal = backIter.peek()
            if (abs(forwardVal - target) <= abs(backVal - target)) :
                ret.push_back(forwardVal)
                if (forwardIter.hasNext()) :
                    forwardIter.next()
             else :
                ret.push_back(backVal)
                if (backIter.hasNext()) :
                    backIter.next()
        return ret
    // differciate fstk and bstk!
    void findHelper(TreeNode* root, double target, stack& fstk, stack& bstk) :   
        if (double(root->val) == target) :
            fstk.push(root)
            bstk.push(root)
            return
        if (double(root->val) > target) :
            if (root->left) :
                fstk.push(root)
                findHelper(root->left, target, fstk, bstk)
                return
            fstk.push(root)
            bstk.push(root)
            return
        if (double(root->val) < target) :
            if (root->right) :
                bstk.push(root)
                findHelper(root->right, target, fstk, bstk)
                return
            fstk.push(root)
            bstk.push(root)
            return
```
# 270. Closest Binary Search Tree Value
* *Difficulty: Easy*
* *Topics: Binary Search, Tree*
* *Similar Questions:*
  * [Count Complete Tree Nodes](count-complete-tree-nodes.md)
  * [Closest Binary Search Tree Value II](closest-binary-search-tree-value-ii.md)
  * [Search in a Binary Search Tree](search-in-a-binary-search-tree.md)
## Problem:
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
Note:
	Given target value is a floating point.
	You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:
Input: root = [4,2,5,1,3], target = 3.714286
    4
   / \
  2   5
 / \
1   3
Output: 4
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int closestValue(TreeNode* root, double target) :
        int ret = root->val
        if (root->left) :
            int leftClose = closestValue(root->left, target)
            if (abs(ret - target) > abs(leftClose - target)) :
                ret = leftClose
        if (root->right) :
            int rightClose = closestValue(root->right, target)
            if (abs(ret - target) > abs(rightClose - target)) :
                ret = rightClose
        return ret
```
# 518. Coin Change 2
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
Input: amount = 10, coins = [10] 
Output: 1
Note:
You can assume that
	0 &lt= amount &lt= 5000
	1 &lt= coin &lt= 5000
	the number of coins is less than 500
	the answer is guaranteed to fit into signed 32-bit integer
## Solutions:
```python
class Solution :
public:
    int change(int amount, vector& coins) :
        int n = coins.size()
        if (n == 0) return amount == 0 ? 1 : 0
        vector> dp(n, vector(amount + 1, 0))
        for (int i = 0 i < n ++i) :
            dp[i][0] = 1
        for (int i = 0 i < coins.size() ++i) :
            for (int j = 1 j <= amount ++j) :
                dp[i][j] = (i - 1 >= 0 ? dp[i-1][j] : 0) + 
                    (j - coins[i] >= 0 ? dp[i][j - coins[i]] : 0)
        return dp[n-1][amount]
```
# 322. Coin Change
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Minimum Cost For Tickets](minimum-cost-for-tickets.md)
## Problem:
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
## Solutions:
```python
class Solution :
public:
    int coinChange(vector& coins, int amount) :
        if (amount < 0) return -1
        if (amount == 0) return 0 // retrun 0
        vector dp(amount + 1, INT_MAX)
        dp[0] = 0
        for (int i = 0 i < coins.size() ++i) :
            int val = coins[i]
            for (int j = 0 j <= amount ++j) :
                // transition function
                dp[j] = min(dp[j], j - val >= 0 && dp[j - val] != INT_MAX ? 1 + dp[j - val] : INT_MAX) // check INT_MAX
        return dp[amount] == INT_MAX ? -1 : dp[amount] // check INT_MAX
```
# 656. Coin Path
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [House Robber](house-robber.md)
  * [House Robber II](house-robber-ii.md)
## Problem:
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the array A indexed i+1, i+2, &hellip, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can&rsquot jump to the place indexed i in the array.
Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed N using minimum coins.
If there are multiple paths with the same cost, return the lexicographically smallest such path.
If it&#39s not possible to reach the place indexed N then you need to return an empty array.
Example 1:
Input: [1,2,4,-1,2], 2
Output: [1,3,5]
Example 2:
Input: [1,2,4,-1,2], 1
Output: []
Note:
	Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where Pai and Pbi differ, Pai &lt Pbi when no such i exists, then n &lt m.
	A1 &gt= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
	Length of A is in the range of [1, 1000].
	B is in the range of [1, 100].
## Solutions:
```python
class Solution :
public:
    vector cheapestJump(vector& A, int B) : // reverse order to get lexical smaller result
        int n = A.size()
        if (n == 0) return :
        if (A[0] == -1 || A[n-1] == -1) return : // this check is essential if we reverse the order of A
        reverse(A.begin(), A.end())
        vector dp(n, INT_MAX)
        vector prev(n, 0)
        dp[0] = A[0]
        prev[0] = -1
        for (int i= 1 i < n ++i) :
            if (A[i] == -1) continue
            for (int j = -1 j >= -B --j) :
                if (i + j < 0)  break
                if (dp[i+j] < dp[i]) :
                    dp[i] = dp[i+j]
                    prev[i] = i + j
            if (dp[i] != INT_MAX)
                dp[i] += A[i]
        vector ret
        int i = n - 1
        while (i >= 0 && dp[i] != INT_MAX) :
            ret.push_back(n - i)
            i = prev[i]
        if (i >= 0) return :
        return ret
```
# 40. Combination Sum II
* *Difficulty: Medium*
* *Topics: Array, Backtracking*
* *Similar Questions:*
  * [Combination Sum](combination-sum.md)
## Problem:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note:
	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
## Solutions:
```python
class Solution :
public:
    vector> combinationSum2(vector& candidates, int target) :
        sort(candidates.begin(), candidates.end())
        vector path
        vector> ret
        helper(candidates, 0, target, path, ret)
        return ret
    void helper(vector& candidates, int pos, int target, vector& path, vector>& ret) :
        if (target < 0) return
        if (pos == candidates.size()) :
            if (target == 0) :
                ret.push_back(path)
            return
        int val = candidates[pos]
        path.push_back(val)
        helper(candidates, pos + 1, target - val, path, ret)
        path.pop_back()
        while (pos + 1 < candidates.size() && candidates[pos + 1] == candidates[pos]) ++pos
        helper(candidates, pos + 1, target, path, ret)
```
# 216. Combination Sum III
* *Difficulty: Medium*
* *Topics: Array, Backtracking*
* *Similar Questions:*
  * [Combination Sum](combination-sum.md)
## Problem:
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Note:
	All numbers will be positive integers.
	The solution set must not contain duplicate combinations.
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
## Solutions:
```python
class Solution :
public:
    vector> combinationSum3(int k, int n) :
        vector path
        vector> ret
        helper(1, n, k, path, ret)
        return ret
    void helper(int pos, int target, int k, vector& path, vector>& ret) :
        if (target < 0) return
        if (pos == 10) :
            if (target == 0 && k == 0) :
                ret.push_back(path)
            return
        path.push_back(pos)
        helper(pos + 1, target - pos, k - 1, path, ret)
        path.pop_back()
        helper(pos + 1, target, k, path, ret)
```
# 39. Combination Sum
* *Difficulty: Medium*
* *Topics: Array, Backtracking*
* *Similar Questions:*
  * [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number.md)
  * [Combination Sum II](combination-sum-ii.md)
  * [Combinations](combinations.md)
  * [Combination Sum III](combination-sum-iii.md)
  * [Factor Combinations](factor-combinations.md)
  * [Combination Sum IV](combination-sum-iv.md)
## Problem:
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
## Solutions:
```python
class Solution :
public:
    vector> combinationSum(vector& candidates, int target) :
        sort(candidates.begin(), candidates.end())
        vector path
        vector> ret
        helper(candidates, 0, target, path, ret)
        return ret
    void helper(vector& candidates, int pos, int target, vector& path, vector>& ret) :  
        if (target < 0) return
        if (target == 0) :
            ret.push_back(path)
            return
        if (pos == candidates.size())   return
        path.push_back(candidates[pos])
        helper(candidates, pos, target - candidates[pos], path, ret)
        path.pop_back()
        helper(candidates, pos + 1, target, path, ret)
```
# 77. Combinations
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [Combination Sum](combination-sum.md)
  * [Permutations](permutations.md)
## Problem:
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
## Solutions:
```python
class Solution :
public:
    vector> combine(int n, int k) :
        vector path
        vector> ret
        helper(n, k, 1, path, ret)
        return ret
    void helper(int n, int k, int pos, vector& path, vector>& ret) :
        if (path.size() == k) :
            ret.push_back(path)
            return
        if (pos > n || n - pos + 1 + path.size() < k) :
            return
        path.push_back(pos)
        helper(n, k, pos + 1, path, ret)      
        path.pop_back()
        helper(n, k, pos + 1, path, ret)
```
# 175. Combine Two Tables
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
  * [Employee Bonus](employee-bonus.md)
## Problem:
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:
FirstName, LastName, City, State
## Solutions:
```python
# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address on Person.PersonId = Address.PersonId 
```
# 165. Compare Version Numbers
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
## Problem:
Compare two version numbers version1 and version2.
If version1 &gt version2 return 1 if version1 &lt version2 return -1otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not &quottwo and a half&quot or &quothalf way to version three&quot, it is the fifth second-level revision of the second first-level revision.
You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
Example 1:
Input: version1 = &quot0.1&quot, version2 = &quot1.1&quot
Output: -1
Example 2:
Input: version1 = &quot1.0.1&quot, version2 = &quot1&quot
Output: 1
Example 3:
Input: version1 = &quot7.5.2.4&quot, version2 = &quot7.5.3&quot
Output: -1
Example 4:
Input: version1 = &quot1.01&quot, version2 = &quot1.001&quot
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
Example 5:
Input: version1 = &quot1.0&quot, version2 = &quot1.0.0&quot
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
Note:
Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes. 
Version strings do not start or end with dots, and they will not be two consecutive dots.
## Solutions:
```python
class Solution :
public:
    int compareVersion(string version1, string version2) :
        int cur1 = 0
        int cur2 = 0
        int len1 = version1.length()
        int len2 = version2.length()
        while (cur1 < len1 || cur2 < len2) :
            int value1 = 0
            int value2 = 0
            while (cur1 < len1 && version1[cur1] == '0') :
                ++cur1
            while (cur1 < len1 && version1[cur1] != '.') :
                value1 = 10 * value1 + version1[cur1] - '0'
                ++cur1
            if (cur1 != len1) :
                ++cur1
            while (cur2 < len2 && version2[cur2] == '0') :
                ++cur2
            while (cur2 < len2 && version2[cur2] != '.') :
                value2 = 10 * value2 + version2[cur2] - '0'
                ++cur2
            if (cur2 != len2) :
                ++cur2
            if (value1 < value2) :
                return -1
             else if (value1 > value2) :
                return 1
        return 0
```
# 537. Complex Number Multiplication
* *Difficulty: Medium*
* *Topics: Math, String*
* *Similar Questions:*
## Problem:
Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
## Solutions:
```python
class Solution :
public:
    string complexNumberMultiply(string a, string b) :
        auto complex1 = parse(a)
        auto complex2 = parse(b)
        int real = complex1.first * complex2.first - complex1.second * complex2.second
        int img = complex1.first * complex2.second + complex2.first * complex1.second
        return to_string(real) + "+" + to_string(img) + "i"
private:
    pair parse(const string& str) :
        int real = 0
        int img = 0
        int realSign = 1
        int imgSign = 1
        int pos = 0
        if (str[pos] == '-') :
            realSign = -1
            ++pos
        while (str[pos] != '+') :
            real = real * 10 + str[pos] - '0'
            ++pos
        ++pos
        if (str[pos] == '-') :
            imgSign = -1
            ++pos
        while (str[pos] != 'i') :
            img = 10 * img + str[pos] - '0'
            ++pos
        return :real * realSign, img * imgSign
```
# 106. Construct Binary Tree from Inorder and Postorder Traversal
* *Difficulty: Medium*
* *Topics: Array, Tree, Depth-first Search*
* *Similar Questions:*
  * [Construct Binary Tree from Preorder and Inorder Traversal](construct-binary-tree-from-preorder-and-inorder-traversal.md)
## Problem:
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* buildTree(vector& inorder, vector& postorder) :
        return helper(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1)
    TreeNode* helper(vector& inorder, int inorderLeft, int inorderRight, vector& postorder, int postorderLeft, int postorderRight) :
        if (inorderRight < inorderLeft) return nullptr
        if (inorderLeft == inorderRight)    return new TreeNode(inorder[inorderLeft])
        TreeNode* root = new TreeNode(postorder[postorderRight])
        int pos = find(inorder.begin() + inorderLeft, inorder.begin() + inorderRight + 1, postorder[postorderRight]) - inorder.begin()
        int leftLen = pos - inorderLeft
        root->left = helper(inorder, inorderLeft, pos - 1, postorder, postorderLeft, postorderLeft + leftLen - 1)
        root->right = helper(inorder, pos + 1, inorderRight, postorder, postorderLeft + leftLen, postorderRight - 1)
        return root
```
# 105. Construct Binary Tree from Preorder and Inorder Traversal
* *Difficulty: Medium*
* *Topics: Array, Tree, Depth-first Search*
* *Similar Questions:*
  * [Construct Binary Tree from Inorder and Postorder Traversal](construct-binary-tree-from-inorder-and-postorder-traversal.md)
## Problem:
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* buildTree(vector& preorder, vector& inorder) :
        return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1)
    TreeNode* helper(vector& preorder, int preorderLeft, int preorderRight, vector& inorder, int inorderLeft, int inorderRight) :
        if (preorderRight < preorderLeft)   return NULL
        TreeNode* root = new TreeNode(preorder[preorderLeft])
        int pos = find(inorder.begin() + inorderLeft, inorder.begin() + inorderRight + 1, preorder[preorderLeft]) - inorder.begin()
        int leftLen = pos - inorderLeft
        int rightLen = inorderRight - pos
        root->left = helper(preorder, preorderLeft + 1, preorderLeft + 1 + leftLen - 1, inorder, inorderLeft, pos - 1)
        root->right = helper(preorder, preorderLeft + 1 + leftLen, preorderRight, inorder, pos + 1, inorderRight)
        return root
```
# 772. Construct Quad Tree
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.
Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.
Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:
Given the 8 x 8 grid below, we want to construct the corresponding quad tree:
It can be divided according to the definition above:
The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.
For the non-leaf nodes, val can be arbitrary, so it is represented as *.
Note:
	N is less than 1000 and guaranteened to be a power of 2.
	If you want to know more about the quad tree, you can refer to its wiki.
## Solutions:
```python
/*
// Definition for a QuadTree node.
class Node :
public:
    bool val
    bool isLeaf
    Node* topLeft
    Node* topRight
    Node* bottomLeft
    Node* bottomRight
    Node() :
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) :
        val = _val
        isLeaf = _isLeaf
        topLeft = _topLeft
        topRight = _topRight
        bottomLeft = _bottomLeft
        bottomRight = _bottomRight
*/
class Solution :
public:
    Node* construct(vector>& grid) :
        if (grid.size() == 0)   return new Node()
        return helper(grid, 0, 0, grid.size())
private:
    Node* helper(vector>& grid, int row, int col, int len) :
        // base case
        if (len == 1) :
            Node* node = new Node()
            node->val = (grid[row][col] == 1)
            node->isLeaf = true
            node->topLeft = nullptr
            node->topRight = nullptr
            node->bottomLeft = nullptr
            node->bottomRight = nullptr
            return node
        Node* upperLeft = helper(grid, row, col, len / 2)
        Node* upperRight = helper(grid, row, col + len /2, len / 2)
        Node* bottomLeft = helper(grid, row + len / 2, col, len / 2)
        Node* bottomRight = helper(grid, row + len / 2, col + len / 2, len / 2)
        if (upperLeft->isLeaf && upperRight->isLeaf && bottomLeft->isLeaf && bottomRight->isLeaf && upperLeft->val == upperRight->val && upperLeft->val == bottomLeft->val && upperLeft->val == bottomRight->val) :
            Node* node = new Node()
            node->val = upperLeft->val
            node->isLeaf = true
            node->topLeft = nullptr
            node->topRight = nullptr
            node->bottomLeft = nullptr
            node->bottomRight = nullptr
            return node
         else :
            return new Node(false, false, upperLeft, upperRight, bottomLeft, bottomRight)
```
# 606. Construct String from Binary Tree
* *Difficulty: Easy*
* *Topics: String, Tree*
* *Similar Questions:*
  * [Construct Binary Tree from String](construct-binary-tree-from-string.md)
  * [Find Duplicate Subtrees](find-duplicate-subtrees.md)
## Problem:
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     
Output: "1(2(4))(3)"
Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    string tree2str(TreeNode* t) :
        string ret
        helper(t, ret)
        return ret
private:
    void helper(TreeNode* t, string& s) :
        if (t == nullptr)   return
        s.append(to_string(t->val))
        if (!t->left && !t->right)  return
        s.push_back('(')
        helper(t->left, s)
        s.push_back(')')
        if (t->right) :
            s.push_back('(')
            helper(t->right, s)
            s.push_back(')')
```
# 492. Construct the Rectangle
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.
Example:
Input: 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
Note:
The given area won't exceed 10,000,000 and is a positive integer
The web page's width and length you designed must be positive integers.
## Solutions:
```python
class Solution :
public:
    vector constructRectangle(int area) :
        vector ret = :area, 1
        for (int i = 2 i <= sqrt(area) ++i) :
            if (area % i == 0) :
                ret = :area / i, i
        return ret
```
# 11. Container With Most Water
* *Difficulty: Medium*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Trapping Rain Water](trapping-rain-water.md)
## Problem:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. 
Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
## Solutions:
```python
class Solution :
public:
    int maxArea(vector& height) :
        int left = 0
        int right = height.size() - 1
        int ret = 0
        while (left < right) :
            ret = max(ret, (right - left) * min(height[left], height[right]))
            if (height[left] <= height[right]) :
                ++left
             else :
                --right
        return ret
```
### Proof sketch
Let's `dp[i][j]` denote the optimal solution if the two axises are between `i` and `j`, inclusive. The induction then should be:
```python
dp[i][j] = max((j - i) * min(height[i], height[j]), max(dp[i+1][j], dp[i][j-1]))
```
The only difference between `dp[i+1][j]` and `dp[i][j-1]` is the ability to use which axis as the boundary. Without losing generality, suppose `height[i] < height[j]`. If the optimal result comes from dp[i][j-1] and `ith` axis is used as the boundary. However, the result is definitely smaller than `(j - i) * min(height[i], height[j])`. 
# 219. Contains Duplicate II
* *Difficulty: Easy*
* *Topics: Array, Hash Table*
* *Similar Questions:*
  * [Contains Duplicate](contains-duplicate.md)
  * [Contains Duplicate III](contains-duplicate-iii.md)
## Problem:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
## Solutions:
```python
class Solution :
public:
    bool containsNearbyDuplicate(vector& nums, int k) :
        unordered_map valToIndex
        for (int i = 0 i < nums.size() ++i) :
            if (valToIndex.count(nums[i]) > 0 && i - valToIndex[nums[i]] <= k) :
                return true
            valToIndex[nums[i]] = i
        return false
```
# 220. Contains Duplicate III
* *Difficulty: Medium*
* *Topics: Sort, Ordered Map*
* *Similar Questions:*
  * [Contains Duplicate](contains-duplicate.md)
  * [Contains Duplicate II](contains-duplicate-ii.md)
## Problem:
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
## Solutions:
```python
class Solution :
public:
    bool containsNearbyAlmostDuplicate(vector& nums, int k, int t) :
        if (k < 0 || t < 0) return false
        long kl = abs(k) // long! not int!
        long tl = abs(t) // long! not int!
        set heap
        int initHeapSize = min(long(nums.size()), kl)
        for (int i = 0 i < initHeapSize ++i) :
            auto it = heap.lower_bound(nums[i] - tl)
            if (it != heap.end() && *it <= nums[i] + tl) return true // if not using long, overflow happens.
            heap.insert(nums[i])
        for (int i = kl  i < nums.size() ++i) :
            auto it = heap.lower_bound(nums[i] - tl)
            if (it != heap.end() && *it - nums[i] <= tl) return true
            heap.insert(nums[i])
            heap.erase(nums[i - k])
        return false
```
# 217. Contains Duplicate
* *Difficulty: Easy*
* *Topics: Array, Hash Table*
* *Similar Questions:*
  * [Contains Duplicate II](contains-duplicate-ii.md)
  * [Contains Duplicate III](contains-duplicate-iii.md)
## Problem:
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Example 1:
Input: [1,2,3,1]
Output: true
Example 2:
Input: [1,2,3,4]
Output: false
Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
## Solutions:
```python
class Solution :
public:
    bool containsDuplicate(vector& nums) :
        unordered_set numSet
        for (auto num : nums) :
            if (numSet.count(num) > 0) :
                return true
            numSet.insert(num)
        return false
```
# 405. Convert a Number to Hexadecimal
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
## Problem:
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0' otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:
Input:
26
Output:
"1a"
Example 2:
Input:
-1
Output:
"ffffffff"
## Solutions:
```python
class Solution :
public:
    string toHex(int num) :
        bool sign = (num >= 0)
        if (!sign) :
            num += INT_MAX
            num += 1
        string ret
        if (num == 0) : // this check is important!
            ret.push_back('0')
        while (num > 0) :
            ret.push_back(decimalToHex(num % 16))
            num /= 16
        if (!sign) :
            while (ret.size() != 8) :
                ret.push_back('0')
            ret.back() = decimalToHex(ret.back() - '0' + 8)
        reverse(ret.begin(), ret.end())
        return ret
private:
    char decimalToHex(int val) :
        if (val < 10)   return '0' + val
        else return 'a' + (val - 10)
```
# 758. Convert Binary Search Tree to Sorted Doubly Linked List
* *Difficulty: Medium*
* *Topics: Linked List, Divide and Conquer, Tree*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
## Problem:
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
Let&#39s take the following BST as an example, it may help you understand the problem better:
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
The figure below shows the circular doubly linked list for the BST above. The &quothead&quot symbol means the node it points to is the smallest element of the linked list.
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.
The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    Node* left
    Node* right
    Node() :
    Node(int _val, Node* _left, Node* _right) :
        val = _val
        left = _left
        right = _right
*/
class Solution :
public:
    Node* treeToDoublyList(Node* root) :
        if (root == NULL)   return NULL
        Node* dummy = new Node(0, NULL, NULL)
        Node* tail = dummy
        helper(root, tail)
        tail->right = dummy->right
        dummy->right->left = tail
        return dummy->right
    void helper(Node* root, Node*& tail) :
        if (root == NULL)   return
        Node* left = root->left
        Node* right = root->right
        helper(left, tail)
        tail->right = root
        root->left = tail
        tail = root
        helper(right, tail)
```
# 538. Convert BST to Greater Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13
Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* convertBST(TreeNode* root) :
        int sum = 0
        helper(root, sum)
        return root
private:
    void helper(TreeNode* root, int& sum) :
        if (root == nullptr)    return
        helper(root->right, sum)
        root->val += sum
        sum = root->val
        helper(root->left, sum)
```
# 108. Convert Sorted Array to Binary Search Tree
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Convert Sorted List to Binary Search Tree](convert-sorted-list-to-binary-search-tree.md)
## Problem:
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* sortedArrayToBST(vector& nums) :
        int n = nums.size()
        return helper(nums, 0, n - 1)
    TreeNode* helper(vector& nums, int left, int right) :
        if (left > right)   return NULL
        if (left == right)  return new TreeNode(nums[left])
        int mid = left + (right - left)/2
        TreeNode* root = new TreeNode(nums[mid])
        root->left = helper(nums, left, mid - 1)
        root->right = helper(nums, mid + 1, right)
        return root
```
# 109. Convert Sorted List to Binary Search Tree
* *Difficulty: Medium*
* *Topics: Linked List, Depth-first Search*
* *Similar Questions:*
  * [Convert Sorted Array to Binary Search Tree](convert-sorted-array-to-binary-search-tree.md)
## Problem:
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* sortedListToBST(ListNode* head) :
        if (head == nullptr)    return nullptr
        int count = 0
        ListNode* cur = head
        while (cur) :
            ++count
            cur = cur->next
        return helper(head, count)        
    TreeNode* helper(ListNode*& head, int count) :
        if (count == 0) return nullptr
        if (count == 1) :
            int val = head->val
            head = head->next
            return new TreeNode(val)
        int mid = (count+1)/2
        int leftCount = mid - 1
        int rightCount = count - 1 - leftCount
        TreeNode* left = helper(head, leftCount)
        int val = head->val
        head = head->next
        TreeNode* root = new TreeNode(val)
        TreeNode* right = helper(head, rightCount)
        root->left = left
        root->right = right
        return root
```
# 1070. Convert to Base -2
* *Difficulty: Medium*
* *Topics: Math*
* *Similar Questions:*
## Problem:
Given a number N, return a string consisting of &quot0&quots and &quot1&quots that represents its value in base -2 (negative two).
The returned string must have no leading zeroes, unless the string is &quot0&quot.
Example 1:
Input: 2
Output: &quot110&quot
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:
Input: 3
Output: &quot111&quot
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:
Input: 4
Output: &quot100&quot
Explantion: (-2) ^ 2 = 4
Note:
	0 &lt= N &lt= 10^9
## Solutions:
```python
class Solution :
public:
    string baseNeg2(int N) :
        if (N == 0) return "0"
        string ret
        while (N != 0) :
            if (N % 2 == 0) :
                ret.push_back('0')
                N /= -2
             else :
                ret.push_back('1')
                N -= 1
                N /= -2
        reverse(ret.begin(), ret.end())
        return ret
```
# 469. Convex Polygon
* *Difficulty: Medium*
* *Topics: Math*
* *Similar Questions:*
## Problem:
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).
Note:
	There are at least 3 and at most 10,000 points.
	Coordinates are in the range -10,000 to 10,000.
	You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don&#39t intersect each other.
Example 1:
[[0,0],[0,1],[1,1],[1,0]]
Answer: True
Explanation:
Example 2:
[[0,0],[0,10],[10,10],[10,0],[5,5]]
Answer: False
Explanation:
## Solutions:
```python
class Solution :
public:
    bool isConvex(vector>& points) :
        int direction = 0
        int n = points.size()
        for (int i = 0 i < points.size() ++i) :
            int newDirection = orientation(points[i%n], points[(i+1)%n], points[(i+2)%n])
            if (newDirection == 0)  continue
            if (newDirection * direction < 0)   return false
            direction = newDirection
        return true
    int orientation(vector& a, vector& b, vector& c) :
        vector v1 = :b[0] - a[0], b[1] - a[1]
        vector v2 = :c[0] - b[0], c[1] - b[1]
        int prodDiff = v1[0] * v2[1] - v1[1] * v2[0]
        if (prodDiff > 0)   return 1
        else if (prodDiff < 0)   return -1
        else return 0
```
# 138. Copy List with Random Pointer
* *Difficulty: Medium*
* *Topics: Hash Table, Linked List*
* *Similar Questions:*
  * [Clone Graph](clone-graph.md)
## Problem:
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
Example 1:
Input:
:&quot$id&quot:&quot1&quot,&quotnext&quot::&quot$id&quot:&quot2&quot,&quotnext&quot:null,&quotrandom&quot::&quot$ref&quot:&quot2&quot,&quotval&quot:2,&quotrandom&quot::&quot$ref&quot:&quot2&quot,&quotval&quot:1
Explanation:
Node 1&#39s value is 1, both of its next and random pointer points to Node 2.
Node 2&#39s value is 2, its next pointer points to null and its random pointer points to itself.
Note:
	You must return the copy of the given head as a reference to the cloned list.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    Node* next
    Node* random
    Node() :
    Node(int _val, Node* _next, Node* _random) :
        val = _val
        next = _next
        random = _random
*/
class Solution :
public:
    Node* copyRandomList(Node* head) :
        copyNodes(head)
        copyRandomPointers(head)
        return partition(head)
    void copyNodes(Node* head) :
        while (head) :
            Node* nodeCopy = new Node(head->val, head->next, nullptr)
            head->next = nodeCopy
            head = nodeCopy->next
    void copyRandomPointers(Node* head) :
        while (head) :
            head->next->random = head->random == nullptr ? nullptr : head->random->next // pay attention to null random pointer
            head = head->next->next
    Node* partition(Node* head) :
        Node* dummy = new Node(0, nullptr, nullptr)
        Node* tail = dummy
        while (head) :
            tail->next = head->next
            tail = tail->next
            head->next = head->next->next
            head = head->next
        return dummy->next
```
# 38. Count and Say
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Encode and Decode Strings](encode-and-decode-strings.md)
  * [String Compression](string-compression.md)
## Problem:
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as &quotone 1&quot or 11.
11 is read off as &quottwo 1s&quot or 21.
21 is read off as &quotone 2, then one 1&quot or 1211.
Given an integer n where 1 &le n &le 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
Example 1:
Input: 1
Output: &quot1&quot
Example 2:
Input: 4
Output: &quot1211&quot
## Solutions:
```python
class Solution :
public:
    string countAndSay(int n) :
        if (n == 1) return "1"
        string last = countAndSay(n - 1)
        string ret
        char prev = last[0]
        int count = 0
        for (auto c : last) :
            if (c == prev) :
                ++count
             else :
                ret.push_back(count + '0')
                ret.push_back(prev)
                count = 1
                prev = c
        if (count > 0) :
            ret.push_back(count + '0')
            ret.push_back(prev)
        return ret
```
# 222. Count Complete Tree Nodes
* *Difficulty: Medium*
* *Topics: Binary Search, Tree*
* *Similar Questions:*
  * [Closest Binary Search Tree Value](closest-binary-search-tree-value.md)
## Problem:
Given a complete binary tree, count the number of nodes.
Note: 
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Example:
Input: 
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int countNodes(TreeNode* root) :
        if (root == nullptr)    return 0
        int leftLevel = getLeftLevel(root)
        int rightLevel = getRightLevel(root)
        if (leftLevel == rightLevel) :
            return (1 << leftLevel) - 1
         else :
            return 1 + countNodes(root->left) + countNodes(root->right)
private:
    int getLeftLevel(TreeNode* root) :
        if (root == nullptr)    return 0
        return 1 + getLeftLevel(root->left)
    int getRightLevel(TreeNode* root) :
        if (root == nullptr)    return 0
        return 1 + getRightLevel(root->right)
```
# 357. Count Numbers with Unique Digits
* *Difficulty: Medium*
* *Topics: Math, Dynamic Programming, Backtracking*
* *Similar Questions:*
## Problem:
Given a non-negative integer n, count all numbers with unique digits, x, where 0 &le x &lt 10n.
Example:
Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 &le x &lt 100, 
             excluding 11,22,33,44,55,66,77,88,99
## Solutions:
```python
class Solution :
public:
    int countNumbersWithUniqueDigits(int n) :
        if (n == 0) return 1
        if (n == 1) return 10
        if (n > 10)    return countNumbersWithUniqueDigits(10)
        return 9 * getUnique(n - 1) + countNumbersWithUniqueDigits(n - 1)
private:
    inline int getUnique(int n) :
        int ret = 1
        for (int i = 0 i < n ++i) :
            ret *= (9 - i)
        return ret
```
# 315. Count of Smaller Numbers After Self
* *Difficulty: Hard*
* *Topics: Binary Search, Divide and Conquer, Sort, Binary Indexed Tree, Segment Tree*
* *Similar Questions:*
  * [Count of Range Sum](count-of-range-sum.md)
  * [Queue Reconstruction by Height](queue-reconstruction-by-height.md)
  * [Reverse Pairs](reverse-pairs.md)
## Problem:
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
Example:
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
## Solutions:
```python
class Solution :
public:
    class BIT :
        public:
            BIT(int upper) :
                nums.resize(upper + 1)
                upperBound = upper
            void add(int index) :
                while (index <= upperBound) :
                    ++nums[index]
                    index += lowerBit(index)
            int query(int index) :
                int sum = 0
                while (index > 0) :
                    sum += nums[index]
                    index -= lowerBit(index)
                return sum
            inline int lowerBit(int i) :
                return i & (-i)
        private:
            int upperBound
            vector nums
    vector countSmaller(vector& nums) :
        if (nums.size() == 0)   return :
        int smallest = *min_element(nums.begin(), nums.end())
        int offset = 0
        if (smallest < 1) :
            offset = 1 - smallest // offset is 1 not 0
        int upper = *max_element(nums.begin(), nums.end())
        BIT bit(upper+offset)
        int n = nums.size()
        vector ret(n)
        for (int i = n - 1 i >= 0 --i) :
            int val = nums[i] + offset
            ret[i] = bit.query(val-1) // query is tricky!
            bit.add(val)
        return ret
```
# 204. Count Primes
* *Difficulty: Easy*
* *Topics: Hash Table, Math*
* *Similar Questions:*
  * [Ugly Number](ugly-number.md)
  * [Ugly Number II](ugly-number-ii.md)
  * [Perfect Squares](perfect-squares.md)
## Problem:
Count the number of prime numbers less than a non-negative number, n.
Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
## Solutions:
```python
class Solution :
public:
    int countPrimes(int n) :
        if (n <= 1) return 0
        vector valid(n, true)
        for (int i = 2 i <= sqrt(n) ++i) :
            if (!valid[i]) continue
            for (int j = i * 2 j < n j = j + i) :
                valid[j] = false
        int count = 0
        for (int i = 2 i < n ++i) :
            if (valid[i]) ++count
        return count
```
# 1131. Count Substrings with Only One Distinct Letter
* *Difficulty: Easy*
* *Topics: Math, String*
* *Similar Questions:*
## Problem:
Given a string S, return the number of substrings that have only one distinct letter.
Example 1:
Input: S = &quotaaaba&quot
Output: 8
Explanation: The substrings with one distinct letter are &quotaaa&quot, &quotaa&quot, &quota&quot, &quotb&quot.
&quotaaa&quot occurs 1 time.
&quotaa&quot occurs 2 times.
&quota&quot occurs 4 times.
&quotb&quot occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:
Input: S = &quotaaaaaaaaaa&quot
Output: 55
Constraints:
	1 &lt= S.length &lt= 1000
	S[i] consists of only lowercase English letters.
## Solutions:
```python
class Solution :
public:
    int countLetters(string S) :
        int count = 0
        int consecutive = 1
        for (int i = 1 i < S.length() ++i) :
            if (S[i] == S[i-1]) :
                ++consecutive
             else :
                count += calculate(consecutive)
                consecutive = 1
        count += calculate(consecutive)
        return count
private:
    int calculate(int num) :
        return num * (num + 1) / 2
```
# 250. Count Univalue Subtrees
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Subtree of Another Tree](subtree-of-another-tree.md)
  * [Longest Univalue Path](longest-univalue-path.md)
## Problem:
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.
Example :
Input:  root = [5,1,5,5,5,null,5]
              5
             / \
            1   5
           / \   \
          5   5   5
Output: 4
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    struct UniInfo :
        bool inclusive
        int num
        UniInfo (bool inclusive, int num) :
            this->inclusive = inclusive
            this->num = num
    int countUnivalSubtrees(TreeNode* root) :
        if (root == nullptr)    return 0
        auto ret = helper(root)
        return ret.num
    UniInfo helper(TreeNode* root) :
        if (root->left == nullptr && root->right == nullptr)    return :true, 1
        if (root->left == nullptr) :
            auto rightInfo = helper(root->right)
            if (rightInfo.inclusive && root->val == root->right->val) return :true, rightInfo.num + 1
            return :false, rightInfo.num
         else if (root->right == nullptr) :
            auto leftInfo = helper(root->left)
            if (leftInfo.inclusive && root->val == root->left->val) return :true, leftInfo.num + 1
            return :false, leftInfo.num
         else :
            auto leftInfo = helper(root->left)
            auto rightInfo = helper(root->right)
            if (leftInfo.inclusive && rightInfo.inclusive && root->val == root->left->val && root->val == root->right->val) :
                return :true, leftInfo.num + rightInfo.num + 1
             else :
                return :false, leftInfo.num + rightInfo.num
```
# 1332. Count Vowels Permutation
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
## Problem:
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
	Each character is a lower case vowel (&#39a&#39, &#39e&#39, &#39i&#39, &#39o&#39, &#39u&#39)
	Each vowel &#39a&#39 may only be followed by an &#39e&#39.
	Each vowel &#39e&#39 may only be followed by an &#39a&#39 or an &#39i&#39.
	Each vowel &#39i&#39 may not be followed by another &#39i&#39.
	Each vowel &#39o&#39 may only be followed by an &#39i&#39 or a &#39u&#39.
	Each vowel &#39u&#39 may only be followed by an &#39a&#39.
Since the answer may be too large, return it modulo 10^9 + 7.
Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: &quota&quot, &quote&quot, &quoti&quot , &quoto&quot and &quotu&quot.
Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: &quotae&quot, &quotea&quot, &quotei&quot, &quotia&quot, &quotie&quot, &quotio&quot, &quotiu&quot, &quotoi&quot, &quotou&quot and &quotua&quot.
Example 3: 
Input: n = 5
Output: 68
Constraints:
	1 &lt= n &lt= 2 * 10^4
## Solutions:
```python
class Solution :
public:
    int countVowelPermutation(int n) :
        if (n == 0) return 1
        if (n == 1) return 5
        vector> dp(n)
        dp[0] = :
            :'a', 1,
            :'e', 1,
            :'i', 1,
            :'o', 1,
            :'u', 1
        for (int i = 1 i < n ++i) :
            unordered_map charToCount
            for (auto& entry : dp[i-1]) :
                char c = entry.first
                int count = entry.second
                for (auto& follower : followers[c]) :
                    charToCount[follower] = (charToCount[follower] + count) % MOD
            dp[i] = charToCount
        int ret = 0
        for (auto& entry : dp[n-1]) :
            ret = (ret + entry.second) % MOD
        return ret
private:
    const int MOD = 1e9 + 7
    unordered_map> followers :
        :'a', :'e',
        :'e', :'a', 'i',
        :'i', :'a', 'e', 'o', 'u',
        :'o', :'i', 'u',
        :'u', :'a'
```
# 338. Counting Bits
* *Difficulty: Medium*
* *Topics: Dynamic Programming, Bit Manipulation*
* *Similar Questions:*
  * [Number of 1 Bits](number-of-1-bits.md)
## Problem:
Given a non negative integer number num. For every numbers i in the range 0 &le i &le num calculate the number of 1&#39s in their binary representation and return them as an array.
Example 1:
Input: 2
Output: [0,1,1]
Example 2:
Input: 5
Output: [0,1,1,2,1,2]
Follow up:
	It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
	Space complexity should be O(n).
	Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
## Solutions:
```python
class Solution :
public:
    vector countBits(int num) :
        vector ret(num + 1, 0)
        for (int i = 1 i <= num ++i) :
            ret[i] = ret[i&(i-1)] + 1
        return ret
```
# 207. Course Schedule
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search, Graph, Topological Sort*
* *Similar Questions:*
  * [Course Schedule II](course-schedule-ii.md)
  * [Graph Valid Tree](graph-valid-tree.md)
  * [Minimum Height Trees](minimum-height-trees.md)
  * [Course Schedule III](course-schedule-iii.md)
## Problem:
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:
	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
	You may assume that there are no duplicate edges in the input prerequisites.
## Solutions:
```python
class Solution :
public:
    bool canFinish(int numCourses, vector>& prerequisites) :
        vector> graph(numCourses, vector())
        vector visit(numCourses)
        for (auto a : prerequisites) :
            graph[a[1]].push_back(a[0])
        for (int i = 0 i < numCourses ++i) :
            if (!canFinishDFS(graph, visit, i)) return false
        return true
    bool canFinishDFS(vector>& graph, vector& visit, int i) :
        if (visit[i] == -1) return false
        if (visit[i] == 1) return true
        visit[i] = -1
        for (auto a : graph[i]) :
            if (!canFinishDFS(graph, visit, a)) return false
        visit[i] = 1
        return true
```
# 1035. Cousins in Binary Tree
* *Difficulty: Easy*
* *Topics: Tree, Breadth-first Search*
* *Similar Questions:*
  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)
## Problem:
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
Note:
	The number of nodes in the tree will be between 2 and 100.
	Each node has a unique integer value from 1 to 100.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isCousins(TreeNode* root, int x, int y) :
        int levels[2] = :-1, -2
        queue q
        int level = 0
        q.push(root)
        while (!q.empty()) :
            int size = q.size()
            for (int i = 0 i < size ++i) :
                TreeNode* node = q.front() q.pop()
                if (node == nullptr)   continue
                if (node->val == x) levels[0] = level
                if (node->val == y) levels[1] = level
                if (levels[0] == levels[1]) return true
                if (node->left && node->right && (node->left->val == x && node->right->val == y || node->left->val == y && node->right->val == x))  return false
                q.push(node->left)
                q.push(node->right)
            ++level
        return false
```
# 754. Cracking the Safe
* *Difficulty: Hard*
* *Topics: Math, Depth-first Search*
* *Similar Questions:*
## Problem:
There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.
While entering a password, the last n digits entered will automatically be matched against the correct password.
For example, assuming the correct password is &quot345&quot, if you type &quot012345&quot, the box will open because the correct password matches the suffix of the entered password.
Return any password of minimum length that is guaranteed to open the box at some point of entering it.
Example 1:
Input: n = 1, k = 2
Output: &quot01&quot
Note: &quot10&quot will be accepted too.
Example 2:
Input: n = 2, k = 2
Output: &quot00110&quot
Note: &quot01100&quot, &quot10011&quot, &quot11001&quot will be accepted too.
Note:
	n will be in the range [1, 4].
	k will be in the range [1, 10].
	k^n will be at most 4096.
## Solutions:
```python
class Solution :
public:
    string crackSafe(int n, int k) :
        const int total_len = pow(k, n) + n - 1
        string ans(n, '0')
        unordered_set visited:ans
        if (dfs(ans, total_len, n, k, visited))
            return ans
        return ""
private:
    bool dfs(string& ans, const int total_len, const int n, const int k, unordered_set& visited) : // return bool
        if (visited.size() == pow(k,n))
            return true
        string node = ans.substr(ans.length() - n + 1, n - 1)
        for (char c = '0' c < '0' + k ++c) :
            node.push_back(c)
            if (!visited.count(node)) :
                ans.push_back(c)
                visited.insert(node)
                if (dfs(ans, total_len, n, k, visited)) return true
                visited.erase(node)
                ans.pop_back()
            node.pop_back()
        return false
```
# 321. Create Maximum Number
* *Difficulty: Hard*
* *Topics: Dynamic Programming, Greedy*
* *Similar Questions:*
  * [Remove K Digits](remove-k-digits.md)
  * [Maximum Swap](maximum-swap.md)
## Problem:
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k &lt= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.
Note: You should try to optimize your time and space complexity.
Example 1:
Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:
Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:
Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
## Solutions:
```python
class Solution :
public:
    vector maxNumber(vector& nums1, vector& nums2, int k) :
        vector ret
        for (int i = 0 i <= nums1.size() ++i) :
            int deleteNum1 = nums1.size() - i
            int deleteNum2 = nums2.size() - (k - i)
            if (deleteNum1 < 0 || deleteNum2 < 0 || k - i < 0) continue // sanity check
            vector deleted1 = deleteDigit(nums1, deleteNum1)
            vector deleted2 = deleteDigit(nums2, deleteNum2)
            vector num = merge(deleted1, deleted2)
            ret = max(ret, num)
        return ret
private:
    bool greater(vector& num1, vector& num2) : // it is not necessary to define it ourself
        for (int i = 0 i < min(num1.size(), num2.size()) ++i) :
            if (num1[i] > num2[i])  return true
            if (num1[i] < num2[i])  return false
        return (num1.size() >= num2.size())
    vector deleteDigit(vector nums, int k) :
        nums.push_back(10)
        vector stk
        for (auto& num : nums) :
            while (!stk.empty() && k > 0 && stk.back() < num) :
                stk.pop_back()
                --k
            stk.push_back(num)
        stk.pop_back()
        return stk
    vector merge(const vector nums1, const vector nums2) :
        vector ans(nums1.size() + nums2.size())
        auto s1 = nums1.cbegin()
        auto e1 = nums1.cend()
        auto s2 = nums2.cbegin()
        auto e2 = nums2.cend()        
        int index = 0
        while (s1 != e1 || s2 != e2)
            ans[index++] = 
              lexicographical_compare(s1, e1, s2, e2) ? *s2++ : *s1++
        return ans
```
# 739. Daily Temperatures
* *Difficulty: Medium*
* *Topics: Hash Table, Stack*
* *Similar Questions:*
  * [Next Greater Element I](next-greater-element-i.md)
## Problem:
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
## Solutions:
```python
class Solution :
public:
    vector dailyTemperatures(vector& T) :
        int n = T.size()
        vector ret(n, 0)
        stack stk
        for (int i = 0 i < T.size() ++i) :
            while (!stk.empty() && T[stk.top()] < T[i]) :
                ret[stk.top()] = i - stk.top()
                stk.pop()
            stk.push(i)
        return ret
```
# 1260. Day of the Year
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
## Problem:
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
Example 1:
Input: date = &quot2019-01-09&quot
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:
Input: date = &quot2019-02-10&quot
Output: 41
Example 3:
Input: date = &quot2003-03-01&quot
Output: 60
Example 4:
Input: date = &quot2004-03-01&quot
Output: 61
Constraints:
	date.length == 10
	date[4] == date[7] == &#39-&#39, and all other date[i]&#39s are digits
	date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
## Solutions:
```python
class Solution :
public:
    int dayOfYear(string date) :
        int year = 0
        for (int i = 0 i < 4 ++i) :
            year = 10 * year + date[i] - '0'
        int month = 10 * (date[5] - '0') + date[6] - '0'
        int day = 10 * (date[8] - '0') + date[9] - '0'
        int dayNum[12] = :31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 // non-leap year
        bool leapYear = false
        if ((year % 100 == 0 && year % 400 == 0) || (year % 100 != 0 && year % 4 == 0)) :
            leapYear = true
        if (leapYear) :
            dayNum[1] = 29
        int count = 0
        for (int i = 0 i < month - 1 ++i) :
            count += dayNum[i]
        return count + day
```
# 394. Decode String
* *Difficulty: Medium*
* *Topics: Stack, Depth-first Search*
* *Similar Questions:*
  * [Encode String with Shortest Length](encode-string-with-shortest-length.md)
  * [Number of Atoms](number-of-atoms.md)
  * [Brace Expansion](brace-expansion.md)
## Problem:
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won&#39t be input like 3a or 2[4].
Examples:
s = &quot3[a]2[bc]&quot, return &quotaaabcbc&quot.
s = &quot3[a2[c]]&quot, return &quotaccaccacc&quot.
s = &quot2[abc]3[cd]ef&quot, return &quotabcabccdcdcdef&quot.
## Solutions:
```python
class Solution :
public:
    string decodeString(string s) :
        int pos = 0
        return helper(s, pos)
private:
    string helper(string& s, int& pos) :
        string ret
        int n = 0
        while (pos < s.length()) :
            char c = s[pos]
            if (isdigit(c)) :
                ++pos // consume digit
                n = 10 * n + c - '0'
             else if (c == '[') :
                ++pos // consume '['
                string innerString = helper(s, pos)
                while (n > 0) :
                    ret.append(innerString)
                    --n
             else if (c == ']') :
                ++pos // consume ']'
                return ret
             else :
                ++pos
                ret.push_back(c)
        return ret
```
# 91. Decode Ways
* *Difficulty: Medium*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
  * [Decode Ways II](decode-ways-ii.md)
## Problem:
A message containing letters from A-Z is being encoded to numbers using the following mapping:
&#39A&#39 -&gt 1
&#39B&#39 -&gt 2
...
&#39Z&#39 -&gt 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: &quot12&quot
Output: 2
Explanation: It could be decoded as &quotAB&quot (1 2) or &quotL&quot (12).
Example 2:
Input: &quot226&quot
Output: 3
Explanation: It could be decoded as &quotBZ&quot (2 26), &quotVF&quot (22 6), or &quotBBF&quot (2 2 6).
## Solutions:
```python
class Solution :
public:
    int numDecodings(string s) :
        int len = s.length()
        vector cache(len, -1)
        return helper(s, 0, cache)
    int helper(string s, int pos, vector& cache) :
        if (pos > s.length())  return 0
        if (pos == s.length())  return 1
        if (cache[pos] != -1)   return cache[pos]
        int count = 0
        if (s[pos] == '0')  return 0
        count += helper(s, pos + 1, cache)
        if (pos + 1 < s.length()) :
            if (10*(s[pos] - '0') + s[pos + 1] - '0' <= 26) :
                count += helper(s, pos + 2, cache)
        cache[pos] = count
        return count
```
# 697. Degree of an Array
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Maximum Subarray](maximum-subarray.md)
## Problem:
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
## Solutions:
```python
class Solution :
public:
    int findShortestSubArray(vector& nums) :
        unordered_map> numToIndex
        for (int i = 0 i < nums.size() ++i) :
            int num = nums[i]
            numToIndex[num].push_back(i)
        int ret = INT_MAX
        int freq = 0
        for (auto& entry : numToIndex) :
            if (entry.second.size() > freq) :
                freq = entry.second.size()
                ret = entry.second.back() - entry.second[0] + 1
             else if (entry.second.size() == freq) :
                ret = min(ret, entry.second.back() - entry.second[0] + 1)
        return ret
```
# 196. Delete Duplicate Emails
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:
Your output is the whole Person table after executing your sql. Use delete statement.
## Solutions:
```python
# Write your MySQL query statement below
delete p1
 FROM Person p1 join Person p2
 on p1.Email = p2.Email AND p1.Id > p2.Id
```
# 450. Delete Node in a BST
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Split BST](split-bst.md)
## Problem:
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).
Example:
root = [5,3,6,2,4,null,7]
key = 3
    5
   / \
  3   6
 / \   \
2   4   7
Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
    5
   / \
  4   6
 /     \
2       7
Another valid answer is [5,2,6,null,4,null,7].
    5
   / \
  2   6
   \   \
    4   7
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* deleteNode(TreeNode* root, int key) :
        if (root == NULL)   return NULL
        if (key val) :
            root->left = deleteNode(root->left, key)
         else if (key > root->val) :
            root->right = deleteNode(root->right, key)
         else :
            if (root->left == NULL) :
                return root->right
            if (root->right == NULL) :
                return root->left
            TreeNode* prev = root
            TreeNode* cur = root->right
            while(cur->left) :
                prev = cur
                cur = cur->left
            // it is very important to have this check
             if (prev == root)
                prev->right = cur->right
            else 
                prev->left = cur->right
            TreeNode* newRoot = cur
            newRoot->left = root->left
            newRoot->right = root->right
            root = newRoot
        return root
```
# 237. Delete Node in a Linked List
* *Difficulty: Easy*
* *Topics: Linked List*
* *Similar Questions:*
  * [Remove Linked List Elements](remove-linked-list-elements.md)
## Problem:
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Given linked list -- head = [4,5,1,9], which looks like following:
Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -&gt 1 -&gt 9 after calling your function.
Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -&gt 5 -&gt 9 after calling your function.
Note:
	The linked list will have at least two elements.
	All of the nodes&#39 values will be unique.
	The given node will not be the tail and it will always be a valid node of the linked list.
	Do not return anything from your function.
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    void deleteNode(ListNode* node) :
        node->val = node->next->val
        node->next = node->next->next
```
# 1209. Design Bounded Blocking Queue
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
Implement a thread safe bounded blocking queue that has the following methods:
	BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
	void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
	int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
	int size() Returns the number of elements currently in the queue.
Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only makes calls to the enqueue method or a consumer thread that only makes calls to the dequeue method. The size method will be called after every test case.
Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview.
Example 1:
Input:
1
1
[&quotBoundedBlockingQueue&quot,&quotenqueue&quot,&quotdequeue&quot,&quotdequeue&quot,&quotenqueue&quot,&quotenqueue&quot,&quotenqueue&quot,&quotenqueue&quot,&quotdequeue&quot]
[[2],[1],[],[],[0],[2],[3],[4],[]]
Output:
[1,0,2,2]
Explanation:
Number of producer threads = 1
Number of consumer threads = 1
BoundedBlockingQueue queue = new BoundedBlockingQueue(2)   // initialize the queue with capacity = 2.
queue.enqueue(1)   // The producer thread enqueues 1 to the queue.
queue.dequeue()    // The consumer thread calls dequeue and returns 1 from the queue.
queue.dequeue()    // Since the queue is empty, the consumer thread is blocked.
queue.enqueue(0)   // The producer thread enqueues 0 to the queue. The consumer thread is unblocked and returns 0 from the queue.
queue.enqueue(2)   // The producer thread enqueues 2 to the queue.
queue.enqueue(3)   // The producer thread enqueues 3 to the queue.
queue.enqueue(4)   // The producer thread is blocked because the queue&#39s capacity (2) is reached.
queue.dequeue()    // The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
queue.size()       // 2 elements remaining in the queue. size() is always called at the end of each test case.
Example 2:
Input:
3
4
[&quotBoundedBlockingQueue&quot,&quotenqueue&quot,&quotenqueue&quot,&quotenqueue&quot,&quotdequeue&quot,&quotdequeue&quot,&quotdequeue&quot,&quotenqueue&quot]
[[3],[1],[0],[2],[],[],[],[3]]
Output:
[1,0,2,1]
Explanation:
Number of producer threads = 3
Number of consumer threads = 4
BoundedBlockingQueue queue = new BoundedBlockingQueue(3)   // initialize the queue with capacity = 3.
queue.enqueue(1)   // Producer thread P1 enqueues 1 to the queue.
queue.enqueue(0)   // Producer thread P2 enqueues 0 to the queue.
queue.enqueue(2)   // Producer thread P3 enqueues 2 to the queue.
queue.dequeue()    // Consumer thread C1 calls dequeue.
queue.dequeue()    // Consumer thread C2 calls dequeue.
queue.dequeue()    // Consumer thread C3 calls dequeue.
queue.enqueue(3)   // One of the producer threads enqueues 3 to the queue.
queue.size()       // 1 element remaining in the queue.
Since the number of threads for producer/consumer is greater than 1, we do not know how the threads will be scheduled in the operating system, even though the input seems to imply the ordering. Therefore, any of the output [1,0,2] or [1,2,0] or [0,1,2] or [0,2,1] or [2,0,1] or [2,1,0] will be accepted.
## Solutions:
```python
#include 
#include 
class BoundedBlockingQueue :
public:
    BoundedBlockingQueue(int capacity) :
        data.resize(capacity + 1)
        MOD = capacity + 1
    void enqueue(int element) :
        std::unique_lock lock(m)
        while (full()) hasSpace.wait(lock)
        data[tail++] = element
        tail = tail % MOD
        hasData.notify_all()
    int dequeue() :
        std::unique_lock lock(m)
        while (empty()) hasData.wait(lock)
        int val = data[head++]
        head = head % MOD
        hasSpace.notify_all()
        return val
    int size() :
        return (tail - head + MOD) % MOD
    bool empty() :
        return head == tail
    bool full() :
        return (tail + 1) % MOD == head
private:
    int MOD
    vector data
    int head = 0
    int tail = 0
    std::mutex m
    std::condition_variable hasSpace
    std::condition_variable hasData
```
# 860. Design Circular Queue
* *Difficulty: Medium*
* *Topics: Design, Queue*
* *Similar Questions:*
  * [Design Circular Deque](design-circular-deque.md)
## Problem:
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called &quotRing Buffer&quot.
One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
Your implementation should support following operations:
	MyCircularQueue(k): Constructor, set the size of the queue to be k.
	Front: Get the front item from the queue. If the queue is empty, return -1.
	Rear: Get the last item from the queue. If the queue is empty, return -1.
	enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
	deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
	isEmpty(): Checks whether the circular queue is empty or not.
	isFull(): Checks whether the circular queue is full or not.
Example:
MyCircularQueue circularQueue = new MyCircularQueue(3) // set the size to be 3
circularQueue.enQueue(1)  // return true
circularQueue.enQueue(2)  // return true
circularQueue.enQueue(3)  // return true
circularQueue.enQueue(4)  // return false, the queue is full
circularQueue.Rear()  // return 3
circularQueue.isFull()  // return true
circularQueue.deQueue()  // return true
circularQueue.enQueue(4)  // return true
circularQueue.Rear()  // return 4
Note:
	All values will be in the range of [0, 1000].
	The number of operations will be in the range of [1, 1000].
	Please do not use the built-in Queue library.
## Solutions:
```python
class MyCircularQueue :
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) :
        buffer.resize(k+1)
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) :
        if (isFull())   return false
        buffer[r] = value
        r = (r + 1) % buffer.size()
        return true
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() :
        if (isEmpty())  return false
        f = (f + 1) % buffer.size()
        return true
    /** Get the front item from the queue. */
    int Front() :
        if(isEmpty())   return -1
        return buffer[f]
    /** Get the last item from the queue. */
    int Rear() :
        if (isEmpty())  return -1
        if (r - 1 < 0)  return buffer.back()
        return buffer[r - 1]
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() :
        return f == r
    /** Checks whether the circular queue is full or not. */
    bool isFull() :
        return (r + 1) % buffer.size() == f
private:
    vector buffer
    int f = 0
    int r = 0
    int cap
/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k)
 * bool param_1 = obj->enQueue(value)
 * bool param_2 = obj->deQueue()
 * int param_3 = obj->Front()
 * int param_4 = obj->Rear()
 * bool param_5 = obj->isEmpty()
 * bool param_6 = obj->isFull()
 */
```
# 604. Design Compressed String Iterator
* *Difficulty: Easy*
* *Topics: Design*
* *Similar Questions:*
  * [LRU Cache](lru-cache.md)
  * [String Compression](string-compression.md)
## Problem:
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.
The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.
next() - if the original string still has uncompressed characters, return the next letter Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.
Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.
Example:
StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1")
iterator.next() // return 'L'
iterator.next() // return 'e'
iterator.next() // return 'e'
iterator.next() // return 't'
iterator.next() // return 'C'
iterator.next() // return 'o'
iterator.next() // return 'd'
iterator.hasNext() // return true
iterator.next() // return 'e'
iterator.hasNext() // return false
iterator.next() // return ' '
## Solutions:
```python
class StringIterator :
public:
    StringIterator(string compressedString) :
        str = compressedString
        index = 0
        count = 0
    char next() :
        if (!hasNext()) return ' '
        if (count > 0) :
            --count
            return c
        c = str[index++]
        count = 0
        while (index < str.length() && isdigit(str[index])) :
            count = 10 * count + (str[index++] - '0')
        --count
        return c
    bool hasNext() :
        return count > 0 || index < str.length()
private:
    string str
    int index
    char c
    int count
/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator* obj = new StringIterator(compressedString)
 * char param_1 = obj->next()
 * bool param_2 = obj->hasNext()
 */
```
# 362. Design Hit Counter
* *Difficulty: Medium*
* *Topics: Design*
* *Similar Questions:*
  * [Logger Rate Limiter](logger-rate-limiter.md)
## Problem:
Design a hit counter which counts the number of hits received in the past 5 minutes.
Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
It is possible that several hits arrive roughly at the same time.
Example:
HitCounter counter = new HitCounter()
// hit at timestamp 1.
counter.hit(1)
// hit at timestamp 2.
counter.hit(2)
// hit at timestamp 3.
counter.hit(3)
// get hits at timestamp 4, should return 3.
counter.getHits(4)
// hit at timestamp 300.
counter.hit(300)
// get hits at timestamp 300, should return 4.
counter.getHits(300)
// get hits at timestamp 301, should return 3.
counter.getHits(301) 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
## Solutions:
```python
class HitCounter :
public:
    /** Initialize your data structure here. */
    HitCounter() :
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) :
        log.push_back(timestamp)
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) :
        int start = timestamp - 299
        int end = timestamp
        auto lower = lower_bound(log.begin(), log.end(), start)
        auto upper = upper_bound(log.begin(), log.end(), end)
        return distance(lower, upper)
private:
    vector log
/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter()
 * obj->hit(timestamp)
 * int param_2 = obj->getHits(timestamp)
 */
```
# 588. Design In-Memory File System
* *Difficulty: Hard*
* *Topics: Design*
* *Similar Questions:*
  * [LRU Cache](lru-cache.md)
  * [LFU Cache](lfu-cache.md)
  * [Design Log Storage System](design-log-storage-system.md)
## Problem:
Design an in-memory file system to simulate the following functions:
ls: Given a path in string format. If it is a file path, return a list that only contains this file&#39s name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.
mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don&#39t exist either, you should create them as well. This function has void return type.
addContentToFile: Given a file path and file content in string format. If the file doesn&#39t exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.
readContentFromFile: Given a file path, return its content in string format.
Example:
Input: 
[&quotFileSystem&quot,&quotls&quot,&quotmkdir&quot,&quotaddContentToFile&quot,&quotls&quot,&quotreadContentFromFile&quot]
[[],[&quot/&quot],[&quot/a/b/c&quot],[&quot/a/b/c/d&quot,&quothello&quot],[&quot/&quot],[&quot/a/b/c/d&quot]]
Output:
[null,[],null,null,[&quota&quot],&quothello&quot]
Explanation:
Note:
	You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just &quot/&quot.
	You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
	You can assume that all directory names and file names only contain lower-case letters, and same names won&#39t exist in the same directory.
## Solutions:
```python
class FileSystem :
public:
    FileSystem() :
        root = new Directory("")
    vector ls(string path) :
        vector tokens = tokenize(path)
        Node* cur = root
        for (auto& token : tokens) :
            cur = cur->next[token]
        return cur->ls()
    void mkdir(string path) :
        vector tokens = tokenize(path)
        Node* cur = root
        for (auto& token : tokens) :
            if (cur->next.count(token) == 0) :
                cur->next[token] = new Directory(token)
            cur = cur->next[token]
    void addContentToFile(string filePath, string content) :
        vector tokens = tokenize(filePath)
        Node* cur = root
        for (auto& token : tokens) :
            if (cur->next.count(token) == 0) :
                cur->next[token] = new File(token)
            cur = cur->next[token]
        ((File*) cur)->append(content)
    string readContentFromFile(string filePath) :
        vector tokens = tokenize(filePath)
        Node* cur = root
        for (auto& token : tokens) :
            cur = cur->next[token]
        return ((File*) cur)->read()
private:
    class Node :
    public:
        Node(const string& name) :
            this->name = name
        string getName() :
            return name
        virtual bool isDirectory() = 0
        virtual vector ls() = 0 
        map next
    protected:
        string name
    class File : public Node :
    public:
        File(const string& name): Node(name) :
        bool isDirectory() override:
            return false
        vector ls() override :
            return :name
        void append(const string& str) :
            data.append(str)
        string read() :
            return data
    private:
        string data
    class Directory : public Node :
    public:
        Directory(const string& name): Node(name) :
        bool isDirectory() override :
            return true
        vector ls() override :
            vector ret
            for (auto it = next.begin() it != next.end() ++it) :
                ret.push_back(it->first)
            return ret
    private:
    vector tokenize(const string& path) :
        vector ret
        int pos = 1
        string token
        while (pos < path.length()) :
            if (path[pos] == '/') :
                ret.push_back(token)
                token.clear()
             else :
                token.push_back(path[pos])
            ++pos
        if (token.length() > 0) :
            ret.push_back(token)
        return ret
    Node* root
/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem()
 * vector param_1 = obj->ls(path)
 * obj->mkdir(path)
 * obj->addContentToFile(filePath,content)
 * string param_4 = obj->readContentFromFile(filePath)
 */
```
# 838. Design Linked List
* *Difficulty: Easy*
* *Topics: Linked List, Design*
* *Similar Questions:*
## Problem:
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
Implement these functions in your linked list class:
	get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
	addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
	addAtTail(val) : Append a node of value val to the last element of the linked list.
	addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. If index is negative, the node will be inserted at the head of the list.
	deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:
MyLinkedList linkedList = new MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)  // linked list becomes 1-&gt2-&gt3
linkedList.get(1)            // returns 2
linkedList.deleteAtIndex(1)  // now the linked list is 1-&gt3
linkedList.get(1)            // returns 3
Note:
	All values will be in the range of [1, 1000].
	The number of operations will be in the range of [1, 1000].
	Please do not use the built-in LinkedList library.
## Solutions:
```python
class MyLinkedList :
public:
    /** Initialize your data structure here. */
    MyLinkedList() :
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) :
        if (index < 0)  return -1
        Node* cur = head
        while (index >= 0) :
            cur = cur->next
            if (cur == nullptr) return -1
            --index
        return cur == head ? -1 : cur->val
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) :
        Node* node = new Node(val)
        node->next = head->next
        head->next = node
        if(node->next == nullptr) :
            tail = node
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) :
        tail->next = new Node(val)
        tail = tail->next
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) :
        if (index < 0) :
            addAtHead(val)
        Node* cur = head
        while (index > 0) :
            cur = cur->next
            --index
            if (cur == nullptr) return
        cur->next = new Node(val, cur->next)
        if (cur->next->next == nullptr) :
            tail = cur->next
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) :
        if (index < 0)  return
        Node* prev = head
        Node* cur = head->next
        while (index > 0) :
            if (cur == nullptr) return
            prev = cur
            cur = cur->next
            --index
        if (cur == nullptr) return
        prev->next = cur->next
        if (prev->next == nullptr) :
            tail = prev
private:
    struct Node:
        int val
        Node* next
        Node(int val, Node* next = nullptr) :
            this->val = val
            this->next = next
    Node* head = new Node(0)
    Node* tail = head
/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList()
 * int param_1 = obj->get(index)
 * obj->addAtHead(val)
 * obj->addAtTail(val)
 * obj->addAtIndex(index,val)
 * obj->deleteAtIndex(index)
 */
```
# 379. Design Phone Directory
* *Difficulty: Medium*
* *Topics: Linked List, Design*
* *Similar Questions:*
## Problem:
Design a Phone Directory which supports the following operations:
get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:
// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3)
// It can return any available phone number. Here we assume it returns 0.
directory.get()
// Assume it returns 1.
directory.get()
// The number 2 is available, so return true.
directory.check(2)
// It returns 2, the only number that is left.
directory.get()
// The number 2 is no longer available, so return false.
directory.check(2)
// Release number 2 back to the pool.
directory.release(2)
// Number 2 is available again, return true.
directory.check(2)
## Solutions:
```python
class PhoneDirectory :
public:
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    PhoneDirectory(int maxNumbers) :
        for (int i = 0 i < maxNumbers ++i) :
            phones.insert(i)
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    int get() :
        auto it = phones.begin() // constant time complexity
        if (it == phones.end()) :
            return -1
        int val = *it
        phones.erase(it)
        return val
    /** Check if a number is available or not. */
    bool check(int number) :
        return phones.count(number) > 0
    /** Recycle or release a number. */
    void release(int number) :
        phones.insert(number)
private:
    unordered_set phones
/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory* obj = new PhoneDirectory(maxNumbers)
 * int param_1 = obj->get()
 * bool param_2 = obj->check(number)
 * obj->release(number)
 */
```
# 348. Design Tic-Tac-Toe
* *Difficulty: Medium*
* *Topics: Design*
* *Similar Questions:*
  * [Valid Tic-Tac-Toe State](valid-tic-tac-toe-state.md)
## Problem:
Design a Tic-tac-toe game that is played between two players on a n x n grid.
You may assume the following rules:
A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
TicTacToe toe = new TicTacToe(3)
toe.move(0, 0, 1) -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |
toe.move(0, 2, 2) -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |
toe.move(2, 2, 1) -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|
toe.move(1, 1, 2) -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|
toe.move(2, 0, 1) -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|
toe.move(1, 0, 2) -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|
toe.move(2, 1, 1) -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
## Solutions:
```python
class TicTacToe :
public:
    /** Initialize your data structure here. */
    TicTacToe(int n) :
        this->n = n
        rowCount[0].resize(n)
        rowCount[1].resize(n)
        colCount[0].resize(n)
        colCount[1].resize(n)
    /** Player :player makes a move at (:row, :col).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) :
        if (++rowCount[player - 1][row] == n)   return player
        if (++colCount[player - 1][col] == n)   return player
        if (row == col) :
            if(++diagonalCount[player - 1] == n) return player
        if (row + col == n - 1) :
            if (++antiDiagonalCount[player - 1] == n)   return player
        return 0
private:
    int n
    vector rowCount[2]
    vector colCount[2]
    int diagonalCount[2] :0
    int antiDiagonalCount[2] :0
/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n)
 * int param_1 = obj->move(row,col,player)
 */
```
# 520. Detect Capital
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
	All letters in this word are capitals, like &quotUSA&quot.
	All letters in this word are not capitals, like &quotleetcode&quot.
	Only the first letter in this word is capital, like &quotGoogle&quot.
Otherwise, we define that this word doesn&#39t use capitals in a right way.
Example 1:
Input: &quotUSA&quot
Output: True
Example 2:
Input: &quotFlaG&quot
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
## Solutions:
```python
class Solution :
public:
    bool detectCapitalUse(string word) :
        if (word.length() == 1) return true
        if (islower(word[0]) && isupper(word[1]))   return false
        for (int i = 2 i < word.length() ++i) :
            if (!(isupper(word[i]) && isupper(word[i-1]) || islower(word[i]) && islower(word[i-1])))   return false
        return true
```
# 498. Diagonal Traverse
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:
Note:
The total number of elements of the given matrix will not exceed 10,000.
## Solutions:
```python
class Solution :
public:
    vector findDiagonalOrder(vector>& matrix) :
        int m = matrix.size()
        if (m == 0) return :
        int n = matrix[0].size()
        if (n == 0) return :
        vector ret
        int row = 0
        int col = 0
        int direction[2] = :-1, 1
        while (row < m && col < n) :
            ret.push_back(matrix[row][col])
            if (row + direction[0] >= 0 && row + direction[0] = 0 && col + direction[1] < n) :
                row = row + direction[0]
                col = col + direction[1]
             else :
                direction[0] = -direction[0]
                direction[1] = -direction[1]
                if (row == 0) :
                    ++col
                 else if (row == m - 1) :
                    ++col
                 else if (col == 0) :
                    ++row
                 else if (col == n - 1) :
                    ++row
                if (!(row>= 0 && row = 0 && col < n)) :
                    row = row + direction[0]
                    col = col + direction[1]
        return ret
```
# 543. Diameter of Binary Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
Note:
The length of path between two nodes is represented by the number of edges between them.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int diameterOfBinaryTree(TreeNode* root) :
        int depth
        return helper(root, depth)
private:
    int helper(TreeNode* root, int& depth) :
        if (root == nullptr) :
            depth = 0
            return 0
        int leftDepth, rightDepth
        int left = helper(root->left, leftDepth)
        int right = helper(root->right, rightDepth)
        depth = 1 + max(leftDepth, rightDepth)
        return max(max(left, right), leftDepth + rightDepth)
```
# 1280. Diet Plan Performance
* *Difficulty: Easy*
* *Topics: Array, Sliding Window*
* *Similar Questions:*
## Problem:
A dieter consumes calories[i] calories on the i-th day. 
Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 &lt= i &lt= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):
	If T &lt lower, they performed poorly on their diet and lose 1 point 
	If T &gt upper, they performed well on their diet and gain 1 point
	Otherwise, they performed normally and there is no change in points.
Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.
Note that the total points can be negative.
Example 1:
Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
Output: 0
Explanation: Since k = 1, we consider each element of the array separately and compare it to lower and upper.
calories[0] and calories[1] are less than lower so 2 points are lost.
calories[3] and calories[4] are greater than upper so 2 points are gained.
Example 2:
Input: calories = [3,2], k = 2, lower = 0, upper = 1
Output: 1
Explanation: Since k = 2, we consider subarrays of length 2.
calories[0] + calories[1] &gt upper so 1 point is gained.
Example 3:
Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
Output: 0
Explanation:
calories[0] + calories[1] &gt upper so 1 point is gained.
lower &lt= calories[1] + calories[2] &lt= upper so no change in points.
calories[2] + calories[3] &lt lower so 1 point is lost.
Constraints:
	1 &lt= k &lt= calories.length &lt= 10^5
	0 &lt= calories[i] &lt= 20000
	0 &lt= lower &lt= upper
## Solutions:
```python
class Solution :
public:
    int dietPlanPerformance(vector& calories, int k, int lower, int upper) :
        int calorie = 0
        int score = 0
        for (int i = 0 i < k - 1 ++i) :
            calorie += calories[i]
        for (int i = k - 1 i < calories.size() ++i) :
            calorie += calories[i]
            if (calorie < lower) :
                score -= 1
             else if (calorie > upper) :
                score += 1
            calorie -= calories[i - k + 1]
        return score
```
# 115. Distinct Subsequences
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, &quotACE&quot is a subsequence of &quotABCDE&quot while &quotAEC&quot is not).
Example 1:
Input: S = &quotrabbbit&quot, T = &quotrabbit&quot
Output: 3
Explanation:
As shown below, there are 3 ways you can generate &quotrabbit&quot from S.
(The caret symbol ^ means the chosen letters)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:
Input: S = &quotbabgbag&quot, T = &quotbag&quot
Output: 5
Explanation:
As shown below, there are 5 ways you can generate &quotbag&quot from S.
(The caret symbol ^ means the chosen letters)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
## Solutions:
```python
class Solution :
public:
    int numDistinct(string s, string t) :
        int sLen = s.length()
        int tLen = t.length()
        vector> dp(sLen + 1, vector (tLen + 1, 0))
        dp[0][0] = 1
        for (int i = 1 i <= sLen ++i) :
            dp[i][0] = 1
        for (int j = 1 j <= tLen ++j) :
            dp[0][j] = 0
        for (int i = 1 i <= sLen ++i) :
            for (int j = 1 j <=tLen ++j) :
                dp[i][j] = dp[i-1][j]
                if (s[i-1] == t[j-1]) :
                    dp[i][j] += dp[i-1][j-1]
        return dp[sLen][tLen]
```
# 575. Distribute Candies
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain. 
Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 
Note:
The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
## Solutions:
```python
class Solution :
public:
    int distributeCandies(vector& candies) :
        int kind = 0
        unordered_set kinds
        for (auto& candy : candies) :
            if (kinds.count(candy) == 0) :
                ++kind
                kinds.insert(candy)
        return min((int)candies.size() / 2, kind)
```
# 29. Divide Two Integers
* *Difficulty: Medium*
* *Topics: Math, Binary Search*
* *Similar Questions:*
## Problem:
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Note:
	Both dividend and divisor will be 32-bit signed integers.
	The divisor will never be 0.
	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus231,  231 &minus 1]. For the purpose of this problem, assume that your function returns 231 &minus 1 when the division result overflows.
## Solutions:
```python
class Solution :
public:
    int divide(int dividend, int divisor) :
        if (dividend == INT_MIN && divisor == -1)   return INT_MAX
        if (dividend == INT_MIN && divisor == 1)    return INT_MIN
        if (dividend == INT_MIN && divisor == INT_MIN)  return 1
        if (divisor == INT_MIN) :
            return 0
        int sign = 1
        if ((dividend >= 0 && divisor = 0)) :
            sign = -1
        divisor = abs(divisor)
        int carry = 0
        if (dividend == INT_MIN) :
            dividend += divisor
            carry = 1
        dividend = abs(dividend)
        int ret = 0
        while (dividend >= divisor) :
            int q = 1
            int d = divisor
            int half = dividend >> 1
            while (half >= d) :
                d <<= 1
                q <<= 1
            ret += q
            dividend -= d
        ret += carry // add carry because it is negative
        return ret * sign
```
# 174. Dungeon Game
* *Difficulty: Hard*
* *Topics: Binary Search, Dynamic Programming*
* *Similar Questions:*
  * [Unique Paths](unique-paths.md)
  * [Minimum Path Sum](minimum-path-sum.md)
  * [Cherry Pickup](cherry-pickup.md)
## Problem:
table.dungeon, .dungeon th, .dungeon td :
  border:3px solid black
 .dungeon th, .dungeon td :
    text-align: center
    height: 70px
    width: 70px
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms other rooms are either empty (0&#39s) or contain magic orbs that increase the knight&#39s health (positive integers).
In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
Write a function to determine the knight&#39s minimum initial health so that he is able to rescue the princess.
For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-&gt RIGHT -&gt DOWN -&gt DOWN.
			-2 (K)
			-3
			3
			-5
			-10
			1
			10
			30
			-5 (P)
Note:
	The knight&#39s health has no upper bound.
	Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
## Solutions:
```python
class Solution :
public:
    int calculateMinimumHP(vector>& dungeon) :
        int m = dungeon.size()
        if (m == 0) return 0
        int n = dungeon[0].size()
        if (n == 0) return 0
        vector> dp (m, vector (n, 0))
        //dp[m - 1][n - 1] = dungeon[m - 1][n - 1]
        for (int i = m - 1 i >= 0 --i) :
            for (int j = n - 1 j >= 0 --j) :
                if (i == m - 1 && j == n - 1) :
                    dp[i][j] = max(-dungeon[i][j], 0)
                    continue
                dp[i][j] = max(-dungeon[i][j] + min(i + 1 < m ? dp[i+1][j] : INT_MAX, j + 1 < n ? dp[i][j+1] : INT_MAX), 0)
        return dp[0][0] + 1
```
# 182. Duplicate Emails
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Write a SQL query to find all duplicate emails in a table named Person.
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.
## Solutions:
```python
# Write your MySQL query statement below
SELECT Email FROM
(SELECT Email, COUNT(Id) AS C
FROM Person
GROUP BY Email
 ) AS T
WHERE T.C > 1
```
# 72. Edit Distance
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
  * [One Edit Distance](one-edit-distance.md)
  * [Delete Operation for Two Strings](delete-operation-for-two-strings.md)
  * [Minimum ASCII Delete Sum for Two Strings](minimum-ascii-delete-sum-for-two-strings.md)
  * [Uncrossed Lines](uncrossed-lines.md)
## Problem:
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
	Insert a character
	Delete a character
	Replace a character
Example 1:
Input: word1 = &quothorse&quot, word2 = &quotros&quot
Output: 3
Explanation: 
horse -&gt rorse (replace &#39h&#39 with &#39r&#39)
rorse -&gt rose (remove &#39r&#39)
rose -&gt ros (remove &#39e&#39)
Example 2:
Input: word1 = &quotintention&quot, word2 = &quotexecution&quot
Output: 5
Explanation: 
intention -&gt inention (remove &#39t&#39)
inention -&gt enention (replace &#39i&#39 with &#39e&#39)
enention -&gt exention (replace &#39n&#39 with &#39x&#39)
exention -&gt exection (replace &#39n&#39 with &#39c&#39)
exection -&gt execution (insert &#39u&#39)
## Solutions:
```python
class Solution :
public:
    int minDistance(string word1, string word2) :
        int len1 = word1.length()
        int len2 = word2.length()
        vector> dp(1 + len1, vector (1 + len2, 0))
        for (int i = 0  i <= len1 ++i) :
            dp[i][0] = i
        for (int j = 0 j <= len2 ++j) :
            dp[0][j] = j
        for (int i = 1 i <= len1 ++i) :
            for (int j = 1 j <= len2 ++j) :
                if (word1[i-1] == word2[j-1]) :
                    dp[i][j] = dp[i-1][j-1]
                 else :
                    dp[i][j] = 1 + min(dp[i-1][j], min(dp[i][j-1],dp[i-1][j-1])) 
        return dp[len1][len2]
```
# 390. Elimination Game
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Find the last number that remains starting with a list of length n.
Example:
Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6
Output:
6
## Solutions:
```python
class Solution :
public:
    int lastRemaining(int n) :
        if (n == 1 || n == 2) return n 
        return ((1 + n/2) - lastRemaining(n/2)) * 2
```
# 761. Employee Free Time
* *Difficulty: Hard*
* *Topics: Heap, Greedy*
* *Similar Questions:*
  * [Merge Intervals](merge-intervals.md)
  * [Interval List Intersections](interval-list-intersections.md)
## Problem:
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren&#39t finite.
Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)
Also, we wouldn&#39t include intervals like [5, 5] in our answer, as they have zero length.
Note:
	schedule and schedule[i] are lists with lengths in range [1, 50].
	0 &lt= schedule[i].start &lt schedule[i].end &lt= 10^8.
NOTE: input types have been changed on June 17, 2019. Please reset to default code definition to get new method signature.
## Solutions:
```python
/*
// Definition for an Interval.
class Interval :
public:
    int start
    int end
    Interval() :
    Interval(int _start, int _end) :
        start = _start
        end = _end
*/
class Solution :
public:
    vector employeeFreeTime(vector> schedule) :
        priority_queue> pq
        for (int i = 0 i < schedule.size() ++i) :
            if (schedule[i].size() > 0) :
                pq.push(:schedule[i][0]->start, true, i, 0)
                pq.push(:schedule[i][0]->end, false, i, 0)
        vector ret
        int count = 0
        int start = -1
        while (!pq.empty()) :
            Node node = pq.top() pq.pop()
            if (!node.isStart && node.index + 1 < schedule[node.employee].size()) :
                pq.push(:schedule[node.employee][node.index + 1]->start, true, node.employee, node.index + 1)
                pq.push(:schedule[node.employee][node.index + 1]->end, false, node.employee, node.index + 1)
            if (node.isStart) :
                ++count
             else :
                --count
            if (node.isStart && count == 1 && start != -1) : // node.isStart check is important!
                ret.push_back(new Interval(start, node.timestamp))
                start = -1
             else if (!node.isStart && count == 0) :
                start = node.timestamp
        return ret
private:
    struct Node :
        int timestamp
        bool isStart
        int employee
        int index
        Node(int timestamp, bool isStart, int employee, int index) :
            this->timestamp = timestamp
            this->isStart = isStart
            this->employee = employee
            this->index = index
        bool operator< (const Node& rhs) const :
            if (timestamp != rhs.timestamp) :
                return timestamp > rhs.timestamp
            return !isStart
```
# 181. Employees Earning More Than Their Managers
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
+----------+
| Employee |
+----------+
| Joe      |
+----------+
## Solutions:
```python
# Write your MySQL query statement below
SELECT T1.Name AS Employee FROM Employee T1 JOIN Employee T2 ON T1.ManagerId = T2.Id WHERE T1.Salary > T2.Salary
```
# 271. Encode and Decode Strings
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
  * [Count and Say](count-and-say.md)
  * [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree.md)
  * [String Compression](string-compression.md)
  * [Count Binary Substrings](count-binary-substrings.md)
## Problem:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Machine 1 (sender) has the function:
string encode(vector&ltstring&gt strs) :
  // ... your code
  return encoded_string
Machine 2 (receiver) has the function:
vector&ltstring&gt decode(string s) :
  //... your code
  return strs
So Machine 1 does:
string encoded_string = encode(strs)
and Machine 2 does:
vector&ltstring&gt strs2 = decode(encoded_string)
strs2 in Machine 2 should be the same as strs in Machine 1.
Implement the encode and decode methods.
Note:
	The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
	Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
	Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
## Solutions:
```python
class Codec :
public:
    // Encodes a list of strings to a single string.
    string encode(vector& strs) :
        string serial
        int n = strs.size()
        serial.append(writeInt(n))
        for (int i = 0 i < n ++i) :
            serial.append(writeString(strs[i]))
        return serial
    // Decodes a single string to a list of strings.
    vector decode(string s) :
        vector strs
        const char* buf = s.c_str()
        int n = readInt(buf)
        for (int i = 0 i < n ++i) :
            strs.push_back(readString(buf))
        return strs
    static const int INT_SIZE = 4
    string writeString(string str) :
        int strLen = str.length()
        string serial
        serial.append(writeInt(strLen))
        char* buf = new char[strLen]
        memcpy(buf, str.c_str(), strLen)
        serial.append(string(buf, strLen))
        delete[] buf
        return serial
    string readString(const char*& buf) :
        int strLen = readInt(buf)
        string content(buf, strLen)
        buf += strLen
        return content
    string writeInt(int num) :
        char buf[INT_SIZE]
        memcpy(buf, (void*)(&num), INT_SIZE)
        return string(buf, INT_SIZE)
    int readInt(const char*& buf) :
        int num = 0
        memcpy((void*)(&num), buf, INT_SIZE)
        buf += INT_SIZE
        return num
```
# 771. Encode N-ary Tree to Binary Tree
* *Difficulty: Hard*
* *Topics: Tree*
* *Similar Questions:*
  * [Serialize and Deserialize N-ary Tree](serialize-and-deserialize-n-ary-tree.md)
## Problem:
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.
For example, you may encode the following 3-ary tree to a binary tree in this way:
Note that the above is just an example which might or might not work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note:
	N is in the range of  [1, 1000]
	Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val = NULL
    vector children
    Node() :
    Node(int _val, vector _children) :
        val = _val
        children = _children
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Codec :
public:
    // Encodes an n-ary tree to a binary tree.
    TreeNode* encode(Node* root) :
        if (root == nullptr)    return nullptr
        int val = root->val
        TreeNode* treeRoot = new TreeNode(val)
        if (root->children.empty()) return treeRoot
        treeRoot->left = encode(root->children[0])
        TreeNode* cur = treeRoot->left
        for (int i = 1 i children.size() ++i) :
            cur->right = encode(root->children[i])
            cur = cur->right
        return treeRoot
    // Decodes your binary tree to an n-ary tree.
    Node* decode(TreeNode* root) :
        if (root == nullptr)    return nullptr
        Node* nAryTreeRoot = new Node()
        nAryTreeRoot->val = root->val
        TreeNode* cur = root->left
        while (cur != nullptr) :
            nAryTreeRoot->children.push_back(decode(cur))
            cur = cur->right
        return nAryTreeRoot
// Your Codec object will be instantiated and called as such:
// Codec codec
// codec.decode(codec.encode(root))
```
# 399. Evaluate Division
* *Difficulty: Medium*
* *Topics: Union Find, Graph*
* *Similar Questions:*
## Problem:
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
Example:
Given  a / b = 2.0, b / c = 3.0.
queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
The input is:  vector&ltpair&ltstring, string&gt&gt equations, vector&ltdouble&gt&amp values, vector&ltpair&ltstring, string&gt&gt queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return  vector&ltdouble&gt.
According to the example above:
equations = [ [&quota&quot, &quotb&quot], [&quotb&quot, &quotc&quot] ],
values = [2.0, 3.0],
queries = [ [&quota&quot, &quotc&quot], [&quotb&quot, &quota&quot], [&quota&quot, &quote&quot], [&quota&quot, &quota&quot], [&quotx&quot, &quotx&quot] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
## Solutions:
```python
class Solution :
public:
    vector calcEquation(vector>& equations, vector& values, vector>& queries) :
        UF uf
        for (int i = 0 i < equations.size() ++i) :
            uf.connect(equations[i][0], equations[i][1], values[i])
        vector ret
        for (auto q : queries) :
            ret.push_back(uf.query(q[0], q[1]))
        return ret
private:
    class UF :
    public:
        pair find(string x) :
            if (parent.count(x) == 0) :
                parent[x] = :x, 1.0
            else if (x != parent[x].first) :
                auto root = find(parent[x].first)
                parent[x] = :root.first, root.second * parent[x].second
            return parent[x]
        // rootA = x / rootX.second = value * y / rootX.second
        // rootB = y / rootY.second
        void connect(string x, string y, double value) :
            auto rootX = find(x)
            auto rootY = find(y)
            if (rootX.first != rootY.first) :
                parent[rootX.first] = :rootY.first, value * rootY.second / rootX.second 
        double query(string x, string y) :
            if (parent.count(x) == 0 || parent.count(y) == 0)   return -1.0
            auto rootX = find(x)
            auto rootY = find(y)
            if (rootX.first != rootY.first) :
                return -1.0
            return rootX.second / rootY.second
    private:
        unordered_map> parent
```
# 150. Evaluate Reverse Polish Notation
* *Difficulty: Medium*
* *Topics: Stack*
* *Similar Questions:*
  * [Basic Calculator](basic-calculator.md)
  * [Expression Add Operators](expression-add-operators.md)
## Problem:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Note:
	Division between two integers should truncate toward zero.
	The given RPN expression is always valid. That means the expression would always evaluate to a result and there won&#39t be any divide by zero operation.
Example 1:
Input: [&quot2&quot, &quot1&quot, &quot+&quot, &quot3&quot, &quot*&quot]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:
Input: [&quot4&quot, &quot13&quot, &quot5&quot, &quot/&quot, &quot+&quot]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:
Input: [&quot10&quot, &quot6&quot, &quot9&quot, &quot3&quot, &quot+&quot, &quot-11&quot, &quot*&quot, &quot/&quot, &quot*&quot, &quot17&quot, &quot+&quot, &quot5&quot, &quot+&quot]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
## Solutions:
```python
class Solution :
public:
    int evalRPN(vector& tokens) :
        stack nums
        for (auto& token : tokens) :
            if (token == "+" || token == "-" || token == "*" || token == "/") :
                int op1 = nums.top() nums.pop()
                int op2 = nums.top() nums.pop()
                int ret
                switch(token[0]) :
                    case '+': 
                        ret = op1 + op2
                        break
                    case '-':
                        ret = op2 - op1 // take care of the order
                        break
                    case '*':
                        ret = op1 * op2
                        break
                    case '/':
                        ret = op2 / op1 // take care of the order
                        break
                nums.push(ret)
             else :
                nums.push(stoi(token))
        return nums.top()
```
# 171. Excel Sheet Column Number
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Excel Sheet Column Title](excel-sheet-column-title.md)
## Problem:
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -&gt 1
    B -&gt 2
    C -&gt 3
    ...
    Z -&gt 26
    AA -&gt 27
    AB -&gt 28 
    ...
Example 1:
Input: &quotA&quot
Output: 1
Example 2:
Input: &quotAB&quot
Output: 28
Example 3:
Input: &quotZY&quot
Output: 701
## Solutions:
```python
class Solution :
public:
    int titleToNumber(string s) :
        int ret = 0
        for (int i = 0 i < s.length() ++i) :
            ret = 26 * ret + (s[i] - 'A' + 1) // be careful about overflow
        return ret
```
# 168. Excel Sheet Column Title
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Excel Sheet Column Number](excel-sheet-column-number.md)
## Problem:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -&gt A
    2 -&gt B
    3 -&gt C
    ...
    26 -&gt Z
    27 -&gt AA
    28 -&gt AB 
    ...
Example 1:
Input: 1
Output: &quotA&quot
Example 2:
Input: 28
Output: &quotAB&quot
Example 3:
Input: 701
Output: &quotZY&quot
## Solutions:
```python
class Solution :
public:
    string convertToTitle(int n) :
        string ret
        while (n > 0) :
            ret.push_back( (n - 1) % 26 + 'A')
            n = (n - 1)/ 26
        reverse(ret.begin(), ret.end())
        return ret
```
# 254. Factor Combinations
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [Combination Sum](combination-sum.md)
## Problem:
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.
Note:
	You may assume that n is always positive.
	Factors should be greater than 1 and less than n.
Example 1: 
Input: 1
Output: []
Example 2: 
Input: 37
Output:[]
Example 3: 
Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4: 
Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
## Solutions:
```python
class Solution :
public:
    vector> getFactors(int n) :
        vector path
        vector> ret
        for (int i = 2 n / i >= i ++i) :
            if (n % i == 0) :
                path.push_back(i)
                helper(n/i, i, path, ret)
                path.pop_back()
        return ret
private:
    void helper(int n, int factor, vector& path, vector>& ret) :
        if (factor > n) return
        for (int i = factor i <= n / i ++i) :
            if (n % i == 0) :
                path.push_back(i)
                helper(n / i, i, path, ret)
                path.pop_back()
        path.push_back(n) // the number itself should be considered!
        ret.push_back(path)
        path.pop_back() // pop back!
```
# 172. Factorial Trailing Zeroes
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Number of Digit One](number-of-digit-one.md)
  * [Preimage Size of Factorial Zeroes Function](preimage-size-of-factorial-zeroes-function.md)
## Problem:
Given an integer n, return the number of trailing zeroes in n!.
Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
## Solutions:
```python
class Solution :
public:
    int trailingZeroes(int n) :
        int count = 0
        int divisor = 5
        while (n >= divisor) :
            count += n/divisor
            n /= 5 // be careful about overflow!
        return count
```
# 1013. Fibonacci Number
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Climbing Stairs](climbing-stairs.md)
  * [Split Array into Fibonacci Sequence](split-array-into-fibonacci-sequence.md)
  * [Length of Longest Fibonacci Subsequence](length-of-longest-fibonacci-subsequence.md)
  * [N-th Tribonacci Number](n-th-tribonacci-number.md)
## Problem:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N &gt 1.
Given N, calculate F(N).
Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
Note:
0 &le N &le 30.
## Solutions:
```python
class Solution :
public:
    int fib(int N) :
        if (N <= 1)  return N
        int prev1 = 0
        int prev2 = 1
        for (int i = 2 i <= N ++i) :
            int value = prev1 + prev2
            prev1 = prev2
            prev2 = value
        return prev2
```
# 442. Find All Duplicates in an Array
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Find All Numbers Disappeared in an Array](find-all-numbers-disappeared-in-an-array.md)
## Problem:
Given an array of integers, 1 &le a[i] &le n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
## Solutions:
```python
class Solution :
public:
    vector findDuplicates(vector& nums) :
        vector ret
        for (int i = 0 i < nums.size() ++i) :
            int kickOut = 0
            swap(kickOut, nums[i])
            while (kickOut != 0 && nums[kickOut - 1] != kickOut) :
                swap(kickOut, nums[kickOut - 1])
            if (kickOut != 0) :
                ret.push_back(kickOut)
        return ret
```
# 448. Find All Numbers Disappeared in an Array
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [First Missing Positive](first-missing-positive.md)
  * [Find All Duplicates in an Array](find-all-duplicates-in-an-array.md)
## Problem:
Given an array of integers where 1 &le a[i] &le n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
## Solutions:
```python
class Solution :
public:
    vector findDisappearedNumbers(vector& nums) :
        for (int i = 0 i < nums.size() ++i) :
            if (nums[i] == i + 1)   continue
            int kickout = nums[i]
            nums[i] = 0
            while (kickout != 0 && nums[kickout-1] != kickout) :
                swap(kickout, nums[kickout-1])
        vector ret
        for (int i = 0 i < nums.size() ++i) :
            if (nums[i] != i + 1) :
                ret.push_back(i + 1)
        return ret
```
# 1044. Find Common Characters
* *Difficulty: Easy*
* *Topics: Array, Hash Table*
* *Similar Questions:*
  * [Intersection of Two Arrays II](intersection-of-two-arrays-ii.md)
## Problem:
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
Example 1:
Input: [&quotbella&quot,&quotlabel&quot,&quotroller&quot]
Output: [&quote&quot,&quotl&quot,&quotl&quot]
Example 2:
Input: [&quotcool&quot,&quotlock&quot,&quotcook&quot]
Output: [&quotc&quot,&quoto&quot]
Note:
	1 &lt= A.length &lt= 100
	1 &lt= A[i].length &lt= 100
	A[i][j] is a lowercase letter
## Solutions:
```python
class Solution :
public:
    vector commonChars(vector& A) :
        if (A.size() == 0)  return :
        vector common = countFreq(A[0])
        for (int i = 1 i < A.size() ++i) :
            vector freq = countFreq(A[i])
            for (int j = 0 j < 26 ++j) :
                common[j] = min(common[j], freq[j])
        vector ret
        for (int i = 0 i < 26 ++i) :
            for (int j = 0 j < common[i] ++j) :
                ret.push_back(string(1, 'a' + i))
        return ret  
private:
    vector countFreq(const string& str) :
        vector freq(26, 0)
        for (auto& c : str) :
            ++freq[c - 'a']
        return freq
```
# 34. Find First and Last Position of Element in Sorted Array
* *Difficulty: Medium*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [First Bad Version](first-bad-version.md)
## Problem:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm&#39s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
## Solutions:
```python
bool searchLeft(vector& nums, int index, int target) :
    return nums[index] >= target
bool searchRight(vector& nums, int index, int target) :
    return nums[index] > target || index == nums.size() - 1 || (nums[index] == target && nums[index + 1] > target)
class Solution :
public:
    typedef bool (*check) (vector&, int, int)
    vector searchRange(vector& nums, int target) :
        if (nums.size() == 0)   return :-1, -1
        int leftBound = search(nums, 0, nums.size() - 1, target, &searchLeft)
        int rightBound = search(nums, 0, nums.size() - 1, target, &searchRight)
        return :nums[leftBound] == target ? leftBound : - 1, nums[rightBound] == target ? rightBound : - 1
    int search(vector& nums, int left, int right, int target, check fn) :
        while (left < right) :
            int mid = left + (right - left) /2 
            if ((*fn) (nums, mid, target)) :
                right = mid
             else :
                left = mid + 1
        return left
```
# 658. Find K Closest Elements
* *Difficulty: Medium*
* *Topics: Binary Search*
* *Similar Questions:*
  * [Guess Number Higher or Lower](guess-number-higher-or-lower.md)
  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)
  * [Find K-th Smallest Pair Distance](find-k-th-smallest-pair-distance.md)
## Problem:
Given a sorted array, two integers k and x, find the k closest elements to x in the array.  The result should also be sorted in ascending order.
If there is a tie,  the smaller elements are always preferred.
Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
 Length of the given array is positive and will not exceed 104
 Absolute value of elements in the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
## Solutions:
```python
class Solution :
public:
    vector findClosestElements(vector& arr, int k, int x) :
        int startIndex = findClosest(arr, x)
        if (startIndex < 0) startIndex = 0
        if (k == 0) return :
        vector ret
        int forward, backward
        if (arr[startIndex] == x) :
            ret.push_back(arr[startIndex])
            --k
            forward = startIndex + 1
            backward = startIndex - 1
         else if (arr[startIndex] > x):
            forward = startIndex
            backward = startIndex - 1
         else :
            forward = startIndex + 1
            backward = startIndex
        while (k > 0) :
            if (forward >= arr.size()) :
                ret.push_back(arr[backward--])
                --k
             else if (backward < 0) :
                ret.push_back(arr[forward++])
                --k
             else :
                int forwardDis = abs(arr[forward] - x)
                int backDis = abs(arr[backward] -x)
                if (forwardDis == backDis) :
                    ret.push_back(arr[backward--])
                    --k
                 else if (forwardDis < backDis) :
                    ret.push_back(arr[forward++])
                    --k
                 else :
                    ret.push_back(arr[backward--])
                    --k
        sort(ret.begin(), ret.end()) // we could construct result from two limits and just return a sublist.
        return ret
    int findClosest(vector& arr, int target) :
        int left = 0
        int right = arr.size() - 1
        while (left < right) :
            int mid = left + (right - left) / 2
            if (arr[mid] == target) return mid
            else if (arr[mid] < target) :
                left = mid + 1
             else :
                right = mid - 1
        return left
```
# 366. Find Leaves of Binary Tree
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
## Problem:
Given a binary tree, collect a tree&#39s nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
Example:
Input: [1,2,3,4,5]
          1
         / \
        2   3
       / \     
      4   5    
Output: [[4,5,3],[2],[1]]
Explanation:
1. Removing the leaves [4,5,3] would result in this tree:
          1
         / 
        2          
2. Now removing the leaf [2] would result in this tree:
          1          
3. Now removing the leaf [1] would result in the empty tree:
          []         
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector> findLeaves(TreeNode* root) :
        vector> ret
        visit(root, ret)
        return ret
private:
    int visit(TreeNode* root, vector>& ret) :
        if (root == nullptr)    return -1
        int leftDepth = visit(root->left, ret)
        int rightDepth = visit(root->right, ret)
        int rootDepth = 1 + max(leftDepth, rightDepth)
        if (ret.size() == rootDepth) :
            ret.push_back(:)
        ret[rootDepth].push_back(root->val)
        return rootDepth
```
# 295. Find Median from Data Stream
* *Difficulty: Hard*
* *Topics: Heap, Design*
* *Similar Questions:*
  * [Sliding Window Median](sliding-window-median.md)
## Problem:
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
	void addNum(int num) - Add a integer number from the data stream to the data structure.
	double findMedian() - Return the median of all elements so far.
Example:
addNum(1)
addNum(2)
findMedian() -&gt 1.5
addNum(3) 
findMedian() -&gt 2
Follow up:
	If all integer numbers from the stream are between 0 and 100, how would you optimize it?
	If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
## Solutions:
```python
class MedianFinder :
public:
    /** initialize your data structure here. */
    MedianFinder() :
    void addNum(int num) :
        v2.insert(num)
        if (v2.size() - v1.size() > 1) :
            auto it = v2.begin()
            v1.insert(*it)
            v2.erase(it)
        if (v1.size() > 0 && *v1.rbegin() > *v2.begin()) :
            int val1 = *v1.rbegin()
            int val2 = *v2.begin()
            v1.erase(--v1.end())
            v2.erase(v2.begin())
            v1.insert(val2)
            v2.insert(val1)
    double findMedian() :
        return v2.size() > v1.size() ? *v2.begin() : ((double) *v1.rbegin() + (double) *v2.begin()) / 2
private:
    multiset v1
    multiset v2
/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder()
 * obj->addNum(num)
 * double param_2 = obj->findMedian()
 */
```
# 153. Find Minimum in Rotated Sorted Array
* *Difficulty: Medium*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [Search in Rotated Sorted Array](search-in-rotated-sorted-array.md)
  * [Find Minimum in Rotated Sorted Array II](find-minimum-in-rotated-sorted-array-ii.md)
## Problem:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.
Example 1:
Input: [3,4,5,1,2] 
Output: 1
Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
## Solutions:
```python
class Solution :
public:
    typedef bool (*check)(vector&, int index)
    static bool checkMin(vector& nums, int index) :
        return nums[index] < nums[0]
    int findMin(vector& nums) :
        if (nums.size() == 0)   return -1
        if (nums.size() == 1)   return nums[0]
        if (nums[0] < nums.back())  return nums[0]
        int left = 0
        int right = nums.size() - 1
        while (left < right) :
            int mid = left + (right - left)/2
            if (checkMin(nums, mid)) :
                right = mid
             else :
                left = mid + 1
        return nums[left]
```
# 501. Find Mode in Binary Search Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Validate Binary Search Tree](validate-binary-search-tree.md)
## Problem:
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
	The left subtree of a node contains only nodes with keys less than or equal to the node&#39s key.
	The right subtree of a node contains only nodes with keys greater than or equal to the node&#39s key.
	Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].
Note: If a tree has more than one mode, you can return them in any order.
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector findMode(TreeNode* root) :
        if (root == nullptr)    return :
        int count = 0
        vector ret
        int lastVal = 0
        int largest = 0
        helper(root, lastVal, count, ret, largest)
        if (count > largest) :
            ret.clear()
            ret.push_back(lastVal)
         else if (count == largest) :
            ret.push_back(lastVal)
        return ret
private:
    void helper(TreeNode* root, int& lastVal, int& count, vector& ret, int& largest) :
        if (root == nullptr)    return
        helper(root->left, lastVal, count, ret, largest)
        if (root->val == lastVal) :
            ++count
         else :
            if (count > 0) :
                if (count > largest) :
                    ret.clear()
                    ret.push_back(lastVal)
                    largest = count
                 else if (count == largest) :
                    ret.push_back(lastVal)
            count = 1
        lastVal = root->val
        helper(root->right, lastVal, count, ret, largest)
```
# 162. Find Peak Element
* *Difficulty: Medium*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [Peak Index in a Mountain Array](peak-index-in-a-mountain-array.md)
## Problem:
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] &ne nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -&infin.
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:
Your solution should be in logarithmic complexity.
## Solutions:
```python
class Solution :
public:
    int findPeakElement(vector& nums) : // this problem does not eliminate the scenario [1]
        int left = 0
        int right = nums.size() - 1
        while (left + 1 < right) :
            int mid = left + (right - left)/2
            if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid + 1])   return mid
            if (nums[mid] < nums[mid - 1]) right = mid
            else left = mid
        if (left == 0) :
            if (nums.size() > left + 1 && nums[left + 1] < nums[left])   return left
            else return right
         else :
            if (nums.size() > left + 1 && left -1 >= 0 && nums[left] > nums[left - 1] && nums[left] > nums[left + 1]) return left
            else return right
```
# 724. Find Pivot Index
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Subarray Sum Equals K](subarray-sum-equals-k.md)
## Problem:
Given an array of integers nums, write a method that returns the &quotpivot&quot index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
Note:
	The length of nums will be in the range [0, 10000].
	Each element nums[i] will be an integer in the range [-1000, 1000].
## Solutions:
```python
class Solution :
public:
    int pivotIndex(vector& nums) :
        int sum = accumulate(nums.begin(), nums.end(), 0)
        int runningSum = 0
        for (int i = 0 i < nums.size() ++i) :
            if (runningSum == sum - runningSum - nums[i])  return i
            runningSum += nums[i]
        return -1
```
# 1143. Find Smallest Common Element in All Rows
* *Difficulty: Medium*
* *Topics: Hash Table, Binary Search*
* *Similar Questions:*
## Problem:
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.
If there is no common element, return -1.
Example 1:
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
Constraints:
	1 &lt= mat.length, mat[i].length &lt= 500
	1 &lt= mat[i][j] &lt= 10^4
	mat[i] is sorted in increasing order.
## Solutions:
```python
class Solution :
public:
    int smallestCommonElement(vector>& mat) :
        int m = mat.size()
        if (m == 0) return -1
        int n = mat[0].size()
        if (n == 0) return -1
        for (auto& num : mat[0]) :
            bool found = true
            for (int i = 1 i < m ++i) :
                if (find(mat[i].begin(), mat[i].end(), num) == mat[i].end()) :
                    found = false
                    break
            if (found) return num
        return -1
```
# 745. Find Smallest Letter Greater Than Target
* *Difficulty: Easy*
* *Topics: Binary Search*
* *Similar Questions:*
## Problem:
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
Letters also wrap around.  For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"
Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"
Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"
Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"
Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"
Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
## Solutions:
```python
class Solution :
public:
    char nextGreatestLetter(vector& letters, char target) :
        auto it = upper_bound(letters.begin(), letters.end(), target)
        return it == letters.end() ? letters[0] : *it
```
# 277. Find the Celebrity
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Find the Town Judge](find-the-town-judge.md)
## Problem:
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: &quotHi, A. Do you know B?&quot to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity&#39s label if there is a celebrity in the party. If there is no celebrity, return -1.
Example 1:
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.
Note:
	The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
	Remember that you won&#39t have direct access to the adjacency matrix.
## Solutions:
```python
// Forward declaration of the knows API.
bool knows(int a, int b)
class Solution :
public:
    int findCelebrity(int n) :
        return findCandidate(n)
private:
    int findCandidate(int n) :
        unordered_set candidates
        for (int i = 0 i < n ++i) :
            candidates.insert(i)
        while (!candidates.empty()) :
            auto it = candidates.begin()
            if (checkCelebrity(n, *it)) return *it
            candidates.erase(it)
        return -1
    bool checkCelebrity(int n, int c) :
        for (int i = 0 i < n ++i) :
            if (i == c) continue
            if (knows(c, i) || !knows(i, c))    return false
        return true
```
# 389. Find the Difference
* *Difficulty: Easy*
* *Topics: Hash Table, Bit Manipulation*
* *Similar Questions:*
  * [Single Number](single-number.md)
## Problem:
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.
Example:
Input:
s = "abcd"
t = "abcde"
Output:
e
Explanation:
'e' is the letter that was added.
## Solutions:
```python
class Solution :
public:
    char findTheDifference(string s, string t) :
        char ret = 0
        for (auto c : s) :
            ret ^= c
        for (auto c : t) :
            ret ^= c
        return ret
```
# 1112. Find Words That Can Be Formed by Characters
* *Difficulty: Easy*
* *Topics: Array, Hash Table*
* *Similar Questions:*
## Problem:
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
Example 1:
Input: words = [&quotcat&quot,&quotbt&quot,&quothat&quot,&quottree&quot], chars = &quotatach&quot
Output: 6
Explanation: 
The strings that can be formed are &quotcat&quot and &quothat&quot so the answer is 3 + 3 = 6.
Example 2:
Input: words = [&quothello&quot,&quotworld&quot,&quotleetcode&quot], chars = &quotwelldonehoneyr&quot
Output: 10
Explanation: 
The strings that can be formed are &quothello&quot and &quotworld&quot so the answer is 5 + 5 = 10.
Note:
	1 &lt= words.length &lt= 1000
	1 &lt= words[i].length, chars.length &lt= 100
	All strings contain lowercase English letters only.
## Solutions:
```python
class Solution :
public:
    int countCharacters(vector& words, string chars) :
        unordered_map charCount
        for (auto c : chars) :
            ++charCount[c]
        int ret = 0
        for (auto& word : words) :
            if (valid(word, charCount)) :
                ret += word.length()
        return ret
private:
    bool valid(string& word, unordered_map charCount) :
        for (auto c : word) :
            if ((--charCount[c]) < 0 )  return false
        return true
```
# 278. First Bad Version
* *Difficulty: Easy*
* *Topics: Binary Search*
* *Similar Questions:*
  * [Find First and Last Position of Element in Sorted Array](find-first-and-last-position-of-element-in-sorted-array.md)
  * [Search Insert Position](search-insert-position.md)
  * [Guess Number Higher or Lower](guess-number-higher-or-lower.md)
## Problem:
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
Example:
Given n = 5, and version = 4 is the first bad version.
call isBadVersion(3) -&gt false
call isBadVersion(5) -&gt true
call isBadVersion(4) -&gt true
Then 4 is the first bad version. 
## Solutions:
```python
// Forward declaration of isBadVersion API.
bool isBadVersion(int version)
class Solution :
public:
    int firstBadVersion(int n) :
        int left = 1
        int right = n
        while (left + 1 < right) :
            int mid = left + (right - left)/2
            if (isBadVersion(mid)) :
                right = mid
             else :
                left = mid // not mid + 1 otherwise overflow
        if (isBadVersion(left))    return left
        return right
```
# 41. First Missing Positive
* *Difficulty: Hard*
* *Topics: Array*
* *Similar Questions:*
  * [Missing Number](missing-number.md)
  * [Find the Duplicate Number](find-the-duplicate-number.md)
  * [Find All Numbers Disappeared in an Array](find-all-numbers-disappeared-in-an-array.md)
  * [Couples Holding Hands](couples-holding-hands.md)
## Problem:
Given an unsorted integer array, find the smallest missing positive integer.
Example 1:
Input: [1,2,0]
Output: 3
Example 2:
Input: [3,4,-1,1]
Output: 2
Example 3:
Input: [7,8,9,11,12]
Output: 1
Note:
Your algorithm should run in O(n) time and uses constant extra space.
## Solutions:
```python
class Solution :
public:
    int firstMissingPositive(vector& nums) :
        int n = nums.size()
        for (int i = 0 i < n ++i) :
            int pendingVal = nums[i]
            nums[i] = -1
            while (pendingVal >= 1 && pendingVal <= n && nums[pendingVal - 1] != pendingVal) :
                swap(pendingVal, nums[pendingVal - 1])
        for (int i = 1 i <= n ++i) :
            if (nums[i-1] != i) return i
        return n+1
```
#### More concise solution
From [Grandyang] (https://www.cnblogs.com/grandyang/p/4395963.html) 
```python
class Solution :
public:
    int firstMissingPositive(vector& nums) :
        int n = nums.size()
        for (int i = 0 i < n ++i) :
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) :
                swap(nums[i], nums[nums[i] - 1])
        for (int i = 0 i < n ++i) :
            if (nums[i] != i + 1) return i + 1
        return n + 1
```
# 387. First Unique Character in a String
* *Difficulty: Easy*
* *Topics: Hash Table, String*
* *Similar Questions:*
  * [Sort Characters By Frequency](sort-characters-by-frequency.md)
## Problem:
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
## Solutions:
```python
class Solution :
public:
    int firstUniqChar(string s) :
        int count[26] = :0
        for (int i = 0 i < s.length() ++i) :
            ++count[s[i] - 'a']
        for (int i = 0 i < s.length() ++i) :
            if (count[s[i] - 'a'] == 1) return i
        return -1
```
# 412. Fizz Buzz
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
## Solutions:
```python
class Solution :
public:
    vector fizzBuzz(int n) :
        vector ret
        for (int i = 1 i <= n ++i) :
            if (i % 15 == 0) :
                ret.push_back("FizzBuzz")
             else if (i % 3 == 0) :
                ret.push_back("Fizz")
             else if (i % 5 == 0) :
                ret.push_back("Buzz")
             else :
                ret.push_back(to_string(i))
        return ret
```
# 251. Flatten 2D Vector
* *Difficulty: Medium*
* *Topics: Design*
* *Similar Questions:*
  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)
  * [Zigzag Iterator](zigzag-iterator.md)
  * [Peeking Iterator](peeking-iterator.md)
  * [Flatten Nested List Iterator](flatten-nested-list-iterator.md)
## Problem:
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.
Example:
Vector2D iterator = new Vector2D([[1,2],[3],[4]])
iterator.next() // return 1
iterator.next() // return 2
iterator.next() // return 3
iterator.hasNext() // return true
iterator.hasNext() // return true
iterator.next() // return 4
iterator.hasNext() // return false
Notes:
	Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
	You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
## Solutions:
```python
class Vector2D :
public:
    Vector2D(vector>& v) :
        this->v = v
        i = 0
        j = 0
    int next() :
        hasNext()
        int val = v[i][j]
        step()
        return val
    bool hasNext() :
        while (i < v.size() && !valid()) : // two conditions!
           step()
        return i < v.size()
    bool valid() :
        return i < v.size() && j < v[i].size()
    void step() :
        if (++j >= v[i].size()) :
            ++i
            j = 0
private:
    vector> v
    int i
    int j
/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D* obj = new Vector2D(v)
 * int param_1 = obj->next()
 * bool param_2 = obj->hasNext()
 */
```
# 114. Flatten Binary Tree to Linked List
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Flatten a Multilevel Doubly Linked List](flatten-a-multilevel-doubly-linked-list.md)
## Problem:
Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    void flatten(TreeNode* root) :
        TreeNode* dummyHead = new TreeNode(0)
        preorder(root, dummyHead)
    void preorder(TreeNode* root, TreeNode*& tail) :
        if (root == NULL)   return
        TreeNode* left = root->left
        TreeNode* right = root->right
        tail->right = root
        tail = tail->right
        root->left = NULL
        preorder(left, tail)
        preorder(right, tail)
```
# 341. Flatten Nested List Iterator
* *Difficulty: Medium*
* *Topics: Stack, Design*
* *Similar Questions:*
  * [Flatten 2D Vector](flatten-2d-vector.md)
  * [Zigzag Iterator](zigzag-iterator.md)
  * [Mini Parser](mini-parser.md)
  * [Array Nesting](array-nesting.md)
## Problem:
Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Example 1:
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
## Solutions:
```python
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger :
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector &getList() const
 * 
 */
class NestedIterator :
public:
    NestedIterator(vector &nestedList) :
        for (int i = 0 i < nestedList.size() ++i) :
            stk.push(nestedList[nestedList.size() - 1 - i])
    int next() :
        int val = stk.top().getInteger()
        stk.pop()
        return val
    bool hasNext() :
        while (!stk.empty()) :
            if (stk.top().isInteger()) :
                return true
             else :
                auto nestedList = stk.top().getList() stk.pop()
                for (int i = 0 i < nestedList.size() ++i) :
                    stk.push(nestedList[nestedList.size() - 1 - i])
        return false
private:
    stack stk
    int buffer
/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList)
 * while (i.hasNext()) cout << i.next()
 */
```
# 294. Flip Game II
* *Difficulty: Medium*
* *Topics: Backtracking, Minimax*
* *Similar Questions:*
  * [Nim Game](nim-game.md)
  * [Flip Game](flip-game.md)
  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)
  * [Can I Win](can-i-win.md)
## Problem:
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive &quot++&quot into &quot--&quot. The game ends when a person can no longer make a move and therefore the other person will be the winner.
Write a function to determine if the starting player can guarantee a win.
Example:
Input: s = &quot++++&quot
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle &quot++&quot to become &quot+--+&quot.
Follow up:
Derive your algorithm&#39s runtime complexity.
## Solutions:
```python
class Solution :
public:
    bool canWin(string s) :
        unordered_map cache
        return helper(s, cache)
private:
    bool helper(string& s, unordered_map& cache) :
        if (cache.count(s) > 0) return cache[s]
        for (int i = 0 i < (int)s.length() - 1 ++i) :
            if (s[i] == '+' && s[i+1] == '+') :
                s[i] = '-'
                s[i+1] = '-'
                auto ret =  (!helper(s, cache))
                s[i + 1] = '+'
                s[i] = '+'
                if (ret == true) : // it is wrong to return result intermediately without set s back!
                    cache[s] = ret
                    return true
        cache[s] = false
        return false
```
# 293. Flip Game
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Flip Game II](flip-game-ii.md)
## Problem:
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive &quot++&quot into &quot--&quot. The game ends when a person can no longer make a move and therefore the other person will be the winner.
Write a function to compute all possible states of the string after one valid move.
Example:
Input: s = &quot++++&quot
Output: 
[
  &quot--++&quot,
  &quot+--+&quot,
  &quot++--&quot
]
Note: If there is no valid move, return an empty list [].
## Solutions:
```python
class Solution :
public:
    vector generatePossibleNextMoves(string s) :
        vector ret
        for (int i = 0 i < int(s.length() - 1)  ++i) : // caution!!!!
            if (s[i] == '+' && s[i + 1] == '+') :
                s[i] = '-'
                s[i + 1] = '-'
                ret.push_back(s)
                s[i + 1] = '+'
                s[i] = '+'
        return ret
```
# 733. Flood Fill
* *Difficulty: Easy*
* *Topics: Depth-first Search*
* *Similar Questions:*
  * [Island Perimeter](island-perimeter.md)
## Problem:
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.  Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.
Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0  and 0 .
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
## Solutions:
```python
class Solution :
public:
    vector> floodFill(vector>& image, int sr, int sc, int newColor) :
        int m = image.size()
        if (m == 0) return :
        int n = image[0].size()
        if (n == 0) return :
        if (sr = m || sc = n) return :
        if (image[sr][sc] == newColor)  return image
        helper(image, sr, sc, m, n, image[sr][sc], newColor)
        return image
    void helper(vector>& image, int sr, int sc, int m, int n, int color, int newColor) :
        image[sr][sc] = newColor
        if (sr + 1 < m && image[sr + 1][sc] == color)   helper(image, sr + 1, sc, m, n, color, newColor)
        if (sr - 1 >= 0 && image[sr - 1][sc] == color)  helper(image, sr - 1, sc, m, n, color, newColor)
        if (sc + 1 < n && image[sr][sc + 1] == color)   helper(image, sr, sc + 1, m, n, color, newColor)
        if (sc - 1 >= 0 && image[sr][sc - 1] == color)  helper(image, sr, sc - 1, m, n, color, newColor)
```
# 166. Fraction to Recurring Decimal
* *Difficulty: Medium*
* *Topics: Hash Table, Math*
* *Similar Questions:*
## Problem:
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
Example 1:
Input: numerator = 1, denominator = 2
Output: &quot0.5&quot
Example 2:
Input: numerator = 2, denominator = 1
Output: &quot2&quot
Example 3:
Input: numerator = 2, denominator = 3
Output: &quot0.(6)&quot
## Solutions:
```python
class Solution :
public:
    string fractionToDecimal(int n, int d) :
        int sign = 1
        if (((n >> 31) & 1) != ((d >> 31) & 1))  sign = -1
        long numerator = n
        long denominator = d
        numerator = abs(numerator)
        denominator = abs(denominator)
        long integral = numerator / denominator // integral should be of type long
        numerator = numerator % denominator
        string fractional
        computeFraction(numerator * 10, denominator, fractional)
        string ret
        if (numerator == 0 && integral == 0)    return "0" // this is essential
        if (sign == -1) :
            ret.push_back('-')
        ret.append(to_string(integral))
        if (numerator == 0) return ret
        ret.push_back('.')
        ret.append(fractional)
        return ret
    void computeFraction(long numerator, long denominator, string& fractional) :
        vector digits
        unordered_map indices
        while (numerator != 0) :
            if (indices.count(numerator)) :
                int unRepeatingIndex = indices[numerator]
                for (int i = 0 i < unRepeatingIndex ++i) :
                    fractional.push_back('0' + digits[i])
                fractional.push_back('(')
                for (int i = unRepeatingIndex i < digits.size() ++i) :
                    fractional.push_back('0' + digits[i])
                fractional.push_back(')')
                return
            int q = numerator / denominator
            digits.push_back(q)
            indices[numerator] = digits.size() - 1
            numerator = (numerator % denominator) * 10
        for (int i = 0 i < digits.size() ++i) :
            fractional.push_back('0' + digits[i])
```
# 597. Friend Requests I: Overall Acceptance Rate
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
In social network like Facebook or Twitter, people send friend requests and accept others&rsquo requests as well. Now given two tables as below:
Table: friend_request
| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016_06-01 |
| 1         | 3          | 2016_06-01 |
| 1         | 4          | 2016_06-01 |
| 2         | 3          | 2016_06-02 |
| 3         | 4          | 2016-06-09 |
Table: request_accepted
| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |
Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.
For the sample data above, your query should return the following result.
|accept_rate|
|-----------|
|       0.80|
Note:
	The accepted requests are not necessarily from the table friend_request. In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
	It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the &lsquoduplicated&rsquo requests or acceptances are only counted once.
	If there is no requests at all, you should return 0.00 as the accept_rate.
Explanation: There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.
Follow-up:
	Can you write a query to return the accept rate but for every month?
	How about the cumulative accept rate for every day?
## Solutions:
```python
# Write your MySQL query statement below
select
round(
ifnull(
(select count(*) from
(select distinct requester_id, accepter_id 
from request_accepted) as a)/
(select count(*) from
(select distinct sender_id, send_to_id 
from friend_request) as b),0)
,2) 
as accept_rate
```
# 403. Frog Jump
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
## Problem:
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.
If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
Note:
The number of stones is &ge 2 and is 
Each stone's position will be a non-negative integer 31.
The first stone's position is always 0.
Example 1:
[0,1,3,5,6,8,12,17]
There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.
Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:
[0,1,2,3,4,8,9,11]
Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
## Solutions:
```python
class Solution :
public:
    bool canCross(vector& stones) :
        map, bool> cache
        unordered_set stoneSet(stones.begin(), stones.end())
        return helper(stoneSet, 0, 0, stones.back(), cache) // start speed is 0
private:
    bool helper(unordered_set& stones, int position, int speed, int last, map, bool>& cache) :
        if (cache.count(:position, speed) > 0) return cache[:position, speed]
        if (position == last)   return true
        for (int jump = speed - 1 jump <= speed + 1 ++jump) :
            if (jump > 0 && stones.count(position + jump) > 0) :
                if (helper(stones, position + jump, jump, last, cache)) :
                    cache[:position, speed] = true
                    return true
        cache[:position, speed] = false
        return false
```
# 289. Game of Life
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Set Matrix Zeroes](set-matrix-zeroes.md)
## Problem:
According to the Wikipedia&#39s article: &quotThe Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.&quot
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
	Any live cell with fewer than two live neighbors dies, as if caused by under-population.
	Any live cell with two or three live neighbors lives on to the next generation.
	Any live cell with more than three live neighbors dies, as if by over-population..
	Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:
	Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
	In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
## Solutions:
```python
class Solution :
public:
    void gameOfLife(vector>& board) :
        int m = board.size()
        if (m == 0) return
        int n = board[0].size()
        if (n == 0) return
        for (int row = 0 row < m ++row) :
            for (int col = 0 col < n ++col) :
                int count = 0
                for (int i = -1 i <= 1 ++i) :
                    for (int j = -1 j <= 1 ++j) :
                        if (i == 0 && j == 0)   continue
                        if (row + i = m || col + j = n) continue
                        count += (board[row+i][col+j] & 0x1)
                if (board[row][col] & 0x1 == 1) : // live
                    if (count >= 2 && count <= 3) :
                        board[row][col] |= (0x1 << 1)
                 else : // dead
                    if (count == 3) :
                        board[row][col] |= (0x1 << 1)
        for (int row = 0 row < m ++row) :
            for (int col = 0 col < n ++col) :
                board[row][col] = board[row][col] >> 1
```
# 134. Gas Station
* *Difficulty: Medium*
* *Topics: Greedy*
* *Similar Questions:*
## Problem:
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station&#39s index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
Note:
	If there exists a solution, it is guaranteed to be unique.
	Both input arrays are non-empty and have the same length.
	Each element in the input arrays is a non-negative integer.
Example 1:
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:
Input: 
gas  = [2,3,4]
cost = [3,4,3]
Output: -1
Explanation:
You can&#39t start at station 0 or 1, as there is not enough gas to travel to the next station.
Let&#39s start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can&#39t travel around the circuit once no matter where you start.
## Solutions:
```python
class Solution :
public:
    int canCompleteCircuit(vector& gas, vector& cost) :
        int n = gas.size()
        int total = 0
        int start = 0
        int acc = 0
        for (int i = 0 i < n ++i) :
            total += gas[i] - cost[i]
            acc += gas[i] - cost[i]
            if (acc < 0) :
                acc = 0
                start = i + 1
        if (total < 0)  return -1
        return start
```
# 320. Generalized Abbreviation
* *Difficulty: Medium*
* *Topics: Backtracking, Bit Manipulation*
* *Similar Questions:*
  * [Subsets](subsets.md)
  * [Unique Word Abbreviation](unique-word-abbreviation.md)
  * [Minimum Unique Word Abbreviation](minimum-unique-word-abbreviation.md)
## Problem:
Write a function to generate the generalized abbreviations of a word. 
Note: The order of the output does not matter.
Example:
Input: &quotword&quot
Output:
[&quotword&quot, &quot1ord&quot, &quotw1rd&quot, &quotwo1d&quot, &quotwor1&quot, &quot2rd&quot, &quotw2d&quot, &quotwo2&quot, &quot1o1d&quot, &quot1or1&quot, &quotw1r1&quot, &quot1o2&quot, &quot2r1&quot, &quot3d&quot, &quotw3&quot, &quot4&quot]
## Solutions:
```python
class Solution :
public:
    vector generateAbbreviations(string word) :
        vector ret
        for (int i = 0 i < (1 << word.size()) ++i) :
            string abbr
            int count = 0
            for (int j = 0 j < word.size() ++j) :
                if ((1 << j) & i) ++count
                else :
                    if (count != 0) :
                        abbr.append(to_string(count))
                        count = 0
                    abbr.push_back(word[j])
            if (count != 0) :
                abbr.append(to_string(count))
            ret.push_back(abbr)
        return ret
```
# 22. Generate Parentheses
* *Difficulty: Medium*
* *Topics: String, Backtracking*
* *Similar Questions:*
  * [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number.md)
  * [Valid Parentheses](valid-parentheses.md)
## Problem:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
## Solutions:
```python
class Solution :
public:
    vector generateParenthesis(int n) :
        vector ret
        if (n == 0) return ret
        string path
        helper(2 * n, 0, path, ret)
        return ret
    void helper(int remain, int left, string& path, vector& ret) :
        if (remain == 0 && left == 0) :
            ret.push_back(path)
            return
        if (left < 0) :
            return
        if (remain < left) :
            return
        path.push_back('(')
        helper(remain - 1, left + 1, path, ret)
        path.pop_back()
        path.push_back(')')
        helper(remain - 1, left - 1, path, ret)
        path.pop_back()
```
#### More intuitive solution
From [Huahua](https://zxi.mytechroad.com/blog/searching/leetcode-22-generate-parentheses/)
```python
// Author: Huahua
// Running time: 0 ms
class Solution :
public:
  vector generateParenthesis(int n) :
    vector ans
    string cur
    if (n > 0) dfs(n, n, cur, ans)
    return ans
private:
  void dfs(int l, int r, string& s, vector& ans) :
    if (l + r == 0) :
      ans.push_back(s)
      return
    if (r < l) return
    if (l > 0) :
      dfs(l - 1, r, s += "(", ans)
      s.pop_back()
    if (r > 0) :
      dfs(l, r - 1, s += ")", ans)
      s.pop_back()
```
# 1321. Get Equal Substrings Within Budget
* *Difficulty: Medium*
* *Topics: Array, Sliding Window*
* *Similar Questions:*
## Problem:
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.
You are also given an integer maxCost.
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.
If there is no substring from s that can be changed to its corresponding substring from t, return 0.
Example 1:
Input: s = &quotabcd&quot, t = &quotbcdf&quot, maxCost = 3
Output: 3
Explanation: &quotabc&quot of s can change to &quotbcd&quot. That costs 3, so the maximum length is 3.
Example 2:
Input: s = &quotabcd&quot, t = &quotcdef&quot, maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.
Example 3:
Input: s = &quotabcd&quot, t = &quotacde&quot, maxCost = 0
Output: 1
Explanation: You can&#39t make any change, so the maximum length is 1.
Constraints:
	1 &lt= s.length, t.length &lt= 10^5
	0 &lt= maxCost &lt= 10^6
	s and t only contain lower case English letters.
## Solutions:
```python
class Solution :
public:
    int equalSubstring(string s, string t, int maxCost) :
        int len = 0
        int cost = 0
        if (maxCost < 0)    return 0
        int left = 0
        for (int right = 0 right < s.length() ++right) :
            cost += abs(t[right] - s[right])
            while (cost > maxCost) :
                cost -= abs(t[left] - s[left])
                ++left
            len = max(len, right - left + 1)
        return len
```
# 261. Graph Valid Tree
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search, Union Find, Graph*
* *Similar Questions:*
  * [Course Schedule](course-schedule.md)
  * [Number of Connected Components in an Undirected Graph](number-of-connected-components-in-an-undirected-graph.md)
## Problem:
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
## Solutions:
```python
class Solution :
public:
    bool validTree(int n, vector>& edges) :
        vector> graph (n)
        for (auto& edge : edges) :
            graph[edge[0]].push_back(edge[1])
            graph[edge[1]].push_back(edge[0])
        int edgeNum = edges.size()
        if (edgeNum != n - 1)   return false
        vector visited(n, false)
        int nodeCount = getConnectedNode(0, graph, visited)
        return nodeCount == n
    int getConnectedNode(int start, vector>& graph, vector& visited) :
        if (visited[start]) return 0
        int count = 1
        visited[start] = true
        for (auto& neighbor : graph[start]) :
            count += getConnectedNode(neighbor, graph, visited)
        return count
```
# 89. Gray Code
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [1-bit and 2-bit Characters](1-bit-and-2-bit-characters.md)
## Problem:
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
Example 1:
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1
Example 2:
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
## Solutions:
```python
class Solution :
public:
    vector grayCode(int n) :
        if (n < 0)  return :
        vector ret = :0
        for (int i = 0 i < n ++i) :
            int size = ret.size()
            for (int j = size - 1 j >= 0 --j) :
                ret.push_back(ret[j] + (1 << i))
        return ret
```
# 49. Group Anagrams
* *Difficulty: Medium*
* *Topics: Hash Table, String*
* *Similar Questions:*
  * [Valid Anagram](valid-anagram.md)
  * [Group Shifted Strings](group-shifted-strings.md)
## Problem:
Given an array of strings, group anagrams together.
Example:
Input: [&quoteat&quot, &quottea&quot, &quottan&quot, &quotate&quot, &quotnat&quot, &quotbat&quot],
Output:
[
  [&quotate&quot,&quoteat&quot,&quottea&quot],
  [&quotnat&quot,&quottan&quot],
  [&quotbat&quot]
]
Note:
	All inputs will be in lowercase.
	The order of your output does not matter.
## Solutions:
```python
class Solution :
public:
    vector> groupAnagrams(vector& strs) :
        unordered_map> anagrams
        for (auto& str : strs) :
            string anagram = str
            sort(anagram.begin(), anagram.end())
            anagrams[anagram].push_back(str)
        vector> ret
        for (auto it = anagrams.begin() it != anagrams.end() ++it) :
            ret.push_back(it->second)
        return ret
```
# 249. Group Shifted Strings
* *Difficulty: Medium*
* *Topics: Hash Table, String*
* *Similar Questions:*
  * [Group Anagrams](group-anagrams.md)
## Problem:
Given a string, we can &quotshift&quot each of its letter to its successive letter, for example: &quotabc&quot -&gt &quotbcd&quot. We can keep &quotshifting&quot which forms the sequence:
&quotabc&quot -&gt &quotbcd&quot -&gt ... -&gt &quotxyz&quot
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
Example:
Input: [&quotabc&quot, &quotbcd&quot, &quotacef&quot, &quotxyz&quot, &quotaz&quot, &quotba&quot, &quota&quot, &quotz&quot],
Output: 
[
  [&quotabc&quot,&quotbcd&quot,&quotxyz&quot],
  [&quotaz&quot,&quotba&quot],
  [&quotacef&quot],
  [&quota&quot,&quotz&quot]
]
## Solutions:
```python
class Solution :
public:
    vector> groupStrings(vector& strings) :
        unordered_map> groups
        for (auto& s : strings) :
            string shift = s
            int diff = s[0] - 'a'
            for (int i = 0 i < shift.length() ++i) :
                shift[i] -= diff
                if (shift[i] < 'a') :
                    shift[i] += 26
            groups[shift].push_back(s)
        vector> ret
        for (auto& entry : groups) :
            ret.push_back(entry.second)
        return ret
```
# 375. Guess Number Higher or Lower II
* *Difficulty: Medium*
* *Topics: Dynamic Programming, Minimax*
* *Similar Questions:*
  * [Flip Game II](flip-game-ii.md)
  * [Guess Number Higher or Lower](guess-number-higher-or-lower.md)
  * [Can I Win](can-i-win.md)
  * [Find K Closest Elements](find-k-closest-elements.md)
## Problem:
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I&#39ll tell you whether the number I picked is higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.
Example:
n = 10, I pick 8.
First round:  You guess 5, I tell you that it&#39s higher. You pay $5.
Second round: You guess 7, I tell you that it&#39s higher. You pay $7.
Third round:  You guess 9, I tell you that it&#39s lower. You pay $9.
Game over. 8 is the number I picked.
You end up paying $5 + $7 + $9 = $21.
Given a particular n &ge 1, find out how much money you need to have to guarantee a win.
## Solutions:
```python
class Solution :
public:
    int getMoneyAmount(int n) :
        if (n <= 0)  return 0
        vector> dp(n + 1, vector (n + 1, 0))
        for (int i = 1 i < n ++i) :
            dp[i][i+1] = i
        for (int l = 3 l <= n ++l) :
            for (int i = 1 i <= n - l + 1 ++i) :
                dp[i][i + l - 1] = INT_MAX
                for (int mid = i + 1 mid <= i + l - 2 ++mid) :
                    dp[i][i + l - 1] = min(dp[i][i + l -1], max(dp[i][mid - 1], dp[mid+1][i + l - 1]) + mid)
        return dp[1][n]
```
# 374. Guess Number Higher or Lower
* *Difficulty: Easy*
* *Topics: Binary Search*
* *Similar Questions:*
  * [First Bad Version](first-bad-version.md)
  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)
  * [Find K Closest Elements](find-k-closest-elements.md)
## Problem:
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I&#39ll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :
Input: n = 10, pick = 6
Output: 6
## Solutions:
```python
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num)
class Solution :
public:
    int guessNumber(int n) :
        int left = 1
        int right = n
        while (left < right) :
            int mid = left + (right - left) / 2
            int ret = guess(mid)
            if (ret == 0)   return mid
            else if (ret == 1) :
                left = mid + 1
             else :
                right = mid - 1
        return left
```
# 275. H-Index II
* *Difficulty: Medium*
* *Topics: Binary Search*
* *Similar Questions:*
  * [H-Index](h-index.md)
## Problem:
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher&#39s h-index.
According to the definition of h-index on Wikipedia: &quotA scientist has index h if h of his/her N papers have at least h citations each, and the other N &minus h papers have no more than h citations each.&quot
Example:
Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:
If there are several possible values for h, the maximum one is taken as the h-index.
Follow up:
	This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
	Could you solve it in logarithmic time complexity?
## Solutions:
```python
class Solution :
public:
    int hIndex(vector& citations) :
        int left = 0 
        int right = citations.size() // not size - 1
        while (left < right) :
            int mid = right - (right - left) / 2
            if (check(citations, mid)) :
                left = mid
             else :
                right = mid - 1
        return left
private:
    bool check(vector& citations, int h) :
        if (h == 0) return true
        int n = citations.size()
        return citations[n - h] >= h
```
# 274. H-Index
* *Difficulty: Medium*
* *Topics: Hash Table, Sort*
* *Similar Questions:*
  * [H-Index II](h-index-ii.md)
## Problem:
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher&#39s h-index.
According to the definition of h-index on Wikipedia: &quotA scientist has index h if h of his/her N papers have at least h citations each, and the other N &minus h papers have no more than h citations each.&quot
Example:
Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
## Solutions:
```python
class Solution :
public:
    int hIndex(vector& citations) :
        sort(citations.begin(), citations.end())
        int left = 0 
        int right = citations.size() // not size - 1
        while (left < right) :
            int mid = right - (right - left) / 2
            if (check(citations, mid)) :
                left = mid
             else :
                right = mid - 1
        return left
private:
    bool check(vector& citations, int h) :
        if (h == 0) return true
        int n = citations.size()
        return citations[n - h] >= h
```
# 461. Hamming Distance
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Number of 1 Bits](number-of-1-bits.md)
  * [Total Hamming Distance](total-hamming-distance.md)
## Problem:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 &le x, y &lt 231.
Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       &uarr   &uarr
The above arrows point to positions where the corresponding bits are different.
## Solutions:
```python
class Solution :
public:
    int hammingDistance(int x, int y) :
        int diff = x ^ y
        int count = 0
        while (diff) :
            diff &= diff - 1
            ++count
        return count
```
# 202. Happy Number
* *Difficulty: Easy*
* *Topics: Hash Table, Math*
* *Similar Questions:*
  * [Linked List Cycle](linked-list-cycle.md)
  * [Add Digits](add-digits.md)
  * [Ugly Number](ugly-number.md)
## Problem:
Write an algorithm to determine if a number is &quothappy&quot.
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
## Solutions:
```python
class Solution :
public:
    bool isHappy(int n) :
        if (n <= 0) return false
        if (n == 1) return true
        unordered_set seen
        int nextVal = 0
        for () :
            nextVal = 0 // reset nextVal
            while (n > 0) :
                nextVal += (n%10) * (n%10)
                n /= 10
            if (nextVal == 1) return true
            if (seen.count(nextVal) > 0)    return false
            seen.insert(nextVal)
            n = nextVal
```
# 475. Heaters
* *Difficulty: Easy*
* *Topics: Binary Search*
* *Similar Questions:*
## Problem:
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.
Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.
Note:
	Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
	Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
	As long as a house is in the heaters&#39 warm radius range, it can be warmed.
	All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
## Solutions:
```python
class Solution :
public:
    int findRadius(vector& houses, vector& heaters) :
        int left = 0
        int right = INT_MAX
        sort(heaters.begin(), heaters.end())
        while (left < right) :
            int mid = left + (right - left) / 2
            if (valid(houses, heaters, mid)) :
                right = mid
             else :
                left = mid + 1
        return left
private:
    bool valid(vector& houses, vector& heaters, int radius) :
        for (auto& house : houses) :
            int left = house - radius
            int right = house + radius
            if (distance(lower_bound(heaters.begin(), heaters.end(), left), upper_bound(heaters.begin(), heaters.end(), right)) < 1)    return false
        return true
```
# 1074. High Five
* *Difficulty: Easy*
* *Topics: Array, Hash Table, Sort*
* *Similar Questions:*
## Problem:
Given a list of scores of different students, return the average score of each student&#39s top five scores in the order of each student&#39s id.
Each entry items[i] has items[i][0] the student&#39s id, and items[i][1] the student&#39s score.  The average score is calculated using integer division.
Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
Note:
	1 &lt= items.length &lt= 1000
	items[i].length == 2
	The IDs of the students is between 1 to 1000
	The score of the students is between 1 to 100
	For each student, there are at least 5 scores
## Solutions:
```python
class Solution :
public:
    vector> highFive(vector>& items) :
        map, greater>> studentToScores
        for (auto& item : items) :
            int id = item[0]
            int score = item[1]
            studentToScores[id].push(score)
            if (studentToScores[id].size() > 5) :
                studentToScores[id].pop()
        vector> ret
        for (auto& entry : studentToScores) :
            int sum = 0
            for (int i = 0 i < 5 ++i) :
                sum += entry.second.top() entry.second.pop()
            ret.push_back(:entry.first, sum/5)
        return ret
```
# 213. House Robber II
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [House Robber](house-robber.md)
  * [Paint House](paint-house.md)
  * [Paint Fence](paint-fence.md)
  * [House Robber III](house-robber-iii.md)
  * [Non-negative Integers without Consecutive Ones](non-negative-integers-without-consecutive-ones.md)
  * [Coin Path](coin-path.md)
## Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Example 1:
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
## Solutions:
```python
class Solution :
public:
    int rob(vector& nums) :
        int n = nums.size()
        if (nums.size() == 0 )  return 0
        if (nums.size() == 1)   return nums[0] // this case is very important. Think about [1]
        int maxValue = 0
        vector dp(n + 1, 0)
        dp[0] = 0
        dp[1] = nums[0]
        for (int i = 2 i <= n - 1 ++i) :
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        maxValue = max(maxValue, dp[n-1])
        dp[1] = 0
        for (int i = 2 i <= n ++i) :
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        maxValue = max(maxValue, dp[n])
        return maxValue
```
# 337. House Robber III
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [House Robber](house-robber.md)
  * [House Robber II](house-robber-ii.md)
## Problem:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the &quotroot.&quot Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that &quotall houses in this place forms a binary tree&quot. It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
Example 1:
Input: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1
Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
Input: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \ 
 1   3   1
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int rob(TreeNode* root) :
        return rob(root, true)
private:
    int rob(TreeNode* root, bool couldRob) :
        if (root == nullptr)    return 0
        if (cache.count(:root, couldRob)) :
            return cache[:root, couldRob]
        int robRoot = 0
        if (couldRob) :
            robRoot = root->val + rob(root->left, false) + rob(root->right, false)
        int notRobRoot = 0
        notRobRoot = rob(root->left, true) +  rob(root->right, true)
        cache[:root, couldRob] = max(robRoot, notRobRoot)
        return max(robRoot, notRobRoot)
    map, int> cache
```
# 198. House Robber
* *Difficulty: Easy*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Maximum Product Subarray](maximum-product-subarray.md)
  * [House Robber II](house-robber-ii.md)
  * [Paint House](paint-house.md)
  * [Paint Fence](paint-fence.md)
  * [House Robber III](house-robber-iii.md)
  * [Non-negative Integers without Consecutive Ones](non-negative-integers-without-consecutive-ones.md)
  * [Coin Path](coin-path.md)
  * [Delete and Earn](delete-and-earn.md)
## Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
## Solutions:
```python
class Solution :
public:
    int rob(vector& nums) :
        int n = nums.size()
        if (n == 0) return 0
        if (n == 1) return nums[0]
        vector dp(n, 0)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for (int i = 2 i < n ++i) :
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]
```
# 1141. How Many Apples Can You Put into the Basket
* *Difficulty: Easy*
* *Topics: Greedy*
* *Similar Questions:*
## Problem:
You have some apples, where arr[i] is the weight of the i-th apple.  You also have a basket that can carry up to 5000 units of weight.
Return the maximum number of apples you can put in the basket.
Example 1:
Input: arr = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.
Example 2:
Input: arr = [900,950,800,1000,700,800]
Output: 5
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.
Constraints:
	1 &lt= arr.length &lt= 10^3
	1 &lt= arr[i] &lt= 10^3
## Solutions:
```python
class Solution :
public:
    int maxNumberOfApples(vector& arr) :
        sort(arr.begin(), arr.end())
        int weight = 0
        for (int i = 0 i < arr.size() ++i) :
            weight += arr[i]
            if (weight > 5000)  return i
        return arr.size()
```
# 661. Image Smoother
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.  If a cell has less than 8 surrounding cells, then use as many as you can.
Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
## Solutions:
```python
class Solution :
public:
    vector> imageSmoother(vector>& M) :
        int m = M.size()
        if (m == 0) return :
        int n = M[0].size()
        if (n == 0) return :
        vector> ret (m, vector (n, 0))
        for (int x = 0 x < m ++x) :
            for (int y = 0 y < n ++y) :
                int count = 0
                int gray = 0
                for (int dx = -1 dx <= 1 ++dx) :
                    for (int dy = -1 dy <= 1 ++dy) :
                        if (x + dx = m || y + dy = n) continue
                        ++count
                        gray += M[x+dx][y+dy]
                ret[x][y] = gray / count
        return ret
```
# 232. Implement Queue using Stacks
* *Difficulty: Easy*
* *Topics: Stack, Design*
* *Similar Questions:*
  * [Implement Stack using Queues](implement-stack-using-queues.md)
## Problem:
Implement the following operations of a queue using stacks.
	push(x) -- Push element x to the back of queue.
	pop() -- Removes the element from in front of queue.
	peek() -- Get the front element.
	empty() -- Return whether the queue is empty.
Example:
MyQueue queue = new MyQueue()
queue.push(1)
queue.push(2)  
queue.peek()  // returns 1
queue.pop()   // returns 1
queue.empty() // returns false
Notes:
	You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
	Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
	You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
## Solutions:
```python
class MyQueue :
public:
    /** Initialize your data structure here. */
    MyQueue() :
    /** Push element x to the back of queue. */
    void push(int x) :
        stk1.push(x)
    /** Removes the element from in front of queue and returns that element. */
    int pop() :
        flip()
        int val = stk2.top()
        stk2.pop()
        return val
    /** Get the front element. */
    int peek() :
        flip()
        return stk2.top()
    /** Returns whether the queue is empty. */
    bool empty() :
        flip()
        return stk2.empty()
private:
    void flip() :
        if (stk2.empty()) :
            while (!stk1.empty()) :
                int val = stk1.top() stk1.pop()
                stk2.push(val)
    stack stk1
    stack stk2
/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue()
 * obj->push(x)
 * int param_2 = obj->pop()
 * int param_3 = obj->peek()
 * bool param_4 = obj->empty()
 */
```
# 225. Implement Stack using Queues
* *Difficulty: Easy*
* *Topics: Stack, Design*
* *Similar Questions:*
  * [Implement Queue using Stacks](implement-queue-using-stacks.md)
## Problem:
Implement the following operations of a stack using queues.
	push(x) -- Push element x onto stack.
	pop() -- Removes the element on top of the stack.
	top() -- Get the top element.
	empty() -- Return whether the stack is empty.
Example:
MyStack stack = new MyStack()
stack.push(1)
stack.push(2)  
stack.top()   // returns 2
stack.pop()   // returns 2
stack.empty() // returns false
Notes:
	You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
	Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
	You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
## Solutions:
```python
class MyStack :
public:
    /** Initialize your data structure here. */
    MyStack() :
    /** Push element x onto stack. */
    void push(int x) :
        q2.push(x)
        while (!q1.empty()) :
            q2.push(q1.front())
            q1.pop()
        swap(q1, q2)
    /** Removes the element on top of the stack and returns that element. */
    int pop() :
        int val = top()
        q1.pop()
        return val
    /** Get the top element. */
    int top() :
        return q1.front()
    /** Returns whether the stack is empty. */
    bool empty() :
        return q1.empty()   
private:
    queue q1
    queue q2 
/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack()
 * obj->push(x)
 * int param_2 = obj->pop()
 * int param_3 = obj->top()
 * bool param_4 = obj->empty()
 */
```
# 28. Implement strStr()
* *Difficulty: Easy*
* *Topics: Two Pointers, String*
* *Similar Questions:*
  * [Shortest Palindrome](shortest-palindrome.md)
  * [Repeated Substring Pattern](repeated-substring-pattern.md)
## Problem:
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = &quothello&quot, needle = &quotll&quot
Output: 2
Example 2:
Input: haystack = &quotaaaaa&quot, needle = &quotbba&quot
Output: -1
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C&#39s strstr() and Java&#39s indexOf().
## Solutions:
```python
class Solution :
public:
    int strStr(string haystack, string needle) :
        if (haystack.length() < needle.length())    return -1
        if (needle.length() == 0)   return 0
        const unsigned int MOD = 10000 
        const unsigned int MUL = 10
        unsigned int needleHash = 0
        for (auto c : needle) :
            needleHash = (needleHash * MUL + c - 'a' + 1) % MOD
        unsigned int haystackHash = 0
        for (int i = 0 i < needle.length() ++i) :
            haystackHash = (haystackHash * MUL + haystack[i] - 'a' + 1) % MOD
        unsigned int highHash = 1
        for (int i = 0 i < needle.length() - 1 ++i) : // be careful! what if needle size is 0
            highHash = (highHash * MUL) % MOD
        for (int i = 0 i < haystack.length() - needle.length() + 1 ++i) :
            if (needleHash == haystackHash && isEqual(haystack, i, needle)) return i
            if (i == haystack.length() - needle.length()) return -1
            haystackHash = ((haystackHash + MOD - highHash * (haystack[i] - 'a' + 1) % MOD ) % MOD * MUL + haystack[i+needle.length()] - 'a' + 1) % MOD // WARNING: don't overflow
        return -1
    bool isEqual(const string& haystack, int start, const string& needle) :
        for (int i = 0 i < 0 + needle.length() ++i) :
            if (haystack[i + start] != needle[i])   return false
        return true
```
# 208. Implement Trie (Prefix Tree)
* *Difficulty: Medium*
* *Topics: Design, Trie*
* *Similar Questions:*
  * [Add and Search Word - Data structure design](add-and-search-word-data-structure-design.md)
  * [Design Search Autocomplete System](design-search-autocomplete-system.md)
  * [Replace Words](replace-words.md)
  * [Implement Magic Dictionary](implement-magic-dictionary.md)
## Problem:
Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie()
trie.insert(&quotapple&quot)
trie.search(&quotapple&quot)   // returns true
trie.search(&quotapp&quot)     // returns false
trie.startsWith(&quotapp&quot) // returns true
trie.insert(&quotapp&quot)   
trie.search(&quotapp&quot)     // returns true
Note:
	You may assume that all inputs are consist of lowercase letters a-z.
	All inputs are guaranteed to be non-empty strings.
## Solutions:
```python
class Trie :
public:
    struct TrieNode:
        bool isWord
        TrieNode* next[26]
        TrieNode(bool isWord = false) :
            this->isWord = isWord
            for (int i = 0 i < 26 ++i) :
                next[i] = nullptr
    /** Initialize your data structure here. */
    Trie() :
        root = new TrieNode(false)
    /** Inserts a word into the trie. */
    void insert(string word) :
        TrieNode* lastNode = findNode(word, true)
        lastNode->isWord = true
    /** Returns if the word is in the trie. */
    bool search(string word) :
        TrieNode* lastNode = findNode(word, false)
        return lastNode != nullptr && lastNode->isWord
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) :
        return findNode(prefix, false) != nullptr
private:
    TrieNode* findNode(string& word, bool modifiable) :
        TrieNode* cur = root
        for (auto& c : word) :
            if (cur->next[c - 'a'] == nullptr) :
                if (!modifiable)    return nullptr
                cur->next[c -'a'] = new TrieNode(false)
            cur = cur->next[c - 'a']
        return cur
    TrieNode* root  
/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie()
 * obj->insert(word)
 * bool param_2 = obj->search(word)
 * bool param_3 = obj->startsWith(prefix)
 */
```
# 334. Increasing Triplet Subsequence
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
  * [Longest Increasing Subsequence](longest-increasing-subsequence.md)
## Problem:
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
Formally the function should:
Return true if there exists i, j, k 
such that arr[i] &lt arr[j] &lt arr[k] given 0 &le i &lt j &lt k &le n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
Example 1:
Input: [1,2,3,4,5]
Output: true
Example 2:
Input: [5,4,3,2,1]
Output: false
## Solutions:
```python
class Solution :
public:
    bool increasingTriplet(vector& nums) :
        int smallest = INT_MAX
        int secondSmallest = INT_MAX
        for (auto num : nums) :
            if (num <= smallest) :
                smallest = num // it is important that secondSmallest is not updated!
             else if (num <= secondSmallest) :
                secondSmallest = num
             else :
                return true
        return false
```
# 285. Inorder Successor in BST
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)
  * [Inorder Successor in BST II](inorder-successor-in-bst-ii.md)
## Problem:
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.
Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1&#39s in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Note:
	If the given node has no in-order successor in the tree, return null.
	It&#39s guaranteed that the values of the tree are unique.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) :
        if (root == NULL || p == NULL)  return NULL
        if (root->val val) :
            return inorderSuccessor(root->right, p)
         else :
            TreeNode* ret = inorderSuccessor(root->left, p)
            return ret == NULL ? root : ret
```
# 380. Insert Delete GetRandom O(1)
* *Difficulty: Medium*
* *Topics: Array, Hash Table, Design*
* *Similar Questions:*
  * [Insert Delete GetRandom O(1) - Duplicates allowed](insert-delete-getrandom-o1-duplicates-allowed.md)
## Problem:
Design a data structure that supports all following operations in average O(1) time.
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet()
// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1)
// Returns false as 2 does not exist in the set.
randomSet.remove(2)
// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2)
// getRandom should return either 1 or 2 randomly.
randomSet.getRandom()
// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1)
// 2 was already in the set, so return false.
randomSet.insert(2)
// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom()
## Solutions:
```python
class RandomizedSet :
public:
    /** Initialize your data structure here. */
    RandomizedSet() :
        tail = 0
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) :
        if (numToIndex.count(val) > 0)  return false
        if (tail == nums.size()) :
            nums.push_back(val)
            numToIndex[val] = tail
            ++tail
         else :
            nums[tail] = val
            numToIndex[val] = tail
            ++tail
        return true
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) :
        if (numToIndex.count(val) == 0) return false
        int lastValue = nums[tail - 1]
        int index = numToIndex[val]
        swap(nums[index], nums[tail - 1])
        numToIndex[lastValue] = index
        --tail
        numToIndex.erase(val)
        return true
    /** Get a random element from the set. */
    int getRandom() :
        int rIndex = rand() % tail
        return nums[rIndex]
private:
    vector nums
    int tail
    unordered_map numToIndex
/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet()
 * bool param_1 = obj->insert(val)
 * bool param_2 = obj->remove(val)
 * int param_3 = obj->getRandom()
 */
```
# 57. Insert Interval
* *Difficulty: Hard*
* *Topics: Array, Sort*
* *Similar Questions:*
  * [Merge Intervals](merge-intervals.md)
  * [Range Module](range-module.md)
## Problem:
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
## Solutions:
```python
class Solution :
public:
    vector> insert(vector>& intervals, vector& newInterval) :
        vector> ret
        int i = 0
        for ( i < intervals.size() ++i) :
            if (intervals[i][1] < newInterval[0])   :
                ret.push_back(intervals[i])
             else :
                break
        if (i == intervals.size()) :
            ret.push_back(newInterval)
            return ret
        if (newInterval[1] < intervals[i][0]) :
            ret.push_back(newInterval)
            ret.push_back(intervals[i])
         else :
            ret.push_back(:min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]))
        ++i
        for ( i < intervals.size() ++i) :
            if (ret.back()[1] < intervals[i][0]) :
                ret.push_back(intervals[i])
             else :
                ret.back()[1] = max(ret.back()[1], intervals[i][1])
        return ret
```
# 784. Insert into a Binary Search Tree
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Search in a Binary Search Tree](search-in-a-binary-search-tree.md)
## Problem:
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:
         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) :
        if (root == NULL) :
            return new TreeNode(val)
        if (val == root->val)   return root
        if (val val) :
            root->left = insertIntoBST(root->left, val)
         else :
            root->right = insertIntoBST(root->right, val)
        return root
```
# 147. Insertion Sort List
* *Difficulty: Medium*
* *Topics: Linked List, Sort*
* *Similar Questions:*
  * [Sort List](sort-list.md)
  * [Insert into a Cyclic Sorted List](insert-into-a-cyclic-sorted-list.md)
## Problem:
Sort a linked list using insertion sort.
A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
Algorithm of Insertion Sort:
	Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
	At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
	It repeats until no input elements remain.
Example 1:
Input: 4-&gt2-&gt1-&gt3
Output: 1-&gt2-&gt3-&gt4
Example 2:
Input: -1-&gt5-&gt3-&gt4-&gt0
Output: -1-&gt0-&gt3-&gt4-&gt5
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* insertionSortList(ListNode* head) :
        ListNode* dummy = new ListNode(0)
        while (head) :
            ListNode* next = head->next
            insert(dummy, head)
            head = next
        return dummy->next
    void insert(ListNode* head, ListNode* cur) :
        while (head->next && head->next->val val)    head = head->next
        if (head->next == nullptr) :
            head->next = cur
            cur->next = nullptr
         else :
            cur->next = head->next
            head->next = cur
```
# 343. Integer Break
* *Difficulty: Medium*
* *Topics: Math, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
Example 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 &times 1 = 1.
Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 &times 3 &times 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
## Solutions:
```python
class Solution :
public:
    int integerBreak(int n) :
        unordered_map cache
        if (n == 2) return 1
        if (n == 3) return 2
        return helper(n, cache)
private:
    int helper(int n, unordered_map& cache) :
        if (cache.count(n) > 0) return cache[n]
        if (n == 1) return 1
        if (n == 2) return 2
        if (n == 3) return 3
        int prod1 = 2 * helper(n - 2, cache)
        int prod2 = 3 * helper(n - 3, cache)
        int ret = max(prod1, prod2)
        cache[n] = ret
        return ret
```
# 397. Integer Replacement
* *Difficulty: Medium*
* *Topics: Math, Bit Manipulation*
* *Similar Questions:*
## Problem:
Given a positive integer n and you can do operations as follow:
If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?
Example 1:
Input:
8
Output:
3
Explanation:
8 -> 4 -> 2 -> 1
Example 2:
Input:
7
Output:
4
Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
## Solutions:
```python
class Solution :
public:
    int integerReplacement(int N) :
        int count = 0
        long n = N // to prevent overflow
        while (n > 3) :
            if (n % 2 == 0) :
                n = (n >> 1)
             else :
                if ((n & 0x2) == 0) :
                    n -= 1
                 else :
                    n += 1
            ++count
        if (n == 3) return count + 2 // special check
        if (n == 2) return count + 1 // special check
        return count
```
# 273. Integer to English Words
* *Difficulty: Hard*
* *Topics: Math, String*
* *Similar Questions:*
  * [Integer to Roman](integer-to-roman.md)
## Problem:
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
Example 1:
Input: 123
Output: &quotOne Hundred Twenty Three&quot
Example 2:
Input: 12345
Output: &quotTwelve Thousand Three Hundred Forty Five&quot
Example 3:
Input: 1234567
Output: &quotOne Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven&quot
Example 4:
Input: 1234567891
Output: &quotOne Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One&quot
## Solutions:
```python
class Solution :
public:
    string numberToWords(int num) :
        if (num == 0)   return "Zero"
        string ret
        if (num >= 1000000000) :
            ret += lessThousand(num / 1000000000) + " Billion "
            num = num % 1000000000
        if (num >= 1000000) :
            ret += lessThousand(num / 1000000) + " Million "
            num = num % 1000000
        if (num >= 1000) :
            ret += lessThousand(num / 1000) + " Thousand "
            num = num % 1000
        ret += lessThousand(num)
        if (ret.back() == ' ') :
            ret.pop_back()
        return ret
private:
    string lessThousand(int num) :
        string twenty[] :"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        string hundred[] :"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        string ret
        if (num / 100 > 0) :
            ret = twenty[num / 100] + " " + "Hundred "
            num = num % 100
        if (num >= 20) :
            ret += hundred[num/10 - 2] + " "
            num = num % 10
        if (num > 0) :
            ret += twenty[num]
        if (ret.length() > 0 && ret.back() == ' ') :
            ret.pop_back()
        return ret
```
# 12. Integer to Roman
* *Difficulty: Medium*
* *Topics: Math, String*
* *Similar Questions:*
  * [Roman to Integer](roman-to-integer.md)
  * [Integer to English Words](integer-to-english-words.md)
## Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one&#39s added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
	I can be placed before V (5) and X (10) to make 4 and 9. 
	X can be placed before L (50) and C (100) to make 40 and 90. 
	C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
Example 1:
Input: 3
Output: &quotIII&quot
Example 2:
Input: 4
Output: &quotIV&quot
Example 3:
Input: 9
Output: &quotIX&quot
Example 4:
Input: 58
Output: &quotLVIII&quot
Explanation: L = 50, V = 5, III = 3.
Example 5:
Input: 1994
Output: &quotMCMXCIV&quot
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
## Solutions:
```python
class Solution :
public:
    string intToRoman(int num) :
        vector> values = :
            :'I', 1,
            :'V', 5,
            :'X', 10,
            :'L', 50,
            :'C', 100,
            :'D', 500,
            :'M', 1000,
            :'?', 5000,
            :'*', 10000
        string ret
        vector digits
        for (int i = 0 i < 4 ++i) :
            int digit = num % 10
            num /= 10
            digits.push_back(digit)
        for (int i = 3 i >= 0 --i) :
            populateStr(ret, digits[i], values[i*2 + 2].first, values[i*2 + 1].first, values[i*2].first)
        return ret
    void populateStr(string& ret, int digit, char tenChar, char fiveChar, char oneChar) :
        if (digit == 0) return
        if (digit <= 3) :
            for (int i = 0 i < digit ++i) :
                ret.push_back(oneChar)
            return
        if (digit == 4) :
            ret.push_back(oneChar)
            ret.push_back(fiveChar)
            return
        if (digit <= 8) :
            ret.push_back(fiveChar)
            for (int i = 0 i < digit - 5 ++i) :
                ret.push_back(oneChar)
            return
        if (digit == 9) :
            ret.push_back(oneChar)
            ret.push_back(tenChar)
            return
```
### More concise solution1
From [Grandyang](https://www.cnblogs.com/grandyang/p/4123374.html)
```python
class Solution :
public:
    string intToRoman(int num) :
        string res = ""
        vector val:1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        vector str:"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        for (int i = 0 i < val.size() ++i) :
            while (num >= val[i]) :
                num -= val[i]
                res += str[i]
        return res
```
### More concise solution2
From [Grandyang](https://www.cnblogs.com/grandyang/p/4123374.html)
```python
class Solution :
public:
    string intToRoman(int num) :
        string res = ""
        vector v1:"", "M", "MM", "MMM"
        vector v2:"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"
        vector v3:"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"
        vector v4:"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"
        return v1[num / 1000] + v2[(num % 1000) / 100] + v3[(num % 100) / 10] + v4[num % 10]
```
# 97. Interleaving String
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
Example 1:
Input: s1 = &quotaabcc&quot, s2 = &quotdbbca&quot, s3 = &quotaadbbcbcac&quot
Output: true
Example 2:
Input: s1 = &quotaabcc&quot, s2 = &quotdbbca&quot, s3 = &quotaadbbbaccc&quot
Output: false
## Solutions:
```python
class Solution :
public:
    bool isInterleave(string s1, string s2, string s3) :
        if (s3.length() != s1.length() + s2.length())   return false
        int len1 = s1.length()
        int len2 = s2.length()
        vector> dp (len1 + 1, vector(len2 + 1, false))
        dp[0][0] = true
        for (int i = 1 i <= len1 ++i) :
            dp[i][0] = dp[i-1][0] && (s1[i-1] == s3[i-1]) 
        for (int j = 1 j <=len2 ++j) :
            dp[0][j] = dp[0][j-1] && (s2[j-1] == s3[j-1])
        for (int i = 1 i <= len1 ++i) :
            for (int j = 1 j <= len2 ++j) :
                // i, j denotes count
                dp[i][j] = (s3[i+j -1] == s1[i-1] ? dp[i-1][j] : false ) || (s3[i+j - 1] == s2[j-1] ? dp[i][j-1] : false)            
        /*
        for (int i = 0 i <= len1 ++i) :
            for (int j = 0 j <=len2 ++j) :
                cout << dp[i][j] << " "
            cout << endl
        */
        return dp[len1][len2]
```
# 1149. Intersection of Three Sorted Arrays
* *Difficulty: Easy*
* *Topics: Hash Table, Two Pointers*
* *Similar Questions:*
  * [Intersection of Two Arrays](intersection-of-two-arrays.md)
## Problem:
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Constraints:
	1 &lt= arr1.length, arr2.length, arr3.length &lt= 1000
	1 &lt= arr1[i], arr2[i], arr3[i] &lt= 2000
## Solutions:
```python
class Solution :
public:
    vector arraysIntersection(vector& arr1, vector& arr2, vector& arr3) :
        vector arr12 = helper(arr1, arr2)
        return helper(arr12, arr3)
private: 
    vector helper(vector& arr1, vector& arr2) :
        int i1 = 0, i2 = 0
        vector ret
        while (i1 < arr1.size() && i2 < arr2.size()) :
            if (arr1[i1] == arr2[i2]) :
                ret.push_back(arr1[i1])
                ++i1
                ++i2
             else if (arr1[i1] < arr2[i2]) :
                ++i1
             else :
                ++i2
        return ret
```
# 350. Intersection of Two Arrays II
* *Difficulty: Easy*
* *Topics: Hash Table, Two Pointers, Binary Search, Sort*
* *Similar Questions:*
  * [Intersection of Two Arrays](intersection-of-two-arrays.md)
  * [Find Common Characters](find-common-characters.md)
## Problem:
Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:
	Each element in the result should appear as many times as it shows in both arrays.
	The result can be in any order.
Follow up:
	What if the given array is already sorted? How would you optimize your algorithm?
	What if nums1&#39s size is small compared to nums2&#39s size? Which algorithm is better?
	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
## Solutions:
```python
class Solution :
public:
    vector intersect(vector& nums1, vector& nums2) :
        if (nums1.size() > nums2.size()) :
            return intersect(nums2, nums1)
        unordered_multiset numSet(nums1.begin(), nums1.end())
        vector ret
        for (auto num : nums2) :
            auto it = numSet.find(num)
            if (it != numSet.end()) :
                ret.push_back(num)
                numSet.erase(it)
        return ret
```
# 349. Intersection of Two Arrays
* *Difficulty: Easy*
* *Topics: Hash Table, Two Pointers, Binary Search, Sort*
* *Similar Questions:*
  * [Intersection of Two Arrays II](intersection-of-two-arrays-ii.md)
## Problem:
Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
	Each element in the result must be unique.
	The result can be in any order.
## Solutions:
```python
class Solution :
public:
    vector intersection(vector& nums1, vector& nums2) :
        unordered_set nums (nums1.begin(), nums1.end())
        unordered_set ret
        for (auto num : nums2) :
            if (nums.count(num) > 0) :
                ret.insert(num)
        return vector(ret.begin(), ret.end())
```
# 160. Intersection of Two Linked Lists
* *Difficulty: Easy*
* *Topics: Linked List*
* *Similar Questions:*
  * [Minimum Index Sum of Two Lists](minimum-index-sum-of-two-lists.md)
## Problem:
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
begin to intersect at node c1.
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node&#39s value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A There are 3 nodes before the intersected node in B.
Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node&#39s value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A There are 1 node before the intersected node in B.
Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
Notes:
	If the two linked lists have no intersection at all, return null.
	The linked lists must retain their original structure after the function returns.
	You may assume there are no cycles anywhere in the entire linked structure.
	Your code should preferably run in O(n) time and use only O(1) memory.
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) :
        if (headA == NULL || headB == NULL) return NULL // rememeber to check NULL at first
        bool rewindA = false
        bool rewindB = false
        ListNode* curA = headA
        ListNode* curB = headB
        do :
            if (curA == curB)   return curA
            if (curA->next) :
                curA = curA->next
             else if (!rewindA) :
                curA = headB
                rewindA = true
             else :
                return NULL
            if (curB->next) :
                curB = curB->next
             else if (!rewindB) :
                curB = headA
                rewindB = true
             else :
                return NULL
         while (true)
```
# 1028. Interval List Intersections
* *Difficulty: Medium*
* *Topics: Two Pointers*
* *Similar Questions:*
  * [Merge Intervals](merge-intervals.md)
  * [Merge Sorted Array](merge-sorted-array.md)
  * [Employee Free Time](employee-free-time.md)
## Problem:
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a &lt= b) denotes the set of real numbers x with a &lt= x &lt= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
Note:
	0 &lt= A.length &lt 1000
	0 &lt= B.length &lt 1000
	0 &lt= A[i].start, A[i].end, B[i].start, B[i].end &lt 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
## Solutions:
```python
class Solution :
public:
    vector> intervalIntersection(vector>& A, vector>& B) :
        vector> ret
        if(A.empty() && B.empty())  return :
        int posA = 0
        int posB = 0
        while (posA < A.size() || posB < B.size()) :
            if (posA == A.size()) :
                merge(ret, B[posB++])
                continue
            if (posB == B.size()) :
                merge(ret, A[posA++])
                continue
            if (A[posA][0] <= B[posB][0]) :
                merge(ret, A[posA++])
             else :
                merge(ret, B[posB++])
        ret.pop_back()
        return ret
private:
    void merge(vector>& ret, vector& interval) :
        if (ret.empty()) :
            ret.push_back(interval)
            return
        vector pending = ret.back()
        ret.pop_back()
        int overLapLeft = max(pending[0], interval[0])
        int overLapRight = min(pending[1], interval[1])
        if (overLapLeft <= overLapRight) :
            ret.push_back(:overLapLeft, overLapRight)
        ret.push_back(:min(pending[1], interval[1]), max(pending[1], interval[1]))
```
# 226. Invert Binary Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Invert a binary tree.
Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can&rsquot invert a binary tree on a whiteboard so f*** off.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* invertTree(TreeNode* root) :
        if (root == NULL)   return NULL
        TreeNode* left = invertTree(root->right)
        TreeNode* right = invertTree(root->left)
        root->left = left
        root->right = right
        return root
```
# 752. IP to CIDR
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Restore IP Addresses](restore-ip-addresses.md)
  * [Validate IP Address](validate-ip-address.md)
## Problem:
Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list (of smallest possible length) of CIDR blocks.
A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length.  For example: "123.45.67.89/20".  That prefix length "20" represents the number of common prefix bits in the specified range.
Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The initial ip address, when converted to binary, looks like this (spaces added for clarity):
255.0.0.7 -> 11111111 00000000 00000000 00000111
The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just this one address.
The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
255.0.0.8 -> 11111111 00000000 00000000 00001000
Addresses with common prefix of 29 bits are:
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111
The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just 11111111 00000000 00000000 00010000.
In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .
There were other representations, such as:
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
but our answer was the shortest possible.
Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100 
that are outside the specified range.
Note:
ip will be a valid IPv4 address.
Every implied address ip + x (for x ) will be a valid IPv4 address.
n will be an integer in the range [1, 1000].
## Solutions:
```python
class Solution :
public:
    vector ipToCIDR(string ip, int n) :
        vector ret
        size_t start = ipToUnsignedInt(ip)
        while (n > 0) :
            long longIp = start
            int mask = max(33 - bitLen(longIp & (-longIp)), 33 - bitLen(n))
            ret.push_back(unsignedIntToIp(start) + "/" + to_string(mask))
            start += (1 << (32 - mask))
            n -= (1 << (32 - mask))
        return ret
private:
    size_t ipToUnsignedInt(const string& ip) :
        size_t ret = 0
        size_t val= 0
        for (auto& c : ip) :
            if (c == '.') :
                ret = 256 * ret + val
                val = 0
             else :
                val = 10 * val + c - '0'
        ret = 256 * ret + val
        return ret
    string unsignedIntToIp(size_t ip) :
        return  to_string((ip >> 24) % 256) + "." + to_string((ip >> 16) % 256) + "." + to_string((ip >> 8) % 256) + "." + to_string(ip % 256)
    size_t bitLen(size_t n) :
        if (n == 0) return 1
        size_t ret = 0
        while (n != 0) :
            ++ret
            n >>= 1
        return ret
```
# 392. Is Subsequence
* *Difficulty: Easy*
* *Topics: Binary Search, Dynamic Programming, Greedy*
* *Similar Questions:*
  * [Number of Matching Subsequences](number-of-matching-subsequences.md)
  * [Shortest Way to Form String](shortest-way-to-form-string.md)
## Problem:
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
s = "abc", t = "ahbgdc"
Return true.
Example 2:
s = "axc", t = "ahbgdc"
Return false.
Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
Credits:Special thanks to @pbrother for adding this problem and creating all test cases.
## Solutions:
```python
class Solution :
public:
    bool isSubsequence(string s, string t) :
        if (s.length() > t.length())    return false
        int pos = 0
        for (int i = 0 i < s.length() ++i) :
            while (pos < t.length() && t[pos] != s[i]) :
                ++pos
            if (pos == t.length())  return false
            ++pos
        return true
```
# 463. Island Perimeter
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Max Area of Island](max-area-of-island.md)
  * [Flood Fill](flood-fill.md)
  * [Coloring A Border](coloring-a-border.md)
## Problem:
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn&#39t have &quotlakes&quot (water inside that isn&#39t connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don&#39t exceed 100. Determine the perimeter of the island.
Example:
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
## Solutions:
```python
class Solution :
public:
    int islandPerimeter(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        vector> visited(m, vector(n, false))
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j]) :
                    return dfs(grid, visited, i, j)
        return 0
private:
    int dfs(vector>& grid, vector>& visited, int row, int col) :
        int m = grid.size()
        int n = grid[0].size()
        if (row = m || col = n || !grid[row][col])  return 1
        if (visited[row][col])  return 0
        visited[row][col] = true
        int ret = 0
        ret += dfs(grid, visited, row + 1, col)
        ret += dfs(grid, visited, row - 1, col)
        ret += dfs(grid, visited, row, col + 1)
        ret += dfs(grid, visited, row, col - 1)
        return ret
```
# 205. Isomorphic Strings
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Word Pattern](word-pattern.md)
## Problem:
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
Example 1:
Input: s = &quotegg&quot, t = &quotadd&quot
Output: true
Example 2:
Input: s = &quotfoo&quot, t = &quotbar&quot
Output: false
Example 3:
Input: s = &quotpaper&quot, t = &quottitle&quot
Output: true
Note:
You may assume both s and t have the same length.
## Solutions:
```python
class Solution :
public:
    bool isIsomorphic(string s, string t) :
        unordered_map s2t
        unordered_map t2s
        if (s.length() != t.length())   return false
        for (int i = 0 i < s.length() ++i) :
            if (s2t.count(s[i]) > 0) :
                if (s2t[s[i]] != t[i] || t2s.count(t[i]) == 0 || t2s[t[i]] != s[i])  return false
             else :
                if (t2s.count(t[i]) > 0)  return false
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
        return true
```
# 782. Jewels and Stones
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
You&#39re given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so &quota&quot is considered a different type of stone from &quotA&quot.
Example 1:
Input: J = &quotaA&quot, S = &quotaAAbbbb&quot
Output: 3
Example 2:
Input: J = &quotz&quot, S = &quotZZ&quot
Output: 0
Note:
	S and J will consist of letters and have length at most 50.
	The characters in J are distinct.
## Solutions:
```python
class Solution :
public:
    int numJewelsInStones(string J, string S) :
        unordered_set jeweries (J.begin(), J.end())
        int count = 0
        for (auto& stone : S) :
            if (jeweries.count(stone) > 0) :
                ++count 
        return count
```
# 45. Jump Game II
* *Difficulty: Hard*
* *Topics: Array, Greedy*
* *Similar Questions:*
  * [Jump Game](jump-game.md)
## Problem:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:
You can assume that you can always reach the last index.
## Solutions:
```python
class Solution :
public:
    int jump(vector& nums) :
        int start = 0
        int reachable = 0
        int count = 0
        for () :
            if (reachable >= nums.size() - 1)   return count
            int nextReachable = 0
            for (int i = start i <= reachable ++i) :
                nextReachable = max(nextReachable, i + nums[i])
            start = reachable + 1
            reachable = nextReachable
            ++count
```
# 55. Jump Game
* *Difficulty: Medium*
* *Topics: Array, Greedy*
* *Similar Questions:*
  * [Jump Game II](jump-game-ii.md)
## Problem:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
## Solutions:
```python
class Solution :
public:
    bool canJump(vector& nums) :
        if (nums.size() == 0)   return false
        int distance = 0
        for (int i = 0 i <= distance ++i) :
            distance = max(distance, i + nums[i])
            if (distance >= nums.size() - 1) return true
        return false
```
# 1014. K Closest Points to Origin
* *Difficulty: Medium*
* *Topics: Divide and Conquer, Heap, Sort*
* *Similar Questions:*
  * [Kth Largest Element in an Array](kth-largest-element-in-an-array.md)
  * [Top K Frequent Elements](top-k-frequent-elements.md)
  * [Top K Frequent Words](top-k-frequent-words.md)
## Problem:
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &lt sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
Note:
	1 &lt= K &lt= points.length &lt= 10000
	-10000 &lt points[i][0] &lt 10000
	-10000 &lt points[i][1] &lt 10000
## Solutions:
```python
class Solution :
public:
    vector> kClosest(vector>& points, int K) :
        auto comparator = [](vector p1, vector p2) :
            return p1[0] * p1[0] + p1[1] * p1[1] < p2[0] * p2[0] + p2[1] * p2[1]
        priority_queue, vector>, decltype(comparator)> pq(comparator)
        for (auto& point : points) :
            pq.push(point)
            if (pq.size() > K) :
                pq.pop()
        vector> ret
        while (!pq.empty()) :
            ret.push_back(pq.top()) pq.pop()
        return ret
```
# 1299. K-Concatenation Maximum Sum
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
## Problem:
Given an integer array arr and an integer k, modify the array by repeating it k times.
For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].
Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.
As the answer can be very large, return the answer modulo 10^9 + 7.
Example 1:
Input: arr = [1,2], k = 3
Output: 9
Example 2:
Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:
Input: arr = [-1,-2], k = 7
Output: 0
Constraints:
	1 &lt= arr.length &lt= 10^5
	1 &lt= k &lt= 10^5
	-10^4 &lt= arr[i] &lt= 10^4
## Solutions:
```python
class Solution :
public:
    int kConcatenationMaxSum(vector& arr, int k) :
        if (k == 0) :
            return maxSubArray(arr)
         else :
            int sum = 0
            for (auto& val : arr) :
                sum += val
            long ret = 0
            if (sum >= 0) :
                ret += (sum * (long (k - 2))) % MOD
            arr.insert(arr.end(), arr.begin(), arr.end())
            ret = (ret + maxSubArray(arr)) % MOD
            return ret
private:
    int maxSubArray(vector& arr) :
        int sum = 0
        int ret = 0
        for (int i = 0 i < arr.size() ++i) :
            sum += arr[i]
            if (sum < 0) :
                sum = 0
             else :
                ret = max(ret, sum)
        return ret
    int MOD = 1e9 + 7
```
# 532. K-diff Pairs in an Array
* *Difficulty: Easy*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Minimum Absolute Difference in BST](minimum-absolute-difference-in-bst.md)
## Problem:
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
## Solutions:
```python
class Solution :
public:
    int findPairs(vector& nums, int k) :
        sort(nums.begin(), nums.end())
        int count = 0
        int j = 0
        for (int i = 1 i < nums.size() ++i) :
            while (j  k) :
                ++j
            if (j < i && nums[i] - nums[j] == k) :
                ++count
                while (j + 1 < nums.size() && nums[j] == nums[j+1]) ++j // this essential to deduplication.
                ++j
        return count
```
# 795. K-th Symbol in Grammar
* *Difficulty: Medium*
* *Topics: Recursion*
* *Similar Questions:*
## Problem:
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).
Examples:
Input: N = 1, K = 1
Output: 0
Input: N = 2, K = 1
Output: 0
Input: N = 2, K = 2
Output: 1
Input: N = 4, K = 5
Output: 1
Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:
	N will be an integer in the range [1, 30].
	K will be an integer in the range [1, 2^(N-1)].
## Solutions:
```python
class Solution :
public:
    int kthGrammar(int N, int K) :
        --K
        return helper(N, K)
private:
    int helper(int N, int K) :
        if (N == 1) return 0 
        int lastLevel = helper(N - 1, K/2)
        if (lastLevel == 0) return K % 2 == 0 ? 0 : 1
        else return K % 2 == 0 ? 1 : 0
```
# 500. Keyboard Row
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
Given a List of words, return the words that can be typed using letters of alphabet on only one row&#39s of American keyboard like the image below.
Example:
Input: [&quotHello&quot, &quotAlaska&quot, &quotDad&quot, &quotPeace&quot]
Output: [&quotAlaska&quot, &quotDad&quot]
Note:
	You may use one character in the keyboard more than once.
	You may assume the input string will only contain letters of alphabet.
## Solutions:
```python
class Solution :
public:
    vector findWords(vector& words) :
        vector ret
        for (auto& word : words) :
            if (sameRow(word)) :
                ret.push_back(word)
        return ret
private:
    bool sameRow(const string& str) :
        if (str.length() == 0)  return true
        char c = tolower(str[0])
        int row = -1
        for (int i = 0 i < 3 ++i) :
            if (board[i].find(c) != string::npos) :
                row = i
                break
        for (int i = 1 i < str.length() ++i) :
            if (board[row].find(tolower(str[i])) == string::npos)   return false
        return true
    vector board = :
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
```
# 688. Knight Probability in Chessboard
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Out of Boundary Paths](out-of-boundary-paths.md)
## Problem:
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.
Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Note:
	N will be between 1 and 25.
	K will be between 0 and 100.
	The knight always initially starts on the board.
## Solutions:
```python
class Solution :
public:
    double knightProbability(int N, int K, int r, int c) :
        map, double> cache
        return helper(N, K, r, c, cache)
private:
    double helper(int N, int K, int r, int c, map, double>& cache) :
        if (!(r >= 0 && r = 0 && c < N)) : // this check should put before getPosition!!!!
            return 0.0
        int position = getPosition(N, r, c)
        if (cache.count(:position, K) > 0) :
            return cache[:position, K]
        if (K == 0) :
            return 1.0
        double prob = 0
        for (int i = 0 i < 8 ++i) :
            prob += helper(N, K - 1, r + directions[i][0], c + directions[i][1], cache)
        prob /= 8
        cache[:position, K] = prob
        return prob
    inline int getPosition(int N, int r, int c) :
        return N * r + c
    int directions[8][2] = :
        :1, 2,
        :2, 1,
        :2, -1,
        :1, -2,
        :-1, -2,
        :-2, -1,
        :-2, 1,
        :-1, 2
```
# 215. Kth Largest Element in an Array
* *Difficulty: Medium*
* *Topics: Divide and Conquer, Heap*
* *Similar Questions:*
  * [Wiggle Sort II](wiggle-sort-ii.md)
  * [Top K Frequent Elements](top-k-frequent-elements.md)
  * [Third Maximum Number](third-maximum-number.md)
  * [Kth Largest Element in a Stream](kth-largest-element-in-a-stream.md)
  * [K Closest Points to Origin](k-closest-points-to-origin.md)
## Problem:
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 &le k &le array&#39s length.
## Solutions:
```python
class Solution :
public:
    int findKthLargest(vector& nums, int k) :
        return helper(nums, 0, nums.size() - 1, nums.size() - k)
    int helper(vector& nums, int left, int right, int k) :
        int oldLeft = left
        int oldRight = right
        if (left == right && left == k) return nums[k]
        int pivotal = nums[left]
        while (left <= right) :
            while (left <= right && nums[left] < pivotal) : // if the operation is <=, the program would run in infinite loop. Consider [2, 1], the program could not progress. 
                ++left
            while (left  pivotal) :
                --right
            if (left <= right) :
                swap(nums[left], nums[right])
                ++left
                --right
        if (k <= right) :
            return helper(nums, oldLeft, right, k)
         else if (k >= left) :
            return helper(nums, left, oldRight, k)
         else :
            return nums[k]
```
## Proof Sketch
The post loop-invariant is that: 
1. All elements left to `left` (exclusive) is smaller or equal to `pivotal`.
2. All elements right to `right` (exclusive) is greater or equal to `pivotal`. 
Therefore, after the crossing of `left` and `right`, all elements right/left to `left`/`right` (inclusive) are greater/smaller or equal to `pivotal`. It is possible that after crossing, `left` and `right` are **NOT** adjacent when both `left` and `right` are pointed to `pivotal` in the last iteration. Therefore, `else :return nums[k]` is essential when `k` happens to be the `pivotal`.
## Common Pitfalls
1. `while (left < right)`. The loop invariant may not hold any more. For example `[5, 6, 4]`, after first iteration, both `left` and `right` point to the middle element. The while loop exists but `6` is not equal to `pivotal`.  
2. `pivotal` is not equal to any element in the array. In this case, it is possible to result in infinite recursions. To avoid this situation, the next pitfall should also be avoided. 
3. `nums[left] <= pivotal`. In this case, the infinite-recursion happens for some cases like `[2, 1]`. The edge case is evil because swap happens at the boundary which makes no progress. 
If the last two pitfalls are avoided, it is guaranteed that the algorithm would make progress because one non-boundary swap is guaranteed. 
# 230. Kth Smallest Element in a BST
* *Difficulty: Medium*
* *Topics: Binary Search, Tree*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
  * [Second Minimum Node In a Binary Tree](second-minimum-node-in-a-binary-tree.md)
## Problem:
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: 
You may assume k is always valid, 1 &le k &le BST&#39s total elements.
Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int kthSmallest(TreeNode* root, int k) :
        int ret = 0
        int count = 0
        helper(root, k, ret, count)
        return ret
    bool helper(TreeNode* root, int k, int& ret, int& count) :
        if (root == NULL)   return false
        if (helper(root->left, k, ret, count))  return true
        ++count
        if (count == k) :
            ret = root->val
            return true
        return helper(root->right, k, ret, count)
```
# 378. Kth Smallest Element in a Sorted Matrix
* *Difficulty: Medium*
* *Topics: Binary Search, Heap*
* *Similar Questions:*
  * [Find K Pairs with Smallest Sums](find-k-pairs-with-smallest-sums.md)
  * [Kth Smallest Number in Multiplication Table](kth-smallest-number-in-multiplication-table.md)
  * [Find K-th Smallest Pair Distance](find-k-th-smallest-pair-distance.md)
  * [K-th Smallest Prime Fraction](k-th-smallest-prime-fraction.md)
## Problem:
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
Note: 
You may assume k is always valid, 1 &le k &le n2.
## Solutions:
```python
class Solution :
public:
    int kthSmallest(vector>& matrix, int k) :
        int m = matrix.size()
        if (m == 0) return -1
        int n = matrix[0].size()
        if (n == 0) return -1
        int left = matrix[0][0] 
        int right = matrix[m-1][n-1]
        while (left < right) :
            int mid = left + (right - left) / 2
            int count = countSmallerNum(matrix, m, n, mid)
            if (count >= k) :
                right =  mid
             else :
                left = mid + 1
        return left
private:
    int countSmallerNum(vector>& matrix, int m, int n, int num) :
        int row = m - 1
        int col = 0
        int count = 0
        while (row >= 0 && col < n) :
            int product = matrix[row][col]
            if (product <= num) :
                count += row + 1
                ++col
             else if (product > num) :
                --row
        return count
```
# 668. Kth Smallest Number in Multiplication Table
* *Difficulty: Hard*
* *Topics: Binary Search*
* *Similar Questions:*
  * [Kth Smallest Element in a Sorted Matrix](kth-smallest-element-in-a-sorted-matrix.md)
  * [Find K-th Smallest Pair Distance](find-k-th-smallest-pair-distance.md)
  * [K-th Smallest Prime Fraction](k-th-smallest-prime-fraction.md)
## Problem:
Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?
Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.
Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9
The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]
## Solutions:
```python
class Solution :
public:
    int findKthNumber(int m, int n, int k) :
        int left = 1 
        int right = m * n
        while (left < right) :
            int mid = left + (right - left) / 2
            int count = countSmallerNum(m, n, mid)
            if (count >= k) :
                right =  mid
             else :
                left = mid + 1
        return left
private:
    int countSmallerNum(int m, int n, int num) :
        int row = m - 1
        int col = 0
        int count = 0
        while (row >= 0 && col < n) :
            int product = (row + 1) * (col + 1)
            if (product <= num) :
                count += row + 1
                ++col
             else if (product > num) :
                --row
        return count
```
# 333. Largest BST Subtree
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
Note:
A subtree must include all of its descendants.
Example:
Input: [10,5,15,1,8,null,7]
   10 
   / \ 
  5  15 
 / \   \ 
1   8   7
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree&#39s size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int largestBSTSubtree(TreeNode* root) :
        int left
        int right
        int num = 0
        helper(root, left, right, num)
        return num
private:
    TreeNode* helper(TreeNode* root, int& left, int& right, int& num) :
        if (root == nullptr)    return nullptr
        int left1 = INT_MAX
        int right1 = INT_MIN
        int num1 = 0
        TreeNode* leftRet = helper(root->left, left1, right1, num1)
        int left2 = INT_MAX 
        int right2 = INT_MIN
        int num2 = 0
        TreeNode* rightRet = helper(root->right, left2, right2, num2)
        if (leftRet == root->left && rightRet == root->right && root->val > right1 && root->val < left2) :
            num = 1 + num1 + num2
            left = (num1 == 0 ? root->val : left1)
            right = (num2 == 0 ? root->val : right2)
            return root
        if (num1 >= num2) :
            num = num1
            return leftRet
         else :
            num = num2
            return rightRet
```
# 368. Largest Divisible Subset
* *Difficulty: Medium*
* *Topics: Math, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.
If there are multiple solutions, return any subset is fine.
Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]
## Solutions:
```python
class Solution :
public:
    vector largestDivisibleSubset(vector& nums) :
        if (nums.size() == 0)   return : // this is essential otherwiseret.push_back(nums[index]) is incorrect
        sort(nums.begin(), nums.end())
        int n = nums.size()
        vector dp(n, 1)
        for (int i = 1 i < nums.size() ++i) :
            for (int j = 0 j < i ++j) :
                if (nums[i] % nums[j] == 0) :
                    dp[i] = max(dp[i], 1 + dp[j])
        int index = 0
        int maxVal = 0
        for (int i = 0 i < nums.size() ++i) :
            if (dp[i] > maxVal) :
                index = i
                maxVal = dp[i]
        vector ret
        ret.push_back(nums[index])
        --index
        while (index >= 0) :
            if (ret.back() % nums[index] == 0 && dp[index] +  ret.size() == maxVal) :
                ret.push_back(nums[index])
            --index
        return ret
```
# 179. Largest Number
* *Difficulty: Medium*
* *Topics: Sort*
* *Similar Questions:*
## Problem:
Given a list of non negative integers, arrange them such that they form the largest number.
Example 1:
Input: [10,2]
Output: &quot210&quot
Example 2:
Input: [3,30,34,5,9]
Output: &quot9534330&quot
Note: The result may be very large, so you need to return a string instead of an integer.
## Solutions:
```python
class Solution :
public:
    struct comparator :
        bool operator()(const string& a, const string& b) :
            return a + b > b + a // not necessary to have stol
    string largestNumber(vector& nums) :
        vector numStr
        bool allZeros = true
        for (auto num : nums) :
            if (num != 0)   allZeros = false
            numStr.push_back(to_string(num))
        if (allZeros == true)   return "0"
        sort(numStr.begin(), numStr.end(), comparator())
        string ret
        for (auto& str : numStr) :
            ret.append(str)
        return ret
```
# 84. Largest Rectangle in Histogram
* *Difficulty: Hard*
* *Topics: Array, Stack*
* *Similar Questions:*
  * [Maximal Rectangle](maximal-rectangle.md)
## Problem:
Given n non-negative integers representing the histogram&#39s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example:
Input: [2,1,5,6,2,3]
Output: 10
## Solutions:
```python
class Solution :
public:
    int largestRectangleArea(vector& heights) :
        heights.push_back(0)
        stack stk
        int area = 0
        for (int i = 0 i < heights.size() ++i) :
            while (!stk.empty() && heights[stk.top()] > heights[i]) :
                int topIndex = stk.top()
                stk.pop()
                area = max(area, heights[topIndex] * (i - (stk.empty() ? 0 : stk.top() + 1)))
                //cout << area << endl
            stk.push(i)
        return area
```
# 830. Largest Triangle Area
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Largest Perimeter Triangle](largest-perimeter-triangle.md)
## Problem:
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.
Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.
Notes: 
	3 &lt= points.length &lt= 50.
	No points will be duplicated.
	 -50 &lt= points[i][j] &lt= 50.
	Answers within 10^-6 of the true value will be accepted as correct.
## Solutions:
```python
class Solution :
public:
    double largestTriangleArea(vector>& points) :
        int n = points.size()
        double ret = 0
        for (int i = 0 i < points.size() ++i) :
            for (int j = i + 1 j < points.size() ++j) :
                for (int k = j + 1 k < points.size() ++k) :
                    ret = max(ret, area(points[i], points[j], points[k]))     
        return ret
private:
    inline double area(vector& p1, vector& p2, vector& p3) :
        // (p2[0] - p1[0], p2[1] - p1[1]) cross product (p3[0] - p1[0], p3[1] - p1[1])
        return 0.5 * abs(((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0])))
```
# 890. Lemonade Change
* *Difficulty: Easy*
* *Topics: Greedy*
* *Similar Questions:*
## Problem:
At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
Note that you don&#39t have any change in hand at first.
Return true if and only if you can provide every customer with correct change.
Example 1:
Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:
Input: [5,5,10]
Output: true
Example 3:
Input: [10,10]
Output: false
Example 4:
Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.
Note:
	0 &lt= bills.length &lt= 10000
	bills[i] will be either 5, 10, or 20.
## Solutions:
```python
class Solution :
public:
    bool lemonadeChange(vector& bills) :
        map changes = :
            :5, 0,
            :10, 0,
            :20, 0
        for (auto& bill : bills) :
            int change = bill - 5
            ++changes[bill]
            while (change > 0) :
                for (auto it = changes.rbegin()  ++it) :
                    if (it == changes.rend())    return false
                    if (it->second > 0 && it->first <= change) :
                        --it->second
                        change -= it->first
                        break
        return true
```
# 58. Length of Last Word
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
Given a string s consists of upper/lower-case alphabets and empty space characters &#39 &#39, return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
Example:
Input: &quotHello World&quot
Output: 5
## Solutions:
```python
class Solution :
public:
    int lengthOfLastWord(string s) :
        int len = 0
        for (int i = 0 i < s.length() ++i) :
            if (s[i] != ' ') :
                if (i != 0 && s[i-1] == ' ') len = 1
                else ++len
        return len
```
# 17. Letter Combinations of a Phone Number
* *Difficulty: Medium*
* *Topics: String, Backtracking*
* *Similar Questions:*
  * [Generate Parentheses](generate-parentheses.md)
  * [Combination Sum](combination-sum.md)
  * [Binary Watch](binary-watch.md)
## Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example:
Input: &quot23&quot
Output: [&quotad&quot, &quotae&quot, &quotaf&quot, &quotbd&quot, &quotbe&quot, &quotbf&quot, &quotcd&quot, &quotce&quot, &quotcf&quot].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
## Solutions:
```python
class Solution :
public:
    vector letterCombinations(string digits) :
        vector ret
        if (digits.length() == 0)   return ret
        int pos = 0
        string path
        dfs(digits, pos, path, ret)
        return ret
    void dfs(string digits, int pos, string& path, vector& ret) :
        if (pos == digits.length()) :
            ret.push_back(path)
            return
        char digit = digits[pos]
        for (auto c : numToLetters[digit]) :
            path.push_back(c)
            dfs(digits, pos + 1, path, ret)
            path.pop_back()
private:
    unordered_map numToLetters :
            :'2', "abc", 
            :'3', "def",
            :'4', "ghi",
            :'5', "jkl",
            :'6', "mno",
            :'7', "pqrs",
            :'8', "tuv",
            :'9', "wxyz"
```
# 482. License Key Formatting
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.
Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.
Given a non-empty string S and a number K, format the string according to the rules described above.
Example 1:
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"
Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
## Solutions:
```python
class Solution :
public:
    string licenseKeyFormatting(string S, int K) :
        string ret
        int count = 0
        if (S.length() == 0)    return ""
        for (int i = S.length() - 1 i >= 0 --i) :
            if (S[i] == '-')    continue
            ret.push_back(toupper(S[i]))
            ++count
            if (count == K) :
                ret.push_back('-')
                count = 0
        if (ret.back() == '-')  ret.pop_back()
        return :ret.rbegin(), ret.rend()
```
# 835. Linked List Components
* *Difficulty: Medium*
* *Topics: Linked List*
* *Similar Questions:*
## Problem:
We are given head, the head node of a linked list containing unique integer values.
We are also given the list G, a subset of the values in the linked list.
Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.
Example 1:
Input: 
head: 0-&gt1-&gt2-&gt3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:
Input: 
head: 0-&gt1-&gt2-&gt3-&gt4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note: 
	If N is the length of the linked list given by head, 1 &lt= N &lt= 10000.
	The value of each node in the linked list will be in the range [0, N - 1].
	1 &lt= G.length &lt= 10000.
	G is a subset of all values in the linked list.
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    int numComponents(ListNode* head, vector& G) :
        unordered_set nums(G.begin(), G.end())
        ListNode* cur = head
        int ret = 0
        bool hasNum = false
        while (cur) :
            if (nums.count(cur->val) == 0) :
                if (hasNum) :
                    ++ret
                    hasNum = false
                cur = cur->next
             else :
                hasNum = true
                cur = cur->next
        if (hasNum) :
            ++ret
        return ret
```
# 142. Linked List Cycle II
* *Difficulty: Medium*
* *Topics: Linked List, Two Pointers*
* *Similar Questions:*
  * [Linked List Cycle](linked-list-cycle.md)
  * [Find the Duplicate Number](find-the-duplicate-number.md)
## Problem:
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
Follow-up:
Can you solve it without using extra space?
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode *detectCycle(ListNode *head) :
        ListNode* fast = head
        ListNode* slow = head
        while (fast && fast->next) :
            fast = fast->next->next
            slow = slow->next
            if (slow == fast) break 
        if (fast != slow || head == NULL || head->next == NULL)   return NULL
        ListNode* another = head
        while (another != slow) :
            another = another->next
            slow = slow->next
        return another
```
# 141. Linked List Cycle
* *Difficulty: Easy*
* *Topics: Linked List, Two Pointers*
* *Similar Questions:*
  * [Linked List Cycle II](linked-list-cycle-ii.md)
  * [Happy Number](happy-number.md)
## Problem:
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
Follow up:
Can you solve it using O(1) (i.e. constant) memory?
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    bool hasCycle(ListNode *head) :
        ListNode* fast = head
        ListNode* slow = head
        while (fast && fast->next) :
            fast = fast->next->next
            slow = slow->next
            if (fast == slow)   return true
        return false
```
# 382. Linked List Random Node
* *Difficulty: Medium*
* *Topics: Reservoir Sampling*
* *Similar Questions:*
  * [Random Pick Index](random-pick-index.md)
## Problem:
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
Example:
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1)
head.next = new ListNode(2)
head.next.next = new ListNode(3)
Solution solution = new Solution(head)
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom()
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) :
        this->head = head
    /** Returns a random node's value. */
    int getRandom() :
        int count = 0
        int val
        ListNode* cur = head
        while (cur != nullptr) :
            ++count
            if (rand() % count == 0) :
                val = cur->val
            cur = cur->next
        return val
private:
    ListNode* head
/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head)
 * int param_1 = obj->getRandom()
 */
```
# 359. Logger Rate Limiter
* *Difficulty: Easy*
* *Topics: Hash Table, Design*
* *Similar Questions:*
  * [Design Hit Counter](design-hit-counter.md)
## Problem:
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.
Example:
Logger logger = new Logger()
// logging string &quotfoo&quot at timestamp 1
logger.shouldPrintMessage(1, &quotfoo&quot) returns true 
// logging string &quotbar&quot at timestamp 2
logger.shouldPrintMessage(2,&quotbar&quot) returns true
// logging string &quotfoo&quot at timestamp 3
logger.shouldPrintMessage(3,&quotfoo&quot) returns false
// logging string &quotbar&quot at timestamp 8
logger.shouldPrintMessage(8,&quotbar&quot) returns false
// logging string &quotfoo&quot at timestamp 10
logger.shouldPrintMessage(10,&quotfoo&quot) returns false
// logging string &quotfoo&quot at timestamp 11
logger.shouldPrintMessage(11,&quotfoo&quot) returns true
## Solutions:
```python
class Logger :
public:
    /** Initialize your data structure here. */
    Logger() :
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) :
        if (!lastTime.count(message)) :
            lastTime[message] = timestamp
            return true
        if (timestamp - lastTime[message] >= 10) :
            lastTime[message] = timestamp
            return true
         else :
            return false
private:
    unordered_map lastTime
/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger()
 * bool param_1 = obj->shouldPrintMessage(timestamp,message)
 */
```
# 531. Lonely Pixel I
* *Difficulty: Medium*
* *Topics: Array, Depth-first Search*
* *Similar Questions:*
  * [Lonely Pixel II](lonely-pixel-ii.md)
## Problem:
Given a picture consisting of black and white pixels, find the number of black lonely pixels.
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively. 
A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].
## Solutions:
```python
class Solution :
public:
    int findLonelyPixel(vector>& picture) :
        int m = picture.size()
        if (m == 0) return 0
        int n = picture[0].size()
        if (n == 0) return 0
        int ret = 0
        for (int row = 0 row < m ++row) :
            int blackIdx = -1
            int blackCount = 0
            for (int col = 0 col < n ++col) :
                if (picture[row][col] == 'B') :
                    blackIdx = col
                    ++blackCount
                    if (blackCount > 1) break
            if (blackCount == 1) :
                int i
                for (i = 0 i < m ++i) :
                    if (i == row)   continue
                    if (picture[i][blackIdx] == 'B')    break
                if (i == m) ++ret
        return ret
```
# 1330. Longest Arithmetic Subsequence of Given Difference
* *Difficulty: Medium*
* *Topics: Math, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
Example 1:
Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:
Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:
Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
Constraints:
	1 &lt= arr.length &lt= 10^5
	-10^4 &lt= arr[i], difference &lt= 10^4
## Solutions:
```python
class Solution :
public:
    int longestSubsequence(vector& arr, int difference) :
        int ret = 0
        unordered_map dp
        for (auto& num : arr) :
            int last = num - difference
            if (dp.count(last) == 0) :
                dp[num] = 1
             else :
                if (dp.count(num) == 0) :
                    dp[num] = 1
                dp[num] = max(dp[num], 1 + dp[last])
            ret = max(ret, dp[num])
        return ret
```
# 14. Longest Common Prefix
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string &quot&quot.
Example 1:
Input: [&quotflower&quot,&quotflow&quot,&quotflight&quot]
Output: &quotfl&quot
Example 2:
Input: [&quotdog&quot,&quotracecar&quot,&quotcar&quot]
Output: &quot&quot
Explanation: There is no common prefix among the input strings.
Note:
All given inputs are in lowercase letters a-z.
## Solutions:
```python
class Solution :
public:
    string longestCommonPrefix(vector& strs) :
        string ret
        if (strs.empty())   return ret   
        int i = 0
        while (true) :
            if (i >= strs[0].length())  return ret
            char commonChar = strs[0][i]
            for (auto& str : strs) :
                if (i >= str.length() || commonChar != str[i])  return ret
            ret.push_back(commonChar)
            ++i
```
# 128. Longest Consecutive Sequence
* *Difficulty: Hard*
* *Topics: Array, Union Find*
* *Similar Questions:*
  * [Binary Tree Longest Consecutive Sequence](binary-tree-longest-consecutive-sequence.md)
## Problem:
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.
Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
## Solutions:
```python
class Solution :
public:
    int longestConsecutive(vector& nums) :
        unordered_set numSet (nums.begin(), nums.end())
        int ret = 0
        for (auto num : nums) :
            if (numSet.count(num) > 0) :
                int count = 1
                count += countToward(numSet, num - 1, true)
                count += countToward(numSet, num + 1, false)
                ret = max(ret, count)
        return ret
    int countToward(unordered_set& numSet, int num, bool backward) :
        int count = 0
        while (true) :
            auto it = numSet.find(num)
            if (it == numSet.end()) return count
            ++count
            numSet.erase(it)
            if (backward)
                --num
            else 
                ++num
```
# 674. Longest Continuous Increasing Subsequence
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Number of Longest Increasing Subsequence](number-of-longest-increasing-subsequence.md)
  * [Minimum Window Subsequence](minimum-window-subsequence.md)
## Problem:
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note:
Length of the array will not exceed 10,000.
## Solutions:
```python
class Solution :
public:
    int findLengthOfLCIS(vector& nums) :
        if (nums.size() == 0)   return 0
        int left = 0
        int ret = 1
        int right = 1
        for (right = 1 right < nums.size() ++right) :
            if (nums[right] > nums[right - 1]) :
                ret = max(ret, right - left + 1)
             else :
                left = right
        ret = max(ret, right - left)
        return ret
```
# 594. Longest Harmonious Subsequence
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
## Solutions:
```python
class Solution :
public:
    int findLHS(vector& nums) :
        unordered_map numCount
        for (auto& num : nums) :
            ++numCount[num]
        int ret = 0
        for (auto& entry : numCount) :
            if (numCount.count(entry.first + 1)) :
                ret = max(ret, entry.second + numCount[entry.first + 1])
        return ret
```
# 329. Longest Increasing Path in a Matrix
* *Difficulty: Hard*
* *Topics: Depth-first Search, Topological Sort, Memoization*
* *Similar Questions:*
## Problem:
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
Example 1:
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
## Solutions:
```python
class Solution :
public:
    int longestIncreasingPath(vector>& matrix) :
        unordered_map memory
        int m = matrix.size()
        if (m == 0) return 0
        int n = matrix[0].size()
        if (n == 0) return 0
        int ret = 0
        for (int row = 0 row < m ++row) :
            for (int col = 0 col < n ++col) :
                ret = max(ret, dfs(matrix, m, n, row, col, memory))
        return ret
    int dfs(const vector>&matrix, int m , int n, int row, int col, unordered_map& memory) :
        int coord = n * row + col
        if (memory.count(coord) > 0) :
            return memory[coord]
         else :
            int maxPathLen = 1
            for (int d = 0 d < 4 ++d) :
                int nextRow = row + directions[d][0]
                int nextCol = col + directions[d][1]
                if (nextRow = m || nextCol = n)  continue
                if (matrix[nextRow][nextCol] <= matrix[row][col]) continue
                maxPathLen = max(maxPathLen, 1 + dfs(matrix, m, n, nextRow, nextCol, memory))
            memory[coord] = maxPathLen
            return maxPathLen
private:
    int directions[4][2] = :
        :1, 0,
        :-1, 0,
        :0, 1,
        :0, -1
```
# 300. Longest Increasing Subsequence
* *Difficulty: Medium*
* *Topics: Binary Search, Dynamic Programming*
* *Similar Questions:*
  * [Increasing Triplet Subsequence](increasing-triplet-subsequence.md)
  * [Russian Doll Envelopes](russian-doll-envelopes.md)
  * [Maximum Length of Pair Chain](maximum-length-of-pair-chain.md)
  * [Number of Longest Increasing Subsequence](number-of-longest-increasing-subsequence.md)
  * [Minimum ASCII Delete Sum for Two Strings](minimum-ascii-delete-sum-for-two-strings.md)
## Problem:
Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note: 
	There may be more than one LIS combination, it is only necessary for you to return the length.
	Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
## Solutions:
```python
class Solution :
public:
    int lengthOfLIS(vector& nums) :
        if (nums.size() == 0)   return 0
        map dp
        for (auto& num : nums) :
            if (dp.empty()) :
                dp[num] = 1
                continue
            if (dp.count(num))  continue
            auto it = dp.lower_bound(num)
            if (it == dp.end()) :
                dp[num] = prev(it)->second + 1
             else :
                dp[num] = it->second
                dp.erase(it)
        return dp.rbegin()->second
```
# 409. Longest Palindrome
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Palindrome Permutation](palindrome-permutation.md)
## Problem:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
Example: 
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
## Solutions:
```python
class Solution :
public:
    int longestPalindrome(string s) :
        int count = 0
        int charCount[256] = :0
        for (auto& c : s) :
            ++charCount[c]
            if (charCount[c] == 2) :
                count += 2
                charCount[c] = 0
        return s.length() == count ? count : count + 1
```
# 516. Longest Palindromic Subsequence
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Longest Palindromic Substring](longest-palindromic-substring.md)
  * [Palindromic Substrings](palindromic-substrings.md)
  * [Count Different Palindromic Subsequences](count-different-palindromic-subsequences.md)
  * [Longest Common Subsequence](longest-common-subsequence.md)
## Problem:
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: 
"bbbab"
Output: 
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
## Solutions:
```python
class Solution :
public:
    int longestPalindromeSubseq(string s) :
        int n = s.length()
        if (n == 0) return 0
        vector> dp (n, vector(n, 0))
        for (int i = 0 i < s.length() ++i) :
            dp[i][i] = 1
        for (int l = 2 l <= s.length() ++l) :
            for (int i = 0 i < s.length() ++i) :
                int left = i
                int right = i + l - 1
                if (right >= n) break
                dp[left][right] = max(dp[left][right-1], dp[left+1][right])
                if (s[left] == s[right]) :
                    dp[left][right] = max(dp[left][right], 2 + dp[left + 1][right - 1])
        return dp[0][n-1]
```
# 5. Longest Palindromic Substring
* *Difficulty: Medium*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
  * [Shortest Palindrome](shortest-palindrome.md)
  * [Palindrome Permutation](palindrome-permutation.md)
  * [Palindrome Pairs](palindrome-pairs.md)
  * [Longest Palindromic Subsequence](longest-palindromic-subsequence.md)
  * [Palindromic Substrings](palindromic-substrings.md)
## Problem:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: &quotbabad&quot
Output: &quotbab&quot
Note: &quotaba&quot is also a valid answer.
Example 2:
Input: &quotcbbd&quot
Output: &quotbb&quot
## Solutions:
```python
class Solution :
public:
    string longestPalindrome(string s) :
        int n = s.length()
        int length1 = 0
        int length2 = 0
        int ret = 0
        int len = 0
        for (int center = 0 center < n ++center) : 
            int left1 = center
            int right1 = center
            int count1 = 0
            while (left1 >= 0 && right1 < n && s[left1] == s[right1]) : // increment is not in while loop
                ++count1
                --left1
                ++right1
            length1 = 2*count1 - 1
            if (length1 > len) :
                len = length1
                ret = left1 + 1
            int count2 = 0
            int left2 = center
            int right2 = center + 1
            while (left2 >= 0 && right2 < n && s[left2] == s[right2]) :
                ++count2
                --left2
                ++right2
            length2 = 2 * count2
            if (length2 > len) :
                len = length2
                ret = left2 + 1
        return s.substr(ret, len)
```
## Optimization
It is possible to refactor the two while loops by define a function `getLen(const string& str, int left, int right)`.
For odd-length palindrome, initially `left == right`. 
The following code is taken from [Huahua](https://zxi.mytechroad.com/blog/greedy/leetcode-5-longest-palindromic-substring/)
```python
// Author: Huahua
class Solution :
public:
  string longestPalindrome(string s) :
    int best_len = 0
    int start = 0
    for (int i = 0 i < s.length() ++i) :
      int l1 = getLen(s, i, i)
      int l2 = getLen(s, i, i + 1)
      int l = max(l1, l2)      
      if (l > best_len) :
        best_len = l
        start = i - (l - 1) / 2
    return s.substr(start, best_len)
private:
  int getLen(const string& s, int l, int r) :
    if (s[l] != s[r]) return 1    
    while (l >= 0 && r <= s.length() - 1 && s[l] == s[r]) :
      --l
      ++r
    return r - l - 1
```
# 1129. Longest String Chain
* *Difficulty: Medium*
* *Topics: Hash Table, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a list of words, each word consists of English lowercase letters.
Let&#39s say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, &quotabc&quot is a predecessor of &quotabac&quot.
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k &gt= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.
Example 1:
Input: [&quota&quot,&quotb&quot,&quotba&quot,&quotbca&quot,&quotbda&quot,&quotbdca&quot]
Output: 4
Explanation: one of the longest word chain is &quota&quot,&quotba&quot,&quotbda&quot,&quotbdca&quot.
Note:
	1 &lt= words.length &lt= 1000
	1 &lt= words[i].length &lt= 16
	words[i] only consists of English lowercase letters.
## Solutions:
```python
class Solution :
public:
    int longestStrChain(vector& words) :
        if (words.size() == 0)  return 0
        auto comparator = [](const string& word1, const string& word2) :
            return word1.length() < word2.length()
        int ret = 0
        unordered_map dp = :
        sort(words.begin(), words.end(), comparator)
        int pos = 0
        for (int len = 1 len <= words.back().length() ++len) :
            unordered_map temp
            while (pos < words.size() && words[pos].length() == len) :
                string word = words[pos]
                temp[word] = 1 // this initializaiton is very important!
                for (auto& entry : dp) :
                    if (isPredecessor(entry.first, word)) :
                        temp[word] = max(temp[word], 1 + entry.second)
                ret = max(ret, temp[word])
                // update pos
                ++pos
            swap(dp, temp)
        return ret
private:
    bool isPredecessor(const string& str1, const string& str2) :
        int pos = 0
        while (pos < str1.length() && str1[pos] == str2[pos]) ++pos
        if (pos == str1.length())   return true
        while (pos < str1.length() && str1[pos] == str2[pos + 1]) ++pos
        return pos == str1.length()
```
# 340. Longest Substring with At Most K Distinct Characters
* *Difficulty: Hard*
* *Topics: Hash Table, String, Sliding Window*
* *Similar Questions:*
  * [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md)
  * [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters.md)
  * [Longest Repeating Character Replacement](longest-repeating-character-replacement.md)
  * [Subarrays with K Different Integers](subarrays-with-k-different-integers.md)
  * [Max Consecutive Ones III](max-consecutive-ones-iii.md)
## Problem:
Given a string, find the length of the longest substring T that contains at most k distinct characters.
Example 1:
Input: s = &quoteceba&quot, k = 2
Output: 3
Explanation: T is &quotece&quot which its length is 3.
Example 2:
Input: s = &quotaa&quot, k = 1
Output: 2
Explanation: T is &quotaa&quot which its length is 2.
## Solutions:
```python
class Solution :
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) :
        unordered_map charCount
        int left = 0
        int maxLen = 0
        for (int right = 0 right < s.length() ++right) :
            ++charCount[s[right]]
            if (charCount.size() <= k) :
                maxLen = max(maxLen, right - left + 1)
             else :
                while (left  k) :
                    if(--charCount[s[left]] == 0)  charCount.erase(s[left])
                    ++left
        return maxLen
```
# 159. Longest Substring with At Most Two Distinct Characters
* *Difficulty: Hard*
* *Topics: Hash Table, Two Pointers, String, Sliding Window*
* *Similar Questions:*
  * [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md)
  * [Sliding Window Maximum](sliding-window-maximum.md)
  * [Longest Substring with At Most K Distinct Characters](longest-substring-with-at-most-k-distinct-characters.md)
  * [Subarrays with K Different Integers](subarrays-with-k-different-integers.md)
## Problem:
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
Example 1:
Input: &quoteceba&quot
Output: 3
Explanation: t is &quotece&quot which its length is 3.
Example 2:
Input: &quotccaabbb&quot
Output: 5
Explanation: t is &quotaabbb&quot which its length is 5.
## Solutions:
```python
class Solution :
public:
    int lengthOfLongestSubstringTwoDistinct(string s) :
        unordered_map charCount
        int left = 0
        int maxLen = 0
        for (int right = 0 right < s.length() ++right) :
            ++charCount[s[right]]
            if (charCount.size() <= 2) :
                maxLen = max(maxLen, right - left + 1)
             else :
                while (left  2) :
                    if(--charCount[s[left]] == 0)  charCount.erase(s[left])
                    ++left
        return maxLen
```
# 3. Longest Substring Without Repeating Characters
* *Difficulty: Medium*
* *Topics: Hash Table, Two Pointers, String, Sliding Window*
* *Similar Questions:*
  * [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters.md)
  * [Longest Substring with At Most K Distinct Characters](longest-substring-with-at-most-k-distinct-characters.md)
  * [Subarrays with K Different Integers](subarrays-with-k-different-integers.md)
## Problem:
Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: &quotabcabcbb&quot
Output: 3 
Explanation: The answer is &quotabc&quot, with the length of 3. 
Example 2:
Input: &quotbbbbb&quot
Output: 1
Explanation: The answer is &quotb&quot, with the length of 1.
Example 3:
Input: &quotpwwkew&quot
Output: 3
Explanation: The answer is &quotwke&quot, with the length of 3. 
             Note that the answer must be a substring, &quotpwke&quot is a subsequence and not a substring.
## Solutions:
```python
class Solution :
public:
    int lengthOfLongestSubstring(string s) :
        int charPos[256] :0 // initialization only for 0, not for other values
        for (int i = 0 i < 256 ++i) charPos[i] = -1
        int ret = 0
        int left = 0
        for (int i = 0 i < s.length() ++i) :
            char c = s[i]
            if (charPos[c] == -1 || charPos[c] < left) :
                charPos[c] = i
                ret = max(ret, i - left + 1)
             else :
                left = max(charPos[c] + 1, left) // first to update left
                charPos[c] = i
        return ret
```
# 521. Longest Uncommon Subsequence I 
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Longest Uncommon Subsequence II](longest-uncommon-subsequence-ii.md)
## Problem:
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), because "aba" is a subsequence of "aba", but not a subsequence of any other strings in the group of two strings. 
Note:
Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings. 
## Solutions:
```python
class Solution :
public:
    int findLUSlength(string a, string b) :
        if (a == b) return -1
        return max(a.length(), b.length())
```
# 32. Longest Valid Parentheses
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
  * [Valid Parentheses](valid-parentheses.md)
## Problem:
Given a string containing just the characters &#39(&#39 and &#39)&#39, find the length of the longest valid (well-formed) parentheses substring.
Example 1:
Input: &quot(()&quot
Output: 2
Explanation: The longest valid parentheses substring is &quot()&quot
Example 2:
Input: &quot)()())&quot
Output: 4
Explanation: The longest valid parentheses substring is &quot()()&quot
## Solutions:
```python
class Solution : //gready method need to consider two scenarios
                // example "(()"
public:
    int longestValidParentheses(string s) :
        string reversed = s
        reverse(reversed.begin(), reversed.end())
        replace(reversed.begin(), reversed.end(), '(', '=')
        replace(reversed.begin(), reversed.end(), ')', '(')
        replace(reversed.begin(), reversed.end(), '=', ')')
        return max(longestValidParenthesesHelper(s), longestValidParenthesesHelper(reversed))
    int longestValidParenthesesHelper(string s) :
        int ret = 0
        int balance = 0
        int left = 0
        for (int i = 0 i < s.length() ++i) :
            if (s[i] == '(') :
                ++balance
             else :
                --balance
                if (balance == 0) :
                    ret = max(ret, i - left + 1)
                 else if (balance < 0) :
                    left = i + 1
                    balance = 0
        return ret
```
#### More concise solution
Stack solution from [Huahua](https://zxi.mytechroad.com/blog/stack/leetcode-32-longest-valid-parentheses/)
```python
// Author: Huahua
class Solution :
public:
  int longestValidParentheses(string s) :
    stack q
    int start = 0
    int ans = 0
    for (int i = 0i < s.length() i++) :
      if(s[i] == '(') :
        q.push(i)
       else :
        if (q.empty()) :
          start = i + 1
         else :
          int index = q.top() q.pop()
          ans = max(ans, q.empty() ? i - start + 1 : i - q.top())          
    return ans
```
DP solution from [Xishuashua](http://bangbingsyb.blogspot.com/2014/11/leetcode-longest-valid-parentheses.html)
```python
class Solution :
public:
    int longestValidParentheses(string s) :
        int n = s.size(), maxLen = 0
        vector dp(n+1,0)
        for(int i=1 i<=n i++) :
            int j = i-2-dp[i-1]
            if(s[i-1]=='(' || j<0 || s[j]==')') 
                dp[i] = 0
            else :
                dp[i] = dp[i-1]+2+dp[j]
                maxLen = max(maxLen, dp[i])
        return maxLen
```
# 720. Longest Word in Dictionary
* *Difficulty: Easy*
* *Topics: Hash Table, Trie*
* *Similar Questions:*
  * [Longest Word in Dictionary through Deleting](longest-word-in-dictionary-through-deleting.md)
  * [Implement Magic Dictionary](implement-magic-dictionary.md)
## Problem:
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words.  If there is more than one possible answer, return the longest word with the smallest lexicographical order.  If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
## Solutions:
```python
class Solution :
public:
    string longestWord(vector& words) :
        auto comparator = [](const string& word1, const string& word2) :
            if (word1.length() != word2.length()) :
                return word1.length() < word2.length()
            return word1 > word2
        sort(words.begin(), words.end(), comparator)
        unordered_set cache
        string ret
        for (int i = 0 i < words.size() ++i) :
            if (words[i].length() <= 1) :
                ret = words[i]
                cache.insert(words[i])
                continue
            string prefix = words[i].substr(0, words[i].length() - 1)
            if (cache.count(prefix)) :
                ret = words[i]
                cache.insert(words[i])
        return ret
```
# 235. Lowest Common Ancestor of a Binary Search Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor-of-a-binary-tree.md)
## Problem:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: &ldquoThe lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).&rdquo
Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Note:
	All of the nodes&#39 values will be unique.
	p and q are different and both values will exist in the BST.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) :
        if (root == nullptr)    return nullptr
        if (root == p || root == q) return root
        TreeNode* leftAncestor = lowestCommonAncestor(root->left, p, q)
        TreeNode* rightAncestor = lowestCommonAncestor(root->right, p, q)
        if (leftAncestor && rightAncestor)  return root
        if (leftAncestor)   return leftAncestor
        return rightAncestor
```
# 236. Lowest Common Ancestor of a Binary Tree
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Lowest Common Ancestor of a Binary Search Tree](lowest-common-ancestor-of-a-binary-search-tree.md)
## Problem:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: &ldquoThe lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).&rdquo
Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Note:
	All of the nodes&#39 values will be unique.
	p and q are different and both values will exist in the binary tree.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) :
        if (root == NULL)   return NULL
        if (root == p)  return p
        if (root == q)  return q
        TreeNode* leftRet = lowestCommonAncestor(root->left, p, q)
        TreeNode* rightRet = lowestCommonAncestor(root->right, p, q)
        if (leftRet == NULL && rightRet == NULL)    return NULL
        if (leftRet == NULL)    return rightRet
        if (rightRet == NULL)   return leftRet
        return root
```
# 146. LRU Cache
* *Difficulty: Medium*
* *Topics: Design*
* *Similar Questions:*
  * [LFU Cache](lfu-cache.md)
  * [Design In-Memory File System](design-in-memory-file-system.md)
  * [Design Compressed String Iterator](design-compressed-string-iterator.md)
## Problem:
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
Follow up:
Could you do both operations in O(1) time complexity?
Example:
LRUCache cache = new LRUCache( 2 /* capacity */ )
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       // returns 1
cache.put(3, 3)    // evicts key 2
cache.get(2)       // returns -1 (not found)
cache.put(4, 4)    // evicts key 1
cache.get(1)       // returns -1 (not found)
cache.get(3)       // returns 3
cache.get(4)       // returns 4
## Solutions:
```python
class LRUCache :
public:
    LRUCache(int capacity) :
        this->capacity = capacity
    int get(int key) :
        if (keyToNode.count(key) == 0) :
            return -1
        int val = keyToNode[key]->second
        cache.splice(cache.begin(), cache, keyToNode[key])
        return val
    void put(int key, int value) :
        if (keyToNode.count(key) > 0) :
            cache.splice(cache.begin(), cache, keyToNode[key])
            keyToNode[key]->second = value
            return
        cache.insert(cache.begin(), :key, value)
        keyToNode[key] = cache.begin()
        if (cache.size() > capacity) :
            int key = cache.back().first
            cache.pop_back()
            keyToNode.erase(key)
private:
    int capacity
    list> cache
    unordered_map>::iterator> keyToNode
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity)
 * int param_1 = obj->get(key)
 * obj->put(key,value)
 */
```
# 229. Majority Element II
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Majority Element](majority-element.md)
  * [Check If a Number Is Majority Element in a Sorted Array](check-if-a-number-is-majority-element-in-a-sorted-array.md)
## Problem:
Given an integer array of size n, find all elements that appear more than &lfloor n/3 &rfloor times.
Note: The algorithm should run in linear time and in O(1) space.
Example 1:
Input: [3,2,3]
Output: [3]
Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
## Solutions:
```python
class Solution :
public:
    vector majorityElement(vector& nums) :
        int majorityVal[2]
        int majorityCount[2] :0, 0
        for (auto& num : nums) : // pay attention to the order of the series of if statements
            if (majorityCount[0] == 0) :
                majorityVal[0] = num
                majorityCount[0] = 1
             else if (num == majorityVal[0]) :
                ++majorityCount[0]
             else if (majorityCount[1] == 0) :
                majorityVal[1] = num
                majorityCount[1] = 1
             else if (num == majorityVal[1]) :
                ++majorityCount[1]
                if (majorityCount[1] > majorityCount[0]) :
                    swap(majorityCount[0], majorityCount[1])
                    swap(majorityVal[0], majorityVal[1])
             else :
                --majorityCount[0]
                --majorityCount[1]
        majorityCount[0] = 0
        majorityCount[1] = 0
        for (auto& num : nums) :
            if (majorityVal[0] == num) :
                ++majorityCount[0]
             else if (majorityVal[1] == num) :
                ++majorityCount[1]
        vector ret
        if (majorityCount[0] > nums.size() / 3) :
            ret.push_back(majorityVal[0])
        if (majorityCount[1] > nums.size() / 3) :
            ret.push_back(majorityVal[1])
        return ret
```
# 169. Majority Element
* *Difficulty: Easy*
* *Topics: Array, Divide and Conquer, Bit Manipulation*
* *Similar Questions:*
  * [Majority Element II](majority-element-ii.md)
  * [Check If a Number Is Majority Element in a Sorted Array](check-if-a-number-is-majority-element-in-a-sorted-array.md)
## Problem:
Given an array of size n, find the majority element. The majority element is the element that appears more than &lfloor n/2 &rfloor times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
## Solutions:
```python
class Solution :
public:
    int majorityElement(vector& nums) :
        if (nums.size() == 0)   return -1
        int count = 0
        int majority = nums[0]
        for (auto num : nums) :
            if (num == majority) :
                ++count
             else :
                if (--count == 0) :
                    majority = num
                    count = 1
        return majority
```
# 695. Max Area of Island
* *Difficulty: Medium*
* *Topics: Array, Depth-first Search*
* *Similar Questions:*
  * [Number of Islands](number-of-islands.md)
  * [Island Perimeter](island-perimeter.md)
## Problem:
Given a non-empty 2D array grid of 0&#39s and 1&#39s, an island is a group of 1&#39s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
## Solutions:
```python
class Solution :
public:
    int maxAreaOfIsland(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        vector> visited(m, vector (n, false))
        int ret = 0
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] && !visited[i][j]) :
                    ret = max(ret, dfs(grid, visited, i, j))
        return ret
private:
    int dfs(const vector>& grid, vector>& visited, int row, int col) :
        int m = grid.size()
        int n = grid[0].size()
        if (row = m || col = n || !grid[row][col] || visited[row][col]) return 0
        visited[row][col] = true
        int ret = 1
        ret += dfs(grid, visited, row + 1, col)
        ret += dfs(grid, visited, row - 1, col)
        ret += dfs(grid, visited, row, col + 1)
        ret += dfs(grid, visited, row, col - 1)
        return ret
```
# 485. Max Consecutive Ones
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Max Consecutive Ones II](max-consecutive-ones-ii.md)
  * [Max Consecutive Ones III](max-consecutive-ones-iii.md)
## Problem:
Given a binary array, find the maximum number of consecutive 1s in this array.
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
## Solutions:
```python
class Solution :
public:
    int findMaxConsecutiveOnes(vector& nums) :
        int ret = 0
        int count = 0
        for (int i = 0 i < nums.size() ++i) :
            if (nums[i] == 1) :
                ++count
             else :
                ret = max(ret, count)
                count = 0
        ret = max(ret, count)
        return ret
```
# 149. Max Points on a Line
* *Difficulty: Hard*
* *Topics: Hash Table, Math*
* *Similar Questions:*
  * [Line Reflection](line-reflection.md)
## Problem:
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+-------------&gt
0  1  2  3  4
Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+-------------------&gt
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
## Solutions:
```python
class Solution :
public:
    int maxPoints(vector>& points) :
        int ret = 0
        for (int i = 0 i < points.size() ++i) :
            map, int> lines
            int verticleCount = 0 // dedicated 
            int horizonCount = 0 // dedicated
            int selfCount = 1
            for (int j = i + 1 j < points.size() ++j) :
                if (points[j][0] == points[i][0] && points[j][1] == points[i][1])   ++selfCount
                else if (points[j][0] == points[i][0])  ++verticleCount
                else if (points[j][1] == points[i][1])  ++horizonCount
                else :
                    ++lines[simplify(points[j][1] - points[i][1], points[j][0] - points[i][0])]
            int count = max(verticleCount, horizonCount)
            for (auto line : lines) :
                count = max(count, line.second)
            count += selfCount
            ret = max(ret, count)
        return ret
    pair simplify(int a, int b) :
        if (a < 0) : // every a should be not negtive
            a = -a
            b = -b
        int divisor = gcd(a, abs(b)) // both number should be positive
        return :a/divisor, b/divisor  // not times sign
    int gcd (int a, int b) :
        if (a < b)  return gcd(b, a)
        if (b == 0) return a           
        return gcd(b, a%b)
```
# 716. Max Stack
* *Difficulty: Easy*
* *Topics: Design*
* *Similar Questions:*
  * [Min Stack](min-stack.md)
## Problem:
Design a max stack that supports push, pop, top, peekMax and popMax.
push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack()
stack.push(5) 
stack.push(1)
stack.push(5)
stack.top() -> 5
stack.popMax() -> 5
stack.top() -> 1
stack.peekMax() -> 5
stack.pop() -> 1
stack.top() -> 5
Note:
-1e7 
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
## Solutions:
```python
class MaxStack :
public:
    /** initialize your data structure here. */
    MaxStack() :
    void push(int x) :
        data.push(x)
        if (maxs.empty() || x >= maxs.top()) :
            maxs.push(x)
    int pop() :
        int val = data.top()
        data.pop()
        if (val == maxs.top()) :
            maxs.pop()
        return val
    int top() :
        return data.top()
    int peekMax() :
        return maxs.top()
    int popMax() :
        int maxVal = maxs.top()
        stack buffer
        while (top() != maxVal) buffer.push(pop())
        pop()
        while (!buffer.empty()) :
            push(buffer.top())
            buffer.pop()
        return maxVal
private:
    stack data
    stack maxs
/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack()
 * obj->push(x)
 * int param_2 = obj->pop()
 * int param_3 = obj->top()
 * int param_4 = obj->peekMax()
 * int param_5 = obj->popMax()
 */
```
# 85. Maximal Rectangle
* *Difficulty: Hard*
* *Topics: Array, Hash Table, Dynamic Programming, Stack*
* *Similar Questions:*
  * [Largest Rectangle in Histogram](largest-rectangle-in-histogram.md)
  * [Maximal Square](maximal-square.md)
## Problem:
Given a 2D binary matrix filled with 0&#39s and 1&#39s, find the largest rectangle containing only 1&#39s and return its area.
Example:
Input:
[
  [&quot1&quot,&quot0&quot,&quot1&quot,&quot0&quot,&quot0&quot],
  [&quot1&quot,&quot0&quot,&quot1&quot,&quot1&quot,&quot1&quot],
  [&quot1&quot,&quot1&quot,&quot1&quot,&quot1&quot,&quot1&quot],
  [&quot1&quot,&quot0&quot,&quot0&quot,&quot1&quot,&quot0&quot]
]
Output: 6
## Solutions:
```python
class Solution :
public:
    int maximalRectangle(vector>& matrix) :
        int m = matrix.size()
        if (m == 0) return 0
        int n = matrix[0].size()
        if (n == 0) return 0
        vector heights (n + 1, 0)
        int ret = 0
        for (int row = 0 row < m ++row) :
            for (int col = 0 col < n ++col) :
                if (matrix[row][col] == '0') :
                    heights[col] = 0
                 else :
                    ++heights[col]
            ret = max(ret, barMaxArea(heights))
        return ret
    int barMaxArea(vector& heights) :
        heights.back() = 0
        stack stk
        int area = 0
        for (int i = 0 i < heights.size() ++i) :
            while (!stk.empty() && heights[stk.top()] > heights[i]) :
                int topIndex = stk.top()
                stk.pop()
               area = max(area, heights[topIndex] * (i - (stk.empty() ? 0 : (stk.top() + 1))))
            stk.push(i)
        return area
```
# 221. Maximal Square
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Maximal Rectangle](maximal-rectangle.md)
  * [Largest Plus Sign](largest-plus-sign.md)
## Problem:
Given a 2D binary matrix filled with 0&#39s and 1&#39s, find the largest square containing only 1&#39s and return its area.
Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
## Solutions:
```python
class Solution :
public:
    int maximalSquare(vector>& matrix) :
        int m = matrix.size()
        if (m == 0) return 0
        int n = matrix[0].size()
        if (n == 0) return 0
        vector> dp(m, vector (n, 0))
        for (int i = 0 i < m ++i) :
            dp[i][0] = matrix[i][0] - '0'
        for (int j = 0 j < n ++j) :
            dp[0][j] = matrix[0][j] - '0'
        for (int i = 1 i < m ++i) :
            for (int j = 1 j < n ++j) :
                if (matrix[i][j] != '0') :
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
        int ret = 0
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                ret = max(ret, dp[i][j])
        return ret * ret
```
# 104. Maximum Depth of Binary Tree
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Balanced Binary Tree](balanced-binary-tree.md)
  * [Minimum Depth of Binary Tree](minimum-depth-of-binary-tree.md)
  * [Maximum Depth of N-ary Tree](maximum-depth-of-n-ary-tree.md)
## Problem:
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int maxDepth(TreeNode* root) :
        if (root == NULL)   return 0
        return 1 + std::max(maxDepth(root->left), maxDepth(root->right))
```
# 774. Maximum Depth of N-ary Tree
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search, Breadth-first Search*
* *Similar Questions:*
  * [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md)
## Problem:
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
For example, given a 3-ary tree:
We should return its max depth, which is 3.
Note:
	The depth of the tree is at most 1000.
	The total number of nodes is at most 5000.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    vector children
    Node() :
    Node(int _val, vector _children) :
        val = _val
        children = _children
*/
class Solution :
public:
    int maxDepth(Node* root) :
        if (root == nullptr)    return 0
        int ret = 0
        for (auto& child : root->children) :
            ret = max(ret, maxDepth(child))
        return 1 + ret
```
# 624. Maximum Distance in Arrays
* *Difficulty: Easy*
* *Topics: Array, Hash Table*
* *Similar Questions:*
## Problem:
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.
Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
## Solutions:
```python
class Solution :
public:
    int maxDistance(vector>& arrays) :
        int m = arrays.size()
        if (m == 0) return 0
        int firstVal = INT_MIN
        int secondVal = INT_MIN
        int firstIndex = -1
        int secondIndex = -1
        for (int i = 0 i < m ++i) :
            if (arrays[i].back() >= firstVal) :
                secondVal = firstVal
                secondIndex = firstIndex
                firstVal = arrays[i].back()
                firstIndex = i
             else if (arrays[i].back() > secondVal) :
                secondVal = arrays[i].back()
                secondIndex = i
        int ret = 0
        for (int i = 0 i < m ++i) :
            if (i == firstIndex) :
                ret = max(ret, secondVal - arrays[i][0])
             else :
                ret = max(ret, firstVal - arrays[i][0])
        return ret
```
# 164. Maximum Gap
* *Difficulty: Hard*
* *Topics: Sort*
* *Similar Questions:*
## Problem:
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Return 0 if the array contains less than 2 elements.
Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:
	You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
	Try to solve it in linear time/space.
## Solutions:
```python
class Solution :
public:
    int maximumGap(vector& nums) :
        if (nums.size() < 2)    return 0
        int n = nums.size()
        int minElement = INT_MAX
        int maxElement = INT_MIN
        for (auto num : nums) :
            minElement = min(minElement, num)
            maxElement = max(maxElement, num)
        int bucketSize = (maxElement - minElement + 1 + n - 1 ) / n
        vector bucketMax (n, INT_MIN)
        vector bucketMin (n, INT_MAX)
        for (auto num : nums) :
            int index = (num - minElement) / bucketSize
            bucketMax[index] = max(bucketMax[index], num)
            bucketMin[index] = min(bucketMin[index], num)
        int max_gap = 0
        int prev_max = bucketMax[0]
        for (int i = 1 i < n ++i) :
            if (bucketMin[i] != INT_MAX) :
                max_gap = max(max_gap, bucketMin[i] - prev_max)
                prev_max = bucketMax[i]
        return max_gap
```
# 1116. Maximum Level Sum of a Binary Tree
* *Difficulty: Medium*
* *Topics: Graph*
* *Similar Questions:*
## Problem:
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
Example 1:
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Note:
	The number of nodes in the given tree is between 1 and 10^4.
	-10^5 &lt= node.val &lt= 10^5
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int maxLevelSum(TreeNode* root) :
        if (root == nullptr)    return 0
        unordered_map sums
        helper(root, 1, sums)
        int maxSum = INT_MIN
        int maxLevel = -1
        for (auto& entry : sums) :
            if (entry.second > maxSum) :
                maxSum = entry.second
                maxLevel = entry.first
             else if (entry.second == maxSum && entry.first < maxLevel) :
                maxLevel = entry.first
        return maxLevel
private:
    void helper(TreeNode* root, int level, unordered_map& sums) :
        sums[level] += root->val
        if (root->left) :
            helper(root->left, level + 1, sums)
        if (root->right) :
            helper(root->right, level + 1, sums)
```
# 1297. Maximum Number of Balloons
* *Difficulty: Easy*
* *Topics: Hash Table, String*
* *Similar Questions:*
## Problem:
Given a string text, you want to use the characters of text to form as many instances of the word &quotballoon&quot as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
Example 1:
Input: text = &quotnlaebolko&quot
Output: 1
Example 2:
Input: text = &quotloonbalxballpoon&quot
Output: 2
Example 3:
Input: text = &quotleetcode&quot
Output: 0
Constraints:
	1 &lt= text.length &lt= 10^4
	text consists of lower case English letters only.
## Solutions:
```python
class Solution :
public:
    int maxNumberOfBalloons(string text) :
        int charCount[26] = :0
        for (auto& c : text) :
            ++charCount[c - 'a']
        int ret = INT_MAX
        string target = "baon"
        for (auto& c : target) :
            ret = min(ret, charCount[c - 'a'])
        ret = min(ret, charCount['l' - 'a'] / 2)
        ret = min(ret, charCount['o' - 'a'] / 2)
        return ret == INT_MAX ? 0 : ret
```
# 628. Maximum Product of Three Numbers
* *Difficulty: Easy*
* *Topics: Array, Math*
* *Similar Questions:*
  * [Maximum Product Subarray](maximum-product-subarray.md)
## Problem:
Given an integer array, find three numbers whose product is maximum and output the maximum product.
Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
	The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
	Multiplication of any three numbers in the input won&#39t exceed the range of 32-bit signed integer.
## Solutions:
```python
class Solution :
public:
    int maximumProduct(vector& nums) :
        vector pos
        vector neg
        for (auto& num : nums) :
            if (num >= 0) :
                pos.push_back(num)
             else :
                neg.push_back(num)
        sort(pos.begin(), pos.end())
        sort(neg.begin(), neg.end())
        int ret = INT_MIN
        if (neg.size() >= 3) :
            ret = max(ret, neg[neg.size() - 1] * neg[neg.size() - 2] * neg[neg.size() - 3])
        if (neg.size() >= 2 && pos.size() >= 1) :
            ret = max(ret, neg[0] * neg[1] * pos.back())
        if (neg.size() >=1 && pos.size() >= 2) :
            ret = max(ret, neg.back() * pos[0] * pos[1])
        if (pos.size() >= 3) :
            ret = max(ret, pos[pos.size() - 1] * pos[pos.size() - 2] * pos[pos.size() - 3])
        return ret
```
# 318. Maximum Product of Word Lengths
* *Difficulty: Medium*
* *Topics: Bit Manipulation*
* *Similar Questions:*
## Problem:
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
Example 1:
Input: [&quotabcw&quot,&quotbaz&quot,&quotfoo&quot,&quotbar&quot,&quotxtfn&quot,&quotabcdef&quot]
Output: 16 
Explanation: The two words can be &quotabcw&quot, &quotxtfn&quot.
Example 2:
Input: [&quota&quot,&quotab&quot,&quotabc&quot,&quotd&quot,&quotcd&quot,&quotbcd&quot,&quotabcd&quot]
Output: 4 
Explanation: The two words can be &quotab&quot, &quotcd&quot.
Example 3:
Input: [&quota&quot,&quotaa&quot,&quotaaa&quot,&quotaaaa&quot]
Output: 0 
Explanation: No such pair of words.
## Solutions:
```python
class Solution :
public:
    int maxProduct(vector& words) :
        unordered_map indexToBit
        for (int i = 0 i < words.size() ++i) :
            int bitmap = getBitMap(words[i])
            indexToBit[i] = bitmap
        int ret = 0
        for (int i = 0 i < words.size() ++i) :
            for (int j = i + 1 j < words.size() ++j) :
                if ((indexToBit[i] & indexToBit[j]) == 0) :
                    ret = max(ret, (int) (words[i].length() * words[j].length()))
        return ret
private:
    int getBitMap(const string& word) :
        int bitmap = 0
        for (auto& c : word) :
            bitmap |= 1 << (c - 'a')
        return bitmap
```
# 152. Maximum Product Subarray
* *Difficulty: Medium*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
  * [Maximum Subarray](maximum-subarray.md)
  * [House Robber](house-robber.md)
  * [Product of Array Except Self](product-of-array-except-self.md)
  * [Maximum Product of Three Numbers](maximum-product-of-three-numbers.md)
  * [Subarray Product Less Than K](subarray-product-less-than-k.md)
## Problem:
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
## Solutions:
```python
class Solution :
public:
    int maxProduct(vector& nums) :
        int n = nums.size()
        if (n == 0) return 0
        vector maxValue (n, 0)
        vector minValue (n, 0)
        maxValue[0] = nums[0]
        minValue[0] = nums[0]
        for (int i = 1 i < nums.size() ++i) :
            maxValue[i] = max(nums[i], max(minValue[i-1] * nums[i], maxValue[i-1] * nums[i]))
            minValue[i] = min(nums[i], min(minValue[i-1] * nums[i], maxValue[i-1] * nums[i]))
        int ret = maxValue[0]
        for (int i = 1 i < nums.size() ++i) :
            ret = max(ret, maxValue[i])
        return ret
```
# 53. Maximum Subarray
* *Difficulty: Easy*
* *Topics: Array, Divide and Conquer, Dynamic Programming*
* *Similar Questions:*
  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)
  * [Maximum Product Subarray](maximum-product-subarray.md)
  * [Degree of an Array](degree-of-an-array.md)
  * [Longest Turbulent Subarray](longest-turbulent-subarray.md)
## Problem:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
## Solutions:
```python
class Solution :
public:
    int maxSubArray(vector& nums) :
        int suffix = 0
        int ret = INT_MIN
        int sum = 0
        for (auto num : nums) :
            sum += num
            ret = max(ret, sum - suffix)
            suffix = min(suffix, sum)
        return ret
```
# 4. Median of Two Sorted Arrays
* *Difficulty: Hard*
* *Topics: Array, Binary Search, Divide and Conquer*
* *Similar Questions:*
## Problem:
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
## Solutions:
```python
class Solution :
public:
    double findMedianSortedArrays(vector& nums1, vector& nums2) :
        int n1 = nums1.size()
        int n2 = nums2.size()
        int n = n1 + n2
        if (n % 2 == 0) :
            return (smallK(n/2, nums1, 0, n1 - 1, nums2, 0, n2 - 1) + smallK(n/2 + 1, nums1, 0, n1 - 1, nums2, 0, n2 - 1)) / double(2)
         else :
            return smallK(n/2 + 1, nums1, 0, n1 - 1, nums2, 0, n2 - 1)
    // k starting from 1
    int smallK(int k, vector& nums1, int left1, int right1, vector& nums2, int left2, int right2) :
        if (left1 > right1) return nums2[left2 + k - 1]
        if (left2 > right2) return nums1[left1 + k - 1]
        if (k == 1) :
            return min(nums1[left1], nums2[left2])
        if (k/2 > right1 - left1 + 1) :
            return smallK(k - k/2, nums1, left1, right1, nums2, left2 + k/2, right2)
        if (k/2 > right2 - left2 + 1) :
            return smallK(k - k/2, nums1, left1 + k/2, right1, nums2, left2, right2)
        if (nums1[left1 + k/2 - 1] < nums2[left2 + k/2 - 1]) :
            return smallK(k - k/2, nums1, left1 + k/2, right1, nums2, left2, right2)
         else :
            return smallK(k - k/2, nums1, left1, right1, nums2, left2 + k/2, right2)
```
## Common pitfalls
It is necessary to understand which is halved for binary search. It is `k`, not indexes. 
# 253. Meeting Rooms II
* *Difficulty: Medium*
* *Topics: Heap, Greedy, Sort*
* *Similar Questions:*
  * [Merge Intervals](merge-intervals.md)
  * [Meeting Rooms](meeting-rooms.md)
  * [Minimum Number of Arrows to Burst Balloons](minimum-number-of-arrows-to-burst-balloons.md)
  * [Car Pooling](car-pooling.md)
## Problem:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si &lt ei), find the minimum number of conference rooms required.
Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:
Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
## Solutions:
```python
class Solution :
public:
    struct MeetingEvent :
        int time
        bool start
        MeetingEvent(int time, bool start) :
            this->time = time
            this->start = start
        bool operator< (const MeetingEvent& event) const :
            if (this->time == event.time) :
                return !(this->start)
             else :
                return this->time < event.time
    int minMeetingRooms(vector>& intervals) :
        vector events
        for (auto& interval : intervals) :
            events.push_back(:interval[0], true)
            events.push_back(:interval[1], false)
        sort(events.begin(), events.end())
        int count = 0
        int ret = 0
        for (int i = 0 i < events.size() ++i) :
            if (events[i].start) :
                ++count
                ret = max(ret, count)
             else :
                --count
        return ret
```
# 252. Meeting Rooms
* *Difficulty: Easy*
* *Topics: Sort*
* *Similar Questions:*
  * [Merge Intervals](merge-intervals.md)
  * [Meeting Rooms II](meeting-rooms-ii.md)
## Problem:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si &lt ei), determine if a person could attend all meetings.
Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
## Solutions:
```python
class Solution :
public:
    bool canAttendMeetings(vector>& intervals) :
        sort(intervals.begin(), intervals.end(), [](vector& lhs, vector& rhs) :
            return lhs[0] < rhs[0]
        )
        for (int i = 1 i < intervals.size() ++i) :
            if (intervals[i][0] < intervals[i-1][1])    return false
        return true
```
# 56. Merge Intervals
* *Difficulty: Medium*
* *Topics: Array, Sort*
* *Similar Questions:*
  * [Insert Interval](insert-interval.md)
  * [Meeting Rooms](meeting-rooms.md)
  * [Meeting Rooms II](meeting-rooms-ii.md)
  * [Teemo Attacking](teemo-attacking.md)
  * [Add Bold Tag in String](add-bold-tag-in-string.md)
  * [Range Module](range-module.md)
  * [Employee Free Time](employee-free-time.md)
  * [Partition Labels](partition-labels.md)
  * [Interval List Intersections](interval-list-intersections.md)
## Problem:
Given a collection of intervals, merge all overlapping intervals.
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
## Solutions:
```python
class Solution :
public:
    vector> merge(vector>& intervals) :
        vector> ret
        sort(intervals.begin(), intervals.end()) // be careful about vector comparison
        for (auto& interval : intervals) :
            if (ret.empty() || ret.back()[1] < interval[0]) :
                ret.push_back(interval)
             else :
                ret.back()[1] = max(ret.back()[1], interval[1])
        return ret
```
# 23. Merge k Sorted Lists
* *Difficulty: Hard*
* *Topics: Linked List, Divide and Conquer, Heap*
* *Similar Questions:*
  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)
  * [Ugly Number II](ugly-number-ii.md)
## Problem:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Example:
Input:
[
  1-&gt4-&gt5,
  1-&gt3-&gt4,
  2-&gt6
]
Output: 1-&gt1-&gt2-&gt3-&gt4-&gt4-&gt5-&gt6
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    struct NodeInfo :
        ListNode* node
        int srcList
        NodeInfo(ListNode* node, int srcList) :
            this->node = node
            this->srcList = srcList
        bool operator<(const NodeInfo& another) const :
            return this->node->val val
         bool operator>(const NodeInfo& another) const :
            return this->node->val > another.node->val
    ListNode* mergeKLists(vector& lists) :
        int n = lists.size()
        priority_queue, greater> pq
        ListNode* dummyHead = new ListNode(0)
        ListNode* tail = dummyHead
        for (int i = 0 i < n ++i) :
            if (lists[i] != NULL) :
                pq.push(:lists[i], i)
                lists[i] = lists[i]->next
        while (!pq.empty()) :
            NodeInfo nodeInfo = pq.top() pq.pop()
            int srcList = nodeInfo.srcList
            ListNode* node = nodeInfo.node
            tail->next = node
            tail = node
            if (lists[srcList] != NULL) :
                pq.push(:lists[srcList], srcList)
                lists[srcList] = lists[srcList]->next
        return dummyHead->next
```
# 88. Merge Sorted Array
* *Difficulty: Easy*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)
  * [Squares of a Sorted Array](squares-of-a-sorted-array.md)
  * [Interval List Intersections](interval-list-intersections.md)
## Problem:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
	The number of elements initialized in nums1 and nums2 are m and n respectively.
	You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
## Solutions:
```python
class Solution :
public:
    void merge(vector& nums1, int m, vector& nums2, int n) :
        nums1.resize(m + n)
        int cur = m + n - 1
        int i1 = m - 1
        int i2 = n - 1
        while (i1 >= 0 || i2 >= 0) :
            if (i1 < 0) :
                nums1[cur--] = nums2[i2--]
             else if (i2 < 0) :
                break
             else :
                if (nums1[i1] >= nums2[i2]) :
                    nums1[cur--] = nums1[i1--]
                 else :
                    nums1[cur--] = nums2[i2--]
```
# 617. Merge Two Binary Trees
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) :
        if (t1 && t2) :
            TreeNode* root = new TreeNode(t1->val + t2->val)
            root->left = mergeTrees(t1->left, t2->left)
            root->right = mergeTrees(t1->right, t2->right)
            return root
        if (!t1 && !t2) return nullptr
        if (t1) :
            return t1
         else :
            return t2
```
# 21. Merge Two Sorted Lists
* *Difficulty: Easy*
* *Topics: Linked List*
* *Similar Questions:*
  * [Merge k Sorted Lists](merge-k-sorted-lists.md)
  * [Merge Sorted Array](merge-sorted-array.md)
  * [Sort List](sort-list.md)
  * [Shortest Word Distance II](shortest-word-distance-ii.md)
## Problem:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) :
        ListNode* head = NULL
        ListNode** cur = &head
        while (l1 != NULL || l2 != NULL) :
            if (l1 == NULL) :
                *cur = l2
                l2 = l2 -> next
            else if (l2 == NULL) :
                *cur = l1
                l1 = l1 ->next
            else : 
               if (l1->val val) :
                    *cur = l1
                    l1 = l1->next
                 else :
                    *cur = l2
                    l2 = l2->next
            cur = &((*cur)->next)
        return head
```
# 908. Middle of the Linked List
* *Difficulty: Easy*
* *Topics: Linked List*
* *Similar Questions:*
## Problem:
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge&#39s serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
Note:
	The number of nodes in the given list will be between 1 and 100.
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* middleNode(ListNode* head) :
        ListNode* fast = head
        ListNode* slow = head
        while (fast && fast->next) : // it is tricky!
            fast = fast->next->next
            slow = slow->next
        return slow
```
# 747. Min Cost Climbing Stairs
* *Difficulty: Easy*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
  * [Climbing Stairs](climbing-stairs.md)
## Problem:
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
## Solutions:
```python
class Solution :
public:
    int minCostClimbingStairs(vector& cost) :
        cost.push_back(0)
        int n = cost.size()
        vector dp(n, INT_MAX)
        dp[0] = 0
        dp[1] = 0
        for (int i = 2 i < n ++i) :
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[n-1]
```
# 155. Min Stack
* *Difficulty: Easy*
* *Topics: Stack, Design*
* *Similar Questions:*
  * [Sliding Window Maximum](sliding-window-maximum.md)
  * [Max Stack](max-stack.md)
## Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
	push(x) -- Push element x onto stack.
	pop() -- Removes the element on top of the stack.
	top() -- Get the top element.
	getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   --&gt Returns -3.
minStack.pop()
minStack.top()      --&gt Returns 0.
minStack.getMin()   --&gt Returns -2.
## Solutions:
```python
class MinStack :
public:
    /** initialize your data structure here. */
    MinStack() :
    void push(int x) :
        if (mins.empty() || mins.top() >= x) :
            mins.push(x)
        stk.push(x)
    void pop() :
        int num = stk.top() stk.pop()
        if (!mins.empty() && num == mins.top()) :
            mins.pop()
    int top() :
        return stk.top()
    int getMin() :
        if (mins.empty()) :
            return -1
        return mins.top()
private:
    stack stk
    stack mins
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack()
 * obj->push(x)
 * obj->pop()
 * int param_3 = obj->top()
 * int param_4 = obj->getMin()
 */
```
# 529. Minesweeper
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search*
* *Similar Questions:*
## Problem:
Let&#39s play the minesweeper game (Wikipedia, online game)!
You are given a 2D char matrix representing the game board. &#39M&#39 represents an unrevealed mine, &#39E&#39 represents an unrevealed empty square, &#39B&#39 represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit (&#391&#39 to &#398&#39) represents how many mines are adjacent to this revealed square, and finally &#39X&#39 represents a revealed mine.
Now given the next click position (row and column indices) among all the unrevealed squares (&#39M&#39 or &#39E&#39), return the board after revealing this position according to the following rules:
	If a mine (&#39M&#39) is revealed, then the game is over - change it to &#39X&#39.
	If an empty square (&#39E&#39) with no adjacent mines is revealed, then change it to revealed blank (&#39B&#39) and all of its adjacent unrevealed squares should be revealed recursively.
	If an empty square (&#39E&#39) with at least one adjacent mine is revealed, then change it to a digit (&#391&#39 to &#398&#39) representing the number of adjacent mines.
	Return the board when no more squares will be revealed.
Example 1:
Input: 
[[&#39E&#39, &#39E&#39, &#39E&#39, &#39E&#39, &#39E&#39],
 [&#39E&#39, &#39E&#39, &#39M&#39, &#39E&#39, &#39E&#39],
 [&#39E&#39, &#39E&#39, &#39E&#39, &#39E&#39, &#39E&#39],
 [&#39E&#39, &#39E&#39, &#39E&#39, &#39E&#39, &#39E&#39]]
Click : [3,0]
Output: 
[[&#39B&#39, &#391&#39, &#39E&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#391&#39, &#39M&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#391&#39, &#391&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#39B&#39, &#39B&#39, &#39B&#39, &#39B&#39]]
Explanation:
Example 2:
Input: 
[[&#39B&#39, &#391&#39, &#39E&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#391&#39, &#39M&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#391&#39, &#391&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#39B&#39, &#39B&#39, &#39B&#39, &#39B&#39]]
Click : [1,2]
Output: 
[[&#39B&#39, &#391&#39, &#39E&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#391&#39, &#39X&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#391&#39, &#391&#39, &#391&#39, &#39B&#39],
 [&#39B&#39, &#39B&#39, &#39B&#39, &#39B&#39, &#39B&#39]]
Explanation:
Note:
	The range of the input matrix&#39s height and width is [1,50].
	The click position will only be an unrevealed square (&#39M&#39 or &#39E&#39), which also means the input board contains at least one clickable square.
	The input board won&#39t be a stage when game is over (some mines have been revealed).
	For simplicity, not mentioned rules should be ignored in this problem. For example, you don&#39t need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
## Solutions:
```python
class Solution :
public:
    vector> updateBoard(vector>& board, vector& click) :
        int m = board.size()
        if (m == 0) return :
        int n = board[0].size()
        if (n == 0) return :
        if (board[click[0]][click[1]] == 'M') :
            board[click[0]][click[1]] = 'X'
            return board
        dfs(board, click[0], click[1])
        return board
private:
    void dfs(vector>& board, int row, int col) :
        int m = board.size()
        int n = board[0].size()
        if (row = m || col = n || isdigit(board[row][col]) || board[row][col] == 'B' || board[row][col] == 'M') return
        else :
            int count = 0
            for (int i = -1 i <= 1 ++i) :
                for (int j = -1 j <= 1 ++j) :
                    if (i == 0 && j == 0)   continue
                    if (row + i = m || col + j = n) continue
                    count += (board[row+i][col+j] == 'M' ? 1 : 0)
            if (count > 0) :
                board[row][col] = '0' + count
             else :
                board[row][col] = 'B'
                for (int i = -1 i <= 1 ++i) :
                    for (int j = -1 j <= 1 ++j) :
                        if (i == 0 && j == 0)   continue
                        if (row + i = m || col + j = n) continue
                        if (board[row+i][col+j] != 'M') :
                            dfs(board, row+i, col+j)
```
# 385. Mini Parser
* *Difficulty: Medium*
* *Topics: String, Stack*
* *Similar Questions:*
  * [Flatten Nested List Iterator](flatten-nested-list-iterator.md)
  * [Ternary Expression Parser](ternary-expression-parser.md)
  * [Remove Comments](remove-comments.md)
## Problem:
Given a nested list of integers represented as a string, implement a parser to deserialize it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Note:
You may assume that the string is well-formed:
String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:
Given s = "324",
You should return a NestedInteger object which contains a single integer 324.
Example 2:
Given s = "[123,[456,[789]]]",
Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
## Solutions:
```python
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger :
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger()
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value)
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector &getList() const
 * 
 */
class Solution :
public:
    NestedInteger deserialize(string s) :
        int pos = 0
        return helper(s, pos)
    NestedInteger base(string&s, int& pos) :
        int sign = 1
        if (s[pos] == '-') :
            sign = -1
            ++pos
        int val = s[pos] - '0'
        while (pos + 1 < s.length() && isdigit(s[pos + 1])) :
            ++pos
            val = 10 * val + (s[pos] - '0')    
        return NestedInteger(val * sign)
    NestedInteger helper(string& s, int& pos) :
        NestedInteger nestedInteger
        if (pos == s.length())  return NestedInteger()
        if (s[pos] == ']')  return NestedInteger()
        NestedInteger temp
        for ( pos < s.length() ++pos) :
            char c = s[pos]
            if (isdigit(c) || c == '-') :
                temp = base(s, pos)
                continue
            if (c == ',') :
                nestedInteger.add(temp)
                continue
            if (c == ']') :
                nestedInteger.add(temp)
                return nestedInteger
            if (c == '[') :
                temp = helper(s, ++pos)
                continue
        return temp
```
# 530. Minimum Absolute Difference in BST
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [K-diff Pairs in an Array](k-diff-pairs-in-an-array.md)
## Problem:
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
Example:
Input:
   1
    \
     3
    /
   2
Output:
1
Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int getMinimumDifference(TreeNode* root) :
        vector last
        int ret = INT_MAX
        helper(root, last, ret)
        return ret
private:
    void helper(TreeNode* root, vector& last, int& ret) :
        if (root == nullptr)    return
        helper(root->left, last, ret)
        if (last.size() == 0) :
            last.push_back(root->val)
         else :
            ret = min(ret, abs(last.back() - root->val))
            last.back() = root->val
        helper(root->right, last, ret)
```
# 1306. Minimum Absolute Difference
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
	a, b are from arr
	a &lt b
	b - a equals to the minimum absolute difference of any two elements in arr
Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
Constraints:
	2 &lt= arr.length &lt= 10^5
	-10^6 &lt= arr[i] &lt= 10^6
## Solutions:
```python
class Solution :
public:
    vector> minimumAbsDifference(vector& arr) :
        int n = arr.size()
        if (n <= 1) return :
        sort(arr.begin(), arr.end())
        vector> ret
        int minDiff = INT_MAX
        for (int i = 1 i < n ++i) :
            if (abs(arr[i] - arr[i-1]) == minDiff) :
                ret.push_back(:arr[i-1], arr[i])
             else if (abs(arr[i] - arr[i-1]) < minDiff) :
                minDiff = abs(arr[i] - arr[i-1])
                ret = ::arr[i-1], arr[i]
        return ret
```
# 111. Minimum Depth of Binary Tree
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search, Breadth-first Search*
* *Similar Questions:*
  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)
  * [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md)
## Problem:
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int minDepth(TreeNode* root) :
        if (root == nullptr)    return 0
        int ret = INT_MAX
        if (root->left) :
            ret = min(ret, 1 + minDepth(root->left))
        if (root->right) :
            ret = min(ret, 1 + minDepth(root->right))
        return ret == INT_MAX ? 1 : ret
```
# 310. Minimum Height Trees
* *Difficulty: Medium*
* *Topics: Breadth-first Search, Graph*
* *Similar Questions:*
  * [Course Schedule](course-schedule.md)
  * [Course Schedule II](course-schedule-ii.md)
## Problem:
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Example 1 :
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
        0
        |
        1
       / \
      2   3 
Output: [1]
Example 2 :
Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
     0  1  2
      \ | /
        3
        |
        4
        |
        5 
Output: [3, 4]
Note:
	According to the definition of tree on Wikipedia: &ldquoa tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.&rdquo
	The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
## Solutions:
```python
class Solution :
public:
    vector findMinHeightTrees(int n, vector>& edges) :
        if (n == 1) return :0 // this check is important
        unordered_map> neighbors
        unordered_map degree
        for (auto& edge : edges) :
            int node1 = edge[0]
            int node2 = edge[1]
            neighbors[node1].push_back(node2)
            neighbors[node2].push_back(node1)
            ++degree[node1]
            ++degree[node2]
        vector ret
        queue q
        for (auto it = degree.begin() it != degree.end() ++it) :
            if (it->second == 1) :
                q.push(it->first)
        while(!q.empty()) :
            int size = q.size()
            ret.clear()
            for (int i = 0 i < size ++i) :
                int node = q.front() q.pop()
                //cout << node << endl
                ret.push_back(node)
                for (auto& neighbor : neighbors[node]) :
                    if (--degree[neighbor] == 1) :
                        q.push(neighbor)
        return ret
```
# 599. Minimum Index Sum of Two Lists
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Intersection of Two Linked Lists](intersection-of-two-linked-lists.md)
## Problem:
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings. 
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
## Solutions:
```python
class Solution :
public:
    vector findRestaurant(vector& list1, vector& list2) :
        unordered_map restaurantIndex
        for (int i = 0 i < list1.size() ++i) :
            restaurantIndex[list1[i]] = i
        int minSum = INT_MAX
        vector ret
        for (int i = 0 i < list2.size() ++i) :
            if (restaurantIndex.count(list2[i]) > 0) :
                int index1 = restaurantIndex[list2[i]]
                if (i + index1 < minSum) :
                    minSum = i + index1
                    ret = :list2[i]
                 else if (i + index1 == minSum) :
                    ret.push_back(list2[i])
        return ret
```
# 1142. Minimum Knight Moves
* *Difficulty: Medium*
* *Topics: Breadth-first Search*
* *Similar Questions:*
## Problem:
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.
Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] &rarr [2, 1]
Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] &rarr [2, 1] &rarr [4, 2] &rarr [3, 4] &rarr [5, 5]
Constraints:
	|x| + |y| &lt= 300
## Solutions:
```python
class Solution :
public:
    int minKnightMoves(int x, int y) :
        set> visited
        queue> q
        q.push(:0, 0)
        int level = 0
        while (!q.empty()) :
            int size = q.size()
            for (int n = 0 n < size ++n) :
                auto pos = q.front() q.pop()
                if (abs(pos.first) == abs(x) && abs(pos.second) == abs(y))  return level
                if (visited.count(:abs(pos.first), abs(pos.second))) continue
                visited.insert(:abs(pos.first), abs(pos.second))
                for (int i = 0 i < 8 ++i) :
                    q.push(:pos.first + directions[i][0], pos.second + directions[i][1])
            ++level
        return -1
private:
    int directions[8][2] = :
        :1, 2, 
        :2, 1,
        :2, -1,
        :1, -2,
        :-1, -2,
        :-2, -1,
        :-2, 1,
        :-1, 2
```
# 64. Minimum Path Sum
* *Difficulty: Medium*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
  * [Unique Paths](unique-paths.md)
  * [Dungeon Game](dungeon-game.md)
  * [Cherry Pickup](cherry-pickup.md)
## Problem:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1&rarr3&rarr1&rarr1&rarr1 minimizes the sum.
## Solutions:
```python
class Solution :
public:
    int minPathSum(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        vector> dp(m, vector(n, 0))
        dp[0][0] = grid[0][0]
        for (int i = 1 i < m ++i) :
            dp[i][0] += grid[i][0] + dp[i-1][0]
        for (int j = 1 j < n ++j) :
            dp[0][j] += grid[0][j] + dp[0][j-1]
        for (int i = 1 i < m ++i) :
            for (int j = 1 j < n ++j) :
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
```
# 209. Minimum Size Subarray Sum
* *Difficulty: Medium*
* *Topics: Array, Two Pointers, Binary Search*
* *Similar Questions:*
  * [Minimum Window Substring](minimum-window-substring.md)
  * [Maximum Size Subarray Sum Equals k](maximum-size-subarray-sum-equals-k.md)
  * [Maximum Length of Repeated Subarray](maximum-length-of-repeated-subarray.md)
## Problem:
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum &ge s. If there isn&#39t one, return 0 instead.
Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
## Solutions:
```python
class Solution :
public:
    int minSubArrayLen(int s, vector& nums) :
        int sum = 0
        int left = 0
        int len = INT_MAX
        for (int right = 0 right < nums.size() ++right) :
            sum += nums[right]
            while (left = s) :
                len = min(len, right - left + 1)
                sum -= nums[left]
                ++left
        return len == INT_MAX ? 0 : len
```
# 1167. Minimum Time to Build Blocks
* *Difficulty: Hard*
* *Topics: Math, Dynamic Programming*
* *Similar Questions:*
## Problem:
You are given a list of blocks, where blocks[i] = t means that the i-th block needs t units of time to be built. A block can only be built by exactly one worker.
A worker can either split into two workers (number of workers increases by one) or build a block then go home. Both decisions cost some time.
The time cost of spliting one worker into two workers is given as an integer split. Note that if two workers split at the same time, they split in parallel so the cost would be split.
Output the minimum time needed to build all blocks.
Initially, there is only one worker.
Example 1:
Input: blocks = [1], split = 1
Output: 1
Explanation: We use 1 worker to build 1 block in 1 time unit.
Example 2:
Input: blocks = [1,2], split = 5
Output: 7
Explanation: We split the worker into 2 workers in 5 time units then assign each of them to a block so the cost is 5 + max(1, 2) = 7.
Example 3:
Input: blocks = [1,2,3], split = 1
Output: 4
Explanation: Split 1 worker into 2, then assign the first worker to the last block and split the second worker into 2.
Then, use the two unassigned workers to build the first two blocks.
The cost is 1 + max(3, 1 + max(1, 2)) = 4.
Constraints:
	1 &lt= blocks.length &lt= 1000
	1 &lt= blocks[i] &lt= 10^5
	1 &lt= split &lt= 100
## Solutions:
```python
class Solution :
public:
    int minBuildTime(vector& blocks, int split) :
        int n = blocks.size()
        if (n == 0) return 0
        sort(blocks.begin(), blocks.end())
        vector> dp(n + 1, vector(n + 1, INT_MAX))
        for (int i = 0 i <= n ++i) :
            dp[0][i] = 0
        for (int i = 1 i <= n ++i) :
            dp[i][i] = blocks[i-1]
        for (int i = 1 i <= n ++i) :
            for (int j = 1 j <= n ++j) :
                int s = -1
                do :
                    ++s
                    dp[i][j] = min(dp[i][j], split * s + max(blocks[i-1], dp[i-1][min(i-1, (1  (1 << s) * j)
        return dp[n][1]
```
# 76. Minimum Window Substring
* *Difficulty: Hard*
* *Topics: Hash Table, Two Pointers, String, Sliding Window*
* *Similar Questions:*
  * [Substring with Concatenation of All Words](substring-with-concatenation-of-all-words.md)
  * [Minimum Size Subarray Sum](minimum-size-subarray-sum.md)
  * [Sliding Window Maximum](sliding-window-maximum.md)
  * [Permutation in String](permutation-in-string.md)
  * [Smallest Range Covering Elements from K Lists](smallest-range-covering-elements-from-k-lists.md)
  * [Minimum Window Subsequence](minimum-window-subsequence.md)
## Problem:
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Example:
Input: S = &quotADOBECODEBANC&quot, T = &quotABC&quot
Output: &quotBANC&quot
Note:
	If there is no such window in S that covers all characters in T, return the empty string &quot&quot.
	If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
## Solutions:
```python
class Solution :
public:
    string minWindow(string s, string t) :
        unordered_map charCount
        for (auto c : t) :
            ++charCount[c]
        int r = 0
        int l = 0
        int count = t.length()
        string ret
        int len = INT_MAX
        for (r = 0 r < s.length() ++r) :
            char c = s[r]
            if (charCount.count(c) == 0) continue
            --charCount[c]
            if (charCount[c] >= 0)  --count
            if (charCount[c] == 0 && count == 0) :  
                while (true) :
                    if (charCount.count(s[l]) == 0) :
                        ++l
                     else :
                        char lastC = s[l]
                        ++l
                        ++charCount[lastC]
                        if (charCount[lastC] == 1) :
                            ++count
                            break
                if (r - l + 2 < len) :
                    len = r - l + 2
                    ret = s.substr(l-1, len)
        return len == INT_MAX ? "" : ret
```
# 268. Missing Number
* *Difficulty: Easy*
* *Topics: Array, Math, Bit Manipulation*
* *Similar Questions:*
  * [First Missing Positive](first-missing-positive.md)
  * [Single Number](single-number.md)
  * [Find the Duplicate Number](find-the-duplicate-number.md)
  * [Couples Holding Hands](couples-holding-hands.md)
## Problem:
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Example 1:
Input: [3,0,1]
Output: 2
Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
## Solutions:
```python
class Solution :
public:
    int missingNumber(vector& nums) :
        int n = nums.size()
        for (int i = 0 i < n ++i) :
            kick(nums, i)
        for (int i = 0 i < n ++i) :
            if (nums[i] != i) :
                return i
        return n
    void kick(vector& nums, int i) :
        int val = nums[i]
        nums[i] = -1
        while (val = 0) :
            swap(val, nums[val])
```
# 163. Missing Ranges
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Summary Ranges](summary-ranges.md)
## Problem:
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: [&quot2&quot, &quot4-&gt49&quot, &quot51-&gt74&quot, &quot76-&gt99&quot]
## Solutions:
```python
class Solution :
public:
    vector findMissingRanges(vector& nums, int lower, int upper) :
        vector ret
        int expected = lower
        for (auto num : nums) :
            if (num <= expected) : // less and equal
                if (num == INT_MAX) return ret // to prevent overflow
                expected = num + 1
             else :
                ret.push_back(missingRange(expected, num - 1))
                if (num == INT_MAX) return ret
                expected = num + 1 // overflow
        if (expected <= upper) :
            ret.push_back(missingRange(expected, upper))
        return ret
    string missingRange(int lower, int upper) :
        if (lower == upper) :
            return to_string(lower)
         else :
            return to_string(lower) + "->" + to_string(upper)
```
# 932. Monotonic Array
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i &lt= j, A[i] &lt= A[j].  An array A is monotone decreasing if for all i &lt= j, A[i] &gt= A[j].
Return true if and only if the given array A is monotonic.
Example 1:
Input: [1,2,2,3]
Output: true
Example 2:
Input: [6,5,4,4]
Output: true
Example 3:
Input: [1,3,2]
Output: false
Example 4:
Input: [1,2,4,5]
Output: true
Example 5:
Input: [1,1,1]
Output: true
Note:
	1 &lt= A.length &lt= 50000
	-100000 &lt= A[i] &lt= 100000
## Solutions:
```python
class Solution :
public:
    bool isMonotonic(vector& A) :
        if (A.size() <= 2)  return true
        int cmp = 0
        for (int i = 1 i < A.size() ++i) :
            if (A[i] == A[i-1]) continue
            if (A[i] > A[i-1]) :
                if (cmp == -1)  return false
                cmp = 1
             else :
                if (cmp == 1)   return false
                cmp = -1
        return true
```
# 837. Most Common Word
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn&#39t banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
Example:
Input: 
paragraph = &quotBob hit a ball, the hit BALL flew far after it was hit.&quot
banned = [&quothit&quot]
Output: &quotball&quot
Explanation: 
&quothit&quot occurs 3 times, but it is a banned word.
&quotball&quot occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as &quotball,&quot), 
and that &quothit&quot isn&#39t the answer even though it occurs more because it is banned.
Note: 
	1 &lt= paragraph.length &lt= 1000.
	0 &lt= banned.length &lt= 100.
	1 &lt= banned[i].length &lt= 10.
	The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
	paragraph only consists of letters, spaces, or the punctuation symbols !?&#39,.
	There are no hyphens or hyphenated words.
	Words only consist of letters, never apostrophes or other punctuation symbols.
## Solutions:
```python
class Solution :
public:
    string mostCommonWord(string paragraph, vector& banned) :
        unordered_set bannedWords (banned.begin(), banned.end())
        unordered_map counts
        paragraph.push_back(' ')
        int pos = 0
        string word
        while (pos < paragraph.length()) :
            char c = paragraph[pos++]
            if (isalpha(c)) :
                word.push_back(tolower(c))
             else :
                if (word.length() != 0 && bannedWords.count(word) == 0) :
                    ++counts[word]
                word = ""
        int freq = 0
        string str
        for (auto& entry : counts) :
            if (entry.second > freq) :
                freq = entry.second
                str = entry.first
        return str
```
# 283. Move Zeroes
* *Difficulty: Easy*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Remove Element](remove-element.md)
## Problem:
Given an array nums, write a function to move all 0&#39s to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
	You must do this in-place without making a copy of the array.
	Minimize the total number of operations.
## Solutions:
```python
class Solution :
public:
    void moveZeroes(vector& nums) :
        int len = 0
        for (int i = 0 i < nums.size() ++i) :
            if (nums[i] == 0) continue
            nums[len++] = nums[i]
        for (int i = len i < nums.size() ++i) :
            nums[i] = 0
```
# 346. Moving Average from Data Stream
* *Difficulty: Easy*
* *Topics: Design, Queue*
* *Similar Questions:*
## Problem:
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Example:
MovingAverage m = new MovingAverage(3)
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
## Solutions:
```python
class MovingAverage :
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) :
        capacity = size
    double next(int val) :
        nums.push(val)
        sum += val
        if (nums.size() > capacity) :
            sum -= nums.front() nums.pop() 
        return (double) sum / nums.size()
private:
    int sum = 0
    queue nums
    int capacity
/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size)
 * double param_1 = obj->next(val)
 */
```
# 43. Multiply Strings
* *Difficulty: Medium*
* *Topics: Math, String*
* *Similar Questions:*
  * [Add Two Numbers](add-two-numbers.md)
  * [Plus One](plus-one.md)
  * [Add Binary](add-binary.md)
  * [Add Strings](add-strings.md)
## Problem:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Example 1:
Input: num1 = &quot2&quot, num2 = &quot3&quot
Output: &quot6&quot
Example 2:
Input: num1 = &quot123&quot, num2 = &quot456&quot
Output: &quot56088&quot
Note:
	The length of both num1 and num2 is &lt 110.
	Both num1 and num2 contain only digits 0-9.
	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
	You must not use any built-in BigInteger library or convert the inputs to integer directly.
## Solutions:
```python
class Solution :
public:
    string multiply(string num1, string num2) :
        int len1 = num1.length()
        int len2 = num2.length()
        if (num1 == "0" || num2 == "0") return "0" // this check is important
        vector digits (len1 + len2, 0)
        for (int i = 0 i < len1 ++i) :
            for (int j = 0 j < len2 ++j) :
                digits[i + j + 1] += (num1[i] - '0') * (num2[j] - '0') // remeber the position of digits.
        string ret
        for (int i = digits.size() - 1 i > 0 --i) :
            int digit = digits[i] % 10
            digits[i-1] += digits[i]/10
            ret.push_back(digit + '0')
        if (digits[0] > 0)  ret.push_back(digits[0] + '0')
        reverse(ret.begin(), ret.end())
        return ret
```
## Another more concise solution
It is possible to aggregate sum and carry. 
From [Huahua](https://zxi.mytechroad.com/blog/string/leetcode-43-multiply-strings/)
```python
// Author: Huahua
// Running time: 4 ms
class Solution :
public:
  string multiply(string num1, string num2) :
    const int l1 = num1.length()
    const int l2 = num2.length()
    string ans(l1 + l2, '0')
    for (int i = l1 - 1 i >= 0 --i)
      for (int j = l2 - 1 j >= 0 --j) :
        int sum = (ans[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0')        
        ans[i + j + 1] = (sum % 10) + '0'
        ans[i + j] += sum / 10 // This line is not a problem if the order is from right to left
    // ans[0] is guaranteed to be less than 10 due to math property
    for (int i = 0 i < ans.length() ++i)
      if (ans[i] != '0' || i == ans.length() - 1) return ans.substr(i)
    return ""
```
# 729. My Calendar I
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [My Calendar II](my-calendar-ii.md)
  * [My Calendar III](my-calendar-iii.md)
## Problem:
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start &lt= x &lt end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar() MyCalendar.book(start, end)
Example 1:
MyCalendar()
MyCalendar.book(10, 20) // returns true
MyCalendar.book(15, 25) // returns false
MyCalendar.book(20, 30) // returns true
Explanation: 
The first event can be booked.  The second can&#39t because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Note:
	The number of calls to MyCalendar.book per test case will be at most 1000.
	In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
## Solutions:
```python
class MyCalendar :
public:
    struct Interval :
        int start
        int end
        Interval(int start, int end) :
            this->start = start
            this->end = end
        bool operator< (const Interval& other) const :
            return start < other.start
    MyCalendar() :
    bool book(int start, int end) :
        if (start == end)   return true
        Interval interval :start, end
        if (intervals.empty()) :
            intervals.insert(interval)
            return true
        auto it = intervals.lower_bound(interval)
        if (it != intervals.begin()) :
            it = prev(it) // assignment1!!!!
            if (interval.start end)   return false
            it = next(it)
        if (it != intervals.end()) :
            if (interval.end > it->start)   return false
            else :
                intervals.insert(interval)
                return true
         else :
            intervals.insert(interval)
            return true
private:
    set intervals
/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar()
 * bool param_1 = obj->book(start,end)
 */
```
# 764. N-ary Tree Level Order Traversal
* *Difficulty: Easy*
* *Topics: Tree, Breadth-first Search*
* *Similar Questions:*
  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)
  * [N-ary Tree Preorder Traversal](n-ary-tree-preorder-traversal.md)
  * [N-ary Tree Postorder Traversal](n-ary-tree-postorder-traversal.md)
## Problem:
Given an n-ary tree, return the level order traversal of its nodes&#39 values. (ie, from left to right, level by level).
For example, given a 3-ary tree:
We should return its level order traversal:
[
     [1],
     [3,2,4],
     [5,6]
]
Note:
	The depth of the tree is at most 1000.
	The total number of nodes is at most 5000.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    vector children
    Node() :
    Node(int _val, vector _children) :
        val = _val
        children = _children
*/
class Solution :
public:
    vector> levelOrder(Node* root) :
        if (root == nullptr)    return :
        queue q
        q.push(root)
        vector> ret
        while (!q.empty()) :
            int size = q.size()
            vector level
            for (int i = 0 i < size ++i) :
                Node* node = q.front() q.pop()
                level.push_back(node->val)
                for (auto& child : node->children) :
                    q.push(child)
            ret.push_back(level)
        return ret
```
# 776. N-ary Tree Postorder Traversal
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Binary Tree Postorder Traversal](binary-tree-postorder-traversal.md)
  * [N-ary Tree Level Order Traversal](n-ary-tree-level-order-traversal.md)
  * [N-ary Tree Preorder Traversal](n-ary-tree-preorder-traversal.md)
## Problem:
Given an n-ary tree, return the postorder traversal of its nodes&#39 values.
For example, given a 3-ary tree:
Return its postorder traversal as: [5,6,3,2,4,1].
Note:
Recursive solution is trivial, could you do it iteratively?
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    vector children
    Node() :
    Node(int _val, vector _children) :
        val = _val
        children = _children
*/
class Solution :
public:
    vector postorder(Node* root) :
        vector ret
        helper(root, ret)
        return ret
private:
    void helper(Node* root, vector& ret) :
        if (root == nullptr)    return
        for (auto& child : root->children) :
            helper(child, ret)
        ret.push_back(root->val)
```
# 775. N-ary Tree Preorder Traversal
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Binary Tree Preorder Traversal](binary-tree-preorder-traversal.md)
  * [N-ary Tree Level Order Traversal](n-ary-tree-level-order-traversal.md)
  * [N-ary Tree Postorder Traversal](n-ary-tree-postorder-traversal.md)
## Problem:
Given an n-ary tree, return the preorder traversal of its nodes&#39 values.
For example, given a 3-ary tree:
Return its preorder traversal as: [1,3,5,6,2,4].
Note:
Recursive solution is trivial, could you do it iteratively?
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    vector children
    Node() :
    Node(int _val, vector _children) :
        val = _val
        children = _children
*/
class Solution :
public:
    vector preorder(Node* root) :
        vector ret
        helper(root, ret)
        return ret
private:
    void helper(Node* root, vector& ret) :
        if (root == nullptr)    return
        ret.push_back(root->val)
        for (auto& child : root->children) :
            helper(child, ret)
```
# 52. N-Queens II
* *Difficulty: Hard*
* *Topics: Backtracking*
* *Similar Questions:*
  * [N-Queens](n-queens.md)
## Problem:
The n-queens puzzle is the problem of placing n queens on an n&timesn chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [&quot.Q..&quot,  // Solution 1
  &quot...Q&quot,
  &quotQ...&quot,
  &quot..Q.&quot],
 [&quot..Q.&quot,  // Solution 2
  &quotQ...&quot,
  &quot...Q&quot,
  &quot.Q..&quot]
]
## Solutions:
```python
class Solution :
public:
    int totalNQueens(int n) :
        int ret = 0
        vector path
        vector colVisited (n, false)
        helper(n, 0, path, colVisited, ret)
        return ret
    bool diagonal(int row, int col, vector& path) :
        int n = path.size()
        for (int i = 0 i < n ++i) :
            if (abs(row - i) == abs(col - path[i])) return true
        return false
    void helper(int n, int pos, vector& path, vector& colVisited, int& ret) :
        if (n == pos) :
            ++ret
            return
        for (int i = 0 i < n ++i) :
            if (colVisited[i] || diagonal(pos, i, path)) continue
            path.push_back(i)
            colVisited[i] = true
            helper(n, pos + 1, path, colVisited, ret)
            colVisited[i] = false
            path.pop_back()
```
# 51. N-Queens
* *Difficulty: Hard*
* *Topics: Backtracking*
* *Similar Questions:*
  * [N-Queens II](n-queens-ii.md)
  * [Grid Illumination](grid-illumination.md)
## Problem:
The n-queens puzzle is the problem of placing n queens on an n&timesn chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens&#39 placement, where &#39Q&#39 and &#39.&#39 both indicate a queen and an empty space respectively.
Example:
Input: 4
Output: [
 [&quot.Q..&quot,  // Solution 1
  &quot...Q&quot,
  &quotQ...&quot,
  &quot..Q.&quot],
 [&quot..Q.&quot,  // Solution 2
  &quotQ...&quot,
  &quot...Q&quot,
  &quot.Q..&quot]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
## Solutions:
```python
class Solution :
public:
    vector> solveNQueens(int n) :
        vector> ret
        vector path
        vector colVisited (n, false)
        helper(n, 0, path, colVisited, ret)
        return ret
    vector generateSolution(vector& path) :
        int n = path.size()
        string row = string(n, '.')
        vector solution
        for (int i = 0 i < n ++i) :
            solution.push_back(row)
            solution.back()[path[i]] = 'Q'
        return solution
    bool diagonal(int row, int col, vector& path) :
        int n = path.size()
        for (int i = 0 i < n ++i) :
            if (abs(row - i) == abs(col - path[i])) return true
        return false
    void helper(int n, int pos, vector& path, vector& colVisited, vector>& ret) :
        if (n == pos) :
            ret.push_back(generateSolution(path))
            return
        for (int i = 0 i < n ++i) :
            if (colVisited[i] || diagonal(pos, i, path)) continue
            path.push_back(i)
            colVisited[i] = true
            helper(n, pos + 1, path, colVisited, ret)
            colVisited[i] = false
            path.pop_back()
```
# 364. Nested List Weight Sum II
* *Difficulty: Medium*
* *Topics: Depth-first Search*
* *Similar Questions:*
  * [Nested List Weight Sum](nested-list-weight-sum.md)
  * [Array Nesting](array-nesting.md)
## Problem:
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.
Example 1:
Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1&#39s at depth 1, one 2 at depth 2.
Example 2:
Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1 1*3 + 4*2 + 6*1 = 17.
## Solutions:
```python
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger :
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger()
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value)
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector &getList() const
 * 
 */
class Solution :
public:
    int depthSumInverse(vector& nestedList) :
        int depth = getDepth(nestedList)
        return helper(nestedList, depth)
private:
    int getDepth(vector& nestedList) :
        int depth = 0
        for (auto& nestedInt : nestedList) :
            if (nestedInt.isInteger()) :
                depth = max(depth, 1)
             else :
                depth = max(depth, 1 + getDepth(nestedInt.getList()))
        return depth
    int helper(vector& nestedList, int depth) :
        int sum = 0
        for (auto& nestedInt : nestedList) :
            if (nestedInt.isInteger()) :
                sum += depth * nestedInt.getInteger()
             else :
                sum += helper(nestedInt.getList(), depth - 1)
        return sum
```
# 339. Nested List Weight Sum
* *Difficulty: Easy*
* *Topics: Depth-first Search*
* *Similar Questions:*
  * [Nested List Weight Sum II](nested-list-weight-sum-ii.md)
  * [Array Nesting](array-nesting.md)
  * [Employee Importance](employee-importance.md)
## Problem:
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Example 1:
Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1&#39s at depth 2, one 2 at depth 1.
Example 2:
Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3 1 + 4*2 + 6*3 = 27.
## Solutions:
```python
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger :
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger()
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value)
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector &getList() const
 * 
 */
class Solution :
public:
    int depthSum(vector& nestedList) :
        return helper(nestedList, 1)
private:
    int helper(vector& nestedList, int depth) :
        int sum = 0
        for (auto& nestedInt : nestedList) :
            if (nestedInt.isInteger()) :
                sum += depth * nestedInt.getInteger()
             else :
                sum += helper(nestedInt.getList(), depth + 1)
        return sum
```
# 681. Next Closest Time
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
## Problem:
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
## Solutions:
```python
class Solution :
public:
    string nextClosestTime(string time) :
        set digitSet
        for (auto c : time) :
            if (c != ':') :
                digitSet.insert(c)
        vector digits (digitSet.begin(), digitSet.end())
        ++time[4]
        char nextChar = next(digits, time[4])
        if (nextChar != '#') :
            time[4] = nextChar
            return time
         else :
            time[4] = digits[0]
        ++time[3]
        nextChar = next(digits, time[3])
        if (nextChar != '#') :
            time[3] = nextChar
            if (time[3] < '6')  return time
            else time[3] = digits[0]
         else :
            time[3] = digits[0]
        ++time[1]
        nextChar = next(digits, time[1])
        if (nextChar != '#') :
            time[1] = nextChar
            if (time[0] == '2' && time[1] > '3') :
                time[1] = digits[0]
             else :
                return time
         else :
            time[1] = digits[0]
        ++time[0]
        nextChar = next(digits, time[0])
        if (nextChar != '#') :
            time[0] = nextChar
            if (time[0] > '2') :
                time[0] = digits[0]
             else :
                return time
         else :
            time[0] = digits[0]
        return time
    char next(vector& digits, char c) :
        auto it = lower_bound(digits.begin(), digits.end(), c)
        if (it != digits.end()) :
            return *it
         else :
            return '#'
```
# 496. Next Greater Element I
* *Difficulty: Easy*
* *Topics: Stack*
* *Similar Questions:*
  * [Next Greater Element II](next-greater-element-ii.md)
  * [Next Greater Element III](next-greater-element-iii.md)
  * [Daily Temperatures](daily-temperatures.md)
## Problem:
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2. 
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
## Solutions:
```python
class Solution :
public:
    vector nextGreaterElement(vector& nums1, vector& nums2) :
        unordered_map numToIndex
        for (int i = 0 i < nums1.size() ++i) :
            numToIndex[nums1[i]] = i
        int n = nums1.size()
        vector ret(n, -1)
        stack stk
        for (int i = 0 i < nums2.size() ++i) :
            int num = nums2[i]
            while (!stk.empty() && stk.top() < num) :
                int target = stk.top() stk.pop()
                if (numToIndex.count(target) > 0) :
                    ret[numToIndex[target]] = num
            stk.push(num)
        return ret
```
# 31. Next Permutation
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Permutations](permutations.md)
  * [Permutations II](permutations-ii.md)
  * [Permutation Sequence](permutation-sequence.md)
  * [Palindrome Permutation II](palindrome-permutation-ii.md)
## Problem:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 &rarr 1,3,2
3,2,1 &rarr 1,2,3
1,1,5 &rarr 1,5,1
## Solutions:
```python
class Solution :
public:
    void nextPermutation(vector& nums) :
        if (nums.size() == 0)   return
        int i =  0
        for (i = nums.size() - 2 i >= 0 --i) :
            if (nums[i] < nums[i+1]) :
                break
        if (i >= 0) :
            int j = nums.size() - 1
            while (j >= 0 && nums[j] <= nums[i]) :
                --j
            swap(nums[i], nums[j])
        reverse(nums, i + 1, nums.size() - 1)        
    void reverse(vector& nums, int start, int end) :
        while (start < end) :
            swap(nums[start], nums[end])
            ++start
            --end
```
# 292. Nim Game
* *Difficulty: Easy*
* *Topics: Brainteaser, Minimax*
* *Similar Questions:*
  * [Flip Game II](flip-game-ii.md)
## Problem:
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
Example:
Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.
## Solutions:
```python
class Solution :
public:
    bool canWinNim(int n) :
        return n % 4 != 0
```
# 665. Non-decreasing Array
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i]  holds for every i (1 <= i < n).
Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note:
The n belongs to [1, 10,000].
## Solutions:
```python
class Solution :
public:
    bool checkPossibility(vector& nums) :
        if (nums.size() <= 1)   return true
        int p = -1
        for (int i = 0 i < nums.size() - 1 ++i) :
            if (nums[i] > nums[i+1]) :
                if (p != -1)    return false
                else :
                    p = i
        return p == -1 || p == 0 || p == nums.size() - 2 || nums[p-1] <= nums[p+1] || nums[p] <= nums[p+2]
```
# 600. Non-negative Integers without Consecutive Ones
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [House Robber](house-robber.md)
  * [House Robber II](house-robber-ii.md)
  * [Ones and Zeroes](ones-and-zeroes.md)
## Problem:
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.
Example 1:
Input: 5
Output: 5
Explanation: 
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
Note:
1 9
## Solutions:
```python
class Solution :
public:
    int findIntegers(int num) :
        unordered_map cache
        return helper(num, 31, cache)
private:
    int helper(int num, int pos, unordered_map& cache) :
        // cout << num << " " << pos << endl
        if (cache.count(num))   return cache[num]
        if (pos < 0)  return 1
        if ((num & (1 << pos)) == 0) :
            return helper(num, pos - 1, cache)
        if (pos == 0) :
            return 2
        if (pos == 1) :
            return 3
        int ret
        int num1 = (1 << pos) - 1
        int num2 = 
            ((num & (1 << (pos - 1))) == 0) ? num & (~(3 << (pos - 1))) : (1 << (pos - 1)) - 1
        ret = helper(num1, pos - 1, cache) + helper(num2, pos - 2, cache)
        cache[num] = ret
        return ret
```
# 476. Number Complement
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
## Problem:
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
## Solutions:
```python
class Solution :
public:
    int findComplement(int num) :
        size_t mask = ~0
        while (mask & num)  mask <<= 1
        return ~mask & ~num
```
# 191. Number of 1 Bits
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Reverse Bits](reverse-bits.md)
  * [Power of Two](power-of-two.md)
  * [Counting Bits](counting-bits.md)
  * [Binary Watch](binary-watch.md)
  * [Hamming Distance](hamming-distance.md)
  * [Binary Number with Alternating Bits](binary-number-with-alternating-bits.md)
  * [Prime Number of Set Bits in Binary Representation](prime-number-of-set-bits-in-binary-representation.md)
## Problem:
Write a function that takes an unsigned integer and return the number of &#391&#39 bits it has (also known as the Hamming weight).
Example 1:
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three &#391&#39 bits.
Example 2:
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one &#391&#39 bit.
Example 3:
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one &#391&#39 bits.
Note:
	Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
	In Java, the compiler represents the signed integers using 2&#39s complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
Follow up:
If this function is called many times, how would you optimize it?
## Solutions:
```python
class Solution :
public:
    int hammingWeight(uint32_t n) :
        int ret = 0
        while (n) :
            n &= n - 1
            ++ret
        return ret
```
# 447. Number of Boomerangs
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Line Reflection](line-reflection.md)
## Problem:
Given n points in the plane that are all pairwise distinct, a &quotboomerang&quot is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
Example:
Input:
[[0,0],[1,0],[2,0]]
Output:
2
Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
## Solutions:
```python
class Solution :
public:
    int numberOfBoomerangs(vector>& points) :
        int ret = 0
        for (int i = 0 i < points.size() ++i) :
            map distances
            for (int j = 0 j < points.size() ++j) :
                if (i == j) continue
                ++distances[computeDistance(points[i], points[j])]
            for (auto it = distances.begin() it != distances.end() ++it) :
                ret += (it -> second) * (it ->second - 1)
        return ret
private:
    int computeDistance(vector& p1, vector& p2) :
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
```
# 1088. Number of Days in a Month
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Given a year Y and a month M, return how many days there are in that month.
Example 1:
Input: Y = 1992, M = 7
Output: 31
Example 2:
Input: Y = 2000, M = 2
Output: 29
Example 3:
Input: Y = 1900, M = 2
Output: 28
Note:
	1583 &lt= Y &lt= 2100
	1 &lt= M &lt= 12
## Solutions:
```python
class Solution :
public:
    int numberOfDays(int Y, int M) :
        int dayNum[12] = :31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        if (Y % 100 == 0) :
            if (Y % 400 == 0) :
                dayNum[1] = 29
         else :
            if (Y % 4 == 0) :
                dayNum[1] = 29
        return dayNum[M - 1]
```
# 233. Number of Digit One
* *Difficulty: Hard*
* *Topics: Math*
* *Similar Questions:*
  * [Factorial Trailing Zeroes](factorial-trailing-zeroes.md)
  * [Digit Count in Range](digit-count-in-range.md)
## Problem:
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
Example:
Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
## Solutions:
```python
class Solution :
public:
    int countDigitOne(int n) :
        int origin = n
        int ret = 0
        int level = 0
        int val = 1
        while (n > 0) :
            int last = n % 10
            if (last != 1) :
                ret += count(last, last * val, level)
             else :
                ret += count(last, last * val, level)
                ret += (origin % (val) + 1)
            level++
            n /= 10
            if (n > 0)
                val *= 10
        return ret
private:
    int count(int mostSig, int num, int level) :
        if (mostSig == 0)   return 0
        if (mostSig == 1)  return num * 0.1 * level
        return num * 0.1 * level + num / mostSig
```
# 694. Number of Distinct Islands
* *Difficulty: Medium*
* *Topics: Hash Table, Depth-first Search*
* *Similar Questions:*
  * [Number of Islands](number-of-islands.md)
  * [Number of Distinct Islands II](number-of-distinct-islands-ii.md)
## Problem:
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)  You may assume all four edges of the grid are surrounded by water.
Count the number of distinct islands.  An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.
Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note:
The length of each dimension in the given grid does not exceed 50.
## Solutions:
```python
class Solution :
public:
    int numDistinctIslands(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        vector> visited (m, vector(n, false))
        unordered_set islands
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] && !visited[i][j]) :
                    string digest
                    dfs(grid, visited, i, j, digest)
                    islands.insert(digest)
        return islands.size()
private:
     void dfs(const vector>& grid, vector>& visited, int row, int col, string& digest) :
         int m = grid.size()
         int n = grid[0].size()
         if (row = m || col = n || !grid[row][col] || visited[row][col]) :
             digest.push_back('e') // empty
             return
         visited[row][col] = true
         digest.push_back('d') dfs(grid, visited, row + 1, col, digest) // down
         digest.push_back('u') dfs(grid, visited, row - 1, col, digest) // up
         digest.push_back('r') dfs(grid, visited, row, col + 1, digest) // right
         digest.push_back('l') dfs(grid, visited, row, col - 1, digest) // left
```
# 305. Number of Islands II
* *Difficulty: Hard*
* *Topics: Union Find*
* *Similar Questions:*
  * [Number of Islands](number-of-islands.md)
## Problem:
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example:
Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:
Can you do it in time complexity O(k log mn), where k is the length of the positions?
## Solutions:
```python
class Solution :
public:
    vector numIslands2(int m, int n, vector>& positions) :
        UF uf
        vector ret
        vector> grid (m, vector (n, false))
        for (auto& position : positions) :
            int row = position[0]
            int col = position[1]
            if (grid[row][col]) :
                ret.push_back(uf.getSize())
                continue
            grid[row][col] = true
            uf.add(row * n + col)
            if (row + 1 < m && grid[row + 1][col]) :
                uf.connect(row * n + col, (row + 1) * n + col)
            if (row - 1 >= 0 && grid[row - 1][col]) :
                uf.connect(row * n + col, (row - 1) * n + col)
            if (col + 1 < n && grid[row][col + 1]) :
                uf.connect(row * n + col, row * n + col + 1)
            if (col - 1 >= 0 && grid[row][col - 1]) :
                uf.connect(row * n + col, row * n + col - 1)
            ret.push_back(uf.getSize())
        return ret
    class UF :
    public:
        int getSize() :
            return size
        void add(int a) :
            parents[a] = a
            ++size
        void connect(int a, int b) :
            int rootA = find(a)
            int rootB = find(b)
            if (rootA != rootB) :
                parents[rootA] = rootB
                --size
        int find(int x) :
            if (parents[x] != x) :
                parents[x] = find(parents[x])
            return parents[x]
    private:
        map parents
        int size = 0
```
# 200. Number of Islands
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search, Union Find*
* *Similar Questions:*
  * [Surrounded Regions](surrounded-regions.md)
  * [Walls and Gates](walls-and-gates.md)
  * [Number of Islands II](number-of-islands-ii.md)
  * [Number of Connected Components in an Undirected Graph](number-of-connected-components-in-an-undirected-graph.md)
  * [Number of Distinct Islands](number-of-distinct-islands.md)
  * [Max Area of Island](max-area-of-island.md)
## Problem:
Given a 2d grid map of &#391&#39s (land) and &#390&#39s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input:
11110
11010
11000
00000
Output: 1
Example 2:
Input:
11000
11000
00100
00011
Output: 3
## Solutions:
```python
class Solution :
public:
    int numIslands(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        vector> visited(m, vector(n, false))
        int count = 0
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (visited[i][j] || grid[i][j] == '0') continue
                ++count
                dfs(grid, visited, m, n, i, j)
        return count
    void dfs(vector>& grid, vector>& visited, int m, int n, int i, int j) :
        if (i = m || j = n || visited[i][j] || grid[i][j] == '0') return
        visited[i][j] = true
        for (int d = 0 d < 4 ++d) :
            dfs(grid, visited, m, n, i + directions[d][0], j + directions[d][1])
private:
    int directions[4][2] ::1, 0, :-1, 0, :0, 1, :0, -1
```
# 434. Number of Segments in a String
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Example:
Input: "Hello, my name is John"
Output: 5
## Solutions:
```python
class Solution :
public:
    int countSegments(string s) :
        if (s.length() == 0)    return 0
        int pos = 1
        int count = (s[0] == ' ' ? 0 : 1)
        while (pos < s.length()) :
            if (s[pos] != ' ' && s[pos-1] == ' ')   ++count
            ++pos
        return count
```
# 328. Odd Even Linked List
* *Difficulty: Medium*
* *Topics: Linked List*
* *Similar Questions:*
  * [Split Linked List in Parts](split-linked-list-in-parts.md)
## Problem:
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
Example 1:
Input: 1-&gt2-&gt3-&gt4-&gt5-&gtNULL
Output: 1-&gt3-&gt5-&gt2-&gt4-&gtNULL
Example 2:
Input: 2-&gt1-&gt3-&gt5-&gt6-&gt4-&gt7-&gtNULL
Output: 2-&gt3-&gt6-&gt7-&gt1-&gt5-&gt4-&gtNULL
Note:
	The relative order inside both the even and odd groups should remain as it was in the input.
	The first node is considered odd, the second node even and so on ...
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* oddEvenList(ListNode* head) :
        ListNode* evenDummyHead = new ListNode(0)
        ListNode* oddDummyHead = new ListNode(0)
        ListNode* evenCur = evenDummyHead
        ListNode* oddCur = oddDummyHead
        ListNode* cur = head
        int count = 0
        while (cur) :
            if (count % 2 == 0) :
                evenCur->next = cur
                evenCur = evenCur->next
             else :
                oddCur->next = cur
                oddCur = oddCur->next
            cur = cur->next
            ++count
        evenCur->next = oddDummyHead->next
        oddCur->next = NULL
        return evenDummyHead->next
```
# 161. One Edit Distance
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
  * [Edit Distance](edit-distance.md)
## Problem:
Given two strings s and t, determine if they are both one edit distance apart.
Note: 
There are 3 possiblities to satisify one edit distance apart:
	Insert a character into s to get t
	Delete a character from s to get t
	Replace a character of s to get t
Example 1:
Input: s = &quotab&quot, t = &quotacb&quot
Output: true
Explanation: We can insert &#39c&#39 into s to get t.
Example 2:
Input: s = &quotcab&quot, t = &quotad&quot
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:
Input: s = &quot1203&quot, t = &quot1213&quot
Output: true
Explanation: We can replace &#390&#39 with &#391&#39 to get t.
## Solutions:
```python
class Solution :
public:
    bool isOneEditDistance(string s, string t) :
        if (s.length() == t.length()) :
            return isOneReplace(s, t)
         else :
            if (s.length() - t.length() == 1) :
                return isOneDelete(s, t)
             else if (t.length() - s.length() == 1) :
                return isOneDelete(t, s)
             else :
                return false
    bool isOneReplace(string& s, string& t) :
        int diff = 0
        for (int i = 0 i < s.length() ++i) :
            if (s[i] != t[i]) :
                if (++diff > 1) return false
        return diff == 1
    bool isOneDelete(string& s, string& t) :
        int i = 0
        while (i < t.length() && s[i] == t[i]) ++i
        if (i == t.length())    return true
        while (i < t.length() && s[i+1] == t[i]) ++i
        return i == t.length()
```
# 465. Optimal Account Balancing
* *Difficulty: Hard*
* *Topics: *
* *Similar Questions:*
## Problem:
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.
Note:
A transaction will be given as a tuple (x, y, z). Note that x &ne y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:
Input:
[[0,1,10], [2,0,5]]
Output:
2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:
Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
Output:
1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
## Solutions:
```python
class Solution :
public:
    int minTransfers(vector>& transactions) :
        if (transactions.size() == 0)   return 0
        unordered_map userBalance
        for (auto& transaction : transactions) :
            int sender = transaction[0]
            int receiver = transaction[1]
            int amount = transaction[2]
            userBalance[sender] += amount
            userBalance[receiver] -= amount
        vector balances
        for (auto& entry : userBalance) :
            if (entry.second != 0)
                balances.push_back(entry.second)
        // for (auto val : balances) :
        //     cout << val << " "
        // 
        // cout << endl
        int ret = INT_MAX
        helper(balances, 0, ret)
        return ret
private:
    void helper(vector& balances, int transfer, int& ret) :
        // cout << "s:" << transfer << endl
        // for (auto val : balances) :
        //     cout << val << " "
        // 
        // cout << endl
        if (balances.size() <= 1) :
            ret = min(ret, transfer)
            return
        int amount = balances.back()
        if (amount == 0) :
            balances.pop_back()
            helper(balances, transfer, ret)
            balances.push_back(0)
            return
        for (int i = 0 i < balances.size() - 1 ++i) :
            if (amount * balances[i] < 0) :
                balances[i] += amount
                balances.pop_back()
                helper(balances, transfer + 1, ret)
                balances.push_back(amount)
                balances[i] -= amount
```
# 576. Out of Boundary Paths
* *Difficulty: Medium*
* *Topics: Dynamic Programming, Depth-first Search*
* *Similar Questions:*
  * [Knight Probability in Chessboard](knight-probability-in-chessboard.md)
## Problem:
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.
Example 1:
Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:
Example 2:
Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:
Note:
	Once you move the ball out of boundary, you cannot move it back.
	The length and height of the grid is in range [1,50].
	N is in range [0,50].
## Solutions:
```python
class Solution :
public:
    int findPaths(int m, int n, int N, int i, int j) :
        map, int> cache
        return helper(m, n, N, i, j, cache)
private:
    int helper(int m, int n, int N, int i, int j, map, int>& cache) :
        if (i = m || j = n) return 1
        int position = getPosition(m, n, i, j)
        if (cache.count(:position, N) > 0) return cache[:position, N]
        if (N == 0) return 0
        int ret = 0
        for (int k = 0 k < 4 ++k) :
            ret = (ret + helper(m, n, N - 1, i + directions[k][0], j + directions[k][1], cache)) % MOD
        cache[:position, N] = ret
        return ret
    inline int getPosition(int m, int n, int i, int j) :
        return n * i + j
    int directions[4][2] = :
        :1, 0,
        :-1, 0,
        :0, 1,
        :0, -1
    int MOD = 1e9 + 7
```
# 276. Paint Fence
* *Difficulty: Easy*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [House Robber](house-robber.md)
  * [House Robber II](house-robber-ii.md)
  * [Paint House](paint-house.md)
  * [Paint House II](paint-house-ii.md)
## Problem:
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.
Note:
n and k are non-negative integers.
Example:
Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
## Solutions:
```python
class Solution :
public:
    int numWays(int n, int k) :
        if (k == 0) return 0
        if (n == 0) return 0
        return k * helper(n - 1, k)
    int helper(int n, int k) :
        if (n == 0) return 1
        if (n == 1) return k 
        int a = 1
        int b = k
        for (int i = 2 i <= n ++i) :
            a = (a + b) * (k - 1)
            swap(a, b)
        return b
```
# 265. Paint House II
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Product of Array Except Self](product-of-array-except-self.md)
  * [Sliding Window Maximum](sliding-window-maximum.md)
  * [Paint House](paint-house.md)
  * [Paint Fence](paint-fence.md)
## Problem:
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0 costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
Note:
All costs are positive integers.
Example:
Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?
## Solutions:
```python
class Solution :
public:
    int minCostII(vector>& costs) :
        int n = costs.size()
        if (n == 0) return 0
        int k = costs[0].size()
        if (k == 0) return 0
        if (k == 1) : // check the situation when there is only one color.
            if (n == 1) return costs[0][0] 
            return -1
        costs.push_back(vector(k, 0))
        ++n
        vector> dp (n + 1, vector(k, 0))
        int least1 = 0
        int color1 = -1
        int least2 = 0
        int color2 = -1
        for (int i = 1 i <= n ++i) :
            int curLeast1 = INT_MAX
            int curColor1 = -1
            int curLeast2 = INT_MAX
            int curColor2 = -1
            for (int j = 0 j < k ++j) :
                if (j == color1) :
                    dp[i][j] = costs[i-1][j] + least2
                 else :
                    dp[i][j] = costs[i-1][j] + least1
                if (dp[i][j] < curLeast1) :
                    curLeast2 = curLeast1
                    curColor2 = curColor1
                    curLeast1 = dp[i][j]
                    curColor1 = j
                 else if (dp[i][j] < curLeast2) :
                    curLeast2 = dp[i][j]
                    curColor2 = j
            cout << endl
            least1 = curLeast1
            color1 = curColor1
            least2 = curLeast2
            color2 = curColor2
        return least1
```
# 256. Paint House
* *Difficulty: Easy*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [House Robber](house-robber.md)
  * [House Robber II](house-robber-ii.md)
  * [Paint House II](paint-house-ii.md)
  * [Paint Fence](paint-fence.md)
## Problem:
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
Note:
All costs are positive integers.
Example:
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
## Solutions:
```python
class Solution :
public:
    int minCost(vector>& costs) :
        int n = costs.size()
        if (n == 0) return 0
        vector> dp(2, vector (3, 0))
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for (int i = 1 i < n ++i) :
            for (int j = 0 j < 3 ++j) :
                dp[i%2][j] = min(dp[(i-1)%2][(j+1)%3], dp[(i-1)%2][(j+2)%3]) + costs[i][j] 
        return min(dp[(n-1)%2][0], min(dp[(n-1)%2][1], dp[(n-1)%2][2]))
```
# 234. Palindrome Linked List
* *Difficulty: Easy*
* *Topics: Linked List, Two Pointers*
* *Similar Questions:*
  * [Palindrome Number](palindrome-number.md)
  * [Valid Palindrome](valid-palindrome.md)
  * [Reverse Linked List](reverse-linked-list.md)
## Problem:
Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1-&gt2
Output: false
Example 2:
Input: 1-&gt2-&gt2-&gt1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    bool isPalindrome(ListNode* head) :
        ListNode* mid = middlePoint(head)
        ListNode* half = reverse(mid)
        //cout val << endl
        //cout val << endl
        while (half) :
            //cout val val << endl
            if (head->val != half->val)  return false
            head = head->next
            half = half->next
        return true
    ListNode* middlePoint(ListNode* head) :
        ListNode* fast = head
        ListNode* slow = head
        while (fast && fast -> next) :
            fast = fast->next->next
            slow = slow->next
        return slow
    ListNode* reverse(ListNode* head) :
        if (head == NULL)   return NULL
        ListNode* dummy = new ListNode(0)
        ListNode* cur = head
        ListNode* next = NULL
        while (cur) :
            next = cur->next
            cur->next = dummy->next
            dummy->next = cur
            cur = next
        return dummy->next
```
# 9. Palindrome Number
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Palindrome Linked List](palindrome-linked-list.md)
## Problem:
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:
Input: 121
Output: true
Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:
Coud you solve it without converting the integer to a string?
## Solutions:
```python
class Solution :
public:
    bool isPalindrome(int x) :
        if (x < 0)  return false
        int reverse = 0
        int val = x
        while (val > 0) :
            int digit = val % 10
            val = val/10
            if (reverse > INT_MAX/10 || reverse == INT_MAX/10 && digit > INT_MAX % 10)  return false // remember to check overflow!
            reverse = 10 * reverse + digit
        return reverse == x
```
# 336. Palindrome Pairs
* *Difficulty: Hard*
* *Topics: Hash Table, String, Trie*
* *Similar Questions:*
  * [Longest Palindromic Substring](longest-palindromic-substring.md)
  * [Shortest Palindrome](shortest-palindrome.md)
## Problem:
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
Example 1:
Input: [&quotabcd&quot,&quotdcba&quot,&quotlls&quot,&quots&quot,&quotsssll&quot]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are [&quotdcbaabcd&quot,&quotabcddcba&quot,&quotslls&quot,&quotllssssll&quot]
Example 2:
Input: [&quotbat&quot,&quottab&quot,&quotcat&quot]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are [&quotbattab&quot,&quottabbat&quot]
## Solutions:
```python
class Solution :
public:
    vector> palindromePairs(vector& words) :
        vector> left = helper(words, true)
        vector reverseWords
        for (int i = 0 i < words.size() ++i) :
            reverseWords.push_back(:words[i].rbegin(), words[i].rend())
        vector> right = helper(reverseWords,false)
        set> ret
        ret.insert(right.begin(), right.end())
        ret.insert(left.begin(), left.end())
        return vector>(ret.begin(), ret.end())
    vector> helper(vector& words, bool direction) :
        unordered_map wordMap
        for (int i = 0 i < words.size() ++i) :
            wordMap[words[i]] = i
        vector> ret
        for (int i = 0 i < words.size() ++i) :
            string word = words[i]
            reverse(word.begin(), word.end())
            for (int j = word.length() - 1 j >= -1 --j) :   
                if (wordMap.count(word.substr(0, j + 1)) > 0 && isPalindrome(word.substr(j + 1, word.length() - j - 1))) :
                    if (i != wordMap[word.substr(0, j + 1)]) :
                        if (direction) // Two directions!!!
                            ret.push_back(:wordMap[word.substr(0, j + 1)], i)
                        else 
                            ret.push_back(:i, wordMap[word.substr(0, j + 1)])
                        continue
        return ret
private:
    bool isPalindrome(string str) :
        //cout << str << endl
        int left = 0
        int right = str.length() - 1
        while (left < right) :
            if (str[left] != str[right])    return false
            ++left
            --right
        return true
```
# 132. Palindrome Partitioning II
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Palindrome Partitioning](palindrome-partitioning.md)
## Problem:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
Example:
Input: &quotaab&quot
Output: 1
Explanation: The palindrome partitioning [&quotaa&quot,&quotb&quot] could be produced using 1 cut.
## Solutions:
```python
class Solution :
public:
    int minCut(string s) :
        int len = s.length()
        vector> dp(len, vector(len, false))
        for (int j = 0 j < len ++j) :
            for (int i = 0 i <= j ++i) :
                if (s[i] == s[j] && (j - i <= 2 || dp[i+1][j-1])) :
                    dp[i][j] = true
        vector cache (len, INT_MAX)
        return helper(s, 0, dp, cache) - 1
    int helper(string& s, int start, vector>& dp, vector& cache) :
        if (start >= s.length())    return 0
        if (cache[start] != INT_MAX)    return cache[start]
        int ret = INT_MAX
        for (int i = start i < s.length() ++i) :
            if (dp[start][i]) :
                ret = min(ret, 1 + helper(s, i + 1, dp, cache)) 
        cache[start] = ret                  
        return ret
```
# 131. Palindrome Partitioning
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [Palindrome Partitioning II](palindrome-partitioning-ii.md)
## Problem:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Example:
Input: &quotaab&quot
Output:
[
  [&quotaa&quot,&quotb&quot],
  [&quota&quot,&quota&quot,&quotb&quot]
]
## Solutions:
```python
class Solution :
public:
    vector> partition(string s) :
        int len = s.length()
        vector> ret
        vector path
        vector> dp(len, vector(len, false))
        helper(s, 0, 0, dp, path, ret)
        return ret
    void helper(string& s, int start, int pos, vector>& dp, vector& path,                  vector>& ret) :
        if (pos == s.length()) :
            if (start == s.length()) :
                ret.push_back(path)
            return
        if (s[pos] == s[start]) :
            if (start + 1 == pos || start == pos) :
                dp[start][pos] = true
             else :
                dp[start][pos] = dp[start + 1][pos - 1] // it works because another branch has compute dp[start+1][pos-1]. However, it is not a good idea to compute dp inside helper function.
        if (dp[start][pos] == false) :
            helper(s, start, pos + 1, dp, path, ret)
            return
        path.push_back(s.substr(start, pos - start + 1))
        helper(s, pos + 1, pos + 1, dp, path, ret)
        path.pop_back()
        helper(s, start, pos + 1, dp, path, ret)
```
# 266. Palindrome Permutation
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Longest Palindromic Substring](longest-palindromic-substring.md)
  * [Valid Anagram](valid-anagram.md)
  * [Palindrome Permutation II](palindrome-permutation-ii.md)
  * [Longest Palindrome](longest-palindrome.md)
## Problem:
Given a string, determine if a permutation of the string could form a palindrome.
Example 1:
Input: &quotcode&quot
Output: false
Example 2:
Input: &quotaab&quot
Output: true
Example 3:
Input: &quotcarerac&quot
Output: true
## Solutions:
```python
class Solution :
public:
    bool canPermutePalindrome(string s) :
        int charCount[256] = :0
        for (auto c : s) :
            charCount[c] ^= 0x1
        int count = 0
        for (int i = 0 i < 256 ++i) :
            count += charCount[i]
        return s.length() % 2 == 0 ? count == 0 : count == 1
```
# 647. Palindromic Substrings
* *Difficulty: Medium*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
  * [Longest Palindromic Substring](longest-palindromic-substring.md)
  * [Longest Palindromic Subsequence](longest-palindromic-subsequence.md)
  * [Palindromic Substrings](palindromic-substrings.md)
## Problem:
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:
Input: &quotabc&quot
Output: 3
Explanation: Three palindromic strings: &quota&quot, &quotb&quot, &quotc&quot.
Example 2:
Input: &quotaaa&quot
Output: 6
Explanation: Six palindromic strings: &quota&quot, &quota&quot, &quota&quot, &quotaa&quot, &quotaa&quot, &quotaaa&quot.
Note:
	The input string length won&#39t exceed 1000.
## Solutions:
```python
class Solution :
public:
    int countSubstrings(string s) :
        int sum = 0
        for (int i = 0 i < s.length() ++i) :
            sum += palindromeNum(s, i, i)
            sum += palindromeNum(s, i, i + 1)
        return sum
private:
    int palindromeNum(const string& s, int left, int right) :
        int count = 0
        while (left >= 0 && right < s.length()) :
            if (s[left] == s[right]) :
                ++count
                --left
                ++right
             else :
                return count
        return count
```
# 736. Parse Lisp Expression
* *Difficulty: Hard*
* *Topics: String*
* *Similar Questions:*
  * [Ternary Expression Parser](ternary-expression-parser.md)
  * [Number of Atoms](number-of-atoms.md)
  * [Basic Calculator IV](basic-calculator-iv.md)
## Problem:
You are given a string expression representing a Lisp-like expression to return the integer value of.
The syntax for these expressions is given as follows.
An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable.  Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially and then the value of this let-expression is the value of the expression expr.
An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.
For the purposes of this question, we will use a smaller subset of variable names.  A variable starts with a lowercase letter, then zero or more lowercase letters or digits.  Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope.  When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially.  It is guaranteed that every expression is legal.  Please see the examples for more details on scope.
Evaluation Examples:
Input: (add 1 2)
Output: 3
Input: (mult 3 (add 2 3))
Output: 15
Input: (let x 2 (mult x 5))
Output: 10
Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.
Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.
Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.
Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.
Input: (let a1 3 b2 (add a1 1) b2) 
Output 4
Explanation: Variable names can contain digits after the first character.
Note:
The given string expression is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses.  The expression is guaranteed to be legal and evaluate to an integer.
The length of expression is at most 2000.  (It is also non-empty, as that would not be a legal expression.)
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
## Solutions:
```python
class Solution :
public:
    int evaluate(string expression) :
        int pos = 0
        unordered_map symbols
        return helper(expression, pos, symbols)
private:
    int getNumber(string& expression, int& pos) :
        int sign = 1
        if (expression[pos] == '-') :
            sign = -1
            ++pos
        int val = 0
        for ( pos < expression.length() && isdigit(expression[pos]) ++pos) :
            val = 10 * val + (expression[pos] - '0')
        return sign * val
    string getOperator(string& expression, int& pos) :
        string ret
        for ( pos < expression.length() && expression[pos] != ' ' ++pos) :
            ret.push_back(expression[pos])
        return ret
    string getSymbol(string& expression, int& pos) :
        string ret
        for ( pos < expression.length() && expression[pos] != ' ' && expression[pos] != ')' ++pos) :
            ret.push_back(expression[pos])
        return ret
    int helper(string& expression, int& pos, unordered_map& symbols) :
        if (expression[pos] == '(') :
            ++pos // remove '('
            string op = getOperator(expression, pos)
            ++pos // remove space
            if (op != "let") :
                int oprand1 = helper(expression, pos, symbols)
                ++pos //remove space
                int oprand2 = helper(expression, pos, symbols)
                ++pos // remove ')'
                if (op == "add") :
                    return oprand1 + oprand2
                 else :
                    return oprand1 * oprand2
             else :
                unordered_set add
                unordered_map replace
                string symbol1 = getSymbol(expression, pos)
                ++pos // remove space
                if (symbols.count(symbol1) > 0) :
                    replace[symbol1] = symbols[symbol1]
                 else :
                    add.insert(symbol1)
                int value1 = helper(expression, pos, symbols)
                ++pos // remove space
                symbols[symbol1] = value1
                while(true) :
                    int cur = pos
                    int val = helper(expression, pos, symbols)
                    if (expression[pos] == ')') :
                        for (auto& symbol : add) :
                            symbols.erase(symbol)
                        for (auto& entry : replace) :
                            symbols[entry.first] = entry.second
                        ++pos // remove ')'
                        return val
                     else :
                        pos = cur
                        string symbol = getSymbol(expression, pos)
                        ++pos // remove space
                        if (symbols.count(symbol) > 0 && add.count(symbol) == 0) :
                            replace[symbol] = symbols[symbol]
                        add.insert(symbol)
                        int value = helper(expression, pos, symbols)
                        ++pos // remove space
                        symbols[symbol] = value
         else if (expression[pos] == '-' || isdigit(expression[pos])):
            return getNumber(expression, pos)
         else :
            string symbol = getSymbol(expression, pos)
            if (symbols.count(symbol) == 0) return -1
            return symbols[symbol]
```
# 1197. Parsing A Boolean Expression
* *Difficulty: Hard*
* *Topics: String*
* *Similar Questions:*
## Problem:
Return the result of evaluating a given boolean expression, represented as a string.
An expression can either be:
	&quott&quot, evaluating to True
	&quotf&quot, evaluating to False
	&quot!(expr)&quot, evaluating to the logical NOT of the inner expression expr
	&quot&amp(expr1,expr2,...)&quot, evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...
	&quot|(expr1,expr2,...)&quot, evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...
Example 1:
Input: expression = &quot!(f)&quot
Output: true
Example 2:
Input: expression = &quot|(f,t)&quot
Output: true
Example 3:
Input: expression = &quot&amp(t,f)&quot
Output: false
Example 4:
Input: expression = &quot|(&amp(t,f,t),!(t))&quot
Output: false
Constraints:
	1 &lt= expression.length &lt= 20000
	expression[i] consists of characters in :&#39(&#39, &#39)&#39, &#39&amp&#39, &#39|&#39, &#39!&#39, &#39t&#39, &#39f&#39, &#39,&#39.
	expression is a valid expression representing a boolean, as given in the description.
## Solutions:
```python
class Solution :
public:
    bool negate(string& expression, int& pos) :
        bool ret = !helper(expression, pos)
        ++pos // remove )
        return ret
    bool logicAdd(string& expression, int& pos) :
        bool ret = true
        do :
            ret = helper(expression, pos) && ret
         while (expression[pos++] == ',')
        return ret
    bool logicOr(string& expression, int& pos) :
        bool ret = false
        do :
            ret = helper(expression, pos) || ret
         while (expression[pos++] == ',')
        return ret
    bool parseBoolExpr(string expression) :
        int pos = 0
        return helper(expression, pos)
    bool helper(string& expression, int& pos) :
        //bool ret
        //for (pos < expression.length() ++pos) :
            char c = expression[pos]
            if (c == '!') :
                ++pos // remove !
                ++pos // remove (
                return negate(expression, pos)
            if (c == '&') :
                ++pos // remove &
                ++pos // remove (
                return logicAdd(expression, pos)
            if (c == '|') :
                ++pos // remove |
                ++pos // remove (
                return logicOr(expression, pos)
            ++pos
            if (c == 't') :
                return true
            else return false
        //
```
# 416. Partition Equal Subset Sum
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Partition to K Equal Sum Subsets](partition-to-k-equal-sum-subsets.md)
## Problem:
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Note:
	Each of the array element will not exceed 100.
	The array size will not exceed 200.
Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
## Solutions:
```python
class Solution :
public:
    bool canPartition(vector& nums) :
        bitset bits
        bits[0] = 1
        int sum = 0
        for (auto& num : nums) :
            bits |= bits << num
            sum += num
        return sum % 2 == 0 && bits[sum>>1] == 1
```
# 768. Partition Labels
* *Difficulty: Medium*
* *Topics: Two Pointers, Greedy*
* *Similar Questions:*
  * [Merge Intervals](merge-intervals.md)
## Problem:
A string S of lowercase letters is given.  We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
## Solutions:
```python
class Solution :
public:
    vector partitionLabels(string S) :
        int charLastIndex[26]
        for (int i = 0 i < 26 ++i) :
            charLastIndex[i] = -1
        for (int i = 0 i < S.length() ++i) :
            charLastIndex[S[i] - 'a'] = i
        vector ret
        int left = 0
        int right = 0
        for (int i = 0 i < S.length() ++i) :
            right = max(right, charLastIndex[S[i] - 'a'])
            if (i != right) :
              continue  
            ret.push_back(right - left + 1)
            left = right + 1
            right = left
        return ret
```
# 86. Partition List
* *Difficulty: Medium*
* *Topics: Linked List, Two Pointers*
* *Similar Questions:*
## Problem:
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example:
Input: head = 1-&gt4-&gt3-&gt2-&gt5-&gt2, x = 3
Output: 1-&gt2-&gt2-&gt4-&gt3-&gt5
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* partition(ListNode* head, int x) :
        ListNode* left = new ListNode(0)
        ListNode* right = new ListNode(0)
        ListNode* leftTail = left
        ListNode* rightTail = right
        while (head) :
            if (head->val < x) :
                leftTail->next = head
                leftTail = head
             else :
                rightTail->next = head
                rightTail = head
            head = head->next
        leftTail->next = right->next
        rightTail->next = nullptr
        return left->next
```
# 119. Pascal's Triangle II
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Pascal's Triangle](pascals-triangle.md)
## Problem:
Given a non-negative index k where k &le 33, return the kth index row of the Pascal&#39s triangle.
Note that the row index starts from 0.
In Pascal&#39s triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 3
Output: [1,3,3,1]
Follow up:
Could you optimize your algorithm to use only O(k) extra space?
## Solutions:
```python
class Solution :
public:
    vector getRow(int rowIndex) :
        vector row(rowIndex + 1)
        row[0] = 1
        for (int i = 1 i <= rowIndex ++i) :
            row[i] = 1
            for (int j = i-1 j > 0 --j) :
                row[j] = row[j] + row[j-1] 
        return row
```
# 118. Pascal's Triangle
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Pascal's Triangle II](pascals-triangle-ii.md)
## Problem:
Given a non-negative integer numRows, generate the first numRows of Pascal&#39s triangle.
In Pascal&#39s triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
## Solutions:
```python
class Solution :
public:
    vector> generate(int numRows) :
        vector> ret
        if (numRows < 1)    return ret
        ret.push_back(:1)
        for (int i = 1 i < numRows ++i) :
            vector row (i + 1, 1)
            for (int j = 1 j < i ++j) :
                row[j] = ret.back()[j-1] + ret.back()[j]
            ret.push_back(row)
        return ret
```
# 113. Path Sum II
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Path Sum](path-sum.md)
  * [Binary Tree Paths](binary-tree-paths.md)
  * [Path Sum III](path-sum-iii.md)
  * [Path Sum IV](path-sum-iv.md)
## Problem:
Given a binary tree and a sum, find all root-to-leaf paths where each path&#39s sum equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector> pathSum(TreeNode* root, int sum) :
        vector path
        vector> ret
        helper(root, sum, path, ret)
        return ret
    void helper(TreeNode* root, int sum, vector& path, vector>& ret) :
        if (root == nullptr)    return
        if (root->left == nullptr && root->right == nullptr) :
            if (sum == root->val) :
                path.push_back(root->val)
                ret.push_back(path)
                path.pop_back()
            return
        int val = root->val
        path.push_back(val)
        helper(root->left, sum - val, path, ret)
        helper(root->right, sum - val, path, ret)
        path.pop_back()
        return
```
# 437. Path Sum III
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Path Sum](path-sum.md)
  * [Path Sum II](path-sum-ii.md)
  * [Path Sum IV](path-sum-iv.md)
  * [Longest Univalue Path](longest-univalue-path.md)
## Problem:
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int pathSum(TreeNode* root, int sum) :
        if (root == nullptr)    return 0
        return helper(root, sum, 0) + pathSum(root->left, sum) + pathSum(root->right, sum)
    int helper(TreeNode* root, int sum, int path) :
        if (root == nullptr)    return 0
        int count = 0
        count += ((sum == path + root->val) ? 1 : 0)       
        count += helper(root->left, sum, path + root->val)
        count += helper(root->right, sum, path + root->val)
        return count
```
# 666. Path Sum IV
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Path Sum](path-sum.md)
  * [Path Sum II](path-sum-ii.md)
  * [Binary Tree Maximum Path Sum](binary-tree-maximum-path-sum.md)
  * [Path Sum III](path-sum-iii.md)
## Problem:
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
For each integer in this list:
	The hundreds digit represents the depth D of this node, 1 &lt= D &lt= 4.
	The tens digit represents the position P of this node in the level it belongs to, 1 &lt= P &lt= 8. The position is the same as that in a full binary tree.
	The units digit represents the value V of this node, 0 &lt= V &lt= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.
Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1
The path sum is (3 + 5) + (3 + 1) = 12.
Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1
The path sum is (3 + 1) = 4.
## Solutions:
```python
class Solution :
public:
    int pathSum(vector& nums) :
        if (nums.size() == 0)   return 0
        sort(nums.begin(), nums.end())
        int curLevel = 0
        vector curLevelVals = :0
        vector lastLevelVals
        vector> tree
        for (auto num : nums) :
            int level = num/100
            int pos = (num - level * 100)/10
            int val = num % 10
            if (level != curLevel) :
                tree.push_back(lastLevelVals)
                lastLevelVals = curLevelVals
                curLevelVals.clear()
                curLevelVals.resize(1 << (level - 1), -1)
                curLevel = level           
            :
                curLevelVals[pos-1] = val + lastLevelVals[(pos-1)/2]
        tree.push_back(lastLevelVals) // don't forget to include lastLevelVals
        tree.push_back(curLevelVals)
        int sum = 0
        for (int level = 0 level < tree.size() ++level) :
            for (int i = 0 i < tree[level].size() ++i) :
                if (tree[level][i] != -1 && (level == tree.size() - 1 || tree[level+1][2*i] == -1 && tree[level + 1][2*i + 1] == -1)) : // should also include leaf not at last level
                    sum += tree[level][i]
        return sum
```
# 112. Path Sum
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Path Sum II](path-sum-ii.md)
  * [Binary Tree Maximum Path Sum](binary-tree-maximum-path-sum.md)
  * [Sum Root to Leaf Numbers](sum-root-to-leaf-numbers.md)
  * [Path Sum III](path-sum-iii.md)
  * [Path Sum IV](path-sum-iv.md)
## Problem:
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5-&gt4-&gt11-&gt2 which sum is 22.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool hasPathSum(TreeNode* root, int sum) :
        if (root == nullptr)    return false
        if (root->left == nullptr && root->right == nullptr) :
            return root->val == sum
        return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val)
```
# 1331. Path with Maximum Gold
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
## Problem:
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
	Every time you are located in a cell you will collect all the gold in that cell.
	From your position you can walk one step to the left, right, up or down.
	You can&#39t visit the same cell more than once.
	Never visit a cell with 0 gold.
	You can start and stop collecting gold from any position in the grid that has some gold.
Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -&gt 8 -&gt 7.
Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -&gt 2 -&gt 3 -&gt 4 -&gt 5 -&gt 6 -&gt 7.
Constraints:
	1 &lt= grid.length, grid[i].length &lt= 15
	0 &lt= grid[i][j] &lt= 100
	There are at most 25 cells containing gold.
## Solutions:
```python
class Solution :
public:
    int getMaximumGold(vector>& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        int ret = 0
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] != 0) :
                    ret = max(ret, dfs(grid, m, n, i, j))
        return ret
private:
    int dfs(vector>& grid, int m, int n, int row, int col) :
        if (row = m || col = n || grid[row][col] == 0)   return 0
        int gold = grid[row][col]
        int sum = gold
        grid[row][col] = 0
        sum += max(max(dfs(grid, m, n, row + 1, col), dfs(grid, m, n, row - 1, col)), max(dfs(grid, m, n, row, col - 1), dfs(grid, m, n, row, col + 1)))
        grid[row][col] = gold
        return sum
```
# 284. Peeking Iterator
* *Difficulty: Medium*
* *Topics: Design*
* *Similar Questions:*
  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)
  * [Flatten 2D Vector](flatten-2d-vector.md)
  * [Zigzag Iterator](zigzag-iterator.md)
## Problem:
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
Example:
Assume that the iterator is initialized to the beginning of the list: [1,2,3].
Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
## Solutions:
```python
// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator :
    struct Data
	Data* data
public:
	Iterator(const vector& nums)
	Iterator(const Iterator& iter)
	virtual ~Iterator()
	// Returns the next element in the iteration.
	int next()
	// Returns true if the iteration has more elements.
	bool hasNext() const
class PeekingIterator : public Iterator :
public:
	PeekingIterator(const vector& nums) : Iterator(nums) :
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
        if (Iterator::hasNext()) :
            val = Iterator::next()
            end = false
         else :
            end = true
    // Returns the next element in the iteration without advancing the iterator.
	int peek() :
        return val
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() :
        if (!Iterator::hasNext()) :
            end = true
            return val
        int ret = val 
	    val = Iterator::next()
        return ret
	bool hasNext() const :
	    return !end
private:
    int val
    bool end
```
# 507. Perfect Number
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Self Dividing Numbers](self-dividing-numbers.md)
## Problem:
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself. 
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note:
The input number n will not exceed 100,000,000. (1e8)
## Solutions:
```python
class Solution :
public:
    bool checkPerfectNumber(int num) :
        if (num <= 1)   return false
        int sum = 1
        int root = sqrt(num)
        for (int i = 2 i <= root ++i) :
            if (num % i == 0) :
                sum += i + num / i
        if (root * root == num) :
            sum -= root
        return sum == num
```
# 279. Perfect Squares
* *Difficulty: Medium*
* *Topics: Math, Dynamic Programming, Breadth-first Search*
* *Similar Questions:*
  * [Count Primes](count-primes.md)
  * [Ugly Number II](ugly-number-ii.md)
## Problem:
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
## Solutions:
```python
class Solution :
public:
    int numSquares(int n) :
        queue q
        unordered_set visited
        q.push(n)
        visited.insert(n)
        int level = 0
        while(true) :
            ++level
            int size = q.size()
            for (int i = 0 i < size ++i) :
                int sum = q.front() q.pop()
                for (int sqrt = 1 sqrt <= sum/sqrt ++sqrt) :
                    if (sum == sqrt * sqrt) return level
                    int remaining = sum - sqrt * sqrt
                    if (visited.count(remaining) > 0)   continue
                    visited.insert(remaining)
                    q.push(remaining)
        return -1
```
# 567. Permutation in String
* *Difficulty: Medium*
* *Topics: Two Pointers, Sliding Window*
* *Similar Questions:*
  * [Minimum Window Substring](minimum-window-substring.md)
  * [Find All Anagrams in a String](find-all-anagrams-in-a-string.md)
## Problem:
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string&#39s permutations is the substring of the second string.
Example 1:
Input: s1 = &quotab&quot s2 = &quoteidbaooo&quot
Output: True
Explanation: s2 contains one permutation of s1 (&quotba&quot).
Example 2:
Input:s1= &quotab&quot s2 = &quoteidboaoo&quot
Output: False
Note:
	The input strings only contain lower case letters.
	The length of both given strings is in range [1, 10,000].
## Solutions:
```python
class Solution :
public:
    bool isPermutation(string s1, string s2) :
        if (s1.length() != s2.length()) return false
        int count[26] = :0
        for (char c : s1) :
            ++count[c - 'a']
        for (char c : s2) :
            if (--count[c - 'a'] < 0)   return false
        return true
    bool checkInclusion(string s1, string s2) :
        map charHash
        for (int i = 0 i < 26 ++i) :
            charHash['a' + i] = i * (i + 1)
        if (s2.length() < s1.length())  return false
        int hash1 = 0
        for (auto c : s1) :
            hash1 = (hash1 + charHash[c]) % MOD
        int hash2 = 0
        for (int i = 0 i < s1.length() - 1 ++i) :
            hash2 = (hash2 + charHash[s2[i]]) % MOD
        for (int i = s1.length() - 1 i < s2.length() ++i) :
            hash2 = (hash2 + charHash[s2[i]]) % MOD
            if (hash1 == hash2 && isPermutation(s1, s2.substr(i - s1.length() + 1, s1.length()))) :
                return true
            hash2 = (hash2 + MOD - charHash[s2[i - s1.length() + 1]]) % MOD 
        return false
private:
    int MOD = INT_MAX/2
```
# 60. Permutation Sequence
* *Difficulty: Medium*
* *Topics: Math, Backtracking*
* *Similar Questions:*
  * [Next Permutation](next-permutation.md)
  * [Permutations](permutations.md)
## Problem:
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
	&quot123&quot
	&quot132&quot
	&quot213&quot
	&quot231&quot
	&quot312&quot
	&quot321&quot
Given n and k, return the kth permutation sequence.
Note:
	Given n will be between 1 and 9 inclusive.
	Given k will be between 1 and n! inclusive.
Example 1:
Input: n = 3, k = 3
Output: &quot213&quot
Example 2:
Input: n = 4, k = 9
Output: &quot2314&quot
## Solutions:
```python
class Solution :
public:
    string getPermutation(int n, int k) :
        string digits = "123456789"
        digits = digits.substr(0, n)
        if (n == 1) return "1"
        int base = 1
        for (int i = 1 i < n ++i) :
            base *= i
       helper(digits, base, k - 1)
        return ret
    void helper(string& digits, int base, int k) :
        cout << base << endl
       if (digits.length() == 0)    return 
        int index = k/base
        ret.push_back(digits[index])
        digits.erase(index, 1)
        if (digits.length() == 1) :
            ret.push_back(digits[0])
            return
        int newBase = base/(digits.length())
        helper(digits, newBase, k - index * base)
private:
    string ret
```
# 47. Permutations II
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [Next Permutation](next-permutation.md)
  * [Permutations](permutations.md)
  * [Palindrome Permutation II](palindrome-permutation-ii.md)
  * [Number of Squareful Arrays](number-of-squareful-arrays.md)
## Problem:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
## Solutions:
```python
class Solution :
public:
    vector> permuteUnique(vector& nums) :
        //sort(nums.begin(), nums.end())
        vector> ret
        helper(nums, 0, ret)
        return ret
    void helper(vector& nums, int pos, vector>& ret) :
        if (pos == nums.size()) :
            ret.push_back(nums)
            return
        unordered_set seen //Use index is not able to deduplicate. for example [0,0,1,2]. If the last element swap with the first, the list becomes [2, 0, 1, 0], which elements with the same value are not adjecent. 
        for (int i = pos i < nums.size() ++i) :
            if (seen.count(nums[i]) > 0)    continue
            seen.insert(nums[i])
            swap(nums[pos], nums[i])
            helper(nums, pos + 1, ret)
            swap(nums[pos], nums[i])
```
# 46. Permutations
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
  * [Next Permutation](next-permutation.md)
  * [Permutations II](permutations-ii.md)
  * [Permutation Sequence](permutation-sequence.md)
  * [Combinations](combinations.md)
## Problem:
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
## Solutions:
```python
class Solution :
public:
    vector> permute(vector& nums) :
        vector> ret
        vector path
        helper(nums, 0, ret)
        return ret
    void helper(vector& nums, int pos, vector>& ret) :
        if (nums.size() == pos) :
            ret.push_back(nums)
            return
        for (int i = pos i < nums.size() ++i) :
            swap(nums[pos], nums[i])
            helper(nums, pos + 1, ret)
            swap(nums[pos], nums[i])
```
# 1329. Play with Chips
* *Difficulty: Easy*
* *Topics: Array, Math, Greedy*
* *Similar Questions:*
## Problem:
There are some chips, and the i-th chip is at position chips[i].
You can perform any of the two following types of moves any number of times (possibly zero) on any chip:
	Move the i-th chip by 2 units to the left or to the right with a cost of 0.
	Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
There can be two or more chips at the same position initially.
Return the minimum cost needed to move all the chips to the same position (any position).
Example 1:
Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
Example 2:
Input: chips = [2,2,2,3,3]
Output: 2
Explanation: Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
Constraints:
	1 &lt= chips.length &lt= 100
	1 &lt= chips[i] &lt= 10^9
## Solutions:
```python
class Solution :
public:
    int minCostToMoveChips(vector& chips) :
        int evenCount = 0
        int oddCount = 0
        for (auto& chip : chips) :
            if (chip % 2 == 0) :
                ++evenCount
             else :
                ++oddCount
        return min(evenCount, oddCount)
```
# 66. Plus One
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Multiply Strings](multiply-strings.md)
  * [Add Binary](add-binary.md)
  * [Plus One Linked List](plus-one-linked-list.md)
  * [Add to Array-Form of Integer](add-to-array-form-of-integer.md)
## Problem:
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
## Solutions:
```python
class Solution :
public:
    vector plusOne(vector& digits) :
        int carry = 1
        for (int i = digits.size() -1 carry > 0 && i >= 0 --i) :
            digits[i] += carry
            carry = digits[i]/10
            digits[i] %= 10
        if (carry == 1) :
            digits.insert(digits.begin(), 1) // how to insert at head
        return digits
```
# 458. Poor Pigs
* *Difficulty: Hard*
* *Topics: Math*
* *Similar Questions:*
## Problem:
There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?
Answer this question, and write an algorithm for the general case.
General case: 
If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.
Note:
	A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
	After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. During this time, only observation is allowed and no feedings at all.
	Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).
## Solutions:
```python
class Solution :
  public:
  int poorPigs(int buckets, int minutesToDie, int minutesToTest) :
    int states = minutesToTest / minutesToDie + 1
    return ceil(log(buckets) / log(states))
```
# 117. Populating Next Right Pointers in Each Node II
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Populating Next Right Pointers in Each Node](populating-next-right-pointers-in-each-node.md)
## Problem:
Given a binary tree
struct Node :
  int val
  Node *left
  Node *right
  Node *next
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Example:
Input: :&quot$id&quot:&quot1&quot,&quotleft&quot::&quot$id&quot:&quot2&quot,&quotleft&quot::&quot$id&quot:&quot3&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:4,&quotnext&quot:null,&quotright&quot::&quot$id&quot:&quot4&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:5,&quotval&quot:2,&quotnext&quot:null,&quotright&quot::&quot$id&quot:&quot5&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot::&quot$id&quot:&quot6&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:7,&quotval&quot:3,&quotval&quot:1
Output: :&quot$id&quot:&quot1&quot,&quotleft&quot::&quot$id&quot:&quot2&quot,&quotleft&quot::&quot$id&quot:&quot3&quot,&quotleft&quot:null,&quotnext&quot::&quot$id&quot:&quot4&quot,&quotleft&quot:null,&quotnext&quot::&quot$id&quot:&quot5&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:7,&quotright&quot:null,&quotval&quot:5,&quotright&quot:null,&quotval&quot:4,&quotnext&quot::&quot$id&quot:&quot6&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot::&quot$ref&quot:&quot5&quot,&quotval&quot:3,&quotright&quot::&quot$ref&quot:&quot4&quot,&quotval&quot:2,&quotnext&quot:null,&quotright&quot::&quot$ref&quot:&quot6&quot,&quotval&quot:1
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
Note:
	You may only use constant extra space.
	Recursive approach is fine, implicit stack space does not count as extra space for this problem.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    Node* left
    Node* right
    Node* next
    Node() :
    Node(int _val, Node* _left, Node* _right, Node* _next) :
        val = _val
        left = _left
        right = _right
        next = _next
*/
class Solution :
public:
    Node* connect(Node* root) :
        if (root == nullptr)    return nullptr
        Node* dummyHead = new Node(0, nullptr, nullptr, nullptr)
        Node* nextDummyHead = new Node(0, nullptr, nullptr, nullptr)
        dummyHead->next = root
        while (dummyHead->next != nullptr) :
            Node* cur = dummyHead->next
            Node* nextTail = nextDummyHead
            while (cur) :
                if (cur->left) :
                    nextTail->next = cur->left
                    nextTail = nextTail->next
                if (cur->right) :
                    nextTail->next = cur->right
                    nextTail = nextTail->next
                cur = cur->next
            dummyHead->next = nextDummyHead->next
            nextDummyHead->next = nullptr
        return root
```
# 116. Populating Next Right Pointers in Each Node
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Populating Next Right Pointers in Each Node II](populating-next-right-pointers-in-each-node-ii.md)
  * [Binary Tree Right Side View](binary-tree-right-side-view.md)
## Problem:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node :
  int val
  Node *left
  Node *right
  Node *next
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Example:
Input: :&quot$id&quot:&quot1&quot,&quotleft&quot::&quot$id&quot:&quot2&quot,&quotleft&quot::&quot$id&quot:&quot3&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:4,&quotnext&quot:null,&quotright&quot::&quot$id&quot:&quot4&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:5,&quotval&quot:2,&quotnext&quot:null,&quotright&quot::&quot$id&quot:&quot5&quot,&quotleft&quot::&quot$id&quot:&quot6&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:6,&quotnext&quot:null,&quotright&quot::&quot$id&quot:&quot7&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:7,&quotval&quot:3,&quotval&quot:1
Output: :&quot$id&quot:&quot1&quot,&quotleft&quot::&quot$id&quot:&quot2&quot,&quotleft&quot::&quot$id&quot:&quot3&quot,&quotleft&quot:null,&quotnext&quot::&quot$id&quot:&quot4&quot,&quotleft&quot:null,&quotnext&quot::&quot$id&quot:&quot5&quot,&quotleft&quot:null,&quotnext&quot::&quot$id&quot:&quot6&quot,&quotleft&quot:null,&quotnext&quot:null,&quotright&quot:null,&quotval&quot:7,&quotright&quot:null,&quotval&quot:6,&quotright&quot:null,&quotval&quot:5,&quotright&quot:null,&quotval&quot:4,&quotnext&quot::&quot$id&quot:&quot7&quot,&quotleft&quot::&quot$ref&quot:&quot5&quot,&quotnext&quot:null,&quotright&quot::&quot$ref&quot:&quot6&quot,&quotval&quot:3,&quotright&quot::&quot$ref&quot:&quot4&quot,&quotval&quot:2,&quotnext&quot:null,&quotright&quot::&quot$ref&quot:&quot7&quot,&quotval&quot:1
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
Note:
	You may only use constant extra space.
	Recursive approach is fine, implicit stack space does not count as extra space for this problem.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val
    Node* left
    Node* right
    Node* next
    Node() :
    Node(int _val, Node* _left, Node* _right, Node* _next) :
        val = _val
        left = _left
        right = _right
        next = _next
*/
class Solution :
public:
    Node* connect(Node* root) :
        if (root == nullptr)    return root
        if (root->left == nullptr && root->right == nullptr)    return root
        Node* rightMostNode = nullptr
        if (root->left != nullptr && root->right != nullptr) :
            root->left->next = root->right
            rightMostNode = root->right
         else if (root->left != nullptr) :
            rightMostNode = root->left
         else :
            rightMostNode = root->right
        if (root->next == nullptr)
            rightMostNode->next = nullptr
        else :
            rightMostNode->next = (root->next->left ? root->next->left : root->next->right)
        root->right = connect(root->right)
        root->left = connect(root->left)
        return root      
```
# 342. Power of Four
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Power of Two](power-of-two.md)
  * [Power of Three](power-of-three.md)
## Problem:
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example 1:
Input: 16
Output: true
Example 2:
Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
## Solutions:
```python
class Solution :
public:
    bool isPowerOfFour(int num) :
        return num > 0 && ((num & (num - 1)) == 0) && ((num & 0x55555555) != 0)
```
# 326. Power of Three
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Power of Two](power-of-two.md)
  * [Power of Four](power-of-four.md)
## Problem:
Given an integer, write a function to determine if it is a power of three.
Example 1:
Input: 27
Output: true
Example 2:
Input: 0
Output: false
Example 3:
Input: 9
Output: true
Example 4:
Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
## Solutions:
```python
class Solution :
public:
    bool isPowerOfThree(int n) :
        if (n <= 0) return false
        int largest = 3
        while (largest <= INT_MAX/3) :
            largest *= 3
        return largest % n == 0
```
# 231. Power of Two
* *Difficulty: Easy*
* *Topics: Math, Bit Manipulation*
* *Similar Questions:*
  * [Number of 1 Bits](number-of-1-bits.md)
  * [Power of Three](power-of-three.md)
  * [Power of Four](power-of-four.md)
## Problem:
Given an integer, write a function to determine if it is a power of two.
Example 1:
Input: 1
Output: true 
Explanation: 20 = 1
Example 2:
Input: 16
Output: true
Explanation: 24 = 16
Example 3:
Input: 218
Output: false
## Solutions:
```python
class Solution :
public:
    bool isPowerOfTwo(int n) :
        return n > 0 && ((n & (n-1)) == 0)
```
# 50. Pow(x, n)
* *Difficulty: Medium*
* *Topics: Math, Binary Search*
* *Similar Questions:*
  * [Sqrt(x)](sqrtx.md)
  * [Super Pow](super-pow.md)
## Problem:
Implement pow(x, n), which calculates x raised to the power n (xn).
Example 1:
Input: 2.00000, 10
Output: 1024.00000
Example 2:
Input: 2.10000, 3
Output: 9.26100
Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:
	-100.0 &lt x &lt 100.0
	n is a 32-bit signed integer, within the range [&minus231, 231 &minus 1]
## Solutions:
```python
class Solution :
public:
    double myPow(double x, int n) :
        if (n == 0) return 1
        if (n == 1) return x
        if (n == -1)    return 1/x
        double sqrt = myPow(x, n/2) // we should not call two myPow twice! Otherwise time limit exceeds. 
        return sqrt * sqrt * myPow(x, n - n/2 - n/2) 
```
# 1279. Prime Arrangements
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
## Problem:
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7.
Example 1:
Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:
Input: n = 100
Output: 682289015
Constraints:
	1 &lt= n &lt= 100
## Solutions:
```python
class Solution :
public:
    int numPrimeArrangements(int n) :
        int prime = primeCount(n)
        long ret = 1
        for (int i = 2 i <= prime ++i) :
            ret = (ret * i) % MOD
        for (int i = 2 i <= n - prime ++i) :
            ret = (ret * i) % MOD
        return ret
private:
    int primeCount(int n) :
        int count = 0
        for (int i = 2 i <= n ++i) :
            if (isPrime(i)) ++count
        return count
    bool isPrime(int num) :
        for (int i = 2 i <= sqrt(num) ++i) :
            if (num % i == 0)   return false
        return true
    const int MOD = 1e9 + 7
```
# 655. Print Binary Tree
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Print a binary tree in an m*n 2D string array following these rules: 
The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them. 
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note:
The height of binary tree is in the range of [1, 10].
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector> printTree(TreeNode* root) :
        if (root == nullptr)    return :
        int height = getHeight(root)
        vector> ret (height, vector((1 << height) - 1, ""))
        printHelper(root, 0, 0, (1 << height) - 2, ret)
        return ret
private:
    int getHeight(TreeNode* root) :
        if (root == nullptr)    return 0
        return 1 + max(getHeight(root->left), getHeight(root->right))
    void printHelper(TreeNode* root, int level, int left, int right, vector>& ret) :
        if (root == nullptr)    return
        int mid = left + (right - left) / 2
        ret[level][mid] = to_string(root->val)
        printHelper(root->left, level + 1, left, mid - 1, ret)
        printHelper(root->right, level + 1, mid + 1, right, ret)
```
# 238. Product of Array Except Self
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Trapping Rain Water](trapping-rain-water.md)
  * [Maximum Product Subarray](maximum-product-subarray.md)
  * [Paint House II](paint-house-ii.md)
## Problem:
Given an array nums of n integers where n &gt 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
## Solutions:
```python
class Solution :
public:
    vector productExceptSelf(vector& nums) :
        int n = nums.size()
        vector ret (n, 1)
        for (int i = n - 2 i >= 0 --i) :
            ret[i] *= ret[i + 1] * nums[i + 1]
        int product = 1
        for (int i = 0 i < n ++i) :
            ret[i] *= product
            product *= nums[i]
        return ret
```
# 406. Queue Reconstruction by Height
* *Difficulty: Medium*
* *Topics: Greedy*
* *Similar Questions:*
  * [Count of Smaller Numbers After Self](count-of-smaller-numbers-after-self.md)
## Problem:
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
Note:
The number of people is less than 1,100.
Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
## Solutions:
```python
class Solution :
public:
    vector> reconstructQueue(vector>& people) :
        auto comparator = [](const vector& person1, const vector& person2) :
            return person1[0] == person2[0] ? person1[1]  person2[0]  
        sort(people.begin(), people.end(), comparator)
        vector> ret
        for (auto& person : people) :
            ret.insert(ret.begin() + person[1], person)
        return ret
```
# 398. Random Pick Index
* *Difficulty: Medium*
* *Topics: Reservoir Sampling*
* *Similar Questions:*
  * [Linked List Random Node](linked-list-random-node.md)
  * [Random Pick with Blacklist](random-pick-with-blacklist.md)
  * [Random Pick with Weight](random-pick-with-weight.md)
## Problem:
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.
Example:
int[] nums = new int[] :1,2,3,3,3
Solution solution = new Solution(nums)
// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3)
// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1)
## Solutions:
```python
class Solution :
public:
    Solution(vector& nums) :
        this->nums = nums
    int pick(int target) :
        int count = 0
        int ret
        for (int i = 0 i < nums.size() ++i) :
            if (nums[i] != target)  continue
            ++count
            if (rand() % count == 0) :
                ret = i
        return ret
private:
    vector nums
/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums)
 * int param_1 = obj->pick(target)
 */
```
# 912. Random Pick with Weight
* *Difficulty: Medium*
* *Topics: Binary Search, Random*
* *Similar Questions:*
  * [Random Pick Index](random-pick-index.md)
  * [Random Pick with Blacklist](random-pick-with-blacklist.md)
  * [Random Point in Non-overlapping Rectangles](random-point-in-non-overlapping-rectangles.md)
## Problem:
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
Note:
	1 &lt= w.length &lt= 10000
	1 &lt= w[i] &lt= 10^5
	pickIndex will be called at most 10000 times.
Example 1:
Input: 
[&quotSolution&quot,&quotpickIndex&quot]
[[[1]],[]]
Output: [null,0]
Example 2:
Input: 
[&quotSolution&quot,&quotpickIndex&quot,&quotpickIndex&quot,&quotpickIndex&quot,&quotpickIndex&quot,&quotpickIndex&quot]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution&#39s constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren&#39t any.
## Solutions:
```python
class Solution :
public:
    Solution(vector& w) :
        sum = 0
        for (int i = 0 i < w.size() ++i) :
            sum += w[i]
            prefixSums[sum] = i
    int pickIndex() :
        int r = (rand() % sum) + 1
        return prefixSums.lower_bound(r)->second
private:
    map prefixSums
    int sum
/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w)
 * int param_1 = obj->pickIndex()
 */
```
# 598. Range Addition II
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Range Addition](range-addition.md)
## Problem:
Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0  and 0 . 
You need to count and return the number of maximum integers in the matrix after performing all the operations.
Example 1:
Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation: 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]
After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]
So the maximum integer in M is 2, and there are four of it in M. So return 4.
Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.
## Solutions:
```python
class Solution :
public:
    int maxCount(int m, int n, vector>& ops) :
        int row = m
        int col = n
        for (auto& op : ops) :
            row = min(row, op[0])
            col = min(col, op[1])
        return (row) * (col)
```
# 370. Range Addition
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Range Addition II](range-addition-ii.md)
## Problem:
Assume you have an array of length n initialized with all 0&#39s and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.
Example:
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:
Initial state:
[0,0,0,0,0]
After applying operation [1,3,2]:
[0,2,2,2,0]
After applying operation [2,4,3]:
[0,2,5,5,3]
After applying operation [0,2,-2]:
[-2,0,3,5,3]
## Solutions:
```python
class Solution :
public:
    vector getModifiedArray(int length, vector>& updates) :
        vector addition(length, 0)
        for (auto& update : updates) :
            int startIndex = update[0]
            int endIndex = update[1]
            int inc = update[2]
            addition[endIndex] += inc
            if (startIndex - 1 >= 0) :
                addition[startIndex - 1] -= inc
        vector ret(length, 0)
        for (int i = length - 1 i > 0 --i) :
            ret[i] = addition[i]
            addition[i-1] += addition[i]
        return addition
```
# 975. Range Sum of BST
* *Difficulty: Easy*
* *Topics: Tree, Recursion*
* *Similar Questions:*
## Problem:
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.
Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
Note:
	The number of nodes in the tree is at most 10000.
	The final answer is guaranteed to be less than 2^31.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int rangeSumBST(TreeNode* root, int L, int R) :
        if (root == nullptr)    return 0
        int sum = (root->val >= L && root->val val : 0)
        if (root->val >= L) :
            sum += rangeSumBST(root->left, L, R)
        if (root->val <= R) :
            sum += rangeSumBST(root->right, L, R)
        return sum
```
# 303. Range Sum Query - Immutable
* *Difficulty: Easy*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Range Sum Query 2D - Immutable](range-sum-query-2d-immutable.md)
  * [Range Sum Query - Mutable](range-sum-query-mutable.md)
  * [Maximum Size Subarray Sum Equals k](maximum-size-subarray-sum-equals-k.md)
## Problem:
Given an integer array nums, find the sum of the elements between indices i and j (i &le j), inclusive.
Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
## Solutions:
```python
class NumArray :
public:
    NumArray(vector& nums) :
        int sum = 0
        for (int i = 0 i < nums.size() ++i) :
            sum += nums[i]
            prefixSum.push_back(sum)
    int sumRange(int i, int j) :
        if (i == 0) return prefixSum[j]
        return prefixSum[j] - prefixSum[i - 1]
private:
    vector prefixSum
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums)
 * int param_1 = obj->sumRange(i,j)
 */
```
# 307. Range Sum Query - Mutable
* *Difficulty: Medium*
* *Topics: Binary Indexed Tree, Segment Tree*
* *Similar Questions:*
  * [Range Sum Query - Immutable](range-sum-query-immutable.md)
  * [Range Sum Query 2D - Mutable](range-sum-query-2d-mutable.md)
## Problem:
Given an integer array nums, find the sum of the elements between indices i and j (i &le j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]
sumRange(0, 2) -&gt 9
update(1, 2)
sumRange(0, 2) -&gt 8
Note:
	The array is only modifiable by the update function.
	You may assume the number of calls to update and sumRange function is distributed evenly.
## Solutions:
```python
class NumArray :
public:
    NumArray(vector& nums) :
        int n = nums.size()
        bits = vector (n+1 , 0)
        this->nums = vector (n, 0) // don't reuse the name
        for (int i = 0 i < nums.size() ++i) :
            update(i, nums[i])
    void update(int i, int val) :
        int diff = val - nums[i]
        nums[i] = val
        add(i + 1, diff)
    void add(int i, int diff) :
        while (i <= nums.size()) :
            bits[i] += diff
            i += lowbit(i)
    int sum(int i) :
        int sum = 0
        while (i > 0) :
            sum += bits[i]
            i -= lowbit(i)
        return sum
    int sumRange(int i, int j) :
        return sum(j + 1) - sum(i)
    inline int lowbit(int i) :
        return i & (-i)
private:
    vector bits
    vector nums
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums)
 * obj->update(i,val)
 * int param_2 = obj->sumRange(i,j)
 */
```
# 383. Ransom Note
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Stickers to Spell Word](stickers-to-spell-word.md)
## Problem:
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines  otherwise, it will return false. 
Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
## Solutions:
```python
class Solution :
public:
    bool canConstruct(string ransomNote, string magazine) :
        unordered_map m
        for (char c : magazine) ++m[c]
        for (char c : ransomNote) :
            if (--m[c] < 0) return false
        return true
```
# 158. Read N Characters Given Read4 II - Call multiple times
* *Difficulty: Hard*
* *Topics: String*
* *Similar Questions:*
  * [Read N Characters Given Read4](read-n-characters-given-read4.md)
## Problem:
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.
Method read4: 
The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.
Definition of read4:
    Parameter:  char[] buf
    Returns:    int
Note: buf[] is destination not source, the results from read4 will be copied to buf[]
Below is a high level example of how read4 works:
File file(&quotabcdefghijk&quot) // File is &quotabcdefghijk&quot, initially file pointer (fp) points to &#39a&#39
char[] buf = new char[4] // Create buffer with enough space to store characters
read4(buf) // read4 returns 4. Now buf = &quotabcd&quot, fp points to &#39e&#39
read4(buf) // read4 returns 4. Now buf = &quotefgh&quot, fp points to &#39i&#39
read4(buf) // read4 returns 3. Now buf = &quotijk&quot, fp points to end of file
Method read:
By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.
The return value is the number of actual characters read.
Definition of read: 
    Parameters:	char[] buf, int n
    Returns:	int
Note: buf[] is destination not source, you will need to write the results to buf[]
Example 1:
File file(&quotabc&quot)
Solution sol
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1) // After calling your read method, buf should contain &quota&quot. We read a total of 1 character from the file, so return 1.
sol.read(buf, 2) // Now buf should contain &quotbc&quot. We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1) // We have reached the end of file, no more characters can be read. So return 0.
Example 2:
File file(&quotabc&quot)
Solution sol
sol.read(buf, 4) // After calling your read method, buf should contain &quotabc&quot. We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1) // We have reached the end of file, no more characters can be read. So return 0.
Note:
	Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
	The read function may be called multiple times.
	Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
	You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
	It is guaranteed that in a given test case the same buffer buf is called by read.
## Solutions:
```python
// Forward declaration of the read4 API.
int read4(char *buf)
class Solution :
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) :
        int count = 0
        while (count < n) :
            if (pos == tail) :
                tail = read4(readBuf)
                pos = 0
                if (tail == 0)  return count
            int readCount = min(tail - pos, n - count)
            memcpy(buf + count, readBuf + pos, readCount)
            pos += readCount
            count += readCount
        return n
private:
    char readBuf[4]
    int pos = 0
    int tail = 0
```
# 157. Read N Characters Given Read4
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Read N Characters Given Read4 II - Call multiple times](read-n-characters-given-read4-ii-call-multiple-times.md)
## Problem:
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.
Method read4: 
The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.
Definition of read4:
    Parameter:  char[] buf
    Returns:    int
Note: buf[] is destination not source, the results from read4 will be copied to buf[]
Below is a high level example of how read4 works:
File file(&quotabcdefghijk&quot) // File is &quotabcdefghijk&quot, initially file pointer (fp) points to &#39a&#39
char[] buf = new char[4] // Create buffer with enough space to store characters
read4(buf) // read4 returns 4. Now buf = &quotabcd&quot, fp points to &#39e&#39
read4(buf) // read4 returns 4. Now buf = &quotefgh&quot, fp points to &#39i&#39
read4(buf) // read4 returns 3. Now buf = &quotijk&quot, fp points to end of file
Method read:
By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.
The return value is the number of actual characters read.
Definition of read: 
    Parameters:	char[] buf, int n
    Returns:	int
Note: buf[] is destination not source, you will need to write the results to buf[]
Example 1:
Input: file = &quotabc&quot, n = 4
Output: 3
Explanation: After calling your read method, buf should contain &quotabc&quot. We read a total of 3 characters from the file, so return 3. Note that &quotabc&quot is the file&#39s content, not buf. buf is the destination buffer that you will have to write the results to.
Example 2:
Input: file = &quotabcde&quot, n = 5
Output: 5
Explanation: After calling your read method, buf should contain &quotabcde&quot. We read a total of 5 characters from the file, so return 5.
Example 3:
Input: file = &quotabcdABCD1234&quot, n = 12
Output: 12
Explanation: After calling your read method, buf should contain &quotabcdABCD1234&quot. We read a total of 12 characters from the file, so return 12.
Example 4:
Input: file = &quotleetcode&quot, n = 5
Output: 5
Explanation: After calling your read method, buf should contain &quotleetc&quot. We read a total of 5 characters from the file, so return 5.
Note:
	Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
	The read function will only be called once for each test case.
	You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
## Solutions:
```python
// Forward declaration of the read4 API.
int read4(char *buf)
class Solution :
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) :
        int count = 0
        char readBuf[4]
        while (count + 4 < n) :
            int readCount = read4(buf + count)
            if (readCount == 0) return count
            count += readCount
        int readCount = read4(readBuf)
        if (count + readCount >= n) :
            memcpy(buf + count, readBuf, n - count)
            return n
         else :
            memcpy(buf + count, readBuf, readCount)
            return count + readCount
```
# 358. Rearrange String k Distance Apart
* *Difficulty: Hard*
* *Topics: Hash Table, Heap, Greedy*
* *Similar Questions:*
  * [Task Scheduler](task-scheduler.md)
  * [Reorganize String](reorganize-string.md)
## Problem:
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string &quot&quot.
Example 1:
Input: s = &quotaabbcc&quot, k = 3
Output: &quotabcabc&quot 
Explanation: The same letters are at least distance 3 from each other.
Example 2:
Input: s = &quotaaabc&quot, k = 3
Output: &quot&quot 
Explanation: It is not possible to rearrange the string.
Example 3:
Input: s = &quotaaadbbcc&quot, k = 2
Output: &quotabacabcd&quot
Explanation: The same letters are at least distance 2 from each other.
## Solutions:
```python
class Solution :
public:
    string rearrangeString(string s, int k) :
        if (k <= 0) return s // This special case if important
        if (s.length() == 0)    return s
        int len = s.length()
        unordered_map charCount
        for (auto c : s) :
            ++charCount[c]
        vector chars
        for (auto& entry : charCount) :
            chars.push_back(entry.first)
        sort(chars.begin(), chars.end(), [charCount](char c1, char c2) :
           return charCount.at(c1) > charCount.at(c2) 
        )
        int maxVal = charCount[chars[0]]
        int maxCount = 0
        for (int i = 0 i < chars.size() && charCount[chars[i]] == maxVal ++i) ++maxCount
        if (len < (k * (maxVal - 1) + maxCount)) return ""
        vector matrix(maxVal - 1)
        int pos = 0
        for (int i = maxCount i < chars.size() ++i) :
            for (int j = 0 j < charCount[chars[i]] ++j) :
                matrix[pos%(maxVal - 1)].push_back(chars[i])
                ++pos
        string ret
        string maxStr
        for (int i = 0 i < maxCount ++i) :
            maxStr.push_back(chars[i])
        for (int i = 0 i < maxVal - 1 ++i) :
            ret.append(maxStr)
            ret.append(matrix[i])
        ret.append(maxStr)
        return ret
```
# 99. Recover Binary Search Tree
* *Difficulty: Hard*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
## Problem:
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
Example 1:
Input: [1,3,null,null,2]
   1
  /
 3
  \
   2
Output: [3,1,null,null,2]
   3
  /
 1
  \
   2
Example 2:
Input: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
Output: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3
Follow up:
	A solution using O(n) space is pretty straight forward.
	Could you devise a constant space solution?
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    void recoverTree(TreeNode* root) :
        vector nodes
        inOrder(root, nodes)
        TreeNode* first = nullptr
        TreeNode* second = nullptr
        for (int i = 1 i < nodes.size() ++i) :
            if (nodes[i]->val val) :
                if (first == nullptr) :
                    first = nodes[i-1]
                    second = nodes[i]
                 else :
                    second = nodes[i]
        swap(first->val, second->val)
private:
    void inOrder(TreeNode* root, vector& nodes) :
        if (root == nullptr)    return
        inOrder(root->left, nodes)
        nodes.push_back(root)
        inOrder(root->right, nodes)
```
# 223. Rectangle Area
* *Difficulty: Medium*
* *Topics: Math*
* *Similar Questions:*
  * [Rectangle Overlap](rectangle-overlap.md)
## Problem:
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:
Assume that the total area is never beyond the maximum possible value of int.
## Solutions:
```python
class Solution :
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) :
        return - overlap(A, C, E, G) * overlap(F, H, B, D) + area(C - A, D - B) + area(G - E, H - F)
    int overlap(int start1, int end1, int start2, int end2) :
        if (start1 > start2) :
            swap(start1, start2)
            swap(end1, end2)
        return min(end1 >= start2 ? end1 - start2 : 0, end2 - start2)
    int area(int a, int b) :
        return a * b
```
# 866. Rectangle Overlap
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Rectangle Area](rectangle-area.md)
## Problem:
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.
Given two (axis-aligned) rectangles, return whether they overlap.
Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:
	Both rectangles rec1 and rec2 are lists of 4 integers.
	All coordinates in rectangles will be between -10^9 and 10^9.
## Solutions:
```python
class Solution :
public:
    bool isRectangleOverlap(vector& rec1, vector& rec2) :
        return overlap(rec1[0], rec1[2], rec2[0], rec2[2]) && overlap(rec1[1], rec1[3], rec2[1], rec2[3])
private:
    bool overlap(int left1, int right1, int left2, int right2) :
        return left2 >= left1 && left2 = left2 && left1 < right2
```
# 684. Redundant Connection
* *Difficulty: Medium*
* *Topics: Tree, Union Find, Graph*
* *Similar Questions:*
  * [Redundant Connection II](redundant-connection-ii.md)
  * [Accounts Merge](accounts-merge.md)
## Problem:
In this problem, a tree is an undirected graph that is connected and has no cycles.
The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.  The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
The resulting graph is given as a 2D-array of edges.  Each element of edges is a pair [u, v] with u , that represents an undirected edge connecting nodes u and v.
Return an edge that can be removed so that the resulting graph is a tree of N nodes.  If there are multiple answers, return the answer that occurs last in the given 2D-array.  The answer edge [u, v] should be in the same format, with u .
Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
## Solutions:
```python
class Solution :
public:
    class UF :
        public:
            bool isConnected(int a, int b) :
                return findParents(a) == findParents(b)
            void connect(int a, int b) :
                int rootA = findParents(a)
                int rootB = findParents(b)
                parents[rootA] = rootB
            int findParents(int a) :
                if (parents.count(a) == 0 || parents[a] == a) : // check whether parents[a] == a otherwise infinite resursion. 
                    parents[a] = a
                 else :
                    parents[a] = findParents(parents[a])
                return parents[a]
        private:
            unordered_map parents
    vector findRedundantConnection(vector>& edges) :
        UF uf
        for (auto& edge : edges) :
            if (uf.isConnected(edge[0], edge[1]))   return edge
            else :
                uf.connect(edge[0], edge[1])
        return :
```
# 999. Regions Cut By Slashes
* *Difficulty: Medium*
* *Topics: Depth-first Search, Union Find, Graph*
* *Similar Questions:*
## Problem:
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.
(Note that backslash characters are escaped, so a \ is represented as &quot\\&quot.)
Return the number of regions.
Example 1:
Input:
[
  &quot /&quot,
  &quot/ &quot
]
Output: 2
Explanation: The 2x2 grid is as follows:
Example 2:
Input:
[
  &quot /&quot,
  &quot  &quot
]
Output: 1
Explanation: The 2x2 grid is as follows:
Example 3:
Input:
[
  &quot\\/&quot,
  &quot/\\&quot
]
Output: 4
Explanation: (Recall that because \ characters are escaped, &quot\\/&quot refers to \/, and &quot/\\&quot refers to /\.)
The 2x2 grid is as follows:
Example 4:
Input:
[
  &quot/\\&quot,
  &quot\\/&quot
]
Output: 5
Explanation: (Recall that because \ characters are escaped, &quot/\\&quot refers to /\, and &quot\\/&quot refers to \/.)
The 2x2 grid is as follows:
Example 5:
Input:
[
  &quot//&quot,
  &quot/ &quot
]
Output: 3
Explanation: The 2x2 grid is as follows:
Note:
	1 &lt= grid.length == grid[0].length &lt= 30
	grid[i][j] is either &#39/&#39, &#39\&#39, or &#39 &#39.
## Solutions:
```python
class Solution :
public:
    class UF :
    public:
        bool exist(int a) :
            return parents.count(a) > 0
        int getSize() :
            return size
        void add(int a) :
            parents[a] = a
            ++size
        void connect(int a, int b) :
            int rootA = find(a)
            int rootB = find(b)
            if (rootA != rootB) :
                parents[rootA] = rootB
                --size
        int find(int x) :
            if (parents.count(x) == 0) :
                parents[x] = x
                ++size
            if (parents[x] != x) :
                parents[x] = find(parents[x])
            return parents[x]
    private:
        map parents
        int size = 0
    int regionsBySlashes(vector& grid) :
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].size()
        if (n == 0) return 0
        UF uf
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                char c = grid[i][j]
                int gridId = i * n + j
                if (c == '/') :
                    uf.connect(gridId * 4 + 0, gridId * 4 + 1) // left and up
                    uf.connect(gridId * 4 + 2, gridId * 4 + 3) // right and down
                 else if (c == '\\') :
                    uf.connect(gridId * 4 + 0, gridId * 4 + 3) // left and down
                    uf.connect(gridId * 4 + 1, gridId * 4 + 2) // up and right
                 else :
                    uf.connect(gridId * 4 + 0, gridId * 4 + 1)
                    uf.connect(gridId * 4 + 0, gridId * 4 + 2)
                    uf.connect(gridId * 4 + 0, gridId * 4 + 3) 
                if (i > 0) :
                    uf.connect(gridId * 4 + 1, ((i - 1) * n + j) * 4 + 3)
                if (i < m - 1) :
                    uf.connect(gridId * 4 + 3, ((i + 1) * n + j) * 4 + 1)
                if (j > 0) :
                    uf.connect(gridId * 4 + 0, (i * n + j - 1) * 4 + 2)
                if (j < n - 1) :
                    uf.connect(gridId * 4 + 2, (i * n + j + 1) * 4 + 0)
        return uf.getSize()
```
# 10. Regular Expression Matching
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming, Backtracking*
* *Similar Questions:*
  * [Wildcard Matching](wildcard-matching.md)
## Problem:
Given an input string (s) and a pattern (p), implement regular expression matching with support for &#39.&#39 and &#39*&#39.
&#39.&#39 Matches any single character.
&#39*&#39 Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:
Input:
s = &quotaa&quot
p = &quota&quot
Output: false
Explanation: &quota&quot does not match the entire string &quotaa&quot.
Example 2:
Input:
s = &quotaa&quot
p = &quota*&quot
Output: true
Explanation: &#39*&#39 means zero or more of the preceding element, &#39a&#39. Therefore, by repeating &#39a&#39 once, it becomes &quotaa&quot.
Example 3:
Input:
s = &quotab&quot
p = &quot.*&quot
Output: true
Explanation: &quot.*&quot means &quotzero or more (*) of any character (.)&quot.
Example 4:
Input:
s = &quotaab&quot
p = &quotc*a*b&quot
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches &quotaab&quot.
Example 5:
Input:
s = &quotmississippi&quot
p = &quotmis*is*p*.&quot
Output: false
## Solutions:
```python
class Solution :
public:
    bool isMatch(string s, string p) :
        int m = s.length()
        int n = p.length()
        vector> dp(m + 1, vector(n + 1, false))
        dp[0][0] = true
        // when s is empty
        for (int j = 1 j <= n ++j) :
            char c = p[j-1]
            if (isalpha(c)) :
                dp[0][j] = false
             else if (c == '.'):
                dp[0][j] = false
             else :
                dp[0][j] = dp[0][j-2]
        // when p is empty
        for (int i = 1 i <= m ++i) :
            dp[i][0] = false
        for (int i = 1 i <= m ++i) :
            for (int j = 1 j <= n ++j) :
                if (p[j-1] == '*') :
                    if (s[i-1] == p[j-2] || p[j-2] == '.') :
                        dp[i][j] = dp[i-1][j] || dp[i][j-2]
                     else :
                        dp[i][j] = dp[i][j-2]
                    continue
                if (p[j-1] == '.' || s[i-1] == p[j-1]) :
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = false
        return dp[m][n]
```
# 506. Relative Ranks
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
## Solutions:
```python
class Solution :
public:
    vector findRelativeRanks(vector& nums) :
        vector> v
        for (int i = 0 i < nums.size() ++i) :
            v.push_back(:nums[i], i)
        string medals[3] = :
            "Gold Medal",
            "Silver Medal",
            "Bronze Medal"
        sort(v.begin(), v.end(), greater>())
        vector ret (v.size())
        for (int i = 0 i < min(3, (int)v.size()) ++i) :
            ret[v[i].second] = medals[i]
        for (int i = 3 i < v.size() ++i) :
            ret[v[i].second] = to_string(i+1)
        return ret
```
# 1217. Relative Sort Array
* *Difficulty: Easy*
* *Topics: Array, Sort*
* *Similar Questions:*
## Problem:
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don&#39t appear in arr2 should be placed at the end of arr1 in ascending order.
Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Constraints:
	arr1.length, arr2.length &lt= 1000
	0 &lt= arr1[i], arr2[i] &lt= 1000
	Each arr2[i] is distinct.
	Each arr2[i] is in arr1.
## Solutions:
```python
class Solution :
public:
    vector relativeSortArray(vector& arr1, vector& arr2) :
        unordered_map numToIndex
        for (int i = 0 i < arr2.size() ++i) :
            numToIndex[arr2[i]] = i
        auto comparator = [&numToIndex](const int& num1, const int& num2) :
            if (numToIndex.count(num1) > 0 && numToIndex.count(num2) > 0) :
                return numToIndex[num1] < numToIndex[num2]
            if (numToIndex.count(num1) == 0 && numToIndex.count(num2) == 0) :
                return num1 < num2
            return numToIndex.count(num1) > 0
        sort(arr1.begin(), arr1.end(), comparator)
        return arr1
```
# 1320. Remove All Adjacent Duplicates in String II
* *Difficulty: Medium*
* *Topics: Stack*
* *Similar Questions:*
  * [Remove All Adjacent Duplicates In String](remove-all-adjacent-duplicates-in-string.md)
## Problem:
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It is guaranteed that the answer is unique.
Example 1:
Input: s = &quotabcd&quot, k = 2
Output: &quotabcd&quot
Explanation: There&#39s nothing to delete.
Example 2:
Input: s = &quotdeeedbbcccbdaa&quot, k = 3
Output: &quotaa&quot
Explanation: 
First delete &quoteee&quot and &quotccc&quot, get &quotddbbbdaa&quot
Then delete &quotbbb&quot, get &quotdddaa&quot
Finally delete &quotddd&quot, get &quotaa&quot
Example 3:
Input: s = &quotpbbcggttciiippooaais&quot, k = 2
Output: &quotps&quot
Constraints:
	1 &lt= s.length &lt= 10^5
	2 &lt= k &lt= 10^4
	s only contains lower case English letters.
## Solutions:
```python
class Solution :
public:
    string removeDuplicates(string s, int k) :
        string ret
        stack count
        for (auto& c : s) :
            if (count.empty()) :
                ret.push_back(c)
                count.push(1)
                continue
            if (c == ret.back()) :
                ret.push_back(c)
                ++count.top()
                if (count.top() == k) :
                    for (int i = 0 i < k ++i) :
                        ret.pop_back()
                    count.pop()
             else :
                ret.push_back(c)
                count.push(1)
        return ret
```
# 1128. Remove All Adjacent Duplicates In String
* *Difficulty: Easy*
* *Topics: Stack*
* *Similar Questions:*
  * [Remove All Adjacent Duplicates in String II](remove-all-adjacent-duplicates-in-string-ii.md)
## Problem:
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
Example 1:
Input: &quotabbaca&quot
Output: &quotca&quot
Explanation: 
For example, in &quotabbaca&quot we could remove &quotbb&quot since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is &quotaaca&quot, of which only &quotaa&quot is possible, so the final string is &quotca&quot.
Note:
	1 &lt= S.length &lt= 20000
	S consists only of English lowercase letters.
## Solutions:
```python
class Solution :
public:
    string removeDuplicates(string S) :
        vector stack
        for (auto& c : S) :
            if (!stack.empty() && stack.back() == c) :
                stack.pop_back()
             else :
                stack.push_back(c)
        return :stack.begin(), stack.end()
```
# 722. Remove Comments
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
  * [Mini Parser](mini-parser.md)
  * [Ternary Expression Parser](ternary-expression-parser.md)
## Problem:
Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code.  This represents the result of splitting the original source code string by the newline character \n.
In C++, there are two types of comments, line comments, and block comments.
The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.
The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored.  (Here, occurrences happen in reading order: line by line from left to right.)  To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.
The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.
There will be no control characters, single quote, or double quote characters.  For example, source = "string s = "/* Not a comment. */"" will not be a test case.  (Also, nothing else such as defines or macros will interfere with the comments.)
It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.
Finally, implicit newline characters can be deleted by block comments.  Please see the examples below for details.
After removing the comments from the source code, return the source code in the same format.
Example 1:
Input: 
source = ["/*Test program */", "int main()", ": ", "  // variable declaration ", "int a, b, c", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c", ""]
The line by line code is visualized as below:
/*Test program */
int main()
: 
  // variable declaration 
int a, b, c
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c
Output: ["int main()",": ","  ","int a, b, c","a = b + c",""]
The line by line code is visualized as below:
int main()
: 
int a, b, c
a = b + c
Explanation: 
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
Example 2:
Input: 
source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
Note:
The length of source is in the range [1, 100].
The length of source[i] is in the range [0, 80].
Every open block comment is eventually closed.
There are no single-quote, double-quote, or control characters in the source code.
## Solutions:
```python
class Solution :
public:
    vector removeComments(vector& source) :
        queue buffer
        bool inContext = false
        vector ret
        for (auto& line : source) :
            auto processed = processLine(buffer, line, inContext)
            addLine(buffer, processed, ret)
        return ret
private:
    string processLine(queue& buffer, string& line, bool& inContext) :
        string ret
        for (int i = 0 i < line.length()) :
            if (line[i] != '/' && line[i] != '*') :
               if (!inContext) :
                   ret.push_back(line[i])
               ++i
               continue
            if (line[i] == '/') :
                if (!inContext) : // not in context
                    if (i + 1 < line.length() && line[i + 1] == '/') :
                        break
                    else if (i + 1 < line.length() && line[i + 1] == '*') :
                        inContext = true
                        i = i + 2
                    else :
                        ret.push_back('/')
                        ++i
                 else : // in context
                    ++i
             else :
                if (!inContext) :
                    ret.push_back('*')
                    ++i
                 else :
                    if (i + 1 < line.length() && line[i + 1] == '/') :
                        inContext = false
                        i = i + 2
                     else :
                        ++i
        if (!inContext && (!buffer.empty() || ret.length() != 0)) : // CAUTION! buffer.empty() should also be checked!
            ret.push_back('\n')
        return ret
    void addLine(queue& buffer, string& line, vector& ret) :
        for (auto c : line) :
            if (c != '\n') :
                buffer.push(c)
             else :
                string str
                while (!buffer.empty()) :
                    str.push_back(buffer.front()) buffer.pop()
                ret.push_back(str)
```
# 80. Remove Duplicates from Sorted Array II
* *Difficulty: Medium*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Remove Duplicates from Sorted Array](remove-duplicates-from-sorted-array.md)
## Problem:
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn&#39t matter what you leave beyond the returned length.
Example 2:
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
It doesn&#39t matter what values are set beyond the returned length.
Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums)
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0 i &lt len i++) :
    print(nums[i])
## Solutions:
```python
class Solution :
public:
    int removeDuplicates(vector& nums) :
        int cur = 0
        for (int i = 0 i < nums.size() ++i) :
            if (i + 2 < nums.size() && nums[i] == nums[i+1] && nums[i] == nums[i+2]) : // it is wrong to look backwards because they maybe modified.
                continue
            nums[cur++] = nums[i]
        return cur
```
# 26. Remove Duplicates from Sorted Array
* *Difficulty: Easy*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Remove Element](remove-element.md)
  * [Remove Duplicates from Sorted Array II](remove-duplicates-from-sorted-array-ii.md)
## Problem:
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn&#39t matter what you leave beyond the returned length.
Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn&#39t matter what values are set beyond the returned length.
Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums)
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0 i &lt len i++) :
    print(nums[i])
## Solutions:
```python
class Solution :
public:
    int removeDuplicates(vector& nums) :
        int len = 0
        for (int i = 0 i < nums.size() ++i) :
            if (i > 0 && nums[i] == nums[i-1]) continue
            nums[len++] = nums[i]
        return len
```
# 82. Remove Duplicates from Sorted List II
* *Difficulty: Medium*
* *Topics: Linked List*
* *Similar Questions:*
  * [Remove Duplicates from Sorted List](remove-duplicates-from-sorted-list.md)
## Problem:
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Example 1:
Input: 1-&gt2-&gt3-&gt3-&gt4-&gt4-&gt5
Output: 1-&gt2-&gt5
Example 2:
Input: 1-&gt1-&gt1-&gt2-&gt3
Output: 2-&gt3
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* deleteDuplicates(ListNode* head) :
        ListNode* dummyHead = new ListNode(0)
        ListNode* tail = dummyHead
        ListNode* cur = head
        while (cur) :
            if (cur->next && cur->val == cur->next->val) :
                int val = cur->val
                cur = cur->next->next
                while (cur && cur->val == val) :
                    cur = cur->next
             else :
                tail->next = cur
                tail = cur
                cur = cur->next
        tail->next = NULL
        return dummyHead->next
```
# 83. Remove Duplicates from Sorted List
* *Difficulty: Easy*
* *Topics: Linked List*
* *Similar Questions:*
  * [Remove Duplicates from Sorted List II](remove-duplicates-from-sorted-list-ii.md)
## Problem:
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1-&gt1-&gt2
Output: 1-&gt2
Example 2:
Input: 1-&gt1-&gt2-&gt3-&gt3
Output: 1-&gt2-&gt3
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* deleteDuplicates(ListNode* head) :
        ListNode* cur = head
        while (cur && cur->next) :
            if (cur->val == cur->next->val) :
                cur->next = cur->next->next
             else :
                cur = cur->next
        return head
```
# 27. Remove Element
* *Difficulty: Easy*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Remove Duplicates from Sorted Array](remove-duplicates-from-sorted-array.md)
  * [Remove Linked List Elements](remove-linked-list-elements.md)
  * [Move Zeroes](move-zeroes.md)
## Problem:
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn&#39t matter what you leave beyond the new length.
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn&#39t matter what you leave beyond the returned length.
Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn&#39t matter what values are set beyond the returned length.
Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val)
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0 i &lt len i++) :
    print(nums[i])
## Solutions:
```python
class Solution :
public:
    int removeElement(vector& nums, int val) :
        int cur = 0
        for (int i = 0 i < nums.size() ++i) :
            if (nums[i] != val) :
                nums[cur++] = nums[i]
        return cur
```
# 402. Remove K Digits
* *Difficulty: Medium*
* *Topics: Stack, Greedy*
* *Similar Questions:*
  * [Create Maximum Number](create-maximum-number.md)
  * [Monotone Increasing Digits](monotone-increasing-digits.md)
## Problem:
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:
The length of num is less than 10002 and will be &ge k.
The given num does not contain any leading zero.
Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
## Solutions:
```python
class Solution :
public:
    string removeKdigits(string num, int k) :
        vector stk
        num.push_back('0' - 1)
        for (auto& c : num) :
            while (k > 0 && !stk.empty() && stk.back() > c) :
                stk.pop_back()
                --k
            stk.push_back(c)
        stk.pop_back()
        int start = 0
        for (start = 0 start < stk.size() && stk[start] == '0' ++start)  
        if (start == stk.size())    return "0"
        return string(stk.begin() + start, stk.end())        
```
# 203. Remove Linked List Elements
* *Difficulty: Easy*
* *Topics: Linked List*
* *Similar Questions:*
  * [Remove Element](remove-element.md)
  * [Delete Node in a Linked List](delete-node-in-a-linked-list.md)
## Problem:
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1-&gt2-&gt6-&gt3-&gt4-&gt5-&gt6, val = 6
Output: 1-&gt2-&gt3-&gt4-&gt5
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* removeElements(ListNode* head, int val) :
        ListNode* dummy = new ListNode(0)
        ListNode* tail = dummy
        ListNode* next = nullptr
        while (head) :
            next = head->next
            if (head->val != val) :
                tail->next = head
                tail = tail->next
                tail->next = nullptr
            head = next
        return dummy->next
```
# 19. Remove Nth Node From End of List
* *Difficulty: Medium*
* *Topics: Linked List, Two Pointers*
* *Similar Questions:*
## Problem:
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1-&gt2-&gt3-&gt4-&gt5, and n = 2.
After removing the second node from the end, the linked list becomes 1-&gt2-&gt3-&gt5.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) :
        ListNode* front = head
        for (int i = 0 i < n ++i) :
            if (front == NULL)  return NULL
            front = front->next
        if (front == NULL) :
            return head->next
        front = front->next
        ListNode* cur = head
        while (front != NULL) :
            front = front->next
            cur = cur->next
        cur->next = cur->next->next
        return head
```
# 1078. Remove Outermost Parentheses
* *Difficulty: Easy*
* *Topics: Stack*
* *Similar Questions:*
## Problem:
A valid parentheses string is either empty (&quot&quot), &quot(&quot + A + &quot)&quot, or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, &quot&quot, &quot()&quot, &quot(())()&quot, and &quot(()(()))&quot are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
Example 1:
Input: &quot(()())(())&quot
Output: &quot()()()&quot
Explanation: 
The input string is &quot(()())(())&quot, with primitive decomposition &quot(()())&quot + &quot(())&quot.
After removing outer parentheses of each part, this is &quot()()&quot + &quot()&quot = &quot()()()&quot.
Example 2:
Input: &quot(()())(())(()(()))&quot
Output: &quot()()()()(())&quot
Explanation: 
The input string is &quot(()())(())(()(()))&quot, with primitive decomposition &quot(()())&quot + &quot(())&quot + &quot(()(()))&quot.
After removing outer parentheses of each part, this is &quot()()&quot + &quot()&quot + &quot()(())&quot = &quot()()()()(())&quot.
Example 3:
Input: &quot()()&quot
Output: &quot&quot
Explanation: 
The input string is &quot()()&quot, with primitive decomposition &quot()&quot + &quot()&quot.
After removing outer parentheses of each part, this is &quot&quot + &quot&quot = &quot&quot.
Note:
	S.length &lt= 10000
	S[i] is &quot(&quot or &quot)&quot
	S is a valid parentheses string
## Solutions:
```python
class Solution :
public:
    string removeOuterParentheses(string S) :
        string ret
        int balance = 0
        int left = 0
        for (int i = 0 i < S.length() ++i) :
            balance += (S[i] == '(' ? 1 : -1)
            if (balance == 1 && S[i] == '(') :
                left = i
             else if (balance == 0 && S[i] == ')') :
                ret.append(S.substr(left + 1, i - left - 1))
        return ret
```
# 974. Reorder Data in Log Files
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
You have an array of logs.  Each log is a space delimited string of words.
For each log, the first word in each log is an alphanumeric identifier.  Then, either:
	Each word after the identifier will consist only of lowercase letters, or
	Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
Return the final order of the logs.
Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Constraints:
	0 &lt= logs.length &lt= 100
	3 &lt= logs[i].length &lt= 100
	logs[i] is guaranteed to have an identifier, and a word after the identifier.
## Solutions:
```python
class Solution :
public:
    vector reorderLogFiles(vector& logs) :
        auto comparator = [this](const string& log1, const string& log2) :
            int pos1 = 0
            int pos2 = 0
            if (isLetterLog(log1, pos1) && isLetterLog(log2, pos2)) :
                string logContent1 = log1.substr(pos1)
                string logContent2 = log2.substr(pos2)
                if (logContent1 != logContent2) :
                    return logContent1 < logContent2
                return log1.substr(0, pos1 - 1) < log2.substr(0, pos2 - 1)
             else if (isLetterLog(log1, pos1) && !isLetterLog(log2, pos2)) :
                return true
             else if (!isLetterLog(log1, pos1) && isLetterLog(log2, pos2)) :
                return false
             else :
                return false
        stable_sort(logs.begin(), logs.end(), comparator)
        return logs
private:
    bool isLetterLog(const string& log, int& pos) :
        pos = 0
        while (log[pos] != ' ') ++pos
        ++pos // eat empty space
        return !isdigit(log[pos])
```
# 778. Reorganize String
* *Difficulty: Medium*
* *Topics: String, Heap, Greedy, Sort*
* *Similar Questions:*
  * [Rearrange String k Distance Apart](rearrange-string-k-distance-apart.md)
  * [Task Scheduler](task-scheduler.md)
## Problem:
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.
Example 1:
Input: S = &quotaab&quot
Output: &quotaba&quot
Example 2:
Input: S = &quotaaab&quot
Output: &quot&quot
Note:
	S will consist of lowercase letters and have length in range [1, 500].
## Solutions:
```python
class Solution :
public:
    string reorganizeString(string S) :
        return rearrangeString(S, 2)
private:
    string rearrangeString(string s, int k) :
        if (k <= 0) return s // This special case if important
        if (s.length() == 0)    return s
        int len = s.length()
        unordered_map charCount
        for (auto c : s) :
            ++charCount[c]
        vector chars
        for (auto& entry : charCount) :
            chars.push_back(entry.first)
        sort(chars.begin(), chars.end(), [charCount](char c1, char c2) :
           return charCount.at(c1) > charCount.at(c2) 
        )
        int maxVal = charCount[chars[0]]
        int maxCount = 0
        for (int i = 0 i < chars.size() && charCount[chars[i]] == maxVal ++i) ++maxCount
        if (len < (k * (maxVal - 1) + maxCount)) return ""
        vector matrix(maxVal - 1)
        int pos = 0
        for (int i = maxCount i < chars.size() ++i) :
            for (int j = 0 j < charCount[chars[i]] ++j) :
                matrix[pos%(maxVal - 1)].push_back(chars[i])
                ++pos
        string ret
        string maxStr
        for (int i = 0 i < maxCount ++i) :
            maxStr.push_back(chars[i])
        for (int i = 0 i < maxVal - 1 ++i) :
            ret.append(maxStr)
            ret.append(matrix[i])
        ret.append(maxStr)
        return ret
```
# 187. Repeated DNA Sequences
* *Difficulty: Medium*
* *Topics: Hash Table, Bit Manipulation*
* *Similar Questions:*
## Problem:
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: &quotACGAATTCCG&quot. When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
Example:
Input: s = &quotAAAAACCCCCAAAAACCCCCCAAAAAGGGTTT&quot
Output: [&quotAAAAACCCCC&quot, &quotCCCCCAAAAA&quot]
## Solutions:
```python
class Solution :
public:
    vector findRepeatedDnaSequences(string s) :
        if (s.length() < 10)    return :
        int code = 0
        for (int i = 0 i < 9 ++i) :
            updateCode(code, s[i])
        unordered_map merCount
        vector ret
        for (int i = 9 i < s.length() ++i) :
            updateCode(code, s[i])
            if (++merCount[code] == 2) :
                ret.push_back(s.substr(i - 9, 10))
        return ret
    void updateCode(int& code, char c) :
        const int mask = 0xFFFFF
        code = ((code << 2) & mask)
        switch(c) :
            case 'A':
                // no-op
                break
            case 'C':
                code = code | 0x1
                break
            case 'G':
                code = code | 0x2
                break
            case 'T':
                code = code | 0x3
                break
            default:
                throw "Illegal input"
```
# 459. Repeated Substring Pattern
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Implement strStr()](implement-strstr.md)
  * [Repeated String Match](repeated-string-match.md)
## Problem:
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: &quotabab&quot
Output: True
Explanation: It&#39s the substring &quotab&quot twice.
Example 2:
Input: &quotaba&quot
Output: False
Example 3:
Input: &quotabcabcabcabc&quot
Output: True
Explanation: It&#39s the substring &quotabc&quot four times. (And the substring &quotabcabc&quot twice.)
## Solutions:
```python
class Solution :
public:
    bool repeatedSubstringPattern(string s) :
        int len = s.length()
        for (int i = 2 i <= len ++i) :
            if (len % i == 0 && isPrime(i)) :
                int patternLen = len / i
                int j = 0
                for (j = 0 j < patternLen ++j) :
                    int k = 1
                    for (k = 1 k < i ++k) :
                        if (s[k * patternLen + j] != s[j]) break
                    if (k != i) break
                if (j == patternLen)    return true
        return false
private:
    bool isPrime(int num) :
        for (int i = 2 i <= sqrt(num) ++i) :
            if (num % i == 0)   return false
        return true
```
# 566. Reshape the Matrix
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
 The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix Otherwise, output the original matrix.
Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
## Solutions:
```python
class Solution :
public:
    vector> matrixReshape(vector>& nums, int r, int c) :
        int m = nums.size()
        if (m == 0) return :
        int n = nums[0].size()
        if (n == 0) return :
        if (m * n != r * c) return nums
        vector> matrix (r, vector(c, 0))
        for (int i = 0 i < m ++i) :
            for (int j = 0 j< n ++j) :
                int index = i * n + j
                int row = index / c
                int col = index % c
                matrix[row][col] = nums[i][j]
        return matrix
```
# 93. Restore IP Addresses
* *Difficulty: Medium*
* *Topics: String, Backtracking*
* *Similar Questions:*
  * [IP to CIDR](ip-to-cidr.md)
## Problem:
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
Example:
Input: &quot25525511135&quot
Output: [&quot255.255.11.135&quot, &quot255.255.111.35&quot]
## Solutions:
```python
class Solution :
public:
    vector restoreIpAddresses(string s) :
        vector path
        vector ret
        helper(s, 0, path, ret)
        return ret
private:
    void helper(const string& s, int pos, vector& path, vector& ret) :
        // for (auto str : path) :
        //     cout << str << " "
        // 
        // cout << "end" << endl
        // base case
        if (path.size() > 4)    return
        if (pos == s.length()) :
            if (path.size() != 4)   return
            ret.push_back(prettyPrint(path))
            //return
        for (int len = 1 len <= 3 && pos + len <= s.length() ++len) :
            if (len != 1 && s[pos] == '0')  return
            int num = 0
            for (int j = 0 j < len ++j) :
                num = 10 * num + (s[pos + j] - '0')
            //cout << num << endl
            if (num > 255)  return
            path.push_back(s.substr(pos, len))
            helper(s, pos + len, path, ret)
            path.pop_back()
    string prettyPrint(vector& path) :
        string ret
        for (auto& seg : path) :
            ret.append(seg)
            ret.push_back('.')
        ret.pop_back()
        return ret
```
# 190. Reverse Bits
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Reverse Integer](reverse-integer.md)
  * [Number of 1 Bits](number-of-1-bits.md)
## Problem:
Reverse bits of a given 32 bits unsigned integer.
Example 1:
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.
Note:
	Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
	In Java, the compiler represents the signed integers using 2&#39s complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
Follow up:
If this function is called many times, how would you optimize it?
## Solutions:
```python
class Solution :
public:
    uint32_t reverseBits(uint32_t n) :
        uint32_t result = 0
        const uint32_t product = 1 << 31 
        while (n) :
            int bitVal = n & (-n)
            result += product/bitVal
            n -= bitVal
        return result
```
# 7. Reverse Integer
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [String to Integer (atoi)](string-to-integer-atoi.md)
  * [Reverse Bits](reverse-bits.md)
## Problem:
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321
Example 2:
Input: -123
Output: -321
Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus231,  231 &minus 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
## Solutions:
```python
class Solution :
public:
    int reverse(int x) :
        bool sign = (x >= 0)
        if (x == INT_MIN)   return 0
        x = abs(x) // it is wrong if x is INT_MIN because of overflow.
        int ret = 0
        while (x > 0) :
            int digit = x%10
            x /= 10
            if (ret > INT_MAX/10 || (ret == INT_MAX/10 && (sign ? digit > INT_MAX%10 : digit > INT_MAX%10 + 1)))    return 0 // the priority of conditional operator is low && abs(INT_MIN) is forbidon!!!
            ret = ret * 10 + digit
        return sign ? ret : -ret
```
### More concise solution
From [https://zxi.mytechroad.com/blog/simulation/leetcode-7-reverse-integer/](Huahua)
It is not necessary to distinguish whether `x` is negative or not. 
The rule to determine the sign of modulus is explained at one [https://stackoverflow.com/questions/7594508/modulo-operator-with-negative-values](article from StackOverFlow).  
Simple examples are shown below. 
(-7/3) => -2
-2 * 3 => -6
so a%b => -1
(7/-3) => -2
-2 * -3 => 6
so a%b => 1
```python
// Author: Huahua
class Solution :
public:
  int reverse(int x) :
    int ans = 0
    while (x != 0) :
      int r = x % 10
      if (ans > INT_MAX / 10 || ans < INT_MIN / 10) return 0
      ans = ans * 10 + r
      x /= 10
    return ans
```
# 92. Reverse Linked List II
* *Difficulty: Medium*
* *Topics: Linked List*
* *Similar Questions:*
  * [Reverse Linked List](reverse-linked-list.md)
## Problem:
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 &le m &le n &le length of list.
Example:
Input: 1-&gt2-&gt3-&gt4-&gt5-&gtNULL, m = 2, n = 4
Output: 1-&gt4-&gt3-&gt2-&gt5-&gtNULL
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) :
        if (head == nullptr)    return nullptr
        ListNode* dummy = new ListNode(0)
        dummy->next = head
        ListNode* cur = dummy
        int index = 0
        while (cur && index < m - 1) :
            cur = cur->next
            ++index
        ListNode* tail = cur
        cur = cur->next
        ListNode* reverseLast = cur
        tail->next = nullptr
        for (int i = 0 i < n - m + 1 ++i) :
            ListNode* next = cur->next
            cur->next = tail->next
            tail->next = cur
            cur = next
        reverseLast->next = cur
        return dummy->next
```
# 206. Reverse Linked List
* *Difficulty: Easy*
* *Topics: Linked List*
* *Similar Questions:*
  * [Reverse Linked List II](reverse-linked-list-ii.md)
  * [Binary Tree Upside Down](binary-tree-upside-down.md)
  * [Palindrome Linked List](palindrome-linked-list.md)
## Problem:
Reverse a singly linked list.
Example:
Input: 1-&gt2-&gt3-&gt4-&gt5-&gtNULL
Output: 5-&gt4-&gt3-&gt2-&gt1-&gtNULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* reverseList(ListNode* head) :
        if (head == NULL || head->next == NULL) return head
        ListNode* reverseSubList = reverseList(head->next)
        head->next->next = head
        head->next = NULL
        return reverseSubList
```
# 25. Reverse Nodes in k-Group
* *Difficulty: Hard*
* *Topics: Linked List*
* *Similar Questions:*
  * [Swap Nodes in Pairs](swap-nodes-in-pairs.md)
## Problem:
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
Example:
Given this linked list: 1-&gt2-&gt3-&gt4-&gt5
For k = 2, you should return: 2-&gt1-&gt4-&gt3-&gt5
For k = 3, you should return: 3-&gt2-&gt1-&gt4-&gt5
Note:
	Only constant extra memory is allowed.
	You may not alter the values in the list&#39s nodes, only nodes itself may be changed.
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* reverseKGroup(ListNode* head, int k) :
        ListNode* dummyHead = new ListNode(0)
        ListNode* tail = dummyHead
        ListNode* left = head
        int count = 0
        while (head) :
            ++count
            ListNode* nextNode = head->next
            if (k == count) :
                tail->next = reverse(left, k)
                tail = left
                left = nextNode
                count = 0
            head = nextNode
        tail->next = left
        return dummyHead->next
    ListNode* reverse(ListNode* head, int k) :
        ListNode* dummyHead = new ListNode(0)
        while (k-- > 0) :
            ListNode* nextNode = head->next
            head->next = dummyHead->next
            dummyHead->next = head
            head = nextNode
        return dummyHead->next
```
# 541. Reverse String II
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Reverse String](reverse-string.md)
  * [Reverse Words in a String III](reverse-words-in-a-string-iii.md)
## Problem:
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions: 
 The string consists of lower English letters only.
 Length of the given string and k will in the range [1, 10000]
## Solutions:
```python
class Solution :
public:
    string reverseStr(string s, int k) :
        int pos = 0
        while (pos < s.length()) :
            int left = pos
            int right = min(pos + k - 1, (int) s.length() - 1)
            while (left < right) :
                swap(s[left], s[right])
                ++left
                --right
            pos += 2 * k
        return s
```
# 344. Reverse String
* *Difficulty: Easy*
* *Topics: Two Pointers, String*
* *Similar Questions:*
  * [Reverse Vowels of a String](reverse-vowels-of-a-string.md)
  * [Reverse String II](reverse-string-ii.md)
## Problem:
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
Example 1:
Input: [&quoth&quot,&quote&quot,&quotl&quot,&quotl&quot,&quoto&quot]
Output: [&quoto&quot,&quotl&quot,&quotl&quot,&quote&quot,&quoth&quot]
Example 2:
Input: [&quotH&quot,&quota&quot,&quotn&quot,&quotn&quot,&quota&quot,&quoth&quot]
Output: [&quoth&quot,&quota&quot,&quotn&quot,&quotn&quot,&quota&quot,&quotH&quot]
## Solutions:
```python
class Solution :
public:
    void reverseString(vector& s) :
        int left = 0 
        int right = s.size() - 1
        while (left < right) :
            swap(s[left], s[right])
            ++left
            --right
```
# 1298. Reverse Substrings Between Each Pair of Parentheses
* *Difficulty: Medium*
* *Topics: Stack*
* *Similar Questions:*
## Problem:
Given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any bracket.
Example 1:
Input: s = &quot(abcd)&quot
Output: &quotdcba&quot
Example 2:
Input: s = &quot(u(love)i)&quot
Output: &quotiloveu&quot
Example 3:
Input: s = &quot(ed(et(oc))el)&quot
Output: &quotleetcode&quot
Example 4:
Input: s = &quota(bcdefghijkl(mno)p)q&quot
Output: &quotapmnolkjihgfedcbq&quot
Constraints:
	0 &lt= s.length &lt= 2000
	s only contains lower case English characters and parentheses.
	It&#39s guaranteed that all parentheses are balanced.
## Solutions:
```python
class Solution :
public:
    string reverseParentheses(string s) :
        int pos = 0
        return helper(s, pos)
private:
    string helper(const string& s, int& pos) :
        string ret
        while (pos < s.length()) :
            if (s[pos] == '(') :
                string inner = helper(s, ++pos)
                reverse(inner.begin(), inner.end())
                ret.append(inner)
             else if (s[pos] == ')') :
                ++pos
                return ret
             else :
                ret.push_back(s[pos++])
        return ret
```
# 345. Reverse Vowels of a String
* *Difficulty: Easy*
* *Topics: Two Pointers, String*
* *Similar Questions:*
  * [Reverse String](reverse-string.md)
  * [Remove Vowels from a String](remove-vowels-from-a-string.md)
## Problem:
Write a function that takes a string as input and reverse only the vowels of a string.
Example 1:
Input: &quothello&quot
Output: &quotholle&quot
Example 2:
Input: &quotleetcode&quot
Output: &quotleotcede&quot
Note:
The vowels does not include the letter &quoty&quot.
## Solutions:
```python
class Solution :
public:
    string reverseVowels(string s) :
        unordered_set vowels = :'a','e','i','o','u','A','E','I','O','U'
        int left = 0
        int right = s.length() - 1
        while (left < right) :
            while (left < right && vowels.count(s[left]) == 0)  ++left
            while (left < right && vowels.count(s[right]) == 0) --right
            swap(s[left], s[right])
            ++left
            --right
        return s
```
# 186. Reverse Words in a String II
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
  * [Reverse Words in a String](reverse-words-in-a-string.md)
  * [Rotate Array](rotate-array.md)
## Problem:
Given an input string , reverse the string word by word. 
Example:
Input:  [&quott&quot,&quoth&quot,&quote&quot,&quot &quot,&quots&quot,&quotk&quot,&quoty&quot,&quot &quot,&quoti&quot,&quots&quot,&quot &quot,&quotb&quot,&quotl&quot,&quotu&quot,&quote&quot]
Output: [&quotb&quot,&quotl&quot,&quotu&quot,&quote&quot,&quot &quot,&quoti&quot,&quots&quot,&quot &quot,&quots&quot,&quotk&quot,&quoty&quot,&quot &quot,&quott&quot,&quoth&quot,&quote&quot]
Note: 
	A word is defined as a sequence of non-space characters.
	The input string does not contain leading or trailing spaces.
	The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
## Solutions:
```python
class Solution :
public:
    void reverseWords(vector& s) :
        int start = 0
        int end = 0
        while (start < s.size()) :
            end = start + 1
            while (end < s.size() && s[end] != ' ') ++end
            reverse(s, start, end - 1)
            start = end + 1
        reverse(s, 0, s.size() - 1)
    void reverse(vector& s, int start, int end) :
        while (start < end) :
            swap(s[start], s[end])
            ++start
            --end
```
# 557. Reverse Words in a String III
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Reverse String II](reverse-string-ii.md)
## Problem:
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note:
In the string, each word is separated by single space and there will not be any extra space in the string.
## Solutions:
```python
class Solution :
public:
    string reverseWords(string s) :
        int pos = 0
        while (pos < s.length()) :
            int left = pos
            int right = left
            while (right < s.length() && s[right] != ' ') ++right
            pos = right + 1
            right = right - 1
            while (left < right) :
                swap(s[left], s[right])
                ++left
                --right
        return s
```
# 151. Reverse Words in a String
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
  * [Reverse Words in a String II](reverse-words-in-a-string-ii.md)
## Problem:
Given an input string, reverse the string word by word.
Example 1:
Input: &quotthe sky is blue&quot
Output: &quotblue is sky the&quot
Example 2:
Input: &quot  hello world!  &quot
Output: &quotworld! hello&quot
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:
Input: &quota good   example&quot
Output: &quotexample good a&quot
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Note:
	A word is defined as a sequence of non-space characters.
	Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
	You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up:
For C programmers, try to solve it in-place in O(1) extra space.
## Solutions:
```python
class Solution :
public:
    string reverseWords(string s) :
        string ret
        stringstream ss(s)
        string word
        if (ss >> word) :
            ret.append(word)
        while (ss >> word) :
            ret.push_back(' ')
            ret.append(word)
        if (ret.length() == 0)  return ret
        // left and right are both facing right
        int left = 0
        int right = 0
        while (right < ret.length()) :
            while (right + 1 < ret.length() && ret[right+1] != ' ') ++right
            stringSwap(ret, left, right)
            right = right + 2
            left = right
        stringSwap(ret, 0, ret.length() - 1)
        return ret
    void stringSwap(string& s, int left, int right) :
        while (left < right) :
            swap(s[left], s[right])
            ++left
            --right
```
# 657. Robot Return to Origin
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Friend Circles](friend-circles.md)
## Problem:
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
Note: The way that the robot is &quotfacing&quot is irrelevant. &quotR&quot will always make the robot move to the right once, &quotL&quot will always make it move left, etc. Also, assume that the magnitude of the robot&#39s movement is the same for each move.
Example 1:
Input: &quotUD&quot
Output: true 
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
Example 2:
Input: &quotLL&quot
Output: false
Explanation: The robot moves left twice. It ends up two &quotmoves&quot to the left of the origin. We return false because it is not at the origin at the end of its moves.
## Solutions:
```python
class Solution :
public:
    bool judgeCircle(string moves) :
        int x = 0, y = 0
        for (auto& c : moves) :
            switch(c) :
                case 'U': y -= 1 break
                case 'D': y += 1 break
                case 'L': x -= 1 break
                case 'R': x += 1 break
        return x == 0 && y == 0
```
# 13. Roman to Integer
* *Difficulty: Easy*
* *Topics: Math, String*
* *Similar Questions:*
  * [Integer to Roman](integer-to-roman.md)
## Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one&#39s added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
	I can be placed before V (5) and X (10) to make 4 and 9. 
	X can be placed before L (50) and C (100) to make 40 and 90. 
	C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
Example 1:
Input: &quotIII&quot
Output: 3
Example 2:
Input: &quotIV&quot
Output: 4
Example 3:
Input: &quotIX&quot
Output: 9
Example 4:
Input: &quotLVIII&quot
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:
Input: &quotMCMXCIV&quot
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
## Solutions:
```python
class Solution :
public:
    int romanToInt(string s) :
        unordered_map romanVal ::'I', 1, :'V', 5, :'X', 10, :'L', 50, :'C', 100, :'D', 500, :'M', 1000
        int last = 0
        int ret = 0
        for (int i = s.length() - 1 i >= 0 --i) :
            int val = romanVal[s[i]]
            if (val >= last) :
                ret += val
             else :
                ret -= val
            last = val
        return ret
```
# 189. Rotate Array
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Rotate List](rotate-list.md)
  * [Reverse Words in a String II](reverse-words-in-a-string-ii.md)
## Problem:
Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:
	Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
	Could you do it in-place with O(1) extra space?
## Solutions:
```python
class Solution :
public:
    void rotate(vector& nums, int k) :
        k = k % nums.size()
        swap(nums, nums.size() - k, nums.size() -1)
        swap(nums, 0, nums.size() - k - 1)
        swap(nums, 0, nums.size() - 1) // it is nums.size() -1
        return
    void swap(vector& nums, int left, int right) :
        while (left < right) :
            int temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left++
            right--
```
# 396. Rotate Function
* *Difficulty: Medium*
* *Topics: Math*
* *Similar Questions:*
## Problem:
Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
Calculate the maximum value of F(0), F(1), ..., F(n-1). 
Note:
n is guaranteed to be less than 105.
Example:
A = [4, 3, 2, 6]
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
## Solutions:
```python
class Solution :
public:
    int maxRotateFunction(vector& A) :
        long sum = 0
        long fun = 0
        for (int i = 0 i < A.size() ++i) :
            sum += A[i]
            fun += i * A[i]
        long ret = fun
        for (int i = A.size() - 1 i > 0 --i) :
            int newFun = fun - A[i] * (A.size() - 1) + (sum - A[i])
            fun = newFun
            ret = max(ret, fun)
        return ret
```
# 48. Rotate Image
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
## Problem:
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
## Solutions:
```python
class Solution :
public:
    void rotate(vector>& matrix) :
        int n = matrix.size()
        for (int i = 0 i < n/2 ++i) :
            for (int j = i j < n - i - 1 ++j) :
                kickOff(matrix, n, i, j)
    void kickOff(vector>& matrix, int n, int row, int col) :
        int coord[4][2] = ::row, col, :col, n - 1 - row, :n - 1 - row, n - 1 - col, :n - 1 - col,row
        int start = 0
        for (int i = 0 i < 5 ++i) :
            swap(start, matrix[coord[i%4][0]][coord[i%4][1]])
```
# 61. Rotate List
* *Difficulty: Medium*
* *Topics: Linked List, Two Pointers*
* *Similar Questions:*
  * [Rotate Array](rotate-array.md)
  * [Split Linked List in Parts](split-linked-list-in-parts.md)
## Problem:
Given a linked list, rotate the list to the right by k places, where k is non-negative.
Example 1:
Input: 1-&gt2-&gt3-&gt4-&gt5-&gtNULL, k = 2
Output: 4-&gt5-&gt1-&gt2-&gt3-&gtNULL
Explanation:
rotate 1 steps to the right: 5-&gt1-&gt2-&gt3-&gt4-&gtNULL
rotate 2 steps to the right: 4-&gt5-&gt1-&gt2-&gt3-&gtNULL
Example 2:
Input: 0-&gt1-&gt2-&gtNULL, k = 4
Output: 2-&gt0-&gt1-&gtNULL
Explanation:
rotate 1 steps to the right: 2-&gt0-&gt1-&gtNULL
rotate 2 steps to the right: 1-&gt2-&gt0-&gtNULL
rotate 3 steps to the right: 0-&gt1-&gt2-&gtNULL
rotate 4 steps to the right: 2-&gt0-&gt1-&gtNULL
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* rotateRight(ListNode* head, int k) :
        if (head == NULL)   return NULL
        int count = 1
        ListNode* cur = head
        while (cur->next) :
            ++count
            cur = cur->next
        cur->next = head
        k = k % count
        cur = head
        for (int i = 0 i < (count - k - 1) ++i) :
            cur = cur->next
        ListNode* ret = cur->next
        cur->next = NULL
        return ret
```
# 100. Same Tree
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
## Problem:
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Example 1:
Input:     1         1
          / \       / \
         2   3     2   3
        [1,2,3],   [1,2,3]
Output: true
Example 2:
Input:     1         1
          /           \
         2             2
        [1,2],     [1,null,2]
Output: false
Example 3:
Input:     1         1
          / \       / \
         2   1     1   2
        [1,2,1],   [1,1,2]
Output: false
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isSameTree(TreeNode* p, TreeNode* q) :
        if (p == nullptr && q == nullptr)   return true
        if (p == nullptr || q == nullptr)   return false
        if (p->val != q->val)   return false
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right)
```
# 87. Scramble String
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = &quotgreat&quot:
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node &quotgr&quot and swap its two children, it produces a scrambled string &quotrgeat&quot.
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that &quotrgeat&quot is a scrambled string of &quotgreat&quot.
Similarly, if we continue to swap the children of nodes &quoteat&quot and &quotat&quot, it produces a scrambled string &quotrgtae&quot.
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that &quotrgtae&quot is a scrambled string of &quotgreat&quot.
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
Example 1:
Input: s1 = &quotgreat&quot, s2 = &quotrgeat&quot
Output: true
Example 2:
Input: s1 = &quotabcde&quot, s2 = &quotcaebd&quot
Output: false
## Solutions:
```python
class Solution :
public:
    bool isScramble(string s1, string s2) :
        int len1 = s1.length()
        int len2 = s2.length()
        map, bool> cache
        return helper(s1, s2, 0, 0, len1, cache)
    bool helper(string s1, string s2, int idx1, int idx2, int len, map, bool>& cache) :
        if (cache.find(:idx1, idx2, len) != cache.end()) :
            return cache[:idx1, idx2, len]
        bool ret = false
        if (stringEqual(s1, s2, idx1, idx2, len)) :
            cache[:idx1, idx2, len] = true
            return true
        for (int part1 = 1 part1 <= len - 1 ++part1) :
            if (helper(s1, s2, idx1, idx2, part1, cache) && helper(s1, s2, idx1 + part1, idx2 + part1, len - part1, cache)) :
                cache[:idx1, idx2, len] = true
                return true
            if (helper(s1, s2, idx1, idx2 + len - part1, part1, cache) && helper(s1, s2, idx1 + part1, idx2, len - part1, cache)) :
                cache[:idx1, idx2, len] = true
                return true
        cache[:idx1, idx2, len] = false
        return false
    bool stringEqual(string s1, string s2, int idx1, int idx2, int len) :
        if (idx1 + len > s1.length())   return false
        if (idx2 + len > s2.length())   return false
        for (int i = 0 i < len ++i) :
            if (s1[i + idx1] != s2[i + idx2]) return false
        return true
```
# 240. Search a 2D Matrix II
* *Difficulty: Medium*
* *Topics: Binary Search, Divide and Conquer*
* *Similar Questions:*
  * [Search a 2D Matrix](search-a-2d-matrix.md)
## Problem:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
	Integers in each row are sorted in ascending from left to right.
	Integers in each column are sorted in ascending from top to bottom.
Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
## Solutions:
```python
class Solution :
public:
    bool searchMatrix(vector>& matrix, int target) :
        int m = matrix.size()
        if (m == 0) return false
        int n = matrix[0].size()
        if (n == 0) return false
        int i = m - 1
        int j = 0
        while (i >= 0 && j < n) :
            if (matrix[i][j] == target) return true
            else if (matrix[i][j] < target) :
                ++j
             else :
                --i
        return false
```
# 74. Search a 2D Matrix
* *Difficulty: Medium*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [Search a 2D Matrix II](search-a-2d-matrix-ii.md)
## Problem:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
	Integers in each row are sorted from left to right.
	The first integer of each row is greater than the last integer of the previous row.
Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
## Solutions:
```python
class Solution :
public:
    bool searchMatrix(vector>& matrix, int target) :
        int m = matrix.size()
        if (m == 0) return false
        int n = matrix[0].size()
        if (n == 0) return false
        int left = 0
        int right = m * n - 1
        while (left <= right) :
            int mid = left + (right - left) / 2
            auto coord = arrayToMatrix(m, n, mid)
            int row = coord.first
            int col = coord.second
            if (matrix[row][col] == target) return true
            if (matrix[row][col] > target) :
                right = mid - 1
             else :
                left = mid + 1
        return false
    inline pair arrayToMatrix(int m, int n, int index) :
        return :index/n, index%n
```
# 783. Search in a Binary Search Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Closest Binary Search Tree Value](closest-binary-search-tree-value.md)
  * [Insert into a Binary Search Tree](insert-into-a-binary-search-tree.md)
## Problem:
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node&#39s value equals the given value. Return the subtree rooted with that node. If such node doesn&#39t exist, you should return NULL.
For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to search: 2
You should return this subtree:
      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.
Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* searchBST(TreeNode* root, int val) :
        if (root == nullptr)    return nullptr
        if (root->val == val)   return root
        if (root->val > val)    return searchBST(root->left, val)
        return searchBST(root->right, val)
```
# 81. Search in Rotated Sorted Array II
* *Difficulty: Medium*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [Search in Rotated Sorted Array](search-in-rotated-sorted-array.md)
## Problem:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:
	This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
	Would this affect the run-time complexity? How and why?
## Solutions:
```python
class Solution :
public:
    bool search(vector& nums, int target) :
        return helper(nums, 0, nums.size() - 1, target)
    bool helper(vector& nums, int left, int right, int target) :
        if (left > right)   return false
        if (left == right)  return nums[left] == target
        int mid = left + (right - left)/2
        if (nums[left] == nums[right] && nums[left] == nums[mid]) :
            return helper(nums, left, mid, target) || helper(nums, mid + 1, right, target)
         else :
            if (nums[left] < nums[right]) :
                return target <= nums[mid] ? helper(nums, left, mid, target) : helper(nums, mid + 1, right, target)
             else :
                if (nums[mid] >= nums[left]) :
                    if (target  nums[mid])  return helper(nums, mid + 1, right, target) 
                    else return helper(nums, left, mid, target)
                 else :
                    if (target > nums[mid] && target <= nums[right]) return helper(nums, mid + 1, right, target)
                    else return helper(nums, left, mid, target)
```
# 33. Search in Rotated Sorted Array
* *Difficulty: Medium*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [Search in Rotated Sorted Array II](search-in-rotated-sorted-array-ii.md)
  * [Find Minimum in Rotated Sorted Array](find-minimum-in-rotated-sorted-array.md)
## Problem:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm&#39s runtime complexity must be in the order of O(log n).
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
## Solutions:
```python
class Solution :
public:
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    int search(vector &A, int target) :
        // write your code here
        if (A.size() == 0)  return -1
        int left = 0
        int right = A.size() - 1
        while (left + 1 < right) :
            int mid = left + ((right - left) >> 1)
            if (A[mid] == target)  return mid
            if (A[left] < A[right]) :
                if (A[mid] < target) :
                    left = mid
                 else :
                    right = mid
             else :
                if (A[mid] > A[left]) :
                    if (A[mid] > target && A[left] <= target) :
                        right = mid
                     else :
                        left = mid
                 else :
                    if (A[mid] = target) :
                        left = mid
                     else :
                        right = mid
        if (A[left] == target)  return left
        if (A[right] == target) return right
        return -1
```
# 35. Search Insert Position
* *Difficulty: Easy*
* *Topics: Array, Binary Search*
* *Similar Questions:*
  * [First Bad Version](first-bad-version.md)
## Problem:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2
Example 2:
Input: [1,3,5,6], 2
Output: 1
Example 3:
Input: [1,3,5,6], 7
Output: 4
Example 4:
Input: [1,3,5,6], 0
Output: 0
## Solutions:
```python
class Solution :
public:
    int searchInsert(vector& nums, int target) :
        int left = 0
        int right = nums.size() - 1
        while (left < right) :
            int mid = left + (right - left)/2
            if (nums[mid] >= target) :
                right = mid
             else :
                left = mid + 1
        return nums[left] >= target ? left : left + 1
```
# 176. Second Highest Salary
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Write a SQL query to get the second highest salary from the Employee table.
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
## Solutions:
```python
# Write your MySQL query statement below
SELECT
    (SELECT DISTINCT Salary 
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary  
```
# 728. Self Dividing Numbers
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Perfect Number](perfect-number.md)
## Problem:
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:
The boundaries of each input argument are 1 .
## Solutions:
```python
class Solution :
public:
    vector selfDividingNumbers(int left, int right) :
        vector ret
        for (int i = left i <= right ++i) :
            if (isSelfDivided(i)) :
                ret.push_back(i)
        return ret
private:
    bool isSelfDivided(int num) :
        int clone = num
        while (clone > 0) :
            int digit = clone % 10
            if (digit == 0) return false
            clone /= 10
            if (num % digit != 0)   return false
        return true
```
# 734. Sentence Similarity
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Friend Circles](friend-circles.md)
  * [Accounts Merge](accounts-merge.md)
  * [Sentence Similarity II](sentence-similarity-ii.md)
## Problem:
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
For example, &quotgreat acting skills&quot and &quotfine drama talent&quot are similar, if the similar word pairs are pairs = [[&quotgreat&quot, &quotfine&quot], [&quotacting&quot,&quotdrama&quot], [&quotskills&quot,&quottalent&quot]].
Note that the similarity relation is not transitive. For example, if &quotgreat&quot and &quotfine&quot are similar, and &quotfine&quot and &quotgood&quot are similar, &quotgreat&quot and &quotgood&quot are not necessarily similar.
However, similarity is symmetric. For example, &quotgreat&quot and &quotfine&quot being similar is the same as &quotfine&quot and &quotgreat&quot being similar.
Also, a word is always similar with itself. For example, the sentences words1 = [&quotgreat&quot], words2 = [&quotgreat&quot], pairs = [] are similar, even though there are no specified similar word pairs.
Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = [&quotgreat&quot] can never be similar to words2 = [&quotdoubleplus&quot,&quotgood&quot].
Note:
	The length of words1 and words2 will not exceed 1000.
	The length of pairs will not exceed 2000.
	The length of each pairs[i] will be 2.
	The length of each words[i] and pairs[i][j] will be in the range [1, 20].
## Solutions:
```python
class Solution :
public:
    bool areSentencesSimilar(vector& words1, vector& words2, vector>& pairs) :
        if (words1.size() != words2.size()) :
            return false
        unordered_map> synonyms
        for (auto& pair : pairs) :
            synonyms[pair[0]].insert(pair[1])
        for (int i = 0 i < words1.size() ++i) :
            if (words1[i] == words2[i]) continue
            if (!(synonyms.count(words1[i]) && synonyms[words1[i]].count(words2[i]) || 
               synonyms.count(words2[i]) && synonyms[words2[i]].count(words1[i]))) :
                return false
        return true
```
# 444. Sequence Reconstruction
* *Difficulty: Medium*
* *Topics: Graph, Topological Sort*
* *Similar Questions:*
  * [Course Schedule II](course-schedule-ii.md)
## Problem:
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 &le n &le 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
Example 1:
Input:
org: [1,2,3], seqs: [[1,2],[1,3]]
Output:
false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:
Input:
org: [1,2,3], seqs: [[1,2]]
Output:
false
Explanation:
The reconstructed sequence can only be [1,2].
Example 3:
Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
Output:
true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:
Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
Output:
true
UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.
## Solutions:
```python
class Solution :
public:
    bool sequenceReconstruction(vector& org, vector>& seqs) :
        unordered_map> nodeToNeighbors
        unordered_map dependencyCount
        for (auto seq : seqs) :
            for (auto num : seq) :
                nodeToNeighbors[num] = :
                dependencyCount[num] = 0
        if (nodeToNeighbors.size() != org.size())   return false
        for (auto seq : seqs) :
            for (int i = 1 i < seq.size() ++i) : // if we use i < sequence.size() -1 , there is underflow if sequence.size() == 0
                nodeToNeighbors[seq[i-1]].push_back(seq[i])
                ++dependencyCount[seq[i]]
        queue q
        for (auto nodeCountInfo : dependencyCount) :
            if (nodeCountInfo.second == 0) :
                q.push(nodeCountInfo.first)
        while (!q.empty()) :
            int size = q.size()
            if (size != 1)  return false
            int num = q.front() q.pop()
            for (auto node : nodeToNeighbors[num]) :
                if ((--dependencyCount[node]) == 0 ) :
                    q.push(node)
        for (auto nodeCountInfo : dependencyCount) :
            if (nodeCountInfo.second != 0)  return false
        return true
```
# 297. Serialize and Deserialize Binary Tree
* *Difficulty: Hard*
* *Topics: Tree, Design*
* *Similar Questions:*
  * [Encode and Decode Strings](encode-and-decode-strings.md)
  * [Serialize and Deserialize BST](serialize-and-deserialize-bst.md)
  * [Find Duplicate Subtrees](find-duplicate-subtrees.md)
  * [Serialize and Deserialize N-ary Tree](serialize-and-deserialize-n-ary-tree.md)
## Problem:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Example: 
You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5
as &quot[1,2,3,null,null,4,5]&quot
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Codec :
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) :
        string ret
        serializeHelper(root, ret)
        return ret
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) :
        int pos = 0
        return deserializeHelper(data, pos)
private:
    void serializeHelper(TreeNode* root, string& ret) :
        const static string NULL_STRING = "NULL" 
        if (root == nullptr) :
            ret.append(NULL_STRING)
            ret.push_back(' ')
            return
        ret.append(to_string(root->val))
        ret.push_back(' ')
        serializeHelper(root->left, ret)
        serializeHelper(root->right, ret)
    TreeNode* deserializeHelper(string& data, int& pos) :
        string token = getToken(data, pos)
        if (token == "NULL") :
            return nullptr
        TreeNode* root = new TreeNode(stoi(token))
        root->left = deserializeHelper(data, pos)
        root->right = deserializeHelper(data, pos)
        return root
    string getToken(string& data, int& pos) :
        string ret
        for (data[pos] != ' ' ++pos) :
            ret.push_back(data[pos])
        ++pos // remove space
        return ret
// Your Codec object will be instantiated and called as such:
// Codec codec
// codec.deserialize(codec.serialize(root)) 
```
# 449. Serialize and Deserialize BST
* *Difficulty: Medium*
* *Topics: Tree*
* *Similar Questions:*
  * [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree.md)
  * [Find Duplicate Subtrees](find-duplicate-subtrees.md)
  * [Serialize and Deserialize N-ary Tree](serialize-and-deserialize-n-ary-tree.md)
## Problem:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Codec :
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) :
        string s
        serializeHelper(root, s)
        return s
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) :
        int pos = 0
        return deserializeHelper(data, pos, INT_MAX)
    TreeNode* deserializeHelper(string& data, int& pos, int upper) :
        if (pos * sizeof(int) == data.length())   return NULL
        int val = *((reinterpret_cast (data.data())) + pos) // data.data()!
        if (val > upper)   return NULL
        TreeNode* root = new TreeNode(val)
        pos += 1
        root->left = deserializeHelper(data, pos, val - 1)
        root->right = deserializeHelper(data, pos, upper)
        return root
    void serializeHelper(TreeNode* root, string& s) :
        if (root == NULL)   return
        s.append(reinterpret_cast(&root->val), sizeof(root->val))
        serializeHelper(root->left, s)
        serializeHelper(root->right, s)
// Your Codec object will be instantiated and called as such:
// Codec codec
// codec.deserialize(codec.serialize(root))
```
# 765. Serialize and Deserialize N-ary Tree
* *Difficulty: Hard*
* *Topics: Tree*
* *Similar Questions:*
  * [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree.md)
  * [Serialize and Deserialize BST](serialize-and-deserialize-bst.md)
  * [Encode N-ary Tree to Binary Tree](encode-n-ary-tree-to-binary-tree.md)
## Problem:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.
For example, you may serialize the following 3-ary tree
as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note:
	N is in the range of  [1, 1000]
	Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
## Solutions:
```python
/*
// Definition for a Node.
class Node :
public:
    int val = NULL
    vector children
    Node() :
    Node(int _val, vector _children) :
        val = _val
        children = _children
*/
class Codec :
public:
    // Encodes a tree to a single string.
    string serialize(Node* root) :
        string buf
        serializeHelper(root, buf)
        return buf
    // Decodes your encoded data to tree.
    Node* deserialize(string data) :
        int pos = 0
        return deserializeHelper(data, pos)
private:
    Node* deserializeHelper(const string& buf, int& pos) :
        bool notNull = readBool(buf, pos)
        if (!notNull)   return nullptr
        int val = readInt(buf, pos)
        int childrenCount = readInt(buf, pos)
        vector children
        for (int i = 0 i < childrenCount ++i) :
            children.push_back(deserializeHelper(buf, pos))
        Node* node = new Node(val, children)
        return node
    void serializeHelper(Node* root, string& buf) :
        if (root == nullptr) :
            writeBool(buf, false)
            return
        writeBool(buf, true)
        writeInt(buf, root->val)
        int childrenCount = root->children.size()
        writeInt(buf, childrenCount)
        for (int i = 0 i children.size() ++i) :
            serializeHelper(root->children[i], buf)
    void writeBool(string& buf, bool val) :
        buf.append(val ? "1000" : "0000") // alignment!!!!
    bool readBool(const string& str, int& pos) :
        char c = str[pos]
        pos += 4
        return c == '1'
    void writeInt(string& str, int& val) :
        const char* valStr = reinterpret_cast (&val)
        str.append(valStr, sizeof(val))
    int readInt(const string& str, int& pos) :
        int val = *((reinterpret_cast (str.data() + pos)))
        pos += sizeof(int)
        return val
// Your Codec object will be instantiated and called as such:
// Codec codec
// codec.deserialize(codec.serialize(root))
```
# 73. Set Matrix Zeroes
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Game of Life](game-of-life.md)
## Problem:
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:
	A straight forward solution using O(mn) space is probably a bad idea.
	A simple improvement uses O(m + n) space, but still not the best solution.
	Could you devise a constant space solution?
## Solutions:
```python
class Solution :
public:
    void setZeroes(vector>& matrix) :
        int m = matrix.size()
        if (m == 0) return
        int n = matrix[0].size()
        if (n == 0) return
        bool firstRowSet = false
        bool firstColSet = false
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (matrix[i][j] == 0) :
                    if (i == 0 && j == 0) :
                        firstRowSet = true
                        firstColSet = true
                     else if (i == 0) :
                        firstRowSet = true
                        matrix[0][j] = 0
                     else if (j == 0) :
                        firstColSet = true
                        matrix[i][0] = 0
                     else :
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        for (int i = 1 i < m ++i) :
            if (matrix[i][0] == 0) :
                for (int j = 1 j < n ++j) :
                    matrix[i][j] = 0
        for (int j = 1 j < n ++j) :
            if (matrix[0][j] == 0) :
                for (int i = 1 i < m ++i) :
                    matrix[i][j] = 0
        if (firstRowSet) :
            for (int j = 0 j < n ++j) :
                matrix[0][j] = 0
        if (firstColSet) :
            for (int i = 0 i < m ++i) :
                matrix[i][0] = 0
```
# 645. Set Mismatch
* *Difficulty: Easy*
* *Topics: Hash Table, Math*
* *Similar Questions:*
  * [Find the Duplicate Number](find-the-duplicate-number.md)
## Problem:
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number. 
Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
## Solutions:
```python
class Solution :
public:
    vector findErrorNums(vector& nums) :
        int dup, miss
        for (auto& num : nums) :
            if (nums[abs(num) - 1] < 0) :
                dup = abs(num)
             else :
                nums[abs(num) - 1] *= -1
        for (int i = 0 i < nums.size() ++i) :
            if (nums[i] > 0) :
                miss = i + 1
                break
        return :dup, miss
```
# 317. Shortest Distance from All Buildings
* *Difficulty: Hard*
* *Topics: Breadth-first Search*
* *Similar Questions:*
  * [Walls and Gates](walls-and-gates.md)
  * [Best Meeting Point](best-meeting-point.md)
  * [As Far from Land as Possible](as-far-from-land-as-possible.md)
## Problem:
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
	Each 0 marks an empty land which you can pass by freely.
	Each 1 marks a building which you cannot pass through.
	Each 2 marks an obstacle which you cannot pass through.
Example:
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
Output: 7 
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
## Solutions:
```python
class Solution :
public:
    int shortestDistance(vector>& grid) :
        int m = grid.size()
        if (m == 0) return -1
        int n = grid[0].size()
        if (n == 0) return -1
        vector> reachable(m, vector(n, true))
        int emptyCount = 0
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] == 0) :
                    ++emptyCount
        if (emptyCount == 0)    return -1
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] != 1)    continue
                auto visited = bfs(grid, i, j)
                matrixAdd(m, n, reachable, visited)
        int minDistance = INT_MAX
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (grid[i][j] <= 0 && reachable[i][j]) :
                    minDistance = min(minDistance, -grid[i][j])
        return minDistance == INT_MAX ? -1 : minDistance
private:
    void matrixAdd(int m, int n, vector>& reachable, vector>& visited) :
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                reachable[i][j] = reachable[i][j] && visited[i][j]
    int directions[4][2] :
        :1, 0,
        :-1, 0,
        :0, 1,
        :0, -1
    vector> bfs(vector>& grid, int row, int col) :
        int m = grid.size()
        int n = grid[0].size()
        vector> visited(m, vector(n, false))
        int count = 0
        int distance = 0
        queue> q
        q.push(:row, col)
        while (!q.empty()) :
            int size = q.size()
            for (int i = 0 i < size ++i) :
                auto coord = q.front() q.pop()
                grid[coord.first][coord.second] -= distance
                for (int d = 0 d < 4 ++d) :
                    int newRow = coord.first + directions[d][0]
                    int newCol = coord.second + directions[d][1]
                    if (newRow >= 0 && newRow = 0 && newCol < n && grid[newRow][newCol] <= 0 && !visited[newRow][newCol]) :
                        q.push(:newRow, newCol)
                        visited[newRow][newCol] = true
                        ++count
            ++distance
        return visited
```
# 1134. Shortest Distance to Target Color
* *Difficulty: Medium*
* *Topics: Binary Search*
* *Similar Questions:*
## Problem:
You are given an array colors, in which there are three colors: 1, 2 and 3.
You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.
Example 1:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:
Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
Constraints:
	1 &lt= colors.length &lt= 5*10^4
	1 &lt= colors[i] &lt= 3
	1 &lt= queries.length &lt= 5*10^4
	queries[i].length == 2
	0 &lt= queries[i][0] &lt colors.length
	1 &lt= queries[i][1] &lt= 3
## Solutions:
```python
class Solution :
public:
    vector shortestDistanceColor(vector& colors, vector>& queries) :
        unordered_map> positions
        for (int i= 0 i < colors.size() ++i) :
            positions[colors[i]].push_back(i)
        vector ret
        for (auto& query : queries) :
            int index = query[0]
            int color = query[1]
            if (positions[color].empty()) :
                ret.push_back(-1)
             else :
                auto upperBound = upper_bound(positions[color].begin(), positions[color].end(), index)
                auto prevIt = prev(upperBound)
                if (upperBound == positions[color].end()) :
                    ret.push_back(abs(index - *prevIt))
                 else if (upperBound == positions[color].begin()) :
                    ret.push_back(abs(index - *upperBound))
                else :
                     ret.push_back(min(abs(index - *prevIt), abs(index - *upperBound)))
        return ret
```
# 214. Shortest Palindrome
* *Difficulty: Hard*
* *Topics: String*
* *Similar Questions:*
  * [Longest Palindromic Substring](longest-palindromic-substring.md)
  * [Implement strStr()](implement-strstr.md)
  * [Palindrome Pairs](palindrome-pairs.md)
## Problem:
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
Example 1:
Input: &quotaacecaaa&quot
Output: &quotaaacecaaa&quot
Example 2:
Input: &quotabcd&quot
Output: &quotdcbabcd&quot
## Solutions:
```python
class Solution :
public:
    string shortestPalindrome(string s) :
        if (s == "")    return ""
        string r = s
        reverse(r.begin(), r.end())
        int n = r.length()
        int forwardHash = 0
        int backwardHash = 0
        int val = 1
        int MOD = INT_MAX / 31
        int ret = 0
        for (int i = 0  i < n ++i) :
            forwardHash = (forwardHash + val * (s[i] - 'a' + 1)) % MOD
            val = (val * 31) % MOD
            backwardHash = ((backwardHash * 31) % MOD + (s[i] - 'a' + 1)) % MOD
            if (forwardHash == backwardHash) :
                ret = i
        return r + s.substr(ret + 1, n - ret - 1)
        return ""
```
# 895. Shortest Path to Get All Keys
* *Difficulty: Hard*
* *Topics: Heap, Breadth-first Search*
* *Similar Questions:*
## Problem:
We are given a 2-dimensional grid. &quot.&quot is an empty cell, &quot#&quot is a wall, &quot@&quot is the starting point, (&quota&quot, &quotb&quot, ...) are keys, and (&quotA&quot, &quotB&quot, ...) are locks.
We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can&#39t walk over a lock unless we have the corresponding key.
For some 1 &lt= K &lt= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys.  If it&#39s impossible, return -1.
Example 1:
Input: [&quot@.a.#&quot,&quot###.#&quot,&quotb.A.B&quot]
Output: 8
Example 2:
Input: [&quot@..aA&quot,&quot..B#.&quot,&quot....b&quot]
Output: 6
Note:
	1 &lt= grid.length &lt= 30
	1 &lt= grid[0].length &lt= 30
	grid[i][j] contains only &#39.&#39, &#39#&#39, &#39@&#39, &#39a&#39-&#39f&#39 and &#39A&#39-&#39F&#39
	The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
## Solutions:
```python
using namespace std
class Solution :
public:
    struct Status :
        int x
        int y
        int keys
        Status(int x, int y, int keys) :
            this->x = x
            this->y = y
            this->keys = keys
        bool operator<(const Status& other) const :
            if (x != other.x) :
                return x < other.x
            if (y != other.y) :
                return y < other.y
            return keys < other.keys
    inline bool isKey(char c) :
        return c >= 'a' && c <= 'z'
    inline bool isLock(char c) :
        return c >= 'A' && c <= 'Z'
    int shortestPathAllKeys(vector& grid) :
        int keyCount = 0
        pair startPoint
        int m = grid.size()
        if (m == 0) return 0
        int n = grid[0].length()
        if (n == 0) return 0
        for (int x = 0 x < m ++x) :
            for (int y = 0 y < n ++y) :
                if (grid[x][y] == '@') :
                    startPoint = :x, y
                 else if (isKey(grid[x][y])) :
                    ++keyCount
        if (keyCount == 0)  return 0
        queue q
        set visited
        q.push(:startPoint.first, startPoint.second, 0)
        int steps = 0
        int allKeys = (1 << keyCount) - 1
        while (!q.empty()) :
            int size = q.size() // The reason for my mistake is that I first define "int n = q.size()" !!! n outside this code block is shadowed! 
            for (int i = 0 i < size ++i) :
                Status s = q.front() q.pop()
                if (s.x = m || s.y = n || grid[s.x][s.y] == '#') continue
                if (visited.count(s) > 0)   continue
                visited.insert(s)
                if (isKey(grid[s.x][s.y])) :
                    s.keys = ((s.keys) | (1 << (grid[s.x][s.y] - 'a')))
                 else if (isLock(grid[s.x][s.y])) :
                    if (((s.keys >> (grid[s.x][s.y] - 'A')) & 1) != 1) :
                        continue
                visited.insert(s)
                if (s.keys == allKeys)  return steps
                q.push(:s.x + 1, s.y, s.keys)
                q.push(:s.x - 1, s.y, s.keys)
                q.push(:s.x, s.y + 1, s.keys)
                q.push(:s.x, s.y - 1, s.keys)
            ++steps
        return -1
```
# 581. Shortest Unsorted Continuous Subarray
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.  
You need to find the shortest such subarray and output its length.
Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means . 
## Solutions:
```python
class Solution :
public:
    int findUnsortedSubarray(vector& nums) :
        if (nums.size() == 0)   return 0
        vector copy = nums
        sort(copy.begin(), copy.end())
        int left = 0
        int right = nums.size() - 1
        while (left <= right && nums[left] == copy[left])  ++left
        while (left <= right && nums[right] == copy[right]) --right
        return right - left + 1
```
# 244. Shortest Word Distance II
* *Difficulty: Medium*
* *Topics: Hash Table, Design*
* *Similar Questions:*
  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)
  * [Shortest Word Distance](shortest-word-distance.md)
  * [Shortest Word Distance III](shortest-word-distance-iii.md)
## Problem:
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 
Example:
Assume that words = [&quotpractice&quot, &quotmakes&quot, &quotperfect&quot, &quotcoding&quot, &quotmakes&quot].
Input: word1 = &ldquocoding&rdquo, word2 = &ldquopractice&rdquo
Output: 3
Input: word1 = &quotmakes&quot, word2 = &quotcoding&quot
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
## Solutions:
```python
class WordDistance :
public:
    WordDistance(vector& words) :
        for (int i = 0 i < words.size() ++i) :
            wordToIndex[words[i]].push_back(i)
    int shortest(string word1, string word2) :
        return shortest(wordToIndex[word1], wordToIndex[word2])
    int shortest(vector& list1, vector& list2) :
        int ret = INT_MAX
        int pos1 = 0
        int pos2 = 0
        int last
        int lastSource
        if (list1[pos1] < list2[pos2]) :
            last = list1[pos1++]
            lastSource = 1
         else :
            last = list2[pos2++]
            lastSource = 2
        while (pos1 < list1.size() && pos2 < list2.size()) :
            if (list1[pos1] < list2[pos2]) :
                if (lastSource == 2) :
                    ret = min(ret, list1[pos1] - last)
                last = list1[pos1++]
                lastSource = 1
             else :
                if (lastSource == 1) :
                    ret = min(ret, list2[pos2] - last)
                last = list2[pos2++]
                lastSource = 2
        if (pos1 == list1.size()) :
            ret = min(ret, list2[pos2] - last)
         else :
            ret = min(ret, list1[pos1] - last)
        return ret
private:
    unordered_map> wordToIndex
/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(words)
 * int param_1 = obj->shortest(word1,word2)
 */
```
# 243. Shortest Word Distance
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Shortest Word Distance II](shortest-word-distance-ii.md)
  * [Shortest Word Distance III](shortest-word-distance-iii.md)
## Problem:
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
Example:
Assume that words = [&quotpractice&quot, &quotmakes&quot, &quotperfect&quot, &quotcoding&quot, &quotmakes&quot].
Input: word1 = &ldquocoding&rdquo, word2 = &ldquopractice&rdquo
Output: 3
Input: word1 = &quotmakes&quot, word2 = &quotcoding&quot
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
## Solutions:
```python
class Solution :
public:
    int shortestDistance(vector& words, string word1, string word2) :
        int index1 = -1
        int index2 = -1
        int distance = INT_MAX
        for (int i = 0 i < words.size() ++i) :
            if (words[i] == word1) :
                index1 = i
                if (index2 != -1)
                    distance = min(distance, i - index2)
             else if (words[i] == word2) :
                index2 = i
                if (index1 != -1) :
                    distance = min(distance, i - index1)
        return distance
```
# 384. Shuffle an Array
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
## Problem:
Shuffle a set of numbers without duplicates.
Example:
// Init an array with set 1, 2, and 3.
int[] nums = :1,2,3
Solution solution = new Solution(nums)
// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle()
// Resets the array back to its original configuration [1,2,3].
solution.reset()
// Returns the random shuffling of array [1,2,3].
solution.shuffle()
## Solutions:
```python
class Solution :
public:
    Solution(vector& nums) :
        this->nums = nums
    /** Resets the array to its original configuration and return it. */
    vector reset() :
        return nums
    /** Returns a random shuffling of the array. */
    vector shuffle() :
        vector ret(nums.begin(), nums.end())
        for (int i = 0 i < ret.size() ++i) :
            int pos = rand() % (ret.size() - i)
            swap(ret[i], ret[i + pos])
        return ret
private:
    vector nums
/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums)
 * vector param_1 = obj->reset()
 * vector param_2 = obj->shuffle()
 */
```
# 71. Simplify Path
* *Difficulty: Medium*
* *Topics: String, Stack*
* *Similar Questions:*
## Problem:
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
Example 1:
Input: &quot/home/&quot
Output: &quot/home&quot
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:
Input: &quot/../&quot
Output: &quot/&quot
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:
Input: &quot/home//foo/&quot
Output: &quot/home/foo&quot
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:
Input: &quot/a/./b/../../c/&quot
Output: &quot/c&quot
Example 5:
Input: &quot/a/../../b/../c//.//&quot
Output: &quot/c&quot
Example 6:
Input: &quot/a//b////c/d//././/..&quot
Output: &quot/a/b/c&quot
## Solutions:
```python
class Solution :
public:
    string simplifyPath(string path) :
        path.push_back('/') // an elegant solution for last element
        deque dq // deque is more appropriate than stack because the result need queue-like access. 
        string directory
        for (int i = 0 i < path.length() ++i) :
            if (path[i] == '/') :
                if (directory == "" || directory == ".") :
                 else if (directory == "..") :
                    if (!dq.empty()) :
                        dq.pop_back()
                 else :
                    dq.push_back(directory)
                directory.clear()
             else :
                directory.push_back(path[i])
        if (dq.empty())    return "/"
        string ret
        while (!dq.empty()) :
            ret.push_back('/')
            ret.append(dq.front()) dq.pop_front()
        return ret
```
# 137. Single Number II
* *Difficulty: Medium*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Single Number](single-number.md)
  * [Single Number III](single-number-iii.md)
## Problem:
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,3,2]
Output: 3
Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
## Solutions:
```python
class Solution :
public:
    int singleNumber(vector& nums) :
        int ones = 0
        int tens = 0
        for (auto num : nums) :
            ones = ones ^ num
            int carry = (~ones) & num
            tens = tens ^ carry
            int mask = ones & tens
            ones = ones & (~mask)
            tens = tens & (~mask)
        return ones
```
# 260. Single Number III
* *Difficulty: Medium*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Single Number](single-number.md)
  * [Single Number II](single-number-ii.md)
## Problem:
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:
	The order of the result is not important. So in the above example, [5, 3] is also correct.
	Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
## Solutions:
```python
class Solution :
public:
    vector singleNumber(vector& nums) :
        int digest = 0
        for (auto& num : nums) :
            digest ^= num
        // String from the least significant bit, the first bit set to 1 
        digest &= (-digest)
        vector ret(2, 0)
        for (auto& num : nums) :
            if (num & digest) :
                ret[0] ^= num
             else :
                ret[1] ^= num
        return ret
```
# 136. Single Number
* *Difficulty: Easy*
* *Topics: Hash Table, Bit Manipulation*
* *Similar Questions:*
  * [Single Number II](single-number-ii.md)
  * [Single Number III](single-number-iii.md)
  * [Missing Number](missing-number.md)
  * [Find the Duplicate Number](find-the-duplicate-number.md)
  * [Find the Difference](find-the-difference.md)
## Problem:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:
Input: [4,1,2,1,2]
Output: 4
## Solutions:
```python
class Solution :
public:
    int singleNumber(vector& nums) :
        int ret = 0
        for (auto num : nums) :
            ret ^= num
        return ret
```
# 787. Sliding Puzzle
* *Difficulty: Hard*
* *Topics: Breadth-first Search*
* *Similar Questions:*
## Problem:
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
Examples:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:
	board will be a 2 x 3 array as described above.
	board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
## Solutions:
```python
class Solution :
public:
    int slidingPuzzle(vector>& board) :
        string start
        int row, col
        for (int i = 0 i < 2 ++i) :
            for (int j = 0 j < 3 ++j) :
                start.push_back(board[i][j] + '0')
                if (board[i][j] == 0) :
                    row = i
                    col = j
        unordered_set visited
        queue> q
        q.push(:start, 3 * row + col)
        string end = "123450"
        int ret = 0
        while (!q.empty()) :
            int size = q.size()
            for (int i = 0 i < size ++i) :
                string state = q.front().first
                int pos = q.front().second
                q.pop()
                if (visited.count(state) > 0)   continue
                visited.insert(state)
                if (state == end)   return ret
                for (auto neighbor : neighbors[pos]) :
                    swap(state[pos], state[neighbor])
                    q.push(:state, neighbor)
                    swap(state[pos], state[neighbor])
            ++ret
        return -1
private:
    vector> neighbors = :
        :1, 3, // 0
        :0, 2, 4, // 1
        :1, 5, // 2
        :0, 4, // 3
        :1, 3, 5, // 4
        :2, 4, // 5
```
# 239. Sliding Window Maximum
* *Difficulty: Hard*
* *Topics: Heap, Sliding Window*
* *Similar Questions:*
  * [Minimum Window Substring](minimum-window-substring.md)
  * [Min Stack](min-stack.md)
  * [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters.md)
  * [Paint House II](paint-house-ii.md)
## Problem:
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 &le k &le input array&#39s size for non-empty array.
Follow up:
Could you solve it in linear time?
## Solutions:
```python
class Solution :
public:
    vector maxSlidingWindow(vector& nums, int k) :
        deque q
        for (int i = 0 i < k - 1 ++i) :
            while (!q.empty() && q.back() < nums[i]) :
                q.pop_back()
            q.push_back(nums[i])
        vector ret
        for (int i = k - 1 i < nums.size() ++i) :
            int val = nums[i]
            while (!q.empty() && q.back() < val) :
                q.pop_back()
            q.push_back(val)
            ret.push_back(q.front())
            if (nums[i - (k - 1)] == q.front()) :
                q.pop_front()
        return ret
```
# 944. Smallest Range I
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
## Problem:
Given an array A of integers, for each integer A[i] we may choose any x with -K &lt= x &lt= K, and add x to A[i].
After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the minimum value of B.
Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:
Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]
Note:
	1 &lt= A.length &lt= 10000
	0 &lt= A[i] &lt= 10000
	0 &lt= K &lt= 10000
## Solutions:
```python
class Solution :
public:
    int smallestRangeI(vector& A, int K) :
        if (A.size() == 0)  return 0
        int minVal = A[0]
        int maxVal = A[0]
        for (int i = 1 i < A.size() ++i) :
            minVal = min(minVal, A[i])
            maxVal = max(maxVal, A[i])
        if (maxVal - minVal <= 2 * K) return 0
        return maxVal - minVal - 2 * K
```
# 302. Smallest Rectangle Enclosing Black Pixels
* *Difficulty: Hard*
* *Topics: Binary Search*
* *Similar Questions:*
## Problem:
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
Example:
Input:
[
  &quot0010&quot,
  &quot0110&quot,
  &quot0100&quot
]
and x = 0, y = 2
Output: 6
## Solutions:
```python
class Solution :
public:
    int minArea(vector>& image, int x, int y) :
        int m = image.size()
        if (m == 0) return 0
        int n = image[0].size()
        if (n == 0) return 0
        int up = searchByRow(image, 0, x, m, n, true)
        int down = searchByRow(image, x, m - 1, m, n, false)
        int right = searchByColumn(image, y, n - 1, m, n, true)
        int left = searchByColumn(image, 0, y, m, n, false)
        return (down - up + 1) * (right - left + 1)
private:
    int searchByRow(vector>& image, int up, int down, int m, int n, bool upwards) :
        while (up + 1 < down) :
            int mid = up + (down - up) / 2
            if (pixelInRow(image, mid, m, n)) :
                if (upwards) :
                    down = mid
                 else :
                    up = mid
             else :
                if (upwards) :
                    up = mid
                 else :
                    down = mid
        if (upwards) :
            return pixelInRow(image, up, m, n) ? up : down
         else :
            return pixelInRow(image, down, m, n) ? down : up
    int searchByColumn(vector>& image, int left, int right, int m, int n, bool forwards) :
        while (left + 1 < right) :
            int mid = left + (right - left) / 2
            if (pixelInColumn(image, mid, m, n)) :
                if (forwards) :
                    left = mid
                 else :
                    right = mid
             else :
                if (forwards) :
                    right = mid
                 else :
                    left = mid
        if (forwards) :
            return pixelInColumn(image, right, m, n) ? right : left
         else :
            return pixelInColumn(image, left, m, n) ? left : right
    bool pixelInRow(vector>& image, int row, int m, int n) :
        for (int i = 0 i < n ++i) :
            if (image[row][i] == '1')   return true
        return false
    bool pixelInColumn(vector>& image, int col, int m, int n) :
        for (int i = 0 i < m ++i) :
            if (image[i][col] == '1')   return true
        return false
```
# 941. Sort Array By Parity
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
## Problem:
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.
Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Note:
	1 &lt= A.length &lt= 5000
	0 &lt= A[i] &lt= 5000
## Solutions:
```python
class Solution :
public:
    vector sortArrayByParity(vector& A) :
        int left = 0
        int right = A.size() - 1
        while (left < right) :
            while (left < right && A[left] % 2 == 0)   ++left
            while (left < right && A[right] % 2 == 1)   --right
            if (left < right) :
                swap(A[left], A[right])
                ++left
                --right
        return A
```
# 75. Sort Colors
* *Difficulty: Medium*
* *Topics: Array, Two Pointers, Sort*
* *Similar Questions:*
  * [Sort List](sort-list.md)
  * [Wiggle Sort](wiggle-sort.md)
  * [Wiggle Sort II](wiggle-sort-ii.md)
## Problem:
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library&#39s sort function for this problem.
Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:
	A rather straight forward solution is a two-pass algorithm using counting sort.
	First, iterate the array counting number of 0&#39s, 1&#39s, and 2&#39s, then overwrite array with total number of 0&#39s, then 1&#39s and followed by 2&#39s.
	Could you come up with a one-pass algorithm using only constant space?
## Solutions:
```python
class Solution :
public:
    void sortColors(vector& nums) :
        int left = 0
        int right = nums.size() - 1
        for (int i = left i <= right ) : // not include ++i to continue swap if necessary otherwise [1, 2, 0] fails 
            if (nums[i] == 0 && i != left) : // remember the second check otherwise [] would fail
                swap(nums[i], nums[left])
                ++left
             else if (nums[i] == 2 && i != right) : // remember the second check otherwise [] would fail
                swap(nums[i], nums[right])
                --right
             else :
                ++i
```
# 148. Sort List
* *Difficulty: Medium*
* *Topics: Linked List, Sort*
* *Similar Questions:*
  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)
  * [Sort Colors](sort-colors.md)
  * [Insertion Sort List](insertion-sort-list.md)
## Problem:
Sort a linked list in O(n log n) time using constant space complexity.
Example 1:
Input: 4-&gt2-&gt1-&gt3
Output: 1-&gt2-&gt3-&gt4
Example 2:
Input: -1-&gt5-&gt3-&gt4-&gt0
Output: -1-&gt0-&gt3-&gt4-&gt5
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* sortList(ListNode* head) :
        if (head == nullptr)    return nullptr
        if (head->next == nullptr)  return head
        ListNode* slow = head
        ListNode* fast = head
        while (fast->next !=  nullptr && fast->next->next != nullptr) :
            slow = slow->next
            fast = fast->next->next
        ListNode* head2 = slow->next
        slow->next = nullptr
        ListNode* leftHead = sortList(head)
        ListNode* rightHead = sortList(head2)
        ListNode* dummy = new ListNode(0)
        ListNode* tail = dummy
        while (leftHead != nullptr && rightHead != nullptr) :
            if (leftHead->val val) :
                tail->next = leftHead
                tail = leftHead
                leftHead = leftHead->next
             else :
                tail->next = rightHead
                tail = rightHead
                rightHead = rightHead->next
        if (leftHead == nullptr) :
            tail->next = rightHead
         else :
            tail->next = leftHead
        return dummy->next
```
# 360. Sort Transformed Array
* *Difficulty: Medium*
* *Topics: Math, Two Pointers*
* *Similar Questions:*
  * [Squares of a Sorted Array](squares-of-a-sorted-array.md)
## Problem:
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.
The returned array must be in sorted order.
Expected time complexity: O(n)
Example 1:
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
## Solutions:
```python
class Solution :
public:
    vector sortTransformedArray(vector& nums, int a, int b, int c) :
        this->a = a
        this->b = b
        this->c = c
        if (nums.size() == 0)   return :
        if (a == 0) :
            if (b < 0) :
                reverse(nums.begin(), nums.end())
            vector ret
            for (auto& val : nums) :
                ret.push_back(f(val))
            return ret
        double vertex = -b / (double)(2 * a)
        int left = 0, right = nums.size() - 1 // largest value smaller than
        while (left < right) :
            int mid = right - (right - left) / 2
            if (vertex <= nums[mid]) :
                right = mid - 1
             else :
                left = mid
        vector ret
        right = left + 1
        while (left >= 0 && right < nums.size()) :
            if (abs(nums[left] - vertex) <= abs(nums[right] - vertex)) :
                ret.push_back(f(nums[left]))
                --left
             else :
                ret.push_back(f(nums[right]))
                ++right
        if (left < 0) :
            while (right < nums.size()) :
                ret.push_back(f(nums[right++]))
        if (right >= nums.size()) :
            while (left >= 0) :
                ret.push_back(f(nums[left--]))
        if (a < 0) :
            reverse(ret.begin(), ret.end())
        return ret
private:
    inline int f(int x) :
        return a * x * x + b * x + c
    int a
    int b
    int c
```
# 826. Soup Servings
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
## Problem:
There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:
	Serve 100 ml of soup A and 0 ml of soup B
	Serve 75 ml of soup A and 25 ml of soup B
	Serve 50 ml of soup A and 50 ml of soup B
	Serve 25 ml of soup A and 75 ml of soup B
When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.
Note that we do not have the operation where all 100 ml&#39s of soup B are used first.  
Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.
Example:
Input: N = 50
Output: 0.625
Explanation: 
If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
Notes: 
	0 &lt= N &lt= 10^9. 
	Answers within 10^-6 of the true value will be accepted as correct.
## Solutions:
```python
class Solution :
public:
    double soupServings(int N) :
        map, double> cache
        if (N > 5000)    return 1.0
        return helper(N, N, cache)
private:
    double helper(int A, int B, map, double>& cache) :
        if (A <= 0 && B <= 0)   return 0.5
        if (A <= 0) return 1
        if (B <= 0) return 0
        if (cache.count(:A, B)) :
            return cache[:A, B]
        double ret = 0.25 * helper(A - 100, B, cache) + 0.25 * helper(A - 75, B - 25, cache) + 0.25 * helper(A - 50, B - 50, cache) + 0.25 * helper(A - 25, B - 75, cache)
        cache[:A, B] = ret
        return ret
```
# 311. Sparse Matrix Multiplication
* *Difficulty: Medium*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
Given two sparse matrices A and B, return the result of AB.
You may assume that A&#39s column number is equal to B&#39s row number.
Example:
Input:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
Output:
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
## Solutions:
```python
class Solution :
public:
    vector> multiply(vector>& A, vector>& B) :
        int m = A.size()
        if (m == 0) return :
        int k = A[0].size()
        if (k == 0) return :
        int n = B[0].size()
        if (n == 0) return :
        vector> matrix(m, vector(n, 0))
        for (int row = 0 row < m ++row) :
            for (int col = 0 col < k ++col) :
                if (A[row][col] == 0)   continue
                for (int i = 0 i < n ++i) :
                    matrix[row][i] += A[row][col] * B[col][i]
        return matrix
```
# 59. Spiral Matrix II
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Spiral Matrix](spiral-matrix.md)
## Problem:
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
## Solutions:
```python
class Solution :
public:
    vector> generateMatrix(int n) :
        int top = 0
        int down = n - 1
        int left = 0
        int right = n - 1
        vector> matrix(n, vector(n, 0))
        int row = 0
        int col = 0
        int val = 1
        matrix[row][col] = val++
        while (true) :
            if (col + 1 > right)    return matrix
            while (col + 1 <= right) :
                ++col
                matrix[row][col] = val++
            ++top
            if (row + 1 > down) return matrix
            while (row + 1 <= down) :
                ++row
                matrix[row][col] = val++
            --right
            if (col - 1 < left) return matrix
            while (col - 1 >= left) :
                --col
                matrix[row][col] = val++
            --down
            if (row - 1 < top) return matrix
            while (row - 1 >= top) :
                --row
                matrix[row][col] = val++
            ++left
private:
    int directions[4][2] = :
        :1, 0,
        :0, 1,
        :-1, 0,
        :0, -1
```
# 54. Spiral Matrix
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Spiral Matrix II](spiral-matrix-ii.md)
## Problem:
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
## Solutions:
```python
class Solution :
public:
    vector spiralOrder(vector>& matrix) :
        int m = matrix.size()
        if (m == 0) return :
        int n = matrix[0].size()
        if (n == 0) return :
        vector ret
        int top = 0
        int bottom = m - 1
        int left = 0
        int right = n - 1
        int row = 0
        int col = -1
        int d = 0
        for () :
            // to right
            if (col + 1 > right)    return ret
            while (col < right) :
                ret.push_back(matrix[row][++col])
            ++top
            // to bottom
            if (row + 1 > bottom)   return ret
            while (row < bottom) :
                ret.push_back(matrix[++row][col])
            --right
            // to left
            if (col - 1 < left) return ret
            while (col > left) :
                ret.push_back(matrix[row][--col])
            --bottom
            //to top
            if (row - 1 < top)  return ret
            while (row > top) :
                ret.push_back(matrix[--row][col])
            ++left
```
# 410. Split Array Largest Sum
* *Difficulty: Hard*
* *Topics: Binary Search, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
Note:
If n is the length of array, assume the following constraints are satisfied:
1 &le n &le 1000
1 &le m &le min(50, n)
Examples: 
Input:
nums = [7,2,5,10,8]
m = 2
Output:
18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
## Solutions:
```python
class Solution :
public:
    int splitArray(vector& nums, int m) :
        int n = nums.size()
        // not finalize
        vector> dp(m + 1, vector(n + 1, INT_MAX))
        dp[0][0] = 0
        for (int i = 1 i <= m ++i) :
            for (int j = i j <= n ++j) :
                long sum = 0
                dp[i][j] = INT_MAX
                for (int k = 0 k <= j - i ++k) :
                    sum += nums[j - 1 - k]
                    dp[i][j] = min(dp[i][j], max(sum, dp[i-1][j - k -1] ))
                //cout << i << " " << j << " " << dp[i][j] << endl
        return dp[m][n]
        //dp[i][j] = min(dp[i-1][0..k], sigma(nums[k..j]))
```
# 69. Sqrt(x)
* *Difficulty: Easy*
* *Topics: Math, Binary Search*
* *Similar Questions:*
  * [Pow(x, n)](powx-n.md)
  * [Valid Perfect Square](valid-perfect-square.md)
## Problem:
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Example 1:
Input: 4
Output: 2
Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
## Solutions:
```python
class Solution :
public:
    int mySqrt(int x) :
        int left = 0
        int right = INT_MAX
        while (left + 1 < right) :
            int mid = left + (right - left)/2
            if (x/mid >= mid) : // mid * mid <= x would cause overflow
                left = mid
             else :
                right = mid
        if (x/right >= right)   return right
        return left
```
# 1019. Squares of a Sorted Array
* *Difficulty: Easy*
* *Topics: Array, Two Pointers*
* *Similar Questions:*
  * [Merge Sorted Array](merge-sorted-array.md)
  * [Sort Transformed Array](sort-transformed-array.md)
## Problem:
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Note:
	1 &lt= A.length &lt= 10000
	-10000 &lt= A[i] &lt= 10000
	A is sorted in non-decreasing order.
## Solutions:
```python
class Solution :
public:
    vector sortedSquares(vector& A) :
        int right = distance(A.begin(), lower_bound(A.begin(), A.end(), 0))
        int left = right - 1
        vector ret
        while (left >= 0 && right < A.size()) :
            if (abs(A[left]) <= abs(A[right])) :
                ret.push_back(A[left] * A[left])
                --left
             else :
                ret.push_back(A[right] * A[right])
                ++right
        if (left < 0) :
            while (right < A.size()) :
                ret.push_back(A[right] * A[right])
                ++right
         else :
            while (left >= 0) :
                ret.push_back(A[left] * A[left])
                --left
        return ret
```
# 1151. Stepping Numbers
* *Difficulty: Medium*
* *Topics: Backtracking*
* *Similar Questions:*
## Problem:
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.
Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.
Example 1:
Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
Constraints:
	0 &lt= low &lt= high &lt= 2 * 10^9
## Solutions:
```python
class Solution :
public:
    vector countSteppingNumbers(int low, int high) :
        vector ret
        if (low = 0)  ret.push_back(0)
        for (int i = 1 i <= 9 ++i) :
            dfs(i, low, high, ret)
        sort(ret.begin(), ret.end())
        return ret
private:
    void dfs(int num, int low, int high, vector& ret) :
        if (num > high) return
        if (num >= low) :
            ret.push_back(num)
        int lastDigit = num % 10
        if (lastDigit - 1 >= 0 && num < INT_MAX / 10) :
            dfs(num * 10 + (lastDigit - 1), low, high, ret)
        if (lastDigit + 1 <= 9 && num < INT_MAX / 10) :
            dfs(num * 10 + (lastDigit + 1), low, high, ret)
```
# 443. String Compression
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Count and Say](count-and-say.md)
  * [Encode and Decode Strings](encode-and-decode-strings.md)
  * [Design Compressed String Iterator](design-compressed-string-iterator.md)
## Problem:
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.
Follow up:
Could you solve it using only O(1) extra space?
Example 1:
Input:
[&quota&quot,&quota&quot,&quotb&quot,&quotb&quot,&quotc&quot,&quotc&quot,&quotc&quot]
Output:
Return 6, and the first 6 characters of the input array should be: [&quota&quot,&quot2&quot,&quotb&quot,&quot2&quot,&quotc&quot,&quot3&quot]
Explanation:
&quotaa&quot is replaced by &quota2&quot. &quotbb&quot is replaced by &quotb2&quot. &quotccc&quot is replaced by &quotc3&quot.
Example 2:
Input:
[&quota&quot]
Output:
Return 1, and the first 1 characters of the input array should be: [&quota&quot]
Explanation:
Nothing is replaced.
Example 3:
Input:
[&quota&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot,&quotb&quot]
Output:
Return 4, and the first 4 characters of the input array should be: [&quota&quot,&quotb&quot,&quot1&quot,&quot2&quot].
Explanation:
Since the character &quota&quot does not repeat, it is not compressed. &quotbbbbbbbbbbbb&quot is replaced by &quotb12&quot.
Notice each digit has it&#39s own entry in the array.
Note:
	All characters have an ASCII value in [35, 126].
	1 &lt= len(chars) &lt= 1000.
## Solutions:
```python
class Solution :
public:
    int compress(vector& chars) :
        if (chars.size() == 0)    return 0
        int pos = 0
        int index = 0
        char c
        int count
        while (index < chars.size()) :
            c = chars[index++]
            count = 1
            while (index < chars.size() && chars[index] == c) :
                ++index
                ++count
            if (count == 1) :
                chars[pos++] = c
             else :
                chars[pos++] = c
                string countStr = to_string(count)
                for (auto& v : countStr) :
                    chars[pos++] = v
        return pos
```
# 8. String to Integer (atoi)
* *Difficulty: Medium*
* *Topics: Math, String*
* *Similar Questions:*
  * [Reverse Integer](reverse-integer.md)
  * [Valid Number](valid-number.md)
## Problem:
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
Note:
	Only the space character &#39 &#39 is considered as whitespace character.
	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus231,  231 &minus 1]. If the numerical value is out of the range of representable values, INT_MAX (231 &minus 1) or INT_MIN (&minus231) is returned.
Example 1:
Input: &quot42&quot
Output: 42
Example 2:
Input: &quot   -42&quot
Output: -42
Explanation: The first non-whitespace character is &#39-&#39, which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:
Input: &quot4193 with words&quot
Output: 4193
Explanation: Conversion stops at digit &#393&#39 as the next character is not a numerical digit.
Example 4:
Input: &quotwords and 987&quot
Output: 0
Explanation: The first non-whitespace character is &#39w&#39, which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:
Input: &quot-91283472332&quot
Output: -2147483648
Explanation: The number &quot-91283472332&quot is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (&minus231) is returned.
## Solutions:
```python
class Solution :
public:
    int myAtoi(string str) :
        int cur = 0
        while (cur < str.length() && str[cur] == ' ') // single quote
            ++cur
        if (str.length() == cur)  return 0
        int sign = 1
        if (str[cur] == '-' || str[cur] == '+') :      // single quote && remeber to handle '+'
            sign = (str[cur] == '-' ? -1 : 1)
            ++cur
        int ret = 0
        while (cur < str.length() && isdigit(str[cur])) :   // isdigit
            int digit = str[cur] - '0'
            if (ret > INT_MAX/10 || ret == INT_MAX/10 && digit > INT_MAX%10 ) : // only compare INT_MAX otherwise the case of "-2147483648" is wrong.  
                return sign == 1 ? INT_MAX : INT_MIN
            ret = ret * 10 + digit
            ++cur // remember to increase cur
        return sign == 1 ? ret : -ret
```
# 246. Strobogrammatic Number
* *Difficulty: Easy*
* *Topics: Hash Table, Math*
* *Similar Questions:*
  * [Strobogrammatic Number II](strobogrammatic-number-ii.md)
  * [Strobogrammatic Number III](strobogrammatic-number-iii.md)
  * [Confusing Number](confusing-number.md)
## Problem:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.
Example 1:
Input:  &quot69&quot
Output: true
Example 2:
Input:  &quot88&quot
Output: true
Example 3:
Input:  &quot962&quot
Output: false
## Solutions:
```python
class Solution :
public:
    bool isStrobogrammatic(string num) :
        unordered_map mirror :
            :'0', '0',
            :'1', '1',
            :'6', '9',
            :'8', '8',
            :'9', '6'
        int left = 0
        int right = num.length() - 1
        while (left <= right) :
            if (mirror.count(num[left]) == 0 || mirror[num[left]] != num[right])    return false
            ++left
            --right
        return true
```
# 551. Student Attendance Record I
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Student Attendance Record II](student-attendance-record-ii.md)
## Problem:
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent. 
'L' : Late.
 'P' : Present. 
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).    
You need to return whether the student could be rewarded according to his attendance record.
Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
## Solutions:
```python
class Solution :
public:
    bool checkRecord(string s) :
        int absentCount = 0
        int lateCount = 0
        for (auto c : s) :
            switch(c) :
                case 'A':
                    if (++absentCount == 2) return false
                    lateCount = 0
                    break
                case 'L':
                    if (++lateCount == 3)   return false
                    break
                case 'P':
                    lateCount = 0
        return true
```
# 552. Student Attendance Record II
* *Difficulty: Hard*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Student Attendance Record I](student-attendance-record-i.md)
## Problem:
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
A student attendance record is a string that only contains the following three characters:
'A' : Absent. 
'L' : Late.
 'P' : Present. 
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note:
The value of n won't exceed 100,000.
## Solutions:
```python
class Solution :
public:
    int checkRecord(int n) :
        vector> dp (2, vector(6, 1))
        for (int i = 1 i <= n ++i) :
            for (int a = 0 a < 2 ++a) :
                for (int l = 0 l < 3 ++l) :
                    int pos = getPosition(a, l)
                    // get P
                    dp[i & 0x1][pos] = dp[(i-1) & 0x1][getPosition(a, 2)] 
                    // get A
                    if (a > 0) :
                        dp[i & 0x1][pos] = (dp[i & 0x1][pos] + dp[(i-1) & 0x1][getPosition(a - 1, 2)]) % MOD
                    // get L
                    if (l > 0) :
                        dp[i & 0x1][pos] = (dp[i & 0x1][pos] + dp[(i-1) & 0x1][getPosition(a, l - 1)]) % MOD
        return dp[n & 0x1][getPosition(1, 2)]
private:
    inline int getPosition(int absent, int late) :
        return absent * 3 + late
    static constexpr int MOD = 1000000007
```
# 560. Subarray Sum Equals K
* *Difficulty: Medium*
* *Topics: Array, Hash Table*
* *Similar Questions:*
  * [Two Sum](two-sum.md)
  * [Continuous Subarray Sum](continuous-subarray-sum.md)
  * [Subarray Product Less Than K](subarray-product-less-than-k.md)
  * [Find Pivot Index](find-pivot-index.md)
  * [Subarray Sums Divisible by K](subarray-sums-divisible-by-k.md)
## Problem:
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
## Solutions:
```python
class Solution :
public:
    int subarraySum(vector& nums, int k) :
        int ret = 0
        int sum = 0
        unordered_map valueCount
        ++valueCount[sum]
        for (auto num : nums) :
            sum += num
            int target = sum - k
            if (valueCount.count(target) > 0) :
                ret += valueCount[target]
            ++valueCount[sum]
        return ret
```
# 1034. Subarrays with K Different Integers
* *Difficulty: Hard*
* *Topics: Hash Table, Two Pointers, Sliding Window*
* *Similar Questions:*
  * [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md)
  * [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters.md)
  * [Longest Substring with At Most K Distinct Characters](longest-substring-with-at-most-k-distinct-characters.md)
## Problem:
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of A.
Example 1:
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:
Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
Note:
	1 &lt= A.length &lt= 20000
	1 &lt= A[i] &lt= A.length
	1 &lt= K &lt= A.length
## Solutions:
```python
/**
 * Two pointer + Indirection
 */
class Solution :
public:
    int subarraysWithKDistinct(vector& A, int K) :
        return lessThanK(A, K) - lessThanK(A, K - 1)
private:
    int lessThanK(vector& A, int K) :
        unordered_map numCount
        int count = 0
        int l = 0
        for (int r = 0 r < A.size() ++r) :
            if (numCount[A[r]]++ == 0) :
                --K
            while (K < 0) :
                if (--numCount[A[l++]] == 0) ++K
            count += r - l + 1
        return count
```
# 829. Subdomain Visit Count
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
A website domain like &quotdiscuss.leetcode.com&quot consists of various subdomains. At the top level, we have &quotcom&quot, at the next level, we have &quotleetcode.com&quot, and at the lowest level, &quotdiscuss.leetcode.com&quot. When we visit a domain like &quotdiscuss.leetcode.com&quot, we will also visit the parent domains &quotleetcode.com&quot and &quotcom&quot implicitly.
Now, call a &quotcount-paired domain&quot to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be &quot9001 discuss.leetcode.com&quot.
We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.
Example 1:
Input: 
[&quot9001 discuss.leetcode.com&quot]
Output: 
[&quot9001 discuss.leetcode.com&quot, &quot9001 leetcode.com&quot, &quot9001 com&quot]
Explanation: 
We only have one website domain: &quotdiscuss.leetcode.com&quot. As discussed above, the subdomain &quotleetcode.com&quot and &quotcom&quot will also be visited. So they will all be visited 9001 times.
Example 2:
Input: 
[&quot900 google.mail.com&quot, &quot50 yahoo.com&quot, &quot1 intel.mail.com&quot, &quot5 wiki.org&quot]
Output: 
[&quot901 mail.com&quot,&quot50 yahoo.com&quot,&quot900 google.mail.com&quot,&quot5 wiki.org&quot,&quot5 org&quot,&quot1 intel.mail.com&quot,&quot951 com&quot]
Explanation: 
We will visit &quotgoogle.mail.com&quot 900 times, &quotyahoo.com&quot 50 times, &quotintel.mail.com&quot once and &quotwiki.org&quot 5 times. For the subdomains, we will visit &quotmail.com&quot 900 + 1 = 901 times, &quotcom&quot 900 + 50 + 1 = 951 times, and &quotorg&quot 5 times.
Notes: 
	The length of cpdomains will not exceed 100. 
	The length of each domain name will not exceed 100.
	Each address will have either 1 or 2 &quot.&quot characters.
	The input count in any count-paired domain will not exceed 10000.
	The answer output can be returned in any order.
## Solutions:
```python
class Solution :
public:
    vector subdomainVisits(vector& cpdomains) :
        for (auto& cpdomain : cpdomains) :
            parseDomainCount(cpdomain)
        vector ret
        for (auto it = domainCount.begin() it != domainCount.end() ++it) :
            ret.push_back(to_string(it->second) + " " + it->first)
        return ret
private:
    unordered_map domainCount
    void parseDomainCount(string& cpdomain) :
        int pos = 0
        while (isdigit(cpdomain[pos])) ++pos
        int count = stoi(cpdomain.substr(0, pos))
        // consume empty space
        ++pos
        domainCount[cpdomain.substr(pos)] += count
        while (true) :
            while (pos < cpdomain.length() && cpdomain[pos] != '.') ++pos
            if (pos == cpdomain.length())   return
            domainCount[cpdomain.substr(++pos)] += count
```
# 90. Subsets II
* *Difficulty: Medium*
* *Topics: Array, Backtracking*
* *Similar Questions:*
  * [Subsets](subsets.md)
## Problem:
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
## Solutions:
```python
class Solution :
public:
    vector> subsetsWithDup(vector& nums) :
        sort(nums.begin(), nums.end())
        vector path
        vector> ret
        helper(nums, 0, path, ret)
        return ret
    void helper(vector& nums, int pos, vector& path, vector>& ret) :
        if (pos == nums.size()) :
            ret.push_back(path)
            return
        path.push_back(nums[pos])
        helper(nums, pos + 1, path, ret)
        path.pop_back()
        while (pos + 1 < nums.size() && nums[pos + 1] == nums[pos]) ++pos
        helper(nums, pos + 1, path, ret)
```
# 78. Subsets
* *Difficulty: Medium*
* *Topics: Array, Backtracking, Bit Manipulation*
* *Similar Questions:*
  * [Subsets II](subsets-ii.md)
  * [Generalized Abbreviation](generalized-abbreviation.md)
  * [Letter Case Permutation](letter-case-permutation.md)
## Problem:
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
## Solutions:
```python
class Solution :
public:
    vector> subsets(vector& nums) :
        vector> ret
        vector path
        helper(nums, 0, path, ret)
        return ret
    void helper(vector& nums, int pos, vector& path, vector>& ret) :
        if (pos == nums.size()) :
            ret.push_back(path)
            return
        path.push_back(nums[pos])
        helper(nums, pos + 1, path, ret)
        path.pop_back()
        helper(nums, pos + 1, path, ret)
```
# 30. Substring with Concatenation of All Words
* *Difficulty: Hard*
* *Topics: Hash Table, Two Pointers, String*
* *Similar Questions:*
  * [Minimum Window Substring](minimum-window-substring.md)
## Problem:
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
Example 1:
Input:
  s = &quotbarfoothefoobarman&quot,
  words = [&quotfoo&quot,&quotbar&quot]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are &quotbarfoor&quot and &quotfoobar&quot respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:
Input:
  s = &quotwordgoodgoodgoodbestword&quot,
  words = [&quotword&quot,&quotgood&quot,&quotbest&quot,&quotword&quot]
Output: []
## Solutions:
```python
class Solution :
public:
    vector findSubstring(string s, vector& words) :
        int n = words.size()
        if (n == 0) return :
        int wordLen = words[0].length()
        int strLen = s.length()
        if (strLen < wordLen * n)   return :
        vector ret
        unordered_map> hashToIndex
        for (int i = 0 i < n ++i) :
            hashToIndex[hash(words[i])].push_back(i)
        vector RobinHash(strLen - wordLen + 1, 0)
        int runningHash = 0
        for (int i = 0 i < wordLen - 1 ++i) :
            runningHash = (runningHash * MAGIC + s[i] - 'a') % MOD
        int mostSignificantHash = 1
        for (int i = 0 i < wordLen - 1 ++i) :
            mostSignificantHash = (mostSignificantHash * MAGIC) % MOD
        for (int i = wordLen - 1 i < strLen ++i) :
            runningHash = (runningHash * MAGIC + s[i] - 'a') % MOD
            RobinHash[i - wordLen + 1] = runningHash
            runningHash = (MOD + runningHash - ((s[i - wordLen + 1] - 'a') * mostSignificantHash % MOD)) % MOD
        for (int i = 0 i < strLen - wordLen * n + 1 ++i) :
            unordered_map seen
            bool stop = false
            int count = 0
            for (int j = 0 j < n && !stop ++j) :
                int h = RobinHash[i + j * wordLen]
                if (hashToIndex.count(h) == 0) :
                    stop = true
                    break
                else :
                    ++seen[h]
                    if (seen[h] > hashToIndex[h].size()) :
                        stop = true
                        break
                    ++count // count is after if
            if (count == n) :
                ret.push_back(i)
        return ret
    int hash(string s) :
        int ret = 0
        for (auto c : s) :
            ret = (ret * MAGIC + c - 'a') % MOD
        return ret
private:
    int MAGIC = 31
    int MOD = INT_MAX/MAGIC
```
# 572. Subtree of Another Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Count Univalue Subtrees](count-univalue-subtrees.md)
  * [Most Frequent Subtree Sum](most-frequent-subtree-sum.md)
## Problem:
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isSubtree(TreeNode* s, TreeNode* t) :
        int tHash = hash(t)
        int sHash = 0
        return helper(s, t, tHash, sHash)
private:
    int MOD = 1e6 + 7
    int hash(TreeNode* root) :
        if (root == nullptr) return 0
        string str = to_string(hash(root->left)) + to_string(root->val) + to_string(hash(root->right))
        return intHash(str)
    int intHash(const string& str) :
        int hash = 0x31
        for (int i = 0 i < str.length() ++i) :
            hash = (hash * 37 + str[i]) % MOD
        return hash
    bool equal(TreeNode* s, TreeNode* t) :
        if (s == nullptr && t == nullptr)   return true
        if (s == nullptr)   return false
        if (t == nullptr)   return false
        if (s->val != t->val)   return false
        return equal(s->left, t->left) && equal(s->right, t->right)
    bool helper(TreeNode* s, TreeNode* t, int tHash, int& sHash) :
        if (s == nullptr) :
            sHash = 0
            return s == t
        int leftHash = 0
        int rightHash = 0
        bool leftResult = helper(s->left, t, tHash, leftHash)
        bool rightResult = helper(s->right, t, tHash, rightHash)
        if (leftResult || rightResult)  return true
        string str = to_string(leftHash) + to_string(s->val) + to_string(rightHash)
        sHash = intHash(str)
        return (sHash == tHash && equal(s, t))
```
# 37. Sudoku Solver
* *Difficulty: Hard*
* *Topics: Hash Table, Backtracking*
* *Similar Questions:*
  * [Valid Sudoku](valid-sudoku.md)
  * [Unique Paths III](unique-paths-iii.md)
## Problem:
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
	Each of the digits 1-9 must occur exactly once in each row.
	Each of the digits 1-9 must occur exactly once in each column.
	Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character &#39.&#39.
A sudoku puzzle...
...and its solution numbers marked in red.
Note:
	The given board contain only digits 1-9 and the character &#39.&#39.
	You may assume that the given Sudoku puzzle will have a single unique solution.
	The given board size is always 9x9.
## Solutions:
```python
class Solution :
public:
    void solveSudoku(vector>& board) :
        int n = 9
        vector> rows (n, vector (n, false))
        vector> cols (n, vector (n, false))
        vector>> blocks (3, vector>(3, vector (n, false)))
        for (int i = 0 i < n ++i) :
            for (int j = 0 j < n ++j) :
                if (board[i][j] == '.') continue
                rows[i][board[i][j] - '1'] = true
                cols[j][board[i][j] - '1'] = true
                blocks[i/3][j/3][board[i][j] - '1'] = true
        helper(board, n, 0, 0, rows, cols, blocks)
    bool helper(vector>& board, int n, int row, int col, vector>& rows, vector>& cols, vector>>& blocks) :
        for (int i = row i < n ++i) :
            for (int j = 0 j < n ++j) :
                if (board[i][j] != '.') continue
                for (int val = 1 val <= 9 ++val) :
                    if (isValid(rows, cols, blocks, i, j, val)) :
                        board[i][j] = '0' + val
                        rows[i][val-1] = true
                        cols[j][val-1] = true
                        blocks[i/3][j/3][val-1] = true
                        if (helper(board, n, i, j, rows, cols, blocks))    return true
                        blocks[i/3][j/3][val-1] = false
                        cols[j][val-1] = false
                        rows[i][val-1] = false
                        board[i][j] = '.'
                return false
        return true
    bool isValid(vector>& rows, vector>& cols, vector>>& blocks, int row, int col, int val) :
        return rows[row][val-1] == false && cols[col][val-1] == false && blocks[row/3][col/3][val-1] == false
```
# 404. Sum of Left Leaves
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Find the sum of all left leaves in a given binary tree.
Example:
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int sumOfLeftLeaves(TreeNode* root) :
        if (!root)  return 0
        int sum = 0
        if (root->left)
            helper(root->left, sum, true)
        if (root->right) 
            helper(root->right, sum, false)
        return sum
private:
    void helper(TreeNode* root, int& sum, bool left) :
        if (!root->left && !root->right && left) :
            sum += root->val
        if (root->left) :
            helper(root->left, sum, true)
        if (root->right) :
            helper(root->right, sum, false)
```
# 633. Sum of Square Numbers
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Valid Perfect Square](valid-perfect-square.md)
## Problem:
Given a non-negative integer c, your task is to decide whether there&#39re two integers a and b such that a2 + b2 = c.
Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
## Solutions:
```python
class Solution :
public:
    bool judgeSquareSum(int c) :
        long left = 0
        long right = sqrt(c) + 1
        while (left <= right) :
            long sum = left * left + right * right
            if (sum == c)   return true
            else if (sum > c) :
                --right
             else :
                ++left
        return false
```
# 371. Sum of Two Integers
* *Difficulty: Easy*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Add Two Numbers](add-two-numbers.md)
## Problem:
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Example 1:
Input: a = 1, b = 2
Output: 3
Example 2:
Input: a = -2, b = 3
Output: 1
## Solutions:
```python
class Solution :
public:
    int getSum(int a, int b) :
        int ret = a^b
        int carry = a&b
        while (carry != 0) :
            // to prevent runtime exception, &0x7fffffff This is not necessary for real program. Platforms other than leetcode do not complain. 
            carry = (carry & 0x7fffffff)<< 1 
            int newRet = ret^carry
            int newCarry = ret&carry
            ret = newRet
            carry = newCarry
        return ret
```
# 129. Sum Root to Leaf Numbers
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Path Sum](path-sum.md)
  * [Binary Tree Maximum Path Sum](binary-tree-maximum-path-sum.md)
  * [Smallest String Starting From Leaf](smallest-string-starting-from-leaf.md)
## Problem:
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1-&gt2-&gt3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.
Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1-&gt2 represents the number 12.
The root-to-leaf path 1-&gt3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4-&gt9-&gt5 represents the number 495.
The root-to-leaf path 4-&gt9-&gt1 represents the number 491.
The root-to-leaf path 4-&gt0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    int sumNumbers(TreeNode* root) :
        int ret = 0
        helper(root, 0, ret)
        return ret
    void helper(TreeNode* root, int path, int& ret) :
        if (root == nullptr) :
            return
        int val = 10 * path + root->val
        if (root->left == nullptr && root->right == nullptr) :
            ret += val
            return
        if (root->left) :
            helper(root->left, val, ret)
        if (root->right) :
            helper(root->right, val, ret)
```
# 228. Summary Ranges
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [Missing Ranges](missing-ranges.md)
  * [Data Stream as Disjoint Intervals](data-stream-as-disjoint-intervals.md)
## Problem:
Given a sorted integer array without duplicates, return the summary of its ranges.
Example 1:
Input:  [0,1,2,4,5,7]
Output: [&quot0-&gt2&quot,&quot4-&gt5&quot,&quot7&quot]
Explanation: 0,1,2 form a continuous range 4,5 form a continuous range.
Example 2:
Input:  [0,2,3,4,6,8,9]
Output: [&quot0&quot,&quot2-&gt4&quot,&quot6&quot,&quot8-&gt9&quot]
Explanation: 2,3,4 form a continuous range 8,9 form a continuous range.
## Solutions:
```python
class Solution :
public:
    vector summaryRanges(vector& nums) :
        auto ranges = helper(nums, 0, nums.size() - 1)
        vector ret
        for (auto& range : ranges) :
            ret.push_back(toString(range))
        return ret
    vector> helper(vector& nums, int left, int right) :
        if (left > right)   return :
        if (long(nums[right]) == long(nums[left]) + right - left) :
            return ::nums[left], nums[right]
        int mid = left + (right - left) / 2
        auto leftRange = helper(nums, left, mid)
        auto rightRange = helper(nums, mid + 1, right)
        if (!leftRange.empty() && !rightRange.empty()) :
            auto leftLast = leftRange.back()
            leftRange.pop_back()
            if (leftLast.second + 1 == rightRange[0].first) :
                rightRange[0].first = leftLast.first
             else :
                leftRange.push_back(leftLast)
        leftRange.insert(leftRange.end(), rightRange.begin(), rightRange.end())
        return leftRange
    inline string toString(pair range) :
        return range.first == range.second ? to_string(range.first) : to_string(range.first) + "->" + to_string(range.second)
```
# 372. Super Pow
* *Difficulty: Medium*
* *Topics: Math*
* *Similar Questions:*
  * [Pow(x, n)](powx-n.md)
## Problem:
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
Example 1:
Input: a = 2, b = [3]
Output: 8
Example 2:
Input: a = 2, b = [1,0]
Output: 1024
## Solutions:
```python
class Solution :
public:
    int superPow(int a, vector& b) :
        int ret = 1
        int base = a % MOD // a need to mod first!
        for (auto it = b.rbegin() it != b.rend() ++it) :
            int digit = *it
            ret = ret * pow(base, digit) % MOD
            base = pow(base, 10)
        return ret
private:
    int pow(int val, int n) :
        int ret = 1
        int power = val
        for (int i = 0 i < 4 ++i) :
            if ((n >> i) & 1) :
                ret = ret * power % MOD
            power = (power * power) % MOD
        return ret
    static const int MOD = 1337
```
# 313. Super Ugly Number
* *Difficulty: Medium*
* *Topics: Math, Heap*
* *Similar Questions:*
  * [Ugly Number II](ugly-number-ii.md)
## Problem:
Write a program to find the nth super ugly number.
Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
Example:
Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:
	1 is a super ugly number for any given primes.
	The given numbers in primes are in ascending order.
	0 &lt k &le 100, 0 &lt n &le 106, 0 &lt primes[i] &lt 1000.
	The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
## Solutions:
```python
class Solution :
public:
     struct UglyNumber:
        int val
        int prime
        int index
        UglyNumber(int val, int prime, int index) :
            this->val = val
            this->prime = prime
            this->index = index
        bool operator>(const UglyNumber& other) const :
            return val*prime > other.val*other.prime
    int nthSuperUglyNumber(int n, vector& primes) :
        vector dp(n, 0)
        dp[0] = 1
        priority_queue, greater> pq
        for (auto prime : primes) :
            pq.push(:1, prime, 0)
        for (int i = 1 i < n ++i) :
            do :
                UglyNumber ugly = pq.top() pq.pop()
                dp[i] = ugly.val * ugly.prime
                pq.push(:dp[ugly.index + 1], ugly.prime, ugly.index + 1)
             while (pq.top().val * pq.top().prime == dp[i]) // DO WHILE!
        return dp[n-1]
```
# 130. Surrounded Regions
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search, Union Find*
* *Similar Questions:*
  * [Number of Islands](number-of-islands.md)
  * [Walls and Gates](walls-and-gates.md)
## Problem:
Given a 2D board containing &#39X&#39 and &#39O&#39 (the letter O), capture all regions surrounded by &#39X&#39.
A region is captured by flipping all &#39O&#39s into &#39X&#39s in that surrounded region.
Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn&rsquot be on the border, which means that any &#39O&#39 on the border of the board are not flipped to &#39X&#39. Any &#39O&#39 that is not on the border and it is not connected to an &#39O&#39 on the border will be flipped to &#39X&#39. Two cells are connected if they are adjacent cells connected horizontally or vertically.
## Solutions:
```python
class Solution :
public:
    void solve(vector>& board) :
        int m = board.size()
        if (m == 0) return
        int n = board[0].size()
        if (n == 0) return
        vector> visited(m, vector (n, false))
        for (int i = 0 i < m ++i) :
            dfs(board, i, 0, visited)
            dfs(board, i, n - 1, visited)
        for (int j = 0 j < n ++j) :
            dfs(board, 0, j, visited)
            dfs(board, m - 1, j, visited)
        for (int i = 1 i < m - 1 ++i) :
            for (int j = 1 j < n - 1 ++j) :
                if (board[i][j] == 'O' && !visited[i][j]) :
                    board[i][j] = 'X'
    void dfs(vector>& board, int row, int col, vector>& visited) :
        int m = board.size()
        int n = board[0].size()
        if (row = m || col = n || board[row][col] == 'X' || visited[row][col])    return
        visited[row][col] = true
        dfs(board, row + 1, col, visited)
        dfs(board, row - 1, col, visited)
        dfs(board, row, col - 1, visited)
        dfs(board, row, col + 1, visited)
```
# 24. Swap Nodes in Pairs
* *Difficulty: Medium*
* *Topics: Linked List*
* *Similar Questions:*
  * [Reverse Nodes in k-Group](reverse-nodes-in-k-group.md)
## Problem:
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list&#39s nodes, only nodes itself may be changed.
Example:
Given 1-&gt2-&gt3-&gt4, you should return the list as 2-&gt1-&gt4-&gt3.
## Solutions:
```python
/**
 * Definition for singly-linked list.
 * struct ListNode :
 *     int val
 *     ListNode *next
 *     ListNode(int x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* swapPairs(ListNode* head) :
        ListNode* dummyHead = new ListNode(0)
        ListNode* tail = dummyHead
        while (head && head->next) :
            ListNode* first = head
            ListNode* second = head->next
            head = head->next->next // remember to the head of next round intermidiately
            tail->next = second
            second->next = first
            tail = first
            tail->next = nullptr
        if (head) :
            tail->next = head
        return dummyHead->next
```
# 627. Swap Salary
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a single update statement and no intermediate temp table.
Note that you must write a single update statement, DO NOT write any select statement for this problem.
Example:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
After running your update statement, the above salary table should have the following rows:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
## Solutions:
```python
# Write your MySQL query statement below
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END
```
# 101. Symmetric Tree
* *Difficulty: Easy*
* *Topics: Tree, Depth-first Search, Breadth-first Search*
* *Similar Questions:*
## Problem:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isSymmetric(TreeNode* root) :
        if (root == NULL)   return true
        return isSymmetricHelper(root->left, root->right)
    bool isSymmetricHelper(TreeNode* left, TreeNode* right) :
        if (left == NULL && right == NULL)  return true
        if (left == NULL || right == NULL)  return false
        if (left->val != right->val)    return false
        return isSymmetricHelper(left->left, right->right) && isSymmetricHelper(left->right, right->left)
```
# 621. Task Scheduler
* *Difficulty: Medium*
* *Topics: Array, Greedy, Queue*
* *Similar Questions:*
  * [Rearrange String k Distance Apart](rearrange-string-k-distance-apart.md)
  * [Reorganize String](reorganize-string.md)
## Problem:
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.
Example:
Input: tasks = [&quotA&quot,&quotA&quot,&quotA&quot,&quotB&quot,&quotB&quot,&quotB&quot], n = 2
Output: 8
Explanation: A -&gt B -&gt idle -&gt A -&gt B -&gt idle -&gt A -&gt B.
Note:
	The number of tasks is in the range [1, 10000].
	The integer n is in the range [0, 100].
## Solutions:
```python
class Solution :
public:
    int leastInterval(vector& tasks, int n) :
        unordered_map taskCount
        for (auto& task : tasks) :
            ++taskCount[task]
        int maxVal = 0
        int maxCount = 0
        for (auto& entry : taskCount) :
            if (entry.second > maxVal) :
                maxVal = entry.second
                maxCount = 1
             else if (entry.second == maxVal) :
                ++maxCount
        return max(int(tasks.size()), (n + 1) * (maxVal - 1) + maxCount) // for max, we can't mix types.
```
# 195. Tenth Line
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Given a text file file.txt, print just the 10th line of the file.
Example:
Assume that file.txt has the following content:
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:
Line 10
Note:
1. If the file contains less than 10 lines, what should you output?
2. There&#39s at least three different solutions. Try to explore all possibilities.
## Solutions:
```python
# Read from the file file.txt and output the tenth line to stdout.
tail -n +10 file.txt | head -n 1
```
# 439. Ternary Expression Parser
* *Difficulty: Medium*
* *Topics: Stack, Depth-first Search*
* *Similar Questions:*
  * [Mini Parser](mini-parser.md)
  * [Remove Comments](remove-comments.md)
  * [Parse Lisp Expression](parse-lisp-expression.md)
## Problem:
Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).
Note:
The length of the given string is &le 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.
Example 1:
Input: "T?2:3"
Output: "2"
Explanation: If true, then result is 2 otherwise result is 3.
Example 2:
Input: "F?1:T?4:5"
Output: "4"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
Example 3:
Input: "T?T?F:5:3"
Output: "F"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"
## Solutions:
```python
class Solution :
public:
    string parseTernary(string expression) :
        if (expression.length() == 0)   return ""
        int pos = 0
        return helper(expression, pos)
    string helper(string& expression, int& pos) :
        char c = expression[pos]
        if ((c == 'T' || c == 'F') && (pos + 1 < expression.length()) && (expression[pos + 1] == '?')) :
            ++pos // remove 'T' or 'F'
            ++pos // remove '?'
            string left = helper(expression, pos)
            ++pos // remove ':'
            string right = helper(expression, pos)
            return c == 'T' ? left : right
        ++pos // remove base case 
        return string(1, c)
```
# 68. Text Justification
* *Difficulty: Hard*
* *Topics: String*
* *Similar Questions:*
## Problem:
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach that is, pack as many words as you can in each line. Pad extra spaces &#39 &#39 when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
Note:
	A word is defined as a character sequence consisting of non-space characters only.
	Each word&#39s length is guaranteed to be greater than 0 and not exceed maxWidth.
	The input array words contains at least one word.
Example 1:
Input:
words = [&quotThis&quot, &quotis&quot, &quotan&quot, &quotexample&quot, &quotof&quot, &quottext&quot, &quotjustification.&quot]
maxWidth = 16
Output:
[
   &quotThis    is    an&quot,
   &quotexample  of text&quot,
   &quotjustification.  &quot
]
Example 2:
Input:
words = [&quotWhat&quot,&quotmust&quot,&quotbe&quot,&quotacknowledgment&quot,&quotshall&quot,&quotbe&quot]
maxWidth = 16
Output:
[
  &quotWhat   must   be&quot,
  &quotacknowledgment  &quot,
  &quotshall be        &quot
]
Explanation: Note that the last line is &quotshall be    &quot instead of &quotshall     be&quot,
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:
Input:
words = [&quotScience&quot,&quotis&quot,&quotwhat&quot,&quotwe&quot,&quotunderstand&quot,&quotwell&quot,&quotenough&quot,&quotto&quot,&quotexplain&quot,
         &quotto&quot,&quota&quot,&quotcomputer.&quot,&quotArt&quot,&quotis&quot,&quoteverything&quot,&quotelse&quot,&quotwe&quot,&quotdo&quot]
maxWidth = 20
Output:
[
  &quotScience  is  what we&quot,
  &quotunderstand      well&quot,
  &quotenough to explain to&quot,
  &quota  computer.  Art is&quot,
  &quoteverything  else  we&quot,
  &quotdo                  &quot
]
## Solutions:
```python
class Solution :
public:
    vector fullJustify(vector& words, int maxWidth) :
        vector ret
        int count = 0
        int n = words.size()
        vector buffer
        for (int i = 0 i < n) :
            if (count == 0) :
                buffer.push_back(words[i])
                count = words[i].length()
                ++i
             else :
                if (count + 1 + words[i].length() > maxWidth) :
                    ret.push_back(lineProcess(buffer, maxWidth))
                    count = 0
                    buffer.clear()
                 else :
                    buffer.push_back(words[i])
                    count += 1 + words[i].length()
                    ++i
        if (buffer.size() != 0) :
            ret.push_back(lastLineProcess(buffer, maxWidth))
        return ret
    string lineProcess(vector& buffer, int maxWidth) :
        if (buffer.size() == 1) return lastLineProcess(buffer, maxWidth)
        int count = 0
        for (auto& word : buffer) :
            count += word.length()
        int quotient = (maxWidth - count) / (buffer.size() - 1)
        int modulo = (maxWidth - count) % (buffer.size() - 1)
        string ret
        ret.append(buffer[0])
        for (int i = 1 i < buffer.size() ++i) :
            int distance = quotient + (modulo-- > 0 ? 1 : 0)
            ret.append(distance, ' ')
            ret.append(buffer[i])
        return ret
    string lastLineProcess(vector& buffer, int maxWidth) :
        string ret = buffer[0]
        for (int i = 1 i < buffer.size() ++i) :
            ret.push_back(' ')
            ret.append(buffer[i])
        if (ret.length() < maxWidth) :
            ret.append(maxWidth - ret.length(), ' ')
        return ret
```
# 505. The Maze II
* *Difficulty: Medium*
* *Topics: Depth-first Search, Breadth-first Search*
* *Similar Questions:*
  * [The Maze](the-maze.md)
  * [The Maze III](the-maze-iii.md)
## Problem:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won&#39t stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the ball&#39s start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
Example 1:
Input 1: a maze represented by a 2D array
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)
Output: 12
Explanation: One shortest way is : left -&gt down -&gt left -&gt down -&gt right -&gt down -&gt right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
Example 2:
Input 1: a maze represented by a 2D array
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)
Output: -1
Explanation: There is no way for the ball to stop at the destination.
Note:
	There is only one ball and one destination in the maze.
	Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
	The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
	The maze contains at least 2 empty spaces, and both the width and height of the maze won&#39t exceed 100.
## Solutions:
```python
class Solution :
public:
    int shortestDistance(vector>& maze, vector& start, vector& destination) :
        int m = maze.size()
        if (m == 0) return 0
        int n = maze[0].size()
        if (n == 0) return 0
        vector> dists(m, vector(n, INT_MAX)) // dist is important
        priority_queue>, vector>>, greater>>> q
        if (start == destination)   return 0
        q.push(:0, start)
        dists[start[0]][start[1]] = 0
        maze[start[0]][start[1]] = -1
        while (!q.empty()) :
            auto coord = q.top() q.pop()
            for (int d = 0 d < 4 ++d) :
                int x = coord.second[0], y = coord.second[1], dist = dists[x][y]
                auto newCoord = reachEnd(maze, m, n, coord.second[0], coord.second[1], directions[d][0], directions[d][1], dist)
                if (dists[newCoord[0]][newCoord[1]] > dist) :
                    dists[newCoord[0]][newCoord[1]] = dist
                    if (newCoord[0] != destination[0] || newCoord[1] != destination[1]) q.push(:dist, :newCoord[0], newCoord[1])
        int res = dists[destination[0]][destination[1]]
        return (res == INT_MAX) ? -1 : res
private:
    vector reachEnd(vector>& maze, int m, int n, int x, int y, int deltaX, int deltaY, int& dist) :
        do :
            x += deltaX
            y += deltaY
            ++dist
         while (x >= 0 && x = 0 && y < n && maze[x][y] != 1)
        --dist
        return :x - deltaX, y - deltaY
    int directions[4][2] :
        :1, 0,
        :-1, 0,
        :0, 1,
        :0, -1
```
# 218. The Skyline Problem
* *Difficulty: Hard*
* *Topics: Divide and Conquer, Heap, Binary Indexed Tree, Segment Tree, Line Sweep*
* *Similar Questions:*
  * [Falling Squares](falling-squares.md)
## Problem:
A city&#39s skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 &le Li, Ri &le INT_MAX, 0 &lt Hi &le INT_MAX, and Ri - Li &gt 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
The output is a list of &quotkey points&quot (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.
For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
Notes:
	The number of buildings in any input list is guaranteed to be in the range [0, 10000].
	The input list is already sorted in ascending order by the left x position Li.
	The output list must be sorted by the x position.
	There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
## Solutions:
```python
class Solution :
public:
    struct Event:
        int x
        int y
        bool up
        Event(int x, int y, bool up) :
            this->x = x
            this->y = y
            this->up = up
        bool operator<(const Event& event) const : // this is the most important part.
            if (x != event.x) :
                return x < event.x
            if (up != event.up) :
                return up
             else :
                if (up) :
                    return y > event.y
                 else :
                    return y < event.y
    vector> getSkyline(vector>& buildings) :
        vector events
        for (auto& building : buildings) :
            events.push_back(:building[0], building[2], true)
            events.push_back(:building[1], building[2], false)
        sort(events.begin(), events.end())
        multiset> heap
        heap.insert(0)
        vector> ret
        for (auto& event : events) :
            if (event.up) :
                if (event.y > (*heap.begin())) :
                    ret.push_back(:event.x, event.y)
                heap.insert(event.y)
             else :
                int currentHeight = *heap.begin()
                auto it = heap.find(event.y)
                heap.erase(it)
                if (currentHeight > *heap.begin()) :
                    ret.push_back(:event.x, *heap.begin())
        return ret
```
# 414. Third Maximum Number
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Kth Largest Element in an Array](kth-largest-element-in-an-array.md)
## Problem:
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
## Solutions:
```python
class Solution :
public:
    int thirdMax(vector& nums) :
        int count = 0
        int first = INT_MIN
        int second = INT_MIN
        int third = INT_MIN
        for (auto& num : nums) :
            if ((count >= 1 && num == first) || (count >= 2 && num == second) || (count >= 3 && num == third))  continue
            ++count
            if (num >= first) :
                third = second
                second = first
                first = num
             else if (num >= second) :
                third = second
                second = num
             else if (num >= third) :
                third = num
        return count >= 3 ? third : first
```
# 1023. Time Based Key-Value Store
* *Difficulty: Medium*
* *Topics: Hash Table, Binary Search*
* *Similar Questions:*
## Problem:
Create a timebased key-value store class TimeMap, that supports two operations.
1. set(string key, string value, int timestamp)
	Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)
	Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev &lt= timestamp.
	If there are multiple such values, it returns the one with the largest timestamp_prev.
	If there are no values, it returns the empty string (&quot&quot).
Example 1:
Input: inputs = [&quotTimeMap&quot,&quotset&quot,&quotget&quot,&quotget&quot,&quotset&quot,&quotget&quot,&quotget&quot], inputs = [[],[&quotfoo&quot,&quotbar&quot,1],[&quotfoo&quot,1],[&quotfoo&quot,3],[&quotfoo&quot,&quotbar2&quot,4],[&quotfoo&quot,4],[&quotfoo&quot,5]]
Output: [null,null,&quotbar&quot,&quotbar&quot,null,&quotbar2&quot,&quotbar2&quot]
Explanation:   
TimeMap kv   
kv.set(&quotfoo&quot, &quotbar&quot, 1) // store the key &quotfoo&quot and value &quotbar&quot along with timestamp = 1   
kv.get(&quotfoo&quot, 1)  // output &quotbar&quot   
kv.get(&quotfoo&quot, 3) // output &quotbar&quot since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie &quotbar&quot   
kv.set(&quotfoo&quot, &quotbar2&quot, 4)   
kv.get(&quotfoo&quot, 4) // output &quotbar2&quot   
kv.get(&quotfoo&quot, 5) //output &quotbar2&quot   
Example 2:
Input: inputs = [&quotTimeMap&quot,&quotset&quot,&quotset&quot,&quotget&quot,&quotget&quot,&quotget&quot,&quotget&quot,&quotget&quot], inputs = [[],[&quotlove&quot,&quothigh&quot,10],[&quotlove&quot,&quotlow&quot,20],[&quotlove&quot,5],[&quotlove&quot,10],[&quotlove&quot,15],[&quotlove&quot,20],[&quotlove&quot,25]]
Output: [null,null,null,&quot&quot,&quothigh&quot,&quothigh&quot,&quotlow&quot,&quotlow&quot]
Note:
	All key/value strings are lowercase.
	All key/value strings have length in the range [1, 100]
	The timestamps for all TimeMap.set operations are strictly increasing.
	1 &lt= timestamp &lt= 10^7
	TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
## Solutions:
```python
class TimeMap :
public:
    /** Initialize your data structure here. */
    TimeMap() :
    void set(string key, string value, int timestamp) :
        keyToValues[key].push_back(:timestamp, value)
    string get(string key, int timestamp) :
        if (keyToValues.count(key) == 0)    return ""
        string dummy
        auto upperBound = upper_bound(keyToValues[key].begin(), keyToValues[key].end(), make_pair(timestamp + 1, dummy)) // pay attention to +1
        if (upperBound == keyToValues[key].begin())   return ""
        return prev(upperBound)->second
private:
    unordered_map>> keyToValues
/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap()
 * obj->set(key,value,timestamp)
 * string param_2 = obj->get(key,timestamp)
 */
```
# 742. To Lower Case
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
Example 1:
Input: &quotHello&quot
Output: &quothello&quot
Example 2:
Input: &quothere&quot
Output: &quothere&quot
Example 3:
Input: &quotLOVELY&quot
Output: &quotlovely&quot
## Solutions:
```python
class Solution :
public:
    string toLowerCase(string str) :
        for (int i = 0 i < str.length() ++i) :
            if (isUpperCase(str[i])) :
                str[i] += 'a' - 'A'
        return str
private:
    inline bool isUpperCase(char c) :
        return c >= 'A' && c <= 'Z' 
```
# 777. Toeplitz Matrix
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Valid Word Square](valid-word-square.md)
## Problem:
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
Example 1:
Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
&quot[9]&quot, &quot[5, 5]&quot, &quot[1, 1, 1]&quot, &quot[2, 2, 2]&quot, &quot[3, 3]&quot, &quot[4]&quot.
In each diagonal all elements are the same, so the answer is True.
Example 2:
Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal &quot[1, 2]&quot has different elements.
Note:
	matrix will be a 2D array of integers.
	matrix will have a number of rows and columns in range [1, 20].
	matrix[i][j] will be integers in range [0, 99].
Follow up:
	What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
	What if the matrix is so large that you can only load up a partial row into the memory at once?
## Solutions:
```python
class Solution :
public:
    bool isToeplitzMatrix(vector>& matrix) :
        int m = matrix.size()
        if (m == 0) return true
        int n = matrix[0].size()
        if (n == 0) return true
        for (int i = 1 i < m ++i) :
            for (int j = 0 j < n - 1 ++j) :
                if (matrix[i-1][j] != matrix[i][j+1])   return false
        return true
```
# 347. Top K Frequent Elements
* *Difficulty: Medium*
* *Topics: Hash Table, Heap*
* *Similar Questions:*
  * [Word Frequency](word-frequency.md)
  * [Kth Largest Element in an Array](kth-largest-element-in-an-array.md)
  * [Sort Characters By Frequency](sort-characters-by-frequency.md)
  * [Split Array into Consecutive Subsequences](split-array-into-consecutive-subsequences.md)
  * [Top K Frequent Words](top-k-frequent-words.md)
  * [K Closest Points to Origin](k-closest-points-to-origin.md)
## Problem:
Given a non-empty array of integers, return the k most frequent elements.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
Note: 
	You may assume k is always valid, 1 &le k &le number of unique elements.
	Your algorithm&#39s time complexity must be better than O(n log n), where n is the array&#39s size.
## Solutions:
```python
class Solution :
public:
    vector topKFrequent(vector& nums, int k) :
        for (auto num : nums) :
            ++counts[num]
        set> topKIndex
        for (auto it = counts.begin() it != counts.end() ++it) :
            topKIndex.insert(:it->second, it->first)
            if (topKIndex.size() > k) :
                topKIndex.erase(topKIndex.begin())
        vector ret
        for (auto it = topKIndex.rbegin() it != topKIndex.rend() ++it) :
            ret.push_back(it->second)
        return ret
private:
    unordered_map counts
```
# 477. Total Hamming Distance
* *Difficulty: Medium*
* *Topics: Bit Manipulation*
* *Similar Questions:*
  * [Hamming Distance](hamming-distance.md)
## Problem:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.
Example:
Input: 4, 14, 2
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0  to 10^9
Length of the array will not exceed 10^4. 
## Solutions:
```python
class Solution :
public:
    int totalHammingDistance(vector& nums) :
        int oneCount[32] = :0
        for (auto num : nums) :
            for (int i = 0 i < 32 ++i) :
                if ((num & (0x1 << i)) != 0) :
                    ++oneCount[i]
        int ret = 0
        int n = nums.size()
        for (int i = 0 i < 32 ++i) :
            ret += oneCount[i] * (n - oneCount[i])
        return ret
```
# 42. Trapping Rain Water
* *Difficulty: Hard*
* *Topics: Array, Two Pointers, Stack*
* *Similar Questions:*
  * [Container With Most Water](container-with-most-water.md)
  * [Product of Array Except Self](product-of-array-except-self.md)
  * [Trapping Rain Water II](trapping-rain-water-ii.md)
  * [Pour Water](pour-water.md)
## Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
## Solutions:
```python
class Solution :
public:
    int trap(vector& height) :
        int ret = 0
        int leftHeight = 0
        int rightHeight = 0
        int left = 0
        int right = height.size() - 1
        while (left <= right) :
            if (height[left] <= height[right]) :
                if (leftHeight - height[left] > 0)  ret += leftHeight - height[left]
                leftHeight = max(leftHeight, height[left])
                ++left
             else :
                if (rightHeight - height[right] > 0) :
                    if (rightHeight - height[right] > 0)    ret += rightHeight - height[right]
                rightHeight = max(rightHeight, height[right])
                --right
        return ret
```
### Another solution with two pointers
```python
class Solution :
public:
    int trap(vector& height) :
        int n = height.size()
        if (n == 0) return 0
        int water = 0
        priority_queue, vector>, greater>> pq
        int left = 0
        int right = n - 1
        int boundary = min(height[0], height[n-1])
        pq.push(:height[0], 0)
        pq.push(:height[n-1], n-1)
        while (left <= right) :
            int bar
            if (height[left] <= height[right]) :
                bar = height[left]
                ++left
             else :
                bar = height[right]
                --right
            if (bar < boundary) :
                water += boundary - bar
             else :
                boundary = bar
        return water
```
# 120. Triangle
* *Difficulty: Medium*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
## Solutions:
```python
class Solution :
public:
    int minimumTotal(vector>& triangle) :
        if (triangle.size() == 0)   return 0
        int level = triangle.size()
        vector dp (level, INT_MAX)
        dp[0] = 0
        for (auto& values : triangle) :
            for (int i = values.size() - 1 i >= 1 --i) :
                dp[i] = values[i] + min(dp[i-1], dp[i])
            dp[0] = values[0] + dp[0]
        int ret = INT_MAX
        for (auto bottom : dp) :
            ret = min(ret, bottom)
        return ret
```
# 669. Trim a Binary Search Tree
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
## Problem:
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
Example 1:
Input: 
    1
   / \
  0   2
  L = 1
  R = 2
Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1
  L = 1
  R = 3
Output: 
      3
     / 
   2   
  /
 1
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* trimBST(TreeNode* root, int L, int R) :
        if (root == nullptr)    return nullptr
        if (root->val < L) :
            return trimBST(root->right, L, R)
        if (root->val > R) :
            return trimBST(root->left, L, R)
        root->left = trimBST(root->left, L,R)
        root->right = trimBST(root->right, L, R)
        return root
```
# 1150. Two Sum BSTs
* *Difficulty: Medium*
* *Topics: Binary Search Tree*
* *Similar Questions:*
  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)
## Problem:
Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
Constraints:
	Each tree has at most 5000 nodes.
	-10^9 &lt= target, node.val &lt= 10^9
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) :
        unordered_set visited
        dfs(root1, target, visited, true)
        return dfs(root2, target, visited, false)
private:
    bool dfs(TreeNode* root, int target, unordered_set& visited, bool populate) :
        if (root == nullptr)    return false
        if (populate) :
            visited.insert(root->val)
         else :
            if (visited.count(target - root->val))  return true
        return dfs(root->left, target, visited, populate) || dfs(root->right, target, visited, populate)
```
# 167. Two Sum II - Input array is sorted
* *Difficulty: Easy*
* *Topics: Array, Two Pointers, Binary Search*
* *Similar Questions:*
  * [Two Sum](two-sum.md)
  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)
  * [Two Sum Less Than K](two-sum-less-than-k.md)
## Problem:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Note:
	Your returned answers (both index1 and index2) are not zero-based.
	You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
## Solutions:
```python
class Solution :
public:
    vector twoSum(vector& numbers, int target) :
        int left = 0
        int right = numbers.size() - 1
        while (left < right) :
            if (numbers[left] + numbers[right] == target)   return :left + 1, right + 1
            else if (numbers[left] + numbers[right] < target) :
                ++left
             else :
                --right
        return :0, 0
```
# 170. Two Sum III - Data structure design
* *Difficulty: Easy*
* *Topics: Hash Table, Design*
* *Similar Questions:*
  * [Two Sum](two-sum.md)
  * [Unique Word Abbreviation](unique-word-abbreviation.md)
  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)
## Problem:
Design and implement a TwoSum class. It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
Example 1:
add(1) add(3) add(5)
find(4) -&gt true
find(7) -&gt false
Example 2:
add(3) add(1) add(2)
find(3) -&gt true
find(6) -&gt false
## Solutions:
```python
class TwoSum :
public:
    /** Initialize your data structure here. */
    TwoSum() :
    /** Add the number to an internal data structure.. */
    void add(int number) :
        ++count[number]
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) :
        for (auto valueCount : count) :
            int target = value - valueCount.first
            auto it = count.find(target)
            if (it != count.end() && (target != valueCount.first || it->second > 1)) return true
        return false
private:
    unordered_map count    
/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum()
 * obj->add(number)
 * bool param_2 = obj->find(value)
 */
```
# 653. Two Sum IV - Input is a BST
* *Difficulty: Easy*
* *Topics: Tree*
* *Similar Questions:*
  * [Two Sum](two-sum.md)
  * [Two Sum II - Input array is sorted](two-sum-ii-input-array-is-sorted.md)
  * [Two Sum III - Data structure design](two-sum-iii-data-structure-design.md)
## Problem:
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
Output: False
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool findTarget(TreeNode* root, int k) :
        unordered_set seen
        return helper(root, k, seen)
private:
    bool helper(TreeNode* root, int k, unordered_set& seen) :
        if (root == nullptr)    return false
        if (seen.count(k - root->val) > 0)  return true
        seen.insert(root->val)
        return helper(root->left, k, seen) || helper(root->right, k, seen)
```
# 1083. Two Sum Less Than K
* *Difficulty: Easy*
* *Topics: Array*
* *Similar Questions:*
  * [Two Sum](two-sum.md)
  * [Two Sum II - Input array is sorted](two-sum-ii-input-array-is-sorted.md)
  * [3Sum Smaller](3sum-smaller.md)
  * [Subarray Product Less Than K](subarray-product-less-than-k.md)
## Problem:
Given an array A of integers and integer K, return the maximum S such that there exists i &lt j with A[i] + A[j] = S and S &lt K. If no i, j exist satisfying this equation, return -1.
Example 1:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:
Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it&#39s not possible to get a pair sum less that 15.
Note:
	1 &lt= A.length &lt= 100
	1 &lt= A[i] &lt= 1000
	1 &lt= K &lt= 2000
## Solutions:
```python
class Solution :
public:
    int twoSumLessThanK(vector& A, int K) :
        if (A.size() < 2)   return -1
        int ret = INT_MIN
        int left = 0
        int right = A.size() - 1
        sort(A.begin(), A.end())
        while (left < right) :
            if (A[left] + A[right] >= K) :
                --right
             else :
                ret = max(ret, A[left] + A[right])
                ++left
        return ret == INT_MIN ? -1 : ret
```
It is possible to use count sort to reduce the space complexity from `O(nlogn)` to `O(n)`. 
[bucket sort strict O(n) solution](https://leetcode.com/problems/two-sum-less-than-k/discuss/328270/bucket-sort-strict-O(n)-solution)
```python
class Solution :
    class Node :
        int v
        int f
        public Node(int v, int f) :
            this.v =v
            this.f = f
        public String toString():return v +"-" + f
    public int twoSumLessThanK(int[] A, int k) :
        if(A == null || A.length < 1) return -1
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE
        for(int a : A) :
            min = Math.min(min, a)
            max = Math.max(max, a)
        Node[] buckets = new Node[max+1]
        for(int a : A) :
            if(buckets[a] == null) buckets[a] = new Node(a, 0)
            buckets[a].f ++
        Node cur = null
        for(int i = 0 i<= max i++) :
            if( buckets[i] != null && buckets[i].v == i) :
                cur = buckets[i]
            buckets[i] = cur
        int sum = -1
        for(int a : A) :
            int target = k - a - 1
            if(target < min) continue
            if(target > max) target = max
            if(a == buckets[target].v && buckets[target].f == 1) continue
            sum = Math.max(sum, buckets[target].v + a)
        return sum
```
# 1. Two Sum
* *Difficulty: Easy*
* *Topics: Array, Hash Table*
* *Similar Questions:*
  * [3Sum](3sum.md)
  * [4Sum](4sum.md)
  * [Two Sum II - Input array is sorted](two-sum-ii-input-array-is-sorted.md)
  * [Two Sum III - Data structure design](two-sum-iii-data-structure-design.md)
  * [Subarray Sum Equals K](subarray-sum-equals-k.md)
  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)
  * [Two Sum Less Than K](two-sum-less-than-k.md)
## Problem:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
## Solutions:
```python
class Solution :
public:
    vector twoSum(vector& nums, int target) :
        unordered_map numToIndex
        for (int i = 0 i < nums.size() ++i) :
            if (numToIndex.count(target - nums[i]) > 0) :
                return :numToIndex[target - nums[i]], i
            numToIndex[nums[i]] = i
        return :
```
# 264. Ugly Number II
* *Difficulty: Medium*
* *Topics: Math, Dynamic Programming, Heap*
* *Similar Questions:*
  * [Merge k Sorted Lists](merge-k-sorted-lists.md)
  * [Count Primes](count-primes.md)
  * [Ugly Number](ugly-number.md)
  * [Perfect Squares](perfect-squares.md)
  * [Super Ugly Number](super-ugly-number.md)
## Problem:
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  
	1 is typically treated as an ugly number.
	n does not exceed 1690.
## Solutions:
```python
class Solution :
public:
    struct UglyNumber:
        int val
        int prime
        int index
        UglyNumber(int val, int prime, int index) :
            this->val = val
            this->prime = prime
            this->index = index
        bool operator>(const UglyNumber& other) const :
            return val*prime > other.val*other.prime
    int nthUglyNumber(int n) :
        vector primes :2, 3, 5 
        vector dp(n, 0)
        dp[0] = 1
        priority_queue, greater> pq
        for (auto prime : primes) :
            pq.push(:1, prime, 0)
        for (int i = 1 i < n ++i) :
            do :
                UglyNumber ugly = pq.top() pq.pop()
                dp[i] = ugly.val * ugly.prime
                pq.push(:dp[ugly.index + 1], ugly.prime, ugly.index + 1)
             while (pq.top().val * pq.top().prime == dp[i])
        return dp[n-1]
```
# 1307. Ugly Number III
* *Difficulty: Medium*
* *Topics: Math, Binary Search*
* *Similar Questions:*
  * [Ugly Number II](ugly-number-ii.md)
## Problem:
Write a program to find the n-th ugly number.
Ugly numbers are positive integers which are divisible by a or b or c.
Example 1:
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:
Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:
Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:
Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
Constraints:
	1 &lt= n, a, b, c &lt= 10^9
	1 &lt= a * b * c &lt= 10^18
	It&#39s guaranteed that the result will be in range [1, 2 * 10^9]
## Solutions:
```python
class Solution :
public:
    int nthUglyNumber(int n, int A, int B, int C) :
        int left = 1
        int right = INT_MAX
        long a = A
        long b = B
        long c = C
        long d = gcm(a, b)
        long e = gcm(a, c)
        e = min(e, long(INT_MAX) )
        long f = gcm(b, c)
        f = min(f, long(INT_MAX) )
        long g = gcm(e, f)
        g = min(g, long(INT_MAX) )
        while (left < right) :
            int mid = left + (right - left) / 2
            if (countUglyNumber(mid, a, b, c, d, e, f, g) >= n) :
                right = mid
             else :
                left = mid + 1
        return left
private:
    int countUglyNumber(long num, long a, long b, long c, long d, long e, long f, long g) :
        return  num / a + num / b + num / c - num / d - num / e - num / f + num / g
    int gcd(int x, int y) :
        if (y > x) :
            return gcd(y, x)
        if (y == 0) return x
        return gcd(y, x % y)
    long gcm(long x, long y) :
        return (x * y) / gcd(x, y)
```
# 263. Ugly Number
* *Difficulty: Easy*
* *Topics: Math*
* *Similar Questions:*
  * [Happy Number](happy-number.md)
  * [Count Primes](count-primes.md)
  * [Ugly Number II](ugly-number-ii.md)
## Problem:
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
Example 1:
Input: 6
Output: true
Explanation: 6 = 2 &times 3
Example 2:
Input: 8
Output: true
Explanation: 8 = 2 &times 2 &times 2
Example 3:
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:
	1 is typically treated as an ugly number.
	Input is within the 32-bit signed integer range: [&minus231,  231 &minus 1].
## Solutions:
```python
class Solution :
public:
    bool isUgly(int num) :
        if (num <= 0)   return false
        while (num % 2 == 0)    num /= 2
        while (num % 3 == 0)    num /= 3
        while (num % 5 == 0)    num /= 5
        return num == 1
```
# 95. Unique Binary Search Trees II
* *Difficulty: Medium*
* *Topics: Dynamic Programming, Tree*
* *Similar Questions:*
  * [Unique Binary Search Trees](unique-binary-search-trees.md)
  * [Different Ways to Add Parentheses](different-ways-to-add-parentheses.md)
## Problem:
Given an integer n, generate all structurally unique BST&#39s (binary search trees) that store values 1 ... n.
Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST&#39s shown below:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector generateTrees(int n) :
        if (n <= 0) return :
        map, vector> cache
        return helper(1, n, cache)
    vector helper(int left, int right, map, vector>& cache) :
        if (left > right)   return :nullptr
        if (left == right)  return :new TreeNode(left)
        auto range = make_pair(left, right)
        if (cache.count(range) > 0) return cache[range]
        vector ret
        for (int rootVal = left rootVal <= right ++rootVal) :
            vector leftRoots = helper(left, rootVal - 1, cache)
            vector rightRoots = helper(rootVal + 1, right, cache)
            for (auto leftRoot : leftRoots) :
                for (auto rightRoot : rightRoots) :
                    TreeNode* root = new TreeNode(rootVal)
                    root->left = leftRoot
                    root->right = rightRoot
                    ret.push_back(root)
        cache[range] = ret
        return ret
```
# 96. Unique Binary Search Trees
* *Difficulty: Medium*
* *Topics: Dynamic Programming, Tree*
* *Similar Questions:*
  * [Unique Binary Search Trees II](unique-binary-search-trees-ii.md)
## Problem:
Given n, how many structurally unique BST&#39s (binary search trees) that store values 1 ... n?
Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST&#39s:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
## Solutions:
```python
class Solution :
public:
    int numTrees(int n) :
        map, int> cache
        return helper(1, n, cache)
    int helper(int left, int right, map, int>& cache) :
        if (left > right)   return 1 // return 1!
        if (left == right)  return 1
        auto range = make_pair(left, right)
        if (cache.count(range) != 0)    return cache[range]
        int count = 0
        for (int num = left num <= right ++num) :
            count += helper(left, num - 1, cache) * helper(num + 1, right, cache)
        cache[range] = count
        return count
```
# 965. Unique Email Addresses
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
## Problem:
Every email consists of a local name and a domain name, separated by the @ sign.
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
Besides lowercase letters, these emails may contain &#39.&#39s or &#39+&#39s.
If you add periods (&#39.&#39) between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, &quotalice.z@leetcode.com&quot and &quotalicez@leetcode.com&quot forward to the same email address.  (Note that this rule does not apply for domain names.)
If you add a plus (&#39+&#39) in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
Example 1:
Input: [&quottest.email+alex@leetcode.com&quot,&quottest.e.mail+bob.cathy@leetcode.com&quot,&quottestemail+david@lee.tcode.com&quot]
Output: 2
Explanation: &quottestemail@leetcode.com&quot and &quottestemail@lee.tcode.com&quot actually receive mails
Note:
	1 &lt= emails[i].length &lt= 100
	1 &lt= emails.length &lt= 100
	Each emails[i] contains exactly one &#39@&#39 character.
	All local and domain names are non-empty.
	Local names do not start with a &#39+&#39 character.
## Solutions:
```python
class Solution :
public:
    int numUniqueEmails(vector& emails) :
        unordered_set uniqueEmails
        for (auto& email : emails) :
            uniqueEmails.insert(getCanonicalEmail(email))
        return uniqueEmails.size()
private:
    string getCanonicalEmail(const string& email) :
        int pos = 0
        string ret
        bool ignore = false
        while (pos < email.length()) :
            if (email[pos] == '@') :
                ret.append(email.substr(pos))
                return ret
            if (ignore) :
                ++pos
                continue
            if (email[pos] == '+') :
                ignore = true
                ++pos
                continue
            if (email[pos] == '.') :
                ++pos
             else :
                ret.push_back(email[pos])
                ++pos
        return ret
```
# 1319. Unique Number of Occurrences
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
Input: arr = [1,2]
Output: false
Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
Constraints:
	1 &lt= arr.length &lt= 1000
	-1000 &lt= arr[i] &lt= 1000
## Solutions:
```python
class Solution :
public:
    bool uniqueOccurrences(vector& arr) :
        unordered_map freq
        for (auto& num : arr) :
            ++freq[num]
        unordered_set seen
        for (auto& entry : freq) :
            if (seen.count(entry.second))   return false
            seen.insert(entry.second)
        return true
```
# 63. Unique Paths II
* *Difficulty: Medium*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
  * [Unique Paths](unique-paths.md)
  * [Unique Paths III](unique-paths-iii.md)
## Problem:
A robot is located at the top-left corner of a m x n grid (marked &#39Start&#39 in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39Finish&#39 in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note: m and n will be at most 100.
Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt Right -&gt Down -&gt Down
2. Down -&gt Down -&gt Right -&gt Right
## Solutions:
```python
class Solution :
public:
    int uniquePathsWithObstacles(vector>& obstacleGrid) :
        int m = obstacleGrid.size()
        if (m == 0) return 0
        int n = obstacleGrid[0].size()
        if (n == 0) return 0
        vector> dp (m, vector (n, 0)) // the type is long otherwise there is possiblity of overflow exception for intermittent positions. 
        dp[0][0] = 1
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (obstacleGrid[i][j] == 1) :
                    dp[i][j] = 0
                 else :
                    dp[i][j] = (i - 1 >= 0 ? dp[i-1][j] : 0) + (j - 1 >= 0 ? dp[i][j-1] : 0)
                    if (i == 0 && j == 0)   dp[i][j] = 1 // otherwise dp[0][0] would be corrupted.
        return dp[m-1][n-1]
```
# 62. Unique Paths
* *Difficulty: Medium*
* *Topics: Array, Dynamic Programming*
* *Similar Questions:*
  * [Unique Paths II](unique-paths-ii.md)
  * [Minimum Path Sum](minimum-path-sum.md)
  * [Dungeon Game](dungeon-game.md)
## Problem:
A robot is located at the top-left corner of a m x n grid (marked &#39Start&#39 in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39Finish&#39 in the diagram below).
How many possible unique paths are there?
Above is a 7 x 3 grid. How many possible unique paths are there?
Note: m and n will be at most 100.
Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt Right -&gt Down
2. Right -&gt Down -&gt Right
3. Down -&gt Right -&gt Right
Example 2:
Input: m = 7, n = 3
Output: 28
## Solutions:
```python
class Solution :
public:
    int uniquePaths(int m, int n) :
        if (m == 0 || n == 0)   return 0
        vector dp(n, 1)
        for (int i = 1 i < m ++i) :
            for (int j = 1 j < n ++j) :
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
```
# 288. Unique Word Abbreviation
* *Difficulty: Medium*
* *Topics: Hash Table, Design*
* *Similar Questions:*
  * [Two Sum III - Data structure design](two-sum-iii-data-structure-design.md)
  * [Generalized Abbreviation](generalized-abbreviation.md)
## Problem:
An abbreviation of a word follows the form &ltfirst letter&gt&ltnumber&gt&ltlast letter&gt. Below are some examples of word abbreviations:
a) it                      --&gt it    (no abbreviation)
     1
     &darr
b) d|o|g                   --&gt d1g
              1    1  1
     1---5----0----5--8
     &darr   &darr    &darr    &darr  &darr    
c) i|nternationalizatio|n  --&gt i18n
              1
     1---5----0
     &darr   &darr    &darr
d) l|ocalizatio|n          --&gt l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word&#39s abbreviation is unique if no other word from the dictionary has the same abbreviation.
Example:
Given dictionary = [ &quotdeer&quot, &quotdoor&quot, &quotcake&quot, &quotcard&quot ]
isUnique(&quotdear&quot) -&gt false
isUnique(&quotcart&quot) -&gt true
isUnique(&quotcane&quot) -&gt false
isUnique(&quotmake&quot) -&gt true
## Solutions:
```python
class ValidWordAbbr :
public:
    ValidWordAbbr(vector& dictionary) :
        words.insert(dictionary.begin(), dictionary.end())
        for (const auto& word : words) :
            string abbr = toAbbr(word)
            ++wordAbbrFreq[abbr]
    bool isUnique(const string& word) :
        if (words.count(word) > 0) :
            return wordAbbrFreq[toAbbr(word)] == 1
         else :
            return wordAbbrFreq.find(toAbbr(word)) == wordAbbrFreq.end()
private:
    string toAbbr(const string& str) :
        string abbr
        abbr.push_back(str[0])
        if (str.length() > 2) :
            abbr.append(to_string(str.length() - 2))
        if (str.length() > 1) :
            abbr.push_back(str.back())
        return abbr
    unordered_set words
    unordered_map wordAbbrFreq
/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr* obj = new ValidWordAbbr(dictionary)
 * bool param_1 = obj->isUnique(word)
 */
```
# 393. UTF-8 Validation
* *Difficulty: Medium*
* *Topics: Bit Manipulation*
* *Similar Questions:*
## Problem:
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.
Example 1:
data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:
data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
## Solutions:
```python
class Solution :
public:
    bool validUtf8(vector& data) :
        int pos = 0
        while (pos < data.size()) :
            bool ret = getToken(data, pos)
            //cout << pos << endl
            if (!ret)   return false
        return true
private:
    bool getToken(const vector& data, int& pos) :
        if (pos >= data.size()) return false
        int firstByte = data[pos++]
        if (firstByte < 128)    return true
        if (firstByte < 192)    return false
        if (firstByte < 224) :
            if (pos >= data.size()) return false
            int secondByte = data[pos++]
            return secondByte >= 128 && secondByte < 192
        if (firstByte < 240) :
            if (pos + 1 >= data.size()) return false
            int bytes[2]
            bytes[0] = data[pos++]
            bytes[1] = data[pos++]
            for (int i = 0  i < 2 ++i) :
                if (bytes[i] = 192)    return false
            return true
        if (firstByte < 248) :
            if (pos + 2 >= data.size()) return false
            int bytes[3]
            bytes[0] = data[pos++]
            bytes[1] = data[pos++]
            bytes[2] = data[pos++]
            for (int i = 0  i < 3 ++i) :
                if (bytes[i] = 192)    return false
            return true
        return false
```
# 242. Valid Anagram
* *Difficulty: Easy*
* *Topics: Hash Table, Sort*
* *Similar Questions:*
  * [Group Anagrams](group-anagrams.md)
  * [Palindrome Permutation](palindrome-permutation.md)
  * [Find All Anagrams in a String](find-all-anagrams-in-a-string.md)
## Problem:
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = &quotanagram&quot, t = &quotnagaram&quot
Output: true
Example 2:
Input: s = &quotrat&quot, t = &quotcar&quot
Output: false
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
## Solutions:
```python
class Solution :
public:
    bool isAnagram(string s, string t) :
        if (s.length() != t.length())   return false
        int count[26] = :0
        for (auto c : s) :
            ++count[c - 'a']
        for (auto c : t) :
            if (--count[c - 'a'] < 0) return false 
        return true
```
# 65. Valid Number
* *Difficulty: Hard*
* *Topics: Math, String*
* *Similar Questions:*
  * [String to Integer (atoi)](string-to-integer-atoi.md)
## Problem:
Validate if a given string can be interpreted as a decimal number.
Some examples:
&quot0&quot =&gt true
&quot 0.1 &quot =&gt true
&quotabc&quot =&gt false
&quot1 a&quot =&gt false
&quot2e10&quot =&gt true
&quot -90e3   &quot =&gt true
&quot 1e&quot =&gt false
&quote3&quot =&gt false
&quot 6e-1&quot =&gt true
&quot 99e2.5 &quot =&gt false
&quot53.5e93&quot =&gt true
&quot --6 &quot =&gt false
&quot-+3&quot =&gt false
&quot95a54e53&quot =&gt false
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
	Numbers 0-9
	Exponent - &quote&quot
	Positive/negative sign - &quot+&quot/&quot-&quot
	Decimal point - &quot.&quot
Of course, the context of these characters also matters in the input.
Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
## Solutions:
```python
class Solution :
public:
    bool isNumber(string s) :
        bool sign = false
        bool dot = false
        bool exponent = false
        bool num = false
        int left = 0
        while (left < s.length() && s[left] == ' ')  ++left
        int right = s.length() - 1
        while (right >= 0 && s[right] == ' ') --right
        if (left > right)   return false
        for (int i = left i <= right ++i) :
            char c = s[i]
            if (isdigit(c)) :
                sign = true
                num = true
               // if (c == '0' && i -1 >= 0 && s[i-1] == '0' && !dot) return false
            else if (c == '+' || c == '-') :
                if (sign)   return false
                sign = true
            else if (c == 'e') :
                if (exponent)   return false
                if (!num)   return false
                sign = false
                dot = true
                exponent = true
                num = false
            else if (c == '.') :
                if (dot)    return false
                dot = true
                sign = true
            else :
                return false
        return s[right] != 'e' && num
```
# 680. Valid Palindrome II
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Valid Palindrome](valid-palindrome.md)
## Problem:
Given a non-empty string s, you may delete at most one character.  Judge whether you can make it a palindrome.
Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.
## Solutions:
```python
class Solution :
public:
    bool validPalindrome(string s) :
        int left = 0
        int right = s.length() - 1
        while (left < right) :
            if (s[left] != s[right]) :
                return isPanlindrome(s, left + 1, right) || isPanlindrome(s, left, right - 1)
            ++left
            --right
        return true
private:
    bool isPanlindrome(string& s, int left, int right) :
        while (left < right) :
            if (s[left] != s[right])    return false
            ++left
            --right
        return true
```
# 1178. Valid Palindrome III
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming*
* *Similar Questions:*
## Problem:
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.
A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.
Example 1:
Input: s = &quotabcdeca&quot, k = 2
Output: true
Explanation: Remove &#39b&#39 and &#39e&#39 characters.
Constraints:
	1 &lt= s.length &lt= 1000
	s has only lowercase English letters.
	1 &lt= k &lt= s.length
## Solutions:
```python
class Solution :
public:
    bool isValidPalindrome(string s, int k) :
        int n = s.length()
        vector> dp(n, vector(n, 0))
        for (int len = 2 len <= n ++len) :
            for (int i = 0 i <= n - len ++i) :
                int left = i
                int right = i + len - 1
                dp[left][right] = 1 + min(dp[left + 1][right], dp[left][right - 1])
                if (s[left] == s[right]) :
                    dp[left][right] = min(dp[left][right], dp[left+1][right-1])
        return dp[0][n-1] <= k
```
# 125. Valid Palindrome
* *Difficulty: Easy*
* *Topics: Two Pointers, String*
* *Similar Questions:*
  * [Palindrome Linked List](palindrome-linked-list.md)
  * [Valid Palindrome II](valid-palindrome-ii.md)
## Problem:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
Input: &quotA man, a plan, a canal: Panama&quot
Output: true
Example 2:
Input: &quotrace a car&quot
Output: false
## Solutions:
```python
class Solution :
public:
    bool isPalindrome(string s) :
        int left = 0
        int right = s.length() - 1
        while (left < right) :
            while (left < right && !isalphanum(s[left])) :
                ++left
            while (left < right && !std::isalnum(s[right])): // remember the name of the funciton
                --right
            if (s[left] >= '0' && s[left] <= '9' && s[left] != s[right]) :
                return false
            if (tolower(s[left]) != tolower(s[right])) :
                return false
            ++left
            --right
        return true
    bool isalphanum(char c) :
        return c >= 'a' && c = 'A' && c = '0' && c <= '9'
```
# 20. Valid Parentheses
* *Difficulty: Easy*
* *Topics: String, Stack*
* *Similar Questions:*
  * [Generate Parentheses](generate-parentheses.md)
  * [Longest Valid Parentheses](longest-valid-parentheses.md)
  * [Remove Invalid Parentheses](remove-invalid-parentheses.md)
  * [Check If Word Is Valid After Substitutions](check-if-word-is-valid-after-substitutions.md)
## Problem:
Given a string containing just the characters &#39(&#39, &#39)&#39, &#39:&#39, &#39&#39, &#39[&#39 and &#39]&#39, determine if the input string is valid.
An input string is valid if:
	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: &quot()&quot
Output: true
Example 2:
Input: &quot()[]:&quot
Output: true
Example 3:
Input: &quot(]&quot
Output: false
Example 4:
Input: &quot([)]&quot
Output: false
Example 5:
Input: &quot:[]&quot
Output: true
## Solutions:
```python
class Solution :
public:
    bool isValid(string s) :
        stack stk
        for (auto c : s) :
            switch(c) :
                case '(':
                case ':':
                case '[':
                    stk.push(c)
                    break
                case ')':
                    if (stk.empty() || stk.top() != '(') return false
                    stk.pop()
                    break
                case '':
                    if (stk.empty() || stk.top() != ':') return false
                    stk.pop()
                    break
                case ']':
                    if (stk.empty() || stk.top() != '[') return false
                    stk.pop()
                    break
                default:
                    continue
        return stk.empty()
```
# 367. Valid Perfect Square
* *Difficulty: Easy*
* *Topics: Math, Binary Search*
* *Similar Questions:*
  * [Sqrt(x)](sqrtx.md)
  * [Sum of Square Numbers](sum-of-square-numbers.md)
## Problem:
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
Example 1:
Input: 16
Output: true
Example 2:
Input: 14
Output: false
## Solutions:
```python
class Solution :
public:
    bool isPerfectSquare(int num) :
        int left = 1 // left is 1!
        int right = INT_MAX
        while (left < right) :
            int mid = left + (right - left) / 2
            if (num / mid > mid) :
                left = mid + 1
             else :
                right = mid
        return num % left == 0 && num / left == left
```
# 193. Valid Phone Numbers
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
## Problem:
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.
You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
You may also assume each line in the text file must not contain leading or trailing white spaces.
Example:
Assume that file.txt has the following content:
987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:
987-123-4567
(123) 456-7890
## Solutions:
```python
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -e '^[0-9]\:3\-[0-9]\:3\-[0-9]\:4\$' -e '^([0-9]\:3\) [0-9]\:3\-[0-9]\:4\$' file.txt
```
# 36. Valid Sudoku
* *Difficulty: Medium*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Sudoku Solver](sudoku-solver.md)
## Problem:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
	Each row must contain the digits 1-9 without repetition.
	Each column must contain the digits 1-9 without repetition.
	Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character &#39.&#39.
Example 1:
Input:
[
  [&quot5&quot,&quot3&quot,&quot.&quot,&quot.&quot,&quot7&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot],
  [&quot6&quot,&quot.&quot,&quot.&quot,&quot1&quot,&quot9&quot,&quot5&quot,&quot.&quot,&quot.&quot,&quot.&quot],
  [&quot.&quot,&quot9&quot,&quot8&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot6&quot,&quot.&quot],
  [&quot8&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot6&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot3&quot],
  [&quot4&quot,&quot.&quot,&quot.&quot,&quot8&quot,&quot.&quot,&quot3&quot,&quot.&quot,&quot.&quot,&quot1&quot],
  [&quot7&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot2&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot6&quot],
  [&quot.&quot,&quot6&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot2&quot,&quot8&quot,&quot.&quot],
  [&quot.&quot,&quot.&quot,&quot.&quot,&quot4&quot,&quot1&quot,&quot9&quot,&quot.&quot,&quot.&quot,&quot5&quot],
  [&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot8&quot,&quot.&quot,&quot.&quot,&quot7&quot,&quot9&quot]
]
Output: true
Example 2:
Input:
[
  [&quot8&quot,&quot3&quot,&quot.&quot,&quot.&quot,&quot7&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot],
  [&quot6&quot,&quot.&quot,&quot.&quot,&quot1&quot,&quot9&quot,&quot5&quot,&quot.&quot,&quot.&quot,&quot.&quot],
  [&quot.&quot,&quot9&quot,&quot8&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot6&quot,&quot.&quot],
  [&quot8&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot6&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot3&quot],
  [&quot4&quot,&quot.&quot,&quot.&quot,&quot8&quot,&quot.&quot,&quot3&quot,&quot.&quot,&quot.&quot,&quot1&quot],
  [&quot7&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot2&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot6&quot],
  [&quot.&quot,&quot6&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot2&quot,&quot8&quot,&quot.&quot],
  [&quot.&quot,&quot.&quot,&quot.&quot,&quot4&quot,&quot1&quot,&quot9&quot,&quot.&quot,&quot.&quot,&quot5&quot],
  [&quot.&quot,&quot.&quot,&quot.&quot,&quot.&quot,&quot8&quot,&quot.&quot,&quot.&quot,&quot7&quot,&quot9&quot]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8&#39s in the top left 3x3 sub-box, it is invalid.
Note:
	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
	Only the filled cells need to be validated according to the mentioned rules.
	The given board contain only digits 1-9 and the character &#39.&#39.
	The given board size is always 9x9.
## Solutions:
```python
class Solution :
public:
    bool isValidSudoku(vector>& board) :
        int m = board.size()
        if (m == 0) return true
        for (int i = 0 i < m ++i) :
            if (!isRowValid(board, i))  return false
            if (!isColumnValid(board, i))   return false
        for (int i = 0 i < m i = i + 3) :
            for (int j = 0 j < m j = j + 3) :
                if (!isBlockValid(board, i, j)) return false
        return true
    bool isRowValid(vector>& board, int row) :
        bool nums[10] = :false
        for (auto c : board[row]) :
            if (c == '.') continue
            if (nums[c - '0'])   return false
            nums[c - '0'] = true
        return true
    bool isColumnValid(vector>& board, int col) :
        bool nums[10] = :false
        int rowNum = board.size()
        for (int i = 0 i < rowNum ++i) :
            char c = board[i][col]
            if (c == '.') continue
            if (nums[c - '0'])  return false
            nums[c - '0'] = true
        return true
    bool isBlockValid(vector>& board, int row, int col) :
        bool nums[10] = :false
        for (int i = row i < row + 3 ++i) :
            for (int j = col j < col + 3 ++j) :
                char c = board[i][j]
                if (c == '.') continue
                if (nums[c - '0']) return false
                nums[c - '0'] = true
        return true
```
# 810. Valid Tic-Tac-Toe State
* *Difficulty: Medium*
* *Topics: Math, Recursion*
* *Similar Questions:*
  * [Design Tic-Tac-Toe](design-tic-tac-toe.md)
## Problem:
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
The board is a 3 x 3 array, and consists of characters &quot &quot, &quotX&quot, and &quotO&quot.  The &quot &quot character represents an empty square.
Here are the rules of Tic-Tac-Toe:
	Players take turns placing characters into empty squares (&quot &quot).
	The first player always places &quotX&quot characters, while the second player always places &quotO&quot characters.
	&quotX&quot and &quotO&quot characters are always placed into empty squares, never filled ones.
	The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
	The game also ends if all squares are non-empty.
	No more moves can be played if the game is over.
Example 1:
Input: board = [&quotO  &quot, &quot   &quot, &quot   &quot]
Output: false
Explanation: The first player always plays &quotX&quot.
Example 2:
Input: board = [&quotXOX&quot, &quot X &quot, &quot   &quot]
Output: false
Explanation: Players take turns making moves.
Example 3:
Input: board = [&quotXXX&quot, &quot   &quot, &quotOOO&quot]
Output: false
Example 4:
Input: board = [&quotXOX&quot, &quotO O&quot, &quotXOX&quot]
Output: true
Note:
	board is a length-3 array of strings, where each string board[i] has length 3.
	Each board[i][j] is a character in the set :&quot &quot, &quotX&quot, &quotO&quot.
## Solutions:
```python
class Solution :
public:
    bool validTicTacToe(vector& board) :
        const int n = 3
        int rowCount[2][n] = :0
        int colCount[2][n] = :0
        int diag[2] = :0
        int antiDiag[2] = :0
        int count[2] = :0 // count!!!
        bool rowWin = false
        bool colWin = false
        bool winner[2] = :false
        for (int i = 0 i < n ++i) :
            for (int j = 0 j < n ++j) :
                if (board[i][j] == ' ') continue
                int player = (board[i][j] == 'X' ? 0 : 1)
                ++count[player]
                if (++rowCount[player][i] == n) :
                    if (rowWin)    return false
                    else rowWin = true
                    winner[player] = true
                if (++colCount[player][j] == n) :
                    if (colWin)    return false
                    else colWin = true
                    winner[player] = true
                if (i == j) :
                    if (++diag[player] == n) :
                        winner[player] = true
                if (i + j == n -1) :
                    if (++antiDiag[player] == n) :
                        winner[player] = true
        if (winner[0] == true) :
            return count[0] == count[1] + 1
         else if (winner[1] == true) :
            return count[0] == count[1]
         else :
            return count[0] == count[1] || count[0] == count[1] + 1
```
# 611. Valid Triangle Number
* *Difficulty: Medium*
* *Topics: Array*
* *Similar Questions:*
  * [3Sum Smaller](3sum-smaller.md)
## Problem:
Given an array consists of non-negative integers,  your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
## Solutions:
```python
class Solution :
public:
    int triangleNumber(vector& nums) :
        if (nums.size() < 3)    return 0
        sort(nums.begin(), nums.end())
        int count = 0
        for (int i = 0 i < nums.size() - 2 ++i) :
            int a = nums[i]
            int bIndex = i + 1
            int cIndex = i + 2
            for ( cIndex < nums.size() ++cIndex) :
                while (bIndex < cIndex && a + nums[bIndex] <= nums[cIndex]) :
                    ++bIndex
                if (cIndex > bIndex) :
                    count += (cIndex - bIndex)
        return count
```
# 408. Valid Word Abbreviation
* *Difficulty: Easy*
* *Topics: String*
* *Similar Questions:*
  * [Minimum Unique Word Abbreviation](minimum-unique-word-abbreviation.md)
  * [Word Abbreviation](word-abbreviation.md)
## Problem:
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
A string such as "word" contains only the following valid abbreviations:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".
Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
Example 1:
Given s = "internationalization", abbr = "i12iz4n":
Return true.
Example 2:
Given s = "apple", abbr = "a2e":
Return false.
## Solutions:
```python
class Solution :
public:
    bool validWordAbbreviation(string word, string abbr) :
        int pos = 0
        int count = 0
        for (int i = 0 i < abbr.length() ++i) :
            if (!isdigit(abbr[i])) :
                pos += count
                count = 0
                if (pos > word.length() || word[pos] != abbr[i])    return false
                ++pos
             else :
                if (count == 0 && abbr[i] == '0')   return false
                count = 10 * count + (abbr[i] - '0')
        pos += count
        return pos == word.length()
```
# 422. Valid Word Square
* *Difficulty: Easy*
* *Topics: *
* *Similar Questions:*
  * [Word Squares](word-squares.md)
  * [Toeplitz Matrix](toeplitz-matrix.md)
## Problem:
Given a sequence of words, check whether it forms a valid word square.
A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 &le k &lt max(numRows, numColumns).
Note:
The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
Example 1:
Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
Output:
true
Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".
Therefore, it is a valid word square.
Example 2:
Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]
Output:
true
Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".
Therefore, it is a valid word square.
Example 3:
Input:
[
  "ball",
  "area",
  "read",
  "lady"
]
Output:
false
Explanation:
The third row reads "read" while the third column reads "lead".
Therefore, it is NOT a valid word square.
## Solutions:
```python
class Solution :
public:
    bool validWordSquare(vector& words) :
        int m = words.size()
        if (m == 0) return true
        int n = words[0].size()
        if (n == 0) return true
        if (m != n) return false
        for (int i = 0 i <m ++i) :
            if (words[i].length() > m)  return false
            for (int j = 0 j < i ++j) :
                if (j >= words[i].length() && i >= words[j].length()) :
                    continue
                else if (j < words[i].length() && j < words[j].length()) :
                    if (words[i][j] != words[j][i]) return false
                else 
                    return false
        return true
```
# 98. Validate Binary Search Tree
* *Difficulty: Medium*
* *Topics: Tree, Depth-first Search*
* *Similar Questions:*
  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)
  * [Find Mode in Binary Search Tree](find-mode-in-binary-search-tree.md)
## Problem:
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
	The left subtree of a node contains only nodes with keys less than the node&#39s key.
	The right subtree of a node contains only nodes with keys greater than the node&#39s key.
	Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Input: [2,1,3]
Output: true
Example 2:
    5
   / \
  1   4
     / \
    3   6
Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node&#39s value is 5 but its right child&#39s value is 4.
## Solutions:
```python
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 *     int val
 *     TreeNode *left
 *     TreeNode *right
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isValidBST(TreeNode* root) :
        return isValidBSTHelper(root, NULL, NULL)
    bool isValidBSTHelper(TreeNode* root, TreeNode*left, TreeNode* right) :
        if (root == NULL)   return true
        if (left && root->val val || right && root->val >= right->val) return false
        return isValidBSTHelper(root->left, left, root) && isValidBSTHelper(root->right, root, right)
```
# 255. Verify Preorder Sequence in Binary Search Tree
* *Difficulty: Medium*
* *Topics: Stack, Tree*
* *Similar Questions:*
  * [Binary Tree Preorder Traversal](binary-tree-preorder-traversal.md)
## Problem:
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
You may assume each number in the sequence is unique.
Consider the following binary search tree: 
     5
    / \
   2   6
  / \
 1   3
Example 1:
Input: [5,2,6,1,3]
Output: false
Example 2:
Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?
## Solutions:
```python
class Solution :
public:
    bool verifyPreorder(vector& preorder) :
        stack stk
        int lowerBound = INT_MIN
        for (auto num : preorder) :
            if (num <= lowerBound)  return false
            if (!stk.empty() && stk.top() == num)   return false
            while (!stk.empty() && stk.top() < num) :
                lowerBound = stk.top()
                //cout << lowerBound << " " << num << endl
                stk.pop()
            stk.push(num)
        return true
```
# 990. Verifying an Alien Dictionary
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
## Problem:
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
Example 1:
Input: words = [&quothello&quot,&quotleetcode&quot], order = &quothlabcdefgijkmnopqrstuvwxyz&quot
Output: true
Explanation: As &#39h&#39 comes before &#39l&#39 in this language, then the sequence is sorted.
Example 2:
Input: words = [&quotword&quot,&quotworld&quot,&quotrow&quot], order = &quotworldabcefghijkmnpqstuvxyz&quot
Output: false
Explanation: As &#39d&#39 comes after &#39l&#39 in this language, then words[0] &gt words[1], hence the sequence is unsorted.
Example 3:
Input: words = [&quotapple&quot,&quotapp&quot], order = &quotabcdefghijklmnopqrstuvwxyz&quot
Output: false
Explanation: The first three characters &quotapp&quot match, and the second string is shorter (in size.) According to lexicographical rules &quotapple&quot &gt &quotapp&quot, because &#39l&#39 &gt &#39&empty&#39, where &#39&empty&#39 is defined as the blank character which is less than any other character (More info).
Note:
	1 &lt= words.length &lt= 100
	1 &lt= words[i].length &lt= 20
	order.length == 26
	All characters in words[i] and order are english lowercase letters.
## Solutions:
```python
class Solution :
public:
  bool isAlienSorted(vector& words, string order) :
    vector m(26)
    for (int i = 0 i < 26 ++i)
      m[order[i] - 'a'] = 'a' + i
    for (int i = 0 i < words.size() ++i) :      
      for (int j = 0 j < words[i].length() ++j)
        words[i][j] = m[words[i][j] - 'a']      
      if (i > 0 && words[i] < words[i - 1]) return false      
    return true        
```
# 286. Walls and Gates
* *Difficulty: Medium*
* *Topics: Breadth-first Search*
* *Similar Questions:*
  * [Surrounded Regions](surrounded-regions.md)
  * [Number of Islands](number-of-islands.md)
  * [Shortest Distance from All Buildings](shortest-distance-from-all-buildings.md)
  * [Robot Room Cleaner](robot-room-cleaner.md)
  * [Rotting Oranges](rotting-oranges.md)
## Problem:
You are given a m x n 2D grid initialized with these three possible values.
	-1 - A wall or an obstacle.
	0 - A gate.
	INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
Example: 
Given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
## Solutions:
```python
class Solution :
public:
    void wallsAndGates(vector>& rooms) :
        int INF = INT_MAX
        queue> q
        int m = rooms.size()
        if (m == 0) return
        int n = rooms[0].size()
        if (n == 0) return
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (rooms[i][j] == 0) :
                    q.push(:i + 1, j)
                    q.push(:i - 1, j)
                    q.push(:i, j + 1)
                    q.push(:i, j - 1)
        int distance = 0
        while (!q.empty()) :
            ++distance
            int size = q.size()
            for (int k = 0 k < size ++k) :
                int row = q.front().first
                int col = q.front().second
                q.pop()
                if (row = m || col = n || rooms[row][col] != INF)  continue
                rooms[row][col] = distance
                q.push(:row + 1, col)
                q.push(:row - 1, col)
                q.push(:row, col - 1)
                q.push(:row, col + 1)
```
# 365. Water and Jug Problem
* *Difficulty: Medium*
* *Topics: Math*
* *Similar Questions:*
## Problem:
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.
If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
Operations allowed:
	Fill any of the jugs completely with water.
	Empty any of the jugs.
	Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous &quotDie Hard&quot example)
Input: x = 3, y = 5, z = 4
Output: True
Example 2:
Input: x = 2, y = 6, z = 5
Output: False
## Solutions:
```python
class Solution :
public:
    bool canMeasureWater(int x, int y, int z) :
        // ax + by = z
        if (z ==0)  return true
        if (x + y < z) return false
        if (x != 0 && y != 0) :
            int divisor = gcd(x, y)
            return z % divisor == 0
         else return false
private:
    int gcd (int x, int y) :
        if (y > x) :
            return gcd(y, x)
        if (y == 0) return x
        return gcd(y, x % y)
```
# 280. Wiggle Sort
* *Difficulty: Medium*
* *Topics: Array, Sort*
* *Similar Questions:*
  * [Sort Colors](sort-colors.md)
  * [Wiggle Sort II](wiggle-sort-ii.md)
## Problem:
Given an unsorted array nums, reorder it in-place such that nums[0] &lt= nums[1] &gt= nums[2] &lt= nums[3]....
Example:
Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
## Solutions:
```python
class Solution :
public:
    void wiggleSort(vector& nums) :
        for (int i = 1 i < nums.size() ++i) :
            if (i % 2 == 1) :
                if (nums[i] < nums[i - 1]) :
                    swap(nums[i], nums[i-1])
             else :
                if (nums[i] > nums[i-1]) :
                    swap(nums[i], nums[i-1])
```
# 44. Wildcard Matching
* *Difficulty: Hard*
* *Topics: String, Dynamic Programming, Backtracking, Greedy*
* *Similar Questions:*
  * [Regular Expression Matching](regular-expression-matching.md)
## Problem:
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for &#39?&#39 and &#39*&#39.
&#39?&#39 Matches any single character.
&#39*&#39 Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:
Input:
s = &quotaa&quot
p = &quota&quot
Output: false
Explanation: &quota&quot does not match the entire string &quotaa&quot.
Example 2:
Input:
s = &quotaa&quot
p = &quot*&quot
Output: true
Explanation: &#39*&#39 matches any sequence.
Example 3:
Input:
s = &quotcb&quot
p = &quot?a&quot
Output: false
Explanation: &#39?&#39 matches &#39c&#39, but the second letter is &#39a&#39, which does not match &#39b&#39.
Example 4:
Input:
s = &quotadceb&quot
p = &quot*a*b&quot
Output: true
Explanation: The first &#39*&#39 matches the empty sequence, while the second &#39*&#39 matches the substring &quotdce&quot.
Example 5:
Input:
s = &quotacdcb&quot
p = &quota*c?b&quot
Output: false
## Solutions:
```python
class Solution :
public:
    bool isMatch(string s, string p) :
        int m = s.length()
        int n = p.length()
        vector> dp(m + 1, vector(n + 1, false))
        dp[0][0] = true
        for (int i = 0 i <= m ++i) :
            for (int j = 0 j <= n ++j) :
                if (i == 0 && j == 0)   continue
                if (j == 0) continue
                if (p[j - 1] == '*') :
                    dp[i][j] = dp[i][j-1]
                    if (i > 0) :
                        dp[i][j] = dp[i][j] || dp[i-1][j]
                 else if (i > 0 && (p[j - 1] == '?' || s[i-1] == p[j-1])) :
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]
```
### More concise DP
It is not necessary to separate the initialization process. 
From [Grandyang] (https://www.cnblogs.com/grandyang/p/4461713.html)
```python
class Solution :
public:
    bool isMatch(string s, string p) :
        int m = s.size(), n = p.size()
        vector> dp(m + 1, vector(n + 1, false))
        dp[0][0] = true
        for (int i = 0 i <= m ++i) :
            for (int j = 1 j <= n ++j) :
                if (j > 1 && p[j - 1] == '*') :
                    dp[i][j] = dp[i][j - 2] || (i > 0 && (s[i - 1] == p[j - 2] || p[j - 2] == '.') && dp[i - 1][j])
                 else :
                    dp[i][j] = i > 0 && dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.')
        return dp[m][n]
```
# 140. Word Break II
* *Difficulty: Hard*
* *Topics: Dynamic Programming, Backtracking*
* *Similar Questions:*
  * [Word Break](word-break.md)
  * [Concatenated Words](concatenated-words.md)
## Problem:
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
Note:
	The same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.
Example 1:
Input:
s = &quotcatsanddog&quot
wordDict = [&quotcat&quot, &quotcats&quot, &quotand&quot, &quotsand&quot, &quotdog&quot]
Output:
[
  &quotcats and dog&quot,
  &quotcat sand dog&quot
]
Example 2:
Input:
s = &quotpineapplepenapple&quot
wordDict = [&quotapple&quot, &quotpen&quot, &quotapplepen&quot, &quotpine&quot, &quotpineapple&quot]
Output:
[
  &quotpine apple pen apple&quot,
  &quotpineapple pen apple&quot,
  &quotpine applepen apple&quot
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:
Input:
s = &quotcatsandog&quot
wordDict = [&quotcats&quot, &quotdog&quot, &quotsand&quot, &quotand&quot, &quotcat&quot]
Output:
[]
## Solutions:
```python
class Solution :
public:
    struct TrieNode:
        bool stop
        TrieNode* next[26]
        TrieNode(bool stop = false) :
            this->stop = stop
            for (int i = 0 i < 26 ++i) :
                next[i] = nullptr
    class Trie :
        public:
            Trie() :
                root = new TrieNode()
                cur = root
            TrieNode* getRoot() :
                return root
            TrieNode* getCur() :
                return cur
            void setCur(TrieNode* cur) :
                this->cur = cur
            void rewind() :
                cur = root
            bool next(char c) :
                if (cur == nullptr || cur->next[c - 'a'] == nullptr) :
                    cur = nullptr
                    return false
                cur = cur->next[c - 'a']
                return true
            bool isWord() :
                return cur->stop
            void input(string s) :
                cur = root
                for (auto c : s) :
                    if (cur->next[c - 'a'] == nullptr) :
                        cur->next[c - 'a'] = new TrieNode()
                    cur = cur->next[c - 'a']
                cur->stop = true
                cur = root
        private:
            TrieNode* root
            TrieNode* cur
    vector wordBreak(string s, vector& wordDict) :
        Trie trie
        for (auto word : wordDict) :
            trie.input(word)
        unordered_map>> cache
        auto wordLists = helper(s, 0, trie, cache)
        vector ret
        for (auto& wordList : wordLists) :
            ret.push_back(join(wordList))
        return ret
    string join(const vector& path) :
        string s
        if (path.size() == 0)   return s
        s = path[0]
        for (int i = 1 i < path.size() ++i) :
            s.append(" ")
            s.append(path[i])
        return s
    vector> helper(const string& s, int pos, Trie& trie, unordered_map>>& cache) :
        vector> ret
        if (cache.count(pos) > 0) :
            return cache[pos]
        for (int j = pos j < s.length() ++j) :
            if (!trie.next(s[j])) :
               break
             else :
                if (trie.isWord()) :
                    if (j == s.length() - 1):
                        ret.push_back(:s.substr(pos))       
                    TrieNode* cur = trie.getCur()
                    trie.rewind()
                    auto suffix = helper(s, j + 1, trie, cache)
                    trie.setCur(cur)
                    for (auto& path : suffix) :
                        ret.push_back(:s.substr(pos, j - pos + 1))
                        ret.back().insert(ret.back().end(), path.begin(), path.end())
        cache[pos] = ret
        return ret
```
# 139. Word Break
* *Difficulty: Medium*
* *Topics: Dynamic Programming*
* *Similar Questions:*
  * [Word Break II](word-break-ii.md)
## Problem:
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
	The same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.
Example 1:
Input: s = &quotleetcode&quot, wordDict = [&quotleet&quot, &quotcode&quot]
Output: true
Explanation: Return true because &quotleetcode&quot can be segmented as &quotleet code&quot.
Example 2:
Input: s = &quotapplepenapple&quot, wordDict = [&quotapple&quot, &quotpen&quot]
Output: true
Explanation: Return true because &quotapplepenapple&quot can be segmented as &quotapple pen apple&quot.
             Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = &quotcatsandog&quot, wordDict = [&quotcats&quot, &quotdog&quot, &quotsand&quot, &quotand&quot, &quotcat&quot]
Output: false
## Solutions:
```python
class Solution :
public:
    struct TrieNode:
        bool stop
        TrieNode* next[26]
        TrieNode(bool stop = false) :
            this->stop = stop
            for (int i = 0 i < 26 ++i) :
                next[i] = nullptr
    class Trie :
        public:
            Trie() :
                root = new TrieNode()
                cur = root
            TrieNode* getCur() :
                return cur
            void setCur(TrieNode* cur) :
                this->cur = cur
            void rewind() :
                cur = root
            bool next(char c) :
                if (cur == nullptr || cur->next[c - 'a'] == nullptr) :
                    cur = nullptr
                    return false
                cur = cur->next[c - 'a']
                return true
            bool isWord() :
                return cur->stop
            void input(string s) :
                cur = root
                for (auto c : s) :
                    if (cur->next[c - 'a'] == nullptr) :
                        cur->next[c - 'a'] = new TrieNode()
                    cur = cur->next[c - 'a']
                cur->stop = true
                cur = root
        private:
            TrieNode* root
            TrieNode* cur
    bool wordBreak(string s, vector& wordDict) :
        Trie trie
        for (auto word : wordDict) :
            trie.input(word)
        unordered_map cache
        return helper(s, 0, trie, cache)
    bool helper(const string& s, int pos, Trie& trie, unordered_map& cache) :
        if (pos == s.length())  return true
        if (cache.count(pos) > 0)   return cache[pos]
        for (int i = pos i < s.length() ++i) :
            if (trie.next(s[i]) == false) :
                cache[pos] = false
                return false
             else :
                if (trie.isWord()) :
                    TrieNode* cur = trie.getCur()
                    trie.rewind()
                    if (helper(s, i + 1, trie, cache)) :
                        cache[pos] = true
                        return true
                    trie.setCur(cur)
        cache[pos] = false
        return false
```
# 192. Word Frequency
* *Difficulty: Medium*
* *Topics: *
* *Similar Questions:*
  * [Top K Frequent Elements](top-k-frequent-elements.md)
## Problem:
Write a bash script to calculate the frequency of each word in a text file words.txt.
For simplicity sake, you may assume:
	words.txt contains only lowercase characters and space &#39 &#39 characters.
	Each word must consist of lowercase characters only.
	Words are separated by one or more whitespace characters.
Example:
Assume that words.txt has the following content:
the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:
the 4
is 3
sunny 2
day 1
Note:
	Don&#39t worry about handling ties, it is guaranteed that each word&#39s frequency count is unique.
	Could you write it in one-line using Unix pipes?
## Solutions:
```python
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk ': print $2, $1 '
```
# 127. Word Ladder
* *Difficulty: Medium*
* *Topics: Breadth-first Search*
* *Similar Questions:*
  * [Word Ladder II](word-ladder-ii.md)
  * [Minimum Genetic Mutation](minimum-genetic-mutation.md)
## Problem:
Given two words (beginWord and endWord), and a dictionary&#39s word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
	Only one letter can be changed at a time.
	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:
	Return 0 if there is no such transformation sequence.
	All words have the same length.
	All words contain only lowercase alphabetic characters.
	You may assume no duplicates in the word list.
	You may assume beginWord and endWord are non-empty and are not the same.
Example 1:
Input:
beginWord = &quothit&quot,
endWord = &quotcog&quot,
wordList = [&quothot&quot,&quotdot&quot,&quotdog&quot,&quotlot&quot,&quotlog&quot,&quotcog&quot]
Output: 5
Explanation: As one shortest transformation is &quothit&quot -&gt &quothot&quot -&gt &quotdot&quot -&gt &quotdog&quot -&gt &quotcog&quot,
return its length 5.
Example 2:
Input:
beginWord = &quothit&quot
endWord = &quotcog&quot
wordList = [&quothot&quot,&quotdot&quot,&quotdog&quot,&quotlot&quot,&quotlog&quot]
Output: 0
Explanation: The endWord &quotcog&quot is not in wordList, therefore no possible transformation.
## Solutions:
```python
class Solution :
public:
    int ladderLength(string beginWord, string endWord, vector& wordList) :
        unordered_set wordSet(wordList.begin(), wordList.end())
        if (wordSet.count(endWord) == 0)    return 0
        unordered_set q1
        unordered_set q2
        q1.insert(beginWord)
        q2.insert(endWord)
        int n = beginWord.length()
        int level = 0
        while (!(q1.empty() || q2.empty())) :
            ++level
            int size1 = q1.size()
            int size2 = q2.size()
            if (size1 > size2) :
                swap(q1, q2)
            unordered_set q
            for (string word : q1) :
                if (q2.count(word) > 0)    return level
                for (int pos = 0 pos < n ++pos) :
                    char origin = word[pos]
                    for (char letter = 'a' letter <= 'z' ++letter) :
                        word[pos] = letter
                        if  (q1.count(word) == 0 && wordSet.count(word) > 0) :
                            q.insert(word)
                    word[pos] = origin
            swap(q1, q)
        return 0
```
# 290. Word Pattern
* *Difficulty: Easy*
* *Topics: Hash Table*
* *Similar Questions:*
  * [Isomorphic Strings](isomorphic-strings.md)
  * [Word Pattern II](word-pattern-ii.md)
## Problem:
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Example 1:
Input: pattern = &quotabba&quot, str = &quotdog cat cat dog&quot
Output: true
Example 2:
Input:pattern = &quotabba&quot, str = &quotdog cat cat fish&quot
Output: false
Example 3:
Input: pattern = &quotaaaa&quot, str = &quotdog cat cat dog&quot
Output: false
Example 4:
Input: pattern = &quotabba&quot, str = &quotdog dog dog dog&quot
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
## Solutions:
```python
class Solution :
public:
    bool wordPattern(string pattern, string str) :
        unordered_map patternToString
        unordered_map stringToPattern
        int pos = 0
        for (int i = 0 i < pattern.length() ++i) :
            char c = pattern[i]
            string sub
            while (pos < str.length() && str[pos] != ' ') :
                sub.push_back(str[pos])
                ++pos
            if (patternToString.count(c) == 0 && stringToPattern.count(sub) == 0) :
                patternToString[c] = sub
                stringToPattern[sub] = c
             else :
                if (sub != patternToString[c] || c != stringToPattern[sub]) return false
            if (pos == str.length()) :
                return i == pattern.length() - 1
            ++pos
        return false
```
# 79. Word Search
* *Difficulty: Medium*
* *Topics: Array, Backtracking*
* *Similar Questions:*
  * [Word Search II](word-search-ii.md)
## Problem:
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where &quotadjacent&quot cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example:
board =
[
  [&#39A&#39,&#39B&#39,&#39C&#39,&#39E&#39],
  [&#39S&#39,&#39F&#39,&#39C&#39,&#39S&#39],
  [&#39A&#39,&#39D&#39,&#39E&#39,&#39E&#39]
]
Given word = &quotABCCED&quot, return true.
Given word = &quotSEE&quot, return true.
Given word = &quotABCB&quot, return false.
## Solutions:
```python
class Solution :
public:
    bool exist(vector>& board, string word) :
        if (word.length() == 0) return true
        int m = board.size()
        if (m == 0) return false
        int n = board[0].size()
        if (n == 0) return false
        // there is on path!
        vector> visited (m, vector(n, false))
        for (int i = 0 i < m ++i) :
            for (int j = 0 j < n ++j) :
                if (helper(board, m, n, i, j, visited, word, 0)) return true
        return false
    bool helper(vector>& board, int m, int n, int i, int j, vector>& visited, string& word, int pos) :
        if (i = m || j = n || visited[i][j])  return false
        if (word[pos] != board[i][j])   return false
        visited[i][j] = true
        if (pos == word.length() - 1)   return true 
        for (int d = 0 d < 4 ++d) :
            if(helper(board, m, n, i + directions[d][0], j + directions[d][1], visited, word, pos + 1))    return true
        visited[i][j] = false
        return false
private:
    int directions[4][2] = :
        :1, 0,
        :-1, 0,
        :0, 1,
        :0, -1
```
# 6. ZigZag Conversion
* *Difficulty: Medium*
* *Topics: String*
* *Similar Questions:*
## Problem:
The string &quotPAYPALISHIRING&quot is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: &quotPAHNAPLSIIGYIR&quot
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows)
Example 1:
Input: s = &quotPAYPALISHIRING&quot, numRows = 3
Output: &quotPAHNAPLSIIGYIR&quot
Example 2:
Input: s = &quotPAYPALISHIRING&quot, numRows = 4
Output: &quotPINALSIGYAHRPI&quot
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
## Solutions:
```python
class Solution :
public:
    string convert(string s, int numRows) :
        if (numRows == 0)    return ""
        if (numRows == 1)   return s
        int period = 2 * (numRows - 1)
        string ret
        for (int row = 0 row < numRows ++row) :
            for (int i = row i < s.length() i = i + period) :
                ret.push_back(s[i])
                if (row != 0 && row != numRows - 1 && i + (numRows - 1 - row) * 2 < s.length()) :
                    ret.push_back(s[i + (numRows - 1 - row) * 2])
        return ret
```
### More intuitive solution
Use multiple strings.
From [https://www.cnblogs.com/grandyang/p/4128268.html]Grandyang:
```python
class Solution :
public:
    string convert(string s, int numRows) :
        if (numRows <= 1) return s
        string res
        int i = 0, n = s.size()
        vector vec(numRows)
        while (i < n) :
            for (int pos = 0 pos < numRows && i < n ++pos) :
                vec[pos] += s[i++]
            for (int pos = numRows - 2 pos >= 1 && i < n --pos) :
                vec[pos] += s[i++]
        for (auto &a : vec) res += a
        return res
```
# 281. Zigzag Iterator
* *Difficulty: Medium*
* *Topics: Design*
* *Similar Questions:*
  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)
  * [Flatten 2D Vector](flatten-2d-vector.md)
  * [Peeking Iterator](peeking-iterator.md)
  * [Flatten Nested List Iterator](flatten-nested-list-iterator.md)
## Problem:
Given two 1d vectors, implement an iterator to return their elements alternately.
Example:
Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
Clarification for the follow up question:
The &quotZigzag&quot order is not clearly defined and is ambiguous for k &gt 2 cases. If &quotZigzag&quot does not look right to you, replace &quotZigzag&quot with &quotCyclic&quot. For example:
Input:
[1,2,3]
[4,5,6,7]
[8,9]
Output: [1,4,8,2,5,9,3,6,7].
## Solutions:
```python
class ZigzagIterator :
public:
    ZigzagIterator(vector& v1, vector& v2) :
        this->v1 = v1
        this->v2 = v2
    int next() :
        if (pos1 == v1.size()) :
            return v2[pos2++]
        if (pos2 == v2.size()) :
            return v1[pos1++]
        if ((pos1 + pos2) % 2 == 0) :
            return v1[pos1++]
         else :
            return v2[pos2++]
    bool hasNext() :
        return pos1 < v1.size() || pos2 < v2.size()
private:
    int pos1 = 0
    int pos2 = 0
    vector v1
    vector v2
/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2)
 * while (i.hasNext()) cout << i.next()
 */
```
