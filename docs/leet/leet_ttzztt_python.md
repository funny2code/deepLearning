------------------------------------------------------------------------------------------------
 200. Number of Islands (Amazon)
===================================
 [Leetcode] Number of Islands, Solution (
 水中的鱼
 )
 Given a 2d grid map
 `'1'` 
 s (land) and
 `'0'` 
 s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Code: with visited 2D record
```python
class Solution :
    m # rows
    n # cols
public:
    numIslands(vector<vector<char>>& grid) :
       m = grid.size()  
      if(m == 0) return 0  
       n = grid[0].size()  
        vector<vector<int>> visited (m, vector<int>(n, 0))
        islands = 0  
      for(i =0 i< m i++) :  
        for(j= 0 j< n j++) :  
          if(grid[i][j] == '0' || visited[i][j]) continue  
           merge0(grid,visited, i, j)  
           islands++  
       return islands  
private:
    void merge0(vector<vector<char>>& grid, vector<vector<int>>& visited, x, y):
        if(x<0 || x>=m) return
        if(y<0 || y>=n) return
        if(grid[x][y] == '0' || visited[x][y]) return  
        visited[x][y] = 1
        #  DFS 四个扩展点
        #  using lvaue so paramter x and y cannot not have & operator
        merge0(grid, visited, x + 1, y)
        merge0(grid, visited, x - 1, y)
        merge0(grid, visited, x , y + 1)
        merge0(grid, visited, x , y - 1)
```

 [Code]
```python
class Solution :
    m # rows
    n # cols
public:
    numIslands(vector<vector<char>>& grid) :
       m = grid.size()  
      if(m == 0) return 0  
       n = grid[0].size()  
      islands = 0  
      for(i =0 i< m i++) :  
        for(j= 0 j< n j++) :  
          if(grid[i][j] == '0') continue  
           merge(grid, i, j)  
           islands++  
       return islands  
private:
    void merge(vector<vector<char>>& grid, x, y):
        if(x<0 || x>=m) return
        if(y<0 || y>=n) return
        if(grid[x][y] == '0') return  
        grid[x][y] = '0'
        #  DFS 四个扩展点
        #  using lvaue so paramter x and y cannot not have & operator
        merge(grid, x + 1, y)
        merge(grid, x - 1, y)
        merge(grid, x , y + 1)
        merge(grid, x , y - 1)
    void merge2(vector<vector<char>>& grid, int& x, int& y):
        if(x<0 || x>=m) return  
        if(y<0 || y>=n) return  
        if(grid[x][y] == '0') return  
        grid[x][y] ='0'
        #  DFS 四个扩展点
        #  using rvalue so paramter x and y can have & operator
         up = x+1
         down = x-1
         left = y-1
         right = y+1
        merge(grid, up, y)
        merge(grid, down, y)
        merge(grid, x , right)
        merge(grid, x , left)
```
------------------------------------------------------------------------------------------------
 16.3 3Sum Closest
===================
 Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
```
    For example, given array S = :-1 2 1 -4, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
 Thoughts:
 add a distance tracking variable and update its value after each two-sum search. Other than this, the implementation is based on standard
 3sum
 .
```python
class Solution :
public:
    threeSumClosest(vector<int>& A, target) :
        len = A.size(), ans = INT_MAX, distance = INT_MAX
        sort(A.begin(),A.end())
        for (i = 0 i < len i++):
            left = i + 1, right = len - 1
            while(left < right):
                sum = A[left] + A[right] + A[i]
                if (sum == target):
                    return sum
                else if (sum < target):
                    update(ans, distance , sum, target)
                    left ++
                else :
                    update(ans, distance, sum, target)
                    right --
        return ans
    void update(int& ans, int& distance, sum, target):
        curDistance = sum > target? sum - target: target - sum
        ans = distance > curDistance? sum : ans
        distance =  distance > curDistance? curDistance : distance
```
 Extension:
 I can also calculate the minimum distance two-sum distance for current target and keep track the corresponding 3sum value in my answer as the following:
```python
class Solution :
public:
    threeSumClosest(vector<int>& A, target) :
        len = A.size(), ans = INT_MAX, distance = INT_MAX
        sort(A.begin(),A.end())
        for (i = 0 i < len i++):
            left = i + 1, right = len - 1
            curTarget = target - A[i] # change 1: find the current target
            while(left < right):
                sum = A[left] + A[right]
                if (sum == curTarget): #  change 2:
                    return target
                else if (sum < curTarget):
                    update(ans, distance , sum, curTarget, A[i]) #  change 3: (important): pass in an extra arguement for updating ans
                    left ++
                else :
                    update(ans, distance, sum, curTarget, A[i]) #  change 3 (important): pass in an extra arguement for updating ans
                    right --
        return ans
    void update(int& ans, int& distance, sum, target, base):
        curDistance = sum > target? sum - target: target - sum
        ans = distance > curDistance? sum + base : ans #  change 4: the candidate for new ans is "sum + base"
        distance =  distance > curDistance? curDistance : distance
```
```python
class Solution(object):
    def threeSumClosest(self, A, target):
        """
 :type A: List[int]
 :type target: int
 :rtype: int
 """
        A.sort()
        ans, dist = sys.maxint, sys.maxint #(sum(abs(A))) - target
        n = len(A)
        for i in range(n - 1):
            j, k = i + 1, n - 1
            while j < k:
                s = A[i] + A[j] + A[k]
                if s == target:
                    return s 
                elif s < target: 
                    j += 1
                else: # s > target:
                    k -= 1
                tmp = dist
                dist = min(abs(s - target), dist)
                ans = ans if dist == tmp else s 
        return ans
```
 I can also update them in the loop, as 水中的鱼's approach in this problem.
------------------------------------------------------------------------------------------------
 15. 3Sum
============
 Given an array S of n integers, are there elements a,b,c in S such that a+b+c= 0? Find all unique triplets in the array which gives the sum of zero.
 Note:
 The solution set must not contain duplicate triplets.
```
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```
 Follow up:
 如果不sort能怎么做
 Thoughts:
 a + b + c =0 <=> a + b = -c
 Traverse each element : a target of two sum. Search direction should be consistent with the direction of traverse order(avoid duplicates).
 [code 1: using map]: O(n^2) + Extra Space (HashMap
 /
 unordered_map) :
 https:# leetcode.com/problems/3sum/discuss/163934/Efficient-Java-Solution
```python
class Solution :
    public List<List<Integer>> threeSum(int[] A) :
        Arrays.sort(A)
        List<List<Integer>> res = new ArrayList<>()
        Map<Integer, Integer> map = new HashMap<>()
        for (i = 0 i < A.length i++) map.put(A[i], i) #  val , last index
        for(i = 0  i < A.length - 2 i++):
            for(j = i + 1 j < A.length -1 j++):
                target = 0 - A[i] - A[j]
                if (map.containsKey(target) && map.get(target) > j):
                    res.add(Arrays.asList(A[i], A[j], target))
                    j = map.get(A[j]) #  Taking the last index of j to remove duplicate 
            i = map.get(A[i]) #  Taking the last index of i to remove duplicate
        return res
```
 FollowUp: without Sort
 https:# leetcode.com/problems/3sum/discuss/110507/Golang-~n2+n-worst-case-no-sort-no-deduplication-O(n2)-beats-50
```python
class Solution :
    public List<List<Integer>> threeSum(int[] A) :
        if(A == null || A.length == 0) return new ArrayList<>()
        n = A.length
        List<List<Integer>> res = new ArrayList<>() #  1
        Map<Integer, Integer> map = new HashMap<>()
        for(i = 0  i < n i++):
            map.put(A[i], map.getOrDefault(A[i], 0) + 1)
        #  cross product
        for(i : map.keySet()):
            for(j: map.keySet()):
                if(i > j || (i == j && map.get(i) == 1)) #  imposing j>= i
                    continue
                k = -i - j
                if(map.containsKey(k)):
                    if(j > k) continue #  imposing k >= j order
                    size = map.get(k)
                    if(((k == j)&& size == 1) ||            #  since k >= j >= i 
                       ((k == i && i == j) && size == 2)) #  deduplication 
                        continue
                    res.add(Arrays.asList(i,j,k))
        return res
```
Python
```python
class Solution(object):
    def threeSum(self, A):
        """
 :type A: List[int]
 :rtype: List[List[int]]
 """
        # time O(n^2), space O(1)
        if not A: return []
        n, m = len(A), collections.defaultdict(int) # :x:A.count(x) for x in A #dict(collections.Counter(A)) 
        for num in A: m[num]+=1
        return [[i, j, -i-j] for i in m.keys() 
            for j in m.keys() if (j > i or (i == j and m[i] > 1)) 
            and ((-i -j) in m )
            and ((-i-j)>= j)
            and (m[(-i-j)] > 2 or m[(-i-j)] == 1 and (-i-j)!=j or m[(-i-j)] == 2 and ((-i-j)!=i or (-i-j)!=j))]
```
 [code 2: two pointer]:
 O(n^2) without extra space (ordered_map)
```python
class Solution :
    public List<List<Integer>> threeSum(int[] A) :
        Arrays.sort(A)
        List<List<Integer>> res = new LinkedList()
        n = A.length
        for(i = 0 i < n - 2  i++):
            if(i == 0 || A[i] != A[i-1]):
                j = i + 1, k = n - 1
                while(j < k):
                    if(A[i] + A[j] + A[k] == 0):
                        res.add(Arrays.asList(A[i], A[j], A[k]))
                        #  deduplication
                        while(j < k && A[j] == A[j + 1]) j ++
                        while(j < k && A[k] == A[k - 1]) k --
                        j++ k--
                    else if(A[i] + A[j] + A[k] < 0) j++
                    else k --
        return res
```
 Variation: Expand sum to be 0 as in general case
```python
class Solution :
    vector<vector<int>>answer
public:
    vector<vector<int>> threeSum(vector<int>& A, target) :
        len = A.size()
        if (len < 3) return answer
        #  sort the vector
        sort(A.begin(), A.end())
        for(i = 0 i < len i++):
            left = i + 1, right = len - 1, twoSumTarget = target - A[i] #  THE ONLY DIFFERENCE!
            #  treat as two sum using two pointers
            while(left < right):
            #  speed up two sum runtime by removing two sum search for duplicated target value 
            #  while(i > 0 && A[i] == A[i-1]) i++ 
            #  alternatively, you can write :
            if(i>0 && A[i] == A[i-1]) continue
            # at the beginning of the for loop
                sum = A[left] + A[right]
                if( sum == twoSumTarget ):
                    answer.push_back(:A[i], A[left],A[right])
                    #  speed up two sum search runtime by removing duplicates 
                    left++
                    right--
                    while(left < right && A[left] == A[left-1]) left++ #  you may not need "left<right"
                    # here in C++
                    while(left < right && A[right] == A[right+1])right-- #  you may not need "left<right" 
                    # here in C++
                else if (sum < twoSumTarget ):
                    left ++
                else:
                    right--
        return answer
```
 Special thanks: 洗刷刷 for the reference!
------------------------------------------------------------------------------------------------
 18. 4Sum
============
 18. 4Sum
==========
 Given an array
 ---S of n integers, are there elements a,b,c,--- 
 and
 ---d in S such that--- 
 a+b+c+d = target? Find all unique quadruplets in the array which gives the sum of target.
 Note:
 The solution set must not contain duplicate quadruplets.
```
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```
 Thoughts
 :
1. Naive way: break down problems into
 3Sum
 ->
 Two Sum
  In general: for sum, use recursion to break down to (k-1)->(k-2) until reaching 2, which is solved using the algorithm for two Sum
2. Since we need
 ALL
 solutions, tricks for removing duplicates, as adopted in
 3Sum
 is also adopted.
3. When k > 2, I prefer using two pointers as the time complexities is no longer dominant by sorting (O(nlogn)).
```python
public class Solution :
public List<List<Integer>> fourSum(int[] num, target) :
    ArrayList<List<Integer>> ans = new ArrayList<>()
    if(num.length<4)return ans
    Arrays.sort(num)
    for(i=0 i<num.length-3 i++):
        if(num[i]+num[i+1]+num[i+2]+num[i+3]>target)break # first candidate too large, search finished
        if(num[i]+num[num.length-1]+num[num.length-2]+num[num.length-3]<target)continue # first candidate too small
        if(i>0&&num[i]==num[i-1])continue # deduplicates
        for(j=i+1 j<num.length-2 j++):
            if(num[i]+num[j]+num[j+1]+num[j+2]>target)break # second candidate too large
            if(num[i]+num[j]+num[num.length-1]+num[num.length-2]<target)continue # second candidate too small
            if(j>i+1&&num[j]==num[j-1])continue # prevents duplicate results in ans list
            low=j+1, high=num.length-1
            while(low<high):
                sum=num[i]+num[j]+num[low]+num[high]
                if(sum==target):
                    ans.add(Arrays.asList(num[i], num[j], num[low], num[high]))
                    while(low<high&&num[low]==num[low+1])low++ # skipping over duplicate on low
                    while(low<high&&num[high]==num[high-1])high-- # skipping over duplicate on high
                    low++ 
                    high--
                # move window
                else if(sum<target)low++ 
                else high--
    return ans
```
 Special thanks: 洗刷刷 for the reference!
------------------------------------------------------------------------------------------------
 721. Accounts Merge
=======================
 Given a list
 `accounts` 
 , each element
 `accounts[i]` 
 is a list of strings, where the first element
 `accounts[i][0]` 
 is a name, and the rest of the elements are emails representing emails of the account.
 Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
 After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails
 in sorted order
 . The accounts themselves can be returned in any order.
 Example 1:
```
Input:
accounts = [["John", "[email protected]", "[email protected]"], ["John", "[email protected]"], ["John", "[email protected]", "[email protected]"], ["Mary", "[email protected]"]]
Output:
 [["John", '[email protected]', '[email protected]', '[email protected]'],  ["John", "[email protected]"], ["Mary", "[email protected]"]]
Explanation:
The first and third John's are the same person as they have the common email "[email protected]".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', '[email protected]'], ['John', '[email protected]'], 
['John', '[email protected]', '[email protected]', '[email protected]']] would still be accepted.
```
 Note:
 The length of
 `accounts` 
 will be in the range
 `[1, 1000]` 
 .
 The length of
 `accounts[i]` 
 will be in the range
 `[1, 10]` 
 .
 The length of
 `accounts[i][j]` 
 will be in the range
 `[1, 30]` 
 .
 Thoughts:
1. Use Union-Find: since
 the goal is to grouping emails whenever there is a connected path (common emails are analogous to shared nodes in the graph)
2. similar idea can applies to DFS: to group accounts by traversing the connected graph
 Code: T: O(V + E) S: O(V + E)
```python
class Solution :
    public List<List<String>> accountsMerge(List<List<String>> accounts) :
        #  initialize the union find & owner info
        Map<String, String> parent = new HashMap<>() #  Map<String, Integer> rank = new HashMap<>()
        Map<String, TreeSet<String>> union = new HashMap<>()
        for(List<String> a: accounts):
            for (i = 1 i < a.size() ++i):
                parent.put(a.get(i), a.get(i))
               #  rank.put(a.get(i), 0)
        for(List<String> a: accounts):
            String p = find(a.get(1), parent)
            #  merge the emails accounts
            for(i = 2 i < a.size() ++i):
                String pi = find(a.get(i), parent)
                #  union
                #  by rank
                #  if(rank.get(pi) > rank.get(p)):
                #  String tmp = pi
                #  pi = p
                #  p = tmp
                #  
                #  inc = rank.get(pi) == rank.get(p)?1:0
                #  rank.put(p, rank.get(p) + inc)
                parent.put(pi, p)
        #  build the union where union<represented email, set of email accounts>
        for(List<String> a: accounts):
            String p = find(a.get(1), parent)
            if(!union.containsKey(p)) :
                union.put(p, new TreeSet<>())
                union.get(p).add(a.get(0))#  add name first
            for(i = 1 i < a.size() ++i):
                union.get(p).add(a.get(i)) 
        List<List<String>> res = new ArrayList<>()
        for(String p : union.keySet()):
            List<String> email = new ArrayList<>(union.get(p))
            res.add(email)
        return res
    private String find(String q, Map<String, String> parent):
        while(parent.get(q) != q):
            #  path compression
            #  parent.put(q, parent.get(parent.get(q)))
            q = parent.get(q)
        return q
```
------------------------------------------------------------------------------------------------
 211. Add and Search Word - Data structure design
====================================================
 Design a data structure that supports the following two operations:
```
void addWord(word)
bool search(word)
```
 search(word) can search a literal word or a regular expression string containing only letters
 `a-z` 
 or
 `.` 
 . A
 `.` 
 means it can represent any one letter.
 Example:
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") ->false
search("bad") ->true
search(".ad") ->true
search("b..") ->true
```
 FB follow up: process "*"
 Thoughts:
1. Trie Tree excercise
```python
class WordDictionary :
    private TrieNode root 
    /** Initialize your data structure here. */
    public WordDictionary() :
        root = new TrieNode()
    /** Adds a word into the data structure. */
    public void addWord(String word) :
        TrieNode node = root
        for (char c: word.toCharArray()):
            if(node.children[c - 'a'] == null):
                node.children[c - 'a'] = new TrieNode()
            node = node.children[c - 'a']
        node.val = word
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) :
        return match(word, 0, root)
    private boolean match(String word, depth, TrieNode node):
        if(depth == word.length()) return !node.val.equals("")
        if(word.charAt(depth) != '.'):
            return (node.children[word.charAt(depth) - 'a'] != null && match(word, depth + 1, node.children[word.charAt(depth) - 'a'] ))
        else:
            for (i = 0 i < node.children.length i++):
                if(node.children[i] != null && match(word, depth + 1, node.children[i]))
                    return true
        return false
class TrieNode:
        public TrieNode [] children = new TrieNode[26]
        public String val = ""
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary()
 * obj.addWord(word)
 * boolean param_2 = obj.search(word)
 */
```
Python
```python
class WordDictionary(object):
    def __init__(self):
        """
 Initialize your data structure here.
 """
        self.root = TrieNode()
    def addWord(self, word):
        """
 Adds a word into the data structure.
 :type word: str
 :rtype: void
 """
        node = self.root
        for s in word:
            if s not in node.child:
                node.child[s] = TrieNode()
            node = node.child[s]
        node.val = word
    def search(self, word):
        """
 Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
 :type word: str
 :rtype: bool
 """
        def match(word, depth, node):
            if depth == len(word): return not (node.val=='')
            if word[depth] != '.':
                return word[depth] in node.child and match(word, depth + 1, node.child[word[depth]])
            else:
                for c in node.child:
                    if match(word, depth+1, node.child[c]):
                        return True
            return False
        return match(word, 0, self.root)
class TrieNode(object):
    def __init__(self):
        self.child = :
        self.val = ""
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
 Python: length based dictionary: psudu- O(1) - O(n)-> for char level: O(len(char in table entry))
```python
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)
    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else: # if no break in previous for loop
                return True
        return False
```
 Python: best Trie Implementation: T: O(len(total words)) S: O(len(total words))
```python
class WordDictionary(object):
    def __init__(self):
        """
 Initialize your data structure here.
 """
        self.root = TrieNode()
    def addWord(self, word):
        """
 Adds a word into the data structure.
 :type word: str
 :rtype: void
 """
        node = self.root
        for s in word:
            if s not in node.child:
                node.child[s] = TrieNode()
            node = node.child[s]
        node.val = True
    def search(self, word):
        """
 Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
 :type word: str
 :rtype: bool
 """
        def match(word, node):
            for i, c in enumerate(word):
                if c == '.':
                    for s in node.child:
                        if match(word[i + 1:], node.child[s]):
                            return True
                    return False #!
                elif c not in node.child:
                    return False
                node = node.child[c]
            return node.val
        return match(word, self.root)
class TrieNode(object):
    def __init__(self):
        self.child = :
        self.val = False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
------------------------------------------------------------------------------------------------
 67. Add Binary
==================
 Given two binary strings, return their sum (also a binary string).
 The input strings are both
 non-empty
 and contains only characters
 `1` 
 or
 `0` 
 .
 Example 1:
```
Input: a = "11", b = "1"
Output: "100"
```
 Example 2:
```
Input: a = "1010", b = "1011"
Output: "10101"
```
 Thoughts: Carry ripple adder
```python
class Solution :
    #  carry ripple adder
    public String addBinary(String a, String b) :
        StringBuilder sb = new StringBuilder()
        i = a.length() - 1, j = b.length() - 1, carry = 0
        while(i >= 0 || j >= 0):
            sum = carry
            if(i>=0) sum += a.charAt(i--) - '0'
            if(j>=0) sum += b.charAt(j--) - '0'
            sb.append(sum % 2)
            carry = sum / 2
        if(carry > 0 ) sb.append(carry)
        return sb.reverse().toString()
```
 Python:
```python
class Solution(object):
    def addBinary(self, a, b):
        """
 :type a: str
 :type b: str
 :rtype: str
 """
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            total = carry
            if i >= 0: 
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(`total % 2`)
            carry = total / 2
        if carry:
            res.append(`carry`)
        return "".join(res)[::-1]
```
------------------------------------------------------------------------------------------------
 415. Add Strings
====================
 Given two non-negative integers
 `num1` 
 and
 `num2` 
 represented as string, return the sum of
 `num1` 
 and
 `num2` 
 .
 Note:
1. The length of both
 `num1` 
 and
 `num2` 
 is < 5100.
2. Both
 `num1` 
 and
 `num2` 
 contains only digits
 `0-9` 
 .
3. Both
 `num1` 
 and
 `num2` 
 does not contain any leading zero.
4. You
 must not use any built-in BigInteger library
 or
 convert the inputs to integer
 directly.
 Code:
```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
 :type num1: str
 :type num2: str
 :rtype: str
 """
        ans, carry = [], 0 
        i, j = len(num1) - 1, len(num2) -1
        while i >= 0 or j >= 0 or carry == 1:
            a = 0 if i < 0 else ord(num1[i]) - ord('0')
            b = 0 if j < 0 else ord(num2[j]) - ord('0')
            s = a + b + carry
            ans.append(str(s % 10))
            carry = s/10
            i-=1 j-= 1
        return ''.join(ans)[::-1]
```
------------------------------------------------------------------------------------------------
 Akuna
=========
------------------------------------------------------------------------------------------------
 432. All O`one Data Structure
=================================
 Implement a data structure supporting the following operations:
1. Inc(Key) - Inserts a new keywith value 1. Or increments an existing key by 1. Key is guaranteed to be a
 non-empty
 string.
2. Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a
 non-empty
 string.
3. GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string
 `""` 
 .
4. GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string
 `""` 
 .
 Challenge: Perform all these in O(1) time complexity.
 Thoughts:
1. Inc, Dec (key) O(1) -> Map(key, val)
2. getMaxKey(), getMinKey() O(1): doubly LinkedList with head and tail bucketNode (each bucket contains key with the same count value)
 Code
 
```python
class AllOne :
    private class BucketNode:
        val
        BucketNode count
        BucketNode pre
        BucketNode next
        Set<String> keySet
        private BucketNode(val):
            this.val = val
            keySet = new HashSet<>()
    private BucketNode head
    private BucketNode tail
    private Map<String, Integer> keyValueMap
    private Map<Integer, BucketNode> valueBucketMap
    /** Initialize your data structure here. */
    public AllOne() :
         head = new BucketNode(Integer.MIN_VALUE)
         tail = new BucketNode(Integer.MAX_VALUE)
         keyValueMap  = new HashMap<>()
         valueBucketMap = new HashMap<>()
         #  link head and tail
         head.next = tail
         tail.pre = head
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    public void inc(String key) :
        if(keyValueMap.containsKey(key)):
            changeValue(key, 1)            
        else:
            if(head.next.val != 1):
                addBucketAfter(new BucketNode(1),head)
            head.next.keySet.add(key)
            #  add the mapping
            keyValueMap.put(key, 1)
            valueBucketMap.put(1, head.next)
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    public void dec(String key) :
        if(keyValueMap.containsKey(key)):
            if(keyValueMap.get(key) == 1):
                #  remove key from KV map
                keyValueMap.remove(key)
                #  remove key from Bucket
                removeKeyfromBucket(valueBucketMap.get(1), key)
            else:
                changeValue(key, -1)
    /** Returns one of the keys with maximal value. */
    public String getMaxKey() :
        return tail.pre == head? "": (String)tail.pre.keySet.iterator().next()
    /** Returns one of the keys with Minimal value. */
    public String getMinKey() :
        return head.next == tail? "": (String)head.next.keySet.iterator().next()
    private void changeValue(String key, offset):
        curVal = keyValueMap.get(key)
        BucketNode curBucket = valueBucketMap.get(curVal)
        BucketNode newBucket
        if(valueBucketMap.containsKey(curVal + offset)):
            newBucket = valueBucketMap.get(curVal + offset)
        else:
            newBucket = new BucketNode(curVal + offset)
            addBucketAfter(newBucket, offset == 1 ?curBucket: curBucket.pre)
            valueBucketMap.put(curVal + offset, newBucket)
        #  remove the key from curBucket
        removeKeyfromBucket(curBucket, key)
        #  add the key to newBucket
        newBucket.keySet.add(key)
        #  update the record
        keyValueMap.put(key, curVal + offset)
    private void addBucketAfter(BucketNode newBucket, BucketNode pre):
        newBucket.pre = pre
        newBucket.next = pre.next
        pre.next.pre = newBucket
        pre.next = newBucket
    private void removeKeyfromBucket(BucketNode bucket, String key):
        #  remove key from bucket
        bucket.keySet.remove(key)
        if(bucket.keySet.size() == 0):
            removeBucketfromBucketList(bucket)
            valueBucketMap.remove(bucket.val)
    private void removeBucketfromBucketList(BucketNode bucket):
        bucket.pre.next = bucket.next
        bucket.next.pre = bucket.pre
        bucket.pre = null
        bucket.next = null
/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * String param_3 = obj.getMaxKey()
 * String param_4 = obj.getMinKey()
 */
```
------------------------------------------------------------------------------------------------
 Arrays
==========
------------------------------------------------------------------------------------------------
 8. String to Integer (Atoi)
===============================
 Implement
 `atoi` 
 which converts a string to an integer.
 The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
 The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
 If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
 If no valid conversion could be performed, a zero value is returned.
 Note:
* Only the space character
 `' '` 
 is considered as whitespace character.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
 Example 1:
```
Input: "42"
Output: 42
```
 Example 2:
```
Input: " -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```
 Example 3:
```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```
 Example 4:
```
Input:
 "words and 987"
Output:
 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```
 Example 5:
```
Input:
 "-91283472332"
Output:
 -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
```
 Thoughts:
1. First jump all the ' ' until if there is a sign ('+' or '-'), then for all the numbers:
	1. check if current value is val > MAX_INT/10 or val == MAX_INT/10 and current value is > 7 (2147483647 is the MAXINT and -2147483648 is the INT_MIN). If sign is 1 output MAXINT otherwise output MININT
	2. update the value by val = 10 * val + (str[i] -'0')
	3. return sign * base
 Code
```python
class Solution :
public:
    myAtoi(string str) :
        sign = 1, val = 0, i = 0
        while(str[i]== ' ') i++
        if(str[i] == '+' or str[i]=='-'):
            sign = 1- 2*((str[i++] == '-'))
        while(str[i] >= '0' and str[i] <='9'):
            if(val > INT_MAX/10 or (val == INT_MAX/10 and str[i] - '0' > 7)):
                if (sign == 1) return INT_MAX
                else return INT_MIN
            val = 10 * val + (str[i++] - '0')
        return sign * val
```
------------------------------------------------------------------------------------------------
 Backpack problem
====================
 Source:
 [LintCode] Backpack I II III IV V VI [背包六问]
 https:# segmentfault.com/a/1190000006325321
------------------------------------------------------------------------------------------------
 BackTracking
================
 This structure might apply to many other backtracking questions, but here I am just going to demonstrate Subsets, Permutations, and Combination Sum.
 Subsets :
 https:# leetcode.com/problems/subsets/
```python
public List<List<Integer>> subsets(int[] A) :
    List<List<Integer>> list = new ArrayList<>()
    Arrays.sort(A)
    backtrack(list, new ArrayList<>(), A, 0)
    return list
private void backtrack(List<List<Integer>> list , List<Integer> tempList, [] A, start):
    list.add(new ArrayList<>(tempList))
    for(i = start i < A.length i++):
        tempList.add(A[i])
        backtrack(list, tempList, A, i + 1)
        tempList.remove(tempList.size() - 1)
```
 Subsets II (contains duplicates) :
 https:# leetcode.com/problems/subsets-ii/
```python
public List<List<Integer>> subsetsWithDup(int[] A) :
    List<List<Integer>> list = new ArrayList<>()
    Arrays.sort(A)
    backtrack(list, new ArrayList<>(), A, 0)
    return list
private void backtrack(List<List<Integer>> list, List<Integer> tempList, [] A, start):
    list.add(new ArrayList<>(tempList))
    for(i = start i < A.length i++):
        if(i > start && A[i] == A[i-1]) continue #  skip duplicates
        tempList.add(A[i])
        backtrack(list, tempList, A, i + 1)
        tempList.remove(tempList.size() - 1)
```
 Permutations :
 https:# leetcode.com/problems/permutations/
```python
public List<List<Integer>> permute(int[] A) :
   List<List<Integer>> list = new ArrayList<>()
   #  Arrays.sort(A) #  not necessary
   backtrack(list, new ArrayList<>(), A)
   return list
private void backtrack(List<List<Integer>> list, List<Integer> tempList, [] A):
   if(tempList.size() == A.length):
      list.add(new ArrayList<>(tempList))
    else:
      for(i = 0 i < A.length i++): 
         if(tempList.contains(A[i])) continue #  element already exists, skip
         tempList.add(A[i])
         backtrack(list, tempList, A)
         tempList.remove(tempList.size() - 1)
```
 Permutations II (contains duplicates) :
 https:# leetcode.com/problems/permutations-ii/
```python
public List<List<Integer>> permuteUnique(int[] A) :
    List<List<Integer>> list = new ArrayList<>()
    Arrays.sort(A)
    backtrack(list, new ArrayList<>(), A, new boolean[A.length])
    return list
private void backtrack(List<List<Integer>> list, List<Integer> tempList, [] A, boolean [] used):
    if(tempList.size() == A.length):
        list.add(new ArrayList<>(tempList))
     else:
        for(i = 0 i < A.length i++):
            if(used[i] || i > 0 && A[i] == A[i-1] && !used[i - 1]) continue
            used[i] = true 
            tempList.add(A[i])
            backtrack(list, tempList, A, used)
            used[i] = false 
            tempList.remove(tempList.size() - 1)
```
 Combination Sum :
 https:# leetcode.com/problems/combination-sum/
```python
public List<List<Integer>> combinationSum(int[] A, target) :
    List<List<Integer>> list = new ArrayList<>()
    Arrays.sort(A)
    backtrack(list, new ArrayList<>(), A, target, 0)
    return list
private void backtrack(List<List<Integer>> list, List<Integer> tempList, [] A, remain, start):
    if(remain < 0) return
    else if(remain == 0) list.add(new ArrayList<>(tempList))
    else: 
        for(i = start i < A.length i++):
            tempList.add(A[i])
            backtrack(list, tempList, A, remain - A[i], i) #  not i + 1 because we can reuse same elements
            tempList.remove(tempList.size() - 1)
```
 Combination Sum II (can't reuse same element) :
 https:# leetcode.com/problems/combination-sum-ii/
```python
public List<List<Integer>> combinationSum2(int[] A, target) :
    List<List<Integer>> list = new ArrayList<>()
    Arrays.sort(A)
    backtrack(list, new ArrayList<>(), A, target, 0)
    return list
private void backtrack(List<List<Integer>> list, List<Integer> tempList, [] A, remain, start):
    if(remain < 0) return
    else if(remain == 0) list.add(new ArrayList<>(tempList))
    else:
        for(i = start i < A.length i++):
            if(i > start && A[i] == A[i-1]) continue #  skip duplicates
            tempList.add(A[i])
            backtrack(list, tempList, A, remain - A[i], i + 1)
            tempList.remove(tempList.size() - 1) 
```
 Palindrome Partitioning :
 https:# leetcode.com/problems/palindrome-partitioning/
```python
public List<List<String>> partition(String s) :
   List<List<String>> list = new ArrayList<>()
   backtrack(list, new ArrayList<>(), s, 0)
   return list
public void backtrack(List<List<String>> list, List<String> tempList, String s, start):
   if(start == s.length())
      list.add(new ArrayList<>(tempList))
   else:
      for(i = start i < s.length() i++):
         if(isPalindrome(s, start, i)):
            tempList.add(s.substring(start, i + 1))
            backtrack(list, tempList, s, i + 1)
            tempList.remove(tempList.size() - 1)
public boolean isPalindrome(String s, low, high):
   while(low < high)
      if(s.charAt(low++) != s.charAt(high--)) return false
   return true
```
------------------------------------------------------------------------------------------------
 110. Balanced Binary Tree
=============================
 Given a binary tree, determine if it is height-balanced.
 For this problem, a height-balanced binary tree is defined as:
> 
> 
>  a binary tree in which the depth of the two subtrees of _every _node never differ by more than 1.
>  
> 
> 
> 
 Example 1:
 Given the following tree
 `[3,9,20,null,null,15,7]` 
 :
```
    3
   / \
  9  20
    /  \
   15   7
```
 Return true.
 Example 2:
 Given the following tree
 `[1,2,2,3,3,null,null,4,4]` 
 :
```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```
 Return false.
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public boolean isBalanced(TreeNode root) :
        return isBalancedHelper(root) != -1
    private isBalancedHelper(TreeNode root):
        if (root == null) return 0
        left = isBalancedHelper(root.left)
        right = isBalancedHelper(root.right)
        if (left == -1 || right== -1|| Math.abs(left - right) > 1) return -1
        return Math.max(left, right) + 1 
```
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
# class Solution :
# public boolean isBalanced(TreeNode root) :
# return isBalancedHelper(root) != -1
# 
# private isBalancedHelper(TreeNode root):
# if (root == null) return 0
# left = isBalancedHelper(root.left)
# right = isBalancedHelper(root.right)
# if (left == -1 || right== -1|| Math.abs(left - right) > 1) return -1
# return Math.max(left, right) + 1 
# 
# 
class Solution(object):
    def isBalanced(self, root):
        """
 :type root: TreeNode
 :rtype: bool
 """
        def helper(root):
            if not root: return 0
            left, right = helper(root.left), helper(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1: return -1
            return max(left, right) + 1
        return helper(root) != -1
```
------------------------------------------------------------------------------------------------
 122. Best Time to Buy and Sell Stock II
===========================================
 Say you have an array for which the
 ---i_thelement is the price of a given stock on day_i--- 
 .
 Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
 Note:
 You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
 Example 1:
```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```
 Example 2:
```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```
 Example 3:
```
Input: [7,6,4,3,1]
Output: 0
Explanation:  In this case, no transaction is done, i.e. max profit = 0.
```
 Thoughts:
1. Greedy buy today's stock if tomorrow it will increase its price
 Code
```python
class Solution(object):
    def maxProfit(self, prices):
        """
 :type prices: List[int]
 :rtype: int
 """
        profit = 0
        for i, p in enumerate(prices[:-1]):
            if prices[i + 1] > p:
                profit += prices[i + 1] - p
        return profit
```
 Code: One line
```python
class Solution(object):
    def maxProfit(self, prices):
        """
 :type prices: List[int]
 :rtype: int
 """
        return sum([b - a if b > a else 0 for a, b in zip(prices, prices[1:])])
```
------------------------------------------------------------------------------------------------
 123. Best Time to Buy and Sell Stock III
============================================
 Say you have an array for which the
 ---i_thelement is the price of a given stock on day_i--- 
 .
 Design an algorithm to find the maximum profit. You may complete at most_two_transactions.
 Note:
 You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
 Example 1:
```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```
 Example 2:
```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```
 Example 3:
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```
 Thoughts:
1. DP
2. DP optimization: only tracking 4 variables:
3. Inspired from
 here
 Code: DP:
```python
class Solution :
    public maxProfit(int[] prices) :
    #  these four variables represent your profit after executing corresponding transaction
    #  in the beginning, your profit is 0. 
    #  when you buy a stock ,the profit will be deducted of the price of stock.
    firstBuy = Integer.MIN_VALUE, firstSell = 0
    secondBuy = Integer.MIN_VALUE, secondSell = 0
        for (curPrice : prices) :
            if (firstBuy < -curPrice) firstBuy = -curPrice #  the max profit after you buy first stock
            if (firstSell < firstBuy + curPrice) firstSell = firstBuy + curPrice #  the max profit after you sell it
            if (secondBuy < firstSell - curPrice) secondBuy = firstSell - curPrice #  the max profit after you buy the second stock
            if (secondSell < secondBuy + curPrice) secondSell = secondBuy + curPrice #  the max profit after you sell the second stock
        return secondSell #  secondSell will be the max profit after passing the prices
```
 Code: DP Optimization
```python
class Solution(object):
    def maxProfit(self, prices):
        """
 :type prices: List[int]
 :rtype: int
 """
        hold1 = hold2 = -sys.maxint - 1 # INT.MIN_VAL
        sell1 = sell2 = 0
        # Assume we only have 0 money at first
        for p in prices: 
            sell2 = max(sell2, hold2 + p) # The maximum if we've just sold 2nd stock so far.
            hold2 = max(hold2, sell1 - p) # The maximum if we've just buy 2nd stock so far.
            sell1 = max(sell1, hold1 + p) # The maximum if we've just sold 1nd stock so far.
            hold1 = max(hold1, -p)        # The maximum if we've just buy 1st stock so far. 
        return sell2
```
------------------------------------------------------------------------------------------------
 121. Best Time to Buy and Sell Stock
========================================
 121. Best Time to Buy and Sell Stock
======================================
 Say you have an array for which the
 ---ith--- 
 element is the price of a given stock on day i.
 If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
 Example 1:
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
```
 Example 2:
```
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
```
 Code
```python
class Solution :
public:
    maxProfit(vector<int>& prices) :
         low = INT_MAX
         max_profit = 0
         for (p: prices):
             if(p <= low) low = p 
             else max_profit = p - low > max_profit? p - low: max_profit
        return max_profit
```
------------------------------------------------------------------------------------------------
 BFS/DFS
===========
------------------------------------------------------------------------------------------------
 173. Binary Search Tree Iterator
====================================
 Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
 Calling
 `next()` 
 will return the next smallest number in the BST.
 Note:
 `next()` 
 and
 `hasNext()` 
 should run in average O(1) time and uses O(h) memory, wherehis the height of the tree.
 Credits:
 Special thanks to
 @ts
 for adding this problem and creating all test cases.
 Thoughts:
1. Using stack to record path.
2. When initialized, traverse to the leftmost
3. when retrieving, pop out from the stack and use its right child (if it does have) as a root node to put more nodes in front of the stack (In order traversal)
 Code Python T:O(1) S:O(h)
```
# Definition for a binary tree node
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class BSTIterator(object):
    def __init__(self, root):
        """
 :type root: TreeNode
 """
        self.stack = []
        cur = root
        while cur is not None:
            self.stack.append(cur)
            if cur.left:
                cur = cur.left
            else:
                break
        # print("len(self.stack) %s" %(len(self.stack)))
    def hasNext(self):
        """
 :rtype: bool
 """
        return self.stack
    def next(self):
        """
 :rtype: int
 """
        if not self.stack: return None
        ans = self.stack.pop() 
        cur = ans
        # check whether there is a right child, if there is, traverse towards the leftmost 
        # of the right child.
        if cur.right:
            cur = cur.right
            while cur:
                self.stack.append(cur)
                if cur.left:
                    cur = cur.left
                else: 
                    break
        return ans.val
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
```
 from
 siyang2
 's
 post
------------------------------------------------------------------------------------------------
 Binary Search
=================
1. Finding the first and last appearance:
	1. Setting the i <= j:
	2. Exclude left sliding through (find the first appearance): left = mid - 1 (include "=", return right in the end)
	3. Exclude right sliding through (find the last appearance): right = mid + 1 (include "=", return left in the end)
	4. if search value: i<=j should care that the terminal index is
	 not the answer if the target falls out of range of the search space
2. Find peak element:
	1. Finding
	 two mid points: mid, mid + 1, compare:
	2. if num[mid1] < A[mid2[: low = mid2
	3. else high = mid1
3. Trail and test (adopting 1)
	1. for certain criteria: if >=: l slide through mid to mid +1, return r (or <= r slide thorugh to mid -1, return l)
4. Search value in a rotated sorted array (
 distinct
 ):
	1. if A[mid] hits the value. return the mid index
	2. Find the continuous
	 increasing
	 part (whether A[i] < A[mid], or >, slide thru to mid+1 if ==.
	3. Comparing whether targets fall into the continuous part:
		1. A[i] < A[mid]: if A[i] <= target < A[mid]: assign
		 j = mid - 1
		 else assign i = mid + 1 (go to the discontinuous part)
		2. A[i] > A[mid] (right part continuous): if A[mid] < target <= A[j]: assign
		 i = mid + 1
		 else assign j = mid - 1
		3. A[i] == A[mid] : just sliding through to i = mid + 1 since A[mid] != target
	4. return -1 (if search failed)
5. Search value in a rotated sorted array (
 duplicates
 )
	1. only difference: handling cases of == among A[i]. A[j], A[mid]:
	 if A[i] == A[mid] == A[j]: move both i and j. (i++/j--) else if only A[i] == A[mid]: i sliding through to mid + 1: i = mid + 1.
	 In this case, leaving no space for A[i] == A[mid]
	2. Only leave cases where: A[i] < A[mid] (test A[i] <= target < A[mid]) or A[i] > A[mid] (test A[mid] < target <= A[j])
6. Find minimum in a rotated sorted array:
	1. Assumption: exists, no duplicates
		1. selecting right as the comparison A[mid[ vs A[right] because natually the number increases from left to the right -> if A[mid] > A[right] -> there MUST BE a pivot on (mid, right] so we can throw our left and directly go left = mid + 1. We cannot draw similar conclusion on the left since if A[mid] > A[left] : we cannot infer there is a pivot in [left, mid).
	2. Assumption: exists,
	 DUPLICATES:
		1. similar to case before: except handling the duplicates: if (A[mid] == A[right]) right-= 1
7. Find first and last position
	1. M1: search a float point approach: search (target - 0.5) and (target+ 0.5) instead: found the first upper bound for query value
	2. Standard solution:
		1. Search for the first appearance:
			1. Condition: i < j -> (so check [i]([j])) in the end
			2. mid = (i + j) /2 i = mid + 1 j = mid
		2. Search for the last appearance
			1. Condition i < j without check since already checked
			2. mid =
			 (i + j + 1) /2 since we need to preserve the mid from the left if A[mid] == target -> i = mid -> we need to bias the mid to the right to prevent being stuck.
8. Search in a 2D partial ordering:
	1. Use
	 Trail and Error to find the upper bound (number that are <= than [mid]) in order to deal with duplicates. for each search:
	2. Start with "middle" point: the point that has the largest value in one dim and least value in another dim. (This helps opt out less optimal solution after the comparison)
	3. With Heap: Maintaining n candidates: initialized by the first column: Each time a value pops out, add in its "children" the value at the same column index but at the next row (if there is)
9. Search in a window: (Find k closest)
	1. Find the optimal starting point i that
	 [i] < [i + k]
	2.
------------------------------------------------------------------------------------------------
 94. Binary Tree Inorder Traversal
=====================================
 94. Binary Tree Inorder Traversal
===================================
 Given a binary tree, return theinordertraversal of its nodes' values.
 For example:
 Given binary tree
 `[1,null,2,3]` 
 ,
```
   1
    \
     2
    /
   3
```
 return
 `[1,3,2]` 
 .
 Note:
 Recursive solution is trivial, could you do it iteratively?
 Trivial Solution: According to the definition of Inorder (O(n) time and O(n) space, for the function call stack)
```python
class Solution :
    vector<int> answer
public:
    vector<int> inorderTraversal(TreeNode* root) :
        inorderTraversalHelper(root)
        return answer        
    void inorderTraversalHelper(TreeNode * root):
        if(!root) return
        inorderTraversalHelper(root->left)
        answer.push_back(root->val)
        inorderTraversalHelper(root->right)
```
 Thoughts
1. Using Stack to keep track path
2. *Morris traversal
 Code
 Using Stack: (O(n) time and O(n) space)
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    stack<TreeNode *> path
    vector<int> answer
public:
    vector<int> inorderTraversal(TreeNode* root) :
        traverse(root)
        return answer
    void traverse(TreeNode* cur):
        while(cur || !path.empty()):
            #  first to the left
            while(cur):
                path.push(cur)
                cur = cur -> left
            #  left done , do cur
            cur = path.top() path.pop()
            answer.push_back(cur->val)
            #  exploring right
            cur = cur->right
```
 Code with
 Morris Traversal
 : O(n) time and O(1) space (two assisting pointers)!
 psudo-code (Thanks
 monkeykingyan
 's
 solution
 )
```
Step1. Initialize current as root
Step2. While current is not NULL
  If current does not have left child
  a. Add current’s value
  b. Go to the right, i.e., current = current.right
 Else
  a. In current's left subtree, make current the right child of the rightmost node
  b. Go to this left child, i.e., current = current.left
```
 Code
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector<int> inorderTraversal(TreeNode* root) :
        vector<int> answer
        TreeNode *cur = root 
        while(cur):
            if(cur->left):
                TreeNode* pre = cur -> left
                while(pre -> right) pre = pre -> right
                pre->right = cur
                TreeNode * temp = cur
                cur = cur -> left
                temp -> left = NULL
            else:
                answer.push_back(cur->val)
                cur = cur -> right
         return answer
```
 Talonj @ Stackoverflow
 explaination:
 Special Thanks
 jianchaolifighter
 for the
 reference
------------------------------------------------------------------------------------------------
 107. Binary Tree Level Order Traversal
==========================================
 107. Binary Tree Level Order Traversal II
===========================================
 Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
 For example:
 Given binary tree
 `[3,9,20,null,null,15,7]` 
 ,
```
    3
   / \
  9  20
    /  \
   15   7
```
 return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```
 Thoughts: BFS + Adding in front (vector insert / deque push_front)
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    vector<vector<int>> answer
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) :
        queue<TreeNode*> q
        q.push(root)
        while(!q.empty()):
            len = q.size()
            vector<int> level
            for(i = 0  i < len i++):
                TreeNode * curNode = q.front() q.pop()
                if(!curNode) continue 
                level.push_back(curNode->val)
                q.push(curNode->left)
                q.push(curNode->right)
                if(!level.empty()) answer.insert(answer.begin(),level)
        return answer
```
------------------------------------------------------------------------------------------------
 124. Binary Tree Maximum Path Sum
=====================================
 124. Binary Tree Maximum Path Sum (any node to any node)
==========================================================
 Given a binary tree, find the maximum path sum.
 For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain
 at least one node
 and does not need to go through the root.
 For example:
 Given the below binary tree,
```
       1
      / \
     2   3
```
 Return
 `6` 
 .
 Thoughts:
 in top down order, for each node do:
1. calculate the current path sum, update the record
2. pass the larger branched sum value to the parent
 Code:
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    answer
public:
    maxPathSum(TreeNode* root) :
        answer = INT_MIN
        maxPathSumDown(root)   
        return answer
    maxPathSumDown(TreeNode * cur):
        if(!cur) return 0
        left = max(0, maxPathSumDown(cur->left))
        right = max(0, maxPathSumDown(cur->right))
        answer = max(answer, left + right + cur ->val)
        return max(left, right) + cur->val
```
 Code
 without global variable
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    answer
public:
    maxPathSum(TreeNode* root) :
        answer = INT_MIN
        maxPathSumDown(root)   
        return answer
    maxPathSumDown(TreeNode * cur):
        if(!cur) return 0
        left = max(0, maxPathSumDown(cur->left))
        right = max(0, maxPathSumDown(cur->right))
        answer = max(answer, left + right + cur ->val)
        return max(left, right) + cur->val
```
 Code (Python)
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    maxVal = float("-inf")
    def maxPathSum(self, root):
        """
 :type root: TreeNode
 :rtype: int
 """
        self.maxPathDown(root)
        return self.maxVal 
    def maxPathDown(self, cur):
        if not cur: 
            return 0
        left = max(0, self.maxPathDown(cur.left))
        right = max(0, self.maxPathDown(cur.right))
        self.maxVal = max(self.maxVal, left + right + cur.val)
        return max(left, right) + cur.val
```
 Special Thanks to
 wei-bung
 for providing this
 solution
------------------------------------------------------------------------------------------------
 257. Binary Tree Paths
==========================
 Given a binary tree, return all root-to-leaf paths.
 Note:
 A leaf is a node with no children.
 Example:
```
Input:
   1
 /   \
2     3
 \
  5
Output:
 ["1->2->5", "1->3"]
Explanation:
 All root-to-leaf paths are: 1->2->5, 1->3
```
 Thoughts:
1. DFS
2. if there is no child, then append itself to the list
3. else add current root.val to every element in the returned list
 Code
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def binaryTreePaths(self, root):
        """
 :type root: TreeNode
 :rtype: List[str]
 """
        def dfs(root):
            if not root: return []
            left = dfs(root.left)
            right = dfs(root.right)
            merge = []
            merge.extend(left)
            merge.extend(right)
            ans = []
            if not merge:
                ans.append(str(root.val))    
            else:
                for s in merge:
                    ans.append(":->:".format(root.val,s))
            return ans
        return dfs(root)
```
------------------------------------------------------------------------------------------------
 145. Binary Tree Post Order Traversal
=========================================
 102. Binary Tree Postorder Traversal
======================================
 Given a binary tree, return thepostordertraversal of its nodes' values.
 For example:
 Given binary tree
 `:1,#,2,3` 
 ,
```
   1
    \
     2
    /
   3
```
 return
 `[3,2,1]` 
 .
 Note:
 Recursive solution is trivial, could you do it iteratively?
 Trivial Solution:
1. Recursion Call
2. Reverse the
 Binary Tree pre order traversal
 output
 Thoughts:
1. Using stack:
 pshizhsysu
 generalized the
 tree traversal idea
 : O(n) in time and O(n) in space
	1. For postorder traversal, we visit a node when popping it. last_pop represents the node which is popped the last time. For the top node in stack, it has three choices, pushing its left child in stack, or pushing its right child in stack, or being popped. If last_pop != top->left, meaning that its left tree has not been pushed in stack, then we push its left child. If last_pop == top->left, we push its right child. Otherwise, we pop the top node.
	2. In contrast, for
	 pre order traversal
	 , we visit a node when pushing it in stack. For
	 in order traversal
	 , we visit a node when pushing its right child in stack.
2. Always use a lastNode, the (last node added to the answer), to keep track whether cur-> right is the same as that (if it is then, we need to visit the CurNode, if it is not, then we need to first visit cur->right)
3. Morris Traversal (Adopted from
 jianchaolifighter
 's
 Solution
 ) : O(n) in time and O(1) in space
 Code 1:
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector<int> postorderTraversal(TreeNode* root) :
    vector<int>answer
    if (root == 0)
            return answer
    stack<TreeNode*> s
    s.push(root)    
    TreeNode* last_pop = root
        while (!s.empty())
        :        
            TreeNode* top = s.top()
            if (top->left && top->left != last_pop && top->right != last_pop) #  push_left
            :
                s.push(top->left)
            else if (top->right && top->right != last_pop && (!top->left || top->left == last_pop)) #  push_right
            :
                s.push(top->right)
            else #  pop
            :
                s.pop()
                last_pop = top
                #  cout << top->val << ' ' #  visit top
                answer.push_back(top -> val)
    return answer
```
 Code 1 by
 jianchaolifighter
 's
 solution
 :
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector<int> postorderTraversal(TreeNode* root) :
        vector<int> answer
        stack<TreeNode *> toVisit
        TreeNode * nodeToLeft = root
        TreeNode * lastNode = NULL #  You must assign NULL here as it will have some wired problems of not passing the 
                                    #  case of "[1,null,2]"( I guess memory leak?)
        while(nodeToLeft || !toVisit.empty()):
            if(nodeToLeft):
                toVisit.push(nodeToLeft)
                nodeToLeft = nodeToLeft -> left
            else:
                TreeNode * topNode = toVisit.top()
                if(topNode -> right && lastNode != topNode -> right) 
                    nodeToLeft = topNode -> right
                else :
                    answer.push_back(topNode->val)
                    lastNode = topNode
                    toVisit.pop()
        return answer
```
 Code 2: Morris Traversal (hard):
1. Visit left subtree find the right the rightmost tree, add a cycle to the current node - left subtree - right most point
2. Iteratively creating cycles to the left (left) , until we detect a cycle, process the answer for the left subtree using three pointers, then move to the right subtree root, repeat 2 (right).
3. right subtree root and current node are included when cycle between right subtree - root, current node - and parent is detected ( reason why to add a dummy node as the root)
```python
class Solution:
public:
    void reverseNodes(TreeNode* start, TreeNode* end) :
        #  if (start == end) return
        TreeNode* slow = start
        TreeNode* fast = start -> right
        TreeNode* fast_next
        while (slow != end) :
            fast_next = fast-> right
            #  changing right
            fast -> right = slow
            #  increment
            slow = fast
            fast = fast_next
    void reverseAddNodes(TreeNode* start, TreeNode* end, vector<int>& nodes) :
        reverseNodes(start, end)
        TreeNode* node = end
        while (true) :
            nodes.push_back(node -> val)
            if (node == start) break
            node = node -> right
        reverseNodes(end, start)
    vector<int> postorderTraversal(TreeNode* root) :
        vector<int> nodes
        TreeNode* dump = new TreeNode (0)
        dump -> left = root
        TreeNode* curNode = dump
        while (curNode) :
            if (curNode -> left) :
            TreeNode* predecessor = curNode -> left
            while (predecessor -> right && predecessor -> right != curNode)
            predecessor = predecessor -> right
            if (!(predecessor -> right)) :
                #  add right path
                predecessor -> right = curNode
                curNode = curNode -> left
            else :
                #  find a cycle, add left subtree 
                reverseAddNodes(curNode -> left, predecessor, nodes)
                #  prune cycle path, finish left subtree, switch to the right 
                predecessor -> right = NULL
                curNode = curNode -> right
            else curNode = curNode -> right
        return nodes
```
 Code 2 : Better Morris Traversal from
 Annie Kim's Blog
------------------------------------------------------------------------------------------------
 144. Binary Tree Preorder Traversal
=======================================
 144. Binary Tree Preorder Traversal
=====================================
 Given a binary tree, return thepreordertraversal of its nodes' values.
 For example:
 Given binary tree
 `[1,null,2,3]` 
 ,
```
   1
    \
     2
    /
   3
```
 return
 `[1,2,3]` 
 .
 Thoughts:
 Using Stack
 Code
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector<int> preorderTraversal(TreeNode* root) :
        stack<TreeNode *> treeSt
        vector<int> answer
        if(!root) return vector<int>()
        treeSt.push(root)
        while(!treeSt.empty()):
            TreeNode* cur = treeSt.top()
            answer.push_back(cur->val)
            treeSt.pop()
            if(cur->right)treeSt.push(cur->right)
            if(cur->left)treeSt.push(cur->left)
        return answer
```
 Code 2: Check from the pop
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    vector<int> preorderTraversal(TreeNode* root) :
        vector<int> answer
        #  if(!root) return answer
        stack<TreeNode *> treeSt
        treeSt.push(root)
        while(!treeSt.empty()):
            TreeNode* cur = treeSt.top()
            treeSt.pop()
            if (cur):
                answer.push_back(cur ->val)
                treeSt.push(cur->right)
                treeSt.push(cur->left)
        return answer
```
 Code (Python)
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def preorderTraversal(self, root):
        """
 :type root: TreeNode
 :rtype: List[int]
 """
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node: 
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
```
------------------------------------------------------------------------------------------------
 199. Binary Tree Right Side View
====================================
 199. Binary Tree Right Side View
==================================
 Given a binary tree, imagine yourself standing on the _right _side of it, return the values of the nodes you can see ordered from top to bottom.
 Example:
```
Input:
 [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```
 Thoughts:
 Recursive: Preorder traversal from right to left: record the result if curDepth ==
 ---list--- 
 .size()
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public List<Integer> rightSideView(TreeNode root) :
        List<Integer> result = new ArrayList<Integer>()
        preorder_reverse(root, result, 0)
        return result
    public void preorder_reverse(TreeNode cur, List<Integer> result, curDepth):
        if (cur == null) return
        if (result.size() == curDepth) result.add(cur.val)
        preorder_reverse(cur.right, result, curDepth + 1)
        preorder_reverse(cur.left, result, curDepth + 1)
```
 Iterative: Using queue to have a BFS (expand from left to right):
```python
class Solution :
    public List<Integer> rightSideView(TreeNode root) :
        List<Integer> result = new ArrayList()
        if(root == null)
            return result
        Queue<TreeNode> que = new LinkedList()
        que.add(root)
        while(!que.isEmpty()):
            size = que.size()
            while(size>0):
                TreeNode node = que.poll()
                if(size==1)
                    result.add(node.val)
                if(node.left != null)
                    que.add(node.left)
                if(node.right != null)
                    que.add(node.right)
                size--
        return result
```
------------------------------------------------------------------------------------------------
 314. Binary Tree Vertical Order Traversal
=============================================
 Given a binary tree, return thevertical ordertraversal of its nodes' values. (ie, from top to bottom, column by column).
 If two nodes are in the same row and column, the order should be from
 left to right
 .
 Examples 1:
```
Input:
[3,9,20,null,null,15,7]
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
```
 Examples 2:
```
Input: 
[3,9,8,4,0,1,7]
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
```
 Examples 3:
```
Input:
[3,9,8,4,0,1,7,null,null,null,2,5]
 (0's right child is 2 and 1's left child is 5)
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
```
 FB: Complexity!
 Thoughts
1. Use map <col, list<val>> to record the col and list value pair. Use BFS to expand the tree to add entry
 Code T O(V), S O(V)
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public List<List<Integer>> verticalOrder(TreeNode root) :
        List<List<Integer>> res = new ArrayList<>()
        if (root == null) return res
        Map <Integer, ArrayList<Integer>> map = new HashMap()
        Queue<TreeNode> q = new LinkedList<>()
        Queue<Integer> cols = new LinkedList<>()
        min = 0, max = 0
        q.add(root) cols.add(0)
        while(!q.isEmpty()):
            TreeNode cur = q.poll()
            j = cols.poll()
            #  add <col, val> pair 
            if(!map.containsKey(j)) map.put(j, new ArrayList<Integer>())
            map.get(j).add(cur.val)
            #  update the range of col value
            min = Math.min(min, j)
            max = Math.max(max, j)
            #  expand children
            if(cur.left != null):
                q.add(cur.left)
                cols.add(j - 1)
            if(cur.right != null):
                q.add(cur.right)
                cols.add(j+ 1)
        #  add all the list entry
        for (i = min  i <= max i++ ):
            res.add(map.get(i))
        return res
```
 Python
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def verticalOrder(self, root):
        """
 :type root: TreeNode
 :rtype: List[List[int]]
 """
        cols = collections.defaultdict(list)
        queue = [(root,0)]
        for node, col in queue:
            if node:
                cols[col].append(node.val)
                queue += (node.left, col - 1), (node.right, col + 1)
        return [cols[col] for col in sorted(cols)]
```
------------------------------------------------------------------------------------------------
 103. Binary Tree Zipzag Level Order Traversal
=================================================
 103. Binary Tree Zigzag Level Order Traversal
===============================================
 Given a binary tree, return thezigzag level ordertraversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
 For example:
 Given binary tree
 `[3,9,20,null,null,15,7]` 
 ,
```
    3
   / \
  9  20
    /  \
   15   7
```
 return its zigzag level order traversal as:
```
[
  [3],
  [20,9],
  [15,7]
]
```
 Thoughts:
1. order to expanding which node's child in the current level -> using stack<TreeNode*> to reverse the order.
2. for each Node in the current level, decide weather to first push left or right into the queue:
	1. curDepth is odd -> next level even -> Normal Order
	2. curDepth is even -> next level odd -> reverse Order
 Code
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    vector<vector<int>> answer
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) :
        queue <TreeNode *> q
        stack<TreeNode *> levelNode
        if(!root) return answer
        q.push(root)
        curDepth = 0
        while(!q.empty()):
            len = q.size()
            vector<int> level
            for(i = 0  i < len i ++):
                TreeNode * cur = q.front()
                #  visit
                level.push_back(cur->val)
                levelNode.push(cur)
                q.pop()
            answer.push_back(level)
            #  add child
            for(i = 0 i < len i++):
                TreeNode * cur = levelNode.top()levelNode.pop()
                if(curDepth %2 ==0):
                    if(cur->right) q.push(cur->right)
                    if(cur->left) q.push(cur->left)
                else:
                    if(cur->left) q.push(cur->left)
                    if(cur->right) q.push(cur->right)
            curDepth++
        return answer
```
 Code (Python)
```python
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
 :type root: TreeNode
 :rtype: List[List[int]]
 """
        if not root: return []
        res, temp, q, flag=[], [], [root], 1
        while q:
            for i in xrange(len(q)):
                node=q.pop(0)
                temp+=[node.val]
                if node.left: q+=[node.left]
                if node.right: q+=[node.right]
            res+=[temp[::flag]] #  flag decides what is the final order being added!
            temp=[]
            flag*=-1
        return res
```
 Special Thanks
 fangkunjnsy
 for the
 reference
------------------------------------------------------------------------------------------------
 156. Binary Upside Down
===========================
 156. Binary Upside Down
=========================
 Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
 For example:
 Given a binary tree
`:1,2,3,4,5` 
 ,
```
    1
   / \
  2   3
 / \
4   5
```
 return the root of the binary tree
 `[4,5,2,#,#,3,1]` 
 .
```
   4
  / \
 5   2
    / \
   3   1
```
 Thoughts:
1. Recursively:
	1. Traverse all the way to the left until the left child of the curNode's left child is null.
	2. Perform rotation: cur->left->left = cur -> right cur->left->right = cur cur - > left = NULL cur->right = NULL
	3. return the newRoot (originally, cur->left).
2. Iteratively: until current Node is NULL:
	1. save left child as next node to explore, set leftChild to be the current sibling node,
	2. set sibling node to be current right child's node (for the next iteration)
	3. set right child to be the predecessor node
 Code 1
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* upsideDownBinaryTree(TreeNode* root) :
        if(!root || !root -> left) return root
        TreeNode * newRoot = upsideDownBinaryTree(root -> left)
        root -> left -> left = root -> right
        root -> left -> right = root
        root -> left = NULL
        root -> right = NULL
        return newRoot
```
 Code 2
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* upsideDownBinaryTree(TreeNode* root) :
        TreeNode* cur = root, * pre = NULL, * next= NULL, * sib = NULL
        while(cur):
            next = (cur->left)
            cur-> left = sib
            sib = cur -> right
            cur -> right = pre
            pre = cur
            cur = next
        return pre
```
 Special Thanks to
 yfcheng
 's solution and explanation
------------------------------------------------------------------------------------------------
 Bit Manipulation
====================
------------------------------------------------------------------------------------------------
 312. Burst Balloons
=======================
 Given
 `n` 
 balloons, indexed from
 `0` 
 to
 `n-1` 
 . Each balloon is painted with a number on it represented by array
 `A` 
 . You are asked to burst all the balloons. If the you burst balloon
 `i` 
 you will get
 `A[left] * A[i] * A[right]` 
 coins. Here
 `left` 
 and
 `right` 
 are adjacent indices of
 `i` 
 . After the burst, the
 `left` 
 and
 `right` 
 then becomes adjacent.
 Find the maximum coins you can collect by bursting the balloons wisely.
 Note:
* You may imagine
 `A[-1] = A[n] = 1` 
 . They are not real therefore you can not burst them.
* 0 ≤
 `n` 
 ≤ 500, 0 ≤
 `A[i]` 
 ≤ 100
 Example:
```
Input:[3,1,5,8]
Output:167 
Explanation: 
A = [3,1,5,8] -->[3,5,8] -->[3,8]   -->[8]  -- >[]
coins =  3*1*5     + 3*5*8   + 1*3*8   + 1*8*1   = 167
```
 Thoughts:
1. dp[left][right]: ... from subarray[left ... right]
2. recursive function: dp[left][right] = max(..., dp[left][i], A[left] * A[i] * A[right] + dp[i][right])
3. propagating direction: from small sliding window to larger sliding window
4. return dp[0][n-1] (from left = 0 to right n-1)
 Code T: O(n^3) & S: O(n^2)
```python
class Solution :
    public maxCoins(int[] A) :
        #  first busing 0s
        [] nums_pad = new [A.length + 2] 
        n = 1
        for (x : A) if( x > 0) nums_pad[n++] = x
        nums_pad[0] = nums_pad[n++] = 1
        [][] dp = new [n][n]
        for(s = 2 s < n s++): #  s is the length of the sliding window
            for(left = 0  left + s < n left++):
                right = left + s
                for(i = left + 1 i < right i++):
                    dp[left][right] = Math.max(dp[left][right],
                                dp[left][i] + nums_pad[left] * nums_pad[i] * nums_pad[right] + dp[i][right]
                                              )
        return dp[0][n-1]
```
```python
class Solution :
public:
    maxCoins(vector<int>& A) :
         #  first bursting 0s
        nums_pad [A.size() + 2] 
        n = 1
        for (x : A) if( x > 0) nums_pad[n++] = x
        nums_pad[0] = nums_pad[n++] = 1
        dp[n][n]  = :
        for(s = 2 s < n s++):
            for(left = 0  left + s < n left++):
                right = left + s
                for(i = left + 1 i < right i++):
                    dp[left][right] = max(dp[left][right],
                                dp[left][i] + nums_pad[left] * nums_pad[i] * nums_pad[right] + dp[i][right]
                                              )
        return dp[0][n-1]
```
```python
class Solution(object):
    def maxCoins(self, A):
        """
 :type A: List[int]
 :rtype: int
 """
        nums_pad = [1] + [x for x in A if x > 0] + [1]
        n = len(nums_pad)
        dp = [[0]* n for _ in range(n)] # a fancy way of building the nxn matrix filled with 0
        for s in range(2,n):
            for left in range(0, n - s):
                right = left + s
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], dp[left][i] + nums_pad[left] *nums_pad[i]* nums_pad[right] + dp[i][right])
        return dp[0][n-1]
```
 A Divide & Conquer solution
```python
class Solution :
    public maxCoins(int[] A) :
        #  first busing 0s
        [] nums_pad = new [A.length + 2] 
        n = 1
        for (x : A) if(x > 0) nums_pad[n++] = x
        nums_pad[0] = nums_pad[n++] = 1
        [][] mem = new [n][n] #  memoization step
        return burstBallon(mem, nums_pad, 0 , n -1)
    public burstBallon(int[][] mem, [] A, left, right):
        #  top down + bottom up fashion
        #  base case
        if (left == right -1) return 0
        if (mem[left][right] > 0) return mem[left][right]
        ans = 0
        #  caculation step
        for(i = left + 1 i < right i++):
            ans = Math.max(ans, A[left] * A[i] * A[right] + burstBallon(mem,A, left, i) +  burstBallon(mem,A, i, right))
        mem[left][right] = ans # memoization step
        return ans
```
 Note:
 In this case the reason why recursive solution with memoization is faster is because for some DP problems, we might not have to examine "all" the sub-problems, which most of the bottom-up table building iterative solutions do. In those cases, recursive solution examine less sub-problems, and that compensate for the overhead from recursion.
 However, iterative solution is definitely faster than recursive solution for this problem (in Python). The reason is that they both "fill up" the same sub-solutions in the dp array, and recursion always has more overhead than iteration.
 from
 dietpepsi
 's
 post
 and explanation by
 StrongerXi
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 70. Climbing Stairs
=======================
 70. Climbing Stairs
=====================
 You are climbing a stair case. It takesnsteps to reach to the top.
 Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 Note:
 Givennwill be a positive integer.
 Example 1:
```
Input:
 2
Output:
  2
Explanation:
  There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
 Example 2:
```
Input:
 3
Output:
  3
Explanation:
  There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```
 Code
```python
class Solution :
public:
    climbStairs(n) :
        if( n < 0) return 0
        d[n + 1] fill_n(d,n+1,1)
        cout<<d[0]<<endl
        for(i = 2 i <= n i++):
            d[i] = d[i-1] + d[i-2]
        return d[n]
```
------------------------------------------------------------------------------------------------
 133. Clone Graph
====================
 133. Clone Graph
==================
 Clone an undirected graph. Each node in the graph contains a
 `label` 
 and a list of its
 `neighbors` 
 .
 OJ's undirected graph serialization:
 Nodes are labeled uniquely.
 We use
 `#` 
 as a separator for each node, and
 `,` 
 as a separator for node label and each neighbor of the node.
 As an example, consider the serialized graph
 `:0,1,2#1,2#2,2` 
 .
 The graph has a total of three nodes, and therefore contains three parts as separated by
 `#` 
 .
1. First node is labeled as
 `0` 
 . Connect node
 `0` 
 to both nodes
 `1` 
 and
 `2` 
 .
2. Second node is labeled as
 `1` 
 . Connect node
 `1` 
 to node
 `2` 
 .
3. Third node is labeled as
 `2` 
 . Connect node
 `2` 
 to node
 `2` 
 (itself), thus forming a self-cycle.
 Visually, the graph looks like the following:
```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
```
 Thoughts:
1. BFS/DFS + node mapping
 Code (BFS)
```
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode :
 * label
 * vector<UndirectedGraphNode *> neighbors
 * UndirectedGraphNode(x) : label(x) :
 * 
 */
class Solution :
    #  mp maps original node to the copy node
    unordered_map <UndirectedGraphNode*, UndirectedGraphNode*> mp
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) :
        if(!node) return node
        queue<UndirectedGraphNode* > q
        UndirectedGraphNode* head = new UndirectedGraphNode(node->label)
        mp[node] = head
        q.push(node)
        while(!q.empty()):
            #  do two things: 1. update mapping record for NEIGH node 2. copy neighbor for the current node 
            UndirectedGraphNode * cur = q.front() q.pop()
            for(auto neigh : cur->neighbors):
                if(mp.find(neigh) == mp.end()):
                    UndirectedGraphNode* cp_node = new UndirectedGraphNode(neigh->label)
                    mp[neigh] = cp_node
                    q.push(neigh)
                #  copy cur neighbors
                mp[cur] -> neighbors.push_back(mp[neigh])
        return head
```
 Code (DFS)
```
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode :
 * label
 * vector<UndirectedGraphNode *> neighbors
 * UndirectedGraphNode(x) : label(x) :
 * 
 */
class Solution :
    unordered_map <UndirectedGraphNode*, UndirectedGraphNode*> mp
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) :
        if(!node) return node
        if(mp.find(node) == mp.end()):
            UndirectedGraphNode * head = new UndirectedGraphNode(node->label)
            mp[node] = head
            for(auto neigh: node->neighbors):
            mp[node]-> neighbors.push_back(cloneGraph(neigh))
        return mp[node]
```
 Special Thanks
 jianchaolifighter
 's
 solution
------------------------------------------------------------------------------------------------
 518. Coin Change 2
======================
 You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
 Note:
 You can assume that
* 0 <= amount <= 5000
* 1 <= coin <= 5000
* the number of coins is less than 500
* the answer is guaranteed to fit into signed 32-bit integer
 Example 1:
```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```
 Example 2:
```
Input:
 amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```
 Example 3:
```
Input: amount = 10, coins = [10] 
Output: 1
```
```python
class Solution :
    public change(amount, int[] coins) :
        int[][] dp = new int[coins.length+1][amount+1]
        dp[0][0] = 1
        for (i = 1 i <= coins.length i++) :
            dp[i][0] = 1
            for (j = 1 j <= amount j++) :
                dp[i][j] = dp[i-1][j] + (j >= coins[i-1] ? dp[i][j-coins[i-1]] : 0)
        return dp[coins.length][amount]
```
------------------------------------------------------------------------------------------------
 40. Combination Sum II
==========================
 Given a collection of candidate numbers (
 `candidates` 
 ) and a target number (
 `target` 
 ), find all unique combinations in
 `candidates` 
 where the candidate numbers sums to
 `target` 
 .
 Each number in
 `candidates` 
 may only be used
 once
 in the combination.
 Note:
* All numbers (including
 `target` 
 ) will be positive integers.
* The solution set must not contain duplicate combinations.
 Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```
 Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```
 Thoughts:
1. Only two lines changes than
 39. Combination Sum
 Code
```python
class Solution :
    public List<List<Integer>> combinationSum2(int[] A, target) :
    List<List<Integer>> list = new ArrayList<>()
    Arrays.sort(A)
    backtrack(list, new ArrayList<>(), A, target, 0)
    return list
private void backtrack(List<List<Integer>> list, List<Integer> tempList, [] A, remain, start):
    if(remain < 0) return
    else if(remain == 0) list.add(new ArrayList<>(tempList))
    else: 
        for(i = start i < A.length i++):
            #  follow-up: Each number in candidates may only be used once in the combination + there are duplicates.
            if(i > start && A[i] == A[i - 1]) continue #  previous DFS has expanded later value!
            tempList.add(A[i])
            backtrack(list, tempList, A, remain - A[i], i + 1) #  i + 1 HERE! because we CANNOT reuse same elements
            tempList.remove(tempList.size() - 1)
```
------------------------------------------------------------------------------------------------
 39. Combination Sum
=======================
 Given a
 set
 of candidate numbers (
 `candidates` 
 )
 (without duplicates)
 and a target number (
 `target` 
 ), find all unique combinations in
 `candidates` 
 where the candidate numbers sums to
 `target` 
 .
 The
 same
 repeated number may be chosen from
 `candidates` 
 unlimited number of times.
 Note:
* All numbers (including
 `target` 
 ) will be positive integers.
* The solution set must not contain duplicate combinations.
 Example 1:
```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```
 Example 2:
```
Input: candidates = [2,3,5], 
target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```
 Thoughts:
1. Backtracking: can select
 distinct number repeated times -> so each time for loop start at the passed-in index
 Code: T:O(N^2) S: O(N^2)
```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
 :type candidates: List[int]
 :type target: int
 :rtype: List[List[int]]
 """
        def dfs(res, path, start, target):
            if target <= 0 : return 
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                if candidates[i] == target:
                    res.append(list(path))
                    # pop the tail for next candidate
                    path.pop()
                    continue
                dfs(res, path, i, target - candidates[i])
                # pop the tail for next candidate
                path.pop()
            return
        res = []
        dfs(res, [], 0, target)
        return res
```
 Code: java with sorting
```python
class Solution :
    public List<List<Integer>> combinationSum(int[] A, target) :
    List<List<Integer>> list = new ArrayList<>()
    Arrays.sort(A)
    backtrack(list, new ArrayList<>(), A, target, 0)
    return list
private void backtrack(List<List<Integer>> list, List<Integer> tempList, [] A, remain, start):
    if(remain < 0) return
    else if(remain == 0) list.add(new ArrayList<>(tempList))
    else: 
        for(i = start i < A.length i++):
            #  follow-up: Each number in candidates may only be used once in the combination + there are duplicates.
            #  follow-up: if(i > start && A[i] == A[i - 1]) continue
            tempList.add(A[i])
            backtrack(list, tempList, A, remain - A[i], i) #  not i + 1 because we can reuse same elements
            tempList.remove(tempList.size() - 1)
```
------------------------------------------------------------------------------------------------
 829. Consecutive Numbers Sum
================================
 829. Consecutive Numbers Sum
==============================
 Given a positive integer
 `N` 
 , how many ways can we write it as a sum of consecutive positive integers?
 Example 1:
```
Input: 
5
Output: 
2
Explanation: 
5 = 5 = 2 + 3
```
 Example 2:
```
Input: 
9
Output: 
3
Explanation: 
9 = 9 = 4 + 5 = 2 + 3 + 4
```
 Example 3:
```
Input: 
15
Output: 
4
Explanation: 
15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
```
 Note:
 `1 <= N <= 10 ^ 9` 
 .
 Thoughts:
1. If
 N = i * j,
 then we want to find
 i
 consecutive numbers with average
 j
 For example, 15 = 3 * 5, then 4 + 5 + 6, 3 numbers with average 5 and 15 = 5 * 3, then 1 + 2 + 3 + 4 + 5, 5 numbers with average 3 But one constraint is that
 i
 must be
 odd
 , since if i is even k + 1, k + 2, ... k + i. The average = (ik + (1 + i)*i/2) / i = k + (1 + i) / 2, cannot be an integer. (
 Original Post
 )
2. Simple Code, but obscure logic (
 Original Post
 )
 Code 1
```python
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == 1: 
            return 1
        res = 1
        for i in range(2, int(N ** .5 + 1)):   
            if N % i == 0:
                if i % 2 == 1: # If i is odd, then we can form a sum of length i
                    res += 1
                j = (N #  i) # Check the corresponding N #  i
                if i != j and j % 2 == 1:
                    res += 1
        if N % 2 == 1: # If N is odd(2k + 1). Then N = k + k + 1, not included above
            res += 1
        return res
```
 Code 2
```python
class Solution :
public:
    consecutiveNumbersSum(N) :
        res = 0
        for(i=1 i*(i-1)<=2*N i++) :
            if((2*N+i-i*i)%(2*i)==0&&(2*N+i-i*i)/(2*i)>0) :
                res++
        return res
```
------------------------------------------------------------------------------------------------
 106. Construct Binary Tree from Inorder and Postorder Traversal
===================================================================
 Given inorder and postorder traversal of a tree, construct the binary tree.
 Note:
 You may assume that duplicates do not exist in the tree.
 For example, given
```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```
 Return the following binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```
 Thoughts:
1. Similar to 105, but build the postidx from the back
2. The the basic idea is to take the last element in postorder array as the root, find the position of the root in the inorder array then locate the range for left sub-tree and right sub-tree and do recursion. Use a HashMap to record the index of root in the inorder array.
 Code:
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public TreeNode buildTree(int[] inorder, int[] postorder) :
        return build(postorder, postorder.length - 1, inorder, 0, inorder.length -1)
    private TreeNode build(int[] postorder, posIdx, int[] inorder, inStart, inEnd):
        if(inStart > inEnd || posIdx < 0) return null
        TreeNode root = new TreeNode(postorder[posIdx])
        i = 0
        for(i = inStart i <= inEnd i ++):
            if(inorder[i] == postorder[posIdx]) break
        root.right = build(postorder, posIdx - 1, inorder, i + 1, inEnd) 
        root.left = build(postorder, posIdx - 1 - (inEnd - i), inorder, inStart, i - 1)
        return root
```
 Code: with hashMap
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public TreeNode buildTree(int[] inorder, int[] postorder) :
        if (inorder == null || postorder == null || inorder.length != postorder.length)
        return null
        HashMap<Integer, Integer> hm = new HashMap<Integer,Integer>()
        for (i=0 i< inorder.length ++i)
            hm.put(inorder[i], i)
        return buildTreePostIn(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1,hm)
private TreeNode buildTreePostIn(int[] inorder, is, ie, int[] postorder, ps, pe, HashMap<Integer,Integer> hm):
    if (ps>pe || is>ie) return null
    TreeNode root = new TreeNode(postorder[pe])
    i = hm.get(postorder[pe])
    #  i - is: number of nodes in the left subtree
    root.left = buildTreePostIn(inorder, is, i-1, postorder, ps, ps+i-is-1, hm)
    root.right  = buildTreePostIn(inorder,i+1, ie, postorder, ps+i-is, pe-1, hm)
    return root
```
------------------------------------------------------------------------------------------------
 105. Construct Binary Tree from Preorder and Inorder Traversal
==================================================================
 Given preorder and inorder traversal of a tree, construct the binary tree.
 Note:
 You may assume that duplicates do not exist in the tree.
 For example, given
```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```
 Return the following binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```
 Thoughts:
1. Given preorder root preorder[preStart]: Find the corresponding index in the inorder array i, then [inStart ... i - 1] is the left tree, and [i + 1, inEnd] is the right tree. Base case: either preStart out of right bounds or inStart > inEnd.
2. Iterative Solution: from
 gpraveenkumar
 's
 post
 :
	1. Keep pushing the nodes from the preorder into a stack (and keep making the tree by adding nodes to the left of the previous node) until the top of the stack matches the inorder.
	2. At this point, pop the top of the stack until the top does not equal inorder (keep a flag to note that you have made a pop).
	3. Repeat 1 and 2 until preorder is empty. The key point is that whenever the flag is set, insert a node to the right and reset the flag.
 Code: Recursive: T:(NlogN),
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public TreeNode buildTree(int[] preorder, int[] inorder) :
        return build(0,0,inorder.length - 1, preorder, inorder)
    private TreeNode build(preStart, inStart, inEnd, [] preorder, [] inorder):
        if(preStart > preorder.length - 1 || inStart > inEnd) return null
        TreeNode root = new TreeNode(preorder[preStart])
        split = 0
        for(i = inStart i <= inEnd i++ ):
            if(inorder[i] == preorder[preStart])  split = i
        root.left = build(preStart + 1, inStart, split - 1, preorder, inorder)
        root.right = build(preStart + 1 + split - inStart, split + 1, inEnd, preorder, inorder)
        return root
```
 Code: Iterative: T: O()
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) :
         if(preorder.size()==0)
             return NULL
         stack<int> s stack<TreeNode *> st
         TreeNode *t,*r,*root
         i,j,f f=i=j=0
         s.push(preorder[i])
         root = new TreeNode(preorder[i])
         st.push(root) t = rooti++
         while(i<preorder.size()) :
             if(!st.empty() && st.top()->val==inorder[j]):
                 t = st.top()
                 st.pop()
                 s.pop()
                 f = 1
                 j++
             else :
                 if(f==0) :
                     s.push(preorder[i])
                     t -> left = new TreeNode(preorder[i])
                     t = t -> left
                     st.push(t)
                     i++
                 else :
                     f = 0
                     s.push(preorder[i])
                     t -> right = new TreeNode(preorder[i])
                     t = t -> right
                     st.push(t)
                     i++
         return root
```
------------------------------------------------------------------------------------------------
 523. Continuous Subarray Sum
================================
 Given a list of
 non-negative
 numbers and a target
 integer
 k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of
 k
 , that is, sums up to n*k where n is also an
 integer
 .
 Example 1:
```
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
```
 Example 2:
```
Input: [23, 2, 6, 4, 7],  k=6
Output:True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
```
 Note:
1. The length of the array won't exceed 10,000.
2. You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
 Thoughts:
1. Use map:
	1. Query whether there is a index with value equal to modulo preSum and whether its distance from current i is > 1
	2. Use end<modulo preSum: index> to record the modulo preSum value
2. Use only set + add delay
```python
class Solution(object):
    def checkSubarraySum(self, A, k):
        """
 :type A: List[int]
 :type k: int
 :rtype: bool
 """
        preS, end = 0, :0: -1
        for i, num in enumerate(A):
            preS += num
            if k != 0:
                preS %= k 
            if preS in end: # keep the least index
                if i - end[preS] > 1:
                    return True
            else: 
                end[preS] = i 
        return False
```
```python
class Solution :
public:
    bool checkSubarraySum(vector<int>& A, k) :
        n = A.size(), sum = 0, pre = 0
        unordered_set<int> modk
        for(i = 0 i < n i++):
            sum += A[i]
            mod =  k == 0 ? sum : sum % k
            if(modk.count(mod)) return true
            modk.insert(pre)
            pre = mod #  delay for two loops
        return false
```
 Python
```python
class Solution(object):
    def checkSubarraySum(self, A, k):
        """
 :type A: List[int]
 :type k: int
 :rtype: bool
 """
        n, s, pre = len(A), 0, 0
        end = set()
        for i, num in enumerate(A):
            s += num
            if k != 0:
                s %= k
            if s in end: return True
            end.add(pre)
            pre = s 
        return False
```
------------------------------------------------------------------------------------------------
 Convert Binary Search Tree (BST) to Sorted Doubly-Linked List
=================================================================
###### 
 Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
 https:# github.com/tongzhang1994/Facebook-Interview-Coding/blob/master/Convert BST to Circular Doubly LinkedList.java
```
Convert BST to Circular Doubly LinkedList
#  http:# articles.leetcode.com/convert-binary-search-tree-bst-to/
注意，head和prev必须用全局变量！！
#  we could safely modify a node’s left pointer to point to the previously traversed node as we never use it once we reach a node. 
#  We would also need to modify the previously traversed node’s right pointer to point to the current node.
#  But wait, we are still missing two more steps. First, we did not assign the list’s head pointer. Second, the last element’s right pointer does not point to the first element (similar to the first element’s left pointer).
#  Just update the current node’s right pointer to point back to the head and the head’s left pointer to point to current node in each recursive call. 
#  As the recursion ends, the list’s head and tail would be automagically updated with the correct pointers. 
#  Don’t forget to check for this special case: A list with only one element should have its left and right pointers both pointing back to itself.
Solution 1: recursion
O(n) time, O(h) space
TreeNode head = null, prev = null
public TreeNode convertBSTtoCircularDL(TreeNode root) :
    convert(root)
    return head
public void convert(TreeNode root) :
    if (root == null)    return
    convert(root.left)
    root.left = prev
    if (prev != null)    prev.right = root
    else    head = root
    #  would make head <-> tail in the end
    TreeNode right = root.right
    head.left = root
    root.right = head
    prev = root
    convert(right)
Solution 2: iteration
O(n) time, O(h) space
public TreeNode bstToDoublyList(TreeNode root) :  
    TreeNode head = null, prev = null
    Stack<TreeNode> stack = new Stack<>()
    while (root != null || !stack.empty()) :
        while (root != null) :
            stack.push(root)
            root = root.left
        root = stack.pop()
        root.left = prev
        if (prev != null)    prev.right = root
        else     head = root
        TreeNode right = root.right
        head.left = root
        root.right = head# remember to update the prev !!!
        prev = root
        root = right# we should root=root.right even if it's null!!!
    return head
```
 https:# coderpad.io/9PQEHACH
 Followup: Reverse Operation:
```
 private static BSTNode DLtoBST(BSTNode head):
    #  unlink the tail 
    BSTNode tail = head.left
    tail.right = null
    head.left = null
    return toBST(head, null)
  private static BSTNode toBST(BSTNode head, BSTNode tail):
    if (head == tail) return null
    BSTNode fast = head, slow = head
    while(fast != tail && fast.right != tail):
        fast = fast.right.right
        slow = slow.right
    #  slow is the root of the tree
    slow.left = toBST(head, slow)
    slow.right = toBST(slow.right, tail)
    return slow
```
------------------------------------------------------------------------------------------------
 109. Convert Sorted List to Binary Search Tree
==================================================
 Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
 For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of_every_node never differ by more than 1.
 Example:
```
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
```
 Thoughts:
 use slow, fast two pointers to divide the tree
 Follow up
 : inplace conversion, assume both use class Node.
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 * val
 * ListNode next
 * ListNode(x) : val = x 
 * 
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
#  try inplace
class Solution :
    public TreeNode sortedListToBST(ListNode head) :
        if (head == null) return null
        return binaryTraversal(head, null)
    private TreeNode binaryTraversal(ListNode head, ListNode tail):
        if(head == tail) return null
        ListNode slow = head, fast = head
        while(fast != tail &&  fast.next != tail):
            fast = fast.next.next
            slow = slow.next
        #  new head is slow.val
        TreeNode thead = new TreeNode(slow.val)
        thead.left = binaryTraversal(head, slow)
        thead.right = binaryTraversal(slow.next, tail)
        return thead
```
------------------------------------------------------------------------------------------------
 38. Count and Say
=====================
 The count-and-say sequence is the sequence of integers with the first five terms as following:
```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```
`1` 
 is read off as
 `"one 1"` 
 or
 `11` 
 .
`11` 
 is read off as
 `"two 1s"` 
 or
 `21` 
 .
`21` 
 is read off as
 `"one 2` 
 , then
 `one 1"` 
 or
 `1211` 
 .
 Given an integer n where 1 ≤
 ---n--- 
 ≤ 30, generate the nth term of the count-and-say sequence.
 Note: Each term of the sequence of integers will be represented as a string.
 Example 1:
```
Input: 1
Output: "1"
```
 Example 2:
```
Input: 4
Output: "1211"
```
 Thoughts:
1. Two pointers: each time counting the number of continuous same number
```python
class Solution(object):
    def countAndSay(self, n):
        """
 :type n: int
 :rtype: str
 """
        if n < 1: return '0'
        res = '1'
        for k in xrange(1,n):
            i, j, tmp = 0,0, ''
            while j < len(res):
                if res[i] == res[j]:
                    j +=1
                else:
                    tmp += str(j - i) + str(res[i])
                    i = j
            tmp += str(j - i) + str(res[i])
            res = tmp
        return res
```
------------------------------------------------------------------------------------------------
 315. Count of Smaller Numbers After Self
============================================
 You are given an integer arraynumsand you have to return a newcountsarray. Thecountsarray has the property where
 `counts[i]` 
 is the number of smaller elements to the right of
 `A[i]` 
 .
 Example:
```
Input:
[5,2,6,1]
Output:
[2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```
 Thoughts:
1. Failed to use template for positive entry... (attaching the code)
2. d
 Code that I failed to implement (failed to handle properly the negative case):
```python
class Solution :
    class SegmentTreeNode:
    public start , end, cnt
    public SegmentTreeNode left, right
    public SegmentTreeNode (start, end, cnt):
        this.start = start
        this.end = end
        this.cnt = cnt
        this.left = this.right = null
    public List<Integer> countSmaller(int[] A) :
        max = Integer.MIN_VALUE
        min = Integer.MAX_VALUE
        for(num: A):
            if (num > max)
                max = num
            if (num < min)
                min = num
        #  System.out.println("1: max: " + max)
        SegmentTreeNode root = build(min, max)
        List<Integer> ans = new ArrayList<Integer>()
        [] record = new int[A.length] 
        for (i = A.length - 1 i >=0 i--):
            #  if(A[i] > 0):
                record[i] = query(root, min, A[i] - 1)
                System.out.println("i: " + i + " A[i]: " + A[i] + " query: " + query(root, min, A[i] - 1))
                modify(root, A[i], 1)
            #  
        for(num: record):
            ans.add(num)
        #  if (ans.isEmpty()):
        #  ans.add(0)
        #  return ans
        #  
        return ans
    public SegmentTreeNode build (start, end):
        if (start > end):
            return null
        if(start == end):
            return new SegmentTreeNode (start, end, 0)
        mid = (start + end) / 2
        if(mid == end):
            mid -= 1
        System.out.println("build start: " + start + " end: " + end + " mid: " + mid)
        SegmentTreeNode left = build(start, mid)
        SegmentTreeNode right = build(mid + 1, end)
        SegmentTreeNode ret = new SegmentTreeNode (start, end, 0)
        ret.left = left
        ret.right = right
        return ret 
    public void modify(SegmentTreeNode root, index, val):
        if(root.start == root.end && root.end == index ):
            root.cnt = val
            #  System.out.println("index: " + index + " modified as: " + val)
            return
        mid = (root.start + root.end) /2 
         if(mid == root.end):
            mid -= 1
        if(root.start <= index && index <=mid):
            modify(root.left, index, val)
        if(mid < index && index <= root.end) :
            modify(root.right, index, val)
        root.cnt = root.left.cnt + root.right.cnt
        return
    public query(SegmentTreeNode root, start, end):
        if(start > end) return 0
        mid = (root.start + root.end) / 2
         if(mid == root.end):
            mid -= 1
        System.out.println("Query start: " + start + " end: " + end + 
                           " root start: " + root.start + " root end: " + root.end + " mid: "  + mid
                          )
        if (start == root.start && root.end == end):
            System.out.println("exact!")
            return root.cnt
        ret = 0
        if (start <= mid ):
             System.out.println("left!")
            ret += query(root.left, start, mid)
        if (mid + 1 <= end ):
            System.out.println("right!")
            ret += query(root.right, mid + 1, end)
        return ret
```
 SegmentTree implementation:
```python
class SegmentTreeNode(object):
    def __init__ (self, val , start, end):
        self.val = val
        self.start = start 
        self.end = end
        self.children = []
class SegmentTree(object):
    def __init__ (self, n):
        self.root = self.build(0, n - 1)
    def build(self, start, end):
        if start > end:
            return
        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root
        mid = start + end >> 1
        root.children = filter(None, [
            self.build(start, end)
            for start, end in ((start, mid),(mid + 1, end))
        ]) 
        return root
    def update(self, i, val, root):
        # root = root or self.root
        if i < root.start or i > root.end:
            return root.val
        if i == root.start == root.end:
            root.val += val 
            return root.val 
        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val
    def sum(self, start, end, root):
        # root = root or self.root
        if end < root.start or start > root.end:
            return 0
        if start <= root.start and end >= root.end:
            return root.val
        return sum([self.sum(start, end, c) for c in root.children])
class Solution(object):
    def countSmaller(self, A):
        """
 :type A: List[int]
 :rtype: List[int]
 """
        table = :v : i for i , v in enumerate(sorted(set(A)))
        # print(table)
        tree , r  = SegmentTree(len(table)), []
        for i in range(len(A) - 1, -1, -1):
            r.append(tree.sum(0, table[A[i]] - 1, tree.root))
            tree.update(table[A[i]], 1, tree.root)
        return r[::-1]
```
 BinaryIndexedTree implementation:
```python
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)
    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r
class Solution(object):
    def countSmaller(self, A):
        hashTable = :v: i for i, v in enumerate(sorted(set(A)))
        tree, r = BinaryIndexedTree(len(hashTable)), []
        for i in xrange(len(A) - 1, -1, -1):
            r.append(tree.sum(hashTable[A[i]]))
            tree.update(hashTable[A[i]] + 1, 1)
        return r[::-1]
```
 BinarySearchTree implementation:
```python
class BSTNode(object):
    def __init__ (self, val):
        self.val = val 
        self.left = None
        self.right = None
        self.count = 1
        self.leftTreeSum = 0
class BST(object):
    def __init__ (self):
        self.root = None
    def insert(self, val, root):
        if not root:
            self.root = BSTNode(val)
            return 0
        if val == root.val:
            root.count += 1
            return root.leftTreeSum
        if val < root.val:
            root.leftTreeSum += 1
            if not root.left:
                root.left = BSTNode(val)
                return 0
            return self.insert(val, root.left)
        if not root.right:
            root.right = BSTNode (val)
            return root.count + root.leftTreeSum 
        return root.count + root.leftTreeSum + self.insert(val, root.right)
class Solution(object):
    def countSmaller(self, A):
        """
 :type A: List[int]
 :rtype: List[int]
 """
        tree = BST()
        return [tree.insert(
            A[i], tree.root)
            for i in range(len(A) -1, -1 , -1)
            ][::-1]
```
 MergeSort implementation T: O(nlogn) S: O(n)
```python
class Solution :
protected:
    void merge(vector<int>& indices, first, last, 
 vector<int>& results, vector<int>&A):
        mid = first + (last - first)/2
        if(mid > first):
            merge(indices, first, mid, results, A)
            merge(indices, mid, last, results, A)
            vector<int> sorted
            subchild = 0
            idx1 = first, idx2 = mid
            while((idx1 < mid) || (idx2 < last)): 
                if((idx2 == last) || ((idx1 < mid)  &&
                                     (A[indices[idx1]] <= A[indices[idx2]]) #  must be <= since only counts numbers that are SMALLER
                                     )) :  # 3
                    sorted.push_back(indices[idx1])
                    results[indices[idx1]] += subchild
                    idx1++
                else:
                    sorted.push_back(indices[idx2])
                    subchild++
                    idx2++
            move(sorted.begin(), sorted.end(), indices.begin() + first)
public:
    vector<int> countSmaller(vector<int>& A) :
        n = A.size()
        vector<int> results (n, 0)
        vector<int> indices (n, 0)
        iota (indices.begin(), indices.end(), 0)
        merge(indices, 0, n, results, A)
        return results
```
------------------------------------------------------------------------------------------------
 338. Counting Bits
====================
 Given a non negative integer number
 num
 . For every numbers
 i
 in the range
 0 ≤ i ≤ num
 calculate the number of 1's in their binary representation and return them as an array.
 Example:
 For
 `num = 5` 
 you should return
 `[0,1,1,2,1,2]` 
 .
 Follow up:
* It is very easy to come up with a solution with run time
 O(n*sizeof(integer))
 . But can you do it in linear time
 O(n)
 /possibly in a single pass?
* Space complexity should be
 O(n)
 .
* Can you do it like a boss? Do it without using any builtin function like
 __builtin_popcount
 in c++ or in any other language.
 Credits:
 Special thanks to
 @ syedee
 for adding this problem and creating all test cases.
 Thoughts:
1. f[i] = f[i/2] (right shift by 1) + f[i%2] with f[0] = 0 and f[1] =1
```python
class Solution :
public:
    vector<int> countBits(num) :
        vector<int> f (num + 1)
        f[0] = 0
        f[1] = 1
        for(i = 2 i <= num  i ++):
            f[i] = f[i/2] + f[i%2]
        return f
```
------------------------------------------------------------------------------------------------
 1.   Course Schedule III
==========================
 There are
 `n` 
 different online courses numbered from
 `1` 
 to
 `n` 
 . Each course has some duration(course length)
 `t` 
 and closed on
 `dth` 
 day. A course should be taken
 continuously
 for
 `t` 
 days and must be finished before or on the
 `dth` 
 day. You will start at the
 `1st` 
 day.
 Given
 `n` 
 online courses represented by pairs
 `(t,d)` 
 , your task is to find the maximal number of courses that can be taken.
 Example:
```
Input:
 [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output:
 3
Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
```
 Note:
1. The integer 1 <= d, t, n <= 10,000.
2. You can't take two courses simultaneously.
 Thoughts:
 Greedy:
 sort course by end time, remove course by descending course length
 Rigorous proof
 here
 Code (Python):
```python
class Solution(object):
    def scheduleCourse(self, courses):
        """
 :type courses: List[List[int]]
 :rtype: int
 """
        pq = [] 
        total = 0
        for t, end in sorted(courses, key = lambda(t,end):end):
            total += t
            heapq.heappush(pq, -t) #-t here since heapq is a minheap by default
            if total > end:
                total += heapq.heappop(pq) # add negative number
        return len(pq)
```
------------------------------------------------------------------------------------------------
 753. Craking the Safe
=========================
 753. Cracking the Safe
========================
 There is a box protected by a password. The password is a sequence of
 `n` 
 digits where each digit can be one of the first
 `k` 
 digits
 `0, 1, ..., k-1` 
 .
 While entering a password, the last
 `n` 
 digits entered will automatically be matched against the correct password.
 For example, assuming the correct password is
 `"345"` 
 , if you type
 `"012345"` 
 , the box will open because the correct password matches the suffix of the entered password.
 Return any password of
 minimum length
 that is guaranteed to open the box at some point of entering it.
 Example 1:
```
Input:
 n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
```
 Example 2:
```
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
```
 Note:
1. `n` 
 will be in the range
 `[1, 4]` 
 .
2. `k` 
 will be in the range
 `[1, 10]` 
 .
3. `k^n` 
 will be at most
 `4096` 
 .
 Thoughts:
1. DFS: A hashset and stringbuilder to edit the string. (
 Original Post
 )
	1. start: n repeated "0".
	2. transit: all the nodes that have not visited so far.
	3. output: string in stringBuilder. (Guaranteed there is an answer after containing k^n visited distinct strings.
2. Greedy:
	1. start: n repeated "0".
	2. for loop through current digit j from k-1 to 0, append the last with the current digit, add the current substring and append current digit j to the answer if the current substring is not in visited (
	 Original Post
	 )
 Code:
 DFS T: O(k^n)
```
 class Solution :
    public String crackSafe(n, k) :
        String start = String.join("", Collections.nCopies(n, "0"))
        StringBuilder sb = new StringBuilder(start)
        Set<String> visited = new HashSet<>()
        visited.add(start)
        target = (int) Math.pow(k,n)
        DFS(sb, visited, target, n, k)
        return sb.toString()
    private boolean DFS(StringBuilder sb, Set<String> visited, target, n, k):
        #  base case: all n-length combinations among digits 0 ~ (k -1)
        if(visited.size() == target)
            return true
        String last = sb.substring(sb.length() - ( n - 1))
        /* DFS expansion*/
        for (char ch = '0' ch < '0' + k ch ++):
            String cand = last + ch
            if(!visited.contains(cand)):
                visited.add(cand)
                sb.append(ch)
                if(DFS(sb, visited, target, n, k))
                    return true
                visited.remove(cand)
                sb.deleteCharAt(sb.length() - 1)
        return false
```
 Code: Greedy T:O(k^n * k)
```python
class Solution :
public:
    string crackSafe(n, k) :
        string ans = string(n, '0')
        unordered_set<string> visited
        visited.insert(ans)
        for(i = 0 i < pow(k,n)i++):
            string prev = ans.substr(ans.size()-n+1,n-1)
            for(j = k - 1 j >= 0 j--):
                string now = prev + to_string(j)
                if(!visited.count(now)):
                    visited.insert(now)
                    ans += to_string(j)
                    break
        return ans
```
------------------------------------------------------------------------------------------------
 675. Cut Off Trees for Golf Event
=====================================
 675.Cut Off Trees for Golf Event
==================================
 You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:
1. `0` 
 represents the
 `obstacle` 
 can't be reached.
2. `1` 
 represents the
 `ground` 
 can be walked through.
3. `The place with number bigger than 1` 
 represents a
 `tree` 
 can be walked through, and this positive number represents the tree's height.
 You are asked to cut off
 all
 the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
 You will start from the point (0, 0) and you should output the minimum steps
 you need to walk
 to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
 You are guaranteed that no two
 `trees` 
 have the same height and there is at least one tree needs to be cut off.
 Example 1:
```
Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output:
 6
```
 Example 2:
```
Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output:
 -1
```
 Example 3:
```
Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output:
 6
Explanation:
 You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
```
 Hint
 : size of the given matrix will not exceed 50x50.
 Thoughts:
 1.BFS
 2.A* without heuristics (Dijkstra's Algorithm)
 Code (BFS)
```python
class Solution :
    m, n
public:
    cutOffTree(vector<vector<int>>& forest) :
        #  find all trees and sort them 
        m = forest.size()
        n = forest[0].size()
        vector<tuple<int, int, int>> trees
        for ( y = 0  y < m y++):
            for (x = 0 x < n x++):
                if(forest[y][x] > 0):
                    trees.emplace_back(forest[y][x], x, y)
            #  sort the trees by height
            sort(trees.begin(), trees.end())
            sx = 0, sy =0, total_steps = 0
        #  Move from current position to next tree to cut
            for(i = 0 i < trees.size() i++):
                dx = get<1>(trees[i])
                dy = get<2>(trees[i])
            #  accumulate pairwise distance using graph search as the answer
                incr_steps = BFS(forest, sx, sy, dx, dy)
                if (incr_steps == -1) return -1
                total_steps += incr_steps
                sx = dx  
                sy = dy  
        return total_steps
private :
    BFS(const vector<vector<int>> & forest,
 sx, sy,
 dx, dy):
        #  left, right, down, up
        static dir [4][2] = ::-1, 0, :1, 0, :0, -1, :0, 1
        auto visited = vector<vector<int>>(m, vector<int>(n,0))
        queue <pair<int, int>> q
        q.emplace(sx, sy)
        steps = 0
        while(!q.empty()):
            cur_nodes = q.size()
            while(cur_nodes--):
                auto node = q.front()
                q.pop()
                cx = node.first
                cy = node.second
                 #  check done 
                if (cx == dx && cy == dy) return steps
                #  move to the next direction
                for ( i = 0 i < 4 i++):
                    x = cx + dir[i][0]
                    y = cy + dir[i][1]
                    if(x < 0 || x == n
                      || y < 0 || y == m
                      || !forest[y][x] 
                      || visited[y][x]
                      ):
                        continue
                    #  complete
                    visited[y][x] = 1
                    q.emplace(x,y)
            steps++
        return -1
```
 Code (Dijkstra's Algorithm)
```python
class Solution:
    def cutOffTree(self, forest):
        """
 :type forest: List[List[int]]
 :rtype: int
 """
        # print (type(forest))
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        def astar(forest, sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            heap = [(0, 0, sr, sc)]
            cost = :(sr, sc): 0
            while heap:
                f, g, r, c = heapq.heappop(heap)
                if r == tr and c == tc: return g
                for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        ncost = g + 1 # + abs(nr - tr) + abs(nc - tc) # heuristic?
                        if ncost < cost.get((nr, nc), 9999):
                            cost[nr, nc] = ncost
                            heapq.heappush(heap, (ncost, g+1, nr, nc))
            return -1
        for _, tr, tc in trees:
            d = astar(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return an
```
------------------------------------------------------------------------------------------------
 Data Structure
==================
------------------------------------------------------------------------------------------------
 91. Decode Ways
===================
 91. Decode Ways
=================
 A message containing letters from
 `A-Z` 
 is being encoded to numbers using the following mapping:
```
'A' ->1
'B' ->2
...
'Z' ->26
```
 Given an encoded message containing digits, determine the total number of ways to decode it.
 For example,
 Given encoded message
 `"12"` 
 , it could be decoded as
 `"AB"` 
 (1 2) or
 `"L"` 
 (12).
 The number of ways decoding
 `"12"` 
 is 2.
 Thoughts:
1. f[s]: number of way to decode string s
2. starting from the least significant digit to the most significant digit:
	1. recursive function: f[s[i ... end]] =
		1. decode as current char s[i] + rest substring: s[i+1...end]
		 (s[i] == 0? 0: f[s[i + 1... end]])
		2. decode as current char and next char s[i ... i+1] + rest substring: s[i+2...end]
		 (if we can both decode s[i...i+1] and s[i+2...end])
 Code Time: O(n), Space O(n^2)
```python
class Solution :
public:
    numDecodings(string s) :
        unordered_map <string, int> f 
        unordered_map <string, int> m 
        f.clear()
        for(i = 1 i <= 26 i++):
            f[to_string(i)] = 1
        m = f #  m is the element dictionary
        for(i = s.length()-2 i>=0 i--):
            string sec2end = s.substr(i + 1, s.length() - (i + 1))
            string third2end = s.substr(i + 2, s.length() - (i + 2))
            if(f.find(sec2end) != f.end() && s[i] != '0' ):
                f[s.substr(i, s.length() - i)]+=f[s.substr(i + 1, s.length() - (i + 1))] 
            if(f.find(third2end)!=f.end() && m.find(s.substr(i,2))!=m.end()):
                f[s.substr(i, s.length() - i)]+=f[third2end]
        return f[s]
```
------------------------------------------------------------------------------------------------
 Deque
=========
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 622. Design Circular Queue
==============================
 Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
 One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
 Your implementation should support following operations:
* `MyCircularQueue(k)` 
 : Constructor, set the size of the queue to be k.
* `Front` 
 : Get the front item from the queue. If the queue is empty, return -1.
* `Rear` 
 : Get the last item from the queue. If the queue is empty, return -1.
* `enQueue(value)` 
 : Insert an element into the circular queue. Return true if the operation is successful.
* `deQueue()` 
 : Delete an element from the circular queue. Return true if the operation is successful.
* `isEmpty()` 
 : Checks whether the circular queue is empty or not.
* `isFull()` 
 : Checks whether the circular queue is full or not.
 Example:
```
MyCircularQueue circularQueue = new MycircularQueue(3) #  set the size to be 3
circularQueue.enQueue(1)  #  return true
circularQueue.enQueue(2)  #  return true
circularQueue.enQueue(3)  #  return true
circularQueue.enQueue(4)  #  return false, the queue is full
circularQueue.Rear()  #  return 3
circularQueue.isFull()  #  return true
circularQueue.deQueue()  #  return true
circularQueue.enQueue(4)  #  return true
circularQueue.Rear()  #  return 4
```
 Note:
* All values will be in the range of [0, 1000].
* The number of operations will be in the range of [1, 1000].
* Please do not use the built-in Queue library.
 Thoughts: Having two pointers , fast and slow and a size, capacity variables to track the current capacity status
1. Init:
 slow = 0 fast = -1 size = 0
```python
class MyCircularQueue :
    size, slow, fast, C
    data []
    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(k) :
        slow = 0 fast = -1 size = 0 C = k
        data = new [k]
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(value) :
        if (isFull()) return false
        fast = (fast + 1) % C
        data[fast] = value
        size ++ 
        return true
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() :
        if(size == 0) return false
        slow = (slow + 1) % C
        size--
        return true
    /** Get the front item from the queue. */
    public Front() :
        if (isEmpty()) return -1
        return data[slow]
    /** Get the last item from the queue. */
    public Rear() :
        if (isEmpty()) return -1
        return data[fast]
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() :
        return size == 0
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() :
        return size == C
/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k)
 * boolean param_1 = obj.enQueue(value)
 * boolean param_2 = obj.deQueue()
 * param_3 = obj.Front()
 * param_4 = obj.Rear()
 * boolean param_5 = obj.isEmpty()
 * boolean param_6 = obj.isFull()
 */
```
------------------------------------------------------------------------------------------------
 642. Design Search Autocomplete System
==========================================
 Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character
 `'#'` 
 ). For
 each character
 they type
 except '#'
 , you need to return the
 top 3
 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:
1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
3. If less than 3 hot sentences exist, then just return as many as you can.
4. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
 Your job is to implement the following functions:
 The constructor function:
`AutocompleteSystem (String[] sentences, int[] times):` 
 This is the constructor. The input is
 historical data
 .
 `Sentences` 
 is a string array consists of previously typed sentences.
 `Times` 
 is the corresponding times a sentence has been typed. Your system should record these historical data.
 Now, the user wants to input a new sentence. The following function will provide the next character the user types:
`List<String> input(char c):` 
 The input
 `c` 
 is the next character typed by the user. The character will only be lower-case letters (
 `'a'` 
 to
 `'z'` 
 ), blank space (
 `' '` 
 ) or a special character (
 `'#'` 
 ). Also, the previously typed sentence should be recorded in your system. The output will be the
 top 3
 historical hot sentences that have prefix the same as the part of sentence already typed.
 Example:
 Operation:
 AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
 The system have already tracked down the following sentences and their corresponding times:
`"i love you"` 
 :
 `5` 
 times
`"island"` 
 :
 `3` 
 times
`"ironman"` 
 :
 `2` 
 times
`"i love leetcode"` 
 :
 `2` 
 times
 Now, the user begins another search:
 Operation:
 input('i')
 Output:
 ["i love you", "island","i love leetcode"]
 Explanation:
 There are four sentences that have prefix
 `"i"` 
 . Among them, "ironman" and "i love leetcode" have same hot degree. Since
 `' '` 
 has ASCII code 32 and
 `'r'` 
 has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
 Operation:
 input(' ')
 Output:
 ["i love you","i love leetcode"]
 Explanation:
 There are only two sentences that have prefix
 `"i "` 
 .
 Operation:
 input('a')
 Output:
 []
 Explanation:
 There are no sentences that have prefix
 `"i a"` 
 .
 Operation:
 input('#')
 Output:
 []
 Explanation:
 The user finished the input, the sentence
 `"i a"` 
 should be saved as a historical sentence in system. And the following input will be counted as a new search.
 Note:
1. The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
2. The number of
 complete sentences
 that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
3. Please use double-quote instead of single-quote when you write test cases even for a character input.
4. Please remember to
 RESET
 your class variables declared in class AutocompleteSystem, as static/class variables are
 persisted across multiple test cases
 . Please see
 here
 for more details.
 Thoughts:
1. Each node records: next (children), counts(String that current tries represents so far -> frequency count)
2. Only thing more than a normal
 `Trie` 
 is added a map of
 `sentence` 
 to
 `count` 
 in each of the
 `Trie` 
 node to facilitate process of getting top 3 results.
 Code: T:O(l * mlogm) for each time, assume current input word is l, there are m keys in the node of cur.
 S: O(max(l)^2 * # of inputs)
```python
class AutocompleteSystem :
    TrieNode root
    String prefix
    public AutocompleteSystem(String[] sentences, int[] times) :
        root = new TrieNode()
        prefix = ""
        for (i = 0 i < times.length i++):
            add(sentences[i], times[i])
    public List<String> input(char c) :
        #  termination
        if(c == '#'):
            add(prefix, 1)
            prefix = ""
            return new ArrayList<String>()
        prefix += c
        TrieNode cur = root
        for(char cc : prefix.toCharArray()):
            TrieNode next = cur.next.get(cc)
            if(next == null)
                return new ArrayList<String>()
            cur = next
        #  Pull out + sort all the counting infor for current string prefix
        PriorityQueue<Pair> pq = new PriorityQueue<>((a,b) -> a.c == b.c? a.s.compareTo(b.s): b.c - a.c)
        #  Add all elements into queue
        for(String s: cur.counts.keySet())
            pq.add(new Pair(s, cur.counts.get(s)))
        List<String> res = new ArrayList<>()
        #  add top 3 results
        for(i = 0 i < 3 && !pq.isEmpty() i++)
            res.add(pq.poll().s)
        return res
    private void add(String s, count):
        TrieNode cur = root
        for(char c: s.toCharArray()):
            TrieNode next = cur.next.get(c)
            if(next == null):
                next = new TrieNode()
                cur.next.put(c, next)
            cur = next
            cur.counts.put(s, cur.counts.getOrDefault(s,0) + count) #  First go then add is to to avoid putting in root
    class Pair :
        String s
        c
        public Pair(String s, count):
            this.s = s
            this.c = count
   class TrieNode:
        Map<Character,TrieNode> next
        Map<String, Integer> counts
        public TrieNode():
            next = new HashMap<>()
            counts = new HashMap<>()
/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times)
 * List<String> param_1 = obj.input(c)
 */
```
------------------------------------------------------------------------------------------------
 348. Design Tic-Tac-Toe
===========================
 Design a Tic-tac-toe game that is played between two players on anxngrid.
 You may assume the following rules:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves is allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
 Example:
```
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
TicTacToe toe = new TicTacToe(3)
toe.move(0, 0, 1) -> Returns 0 (no one wins)
|X| | |
| | | |    #  Player 1 makes a move at (0, 0).
| | | |
toe.move(0, 2, 2) -> Returns 0 (no one wins)
|X| |O|
| | | |    #  Player 2 makes a move at (0, 2).
| | | |
toe.move(2, 2, 1) -> Returns 0 (no one wins)
|X| |O|
| | | |    #  Player 1 makes a move at (2, 2).
| | |X|
toe.move(1, 1, 2) -> Returns 0 (no one wins)
|X| |O|
| |O| |    #  Player 2 makes a move at (1, 1).
| | |X|
toe.move(2, 0, 1) -> Returns 0 (no one wins)
|X| |O|
| |O| |    #  Player 1 makes a move at (2, 0).
|X| |X|
toe.move(1, 0, 2) -> Returns 0 (no one wins)
|X| |O|
|O|O| |    #  Player 2 makes a move at (1, 0).
|X| |X|
toe.move(2, 1, 1) -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    #  Player 1 makes a move at (2, 1).
|X|X|X|
```
 Follow up:
 Could you do better than O(n2) per
 `move()` 
 operation?
 Thoughts:
1. only need to record row, col, diagonal, antidiagonal: for each move, player1 add 1 and player 2 mimus 1
 Code: T: O(n)
```python
class TicTacToe :
public:
    /** Initialize your data structure here. */
    TicTacToe(n) :
        size = n
        rows.resize(n, 0)
        cols.resize(n, 0)
        diag = 0, anti_diag = 0
    /** Player :player makes a move at (:row, :col).
 @param row The row of the board.
 @param col The column of the board.
 @param player The player, can be either 1 or 2.
 @return The current winning condition, can be either:
 0: No one wins.
 1: Player 1 wins.
 2: Player 2 wins. */
    move(row, col, player) :
        if(player == 1):
            rows[row]++ cols[col]++
            if(row == col) diag++
            if(row + col == size - 1) anti_diag++
            if(rows[row] == size || cols[col] == size || diag == size || anti_diag == size) return 1
        else : # player 2
            rows[row] -- cols[col]--
            if(row == col) diag--
            if(row + col == size - 1) anti_diag--
            if(rows[row] == -size || cols[col] == -size || diag == -size || anti_diag == -size) return 2
        return 0
private:
    vector<int> rows, cols
    diag, anti_diag
    size
/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n)
 * param_1 = obj.move(row,col,player)
 */
```
 Similar idea in Java
```python
public class TicTacToe :
private int[] rows
private int[] cols
private diagonal
private antiDiagonal
/** Initialize your data structure here. */
public TicTacToe(n) :
    rows = new int[n]
    cols = new int[n]
/** Player :player makes a move at (:row, :col).
    @param row The row of the board.
    @param col The column of the board.
    @param player The player, can be either 1 or 2.
    @return The current winning condition, can be either:
            0: No one wins.
            1: Player 1 wins.
            2: Player 2 wins. */
public move(row, col, player) :
    toAdd = player == 1 ? 1 : -1
    rows[row] += toAdd
    cols[col] += toAdd
    if (row == col)
    :
        diagonal += toAdd
    if (col == (cols.length - row - 1))
    :
        antiDiagonal += toAdd
    size = rows.length
    if (Math.abs(rows[row]) == size ||
        Math.abs(cols[col]) == size ||
        Math.abs(diagonal) == size  ||
        Math.abs(antiDiagonal) == size)
        :
        return player
    return 0
```
------------------------------------------------------------------------------------------------
 498. Diagonal Traverse
==========================
 Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
 Example:
```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,4,7,5,3,6,8,9]
Explanation:
```
![](assets/trav.png)
 Thoughts:
 Check boundary, if OOB then reset the proper initial point + switching the traverse direction
```python
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
 :type matrix: List[List[int]]
 :rtype: List[int]
 """
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        m, n = len(matrix), len(matrix[0])
        row, col, d = 0 , 0 , 0
        dirs = [-1,1, 1,-1] # upright vs downleft
        res = []
        for i in range(m*n):
            res.append(matrix[row][col])
            row+= dirs[2*d + 0]
            col+= dirs[2*d + 1]
            # check if OOB, then switching the direction + initial point
            if row >= m: row, col, d = m - 1, col + 2, 1 - d
            if col >= n: row, col, d = row + 2, n - 1, 1 - d
            if row < 0: row, col, d = 0, col, 1 - d
            if col < 0: row, col, d = row, 0, 1 - d
        return res
```
------------------------------------------------------------------------------------------------
 543. Diameter of Binary Tree
================================
 Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the
 longest
 path between any two nodes in a tree. This path may or may not pass through the root.
 Example:
 Given a binary tree
```
          1
         / \
        2   3
       / \     
      4   5
```
 Return
 3
 , which is the length of the path [4,2,1,3] or [5,2,1,3].
 Thoughts:
1. Need two paths, a open path from the left and right and a closed path from the left and right
 Code
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
 :type root: TreeNode
 :rtype: int
 """
        def helper(root):
            if not root:
                return (0 , 0)
            left = helper(root.left)
            right = helper(root.right)
            return (max(left[0], right[0]) + 1 , max(left[0] + right[0] + 1, max(left[1], right[1]))) # (node numbers of open path , node numbers of of closed path)
        if not root:
            return 0
        return  helper(root)[1] - 1 # for node number > 0, path = node -1
```
------------------------------------------------------------------------------------------------
 29. Divide Two Integers
===========================
 Given two integers
 `dividend` 
 and
 `divisor` 
 , divide two integers without using multiplication, division and mod operator.
 Return the quotient after dividing
 `dividend` 
 by
 `divisor` 
 .
 The integer division should truncate toward zero.
 Example 1:
```
Input: dividend = 10, divisor = 3
Output: 3
```
 Example 2:
```
Input: dividend = 7, divisor = -3
Output:-2
```
 Note:
* Both dividend and divisor will be 32-bit signed integers.
* The divisor will never be 0.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2
^31, 2^31− 1]. For the purpose of this problem, assume that your function returns 2^31− 1 when the division result overflows.
 Thoughts:
 Convert the definition of division to subtraction: iteratively shifting the divisor until it cannot be shifted to still be smaller or equal to the dividend. Subtract dividend from the subtractor and the shifted number to the current result. Repeat until the final dividend is the reminder (less than divisor)
 Code:
```python
class Solution :
public:
    divide(dividend, divisor) :
        #  1. divisor = 0 2. dividend = INT_MIN && divisor = -1
        if(!divisor || dividend == INT_MIN && divisor == -1) return INT_MAX
        sign = ((dividend < 0) ^ (divisor < 0))? -1: 1
        long long dvd = labs(dividend), dvs = labs(divisor)
        res = 0
        while(dvd >= dvs):
            long long subtractor = dvs, multiplicand = 1
            while(dvd >= (subtractor << 1)):
                subtractor <<= 1
                multiplicand <<= 1
            dvd -= subtractor
            res += multiplicand
        return sign == 1? res: -res
```
------------------------------------------------------------------------------------------------
 Dynamic Programming
=======================
 Dynamic Programming: Using tablulated space to avoid repeated recursive call.
 Traveling Sales Man (TSP) problem Template:
 https:# www.geeksforgeeks.org/bitmasking-dynamic-programming-set-2-tsp/
```
#include <bits/stdc++.h>
using namespace std
#define INF 99999999
#define MAXR 12
#define MAXC 12
#define MAXMASK 2048
#define MAXHOUSE 12
#  stores distance taking souce
#  as every dirty tile
dist[MAXR][MAXC][MAXHOUSE]
#  memoization for dp states
dp[MAXHOUSE][MAXMASK]
#  stores coordinates for
#  dirty tiles
vector < pair < int, > > dirty
#  Directions
X[] = :-1, 0, 0, 1
Y[] = :0, 1, -1, 0
char arr[21][21]
#  len : number of dirty tiles + 1
#  limit : 2 ^ len -1
#  r, c : number of rows and columns
len, limit, r, c
#  Returns true if current position
#  is safe to visit
#  else returns false
#  Time Complexity : O(1)
bool safe(x, y)
:
    if (x >= r or y>= c or x<0 or y<0)
    return false
    if (arr[x][y] == '#')
    return false
    return true
#  runs BFS traversal at tile idx
#  calulates distance to every cell
#  in the grid
#  Time Complexity : O(r*c)
void getDist(idx):
    #  visited array to track visited cells
    bool vis[21][21]
    memset(vis, false, sizeof(vis))
    #  getting current positon
    cx = dirty[idx].first
    cy = dirty[idx].second
    #  initializing queue for bfs
    queue < pair < int, > > pq
    pq.push(:cx, cy)
    #  initializing the dist to max
    #  because some cells cannot be visited
    #  by taking source cell as idx
    for (i = 0i<= ri++)
        for (j = 0j<= cj++)
            dist[i][j][idx] = INF
    #  base conditions
    vis[cx][cy] = true
    dist[cx][cy][idx] = 0
    while (! pq.empty())
    :
        auto x = pq.front()
        pq.pop()
        for (i = 0i<4i++)
        :
        cx = x.first + X[i]
        cy = x.second + Y[i]
        if (safe(cx, cy))
        :
            if (vis[cx][cy])
                continue
            vis[cx][cy] = true
            dist[cx][cy][idx] = dist[x.first][x.second][idx] + 1
            pq.push(:cx, cy)
#  Dynamic Programming state transition recursion
#  with memoization. Time Complexity: O(n*n*2 ^ n)
solve(idx, mask)
:
    #  goal state
    if (mask == limit)
    return dist[0][0][idx]
    #  if already visited state
    if (dp[idx][mask] != -1)
    return dp[idx][mask]
    ret = INT_MAX
    #  state transiton relation
    for (i = 0i<leni++)
    :
        if ((mask & (1<<i)) == 0)
        :
            newMask = mask | (1<<i)
            ret = min( ret, solve(i, newMask)
                + dist[dirty[i].first][dirty[i].second][idx])
    #  adding memoization and returning
    return dp[idx][mask] = ret
void init()
:
    #  initializing containers
    memset(dp, -1, sizeof(dp))
    dirty.clear()
    #  populating dirty tile positions
    for (i = 0i<ri++)
        for (j = 0j<cj++)
        :
            if (arr[i][j] == '*')
            dirty.push_back(:i, j)
    #  inserting ronot's location at the
    #  begining of the dirty tile
    dirty.insert(dirty.begin(), :0, 0)
    len = dirty.size()
    #  calculating LIMIT_MASK
    limit = (1<<len) - 1
    #  precalculating distances from all
    #  dirty tiles to each cell in the grid
    for (i = 0i<leni++)
    getDist(i)
main(argc, char const *argv[])
:
    #  Test case #1:
    #  .....*.
    #  ...#...
    #  .*.#.*.
    #  .......
char A[4][7] = : :'.', '.', '.', '.', '.', '*', '.',
                    :'.', '.', '.', '#', '.', '.', '.',
                    :'.', '*', '.', '#', '.', '*', '.',
                    :'.', '.', '.', '.', '.', '.', '.'
    r = 4 c = 7
    cout << "The given grid : " << endl
    for (i = 0i<ri++)
    :
        for (j = 0j<cj++)
        :
            cout << A[i][j] << " "
            arr[i][j] = A[i][j]
        cout << endl
    #  - initializitiation
    #  - precalculations
    init()
    ans = solve(0, 1)
    cout << "Minimum distance for the given grid : "
    cout << ans << endl
    #  Test Case #2
    #  ...#...
    #  ...#.*.
    #  ...#...
    #  .*.#.*.
    #  ...#...
    char Arr[5][7] = : :'.', '.', '.', '#', '.', '.', '.',
                        :'.', '.', '.', '#', '.', '*', '.',
                        :'.', '.', '.', '#', '.', '.', '.',
                        :'.', '*', '.', '#', '.', '*', '.',
                        :'.', '.', '.', '#', '.', '.', '.'
                #include <bits/stdc++.h>
using namespace std
#define INF 99999999
#define MAXR 12
#define MAXC 12
#define MAXMASK 2048
#define MAXHOUSE 12
#  stores distance taking souce
#  as every dirty tile
dist[MAXR][MAXC][MAXHOUSE]
#  memoization for dp states
dp[MAXHOUSE][MAXMASK]
#  stores coordinates for
#  dirty tiles
vector < pair < int, > > dirty
#  Directions
X[] = :-1, 0, 0, 1
Y[] = :0, 1, -1, 0
char arr[21][21]
#  len : number of dirty tiles + 1
#  limit : 2 ^ len -1
#  r, c : number of rows and columns
len, limit, r, c
#  Returns true if current position
#  is safe to visit
#  else returns false
#  Time Complexity : O(1)
bool safe(x, y)
:
    if (x >= r or y>= c or x<0 or y<0)
    return false
    if (arr[x][y] == '#')
    return false
    return true
#  runs BFS traversal at tile idx
#  calulates distance to every cell
#  in the grid
#  Time Complexity : O(r*c)
void getDist(idx):
    #  visited array to track visited cells
    bool vis[21][21]
    memset(vis, false, sizeof(vis))
    #  getting current positon
    cx = dirty[idx].first
    cy = dirty[idx].second
    #  initializing queue for bfs
    queue < pair < int, > > pq
    pq.push(:cx, cy)
    #  initializing the dist to max
    #  because some cells cannot be visited
    #  by taking source cell as idx
    for (i = 0i<= ri++)
        for (j = 0j<= cj++)
            dist[i][j][idx] = INF
    #  base conditions
    vis[cx][cy] = true
    dist[cx][cy][idx] = 0
    while (! pq.empty())
    :
        auto x = pq.front()
        pq.pop()
        for (i = 0i<4i++)
        :
        cx = x.first + X[i]
        cy = x.second + Y[i]
        if (safe(cx, cy))
        :
            if (vis[cx][cy])
                continue
            vis[cx][cy] = true
            dist[cx][cy][idx] = dist[x.first][x.second][idx] + 1
            pq.push(:cx, cy)
#  Dynamic Programming state transition recursion
#  with memoization. Time Complexity: O(n*n*2 ^ n)
solve(idx, mask)
:
    #  goal state
    if (mask == limit)
    return dist[0][0][idx]
    #  if already visited state
    if (dp[idx][mask] != -1)
    return dp[idx][mask]
    ret = INT_MAX
    #  state transiton relation
    for (i = 0i<leni++)
    :
        if ((mask & (1<<i)) == 0)
        :
            newMask = mask | (1<<i)
            ret = min( ret, solve(i, newMask)
                + dist[dirty[i].first][dirty[i].second][idx])
    #  adding memoization and returning
    return dp[idx][mask] = ret
void init()
:
    #  initializing containers
    memset(dp, -1, sizeof(dp))
    dirty.clear()
    #  populating dirty tile positions
    for (i = 0i<ri++)
        for (j = 0j<cj++)
        :
            if (arr[i][j] == '*')
            dirty.push_back(:i, j)
    #  inserting ronot's location at the
    #  begining of the dirty tile
    dirty.insert(dirty.begin(), :0, 0)
    len = dirty.size()
    #  calculating LIMIT_MASK
    limit = (1<<len) - 1
    #  precalculating distances from all
    #  dirty tiles to each cell in the grid
    for (i = 0i<leni++)
    getDist(i)
main(argc, char const *argv[])
:
    #  Test case #1:
    #  .....*.
    #  ...#...
    #  .*.#.*.
    #  .......
char A[4][7] = : :'.', '.', '.', '.', '.', '*', '.',
                    :'.', '.', '.', '#', '.', '.', '.',
                    :'.', '*', '.', '#', '.', '*', '.',
                    :'.', '.', '.', '.', '.', '.', '.'
    r = 4 c = 7
    cout << "The given grid : " << endl
    for (i = 0i<ri++)
    :
        for (j = 0j<cj++)
        :
            cout << A[i][j] << " "
            arr[i][j] = A[i][j]
        cout << endl
    #  - initializitiation
    #  - precalculations
    init()
    ans = solve(0, 1)
    cout << "Minimum distance for the given grid : "
    cout << ans << endl
    #  Test Case #2
    #  ...#...
    #  ...#.*.
    #  ...#...
    #  .*.#.*.
    #  ...#...
    char Arr[5][7] = : :'.', '.', '.', '#', '.', '.', '.',
                        :'.', '.', '.', '#', '.', '*', '.',
                        :'.', '.', '.', '#', '.', '.', '.',
                        :'.', '*', '.', '#', '.', '*', '.',
                        :'.', '.', '.', '#', '.', '.', '.'
    r = 5 c = 7
    cout << "The given grid : " << endl
    for (i = 0i<ri++)
    :
        for (j = 0j<cj++)
        :
            cout << Arr[i][j] << " "
            arr[i][j] = Arr[i][j]
        cout << endl
    #  - initializitiation
    #  - precalculations
    init()
    ans = solve(0, 1)
    cout << "Minimum distance for the given grid : "
    if (ans >= INF)
        cout << "not possible" << endl
    else
        cout << ans << endl
    return 0
    r = 5 c = 7
    cout << "The given grid : " << endl
    for (i = 0i<ri++)
    :
        for (j = 0j<cj++)
        :
            cout << Arr[i][j] << " "
            arr[i][j] = Arr[i][j]
        cout << endl
    #  - initializitiation
    #  - precalculations
    init()
    ans = solve(0, 1)
    cout << "Minimum distance for the given grid : "
    if (ans >= INF)
        cout << "not possible" << endl
    else
        cout << ans << endl
    return 0
```
 From
 engmonsh
 /
 gist:5231428
```
/**
 * Returns the order to visit predefined products of certain store in minimal distance
 * which returns the sequence number to visit these products
 * 
 * @author Ayman Mahgoub
 * 
 */
public class TravellingSalesMan :
  private double[][] distances
    private short minDistances[][], paths[][]
    private ArrayList<Integer> products_visit_order
    private products_number_power, products_number
    public HashMap<Product, Integer> getOrderForVisitingProducts(
 ArrayList<Product> products) :
        distances = calculateDistanceBetweenProducts(products)
        products_number = products.size()
        /*
 * you represent a subset with a bitmask, which is just an integer. If
 * location i is in the subset, bit number i is set in the integer. For
 * instance, the subset where location 3 and 4 are visited, is
 * represented by the number 24, because bit number 3 (2^3) + bit number
 * 4 (2^4) are set.
 * 
 * suppose if i take 4 vertices 1,2,3,4 then if i visit 1->2->3 then
 * (2^2)+(2^3) =12 d[1][12] will be the distance from 1->2->3
 * 
 * for 1->3->4 (2^3)+(2^4) =24 d[1][24] will be the distance from
 * 1->3->4
 * 
 * SO the matrix length is 2 ^ (product_number)
 */
        products_number_power = (int) Math.pow(2, products_number)
        minDistances = new short[products_number][products_number_power]
        paths = new short[products_number][products_number_power]
        for (i = 0 i < products_number i++) :
            for (j = 0 j < products_number_power j++) :
                minDistances[i][j] = -1
                paths[i][j] = -1
        #  initialize based on distance matrix
        for (i = 0 i < products_number i++) :
            minDistances[i][0] = 0
        #  get value of item[0][products_number_power - 2] which indicates that
        #  we took all the other nodes
        getMinTraversingDistance(0, products_number_power - 2, 1)
        products_visit_order = new ArrayList<Integer>()
        getMinTraversingDistancePath(0, products_number_power - 2)
        HashMap<Product, Integer> productsOrder = new HashMap<Product, Integer>()
        i
        for (i = 1 i < products_number - checkout_points_numbers i++) :
            productsOrder.put(products.get(products_visit_order.get(i - 1)), i)
        minDistances = null
        paths = null
        return productsOrder
    private double getMinTraversingDistance(start, set, level) :
        double temp = 0, result = -1
        masked, mask
        if (minDistances[start][set] != -1) :
            return minDistances[start][set]
         else :
            for (x = 0 x < products_number x++) :
                #  minus Math.pow(2, x), means you removed this node 'x' from
                #  my set to try other possibility
                mask = products_number_power - 1 - (int) Math.pow(2, x)
                masked = set & mask
                if (masked != set) :
                        temp = distances[start][x]
                                + getMinTraversingDistance(x, masked, level + 1)
                    if (result == -1 || result > temp) :
                        result = temp
                        paths[start][set] = (short) x
            minDistances[start][set] = (short) result
            return result
    /**
 * Gets Visiting sequence by moving backwards from source node '0'
 * to destination node
 * 
 * @param start
 * @param set
 */
    private void getMinTraversingDistancePath(start, set) :
        if (paths[start][set] == -1) :
            return
        x = paths[start][set]
        mask = products_number_power - 1 - (int) Math.pow(2, x)
        masked = set & mask
        products_visit_order.add(x)
        getMinTraversingDistancePath(x, masked)
    /**
 * Calculates all the distances (sum of horizontal and vertical distances)
 * between all nodes
 * 
 * @param products
 * @return
 */
    private double[][] calculateDistanceBetweenProducts(List<Product> products) :
        double[][] distances = new double[products.size()][products.size()]
        for (i = 0 i < products.size() i++) :
            for (j = 0 j < products.size() j++) :
                if (i != j) :
                    double distance = Math.abs(products.get(i)
                            .getAverageLocation().x
                            - products.get(j).getAverageLocation().x)
                            + Math.abs(products.get(i).getAverageLocation().y
                                    - products.get(j).getAverageLocation().y)
                    distances[i][j] = distance
        return distances
```
 In C and C++
 (by Neeraj Mishra):
```
#include<stdio.h>
ary[10][10],completed[10],n,cost=0
void takeInput()
:
    i,j
    printf("Enter the number of villages: ")
    scanf("%d",&n)
    printf("\nEnter the Cost Matrix\n")
    for(i=0i < ni++)
    :
        printf("\nEnter Elements of Row: %d\n",i+1)
        for( j=0j < nj++)
            scanf("%d",&ary[i][j])
        completed[i]=0
    printf("\n\nThe cost list is:")
    for( i=0i < ni++)
    :
        printf("\n")
        for(j=0j < nj++)
            printf("\t%d",ary[i][j])
void mincost(city)
:
    i,ncity
    completed[city]=1
    printf("%d--->",city+1)
    ncity=least(city)
    if(ncity==999)
    :
        ncity=0
        printf("%d",ncity+1)
        cost+=ary[city][ncity]
        return
    mincost(ncity)
least(c)
:
    i,nc=999
    min=999,kmin
    for(i=0i < ni++)
    :
        if((ary[c][i]!=0)&&(completed[i]==0))
            if(ary[c][i]+ary[i][c] < min)
            :
                min=ary[i][0]+ary[c][i]
                kmin=ary[c][i]
                nc=i
    if(min!=999)
        cost+=kmin
    return nc
main()
:
    takeInput()
    printf("\n\nThe Path is:\n")
    mincost(0) # passing 0 because starting vertex
    printf("\n\nMinimum cost is %d\n ",cost)
    return 0
```
 Branch And Bound | Set 6 (Traveling Salesman Problem):
 https:# www.geeksforgeeks.org/branch-bound-set-5-traveling-salesman-problem/
------------------------------------------------------------------------------------------------
 72. Edit Distance
=====================
 72. Edit Distance
===================
 Given two wordsword1andword2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
 You have the following 3 operations permitted on a word:
 a) Insert a character
 b) Delete a character
 c) Replace a character
 Thoughts:
1. f[i][j]: minimum number of edit distance between word1[0,...i-1] to word2[0,...j-1].
2. initial state:
	1. f[i][0] = i ( need i operations(deletions) to convert word1[0, i - 1] to empty string)
	2. f[0][j] = j (need j operations (deletions) to convert word2[0, j - 1] to empty string)
3. recursive state:
	1. if word1[i-1] is equal to word2[j-1]: f[i][j] = f[i-1][j-1] (no op on current char)
	2. else min(f[i-1][j-1] + 1 (for replacement), f[i-1][j] + 1 (for deletion of word1[i-1]), f[i][j-1] +1 (for insertion of word2[j-1] to word1[0,...i-1])
4. Optimization: only maintaining a row/column of the original matrix to reduce space complexity to O(n)
 Code time complexity: O(n^2), space complexity: O(n^2)
```python
class Solution :
public:
    minDistance(string word1, string word2) :
        m = word1.length()
        n = word2.length()
        #  f [m + 1][n + 1] fill_n(f, (m+1)*(n+1), 0)
        vector<vector<int>> f (m + 1, vector<int>(n + 1, 0))
        for(i = 1 i <= m i++)
            f[i][0] = i
        for(j = 1 j <= n j++)
            f[0][j] = j
        for(i = 1 i<= m i ++):
            for(j = 1 j <=n j++):
                if(word1[i-1] == word2[j-1]):f[i][j] = f[i-1][j-1]
                else : f[i][j] = min(f[i-1][j-1] + 1, min(f[i - 1][j] + 1, f[i][j-1] + 1))
        return f[m][n]
```
 Code (with optimization) time complexity: O(n^2), space complexity: O(n)
```python
class Solution : 
public:
    minDistance(string word1, string word2) :
        m = word1.length(), n = word2.length()
        vector<int> cur(m + 1, 0)
        for (i = 1 i <= m i++)
            cur[i] = i
        for (j = 1 j <= n j++) :
            pre = cur[0] #  pre records equivalent f[i-1][j-1]
            cur[0] = j
            for (i = 1 i <= m i++) :
                temp = cur[i] 
                if (word1[i - 1] == word2[j - 1])
                    cur[i] = pre
                else cur[i] = min(pre + 1, min(cur[i] + 1, cur[i - 1] + 1)) #  cur[i] + 1: insertion
                                                                             #  cur[i-1] + 1: deletion
                pre = temp #  save f[i - 1][j - 1] for the next state f[i][j]
        return cur[m] 
```
 Special Thanks to the nice
 explanation
 by
 jianchao.li.fighter
------------------------------------------------------------------------------------------------
 535. Encode and Decode TinyURL
==================================
 Note: This is a companion problem to the
 System Design
 problem:
 Design TinyURL
 .
 TinyURL is a URL shortening service where you enter a URL such as
 `https:# leetcode.com/problems/design-tinyurl` 
 and it returns a short URL such as
 `http:# tinyurl.com/4e9iAk` 
 .
 Design the
 `encode` 
 and
 `decode` 
 methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
 Thoughts:
 1. link to algorithm discussed in
 534. Design TinyURL
 :
 Hash Function
 : long_url -> md5/sha1: a. md5 convert a string into 128 binary bits, generally represented as 16 bytes hex:
 http:# site.douban.com/chuan
 -> c93a360dc7f3eb093ab6e304db516653 b. sha1 convert a string into 160 binary bits, generally represented as 20 bytes hex:
 http:# site.douban.com/chuan
 -> dff85871a72c73c3eae09e39ffe97aea63047094
1. 1. These two algorithms could make sure hash values are randomly distributed, implementation-wise simple.
	2. Cons: the conflicts are inevitable. Any hash algorithm could have inevitable conflicts.
	3. Solutions: 1. use (long_url + timestamp) as the hash function key. 2. When conflicts, regenerates the hash value(it's different because timestamp changes).
	 Overall, when urls are over 1 billion, there would be a lot of conflicts and the efficiency could be very low.
2. Base62
 : Take short_url as a 62 base notation. 6 bits could represent 62^6=57 billion.
	1. This implementation simply adopts the base-62 (26*2 letters + 10 digits) mapping to the URL string. Take short_url as a 62 base notation. 6 bits could represent 62^6=57 billion.
	2. Each short_url represent a decimal digit. It could be the auto_increment_id in SQL database.
```
#  You can type code here and execute it.
#include<iostream>
#include<algorithm>
#include<string>
using namespace std
string idToShortURL(long test):
    char map[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    string shorturl
    while(test):
        shorturl.push_back(map[test%62])
        test = test/62
    reverse(shorturl.begin(), shorturl.end())
    return shorturl
long shortURLtoID (string shortURL):
    long id = 0
    for (i = 0 i < shortURL.length() i++):
        if ('a' <= shortURL[i] && shortURL[i]<='z')
            id = id * 62 + shortURL[i] - 'a'
        if ('A' <= shortURL[i] && shortURL[i] <= 'Z')
            id = id * 62 + shortURL[i] - 'A' + 26
        if('0' <= shortURL[i] && shortURL[i]<='9')
            id = id * 62 + shortURL[i] - '0' + 52
    return id
#  function 
main(argc, char** argv) :
    unordered_map<int, string> record
    for (i = 1 i< argc i++):
         cout<<"original URL: "<<(argv[i])<<endl
        record[i] = (argv[i])
    for (i = 1 i< argc i++):
        cout<<"test URL: "<<record[i]<<endl
        string shortURL = idToShortURL(i)
        cout<<"generated URL: "<<shortURL<<endl
        cout<<"Mapped URL back to ID: "<<shortURLtoID(shortURL)<<endl
    #  test = 66666
    #  string shortURL = idToShortURL(test)
    #  cout<<"generated URL: "<<shortURL<<endl
    #  cout<<"Mapped URL back to ID: "<<shortURLtoID(shortURL)<<endl
```
1. Base 62 with Random Generator: by
 StefanPochmann
 's
 post
 The following solution doesn't have these problems. It produces short URLs like
 `http:# tinyurl.com/KtLa2U` 
 , using a random code of six digits or letters. If a long URL is already known, the existing short URL is used and no new entry is generated.
```python
class Codec:
    alphabet = string.ascii_letters + '0123456789'
    def __init__ (self):
        self.long2short = :
        self.short2long = :
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
 :type longUrl: str
 :rtype: str
 """
        while longUrl not in self.long2short:
            # randromly generate a code 
            shortUrl = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            # check the existence
            if shortUrl not in self.short2long:
                self.long2short[longUrl] = shortUrl
                self.short2long[shortUrl] = longUrl
        return 'http:# tinyurl.com/' + shortUrl
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
 :type shortUrl: str
 :rtype: str
 """
        return self.short2long[shortUrl[-6:]]
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```
 It's possible that a randomly generated code has already been generated before. In that case, another random code is generated instead. Repeat until we have a code that's not already in use. How long can this take? Well, even if we get up to using half of the code space, which is a whopping 626/2 = 28,400,117,792 entries, then each code has a 50% chance of not having appeared yet. So the expected/average number of attempts is 2, and for example only one in a billion URLs takes more than 30 attempts. And if we ever get to an even larger number of entries and this does become a problem, then we can just use length 7. We'd need to anyway, as we'd be running out of available codes.
------------------------------------------------------------------------------------------------
 399. Evaluate Division
==========================
 Equations are given in the format
 `A / B = k` 
 , where
 `A` 
 and
 `B` 
 are variables represented as strings, and
 `k` 
 is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return
 `-1.0` 
 .
 Example:
 Given
 `a / b = 2.0, b / c = 3.0.` 
 queries are:
 `a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .` 
 return
 `[6.0, 0.5, -1.0, 1.0, -1.0 ].` 
 The input is:
 `vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries` 
 , where
 `equations.size() == values.size()` 
 , and the values are positive. This represents the equations. Return
 `vector<double>` 
 .
 According to the example above:
```
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
```
 The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
 Thoughts:
1. Explicity building adj list: for permutation of all the pairs of neighbors in one's node i , j, calculate the i , j value as q[i][k] * q[k][j]: assume q[i][i] = 1
2. Union Find
3. DFS
 Code: Building adj list: T: O(n^3), S:(n^2)
```python
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
 :type equations: List[List[str]]
 :type values: List[float]
 :type queries: List[List[str]]
 :rtype: List[float]
 """
        q = collections.defaultdict(dict)
        # build the graph by building the adj list
        for (a, b) , val in zip(equations, values):
            # identity
            q[a][a] = q[b][b] = 1.0
            q[a][b] = val 
            q[b][a] = 1/val
        for k in q:
            for i in q[k]:
                for j in q[k]:
                    q[i][j] = q[i][k] * q[k][j] # connecting nodes explicitly
        return [q[a].get(b, -1.0) for a , b in queries]
```
 Code: DFS + Hash
```python
class Solution :
public:
    vector<double> calcEquation(vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries) :
        unordered_map<string, unordered_map<string, double>> adj
        vector<double> res
        for (i = 0  i < values.size() i++):
            adj[equations[i].first].insert(make_pair(equations[i].second, values[i]))
            adj[equations[i].second].insert(make_pair(equations[i].first, 1/values[i]))
        for (auto q: queries):
            unordered_set<string> s
            double tmp = dfs(adj, s, q.first, q.second)
            if(tmp) res.push_back(tmp)
            else res.push_back(-1)
        return res
private:
    double dfs(unordered_map<string, unordered_map<string, double>>& adj, unordered_set<string>& s, 
 string a, string b):
        if (adj[a].find(b) != adj[a].end()) return adj[a][b]
        for (auto n : adj[a]):
            if(s.find(n.first) == s.end()):
                s.insert(n.first)
                double tmp =  dfs(adj, s, n.first, b)
                if (tmp) return n.second * tmp 
        return 0 #  did not find
```
 Code: Union Find
```python
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
 :type equations: List[List[str]]
 :type values: List[float]
 :type queries: List[List[str]]
 :rtype: List[float]
 """
        def union(n1, n2, val):
            p1, p2 = find(n1), find(n2)
            r = n2.value * val / n1.value # v(n1) * val = v(n2) * r , r = v(n1) * val / v(n2)
            # doing the reverse linear searching for p1's child in the map, normalize the value
            for entry in m.values():
                if find(entry) == p1:
                    entry.value *= r  
            p1.parent = p2
        def find(node):
            while node.parent!= node:
                # node.parent = node.parent.parent
                node = node.parent
            return node
        m, res = :, []
        for i, (a , b) in enumerate(equations):
            value = values[i]
            if a not in m and b not in m:
                node_a, node_b = Node(), Node()
                node_a.value = value
                node_a.parent = node_b
                node_b.value = 1
                m[a] = node_a
                m[b] = node_b
            elif a not in m:
                node_a = Node()
                node_a.value = m[b].value * value
                node_a.parent = m[b]
                m[a] = node_a
            elif b not in m:
                node_b = Node()
                node_b.value = m[a].value / value
                node_b.parent = m[a] # order switched
                m[b] = node_b
            else:
                union(m[a], m[b], value)
        for a, b in queries:
            if a not in m or b not in m or find(m[a]) != find(m[b]):
                res.append(-1)
            else:
                res.append(m[a].value/m[b].value)
        return res
class Node(object):
    def __init__ (self):
        self.parent = self
        self.value = 0
```
------------------------------------------------------------------------------------------------
 282. Expression Add Operators
=================================
 Given a string that contains only digits
 `0-9` 
 and a target value, return all possibilities to add
 binary
 operators (not unary)
 `+` 
 ,
 `-` 
 , or
 `*` 
 between the digits so they evaluate to the target value.
 Example 1:
```
Input:
num = "123", 
target= 6
Output: ["1+2+3", "1*2*3"]
```
 Example 2:
```
Input:
num = "232", 
target = 8
Output: ["2*3+2", "2+3*2"]
```
 Example 3:
```
Input:
num = "105", 
target = 5
Output: ["1*0+5","10-5"]
```
 Example 4:
```
Input:
num = "00", 
target = 0
Output: ["0+0", "0-0", "0*0"]
```
 Example 5:
```
Input:
num = "3456237490", 
target = 9191
Output: []
```
 Thoughts:
1. DFS: expanding each level:
	1. from curDepth to the end of the string, first extract the operand:
	2. if num[curDepth] == '0', stop further expanding since we do not want a number with leading 0's
	3. if current level is 0, then expanding it as the first operator
	4. otherwise: expanding by appending the ['+', '-', '*'] at the end
 Code
```python
class Solution :
    public List<String> addOperators(String num, target) :
        List<String> ans = new ArrayList<>()
        if(num == null || num.length()== 0) return ans
        dfs(ans, num, "", target, 0, 0, 0)
        return ans
    private void dfs(List<String> ans, String num, String path, target, depth, long eval, long lastAdd):
        if(depth == num.length()):
            if(eval == target) ans.add(path)
            return
        for(i = depth i < num.length() i++):
            #  substring the operand, excluding the leading '0' ones 
            if(i > depth && num.charAt(depth) == '0') break
            long cur = Long.parseLong(num.substring(depth, i + 1)) # [depth... i]
            #  global first operand 
            if(depth == 0):
               dfs(ans, num , Long.toString(cur), target, i + 1, cur, cur) #  leading element
            else:
                # add
                dfs(ans,num,path + "+" + cur, target, i + 1, eval + cur, cur)
                # subtract
                dfs(ans,num,path + "-" + cur, target, i + 1, eval - cur, -cur)
                # multiply
                dfs(ans,num,path + "*" + cur, target, i + 1, eval - lastAdd + lastAdd * cur, lastAdd * cur)
```
------------------------------------------------------------------------------------------------
 FB 19
=========
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 760. Find Anagram Mappings
==============================
 Given two lists
 `A` 
 and
 `B` 
 , and
 `B` 
 is an anagram of
 `A` 
 .
 `B` 
 is an anagram of
 `A` 
 means
 `B` 
 is made by randomizing the order of the elements in
 `A` 
 .
 We want to find anindex mapping
 `P` 
 , from
 `A` 
 to
 `B` 
 . A mapping
 `P[i] = j` 
 means the
 `i` 
 th element in
 `A` 
 appears in
 `B` 
 at index
 `j` 
 .
 These lists
 `A` 
 and
 `B` 
 may contain duplicates. If there are multiple answers, output any of them.
 For example, given
```
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
```
 We should return
```
[1, 4, 3, 2, 0]
```
 as
 `P[0] = 1` 
 because the
 `0` 
 th element of
 `A` 
 appears at
 `B[1]` 
 , and
 `P[1] = 4` 
 because the
 `1` 
 st element of
 `A` 
 appears at
 `B[4]` 
 , and so on.
 Note:
1. `A, B` 
 have equal lengths in range
 `[1, 100]` 
 .
2. `A[i], B[i]` 
 are integers in range
 `[0, 10^5]` 
 .
 Thoughts:1
1. (K,V) : (value, list of (index of B))
2. get the value of A[i], retrieve the last element from the mapped list
 Code
```python
class Solution :
    public int[] anagramMappings(int[] A, int[] B) :
        [] result = new [A.length]
        Map<Integer, List<Integer>> map = new HashMap<>()
        for( i = 0 i < B.length i++):
            map.computeIfAbsent(B[i], k->new ArrayList<>()).add(i)
        for( i = 0 i < A.length i++):
            result[i] = map.get(A[i]).remove(map.get(A[i]).size() - 1)
        return result
```
 from
 diddit
 's
 post
 Use Sorting:
```python
public int[] anagramMappings(int[] A, int[] B) :
    n = A.length
    for(i = 0 i < n i++) :
        A[i] = (A[i] << 8) + i
        B[i] = (B[i] << 8) + i
    Arrays.sort(A)
    Arrays.sort(B)
    int[] ans = new int[n]
    for(i = 0 i < n i++)
        ans[A[i] & 0xFF] = B[i] & 0xFF
    return ans
```
 from
 tyuan73
 's
 post
```python
class Solution :
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) :
        vector<int> result
        unordered_multimap<int, int> m
        for(i = 0 i < B.size() i++):
            m.emplace(B[i],i)
        for(i: A):
            auto iter = m.find(i)
            result.push_back(iter->second) #  iter->first: value from B iter->second: associated index in B
            #  cout<<"iter->first: "<<(iter->first)<<" iter->second: "<<(iter->second)<<endl
            m.erase(iter)
        return result
```
 from
 PuckDuck
 's
 post
 fastest C++:
```
hashFn(input) :
    return input % 100
class Solution :
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) :
        unordered_map<int, int> bHash
        vector<int> P
        for (i = 0 i < B.size() i++) :
            bHash[B[i]] = i
        for (i = 0 i < A.size() i++) :
            P.push_back(bHash[A[i]])
        return P
```
 fastest
 Java
```
/*
 A = [1,3,2]
 B = [1,2,3]
 output = [0,2,1]
*/
class Solution :
    public int[] anagramMappings(int[] A, int[] B) :
        int[] ret = new int[A.length]
        for (i = 0  i < ret.length  i++) :
            ret[i] = indexOf(B, A[i])
        return ret
    private indexOf(int[] target, value) :
        for (i = 0  i < target.length i++) :
            if (target[i] == value) :
                return i
        return -1
```
 fastest
 Python
```python
class Solution(object):
    def anagramMappings(self, A, B):
        """
 :type A: List[int]
 :type B: List[int]
 :rtype: List[int]
 """
        # mapped to the same index of B if duplicates exist
        C = :x : i for i, x in enumerate(B)
        return [C[x] for x in A]
```
------------------------------------------------------------------------------------------------
 295. Find Median from Data Stream
=====================================
 Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
 For example,
`[2,3,4]` 
 , the median is
 `3` 
`[2,3]` 
 , the median is
 `(2 + 3) / 2 = 2.5` 
 Design a data structure that supports the following two operations:
* void addNum(num) - Add a integer number from the data stream to the data structure.
* double findMedian() - Return the median of all elements so far.
 Example:
```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```
 Follow up:
1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it? (Segment Trees)
3. how to improve it and make sure the method is thread-safe if the two heaps are shared - Use read and write locks.
 Thoughts:
1. Having two queues, one (right part) puts smallest number on the top, and one (left part) keeps largest element on the top.
2. Using Binary Search Tree: As the input numbers are random, so the height of the binary search tree is O(logN) We maintain every single node's children's size and it's easy to implement because it just has add operation.
3. #### 
 Further Thoughts (Analysis written by
 @babhishek21
 )
 There are so many ways around this problem, that frankly, it is scary. Here are a few more that I came across:
	* Buckets!
	 If the numbers in the stream are statistically distributed, then it is easier to keep track of buckets where the median would land, than the entire array. Once you know the correct bucket, simply sort it find the median. If the bucket size is significantly smaller than the size of input processed, this results in huge time saving.
	 @mitbbs8080
	 has an interesting implementation
	 here.
	* Reservoir Sampling.
	 Following along the lines of using buckets: if the stream is statistically distributed, you can rely on Reservoir Sampling. Basically, if you could maintain just one good bucket (or
	 ---reservoir--- 
	 ) which could hold a representative sample of the entire stream, you could estimate the median of the entire stream from just this one bucket. This means good time and memory performance. Reservoir Sampling lets you do just that. Determining a
	 "good"
	 size for your reservoir?_Now, that's a whole other challenge. A good explanation for this can be found in
	 this StackOverflow answer.
	* Segment Trees
	 are a great data structure if you need to do a lot of insertions or a lot of read queries over a limited range of input values. They allow us to do all such operations
	 ---fast
	 and
	 in
	 roughly the same amount of time--- 
	 , always
	 .
	 The only problem is that they are far from trivial to implement. Take a look at my
	 introductory article on Segment Trees
	 if you are interested.
	* Order Statistic Trees
	 are data structures which seem to be tailor-made for this problem. They have all the nice features of a BST, but also let you find the k^:th ​​order element stored in the tree. They are a pain to implement and no standard interview would require you to code these up. But they are fun to use if they are already implemented in the language of your choice.
	 5
4. Code
```python
class MedianFinder :
    /** initialize your data structure here. */
    private Queue<Long> left
    private Queue<Long> right
    public MedianFinder() :
            left = new PriorityQueue()
            right = new PriorityQueue()
    public void addNum(num) :
        right.add((long) num)
        left.add(-right.poll())
        if(right.size() < left.size())
            right.add(-left.poll())
    public double findMedian() :
        return right.size() > left.size()
            ?right.peek()
            :(right.peek() - left.peek())/2.0 
/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder()
 * obj.addNum(num)
 * double param_2 = obj.findMedian()
 */
```
 Java: reverse ordering
```python
class MedianFinder :
    /** initialize your data structure here. */
    private Queue<Integer> l
    private Queue<Integer> r
    boolean even
    public MedianFinder() :
            l = new PriorityQueue()
            r = new PriorityQueue(Collections.reverseOrder())
            even = true
    public void addNum(num) :
             if(even):
                l.add(num)
                r.add(l.poll())
            else:
                r.add(num)
                l.add(r.poll())
        even=!even
    public double findMedian() :
         return even?(r.peek() + l.peek()) / 2.0:r.peek()
/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder()
 * obj.addNum(num)
 * double param_2 = obj.findMedian()
 */
```
 C++: max_heap
```python
class MedianFinder :
    priority_queue<long> left, right#  max_heap
public:
    /** initialize your data structure here. */
    MedianFinder() :
    void addNum(num) :
        left.push(num)
        right.push(-left.top()) left.pop()
        if(left.size() < right.size()):
            left.push(-right.top()) right.pop()
    double findMedian() :
        return left.size() > right.size()
            ? left.top()
            : (left.top() - right.top())/2.0
/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder()
 * obj.addNum(num)
 * double param_2 = obj.findMedian()
 */
```
 Python
```
from heapq import *
class MedianFinder(object):
    def __init__(self):
        """
 initialize your data structure here.
 """
        self.heaps = [], []
    def addNum(self, num):
        """
 :type num: int
 :rtype: void
 """
        left, right = self.heaps # min heap
        heappush(left, -heappushpop(right, num))
        if len(right) < len(left):
            heappush(right, -heappop(left))
    def findMedian(self):
        """
 :rtype: float
 """
        left, right = self.heaps
        if len(right) > len(left):
            return float(right[0])
        return (right[0] - left[0])/2.0        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
 Code: BST (
 Even if the incoming data ins't random, we can still use
 red-black tree
 so that finding median value is super fast.)
```
struct BST :
    struct node :
        val
        size
        node* left, *right
        node(v) : size(1), val(v) :
     *Null, *root
    BST() :
        Null = new node(0)
        Null -> size = 0
        root = Null
    void add(val, node*& R) :
        if(R == Null) :
            R = new node(val)
            R -> left = R -> right = Null
            return
        if(R->val <= val) add(val, R->left)
        else add(val, R->right)
        R->size = R->left->size + R->right->size + 1
    rank(k) :
        node* t = root
        while(true) :
            leftSize =  t -> left -> size
            if(leftSize == k) return t -> val
            if(leftSize > k) :
                t = t -> left
             else :
                k = k - leftSize - 1
                t = t -> right
        return -1
class MedianFinder :
public:
    BST* bst
    MedianFinder() :
        bst = new BST()
    #  Adds a number into the data structure.
    void addNum(num) :
        bst->add(num, bst->root)
    #  Returns the median of current data stream
    double findMedian() :
        sz = bst -> root -> size
        if(sz % 2 == 0) :
            return 1.0 * (bst -> rank(sz / 2) + bst -> rank(sz / 2 - 1)) / 2
         else return bst->rank(sz / 2)
```
 Binary Search: O(n) (
 Add function may cost o(n).Insert function costs o(n))
```
private List<double> m_listNum = new List<double>()
public void AddNum(double num) :
    lintPos = m_listNum.BinarySearch( num ) 
    if (lintPos >= 0) :
        m_listNum.Insert(lintPos, num)
     else :
        lintPos = ~lintPos
        if (lintPos == m_listNum.Count) :
            m_listNum.Add(num)
         else :
            m_listNum.Insert(lintPos, num)
#  return the median of current data stream
public double FindMedian() :
    lintCount = m_listNum.Count 
    if (lintCount == 0 ) throw new Exception("array is empty")
    if (lintCount % 2 == 0)
        return (m_listNum[lintCount / 2 - 1] + m_listNum[lintCount / 2]) / 2
    else 
        return m_listNum[lintCount / 2]
```
 Reference:
 StefanPochmann
 's
 post
 and
 lgn
 's
 post
------------------------------------------------------------------------------------------------
 277. Find the Celebrity
===========================
 Suppose you are at a party with
 `n` 
 people (labeled from
 `0` 
 to
 `n - 1` 
 ) and among them, there may exist one celebrity. The definition of a celebrity is that all the other
 `n - 1` 
 people know him/her but he/she does not know any of them.
 Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
 You are given a helper function
 `bool knows(a, b)` 
 which tells you whether A knows B. Implement a function
 `findCelebrity(n)` 
 , your function should minimize the number of calls to
 `knows` 
 .
 Note
 : There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return
 `-1` 
 .
 Thoughs:
1. O(3n): Explanation from
 scy_usc
 in
 here
	1. :The first loop will stop to an candidate i who doesn't know anyone from i+1 to n-1. For any previous x<i either know sb else or is not known by sb else.
	2. The second loop will check whether i knows anyone from 0 to i-1.
	3. The third loop is gonna check whether all party participants know x or not.
2. O(2n): Explanation from
 czonzhu
 in
 here
	1. The first pass is to pick out the candidate. If candidate knows i, then switch candidate.
	2. The second pass is to check whether the candidate is real.
 Code
```
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
class Solution(object):
    def findCelebrity(self, n):
        """
 :type n: int
 :rtype: int
 """
        ix = 0
        # check if someone knows ix and ix does not know anyone from ix + 1 to n -1
        for i in range(n):
            if knows(ix, i):
                ix = i
        if any(knows(ix, i) for i in range(ix)): return -1 # check if ix knows any one from 0 to ix -1
        if any(not knows(i, ix) for i in range(n)): return -1 # check if everyone else knows ix
        return ix
```
------------------------------------------------------------------------------------------------
 341. Flatten Nested List Iterator
=====================================
 Given a nested list of integers, implement an iterator to flatten it.
 Each element is either an integer, or a list -- whose elements may also be integers or other lists.
 Example 1:
```
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by nextshould be: [1,1,2,1,1].
```
 Example 2:
```
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
```
 Thoughts:
1. Recursive structure: Use a stack to add element: from back to front
2. hasNext(): check the top element is integer, if not flatten the top element and add it from back to front to the stack
 Code
```
/**
 * #  This is the interface that allows for creating nested lists.
 * #  You should not implement it, or speculate about its implementation
 * public interface NestedInteger :
 *
 * #  @return true if this NestedInteger holds a single integer, rather than a nested list.
 * public boolean isInteger()
 *
 * #  @return the single integer that this NestedInteger holds, if it holds a single integer
 * #  Return null if this NestedInteger holds a nested list
 * public Integer getInteger()
 *
 * #  @return the nested list that this NestedInteger holds, if it holds a nested list
 * #  Return null if this NestedInteger holds a single integer
 * public List<NestedInteger> getList()
 * 
 */
public class NestedIterator implements Iterator<Integer> :
    Stack<NestedInteger> stack
    public NestedIterator(List<NestedInteger> nestedList) :
        stack = new Stack<>()
        for(i = nestedList.size() -1 i >= 0 i--):
            stack.push(nestedList.get(i))
    @Override
    public Integer next() :
        return stack.pop().getInteger()
    @Override
    public boolean hasNext() :
        while(!stack.isEmpty()):
            NestedInteger cur = stack.peek()
            if(cur.isInteger()) return true
            stack.pop()
            for(i = cur.getList().size() - 1 i >=0 i--)
                stack.push(cur.getList().get(i))
        return false
/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList)
 * while (i.hasNext()) v[f()] = i.next()
 */
```
------------------------------------------------------------------------------------------------
 Flatten
===========
------------------------------------------------------------------------------------------------
 733. Flood Fill
===================
 An
 `image` 
 is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
 Given a coordinate
 `(sr, sc)` 
 representing the starting pixel (row and column) of the flood fill, and a pixel value
 `newColor` 
 , "flood fill" the image.
 To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
 At the end, return the modified image.
 Example 1:
```
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output:
 [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
```
 Note:
 The length of
 `image` 
 and
 `image[0]` 
 will be in the range
 `[1, 50]` 
 .
 The given starting pixel will satisfy
 `0 <= sr < image.length` 
 and
 `0 <= sc < image[0].length` 
 .
 The value of each color in
 `image[i][j]` 
 and
 `newColor` 
 will be an integer in
 `[0, 65535]` 
 .
 Thoughts:
1. DFS with visited map
2. DFS without visited map: only need to change the value at int[][]image.
 Code: DFS with visited map
```python
class Solution :
    public static d [] = :0,1,0,-1,0
    public int[][] floodFill(int[][] image, sr, sc, newColor) :
        m = image.length, n = image[0].length
        int[][] visited = new [m][n]
        dfs(image, sr, sc, m, n, image[sr][sc], newColor,visited)
        return image
    private void dfs(int[][] image, sr, sc, m, n, oldColor, newColor,int[][] visited):
        if(sr < 0 || sr >= m || sc < 0 || sc >= n || image[sr][sc] != oldColor) return
        if (visited[sr][sc] == 1) return
        image[sr][sc] = newColor
        visited[sr][sc] = 1
        for(i = 0 i < 4 i++):
            x = sr + d[i], y = sc + d[i + 1]
            dfs(image,x,y,m,n,oldColor, newColor,visited)
```
 Code: DFS without visited map
```python
class Solution :
    public static d [] = :0,1,0,-1,0
    public int[][] floodFill(int[][] image, sr, sc, newColor) :
        m = image.length, n = image[0].length
        if(newColor == image[sr][sc]) return image #  only need to check if there is a change
        dfs(image, sr, sc, m, n, image[sr][sc], newColor)
        return image
    private void dfs(int[][] image, sr, sc, m, n, oldColor, newColor):
        if(sr < 0 || sr >= m || sc < 0 || sc >= n || image[sr][sc] != oldColor) return
        image[sr][sc] = newColor
        for(i = 0 i < 4 i++):
            x = sr + d[i], y = sc + d[i + 1]
            dfs(image,x,y,m,n,oldColor, newColor)
```
------------------------------------------------------------------------------------------------
 597. Friend Requests I: Overall Acceptance Rate
===================================================
 In social network like Facebook or Twitter, people send friend requests and accept others’ requests as well. Now given two tables as below:
 Table:
`friend_request` 
```
| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016_06-01 |
| 1         | 3          | 2016_06-01 |
| 1         | 4          | 2016_06-01 |
| 2         | 3          | 2016_06-02 |
| 3         | 4          | 2016-06-09 |
```
 Table:
`request_accepted` 
```
| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |
```
 Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.
 For the sample data above, your query should return the following result.
```
|accept_rate|
|-----------|
|       0.80|
```
 Note:
 The accepted requests are not necessarily from the table
 `friend_request.` 
 In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
 It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances are only counted once.
 If there is no requests at all, you should return 0.00 as the accept_rate.
 Explanation:
 There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.
 Follow-up:
 Can you write a query to return the accept rate but for every month?
 How about the cumulative accept rate for every day?
```
# Write your MySQL query statement below
SELECT ifnull(Round(count(distinct requester_id, accepter_id) / count(distinct sender_id, send_to_id), 2),0) as accept_rate
FROM request_accepted, friend_request
```
 Follow up:
 https:# leetcode.com/problems/friend-requests-i-overall-acceptance-rate/discuss/103579/Following-up-questions.-Solved-Q1-how-to-solve-Q2
```
select if(d.req =0, 0.00, round(c.acp/d.req,2)) as accept_rate, c.month from 
(select count(distinct requester_id, accepter_id) as acp, Month(accept_date) as month from request_accepted) c, 
(select count(distinct sender_id, send_to_id) as req, Month(request_date) as month from friend_request) d 
where c.month = d.month 
group by c.month
```
	1.
```
 SELECT 
    `date`, (@csum := @csum + accept_rate) as daily_cumulative_accept_rate
FROM
    (
    SELECT
        `date`, SUM(IF(`action`='ACCEPT', `count`, 0)) / SUM(IF(`action`='SEND', `count`, 0)) as accept_rate
    FROM
        (
        SELECT 
            request_date as `date`, COUNT(DISTINCT sender_id, send_to_id) as `count`, 'SEND' as `action`
        FROM
            friend_request
        GROUP BY
            request_date
        UNION
        SELECT 
            accept_date as `date`, COUNT(DISTINCT requester_id, accepter_id) as `count`, 'ACCEPT' as `action`
        FROM
            request_accepted
        GROUP BY
            accept_date) as t1
    GROUP BY
        `date`
    ORDER BY
        `date`) as t2, (SELECT @csum := 0) as t3
```
------------------------------------------------------------------------------------------------
 friends
===========
 http:# www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=437487&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption[3088][value]%3D1%26searchoption[3088][type]%3Dradio%26searchoption[3090][value]%3D2%26searchoption[3090][type]%3Dradio%26searchoption[3046][value]%3D2%26searchoption[3046][type]%3Dradio%26sortid%3D311
1. getMutualFriends()
 use one set to store friends from the other guy and collect all the friends of you that is in the set.
 给你一个getfriends的function然后写找共同好友 (s1.retainAll(s2)). T:O(n)
 2.suggest（）
 排序好友的好友，谁共同好友多就放前面。。
 每个都问了下run time
 第2题我有点卡了，最后提示用了hashmap但我不知道map怎么用value来排序。。
```
/**
 * Created by Zirui Tao on 9/8/2018.
 */
import java.util.*
public class Friends :
    String name
    List<Friends> friends
    public static void main(String [] args):
         Friends me = new Friends("zirui")
         Friends zero = new Friends("zero")
         Friends one = new Friends("one")
         Friends two = new Friends("two")
         Friends three = new Friends("three")
         Friends four = new Friends("four")
         me.friends = Arrays.asList(one, two ,three)
         zero.friends = Arrays.asList(one, three, four)
         one.friends = Arrays.asList(me, zero, two ,three, four)
         two.friends = Arrays.asList(me, one)
         three.friends = Arrays.asList(me, zero, one, four)
         four.friends = Arrays.asList(zero,  one, three)
#  me.findCommon(zero)
         me.rank(zero)
    public Friends(String name, List<Friends> friends):
        this.name= name
        this.friends = friends
    public Friends(String name):
        this.name= name
        this.friends = null
    public List<Friends> findCommon(Friends o):
#  O(n)
        Set<Friends> set = new HashSet<Friends>(o.friends)
        set.retainAll(this.friends)
#  set.forEach(n -> System.out.print(n.name + " "))
#  System.out.println()
        return new ArrayList<>(set)
    public void rank(Friends o):
        #  <Integer, String> find the O(n): n: size of friends
        Map<Integer, List<String>> rank = new HashMap<>()
        for (Friends f:  this.findCommon(o)):
            key = this.findCommon(f).size()
            List<String> l = rank.getOrDefault(key, new ArrayList<String>())
            l.add(f.name)
            rank.put(key,l)
        #  traverse through the friends ranks map O(n ^2) since print takes O(n)
        for ( i = this.friends.size() i >= 0 i--):
            if (rank.get(i) != null) :
                rank.get(i).forEach(x -> System.out.print(x))
                System.out.println()
        System.out.println()
        #  alternatively using sort: O(n^2logn) since sort takes O(nlogn) to sort and O(n) to print
#  SortedSet<Integer> keys = new TreeSet<>(new Comparator<Integer>():
#  @Override
#  public compare(Integer i1, Integer i2):
#  return i2 - i1
#  
#  )
# 
#  keys.addAll(rank.keySet())
# #  keys.forEach(x-> rank.get(x).forEach(y->System.out.print(y)))
#  for(Integer key: keys):
#  rank.get(key).forEach(x-> System.out.print(x))
#  System.out.println()
#  
```
------------------------------------------------------------------------------------------------
 Graph
=========
------------------------------------------------------------------------------------------------
 261. Graph Valid Tree
=========================
 261. Graph Valid Tree
=======================
 Given
 `n` 
 nodes labeled from
 `0` 
 to
 `n - 1` 
 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
 For example:
 Given
 `n = 5` 
 and
 `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]` 
 , return
 `true` 
 .
```
0 ----- 3
|\
| \ 
|  \       
1   2 
|
4
```
 Given
 `n = 5` 
 and
 `edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]` 
 , return
 `false` 
 .
```
0---1--2
    /\/
    |/\ 
    3   4
```
 Note
 : you can assume that no duplicate edges will appear in
 `edges` 
 . Since all edges are undirected,
 `[0, 1]` 
 is the same as
 `[1, 0]` 
 and thus will not appear together in
 `edges` 
 .
 Thoughts:
1. Use Union-Find to detect cycles: a. initialize an array of size as number of nodes in the graph with a value as -1. b. for each edge, explore their "roots" , if their roots are not the same, replace the root of one to the other (make them connected) otherwise, if their roots are the same, it means two nodes are already belong to the same connected components, add add extra edge would result in
 cycle
 .
2. Time Complexity O(n * len(edges))-> since each time of exploring edges there might be at most n - 1 traversing to find the current node's root. Space Complexity: O(n)
 Code
```python
class Solution :
public:
    bool validTree(n, vector<pair<int, int>>& edges) :
        m = edges.size()
        if(n < 1 || edges.size()!= n - 1) return false
        roots[n]
        fill_n(roots, n, -1)
        for(pair<int,int> p: edges):
            roota = find(roots, p.first)
            rootb = find(roots, p.second)
            #  cycle detection
            if(roota == rootb) return false
            roots[roota] = rootb
        return true
    find ( roots [], v):
        while(roots[v] != -1) v = roots[v]
        return v
```
------------------------------------------------------------------------------------------------
 Greedy
==========
 Greedy
 usually cannot leave without some types of sorting, in combination with partitioning (sort in dictionary)
------------------------------------------------------------------------------------------------
 Heap
========
------------------------------------------------------------------------------------------------
 198. House Robber
=====================
 198. House Robber
===================
 You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
 it will automatically contact the police if two adjacent houses were broken into on the same night
 .
 Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight
 without alerting the police
 .
 Credits:
 Special thanks to
 @ifanchu
 for adding this problem and creating all test cases. Also thanks to
 @ts
 for adding additional test cases.
 Thoughts
1. one looking ahead: not only considering whether to include or exclude this house, but also considering whether to include or exclude the previous house.
 Code ( a , b alternating updates)
```python
class Solution :
public:
    rob(vector<int>& A) :
        n = A.size()
        a = 0, b= 0
        for(i = 0  i < n i++):
            if(i%2 == 0):
                a = max(b, a + A[i])
            else:
                b = max(a, b + A[i])
        return max(a,b)
```
 Code ()
```python
class Solution :
public:
    rob(vector<int>& A) :
        n = A.size()
        a = 0, e= 0
        for(i = 0  i < n i++):
            tmp = a
            #  update current a and e
            a = e + A[i]
            e = max(tmp, e) #  whether to include previous house or exclude
        return max(a,e)
```
------------------------------------------------------------------------------------------------
 Identifying Triangle
========================
 Write a query identifying the_type_of each record in the
 TRIANGLES
 table using its three side lengths. Output one of the following statements for each record in the table:
* Equilateral
 : It's a triangle with 3 sides of equal length.
* Isosceles
 : It's a triangle with 2 sides of equal length.
* Scalene
 : It's a triangle with 3 sides of differing lengths.
* Not A Triangle
 : The given values of
 ---A--- 
 ,
 ---B--- 
 , and _C _don't form a triangle.
 Input Format
 The
 TRIANGLES
 table is described as follows:
![](https:# s3.amazonaws.com/hr-challenge-images/12887/1443815629-ac2a843fb7-1.png)
 Each row in the table denotes the lengths of each of a triangle's three sides.
 Sample Input
![](https:# s3.amazonaws.com/hr-challenge-images/12887/1443815827-cbfc1ca12b-2.png)
 Sample Output
```
Isosceles
Equilateral
Scalene
Not A Triangle
```
 Explanation
 Values in the tuple $$(20, 20, 23)$$ form an Isosceles triangle, because $$A \equiv B$$.
 Values in the tuple $$(20,20,20)$$ form an Equilateral triangle, because $$A \equiv B \equiv C$$.
 Values in the tuple $$(20, 21, 22)$$ form a Scalene triangle, because $$A \not= B \not= C$$.
 Values in the tuple $$(13,14,30)$$ cannot form a triangle because the combined value of sides $$A$$ and $$B$$ is not larger than that of side $$C$$.
 Thoughts:
1. Ideas from
 GeeksforGeeks
 Code
```
SELECT 
CASE WHEN A + B > C AND A+C>B AND B+C>A 
THEN CASE WHEN A = B AND B = C 
THEN 'Equilateral' WHEN A = B OR B = C OR A = C 
THEN 'Isosceles' WHEN A != B OR B != C OR A != C 
THEN 'Scalene' END ELSE 'Not A Triangle' 
END 
FROM TRIANGLES
```
------------------------------------------------------------------------------------------------
 208. Implement Trie (Prefix Tree)
=====================================
 Implement a trie with
 `insert` 
 ,
 `search` 
 , and
 `startsWith` 
 methods.
 Example:
```
Trie trie = new Trie()
trie.insert("apple")
trie.search("apple")   #  returns true
trie.search("app")     #  returns false
trie.startsWith("app") #  returns true
trie.insert("app")   
trie.search("app")     #  returns true
```
 Thoughts:
1. Design the TrieNode with three field: val, is Word, and Children list.
2. Go through each element and if current letter is not in current node's children set, it means there is currently no record.
3. If found such letter, then check there is a word ending there by accessing the field "isWord".
 Code Java
```python
class TrieNode:
    char val
    boolean isWord
    TrieNode[] children = new TrieNode[26]
    public TrieNode():
    TrieNode(char c):
        val = c
public class Trie :
    private TrieNode root
    /** Initialize your data structure here. */
    public Trie() :
        root = new TrieNode()
        root.val = ' '
    /** Inserts a word into the trie. */
    public void insert(String word) :
        TrieNode cur = root
        for(i = 0 i < word.length() i++):
            char c = word.charAt(i)
            if(cur.children[c-'a']== null) cur.children[c-'a'] = new TrieNode(c)
            cur = cur.children[c-'a']
        cur.isWord = true
    /** Returns if the word is in the trie. */
    public boolean search(String word) :
        TrieNode cur = root
        for(i = 0 i < word.length() i++):
            char c = word.charAt(i)
            if(cur.children[c-'a']== null) return false
            cur = cur.children[c-'a']
        return cur.isWord
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) :
        TrieNode cur = root
        for(i = 0 i < prefix.length() i++):
            char c = prefix.charAt(i)
            if(cur.children[c-'a']==null) return false
            cur = cur.children[c-'a']
        return true
/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie()
 * obj.insert(word)
 * boolean param_2 = obj.search(word)
 * boolean param_3 = obj.startsWith(prefix)
 */
```
 from
 mlblount45
 's
 post
------------------------------------------------------------------------------------------------
 491. Increasing Subsequences
================================
 Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .
 Example:
```
Input:[4, 6, 7, 7]
Output:[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
```
 Note:
1. The length of the given array will not exceed 15.
2. The range of integer in the given array is [-100,100].
3. The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
 Thoughts:
1. dfs + use list to record tracking, use set to prevent redundance:
2. Code: Java: Standard backtracking
```python
class Solution :
    public List<List<Integer>> findSubsequences(int[] A) :
        List<List<Integer>>res = new ArrayList<>()
        List<Integer> element = new ArrayList<>()
        dfs(res, element, 0, A)
        return new ArrayList(res)
    private void dfs(List<List<Integer>>res, List<Integer> element, pos, int[] A):
        if(element.size()>= 2) res.add(new ArrayList(element))
        Set<Integer> s = new HashSet<>(A.length)
        for (i  = pos i < A.length i++):
            if ((element.size() == 0 || element.get(element.size() - 1) <= A[i] )&& !s.contains(A[i])):
                element.add(A[i])
                dfs(res, element, i + 1, A)
                element.remove(element.size() - 1)
                s.add(A[i])
```
 Code: C++: Standard backtracking with hash checking
```python
class Solution :
public:
    vector<vector<int>> findSubsequences(vector<int>& A) :
         vector<vector<int>> res
         vector<int> element
         dfs(res, element, A,  0)
         return res
private:
    void dfs(vector<vector<int>>& res, vector<int>& element, vector<int>& A, pos):
        if (element.size() > 1) res.push_back(element)
        unordered_set<int> set 
        for(i = pos i < A.size() ++i):
            if((element.empty() || element.back() <= A[i]) && set.find(A[i]) == set.end()):
                element.push_back(A[i])
                dfs(res, element, A, i + 1)
                element.pop_back()
                set.insert(A[i])
```
 Using python itertools.combinations
```python
class Solution(object):
    def findSubsequences(self, A):
        """
 :type A: List[int]
 :rtype: List[List[int]]
 """
        return [ x
                for i in range(2, len(A) + 1)
                for x in set(itertools.combinations(A,i))
                if all(a <= b for a, b in zip(x, x[1:]))
        ]
```
------------------------------------------------------------------------------------------------
 285. Inorder Successor in BST
=================================
 Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
 Note
 : If the given node has no in-order successor in the tree, return
 `null` 
 .
 Example 1:
```
Input:
 root = [2,1,3], p = 1
  2
 / \
1   3
Output: 2
```
 Example 2:
```
Input:
 root = [5,3,6,2,4,null,null,1], p = 6
      5
     / \
    3   6
   / \
  2   4
 /   
1
Output:null
```
 Thoughts:
 Utilize the binary search property of BST: during the traversal: if a node is about to traverse to its left. Then record the node as successor before doing so.
 Code: T: O(h) -> O(logn)
 Python
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
 :type root: TreeNode
 :type p: TreeNode
 :rtype: TreeNode
 """
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
```
 C++
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) :
        TreeNode* suc = NULL
        while(root ):
            if(root-> val > p ->val) :
                suc = root
                root = root -> left
            else root = root -> right
        return suc
```
 Java
```python
public TreeNode inorderSuccessor(TreeNode root, TreeNode p) :
    TreeNode succ = null
    while (root != null) :
        if (p.val < root.val) :
            succ = root
            root = root.left
        else
            root = root.right
    return succ
```
------------------------------------------------------------------------------------------------
 381. Insert Delete GetRandom O(1) - Duplicates allowed
==========================================================
 Design a data structure that supports all following operations inaverage
 O(1)
 time.
 Note: Duplicate elements are allowed.
1. `insert(val)` 
 : Inserts an item val to the collection.
2. `remove(val)` 
 : Removes an item val from the collection if present.
3. `getRandom` 
 : Returns a random element from current collection of elements. The probability of each element being returned is
 linearly related
 to the number of same value the collection contains.
 Example:
```
#  Init an empty collection.
RandomizedCollection collection = new RandomizedCollection()
#  Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1)
#  Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1)
#  Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2)
#  getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom()
#  Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1)
#  getRandom should return 1 and 2 both equally likely.
collection.getRandom()
```
 Thoughts:
1. A: data lsit
2. indiecs: index reverse mapping: <val, i>
3. for add: check key is in the indices list set. if not put a new set in to val: <val, new set> add i as current A.size(), then add value to data array A.
4. for remove: for check if the val is a valid key: if it is, retrieve the next index value for the val as iterator.next(), remove the index value from val entry. Then i is not at the end of the A. Then fill the last element to the ith position in the A list:
	1. retrieve the value from the last element in A as "last"
	2. updating last's position entry record in set by first removing old index value then add value of position to be filled to the set
	3. remove the last element from the data A.
	4. check the set in val becomes empty, if it is, remove the set entry in map.
 Code: java
```python
class RandomizedCollection :
    ArrayList<Integer> A
    HashMap<Integer, Set<Integer>> indices
    java.util.Random rand 
    /** Initialize your data structure here. */
    public RandomizedCollection() :
        A = new ArrayList<>()
        rand = new java.util.Random()
        indices = new HashMap<>()
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(val) :
        boolean contain = indices.containsKey(val)
        if(!contain) indices.put(val, new LinkedHashSet<>())
        indices.get(val).add(A.size())
        A.add(val)
        return !contain
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(val) :
        boolean contain = indices.containsKey(val)
        if (!contain) return false
        i = indices.get(val).iterator().next()
        #  remove from indices record
        indices.get(val).remove(i)
        #  remove from A data
        if(i < A.size() -1):
            last = A.get(A.size() -1)
            A.set(i, last)
            #  update last's record
            indices.get(last).remove(A.size() - 1)
            indices.get(last).add(i)
        A.remove(A.size() - 1) #  remove last element
        #  check set entry is empty()?
        if(indices.get(val).isEmpty()) indices.remove(val)
        return true
    /** Get a random element from the collection. */
    public getRandom() :
        return A.get(rand.nextInt(A.size()))
/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection()
 * boolean param_1 = obj.insert(val)
 * boolean param_2 = obj.remove(val)
 * param_3 = obj.getRandom()
 */
```
------------------------------------------------------------------------------------------------
 12. Integer to Roman
========================
 Roman numerals are represented by seven different symbols:
 `I` 
 ,
 `V` 
 ,
 `X` 
 ,
 `L` 
 ,
 `C` 
 ,
 `D` 
 and
 `M` 
 .
```
Symbol      Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
 For example, two is written as
 `II` 
 in Roman numeral, just two one's added together. Twelve is written as,
 `XII` 
 , which is simply
 `X` 
 +
 `II` 
 . The number twenty seven is written as
 `XXVII` 
 , which is
 `XX` 
 +
 `V` 
 +
 `II` 
 .
 Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
 `IIII` 
 . Instead, the number four is written as
 `IV` 
 . Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as
 `IX` 
 . There are six instances where subtraction is used:
* `I` 
 can be placed before
 `V` 
 (5) and
 `X` 
 (10) to make 4 and 9.
* `X` 
 can be placed before
 `L` 
 (50) and
 `C` 
 (100) to make 40 and 90.
* `C` 
 can be placed before
 `D` 
 (500) and
 `M` 
 (1000) to make 400 and 900.
 Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
 Example 1:
```
Input: 3
Output: "III"
```
 Example 2:
```
Input: 4
Output: "IV"
```
 Example 3:
```
Input: 9
Output: "IX"
```
 Example 4:
```
Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
```
 Example 5:
```
Input: 1994
Output: "MCMXCIV"
Explanation:
 M = 1000, CM = 900, XC = 90 and IV = 4.
```
 Thoughts:
1. Most straightforward way is to enumerate all 1th, 10th, 100 th, 1000 th units expressions
2. Iterative solution:
 Code: Enumerate
```python
class Solution(object):
    def intToRoman(self, num):
        """
 :type num: int
 :rtype: str
 """
        # Input is guaranteed to be within the range from 1 to 3999
        M = ['', 'M', 'MM', 'MMM'] # 1000s
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC','DCC','DCCC','CM'] # 100s
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] # 10s
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
```
 Code: Enumerate
```python
class Solution :
    public String intToRoman(num) :
        String[] romanPieces=:"","I","II","III","IV","V","VI","VII","VIII","IX",
                                "","X","XX","XXX","XL","L","LX","LXX","LXXX","XC",
                                "","C","CC","CCC","CD","D","DC","DCC","DCCC","CM",
                                "","M","MM","MMM","MMMM"
        return romanPieces[num/1000+30]+romanPieces[(num/100)%10+20]
        +romanPieces[(num/10)%10+10]+romanPieces[num%10]
```
 Code: Enumerate
```python
class Solution(object):
     def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(values):
            res += (num/v) * numerals[i]
            num %= v
        return res
```
 Code: Iterative:
```python
class Solution :
    public String intToRoman(num) :
        int[] weights=:1000,900,500,400,100,90,50,40,10,9,5,4,1
        String[] tokens=:"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"
        StringBuilder sb=new StringBuilder("")
        start=0
        while(num>0):
            for(i=starti<13i++):
                if(num>=weights[i]):
                    num-=weights[i]
                    sb.append(tokens[i])
                    break
                start=i+1 #  skip those impossible check, make it faster
        return sb.toString()
```
------------------------------------------------------------------------------------------------
 350. Intersection of Two Arrays II
======================================
 Given two arrays, write a function to compute their intersection.
 Example 1:
```
Input: 
nums1 = [1,2,2,1], nums2 = [2,2]
Output: 
[2,2]
```
 Example 2:
```
Input: 
nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: 
[4,9]
```
 Note:
* Each element in the result should appear as many times as it shows in both arrays.
* The result can be in any order.
 Follow up:
* What if the given array is already sorted? How would you optimize your algorithm?
* What if nums1's size is small compared to nums2 's size? Which algorithm is better?
* What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
 Example 1:
```
Input: 
nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```
 Example 2:
```
Input: 
nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```
 Thoughts:
1. Hashtable implementaion:
	1. Time: O(m + n) Space: O(m + n)
	2. Time: O(m + n) Space: O(m)
2. Sort + two pointers Solution:
	1. Time: O(max(m,n)log(max(m,n)) Space: O(m + n)
 Code:
 Hashtable implementaion Time: O(m + n) Space: O(m + n)
```python
class Solution :
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) :
        unordered_map<int, int> map
        vector<int> res
        for (i = 0 i < nums1.size() i++) map[nums1[i]]++
        for (i = 0 i < nums2.size() i++) :
            if(--map[nums2[i]] >= 0) res.push_back(nums2[i])
        return res
```
 Code:
 Time: O(m + n) Space: O(m)
1. change
 `if(--map[nums2[i]] >= 0) res.pushback(nums2[i])` 
 to
 `if(map.find(nums2[i])!=map.end() && --map[nums2[i]]>= 0 res.push_back(nums2[i])`
 Code:
 Sort + Two Pointers:
 Time: O(max(m + n, mlogm, nlogn)) Space: O(m + n)
```python
class Solution :
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) :
        sort(nums1.begin(), nums1.end())
        sort(nums2.begin(), nums2.end())
        m = nums1.size(), n = nums2.size()
        vector<int> res
        i1 = 0, i2 = 0
        while(i1 < m && i2 < n):
            if(nums1[i1] == nums2[i2]):
                res.push_back(nums1[i1])
                i1++
                i2++
            else if (nums1[i1] > nums2[i2]):
                i2++
            else :
                i1++
        return res
```
 Follow up:
1. two pointer: Time: max(m + n, mlogm, nlogn), Space O(1)
2. Suppose lengths of two arrays are
 `N` 
 and
 `M` 
 , the time complexity of my solution is
 `O(N+M)` 
 and the space complexity if
 `O(N)` 
 considering the hash. So it's better to
 use the smaller array to construct the counter hash
 . Well, as we are calculating the intersection of two arrays, the order of array doesn't matter. We are totally free to swap to arrays.
3. Divide and conquer. Repeat the process frequently: Slice
 `nums2` 
 to fit into memory, process (calculate intersections), and write partial results to memory.
------------------------------------------------------------------------------------------------
 785. Is Graph Bipartite?
============================
 Given an undirected
 `graph` 
 , return
 `true` 
 if and only if it is bipartite.
 Recall that a graph is _bipartite _if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
 The graph is given in the following form:
 `graph[i]` 
 is a list of indexes
 `j` 
 for which the edge between nodes
 `i` 
 and
 `j` 
 exists. Each node is an integer between
 `0` 
 and
 `graph.length - 1` 
 . There are no self edges or parallel edges:
 `graph[i]` 
 does not contain
 `i` 
 , and it doesn't contain any element twice.
```
Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: :0, 2 and :1, 3.
```
```
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
```
 Note:
* `graph` 
 will have length in range
 `[1, 100]` 
 .
* `graph[i]` 
 will contain integers in range
 `[0, graph.length - 1]` 
 .
* `graph[i]` 
 will not contain
 `i` 
 or duplicate values.
* The graph is undirected: if any element
 `j` 
 is in
 `graph[i]` 
 , then
 `i` 
 will be in
 `graph[j]` 
 .
 Thoughts:
1. DFS: color each node:
	1. for each node, first check if it has been colored, if is, return current color value == color to be added
	2. color the node
	3. try color all of its neightbor with different value, if failed, returned false else return true
2. BFS: we need to check each if each cluster(edges linked together) is Bipartite. By
 shawntsai
 at
 here
 Code: BFS T:(V+E) S: O(E): (
 For a directed graph, the sum of the sizes of the adjacency lists of all the nodes is E (total number of edges). So, the complexity of DFS is
 O(V) + O(E) = O(V + E)
 for an undirected graph, each edge will appear twice. Once in the adjacency list of either end of the edge. So, the overall complexity will be
 O(V) + O (2E) ~ O(V + E)
 .)
```python
class Solution :
    public boolean isBipartite(int[][] graph) :
        n = graph.length
        int[] colors = new int[n]
        Arrays.fill(colors, -1)            
        for (i = 0 i < n i++) :              # This graph might be a disconnected graph. So check each unvisited node.
            if (colors[i] == -1 && !validColor(graph, colors, 0, i)) :
                return false
        return true
    public boolean validColor(int[][] graph, int[] colors, color, node) :
        if (colors[node] != -1) :
            return colors[node] == color
        colors[node] = color       
        for (next : graph[node]) :
            if (!validColor(graph, colors, 1 - color, next)) :
                return false
        return true
```
 Code: BFS T:(V+E) S:O(V)
```python
class Solution :
    public boolean isBipartite(int[][] graph) :
        # BFS
        #  0(not meet), 1(black), 2(white)
        int[] colors = new int[graph.length]
        for (i = 0 i < graph.length i++) :
            if (graph[i].length != 0 && colors[i] == 0) :
                colors[i] = 1
                #  BFS
                Queue<Integer> q = new LinkedList<>()
                q.offer(i)
                while(! q.isEmpty()) :
                    cur = q.poll()
                    for (v: graph[cur]) : #  expand its neighbor
                        if (colors[v] == 0) :
                            colors[v] = (colors[cur] == 1) ? 2 : 1
                            q.offer(v)
                         else :
                            if (colors[v] == colors[cur]) return false
        return true
```
------------------------------------------------------------------------------------------------
 463. Island Perimeter
=========================
 You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
 Example:
```
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
```
![](https:# leetcode.com/static/images/problemset/island.png)
 FB Variant: only need to output the number of islands counts
 Thoughts:
1. loop over the matrix and count the number of islands
2. if the current dot is an island, count if it has any left(right) neighbour or up(down) neighbour
3. the result is islands * 4 - neighbours * 2
```python
class Solution(object):
    def islandPerimeter(self, grid):
        count = repeat = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]):
                    count+= 1
                    # check left and up in this scenario
                    if (j!=0 and grid[i][j-1]):
                        repeat += 1
                    if (i !=0 and grid[i-1][j]):
                        repeat += 1
        print("count: %s repeat: %s"%(count,repeat))
        return 4*count - 2*repeat
```
------------------------------------------------------------------------------------------------
 Islands
===========
 200
 305
 711
------------------------------------------------------------------------------------------------
 JingChi.ai
==============
------------------------------------------------------------------------------------------------
 84. Largest Rectangle in Histogram
======================================
 84.Largest Rectangle in Histogram
===================================
 Givennnon-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
![](https:# leetcode.com/static/images/problemset/histogram.png)
 Above is a histogram where width of each bar is 1, given height =
 `[2,1,5,6,2,3]` 
 .
![](https:# leetcode.com/static/images/problemset/histogram_area.png)
 The largest rectangle is shown in the shaded area, which has area =
 `10` 
 unit.
 For example,
 Given heights =
 `[2,1,5,6,2,3]` 
 ,
 return
 `10` 
 .
 Thoughts:
1. have a stack to record increasing index
2. while current index is less that the top of the stack, update the maximum area
3. having a increasing stack is because as index gets larger, the
 only
 possible way for rectangle starting from larger index is due to its larger height value.
 Code time complexity: O(n), space complexity: O(n)
```python
class Solution :
public:
    largestRectangleArea(vector<int>& heights) :
        stack<int> s
        s.push(-1)
        ans = 0
        n = heights.size()
        for(i = 0 i < n i++):
            while((s.top()!= -1) && heights[s.top()] >= heights[i]):
                last_idx = s.top() s.pop()
                ans = max(ans, heights[last_idx] * (i - s.top() - 1))
            s.push(i)
        #  reach the end of list
        while(s.top()!= -1):
            last_idx = s.top() s.pop()
            ans = max(ans, (heights[last_idx]) * (n - 1 - s.top()))
        return ans
```
 Code using 0 padding at the end and vector as stack
```
 class Solution :
    public:
        largestRectangleArea(vector<int> &height) :
            ret = 0
            height.push_back(0)
            vector<int> index
            for(i = 0 i < height.size() i++)
            :
                while(index.size() > 0 && height[index.back()] >= height[i])
                :
                    h = height[index.back()]
                    index.pop_back()
                    sidx = index.size() > 0 ? index.back() : -1
                    if(h * (i-sidx-1) > ret)
                        ret = h * (i-sidx-1)
                index.push_back(i)
            return ret
```
 Special thanks to
 sipiprotoss5
 's for the last
 solution
------------------------------------------------------------------------------------------------
 Last and Second-Last
========================
 Last and Second-Last
======================
 找到字符串和倒数第二个字符， 用whitespace 隔开
 解法： 直接判断最后一个和倒数第二个字符存不存在，存在就输出。
------------------------------------------------------------------------------------------------
 102. Level Order Traversal
==============================
 102. Binary Tree Level Order Traversal
========================================
 Given a binary tree, return thelevel ordertraversal of its nodes' values. (ie, from left to right, level by level).
 For example:
 Given binary tree
 `[3,9,20,null,null,15,7]` 
 ,
```
    3
   / \
  9  20
    /  \
   15   7
```
 return its level order traversal as:
```
[
  [3],
  [9,20],
  [15,7]
]
```
 Thoughts:
1. PreOrder Traversal + Add a "depth" variable to keep track of what level curNode should be inserted into
2. Solve using
 Queue
 Code 1
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    vector<vector<int>>answer
public:
    vector<vector<int>> levelOrder(TreeNode* root) :
        levelOrderHelper(root,0)
        return answer
    void levelOrderHelper(TreeNode* cur, depth):
        if(!cur) return
        if(answer.size()==depth)answer.push_back(vector<int>())
        answer[depth].push_back(cur->val)
        levelOrderHelper(cur-> left, depth + 1)
        levelOrderHelper(cur-> right, depth + 1)
```
 Code 2
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    vector<vector<int>> answer
public:
    vector<vector<int>> levelOrder(TreeNode* root) :
       queue <TreeNode*> q
       if(root) q.push(root)
        while(!q.empty()):
            len = q.size()
            vector<int> level
            for(i = 0 i < len i ++):
                TreeNode* cur = q.front()
                level.push_back(cur->val)
                if(cur->left) q.push(cur->left)
                if(cur->right) q.push(cur->right)
                q.pop()
            answer.push_back(level)
        return answer
```
 Code 2: checking null at the current node
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
    vector<vector<int>> answer
public:
    vector<vector<int>> levelOrder(TreeNode* root) :
       queue <TreeNode*> q
         q.push(root)
        while(!q.empty()):
            len = q.size()
            vector<int> level
            for(i = 0 i < len i ++):
                TreeNode* cur = q.front() q.pop()
                if (!cur) continue
                level.push_back(cur->val)
                q.push(cur->left)
                q.push(cur->right)
            if (!level.empty()) answer.push_back(level)
        return answer
```
------------------------------------------------------------------------------------------------
 Linked List
===============
------------------------------------------------------------------------------------------------
 LintCode 558: Sliding Window Matrix Maximum
===============================================
 Sliding Window Matrix Maximum 558
===================================
 Given an array of n*n matrix, and a moving matrix window (size k), move the window from top left to bottom right at each iteration, find the maximum sum of the elements inside the window at each moving. Return 0 if the answer does not exist.
 Example
 For matrix
 `[ [1, 5, 3], [3, 2, 1], [4, 1, 9], ]` 
 The moving window size k = 2. return 13.
 At first the window is at the start of the array like this
`[ [|1, 5|, 3], [|3, 2|, 1], [4, 1, 9], ]` 
 ,get the sum 11 then the window move one step forward.
`[ [1, |5, 3|], [3, |2, 1|], [4, 1, 9], ]` 
 ,get the sum 11 then the window move one step forward again.
`[ [1, 5, 3], [|3, 2|, 1], [|4, 1|, 9], ]` 
 ,get the sum 10 then the window move one step forward again.
`[ [1, 5, 3], [3, |2, 1|], [4, |1, 9|], ]` 
 ,get the sum 13
 So finally, get the maximum from all the sum which is 13.
 Challenge:
 O(n^2) time.
 Thoughts:
 O(n^2) time->traverse maps of dim O(n^2) -> Dynamic Programming:
1. state function: sum[i][j]: sum of all the elements from (0, i-1) and (0, j-1) and initially set sum[0][0] = 0
2. state transition: sum[i][j] = matrix[i-1][j-1] + sum[i][j-1] + sum[i - 1][j] - sum[i-1][j-1]
3. to get window sum value, we reverse the calculation from step 2 with window size parameter k: window_sum = sum[i][j] - sum[i][j-k] - sum[i-k][j] + sum[i-k][j-k]
 Code:
```python
public class Solution :
    /**
 * @param matrix an integer array of n * m matrix
 * @param k an integer
 * @return the maximum number
 */
    public maxSlidingWindow2(int[][] matrix, k) :
        #  Write your code here
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0 || k > matrix.length || k > matrix[0].length):
            return 0
        n = matrix.length
        m = matrix[0].length
        int[][] sum = new int[n + 1][m + 1]
        for(i = 0 i <= n i++):
            sum[i][0] = 0
        for(j = 1 j <= m j++):
            sum[0][j] = 0
        for(i = 1 i <= n i++):
            for(j = 1 j <= m j++):
                sum[i][j] = matrix[i - 1][j - 1] + sum[i][j - 1] + sum[i - 1][j] -sum[i - 1][j - 1]
        max = Integer.MIN_VALUE
        for(i = k i <= n i++):
            for(j = k j <= m j++):
                window= sum[i][j] - sum[i - k][j] - sum[i][j - k] + sum[i - k][j - k]
                max = Math.max(max, window)
        return max
```
 Special Thanks
 zhengyang2015's gitbook solution
------------------------------------------------------------------------------------------------
 LintCode Contest
====================
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 Longest Arithmetic Progression
==================================
 Longest Arithmetic Progression (Google)
=========================================
 [Google] Longest Arithmetic Sequence
  https:# www.geeksforgeeks.org/longest-arithmetic-progression-dp-35/
======================================================================
------------------------------------------------------------------------------------------------
 128. Longest Consecutive Sequence
=====================================
 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
 Your algorithm should run in O(
 ---n--- 
 ) complexity.
 Example:
```
Input:
 [100, 4, 200, 1, 3, 2]
Output:
 4
Explanation:
 The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```
 Thoughts:
 m[k] -> length for key k,
 m[k] == m[k-1] + m[k+1] m[]
 keep expanding the boundary by looking up neighbor value and update the boundary point records
 Code O(n)
```python
class Solution :
public:
    longestConsecutive(vector<int>& A) :
        ans = 0
        unordered_map <int, int> m
        for(n : A):
            if(m.find(n)== m.end()):
                #  must first lookup then get the value, otherwise the map will put an default KV pair
                left = (m.find(n-1)!= m.end())?m[n-1]:0, right = (m.find(n+1)!= m.end())?m[n+1]:0, 
                sum = left + 1 + right
                ans = max(ans, sum)
                #  update
                m[n] = sum
                m[n - left] = sum
                m[n + right] = sum
        return ans
```
 Thanks 's
 dchen0215 's
 answer
 .
------------------------------------------------------------------------------------------------
 329. Longest Increasing Path in a Matrix
============================================
 Given an integer matrix, find the length of the longest increasing path.
 From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
 Example 1:
```
Input: 
A = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
  ] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
```
 Example 2:
```
Input: A = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```
 Thoughts:
1. DFS + memoization:
2. Topological sort: impose an directed edge a -> b if a < b. Then each time, delete the node with out degree zero, then the number of iteration is the result. (from
 post
 )
 Code: DFS + Memoization: T:O(mn) S:O(mn)
```python
class Solution :
    public longestIncreasingPath(int[][] matrix) :
        if (matrix == null || matrix.length == 0|| matrix[0].length == 0) return 0
        m = matrix.length, n = matrix[0].length, max = 0
        dp [][]  = new [m][n]
        for(i = 0 i < m i++):
            for(j = 0 j < n j++):
                max = Math.max(max, dfs(matrix, m , n, i, j, dp))
        return max
    private dfs(int[][] matrix, m, n,i, j, [][] dp):
        if(dp[i][j] != 0) return dp[i][j] #  memoization
        cnt = 1
        d[] = :0,1,0,-1,0
        for(k = 0 k < 4 k++):
            x = i + d[k], y= j + d[k + 1]
            if(x < 0 || x >= m || y < 0 || y>= n || matrix[i][j] >= matrix[x][y]) continue
            cnt = Math.max(cnt, dfs(matrix, m, n, x, y, dp) + 1)
        dp[i][j] = cnt
        return cnt
```
 Code: Python
```python
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
 :type matrix: List[List[int]]
 :rtype: int
 """
        def dfs(i,j):
            if dp[i][j]: return dp[i][j]
            cur = matrix[i][j]
            dp[i][j] = 1 + max(dfs(i + 1, j) if i + 1 < m  and cur > matrix[i + 1][j] else 0,
                           dfs(i - 1, j) if i and cur > matrix[i - 1][j] else 0,
                           dfs(i, j + 1) if j + 1 < n and cur > matrix[i][j + 1] else 0,
                           dfs(i, j - 1) if j and cur > matrix[i][j - 1] else 0
                          )
            return dp[i][j]
        if not matrix or not matrix[0]: return 0
        m,n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)] 
        return max(dfs(i,j) for j in range (n) for i in range(m))
```
 Code: Topological Sort O(mn * h), where h is the height of the order: (TLE)
```python
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
 :type matrix: List[List[int]]
 :rtype: int
 """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        count, res = m * n, 0
        while count > 0:
            s = set()
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == -sys.maxint-1: continue
                    up = (not i) or matrix[i][j] >= matrix[i - 1][j]
                    down = i + 1 == m or matrix[i][j] >= matrix[i + 1][j]
                    left = (not j) or matrix[i][j] >= matrix[i][j - 1]
                    right = j + 1 == n or matrix[i][j] >= matrix[i][j + 1]
                    if up and down and left and right:
                        s.add((i,j))
            for x, y in s:
                matrix[x][y] = -sys.maxint-1
                count -= 1
            res += 1
        return res
```
------------------------------------------------------------------------------------------------
 300. Longest increasing subsequence
=======================================
 300. Longest increasing Subsequence
=====================================
 Given an unsorted array of integers, find the length of longest increasing subsequence.
 For example,
 Given
 `[10, 9, 2, 5, 3, 7, 101, 18]` 
 ,
 The longest increasing subsequence is
 `[2, 3, 7, 101]` 
 , therefore the length is
 `4` 
 . Note that there may be more than one LIS combination, it is only necessary for you to return the length.
 Your algorithm should run in O(n^2) complexity.
 Follow up:
 Could you improve it to O(nlogn) time complexity?
 Credits:
 Special thanks to
 @pbrother
 for adding this problem and creating all test cases.
 Thoughts
1. O(n^2) solution with
 recursive and dynamic programming approach by GeeksforGeeks
2. Dynamic Programming
 (Original
 GeeksforGeeks
 explanation)
 O(n^2)
3. Binary search + Dynamic Programming
 :
 O(nlogn)
 (Original
 GeeksforGeeks
 explanation)
 Code Binary Search (Java)
 inspired by
 GeeksforGeeks
 :
 “end element of smaller list is smaller than end elements of larger lists“.
```
record the tail table by keeping updating current value to correct position into the tail table 
through binary search
```
```python
class Solution :
    public lengthOfLIS(int[] A) :
    int[] tails = new int[A.length]
    size = 0
    for (x : A) :
        i = 0, j = size
        while (i != j) :
            m = (i + j) / 2
            if (tails[m] < x)
                i = m + 1
            else
                j = m
        tails[i] = x
        if (i == size) ++size
    return size
```
 using
 Arrays.binarySearch
 by
 jopiko123
 :
```python
public class Solution :
    public lengthOfLIS(int[] A) :            
        int[] dp = new int[A.length]
        len = 0
        for(x : A) :
            i = Arrays.binarySearch(dp, 0, len, x)
            if(i < 0) i = -(i + 1)
            dp[i] = x
            if(i == len) len++
        return len
```
 Code Binary Search
 with
 O(nlogn)
 by
 dtccwl
 , inspired by
 GeeksforGeeks
```python
class Solution :
public:
    lengthOfLIS(vector<int>& A) :
    vector<int> res
    for(i=0 i<A.size() i++) :
        auto it = std::lower_bound(res.begin(), res.end(), A[i])
        if(it==res.end()) res.push_back(A[i])
        else *it = A[i]
    return res.size()
```
------------------------------------------------------------------------------------------------
 409. Longest Palindrome
===========================
 Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
 This is case sensitive, for example
 `"Aa"` 
 is not considered a palindrome here.
 Note:
 Assume the length of given string will not exceed 1,010.
 Example:
```
Input:"abccccdd"
Output:7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
```
 Thoughts:
1. Total len - number of odds +
 1 (indicator of whether odds > 0)
 Code: Python
```python
class Solution(object):
    def longestPalindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
```
 Code: Python with counting even number (slower)
```python
class Solution(object):
    def longestPalindrome(self, s):
        even = sum(v & ~1 for v in collections.Counter(s).values())
        return even + (even < len(s))
```
------------------------------------------------------------------------------------------------
 5. longest Palindromic Substring
====================================
 5. Longest Palindromic Substring
==================================
 Given a string
 s
 , find the longest palindromic substring in
 s
 . You may assume that the maximum length of
 s
 is 1000.
 Example:
```
Input:
 "babad"
Output:
 "bab"
Note:
 "aba" is also a valid answer.
```
 Example:
```
Input:
 "cbbd"
Output:
 "bb"
```
 Thoughs:
1. similar to
 647. Number of palindromic substring
2. O(n^2) with DP or center expansion, O(n) with
 Manacher’s algorithm
3. the number
 between
 ---left--- 
 and
 ---right--- 
 (exclusive) is "
 ---right - left - 1" and number from left and right (inclusive) is "right - left + 1"---
 Code
 (O (n^2) DP)
```python
class Solution :
public:
    string longestPalindrome(string s) :
        n = s.length()
        string ans = ""
        bool d[n][n] = ::false 
        for(i = n i >= 0 i--):
            for(j = i j < n j++):
                d[i][j] = (s[i] == s[j]) && (j - i < 3 || d[i+1][j-1])
                if(d[i][j] && j - i + 1 > ans.length())
                    ans = s.substr(i,j - i + 1) #  +1 since end exlusive 
        return ans
```
 Code
 (O (n^2) without extra space)
```python
class Solution :
public:
    string longestPalindrome(string s) :
        string ans = ""
        for(i = 0 i < s.length()  i ++):
            string s1 = extend(s,i,i), s2 = extend(s, i, i+1)
            if(s1.length() > ans.length()) ans = s1
            if(s2.length() > ans.length()) ans = s2
        return ans
    string extend(string s, left, right):
        while(left >= 0 && right < s.length() && s[left] == s[right]):
            left--
            right++
        return s.substr(left+1, right - left - 1)
```
 Code (O(n)) with Manacher's algorithm
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
 :type s: str
 :rtype: str
 """
        # For example, s = "abba", A = "@#a#b#b#a#$".
        A = '#'.join('@:$'.format(s))
        Z = [0] * len(A)
        # print "%s\n%s"%(A,Z)
        center = right = 0
        for i in xrange(1, len(A) - 1):
        # get the palindrome numbers based on right boundary 
        # and mirror palindrome
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            #equivalent to: Z[i] = (right > i) and min(right - i, P[2*center - i])
            # explore the palindrome at current pivot
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
        # update right boundary
        if i + Z[i] > right:
            center, right = i, i + Z[i]
        maxlen, center = max((n, i) for i , n in enumerate(Z))
        return s[(center - maxlen)# 2:(center + maxlen)# 2 ]
```
------------------------------------------------------------------------------------------------
 159. Longest Substring with At Most Two Distinct Characters
===============================================================
 159. Longest Substring with At Most Two Distinct Characters
=============================================================
 Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
 For example, Given s =
 `“eceba”` 
 ,
 T is "ece" which its length is 3.
 Thoughts
 count: count # of distinct characters
```python
class Solution :
public:
    lengthOfLongestSubstringTwoDistinct(string s) :
        left = 0, right = 0, count = 0, len = 0
        unordered_map <char, int> map
        while(right < s.length()):
            #  put, check new 
            if(++map[s[right]] == 1) count++
            right++
            #  move left to reduce the window size if 
            #  there are more than two distinct chars in the current window
            while(count > 2):
                if(--map[s[left]] == 0) count--
                left++
            len = max(len, right - left)
        return len
```
 template
```python
class Solution :
public:
    lengthOfLongestSubstringTwoDistinct(string s) :
        vector<int> map(128,0)
        cnt = 0, slow = 0 , fast = 0, d = 0
        while (fast < s.size()):
            if(map[s[fast++]]++ == 0) cnt ++
            while(cnt > 2) if(map[s[slow++]]-- == 1) cnt-- #  after subtraction is 0
            d = max(d, fast - slow)
        return d
```
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 146.LRU Cache(Amazon)
=========================
 http:# fisherlei.blogspot.com/search?q=LRUcache
 Design and implement a data structure for
 Least Recently Used (LRU) cache
 . It should support the following operations:
 `get` 
 and
 `put` 
 .
`get(key)` 
 - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
`put(key, value)` 
 - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
 Follow up:
 Could you do both operations in
 (1)
 time complexity?
 Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ )
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       #  returns 1
cache.put(3, 3)    #  evicts key 2
cache.get(2)       #  returns -1 (not found)
cache.put(4, 4)    #  evicts key 1
cache.get(1)       #  returns -1 (not found)
cache.get(3)       #  returns 3
cache.get(4)       #  returns 4
```
* O(1) -> HashMap + Maintaining the state for each put and get
```python
class LRUCache :
public:
    struct cache:
        key
        value
        cache(k, v):key(k), value(v):
    LRUCache(capacity) :
        _capacity = capacity
    get(key) :
        if(record.find(key) != record.end()):
            #  move the cache to the front
            MovetoHead(key)
            return record[key]-> value
        return -1
    void put(key, value) :
        #  already exists, update
        if(record.find(key) != record.end()):
            record[key]->value = value
            MovetoHead(key)
            return
        #  insert in front
        if (caches.size() >= _capacity):
            #  pop the last and eliminate iterator from the record
            cout<<class(caches.back())<<endl
            record.erase(caches.back().key)
            caches.pop_back()
        cache newCache(key, value)
        caches.push_front(newCache)
        record[key] = caches.begin()
 private: 
    unordered_map <int, list<cache>::iterator> record
    list<cache> caches
    _capacity
    void MovetoHead(key):
        #  move key from current location to head of the caches list
        auto updatedCache = *record[key]
        caches.erase(record[key])
        caches.push_front(updatedCache)
        #  update record info
        record[key] = caches.begin()
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity)
 * param_1 = obj.get(key)
 * obj.put(key,value)
 */
```
 Special Thanks:
 水中的鱼
 for the reference!
------------------------------------------------------------------------------------------------
 Map
=======
------------------------------------------------------------------------------------------------
 Math
========
------------------------------------------------------------------------------------------------
 221. Maximal Square
=======================
 221. Maximal Square
=====================
 Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
 For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
 Return 4.
 Thoughts:
1. different approach from maximal rectangle problems (
 84
 and
 85
 )since it is a square (current state value only depends on top, left and top-left corner
2. f[i][j] number of maximal square from matrix[0, ...i -1][0,...j-1] so far
3. initial state: f[i][0] = f[0][j] = 0
4. recursive state : f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) for (1<= i <= matrix.size() 1<=j<=matrix[0].size()).
5. further optimization
 Code Time Complexity O(row * col), Space Complexity O(row * col)
```python
class Solution :
public:
    maximalSquare(vector<vector<char>>& matrix) :
        if(matrix.empty()) return 0
        m = matrix.size(), n = matrix[0].size()
        vector<vector<int>> f(m + 1, vector<int>(n + 1, 0))
        ans = 0
        for(i = 1 i <= m i ++):
            for(j = 1 j <=n j ++):
                if(matrix[i-1][j-1] == '1'):
                    f[i][j] = min(f[i-1][j], min(f[i-1][j-1], f[i][j-1])) + 1
                    ans = max(ans, f[i][j])
        return ans * ans
```
 Code (Optimization): with Space Complexity O(row) or O(col)
```
maximalSquare(vector<vector<char>>& matrix) :
    if (matrix.empty()) return 0
    m = matrix.size(), n = matrix[0].size()
    vector<int> dp(m + 1, 0) #  0 padding on the top
    maxsize = 0, pre = 0
    for (j = 0 j < n j++) :
        for (i = 1 i <= m i++) :
            temp = dp[i] 
            if (matrix[i - 1][j] == '1') :
                dp[i] = min(dp[i], min(dp[i - 1], pre)) + 1 # dp[i]: dp[i][j-1], dp[i-1]: dp[i-1][j]
                maxsize = max(maxsize, dp[i])
            else dp[i] = 0 
            pre = temp #  serve as dp[i-1][j-1] for the next iteration 
    return maxsize * maxsize
```
 Special Thanks to
 jianchao.li.fighter
 's
 solution
------------------------------------------------------------------------------------------------
 325. Maximum Size Subarray Sum Equals k
===========================================
 Given an array A and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
 Note:
 The sum of the entirenumsarray is guaranteed to fit within the 32-bit signed integer range.
 Example 1:
```
Input: 
A = [1, -1, 5, -2, 3], k= 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```
 Example 2:
```
Input: A = [-2, -1, 2, 1], k= 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```
 Follow Up:
 Can you do it in O(n) time?
 Thoughts:
1. Have a prefix sum record
2. Use hashtable to record the smallest index for the same sum
```python
class Solution(object):
    def maxSubArrayLen(self, A, k):
        """
 :type A: List[int]
 :type k: int
 :rtype: int
 """
        preSum, end, s, ans =[0], :, 0 , 0
        for i, num in enumerate(A):
            s += num
            preSum.append(s)
        # prepreSum[i]: sum of A[0...i] exslusive i
        ans = 0
        for i, preS in enumerate(preSum):
            if preS - k in end:
                ans = max(ans, i - end[preS - k])
            if preS not in end: #keep smaller
                end[preS] = i 
        return ans
```
------------------------------------------------------------------------------------------------
 155. Min Stack
==================
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.
 Example:
```
MinStack minStack = new MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   -->Returns -3.
minStack.pop()
minStack.top()      -->Returns 0.
minStack.getMin()   -->Returns -2.
```
 Thoughts:
 Linkedlist style to record the head info,
 record min history by iteratively comparing the min of the current value and history min
 Code (Python)
```python
class MinStack(object):
    def __init__(self):
        """
 initialize your data structure here.
 """
        self.head = None
    def push(self, x):
        """
 :type x: int
 :rtype: void
 """
        if(self.head == None):
            self.head = Node(x, x)
        else:
            self.head = Node(x, min(self.head.min, x), self.head)
    def pop(self):
        """
 :rtype: void
 """
        self.head = self.head.next
    def top(self):
        """
 :rtype: int
 """
        return self.head.val
    def getMin(self):
        """
 :rtype: int
 """
        return self.head.min
class Node(object):
    def __init__(self, val, minval, next = None):
        self.val = val
        self.min = minval
        self.next = next
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
------------------------------------------------------------------------------------------------
 MiniMax
===========
------------------------------------------------------------------------------------------------
 111. Minimum Depth of Binary Tree
=====================================
 Given a binary tree, find its minimum depth.
 The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 Note:
 A leaf is a node with no children.
 Example:
 Given binary tree
 `[3,9,20,null,null,15,7]` 
 ,
```
    3
   / \
  9  20
    /  \
   15   7
```
 return its minimum depth = 2.
```python
class Solution :
    public minDepth(TreeNode root) :
        if (root == null) return 0
        left = minDepth(root.left), right = minDepth(root.right)
        return left == 0 && right == 0? 1: left == 0? right + 1: right == 0? left + 1: Math.min(left, right) + 1
```
------------------------------------------------------------------------------------------------
 76. Minimum Window Substring
================================
 76. Minimum Window Substring (Shortest Substring from Pangram)
================================================================
 Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
 For example,
 S
 =
 `"ADOBECODEBANC"` 
 T
 =
 `"ABC"` 
 Minimum window is
 `"BANC"` 
 .
 Note:
 If there is no such window in S that covers all characters in T, return the empty string
 `""` 
 .
 If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
 Thoughts:
1. "Do" Section keeps tracking "head" and "len" variable by "len"'s value
2. Count: # character current sliding window needs (does not have)
3. Very similar to
 438. Find All Anagrams in a String
```python
class Solution :
public:
    string minWindow(string s, string t) :
        if(t.length() > s.length()) return ""
        unordered_map <char, int> map
        for(i = 0 i < t.length() i++ ):
            ++map[t[i]]
        left = 0, right = 0, head = INT_MAX, len = INT_MAX, count = map.size()
        while(right < s.length()):
            char rightChar = s[right]
            if(map.find(rightChar) != map.end()):
                if(--map[rightChar] == 0) count --
            right ++
            while(count == 0):  #  here we already find the window that contains the targeted substring
                #  do 
               if(right - left < len):
                    head = left
                    len = right - left
                #  increment
                char leftChar = s[left]
                if (map.find(leftChar)!= map.end()):
                    if(++map[leftChar] > 0):
                        count++
                left ++
        if(len == INT_MAX) return ""
        return s.substr(head, len)
```
 Template:
 https:# leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
 Java Implementation: T: O(|S|), S:O(1)
```python
class Solution :
    public String minWindow(String s, String t) :
        [] map = new [128]
        char [] chs = s.toCharArray()
        for(char c : t.toCharArray()):
            map[c]++
        count = t.length(), slow = 0, fast = 0, head = 0, len = Integer.MAX_VALUE
        while(fast < chs.length):
            if(map[chs[fast++]]-- > 0) count--
            while(count == 0):
                if(fast - slow < len) :
                    len = fast - slow
                    head = slow
                if(map[chs[slow++]]++ == 0) count++
        return len == Integer.MAX_VALUE ? "": s.substring(head, head + len)
```
```
string minWindow(string s, string t) :
        vector<int> map(128,0)
        for(auto c: t) map[c]++
        counter=t.size(), begin=0, end=0, d=INT_MAX, head=0
        while(end<s.size()):
            if(map[s[end++]]-->0) counter-- # in t
            while(counter==0): # valid
                if(end-begin<d)  d=end-(head=begin)
                if(map[s[begin++]]++==0) counter++  # make it invalid
        return d==INT_MAX? "":s.substr(head, d)
```
```
findSubstring(string s):
        vector<int> map(128,0)
        counter #  check whether the substring is valid
        begin=0, end=0 # two pointers, one point to tail and one head
        d # the length of substring
        for() : /* initialize the hash map here */ 
        while(end<s.size()):
            if(map[s[end++]]-- ?):  /* modify counter here */ 
            while(/* counter condition */): 
                 /* update d here if finding minimum*/
                # increase begin to make it invalid/valid again
                if(map[s[begin++]]++ ?): /*modify counter here*/ 
            /* update d here if finding maximum*/
        return d
```
 Python:
 https:# leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
```
def minWindow(self, s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]
```
 Java:
 https:# leetcode.com/problems/minimum-window-substring/discuss/26805/Accepted-O(n)-solution
```python
class Solution :
public:
    string minWindow(string S, string T) :
        if (S.empty() || T.empty())
        :
            return ""
        count = T.size()
        require[128] = :0
        bool chSet[128] = :false
        for (i = 0 i < count ++i)
        :
            require[T[i]]++
            chSet[T[i]] = true
        i = -1
        j = 0
        minLen = INT_MAX
        minIdx = 0
        while (i < (int)S.size() && j < (int)S.size())
        :
            if (count)
            :
                i++
                require[S[i]]--
                if (chSet[S[i]] && require[S[i]] >= 0)
                :
                    count--
            else
            :
                if (minLen > i - j + 1)
                :
                    minLen = i - j + 1
                    minIdx = j
                require[S[j]]++
                if (chSet[S[j]] && require[S[j]] > 0)
                :
                    count++
                j++
        if (minLen == INT_MAX)
        :
            return ""
        return S.substr(minIdx, minLen)
```
------------------------------------------------------------------------------------------------
 Morris Traversal
====================
 http:# www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
 Inorder:
```
1 void inorderMorrisTraversal(TreeNode *root) :
 2     TreeNode *cur = root, *prev = NULL
 3     while (cur != NULL)
 4     :
 5         if (cur->left == NULL)          #  1.
 6         :
 7             printf("%d ", cur->val)
 8             cur = cur->right
 9         
10         else
11         :
12             #  find predecessor
13             prev = cur->left
14             while (prev->right != NULL && prev->right != cur)
15                 prev = prev->right
16 
17             if (prev->right == NULL)   #  2.a)
18             :
19                 prev->right = cur
20                 cur = cur->left
21             
22             else                       #  2.b)
23             :
24                 prev->right = NULL
25                 printf("%d ", cur->val)
26                 cur = cur->right
27             
28         
29     
30 
```
![](assets/Morris_Inorder.png)
 Preorder:
```
 1 void preorderMorrisTraversal(TreeNode *root) :
 2     TreeNode *cur = root, *prev = NULL
 3     while (cur != NULL)
 4     :
 5         if (cur->left == NULL)
 6         :
 7             printf("%d ", cur->val)
 8             cur = cur->right
 9         
10         else
11         :
12             prev = cur->left
13             while (prev->right != NULL && prev->right != cur)
14                 prev = prev->right
15 
16             if (prev->right == NULL)
17             :
18                 printf("%d ", cur->val)  #  the only difference with inorder-traversal
19                 prev->right = cur
20                 cur = cur->left
21             
22             else
23             :
24                 prev->right = NULL
25                 cur = cur->right
26             
27         
28     
29 
```
![](assets/Morris_Preorder.png)
```
 1 void reverse(TreeNode *from, TreeNode *to) #  reverse the tree nodes 'from' -> 'to'.
 2 :
 3     if (from == to)
 4         return
 5     TreeNode *x = from, *y = from->right, *z
 6     while (true)
 7     :
 8         z = y->right
 9         y->right = x
10         x = y
11         y = z
12         if (x == to)
13             break
14     
15 
16 
17 void printReverse(TreeNode* from, TreeNode *to) #  print the reversed tree nodes 'from' -> 'to'.
18 :
19     reverse(from, to)
20     
21     TreeNode *p = to
22     while (true)
23     :
24         printf("%d ", p->val)
25         if (p == from)
26             break
27         p = p->right
28     
29     
30     reverse(to, from)
31 
32 
33 void postorderMorrisTraversal(TreeNode *root) :
34     TreeNode dump(0)
35     dump.left = root
36     TreeNode *cur = &dump, *prev = NULL
37     while (cur)
38     :
39         if (cur->left == NULL)
40         :
41             cur = cur->right
42         
43         else
44         :
45             prev = cur->left
46             while (prev->right != NULL && prev->right != cur)
47                 prev = prev->right
48 
49             if (prev->right == NULL)
50             :
51                 prev->right = cur
52                 cur = cur->left
53             
54             else
55             :
56                 printReverse(cur->left, prev)  #  call print
57                 prev->right = NULL
58                 cur = cur->right
59             
60         
61     
62 
```
![](assets/Morris_postorder.png)
------------------------------------------------------------------------------------------------
 947. Most Stones Removed with Same Row or Column
====================================================
 947. Most Stones Removed with Same Row or Column
==================================================
 On a 2D plane, we place stones at some integer coordinate points. Each coordinate point may have at most one stone.
 Now, a _move _consists of removing a stone that shares a column or row with another stone on the grid.
 What is the largest possible number of moves we can make?
 Example 1:
```
Input: 
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```
 Example 2:
```
Input: 
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
```
 Example 3:
```
Input: 
stones = [[0,0]]
Output: 0
```
 Note:
1. `1 <= stones.length <= 1000`
2. `0 <= stones[i][j] < 10000`
 Thoughts:
1. Union Find: Similar to number of islands, where a "connected" graph is a island.
 Unify the row and col index
 (
 Original Post
 )
	1. Optimization: Path Compression, Union by rank (see
	 305. Number of Islands II
	 )
2. DFS: number of islands -> island: collection of points connected by row or column (
 Original Post
 )
 Code: T: O(n) -> O(1)
```python
class Solution :
public:
    unordered_map <int, int> f
    islands = 0
    removeStones(vector<vector<int>>& stones) :
        for(i = 0 i < stones.size() i++):
            unify(stones[i][0], ~stones[i][1])
        return stones.size() - islands
    find(x):
        if (!f.count(x)) f[x] = x, islands++
        if (x != f[x]) f[x] = find(f[x])
        return f[x]
    void unify(x, y):
        x = find(x), y = find(y)
        if (x != y) f[x] = y, islands--
```
 Code: T:O(n) -> O(1): Path Compression + Union by rank
```python
class Solution(object):
    def removeStones(self, stones):
        """
 :type stones: List[List[int]]
 :rtype: int
 """
        UF = :
        """
 Union by rank
 rank = :
 """
        def find(x):
            while UF[x] != x:
                """
 Path Compression
 UF[x] = UF[UF[x]]
 """
                x = UF[x]
            return x
        def union(x,y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            """
 Union by rank
 rank.setdefault(x, 0)
 rank.setdefault(y, 0)
 if rank[x] > rank[y]:
 x, y = y, x
 rank[y] += rank[x] == rank[y]
 """                
            UF[find(x)] = find(y) 
        for i, j in stones:
            union(i, ~j)
        cc = :find(x) for x in UF # set
        return len(stones) - len(cc)
```
 Code: DFS: discard points for the same island
```python
class Solution:
    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)
        points, island, rows, cols = :(i, j) for i, j in stones, 0, collections.defaultdict(list), collections.defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island
```
------------------------------------------------------------------------------------------------
 346. Moving Average from Data Stream
========================================
 Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
 Example:
```
MovingAverage m = new MovingAverage(3)
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```
 Thoughts:
1. with deque: trival
2. without deque: use ( i + 1) % as circular array
 Code: with deque
```python
class MovingAverage(object):
    def __init__(self, size):
        """
 Initialize your data structure here.
 :type size: int
 """
        self.queue = collections.deque(maxlen = size)
    def next(self, val):
        """
 :type val: int
 :rtype: float
 """
        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```
 Code: without deque
```python
class MovingAverage(object):
    def __init__(self, size):
        """
 Initialize your data structure here.
 :type size: int
 """
        self.w = [0] * size
        self.n = 0 
        self.i = 0
        self.size = size
        self.sum = 0
    def next(self, val):
        """
 :type val: int
 :rtype: float
 """
        if self.n < self.size: self.n +=1
        self.sum -= self.w[self.i]
        self.sum += val
        self.w[self.i] = val
        self.i = (self.i + 1) % self.size
        return float(sum(self.w))/self.n
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```
------------------------------------------------------------------------------------------------
 43. Multiply Strings
========================
 Given two non-negative integers
 `num1` 
 and
 `num2` 
 represented as strings, return the product of
 `num1` 
 and
 `num2` 
 , also represented as a string.
 Example 1:
```
Input: num1 = "2", num2 = "3"
Output: "6"
```
 Example 2:
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```
 Note:
1. The length of both
 `num1` 
 and
 `num2` 
 is < 110.
2. Both
 `num1` 
 and
 `num2` 
 contain only digits
 `0-9` 
 .
3. Both
 `num1` 
 and
 `num2` 
 do not contain any leading zero, except the number 0 itself.
4. You
 must not use any built-in BigInteger library
 or
 convert the inputs to integer
 directly.
 Thoughts:
 Start from right to left, perform multiplication on every pair of digits, and add them together. Let's draw the process! From the following draft, we can immediately conclude:
```
 `num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]` 
```
![](assets/mul.png)
```python
class Solution :
    public String multiply(String num1, String num2) :
        m = num1.length(), n = num2.length()
        [] pro = new int[m + n]
        for(i = m-1 i >= 0   i--):
            for (j = n-1 j >= 0 j-- ):
                mul = (num1.charAt(i) - '0')*(num2.charAt(j) - '0')
                p1 = i + j, p2 = i + j + 1
                sum = pro[p2] + mul
                pro[p1] += sum / 10
                pro[p2] = sum % 10
        StringBuilder sb = new StringBuilder()
        for(p : pro) if(!(sb.length() == 0 && p == 0)) sb.append(p) #  triming leading 0 zeros
        return sb.length() == 0 ? "0": sb.toString()
```
------------------------------------------------------------------------------------------------
 52. N-Queens II
===================
 The
 ---n--- 
 -queens puzzle is the problem of placing
 ---n queens on an n--- 
 × n chessboard such that no two queens attack each other.
![](https:# leetcode.com/static/images/problemset/8-queens.png)
 Given an integer
 ---n--- 
 , return the
 number
 of distinct solutions to the
 ---n--- 
 -queens puzzle.
 Example:
```
Input:
 4
Output: 2
Explanation:
 There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  #  Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  #  Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```
 Thoughts:
1. Backtracking:
	1. Having 3 boolean vectors, col, diag, anti-diag to mark where there is a queen on the same column, same diagnal, or same anti-diagnal. for col, the level set is col for diagnal: the level set is col - row + n for antidiagnal: the level set is row + col.
	2. for each row, expanding the cols and check where there is a queen in col, diag, and anti-diag, then recursively call the backtracking until the row reaches the end or did get in depth due to the disqualification of the results.
 Code:
```python
class Solution :
    count = 0
    public totalNQueens(n) :
        boolean [] cols = new boolean[n], diag = new boolean[2*n], antiDiag = new boolean[2*n]
        backtrack(0,n,cols,diag,antiDiag)
        return count
    private void backtrack(row, n, boolean[] cols, boolean[]diag, boolean[]antiDiag):
        if(row == n) count++
        for(col = 0 col < n col++):
            d = row - col + n 
            aD = row + col
            if(cols[col] || diag[d] || antiDiag[aD]) continue
            cols[col] = true diag[d] = true antiDiag[aD] = true
            backtrack(row + 1, n, cols, diag, antiDiag)
            cols[col] = false diag[d] = false antiDiag[aD] = false
```
------------------------------------------------------------------------------------------------
 51. N-Queens
================
 The
 ---n--- 
 -queens puzzle is the problem of placing
 ---n_queens on an_n--- 
 ×_n_chessboard such that no two queens attack each other.
![](https:# leetcode.com/static/images/problemset/8-queens.png)
 Given an integer
 ---n--- 
 , return all distinct solutions to the
 ---n--- 
 -queens puzzle.
 Each solution contains a distinct board configuration of the
 ---n--- 
 -queens' placement, where
 `'Q'` 
 and
 `'.'` 
 both indicate a queen and an empty space respectively.
 Example:
```
Input:
 4
Output:[
 [".Q..",  #  Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  #  Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```
 Thoughts:
1. The number of columns is
 `n` 
 , the number of 45° diagonals is
 `2 * n - 1` 
 , the number of 135° diagonals is also
 `2 * n - 1` 
 . When reach
 `[row, col]` 
 , the column No. is
 `col` 
 , the 45° diagonal No. is
 `row + col` 
 and the 135° diagonal No. is
 `n - 1 + col - row` 
 . We can use three arrays to indicate if the column or the diagonal had a queen before, if not, we can put a queen in this position and continue.
2. Optimization:
 Merge all arrays into one: only need one boo array flag for size 5*n - 1:n for col 2n -1 for col + row -> diag 2n - 1 for n - 1 - row + row for anti_diag.
 Code: T: O(n^2) S: O(n)
```python
class Solution :
public:
    vector<vector<string>> solveNQueens(n) :
        vector<vector<string>>res
        vector<string>nQueens(n, string(n,'.'))
        vector<int> flag_col (n , 1), flag_45(2*n -1, 1), flag_135( 2*n - 1, 1)
        dfs(res, nQueens, flag_col, flag_45, flag_135, 0, n)
        return res
private:
    void dfs(vector<vector<string>>&res, vector<string>&nQueens, vector<int> &flag_col ,vector<int> &flag_45 ,vector<int> &flag_135
 , row, n):
        if (row == n):
          res.push_back(nQueens)
          return
        for (col = 0 col < n col++ ):
            if (flag_col[col] && flag_45[row + col] && flag_135[n - 1 - row + col]):
                flag_col[col] = flag_45[row + col] = flag_135[n - 1 - row + col] = 0
                nQueens[row][col] = 'Q'
                dfs(res, nQueens, flag_col, flag_45, flag_135, row + 1, n)
                nQueens[row][col] = '.'
                flag_col[col] = flag_45[row + col] = flag_135[n - 1 - row + col] = 1
```
 Code: merged T: O(n^2) S: O(n)
```python
class Solution :
public:
    vector<vector<string>> solveNQueens(n) :
        vector<vector<string>>res
        vector<string>nQueens(n, string(n,'.'))
        vector<int> flag (5*n -2, 1) #  n for col 2n -1 for col + row -> diag 2n - 1 for n - 1 - row + row for anti_diag
        dfs(res, nQueens, flag, 0, n)
        return res
private:
    void dfs(vector<vector<string>>&res, vector<string>&nQueens, vector<int> flag, row, n):
        if (row == n):
          res.push_back(nQueens)
          return
        for (col = 0 col < n col++ ):
            if (flag[col] && flag[n + row + col] && flag[3*n - 1 + n - 1 - row + col]):
                flag[col] = flag[n + row + col] = flag[3*n - 1 + n - 1 - row + col] = 0
                nQueens[row][col] = 'Q'
                dfs(res, nQueens, flag, row + 1, n)
                nQueens[row][col] = '.'
                flag[col] = flag[n + row + col] = flag[3*n - 1 + n - 1 - row + col] = 1
```
------------------------------------------------------------------------------------------------
 339. Nested List Weight Sum
===============================
 Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
 Each element is either an integer, or a list -- whose elements may also be integers or other lists.
 Example 1:
```
Input: 
[[1,1],2,[1,1]]
Output: 
10 
Explanation: 
Four 1's at depth 2, one 2 at depth 1.
```
 Example 2:
```
Input: 
[1,[4,[6]]]
Output: 
27 
Explanation: 
One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3 1 + 4*2 + 6*3 = 27.
```
```
/**
 * #  This is the interface that allows for creating nested lists.
 * #  You should not implement it, or speculate about its implementation
 * public interface NestedInteger :
 * #  Constructor initializes an empty nested list.
 * public NestedInteger()
 *
 * #  Constructor initializes a single integer.
 * public NestedInteger(value)
 *
 * #  @return true if this NestedInteger holds a single integer, rather than a nested list.
 * public boolean isInteger()
 *
 * #  @return the single integer that this NestedInteger holds, if it holds a single integer
 * #  Return null if this NestedInteger holds a nested list
 * public Integer getInteger()
 *
 * #  Set this NestedInteger to hold a single integer.
 * public void setInteger(value)
 *
 * #  Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * public void add(NestedInteger ni)
 *
 * #  @return the nested list that this NestedInteger holds, if it holds a nested list
 * #  Return null if this NestedInteger holds a single integer
 * public List<NestedInteger> getList()
 * 
 */
class Solution :
    public depthSum(List<NestedInteger> nestedList) :
        return dfs(nestedList, 1)
    private dfs(List<NestedInteger> nestedList, depth):
        sum = 0
        for(NestedInteger ni: nestedList):
           if(ni.isInteger()) sum+= ni.getInteger() * depth
           else sum+= dfs(ni.getList(), depth + 1)
        return sum
```
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 323. Number of Connected Components in an Undirected Graph
==============================================================
 Number of Connected Components in an Un-directed Graph
========================================================
 Given
 `n` 
 nodes labeled from
 `0` 
 to
 `n - 1` 
 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
 Example 1:
```
     0          3
     |          |
     1 --- 2    4
```
 Given
 `n = 5` 
 and
 `edges = [[0, 1], [1, 2], [3, 4]]` 
 , return
 `2` 
 .
 Example 2:
```
     0           4
     |           |
     1 --- 2 --- 3
```
 Given
 `n = 5` 
 and
 `edges = [[0, 1], [1, 2], [2, 3], [3, 4]]` 
 , return
 `1` 
 .
 Thoughts:
1. Connected graph: add new edge to merge (make less) components
 if no cycle after being added is introduced->
 union find: using an array to map each nodes's root value to detect cycle.
2. Time: O(n*len(edges)). space(n)
3. Very similar to
 261.Graph Valid Tree
 Code:
```python
class Solution :
public:
    countComponents(n, vector<pair<int, int>>& edges) :
        if(n == 0) return n #  need to manually check this case as array length > 0, 
        #  which is different from Java
        res = n roots [n]
        for(auto & i: roots) i = -1
        for(pair<int,int> p : edges):
            roota = find(roots, p.first)
            rootb = find(roots, p.second)
            if(roota != rootb) :
                #  union
                roots[roota] = rootb
                res--
        return res
    find(roots [], v):
        while(roots[v] != -1) v = roots[v]
        return v
```
 Code (Java):
```python
class Solution :
public:
    countComponents(n, vector<pair<int, int>>& edges) :
        if(n == 0) return n #  need to manually check this case as array length > 0, 
        #  which is different from Java
        res = n roots [n], rank[n]
        for(i = 0  i < n i++) roots[i] = i
        for(pair<int,int> p : edges):
            roota = find(roots, p.first)
            rootb = find(roots, p.second)
            if(roota != rootb) :
                #  union by rank
                #  if(rank[roota] > rank[rootb]):
                #  roota += rootb
                #  rootb = roota - rootb
                #  roota -= rootb
                #  
                #  rank[rootb] += (rank[roota] == rank[rootb]) ?1:0
                roots[roota] = rootb
                res--
        return res
    find(roots [], v):
        while(roots[v] != v) :
            #  path compression
            #  roots[v] = roots[roots[v]]
            v = roots[v]
        return v
```
------------------------------------------------------------------------------------------------
 694. Number of Distinct Islands
===================================
 Given a non-empty 2D array
 `grid` 
 of 0's and 1's, an
 island
 is a group of
 `1` 
 's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
 Count the number of
 distinct
 islands. An island is considered to be the same as another if and only if one island can be
 translated
 (and not rotated or reflected) to equal the other.
 Example 1:
```
11000
11000
00011
00011
```
 Given the above grid map, return
 `1` 
 .
 Example 2:
```
11011
10000
00001
11011
```
 Given the above grid map, return
 `3` 
 .
 Notice that:
```
11
1
```
 and
```
 1
11
```
 are considered different island shapes, because we do not consider reflection / rotation.
 Note:
 The length of each dimension in the given
 `grid` 
 does not exceed 50.
 Thoughts:
1. Distinct islands: island 2d coordinates sets are distinct
 based off its offset
 Code: Java
```python
class Solution :
    private static final d [] = :0,1,0,-1,0
    public numDistinctIslands(int[][] grid):
        m = grid.length, n = grid[0].length
        Set<List<List<Integer>>> distinctIslands = new HashSet<>()
        for(i = 0 i < m i ++):
            for(j = 0 j < n j++):
                List<List<Integer>> island = new ArrayList<>()
                if (dfs(i, j, i, j, grid, m, n, island)):
                    distinctIslands.add(island)
        return distinctIslands.size()
    private boolean dfs(i, j, x, y, int[][] grid, m, n, List<List<Integer>> island ):
        if(x < 0 || x >= m || y < 0 || y >= n || grid[x][y] <= 0) return false #  1: island, -: visited path
        grid[x][y] = -1
        island.add(Arrays.asList(x - i, y - j))
        for( k = 0 k < 4 k ++):
            dfs(i, j, x + d[k], y + d[k + 1], grid, m, n, island)
        return true
```
 Code: C++
```python
class Solution :
public:
    numDistinctIslands(vector<vector<int>>& grid) :
        m = grid.size(), n = grid[0].size()
        set<vector<vector<int>>> distinctIslands
        for(i = 0 i < m i ++):
            for(j = 0 j < n j++):
                vector<vector<int>> island
                if (dfs(i, j, i, j, grid, m, n, island)):
                    distinctIslands.insert(island)
        return distinctIslands.size()
private:
    d [5]  = :0,1,0,-1,0
    bool dfs(i, j, x, y, vector<vector<int>> & grid, m, n, vector<vector<int>> & island):
        if(x < 0 or x >= m or y < 0 or y >= n or grid[x][y] <= 0) return false
        grid[x][y] *= -1
        island.emplace_back(x-i, y-j)
        for(k = 0 k < 4 k++):
            dfs(i, j, x + d[k], y + d[k + 1], grid, m, n, island)
        return true
```
------------------------------------------------------------------------------------------------
 305. Number of Islands II
=============================
 A 2d grid map of
 `m` 
 rows and
 `n` 
 columns is initially filled with water. We may perform an
 ---addLand
 operation which turns the water at position (row, col) into a land. Given a list of positions to operate,
 count the number of islands after each addLand--- 
 operation
 . An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 Example:
```
Input:
 m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output:
 [1,1,2,3]
```
 Explanation:
 Initially, the 2d grid
 `grid` 
 is filled with water. (Assume 0 represents water and 1 represents land).
```
0 0 0
0 0 0
0 0 0
```
 Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
```
1 0 0
0 0 0   Number of islands = 1
0 0 0
```
 Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
```
1 1 0
0 0 0   Number of islands = 1
0 0 0
```
 Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
```
1 1 0
0 0 1   Number of islands = 2
0 0 0
```
 Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
```
1 1 0
0 0 1   Number of islands = 3
0 1 0
```
 Follow up:
 Can you do it in time complexity O(k log mn), where k is the length of the
 `positions` 
 ?
 Thoughts:
1. Union-find:
 UNION
 operation
 `O(1)` 
 .
 FIND
 operation is proportional to the depth of the tree. If N is the number of points added, the average running time is
 `O(logN)` 
 , and a sequence of
 `4N` 
 operations take
 `O(NlogN)` 
 . If there is no balancing, the worse case could be
 `O(N^2)` 
 .
2. Improvements:
	1. Path Compression: change the parent in the finding when the parent is not the root
	2. Union by rank:
		1. if rank a > rank b: then parent[b] = a
		2. if rank a < rank b: then parent[a] = b
		3. else make parent either way and just increase the rank of the parent one
 Code:
```python
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
 :type m: int
 :type n: int
 :type positions: List[List[int]]
 :rtype: List[int]
 """
        def find(parent, val):
            while parent[val] != val:
                '''
 Path Compression:
 parent[val] = parent[parent[val]]
 '''
                val = parent[val]
            return val
        def union(x, y):
            '''
 Union by Rank: 
 if rank[x] > rank[y]:
 x, y = y, x
 rank[y] += rank[x] == rank[y]
 '''
            parent[find(x)] = find(y)
            return find(y)
        parent ,  rank =  [-1] * (m * n), [0] * (m * n)
        d = [0, 1 , 0 , -1, 0]
        cnt = 0
        ans = []
        if m < 1 or n < 1:
            return []
        for pos in positions:
            cnt += 1
            root = n * pos[0] + pos[1]
            parent[root] = root
            # expanding its neightbor: once find there is a island, connect them
            for i in range(4):
                x , y = pos[0] + d[i] , pos[1] + d[i + 1]
                nb = x * n + y
                if x >= 0 and x < m and y >= 0 and y < n and parent[nb] != -1:
                    rootN = find(parent, nb)
                    if root != rootN:
                        root = union (root, rootN)
                        cnt -= 1
            ans.append(cnt)
        return ans
```
------------------------------------------------------------------------------------------------
 647. Number of palindromic substring
========================================
 647. Palindromic Substrings
==============================
 Given a string, your task is to count how many palindromic substrings in this string.
 The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
 Example 1:
```
Input:
 "abc"
Output:
 3
Explanation:
 Three palindromic strings: "a", "b", "c".
```
 Example 2:
```
Input:
 "aaa"
Output:
 6
Explanation:
 Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```
 Note:
1. The input string length won't exceed 1000.
 Thoughts:
1. Explanation by
 GeeksforGeeks
 (with
 extension problem to output all the substrings
 )
2. for loop with O(n^2) solution: having a pivot as a midpoint of palindrome and expand it in both directions to find all palindromes of even and odd lengths.
3. O(n) with
 Manacher’s algorithm
 Code:
```python
class Solution :
public:
    countSubstrings(string s) :
        ans = 0, n = s.length()
        for(i = 0 i < n ++i):
             #  odd: substring s[i-j, ..., i+j],
             #  i is the middle index of the substring 
            for(j = 0 i - j >= 0 && i + j < n
             && s[i - j] == s[i + j] j++) ans++
            #  even: substring s[i-1-j, ..., i+j], 
            #  (i-1, i) is the middle index of the substring
            for(j = 0 i - j  >= 0 && i + j + 1< n
             && s[i - j ] == s[i + j + 1] j++) ans++
        return ans
```
 Special thanks to
 caihao0727mail
 for providing this
 solution
 .
 Code: Interesting implementation using round-off
```
countSubstrings(string s) :
    num = s.size()
    for(float center = 0.5 center < s.size() center += 0.5) :
        left = int(center - 0.5), right = int(center + 1)
        while(left >= 0 && right < s.size() &&
         s[left--] == s[right++]) ++num
    return num
```
```
center 0.5: 0 1
center 1: 0 2
center 1.5: 1 2
center 2: 1 3
center 2.5: 2 3
center 3: 2 4
center 3.5: 3 4
center 4: 3 5
center 4.5: 4 5
```
 Code: Manacher's Algorithm: O(n) !
```python
class Solution(object):
    def countSubstrings(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            print "%s\n%s"%(A,Z)
            center = right = 0
            for i in xrange(1, len(A) - 1):
                # get the palindrome numbers based on right boundary 
                # and mirror palindrome 
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                # expand the palindrome at current pivot
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                    # update right boundary
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z
        return sum((v+1)/2 for v in manachers(S))
```
 Special thanks to
 hellokenlee
 for providing this
 solution
 .
------------------------------------------------------------------------------------------------
 975. Odd Even Jump
======================
 975. Odd Even Jump
====================
 You are given an integer array
 `A` 
 . From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called
 ---odd numbered jumps--- 
 , and the (2nd, 4th, 6th, ...) jumps in the series are called
 ---even numbered jumps--- 
 .
 You may from index
 `i` 
 jump forward to index
 `j` 
 (with
 `i < j` 
 ) in the following way:
* During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that
 `A[i] <= A[j]` 
 and
 `A[j]` 
 is the smallest possible value. If there are multiple such indexes
 `j` 
 , you can only jump to the
 smallest
 such index
 `j` 
 .
* During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that
 `A[i] >= A[j]` 
 and
 `A[j]` 
 is the largest possible value. If there are multiple such indexes
 `j` 
 , you can only jump to the
 smallest
 such index
 `j` 
 .
* (It may be the case that for some index
 `i,` 
 there are no legal jumps.)
 A starting index is_good_if, starting from that index, you can reach the end of the array (index
 `A.length - 1` 
 ) by jumping some number of times (possibly 0 or more than once.)
 Return the number of good starting indexes.
 Example 1:
```
Input: 
[10,13,12,14,15]
Output: 
2
Explanation: 
From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.
From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
From starting index i = 3, we can jump to i = 4, so we've reached the end.
From starting index i = 4, we've reached the end already.
In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.
```
 Example 2:
```
Input: 
[2,3,1,1,4]
Output: 
3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd numbered), we first jump to i = 1 because A[1] is the smallest value in (A[1], A[2], A[3], A[4]) that is greater than or equal to A[0].
During our 2nd jump (even numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in (A[2], A[3], A[4]) that is less than or equal to A[1].  A[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3.
During our 3rd jump (odd numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in (A[3], A[4]) that is greater than or equal to A[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with some number of jumps.
```
 Example 3:
```
Input: 
[5,1,3,4,2]
Output: 
3
Explanation: 
We can reach the end from starting indexes 1, 2, and 4.
```
 Note:
1. `1 <= A.length <= 20000`
2. `0 <= A[i] < 100000`
 Thoughts:
1. DP: dp[i][0]: even jump at i dp[i][1]: odd jump at i
 T:O(n^2)
2. Sort + Stack to eliminate double for loop: keep stack monotonic decreasing as frogs jump to index monotonic increasing.
 Code DP:
```python
class Solution(object):
    def oddEvenJumps(self, A):
        """
 :type A: List[int]
 :rtype: int
 """
        n = len(A)
        odd = [-1] * n
        even = [-1] * n
        dp = [[0,0] for _ in range(n)] 
        dp[-1] = [1, 1]
        for i in range(n - 2, -1, -1):
            max_val, max_idx, min_val, min_idx = min(A[i + 1:]) - 1, -1, max(A[i + 1:]) + 1, -1
            for j in range(i + 1, n):
                if A[i] >= A[j] and A[j] > max_val:
                    max_idx = j 
                    max_val = A[j]
                if A[i] <= A[j] and A[j] < min_val:
                    min_idx = j
                    min_val = A[j]
            odd[i] = min_idx
            even[i] = max_idx
        ans = 1
        for k in range(n - 2, -1, -1):
            if even[k] != -1: 
                dp[k][0] = dp[even[k]][1] # even -> odd 
            if odd[k] != -1:
                dp[k][1] = dp[odd[k]][0] # odd -> even
            ans += dp[k][1]
        return ans
```
 Code DP with stack optimization: T: O(nlogn)
```python
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        # odd/even[i] -- start at i, next jump is odd/even
        odd, even = [False] * n, [False] * n
        odd[-1], even[-1] = True, True
        # sort by value then by index
        Asort = sorted([(x, i) for i, x in enumerate(A)])
        Asort_rev = sorted([(-x, i) for i, x in enumerate(A)])
        # find the jump-to location of each index
        oddjump = self.findjump(Asort)
        evenjump = self.findjump(Asort_rev)
        n_good = 1
        # try all starting locations, both odd and even
        # make one jump, use the solution of the jump-to location
        for i in range(n-2, -1, -1):  # n-1,n-2...1,0
            j = oddjump[i]
            if j is not None:
                odd[i] = even[j]
            # if j is None, then no legal jump
            j = evenjump[i]
            if j is not None:
                even[i] = odd[j]
            if odd[i]:
                n_good += 1
        return n_good
    def findjump(self, Asort):
        # monotonic stack
        stack = []
        # the jump-to index of each index
        jumpto = [None] * len(Asort)
        for _, i in Asort:
            # pop the indexes smaller than current
            # point th jump-to of these indexes to current
            while stack and stack[-1] < i:
                jumpto[stack.pop()] = i
            # push into stack
            stack.append(i)
        return jumpto
```
------------------------------------------------------------------------------------------------
 OOD
=======
------------------------------------------------------------------------------------------------
 Orienteering Game
===================
 We are planning an orienteering game.
 The aim of this game is to arrive at the goal (G) from the start (S) with the shortest distance.
 However, the players have to pass all the checkpoints (@) on the map.
 An orienteering map is to be given in the following format.
 ########
 #@....G#
 ##.##@##
 #
 [email protected]
 #
 #@.....#
 ########
 In this problem, an orienteering map is to be given.
 Calculate the minimum distance from the start to the goal with passing all the checkpoints.
 Specification
 * A map consists of 5 characters as following.
 You can assume that the map does not contain any invalid characters and
 the map has exactly one start symbol 'S' and exactly one goal symbol 'G'.
 * 'S' means the orienteering start.
 * 'G' means the orienteering goal.
 * '@' means an orienteering checkpoint.
 * '.' means an opened-block that players can pass.
 * '#' means a closed-block that players cannot pass.
 * It is allowed to move only by one step vertically or horizontally (up, down, left, or right) to the
 next block.
 Other types of movements, such as moving diagonally (left up, right up, left down and right down)
 and skipping one or more blocks, are NOT permitted.
 * You MUST NOT get out of the map.
 * Distance is to be defined as the number of movements to the different blocks.
 * You CAN pass opened-blocks, checkpoints, the start, and the goal more than once if necessary.
 * You can assume that parameters satisfy following conditions.
 * 1 <= width <= 100
 * 1 <= height <= 100
 * The maximum number of checkpoints is 18.
------------------------------------------------------------------------------------------------
 1.   Palindrome Pairs
=========================
 Given a list of
 unique
 words, find all pairs of
 distinct
 indices
 `(i, j)` 
 in the given list, so that the concatenation of the two words, i.e.
 `words[i] + words[j]` 
 is a palindrome.
 Example 1:
```
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
```
 Example 2:
```
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
```
 Thoughts:
1. Build the trie tree in a reverse order ( assume the answer will be "word" + "reverse suffix" in the trie tree). For each node N that consists of:
	1. the corresponding word index for current trie tree sequence representation from the root.
	2. next: children nodes
	3. cover list (list of word index in which the word contains the current trie suffix and MAY also contain palindrome on its left part itself.
2. Search each word w1 matching suffix by traversing down the trie tree. If there is a stop node before the leaf node of the Trie tree (TrieNode that represents a word w2 in reverse order and that word is not the wording being searched itself (w2 != w1)) and also the rest part of w1 (len(l2) > len(w1)) is also a palindrome, then an concatenation of w1 + w2 is an answer. Else if at the leaf node of the Trie, then adding in every index element in terminal nodes' cover list such that the concatenation of w2 + w1 are also answers. Thus, we find all the solutions.
 Code: T: O(max(n * k^2, n^2) S:O(n^2 * k)
```python
class Solution :
    public List<List<Integer>> palindromePairs(String[] words) :
        List<List<Integer>>res = new ArrayList<>()
        TrieNode root = new TrieNode()
        for(i = 0 i < words.length i++) addWords (root, words[i], i)
        for(i = 0 i < words.length i++) search (root, words[i], i, res)
        return res
    private void addWords(TrieNode root, String word, index):
        for(i = word.length() - 1 i >=0 --i):
            pos = word.charAt(i) - 'a'
            if (isPalindrome(word, 0, i))
                root.cover.add(index)
            #  checking & traversing down to the trie tree
            if(root.next[pos] == null) root.next[pos] = new TrieNode()
            root = root.next[pos]
        root.index = index
        root.cover.add(index)#  since we have root node, in search when we go out of the for loop we
        #  ends up in the terminate node, so we need to add itslef to the cover list
    private void search(TrieNode root, String word, index, List<List<Integer>> res):
        for(i = 0 i < word.length() i++):
            if(root.index >= 0 && root.index != index && isPalindrome(word, i, word.length() - 1)) res.add(Arrays.asList(index, root.index))
            pos = word.charAt(i) - 'a'
            if(root.next[pos] == null) return
            root = root.next[pos]
        #  add the cover list index 
        for(i: root.cover):
            if(i != index)
                res.add(Arrays.asList(index, i))
    private boolean isPalindrome(String word, i, j):
        while(i < j):
            if(word.charAt(i++) != word.charAt(j--)) return false
        return true
class TrieNode:
    index
    TrieNode [] next
    List<Integer> cover
    TrieNode():
        index = -1
        next = new TrieNode [26]#  consider small cases only
        cover = new ArrayList<>()
```
------------------------------------------------------------------------------------------------
 Palindromic Substring
=========================
------------------------------------------------------------------------------------------------
 Parentheses
===============
------------------------------------------------------------------------------------------------
 113. Path Sum II
====================
 Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
 Note:
 A leaf is a node with no children.
 Example:
 Given the below binary tree and
 `sum = 22` 
 ,
```
       5
      / \
     4   8
    /   / \
   11  13  4
  /  \    / \
 7    2  5   1
```
 Return:
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```
 Thoughts:
1. Standard DFS backTracking
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public List<List<Integer>> pathSum(TreeNode root, sum) :
        List<List<Integer>> res = new ArrayList<>()
        List<Integer> path = new ArrayList<>()
        dfs(res, path, root, sum)
        return res
    private void dfs(List<List<Integer>> res, List<Integer>path, TreeNode root, sum):
        if(root == null) return
        path.add(root.val)
        if(root.left == null && root.right == null):
            if(sum == root.val) res.add(new ArrayList<>(path))
            path.remove(path.size() - 1)
            return
        dfs(res, path, root.left, sum - root.val)
        dfs(res, path, root.right, sum - root.val)
        path.remove(path.size() - 1)
```
------------------------------------------------------------------------------------------------
 437. Path Sum III
=====================
 You are given a binary tree in which each node contains an integer value.
 Find the number of paths that sum to a given value.
 The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
 The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
 Example:
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   /\     \
  3  2    11
 / \   \
3  -2   1
Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```
 Thoughts:
1. DFS recursion: T: O(N^2)
	1. Find the root.left and root.right: (base case: for root == null return 0)
	2. if (both left and right ==0)-> leaf node, then return 1,
	3. if only left == 0: have to return right + 1
	4. if only right == 0 have to return left + 1
	5. if both left and right != 0 then return the min(left,right) + 1
	6. Merge sort : T: T(N) = N + 2T(N/2) = O(NlogN) or O(N^2) for worse complexity (unbalanced tree)
2. Two Sum Method: Hash table: T: O(n) S: O(n):
	1. As we traverse down the tree, at an arbitrary node N, we store the sum until this node N (
	 sum_so_far (prefix) + N.val
	 ). in hash-table. Note this sum is the sum from root to N.
	2. Now at a grand-child of N, say G, we can compute the sum from the root until G since we have the prefix_sum until this grandchild available.We pass in our recursive routine.
	3. Search for prefixSum + node.val - target for the predecessor
	4. Once done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended(started) at a predecessor node.
 Code: DFS Recursion O(N^2)
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public pathSum(TreeNode root, sum) :
        if(root == null) return 0
        left = pathSum(root.left, sum)        
        right = pathSum(root.right, sum)      
        return left + right + pathSumStart(root, sum)
        #  wrong:
        #  left = pathSum(root.left, sum) + pathSum(root.left, sum - root.val) 
        #  right = pathSum(root.right, sum) + pathSum(root.right, sum - root.val) 
        #  System.out.println(root.val + " " + sum + " " + left + " " + right )
        #  return left + right + (root.val == sum ?1:0)
    private pathSumStart(TreeNode node, sum):
        if(node == null) return 0
        return (node.val == sum ?1:0)
            + pathSumStart(node.left, sum - node.val)
            + pathSumStart(node.right, sum - node.val)
```
 Code: Python
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def find_paths(self, root, sum):
        """
 :type root: TreeNode
 :type sum: int
 :rtype: int
 """
        if root:
            return int(root.val == sum) + self.find_paths(root.left, sum - root.val) + self.find_paths(root.right, sum - root.val)
        return 0
    def pathSum(self, root, sum):
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
```
 Code: Two-Sum: HashTable:
 T: O(n) S: O(n)
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def helper(self,root, target, preS, path):
        if root:
            key = preS + root.val - target
            if key in path:
                self.result += path[key]
            path.setdefault(preS + root.val, 0) # if not found, set to 0
            path[preS + root.val] +=1
            self.helper(root.left, target, preS+root.val, path)
            self.helper(root.right, target, preS+root.val, path)
            # remove predecessor from the record 
            path[preS + root.val] -=1
        return
    def pathSum(self, root, sum):
        """
 :type root: TreeNode
 :type sum: int
 :rtype: int
 """
        self.result = 0
        self.helper(root,sum,0, :0:1)
        return self.result
```
------------------------------------------------------------------------------------------------
 Path sum
============
------------------------------------------------------------------------------------------------
 279. Perfect Squares
========================
 Given a positive integer
 n
 , find the least number of perfect square numbers (for example,
 `1, 4, 9, 16, ...` 
 ) which sum to
 n
 .
 Example 1:
```
Input:
n = 12
Output: 3 
Explanation: 
12 = 4 + 4 + 4.
```
 Example 2:
```
Input:
n = 13
Output: 2
Explanation: 
13 = 4 + 9.
```
 Thoughts:
1. Dynamic Programming
	1. sq[i] = ... to number i
	2. sq[0] = 0
	3. search from 1 to j (j ^2 <= i): sq[i] = min(sq[i], sq[i-j^2] + 1)
2. Static Dynamic Programming
	1. sq[i]: ... to number i
	2. sq[0] = 0
	3. in the loop, each time push the result for sq[i] into ith of the container.
3. Mathematical Solution
	1. Lagrange's Four Square Theorem: Any natural number can be represented by the sum of at most 4 perfect square numbers
	2. number that need 4 perfect square meets: 4^k(8m + 7)
4. BFS
	1. Each node a number
	2. An edge between i and j exists if from node i to j, there is only one perfect number away.
 Code 1:
```python
class Solution :
public:
    numSquares(n) :
        vector<int> sq (n + 1, INT_MAX)
        sq[0] = 0
        for(i = 1 i < n + 1 i++):
            for(j = 1 j * j <= i  j++):
                sq[i] = min(sq[i], sq[i - j*j] + 1)
        return sq[n]
```
 Code 2:
```python
class Solution :
public:
    numSquares(n) :
        if( n <= 0 ) return 0
        static vector<int> sq (:0)
        while(sq.size() <= n):
            m = sq.size()
            cur = INT_MAX
            for(i = 1 i * i <= m i++):
                cur = min(cur, sq[m - i * i] + 1)
            sq.push_back(cur)
        return sq[n]
```
 Code 3: Lagrange's Four Square Theorem
```python
class Solution :
private: 
    is_square (n):
        sqrt_n = (int) (sqrt(n))
        return ( sqrt_n * sqrt_n == n)
public:
    numSquares(n) :
        #  result of 1:
        if(is_square(n)) return 1
        #  Based on Lagrange's Four Square theorem, there 
        #  are only 4 possible results: 1, 2, 3, 4.
        #  result of 4: 4^k(8m + 7) https:# en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
        while((n & 3) == 0) n >>= 2 #  n%4 == 0
        if((n & 7) == 7) return 4 #  n%8 == 7
        #  result of 2:
        sqrt_n = (int)(sqrt(n))
        for(i = 1 i <= sqrt_n i++):
            if(is_square(n - i * i)) return 2
        return 3
```
 Code 4: BFS: O(n*E)
```python
class Solution :
public:
    numSquares(n) :
        if(n <= 0):
            return 0
        vector<int> perfectSquares
        vector<int> record (n)
        for(i = 1 i * i <= n i++):
            perfectSquares.push_back(i * i)
            record[i * i - 1] = 1
        if(perfectSquares.back() == n) return 1
        queue<int> q
        for(auto& num: perfectSquares):
            q.push(num)
        count = 1
        while(!q.empty()):
            count++
            size = q.size()
            for(i = 0 i < size i++):
                curNum = q.front()
                for(auto& sqNum: perfectSquares):
                    if(curNum + sqNum == n) return count
                    else if((curNum + sqNum < n) && (record[curNum + sqNum - 1] == 0)):
                        q.push(curNum + sqNum)
                        record[curNum + sqNum - 1] = 1 # add into the queue, mark as explored
                    else if( curNum + sqNum > n) break
                q.pop()
        return 0
```
 from
 zhukov
 's
 post
------------------------------------------------------------------------------------------------
 326. Power of Three
=======================
 Given an integer, write a function to determine if it is a power of three.
 Example 1:
```
Input:
 27
Output:
 true
```
 Example 2:
```
Input:
 0
Output:
 false
```
 Example 3:
```
Input:
 9
Output:
 true
```
 Example 4:
```
Input:
 45
Output:
 false
```
 Follow up:
 Could you do it without using any
 loop / recursion?
 Thoughts
 because 3 is a prime number. Detection of power of 3 can be converted to whether 3^19 = 1162261467 (largest power of 3 you can get for value in a 32 bit machine) can divide the number n.
```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
 :type n: int
 :rtype: bool
 """
        return n > 0 and pow(3,19,n)== 0
```
------------------------------------------------------------------------------------------------
 298. Product of Array Except Self
=====================================
 Given an array
 `A` 
 of
 ---n integers where n--- 
 > 1, return an array
 `output` 
 such that
 `output[i]` 
 is equal to the product of all the elements of
 `A` 
 except
 `A[i]` 
 .
 Example:
```
Input: [1,2,3,4]
Output: [24,12,8,6]
```
 Note:
 Please solve it
 without division
 and in O(
 ---n--- 
 ).
 Follow up:
 Could you solve it with constant space complexity? (The output array
 does not
 count as extra space for the purpose of space complexity analysis.)
 Code: with extra space:
```python
class Solution(object):
    def productExceptSelf(self, A):
        """
 :type A: List[int]
 :rtype: List[int]
 """
        m = collections.defaultdict(list)
        p = 1
        for i, num in enumerate(A):
            m[i] = p
            p *= num
        p = 1
        for i, num in reversed(list(enumerate(A))):
            m[i] *= p
            p *= num
        return [m[k] for k in sorted(m.keys())]
```
 Code: without extra space:
```python
class Solution :
    public int[] productExceptSelf(int[] A) :
        n = A.length
        res [] = new [n]
        p = 1
        #  multiply left
        for(i = 0 i < n i++):
            res[i] = p
            p *= A[i]
        #  multiply right
        p = 1
        for(i = n - 1 i >=0  i--):
            res[i]*= p
            p *= A[i]
        return res
```
 Code: actually index is the key: so we do not need the extra dictionary
```python
class Solution(object):
    def productExceptSelf(self, A):
        """
 :type A: List[int]
 :rtype: List[int]
 """
        # m = collections.defaultdict(list)
        res = [0] * len(A)
        p = 1
        # left
        for i, num in enumerate(A):
            res[i] = p
            p *= num
        p = 1
        for i, num in reversed(list(enumerate(A))): # i is also reversed
            res[i] *= p
            p *= num
        return res
```
------------------------------------------------------------------------------------------------
 Quant Dev
=============
------------------------------------------------------------------------------------------------
 406. Queue Reconstruction by Height
=======================================
 Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers
 `(h, k)` 
 , where
 `h` 
 is the height of the person and
 `k` 
 is the number of people in front of this person who have a height greater than or equal to
 `h` 
 . Write an algorithm to reconstruct the queue.
 Note:
 The number of people is less than 1,100.
 Example
```
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```
 Thoughts:
1. Sort the h in descending order and k in ascending order.
2. Traverse the sorted list and insert the current person into kth position of new list.
 Code T: O(n^2) S:O(n)
```python
class Solution(object):
    def reconstructQueue(self, people):
        """
 :type people: List[List[int]]
 :rtype: List[List[int]]
 """
        people.sort(key = lambda x: [-x[0], x[1]])
        result = []
        for [h, k] in people:
            result.insert(k, [h,k])
        return result
```
 more explicit way: first group the height, then sort in each group, then insert into the final list:
```python
class Solution(object):
    def reconstructQueue(self, people):
        """
 :type people: List[List[int]]
 :rtype: List[List[int]]
 """
        # sort the h, and then sort the k and insert into kth postiion in new list
        peopledict, height, res = :, [], [] 
        for i in range(len(people)):
            p = people[i]
            if p[0] not in peopledict:
                peopledict[p[0]] = [(p[1], i)]
                height+= p[0],
            else:
                peopledict[p[0]] += (p[1], i),
        height.sort(reverse=True)
        for h in height:
            peopledict[h].sort()
            for k, i in peopledict[h]:
                res.insert(k, people[i])
        return res
```
 the first solution is from
 djrochford
 and the second is from
 YJL1228
 in this
 post
------------------------------------------------------------------------------------------------
 304. Range Sum Query 2D - Immutable
=======================================
 Given a 2D matrixmatrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1,col1) and lower right corner (row2,col2).
![](https:# leetcode.com/static/images/courses/range_sum_query_2d.png "Range Sum Query 2D")
 The above rectangle (with the red border) is defined by (row1, col1) =
 (2, 1)
 and (row2, col2) =
 (4, 3)
 , which contains sum =
 8
 .
 Example:
```
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```
 Note:
1. You may assume that the matrix does not change.
2. There are many calls tosumRegion function.
3. You may assume that row1 ≤ row2 and col1 ≤ col2.
 Thoughts:
1. Having a 2D dp arrays (m + 1, n + 1)
2. When building: dp[i][i] = matrix[i -1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] for i, j in [1,m] and [1,n]
3. When calculating the query: res = dp[row2 + 1][col2 + 1] - dp[row2 + 1][col1] - dp[row1][col2 + 1] + dp[row1][col1]
4. In Python: Initialize 2D list needs to be initialized as [[0] * m] for _ in range(n)) instead of [[0] * m]*n] since this would create n identical lists with the same reference.
 Code
```python
class NumMatrix(object):
    def __init__(self, matrix):
        """
 :type matrix: List[List[int]]
 """
        self.m, self.n = len(matrix), len(matrix[0]) if len(matrix) else 0
        self.dp = [[0] * (self.n + 1) for _ in range(self.m + 1)] # cannot do [[0] * (self.n + 1)] * (self.m + 1)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.dp[i][j] =  matrix[i - 1][j - 1] + self.dp[i - 1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]
    def sumRegion(self, row1, col1, row2, col2):
        """
 :type row1: int
 :type col1: int
 :type row2: int
 :type col2: int
 :rtype: int
 """
        return self.dp[row2 + 1][col2 + 1] -self.dp[row2 + 1][col1] -self.dp[row1][col2 + 1] + self.dp[row1][col1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```
------------------------------------------------------------------------------------------------
 308. Range Sum Query 2D - Mutable
=====================================
 Given a 2D matrixmatrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1,col1) and lower right corner (row2,col2).
![](https:# leetcode.com/static/images/courses/range_sum_query_2d.png "Range Sum Query 2D")
 The above rectangle (with the red border) is defined by (row1, col1) =
 (2, 1)
 and (row2, col2) =
 (4, 3)
 , which contains sum =
 8
 .
 Example:
```
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -
>
 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -
>
 10
```
 Note:
1. The matrix is only modifiable by the update function.
2. You may assume the number of calls to update and sumRegion function is distributed evenly.
3. You may assume that row 1 ≤ row 2 and col 1 ≤ col 2.
 Thoughts:
 Construct a 2D binary indexed tree such that each entry in the tree [i,j] corresponds the
 sum
 of its responsible children
 Sum in the tree expresses the sum from matrix[i -1][j -1] to [0][0] so a solution performed using the submatrix sum: that is sum(row2 + 1, col + 1) - sum(row1, col2 + 1) - sum(row2 + 1, col1) + sum(row1, col1)
 Code: T: O(log(mn)) = O(log(m) +
```python
class NumMatrix :
    [][] tree, A
    m , n
    public NumMatrix(int[][] matrix) :
        if(matrix.length == 0 || matrix[0].length == 0)
            return
        m = matrix.length
        n = matrix[0].length
        tree = new int[m + 1][n + 1]
        A = new int[m][n]
        for (i = 0 i < m  i ++):
            for (j = 0 j < n j++):
                update(i,j,matrix[i][j])
    public void update(row, col, val) :
        if(m == 0 || n == 0) return
        delta = val - A[row][col]
        A[row][col] = val
        for(i = row + 1 i <= m  i += i & (-i)):
            for(j = col + 1 j <= n  j += j & (-j)):
                tree[i][j] += delta
    public sumRegion(row1, col1, row2, col2) :
        return (sum(row2 + 1, col2 + 1) - sum(row1, col2 + 1) - sum(row2+ 1, col1) + sum(row1, col1))
    public sum(row, col):
        sum = 0
        for(i = row i > 0 i -= i & (-i) ):
            for (j = col j > 0 j-= j & (-j)):
                sum += tree[i][j]
        return sum
/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix)
 * obj.update(row,col,val)
 * param_2 = obj.sumRegion(row1,col1,row2,col2)
 */
```
------------------------------------------------------------------------------------------------
 358. Rearrange String k Distance Apart
==========================================
 358. Rearrange String k Distance Apart
========================================
 Given a non-empty string
 s
 and an integer
 k
 , rearrange the string such that the same characters are at least distance
 k
 from each other.
 All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string
 `""` 
 .
 Example 1:
```
s = "aabbcc", k = 3
Result: "abcabc"
The same letters are at least distance 3 from each other.
```
 Example 2:
```
s = "aaabc", k = 3 
Answer: ""
It is not possible to rearrange the string.
```
 Example 3:
```
s = "aaadbbcc", k = 2
Answer: "abacabcd"
Another possible answer is: "abcabcda"
The same letters are at least distance 2 from each other.
```
 Credits:
 Special thanks to
 @elmirap
 for adding this problem and creating all test cases.
------------------------------------------------------------------------------------------------
 99. Recover Binary Search Tree
==================================
 99. Recover Binary Search Tree
================================
 Two elements of a binary search tree (BST) are swapped by mistake.
 Recover the tree without changing its structure.
 Example 1:
```
Input:
 [1,3,null,null,2]
   1
  /
 3
  \
   2
Output:
 [3,1,null,null,2]
   3
  /
 1
  \
   2
```
 Example 2:
```
Input:
 [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
Output:
 [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3
```
 Follow up:
* A solution using O(
 ---n--- 
 ) space is pretty straight forward.
* Could you devise a constant space solution?
 Thoughts:
1. In-order traversal + first, sec, prev node global record
2. Morris traversal to save space
 Code 1 T: O(n) S: O(n) due to call stack space:
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    TreeNode first
    TreeNode sec
    TreeNode prev
    public void recoverTree(TreeNode root) :
        if(root == null) return
        inorder_traversal(root)
        #  swap the first and sec value
        tmp = first.val
        first.val = sec.val
        sec.val = tmp
        return
    private void inorder_traversal(TreeNode cur):
        if(cur == null) return
        inorder_traversal(cur.left)
        if(first == null && (prev != null && prev.val > cur.val)) first = prev
        if(first != null && prev.val > cur.val) sec = cur
        prev = cur
        inorder_traversal(cur.right)
```
 Code 2: T:O(n) S: O(1)
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public void recoverTree(TreeNode root) :
        TreeNode prev = null #  previous node in in-order traversal
        TreeNode first = null
        TreeNode sec = null
        #  Morris Traversal:
        TreeNode pred = null #  previous node in Morris Traversal
        while(root != null):
            #  constructing threading
            if (root.left != null):
                 pred = root.left
                    while(pred.right != null && pred.right != root):
                        pred = pred.right
                    if(pred.right == null):
                        #  connecting 
                        pred.right = root
                        root = root.left
                    else:
                        #  pred.right == root: visited
                        #  record the first and second node
                        if(prev.val > root.val):
                            if(first == null) :first = prev sec = root
                            else :sec = root
                        #  disconnecting
                        pred.right = null
                        #  updating prev
                        prev = root
                        root = root.right
            else:
                if(prev != null && prev.val > root.val):
                        if(first == null) :first = prev sec = root
                        else :sec = root
                prev = root
                root = root.right
        #  swap first and sec node values
        #  if(first != null && sec != null):
            tmp = first.val
            first.val = sec.val
            sec.val = tmp
        #  
```
------------------------------------------------------------------------------------------------
 10. Regular Expression Matching
===================================
 10. Regular Expression Matching
=================================
 Implement regular expression matching with support for
 `'.'` 
 and
 `'*'` 
 .
```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the 
entire
 input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```
 Thoughts:
1. similar to
 44. Wildcard Matching
2. Recursion:
	1. if there is a X* in pattern string: can match empty string ( so we jump to matching the rest) or matching current string ( so we compare them one by one)
	2. if current pattern string is NOT a character followed by a * wildcard, just check whether the current char matches the one in the input string.
3. DP idea: f[i][j]: if s[0..i-1] matches p[0..j-1]
	1. if p[j - 1] != '*'
		1. f[i][j] = f[i - 1][j - 1] && s[i - 1] == p[j - 1]
	2. if p[j - 1] == '*', denote p[j - 2] with x
		1. 1) "x*" repeats 0 time and matches empty: f[i][j - 2]
		2. 2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && f[i - 1][j]
 Code T: O(n) S: O(n^2)
```python
class Solution :
public:
    bool isMatch(string s, string p) :
        if (p.empty())    return s.empty()
        if ('*' == p[1])
            #  x* matches empty string or at least one character: x* -> xx*
            #  *s is to ensure s is non-empty
            return (isMatch(s, p.substr(2)) || !s.empty()
                    && (s[0] == p[0] || '.' == p[0]) && isMatch(s.substr(1), p))
        else
            return !s.empty() && (s[0] == p[0] || '.' == p[0]) 
            && isMatch(s.substr(1), p.substr(1))
```
 Code DP T: O(n^2)
```python
class Solution :
public:
    bool isMatch(string s, string p) :
        m = s.size(), n = p.size()
        vector<vector<bool>> f (m + 1, vector<bool>(n + 1, false))
        f[0][0] = true
        for (j = 1  j <= n j++):
            f[0][j] = j > 1 && f[0][j-2] && '*' == p[j - 1]
        for( i = 1 i <= m  i++):
            for(j = 1 j <= n j++):
                if(p [j-1] == '*' && j > 1)
                    f[i][j] = (f[i][j - 2])||(s[i - 1] == p[j - 2] || '.' == p[j - 2]) && f[i - 1][j]
                else
                    f[i][j] = (s[i - 1] == p[j - 1] || '.' == p[j-1]) && f[i - 1][j - 1]
        return f[m][n]
```
 Special Thanks
 Pale Blue Dot's
 solution
------------------------------------------------------------------------------------------------
 316. Remove Duplicate Letters
=================================
 Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
 Example 1:
```
Input:
"bcabc"
Output:
"abc"
```
 Example 2:
```
Input:
"cbacdcbc"
Output:
"acdb"
```
 Thoughts
1. Greedy: In the search space of i to j where the last character in s[i...j] in also of its last appearance of the whole string s, find the small character in lexicographical order, delete it in the subsequent substring and then perform the search starting from j + 1.
2. Using stack:
	1. Count the letter frequency with an Array
	2. Build a ascending stack: Each time adding a letter to the stack if it has not been added into the stack, mark letter as
	 visited
	 . If current letter is smaller than the that on top of the stack,
	 and
	 top letter has remaining appearance after (as checked by indexing the letter frequency array), pop the letter out and mark it as
	 not visited
 Code 1: O(n)
```python
class Solution :
    public String removeDuplicateLetters(String s) :
        [] cnt = new [26]
        for (i = 0 i < s.length() i++):
            cnt[s.charAt(i) - 'a']++
        pos = 0
        for(i = 0 i < s.length() i++):
            if(s.charAt(pos) > s.charAt(i)) pos = i
            if (--cnt[s.charAt(i) - 'a'] == 0) break
        return s.length() == 0 ? "": s.charAt(pos) + removeDuplicateLetters(s.substring(pos + 1).replaceAll("" + s.charAt(pos), ""))
```
 Code 2 : O(n)
```python
class Solution :
    public String removeDuplicateLetters(String s) :
        [] res = new int[26]
        boolean [] vis = new boolean [26]
        char[] chars = s.toCharArray()
        Stack<Character> st = new Stack<>()
        for(char c: chars):
            res[c - 'a']++
        index = -1
        for (char c: chars):
            index = c - 'a'
            res[index] --
            if (vis[index])
                continue
            while (!st.isEmpty() && c < st.peek() && res[st.peek() - 'a']!= 0):
                char top = st.pop()
                vis[top - 'a'] = false
            st.push(c)
            vis[index] = true
        StringBuilder sb = new StringBuilder()
        while (!st.isEmpty()):
            sb.insert(0, st.pop())
        return sb.toString()
```
------------------------------------------------------------------------------------------------
 301. Remvoe Invalid Parenthesis
===================================
 301. Remove Invalid Parentheses
=================================
 Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
 Note:
 The input string may contain letters other than the parentheses
 `(` 
 and
 `)` 
 .
 Example 1:
```
Input:
 "()())()"
Output:
 ["()()()", "(())()"]
```
 Example 2:
```
Input:
 "(a)())()"
Output:
 ["(a)()()", "(a())()"]
```
 Example 3:
```
Input:")("
Output: [""]
```
 Facebook Variation: any solution that results in minimum removal of parentheses
 Thoughts
 : 楼主用了一个3-pass的方法: 先从头到尾找close比open多的，移掉 从尾到头找open比close多的，移掉 然后最后一遍build
```python
class Solution:
    def removeInvalidParentheses(self, s):
        cnt = 0
        idx = []
        ans = ''
        # forward to remove close first
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
            if c == ')':
                cnt -= 1
                if cnt < 0:
                    idx.append(i)
                    cnt = 0  # reset the cnt
        cnt = 0
        # reverse to remove open first
        for i, c in enumerate(s[::-1]):
            if c == ')':
                cnt += 1
            if c == '(':
                cnt -= 1
                if cnt < 0:
                    idx.append(len(s) - i - 1)
                    cnt = 0
        return ''.join([s[i] for i in range(len(s)) if i not in idx])
s1= Solution()
print(s1.removeInvalidParentheses(""))
print(s1.removeInvalidParentheses("("))
print(s1.removeInvalidParentheses(")"))
print(s1.removeInvalidParentheses("(()"))
print(s1.removeInvalidParentheses("(()))"))
```
 Thoughts:
1. Expanding the set and test whether each combination is valid, once there is answer in the set , then return (we want the minimum edition)
 Code: Python
```python
class Solution:
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = :s
        while True:
            res = filter(isvalid, level)
            if res:
                return res
            level = :s[:i] + s[i+1:] for s in level for i in range(len(s))
```
------------------------------------------------------------------------------------------------
 767. Reorganize String
==========================
 Given a string
 `S` 
 , check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
 If possible, output any possible result. If not possible, return the empty string.
 Example 1:
```
Input: S = "aab"
Output: "aba"
```
 Example 2:
```
Input: S = "aaab"
Output: ""
```
 Note:
* `S` 
 will consist of lowercase letters and have length in range
 `[1, 500]` 
 .
 Thought:
1. Priority Queue + queue: Having two queues, ones pq: recording the priority of the element: the other with queue, record the use of previous charcter. First dump all the <int, char> pair into priority queue, then everytime pq pops() add it to the queue. if the top element of the queue has count < =0 then use one count, add it to the result string and take it back to priority queue until pq is empty and queue.size() <= 1. (Detailed implementation see the code)
2. Sort
3. Greedy + Sort (Optimized): sort the arr according to frequency, then insert the top half frequent into even position and bottom half, less frequent one into odd position. Final answer is return if the last two element is not the same (meaning
 Code: Sort
```python
class Solution :
public:
    string reorganizeString(string S) :
        #  sort the string by occurance and reorder them as count * val
        #  having two pointers i,j: starting from 0, and (n-1)1/2 + 1, append the result sequentially from i and j
        n = S.size()
        vector<int> m (26)
        for(char c : S)m[c-'a']++
        vector<pair<int, char>> charCounts
        for(i = 0  i < 26 i++):
            if (m[i] > (n + 1)/2) return ""
            if(m[i]) charCounts.push_back(:m[i], i+'a')
        sort(charCounts.rbegin(), charCounts.rend())
        string sorted
        for(auto& p :charCounts)
            sorted += string(p.first, p.second)
        string ans
        for(i = 0, j = (n-1)/2 + 1 i <= (n-1)/2 i++, j++):
            ans += sorted[i]
            if(j < n) ans += sorted[j]
        return ans
```
 Greedy + Sort:
```python
class Solution(object):
    def reorganizeString(self, S):
        """
 :type S: str
 :rtype: str
 """
        a = sorted(sorted(S), key=S.count)
        h = len(a) / 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1:] != a[-2:-1])
```
 PriorityQueue:
```python
class Solution :
public:
    string reorganizeString(string S) :
        vector<int> m(26) n =S.size()
        priority_queue<pair<int,char>>pq
        queue<pair<int,char>>q
        for(char c: S) m[c-'a']++
        for(i = 0 i < 26 i++):
            if (m[i] > (n+ 1) /2) return ""
            if(m[i]) pq.push(:m[i], i + 'a')
        string ans
        while(!pq.empty()||q.size() > 1):
            if(q.size() > 1):
                auto cur = q.front()
                q.pop()
                if(cur.first != 0) pq.push(cur)
            if (!pq.empty()):
                auto cur = pq.top() pq.pop()
                ans += cur.second
                cur.first--
                q.push(cur)
        return ans
```
------------------------------------------------------------------------------------------------
 398. Reservoir Sampling
===========================
 Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
 Note:
 The array size can be very large. Solution that uses too much extra space will not pass the judge.
 Example:
```
int[] A = new int[] :1,2,3,3,3
Solution solution = new Solution(A)
#  pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3)
#  pick(1) should return 0. Since in the array only A[0] is equal to 1.
solution.pick(1)
```
```python
class Solution :
    vector<int> A
public:
    Solution(vector<int> A) :
        this->A = A
    pick(target) :
        res
        cnt = 0
        for(i = 0 i < A.size() i++):
            if(A[i] != target) continue
            if(cnt == 0) :res = i cnt++
            else:
                #  with prob 1/(n+1) to replace the previous index
                if(rand()%(++cnt) == 0) res = i
        return res
/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(A)
 * param_1 = obj.pick(target)
 */
```
```python
class Solution :
    int[] A
    Random rand
    public Solution(int[] A) :
        this.A = A
        rand = new Random()
    public pick(target) :
        cnt = 0, res = -1
        for(i = 0 i < A.length i++):
            if(A[i] != target) continue
            #  with prob 1/(n+1) to replace the previous index
            if(rand.nextInt(++cnt) == 0)  res = i
        return res
/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(A)
 * param_1 = obj.pick(target)
 */
```
------------------------------------------------------------------------------------------------
 7. Reverse Integer
======================
 Given a 32-bit signed integer, reverse digits of an integer.
 Example 1:
```
Input: 123
Output: 321
```
 Example 2:
```
Input: -123
Output: -321
```
 Example 3:
```
Input: 120
Output: 21
```
 Note:
 Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range
 : [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
 Thoughts:
1. Use String:
	1. sign:
	2. reverse abs value: sign * x [::-1]
	3. s * r* (r < 2 ^31)
2. Not use string: Standard way of detecting overflow
```python
class Solution(object):
    def reverse(self, x):
        """
 :type x: int
 :rtype: int
 """
        #sign 
        s = cmp(x,0)
        # reverse abs
        r = int(`s*x`[::-1])
        return s * r * (r < 2 ** 31)
```
```python
class Solution :
    public reverse(x):
        result = 0
        while (x != 0)
        :
            tail = x % 10
            newResult = result * 10 + tail
            if ((newResult - tail) / 10 != result) return 0
            result = newResult
            x /= 10
        return result
```
------------------------------------------------------------------------------------------------
 493. Reverse Pairs
======================
 493. Reverse Pairs
====================
 Given an array
 `A` 
 , we call
 `(i, j)` 
 an
 important reverse pair
 if
 `i < j` 
 and
 `A[i] > 2*A[j]` 
 .
 You need to return the number of important reverse pairs in the given array.
 Example1:
```
Input: [1,3,2,3,1]
Output: 2
```
 Example2:
```
Input: [2,4,3,5,1]
Output: 3
```
 Note:
1. The length of the given array will not exceed
 `50,000` 
 .
2. All the numbers in the input array are in the range of 32-bit integer.
 Thoughts:
1. Implementation of BST (Binary Search Tree):
	1. Node : val, cnt (sub-problem result), left, right
	2. for each element in the A: perform search and insert: search element >= 2nums[i] + 1 from the root, and insert val into the root.
	3. implementation of search:
		1. if root is none -> return
		2. if val < root.val -> meaning hitting the upper bound -> return root.cnt + search (root.left, val)
		3. if val == root.val -> return root.cnt
		4. if val > root.val -> meaning current root.val in not the upper bound -> search (root.right, val)
	4. T: O(nlogn) - O(n^2)
2. Implementation of BIT (Binary Indexed Tree):
	1. Sort the original array into a copy
	2. For each element in the original array sequentially:
		1. Using binary search to find corresponding index in the sorted array from the element in the original array
		2. Search in the BIT and then Insert the entry into BIT
3. Implementation of Merge Sort:
	1. For partition recurrence relation, setting
	 `i = 0, j = n - 1, m = (n-1)/2` 
	 , we have:
	 `T(0, n - 1) = T(0, m) + T(m + 1, n - 1) + C`
	2. where the subproblem
	 `C` 
	 now reads
	 "find the number of important reverse pairs with the first element of the pair coming from the left subarray
	 `A[0, m]` 
	 while the second element of the pair coming from the right subarray
	 `A[m + 1, n - 1]` 
	 "
	 .
	3. Again for this subproblem, the first of the two aforementioned conditions is met automatically. As for the second condition, we have as usual this plain linear scan algorithm, applied for each element in the left (or right) subarray. This, to no surprise, leads to the
	 `O(n^2)` 
	 naive solution.
	4. Fortunately
	 the observation holds true here that the order of elements in the left or right subarray does not matter
	 , which prompts sorting of elements in both subarrays. With both subarrays sorted,
	 the number of important reverse pairs can be found in linear time by employing the so-called two-pointer technique
	 : one pointing to elements in the left subarray while the other to those in the right subarray and both pointers will go only in one direction due to the ordering of the elements.
	5. The last question is which algorithm is best here to sort the subarrays. Since we need to partition the array into halves anyway, it is most natural to adapt it into a
	 `Merge-sort` 
	 . Another point in favor of
	 `Merge-sort` 
	 is that the searching process above can be embedded seamlessly into its merging stage.
	6. So here is the
	 `Merge-sort` 
	 -based solution, where the function
	 `"reversePairsSub"` 
	 will return the total number of important reverse pairs within subarray
	 `A[l, r]` 
	 . The two-pointer searching process is represented by the nested
	 `while` 
	 loop involving variable
	 `p` 
	 , while the rest is the standard merging algorithm.
4. Reference
 Code : BST (LTE) since O(n^2) for data like [1,2,3....]
```python
class Solution(object):
    def reversePairs(self, A):
        """
 :type A: List[int]
 :rtype: int
 """
        ans = 0
        root = None
        for num in A:
            ans += self.search(root, (num << 1) + 1)
            root = self.insert(root, num)
        return ans
    def search(self, root, val):
        if root is None:
            return 0
        elif val < root.val:
            return root.cnt + self.search(root.left, val)
        elif val == root.val:
            return root.cnt
        else:
            return self.search(root.right, val)
    def insert(self, root, val):
        if root is None:
            root = BSTNode(val)
        elif val < root.val:
            root.left = self.insert(root.left,val)
        elif val == root.val:
            root.cnt+= 1
        else:
            root.cnt+= 1
            root.right = self.insert(root.right, val)
        return root
class BSTNode(object):
    def __init__ (self, val):
        self.val = val
        self.cnt = 1
        self.left = self.right = None
```
 Code : BIT T: O(nlogn)
```python
class Solution(object):
    def reversePairs(self, A):
        """
 :type A: List[int]
 :rtype: int
 """
        def index (arr, val):
            l, r, m = 0, len(arr) - 1, 0
            while(l <= r):
                m = l + ((r - l)>> 1)
                if(arr[m] >= val):
                    r = m - 1
                else: 
                    l = m + 1
            return l + 1
        def search(bit, i):
            s = 0
            while i < len(bit): # this problem asks "greater than", opposite to the conventional BIT
                s += bit [i]
                i += i & -i
            return s 
        def insert(bit, i): # this problem asks "greater than", opposite to the conventional BIT
            while i > 0 : 
                bit[i] += 1
                i -= i& -i
        ans = 0
        bit = [0] * (len(A) + 1)
        sortedNums = sorted(A)
        for num in A:
            ans += search(bit, index(sortedNums, 2L * num + 1))
            insert( bit,  index(sortedNums, num))    
        return ans
```
 Code: Merge-Sort T: O(nlogn)
```python
class Solution :
    public reversePairs(int[] A) :
        return reversePairsHelper(A, 0, A.length - 1)
    private reversePairsHelper([] A, l, r):
        if(l >= r ) return 0
        m = l + ((r - l) >> 1)
        ans = reversePairsHelper(A, l, m) + reversePairsHelper(A, m + 1, r)
        left = l, right = m + 1, i = 0, pair = m + 1
        [] merge = new int[r - l + 1]
        while(left <= m):
            #  search
            while(pair <= r && A[left] > 2L * A[pair]) pair++
            ans += pair - (m + 1)
            #  merge (insert)
            while(right <= r && A[left] >= A[right]) merge[i++] = A[right++]
            merge[i++] = A[left++]
        #  add the leftover from right to r
        while(right <= r) merge[i++] = A[right++]
        System.arraycopy(merge, 0, A, l, merge.length)
        return ans
```
------------------------------------------------------------------------------------------------
 48. Rotate Image(Amazon, MicroSoft, Apple)
==============================================
### 
 48. Rotate Image
 You are given annxn2D matrix representing an image.
 Rotate the image by 90 degrees (clockwise).
 Note:
 You have to rotate the image
 in-place
 , which means you have to modify the input 2D matrix directly.
 DO NOT
 allocate another 2D matrix and do the rotation.
 Example 1:
```
Given 
input matrix
 = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix 
in-place
 such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```
 Example 2:
```
Given 
input matrix
 =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
rotate the input matrix 
in-place
 such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```
 [Thoughts]
 两种常用解法，建议用第二种，快，简洁，好记
 [Code1:
 Figure out the correct corresponding index and i,j range in the for loop
 ]
```python
class Solution :
    n
public:
    void rotate(vector<vector<int>>& matrix) :
        if (matrix.size() == 0) return
        n = matrix.size()
        for (i = 0 i < (n+1)/2 i++ ):
            for (j = 0 j < n/2  j++):
                #  here i and j only needs one to be (n+1)/2 and the other be n/2
                #  [i,j] -> [j][n-1-i] -> [n-1-i][n-1-j]->[n-1-j][i] 
                #  ^ |
                #  |----------------------------------------------------------------------------------------------------------------|
                temp = matrix[j][n-1-i] #  who is the temp does not matter
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = temp
```
 [Code2:
 reverse up down + swap symmetry
 (Recommend)]
```
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3 7 8 9 7 4 1
 * 4 5 6 => 4 5 6 => 8 5 2
 * 7 8 9 1 2 3 9 6 3
*/
void rotate(vector<vector<int> > &matrix) :
    reverse(matrix.begin(), matrix.end())
    for (i = 0 i < matrix.size() ++i) :
        for (j = i + 1 j < matrix[i].size() ++j)
            swap(matrix[i][j], matrix[j][i])
```
 Extension:
 counter-clockwise
 : reverse left to right + swap the symmetry
```
/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3 3 2 1 3 6 9
 * 4 5 6 => 6 5 4 => 2 5 8
 * 7 8 9 9 8 7 1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) :
    for (auto vi : matrix) reverse(vi.begin(), vi.end())
    for (i = 0 i < matrix.size() ++i) :
        for (j = i + 1 j < matrix[i].size() ++j)
            swap(matrix[i][j], matrix[j][i])
```
------------------------------------------------------------------------------------------------
 扫雷
======
 扫雷
====
 游戏的目标是尽快找到雷区中的所有地雷，而不许踩到地雷。如果方块上的是地雷，将输掉游戏。如果方块上出现数字，则表示在其周围的八个方块中共有多少颗地雷。你的任务是在
 已知地雷出现位置的情况下，得到各个方块中的数据。
 Example:
 for map:
```
*...
....
.*..
....
```
 we have:
```
*100
2210
1*10
1110
```
 I/O format:
 --input--
 输入有多组数据，每组数据的第一行有两个数字，m,n(0<m,n<100)表示游戏中雷区的范围为m×n。接下来m行每行有n个字符。“*” 表示有地雷，“.”表示无地雷。最后一组数据m=0,n=0表示输入结束，不需要处理。
 --output--
 #x:
 其中 x 是当前地图的编号（从 1 开始）。下面的 n 行则将地图中的 "." 以数字表示，该数字表示该方格周围有多少颗地雷。
 --example input--
```
4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
```
 --example output--
```
Field #1:
*100
2210
1*10
1110
Field #2:
**100
33200
1*100
```
 Code
```
# 
#  Created by Zirui Tao on 1/12/2018.
# 
#include <stdlib.h>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define max std::max
#define min std::min
# 布局
char block[101][101]
# 格子周围雷数
num[101][101]
# max(a,b)
# :
#  return a>b?a:b
# 
# min(a,b)
# :
#  return a<b?a:b
# 
input(raw,colum)
:
    /**输入扫雷布局*/
    memset(block,'0',sizeof(block))
    for(i=0i<raw++i)
    :
        for(j=0j<colum++j)
        :
            scanf("%c",&block[i][j])
        scanf("%*c")
    printf("%c", block[0][0])
    return 0
mineNum(raw,colum)
:
    for(i=0i<rawi++)
    :
        for(j=0j<columj++)
        :
            num[i][j]=0
            if(block[i][j]=='*')
            :
                printf("*")
            else
            :
                # 上下,行，区间左端点的最大值（>=0），区间右端点的最小值（<=row-1）
                for(k=max(i-1,0)k<=min(i+1,raw-1)k++)
                :
                    for(t=max(j-1,0)t<=min(j+1,colum-1)t++)
                    :
                        if(block[k][t]=='*')
                        :
                            num[i][j]++
                printf("%d",num[i][j])
        printf("\n")
    return 0
main()
:
    time=0
    raw,col
    while(scanf("%d%d",&raw,&col)!=EOF)
    :
        # 输入行列后又回车了，所以回车也算一个字符……
        scanf("%*c")
        printf("raw:%d, col:%d\n", raw, col)
        if(raw==0&&col==0)
            exit(0)
        else
        :
            input(raw,col)
            printf("Field#%d\n",++time)
            mineNum(raw,col)
    return 0
```
------------------------------------------------------------------------------------------------
 sec
=======
------------------------------------------------------------------------------------------------
 176. Second Highest Salary
==============================
 Write a SQL query to get the second highest salary from the
 `Employee` 
 table.
```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
 For example, given the above Employee table, the query should return
 `200` 
 as the second highest salary. If there is no second highest salary, then the query should return
 `null` 
 .
```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```
```
# Write your MySQL query statement below
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
```
------------------------------------------------------------------------------------------------
 Segment Tree / Binary Indexed Tree
======================================
### 
 Description
 The structure of Segment Tree is a binary tree which each node has two attributes
 `start` 
 and
 `end` 
 denote an segment / interval.
 _start _and _end _are both integers, they should be assigned in following rules:
* The root's _start _and _end _is given by
 `build` 
 method.
* The left child of node A has
 `start=A.left, end=(A.left + A.right) / 2` 
 .
* The right child of node A has
 `start=(A.left + A.right) / 2 + 1, end=A.right` 
 .
* if
 ---start _equals to _end--- 
 , there will be no children for this node.
 Implement a
 `build` 
 method with a given array, so that we can create a corresponding segment tree with every node value represent the corresponding interval max value in the array, return the root of this segment tree.
 Build:
```
/**
 * Definition of SegmentTreeNode:
 * public class SegmentTreeNode :
 * public start, end, max
 * public SegmentTreeNode left, right
 * public SegmentTreeNode(start, end, max) :
 * this.start = start
 * this.end = end
 * this.max = max
 * this.left = this.right = null
 * 
 * 
 */
public class Solution :
    /**
 * @param A: a list of integer
 * @return: The root of Segment Tree
 */
    public SegmentTreeNode build(int[] A) :
        #  write your code here
        return buildHelper(0, A.length -1, A)
    public SegmentTreeNode buildHelper(start, end, int[] A ):
        if(start > end):
            return null
        if (start == end):
            return new SegmentTreeNode (start, end, A[start])
        SegmentTreeNode left = buildHelper(start, (start + end) / 2, A)
        SegmentTreeNode right = buildHelper((start + end) / 2 + 1, end, A)
        SegmentTreeNode ret = new SegmentTreeNode(start, end, Math.max(left.max, right.max))
        ret.left = left
        ret.right = right
        return ret
```
 Query:
```
/**
 * Definition of SegmentTreeNode:
 * public class SegmentTreeNode :
 * public start, end, max
 * public SegmentTreeNode left, right
 * public SegmentTreeNode(start, end, max) :
 * this.start = start
 * this.end = end
 * this.max = max
 * this.left = this.right = null
 * 
 * 
 */
public class Solution :
    /**
 * @param root: The root of segment tree.
 * @param start: start value.
 * @param end: end value.
 * @return: The maximum number in the interval [start, end]
 */
    public query(SegmentTreeNode root, start, end) :
        #  write your code here
        if (start <= root.start && root.end <= end ) :
            return root.max
        mid = (root.start  + root.end) /2
        ans = Integer.MIN_VALUE
        if (mid >= start):
            ans = Math.max(ans, query(root.left, start, end))
        if (mid + 1 <= end):
            ans = Math.max(ans, query(root.right, start, end))
        return ans
```
 Modify:
```
/**
 * Definition of SegmentTreeNode:
 * public class SegmentTreeNode :
 * public start, end, max
 * public SegmentTreeNode left, right
 * public SegmentTreeNode(start, end, max) :
 * this.start = start
 * this.end = end
 * this.max = max
 * this.left = this.right = null
 * 
 * 
 */
public class Solution :
    /**
 * @param root: The root of segment tree.
 * @param index: index.
 * @param value: value
 * @return: nothing
 */
    public void modify(SegmentTreeNode root, index, value) :
        #  write your code here
        if(root.start == root.end && root.end == index):
            root.max = value
            return
          #  can getting rid of the last one? unless the input is within the segment tree range
        mid = (root.start + root.end) / 2 
        if (index <= mid):
            modify(root.left, index, value)
            root.max = Math.max(root.left.max, root.right.max)
        else :
            modify(root.right, index, value)
            root.max = Math.max(root.left.max, root.right.max)
        return 
```
------------------------------------------------------------------------------------------------
 1.   Serialize and Deserialize Binary Tree
============================================
 Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
 Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
 For example, you may serialize the following tree
```
    1
   / \
  2   3
     / \
    4   5
```
 as
 `"[1,2,3,null,null,4,5]"` 
 , just the same as
 how LeetCode OJ serializes a binary tree
 . You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
 Note:
 Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
 Thoughts：
 Serialization/Deserialization: Choose an order traversal and implement it.
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Codec :
   #  preorder implementaion 
public:
    #  Encodes a tree to a single string.
    string serialize(TreeNode* root) :
        ostringstream os #  altervatively, stringstream os
        serialize(root, os)
        return os.str()
    void serialize(TreeNode * root, ostringstream & os):
        if(root):
            os<< root->val << ' ' #  altervatively, os<< root->val << ","
            serialize(root->left, os)
            serialize(root->right, os)
        else:
            os << "# " # stop token #  altervatively, stringstream os << "#,"
    #  Decodes your encoded data to tree.
    TreeNode* deserialize(string data) :
        istringstream in(data) 
        return deserialize(in)    
    TreeNode* deserialize(istringstream& in):
        string val
        in >> val                    #  if serialize data as "," separated, do: getline(in, val, ",")
        if(val == "#") return nullptr
        TreeNode * root = new TreeNode(stoi(val))
        # preorder traversal
        root-> left = deserialize(in)
        root-> right = deserialize(in)
        return root
#  Your Codec object will be instantiated and called as such:
#  Codec codec
#  codec.deserialize(codec.serialize(root))
```
 Credits:
 Special thanks to
 @Louis1992
 for adding this problem and creating all test cases. Special thanks to
 @StefanPochmann
 and
 zhang lei
 in
 水中的鱼
 for adding the solution for this problem!
------------------------------------------------------------------------------------------------
 1.   Sliding Window Maximum
=============================
 Given an arraynums, there is a sliding window of sizekwhich is moving from the very left of the array to the very right. You can only see theknumbers in the window. Each time the sliding window moves right by one position.
 For example,
 Givennums=
 `[1,3,-1,-3,5,3,6,7]` 
 , andk= 3.
```
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```
 Therefore, return the max sliding window as
 `[3,3,5,5,6,7]` 
 .
 Note:
 You may assumekis always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
 Follow up:
 Could you solve it in linear time?
 Thoughts:
1. O(nlogk): Maintain a max heap of k elements
2. O(n): Have a deque to keep track of current window maximum
 Code: Heap
```python
public class Solution :
    public int[] maxSlidingWindow(int[] A, k) :
        len = A.length
        int[] result = new int[len - k + 1]
        if(A.length == 0) return new int[0]
        Queue<Integer> queue = new PriorityQueue<Integer>((n1, n2) -> n2 - n1)
        i = 0
        for( i < k i ++) queue.add(A[i])
        result[i - k] = queue.peek()
        for( i < len i ++):
            queue.remove(A[i - k])
            queue.add(A[i])
            result[i - k + 1] = queue.peek()
        return result
```
 Code
```python
class Solution :
public:
    vector<int> maxSlidingWindow(vector<int>& A, k) :
        if(A.empty() || k <= 0) return A
        n = A.size()
        vector<int> windowMax 
        deque<int> dq
        for(i = 0 i < A.size() i ++):
            #  check in the range
            while(!dq.empty() && dq.front() < i - k  + 1):
                dq.pop_front()
            #  remove smaller numbers in k range as they are useless
            while(!dq.empty()&& A[dq.back()] < A[i]):
                dq.pop_back()
        dq.push_back(i)
        if(i >= k - 1): windowMax.push_back(A[dq.front()])
     return windowMax
```
 Python
```python
class Solution(object):
    def maxSlidingWindow(self, A, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(A):
            while d and A[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += A[d[0]],
        return out
```
 Special Thanks to
 flyingpenguin
 and
 jianchaolifighter
 for the
 reference
------------------------------------------------------------------------------------------------
 360. Sort Transformed Array
===============================
 Given a
 sorted
 array of integersnumsand integer valuesa,bandc. Apply a quadratic function of the form f(x) =ax2+bx+cto each elementxin the array.
 The returned array must be in
 sorted order
 .
 Expected time complexity:
 O(n)
 Example 1:
```
Input: 
A = 
[-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
```
 Example 2:
```
Input: 
A = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
```
 Thoughts:
1. Identify & utilize the convexity & concavity of the quadratic function based on a value
2. Use to pointers to select two candidate A[left] and A[right]
 Code O(n)
```python
class Solution(object):
    def sortTransformedArray(self, A, a, b, c):
        """
 :type A: List[int]
 :type a: int
 :type b: int
 :type c: int
 :rtype: List[int]
 """
        def qua(x, a, b, c):
            return a * x ** 2 + b * x  + c
        n = len(A)
        left , right = 0, n - 1
        ans = []
        while left<= right:
            left_val = qua(A[left], a ,b ,c)
            right_val = qua(A[right], a ,b ,c)
            if a >= 0: # a == 0: put larger at the end or smaller in the front both would be ok 
                if left_val <= right_val: # a > 0 find larger value garanteed larger than any number in the list put at the end
                    ans =[right_val]  + ans
                    right -= 1
                else:
                    ans = [left_val] + ans
                    left += 1
            else:
                if left_val <= right_val: # a > 0 find smaller value garanteed smaller than any number in the list put in the front
                    ans.append(left_val)
                    left += 1
                else:
                    ans.append(right_val)
                    right -= 1
        return ans
```
 Java
```python
class Solution :
    public int[] sortTransformedArray(int[] A, a, b, c) :
        if(A == null || A.length == 0) return null
        n = A.length
        i = 0, j = n - 1
        [] ans = new [n]
        k = (a >= 0) ?n - 1 : 0
        while(i <= j):
            left = qua(A[i], a, b, c)
            right = qua(A[j], a, b, c)
            if(a >= 0):
                #  current larger would be larger for the rest  
                ans[k--] = (left >= right)? qua(A[i++], a, b, c): qua(A[j--], a, b, c) #  a == 0 both conditions would apply
            else:
                #  current smaller would be smaller for the rest 
                ans[k++] = (left <= right)? qua(A[i++], a, b, c): qua(A[j--], a, b, c)
        return ans
    private qua (x, a, b, c):
        return a * x * x + b *x + c
```
------------------------------------------------------------------------------------------------
 Sort
========
------------------------------------------------------------------------------------------------
 311. Sparse Matrix Multiplication
=====================================
 Given two
 sparse matrices
 A
 and
 B
 , return the result of
 AB
 .
 You may assume that
 A
 's column number is equal to
 B
 's row number.
 Example:
```
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
```
 Thoughts:
1. Idea from
 a CMU lecture.
 : A sparse matrix can be represented as a sequence of rows, each of which is a sequence of (column-number, value) pairs of the nonzero values in the row.
2. Time Complexity Proposal: O(m*n + k*nB). Here k: number of non-empty elements in A. So in the worst case (dense matrix), it's O(m*n*nB)(from
 here
 )
 Code:
```python
class Solution :
    public int[][] multiply(int[][] A, int[][] B) :
        m = A.length, n = A[0].length, nB = B[0].length
        [][] res = new [m][nB]
        List[] rowA = new List[m]
        for(i = 0 i < m i++):
            List<Integer> colVal = new ArrayList<>()
            for (j = 0  j < n j ++):
                if(A[i][j]!= 0):
                  colVal.add(j)
                  colVal.add(A[i][j])
            rowA[i] = colVal
        for(i = 0 i < m i++):
            List<Integer> colVal = rowA[i]
            for(p = 0 p < colVal.size() p+=2):
                colA = colVal.get(p)
                valA = colVal.get(p + 1)
                for(j = 0 j < nB j++):
                    valB = B[colA][j]
                    res[i][j] += valA * valB
        return res
```
 Code: improvements: Definition of matrix multiplication: No extra space required
```python
class Solution :
    public int[][] multiply(int[][] A, int[][] B) :
        m = A.length, n = A[0].length, nB = B[0].length
        int[][] res = new int[m][nB]
        for(i = 0 i < m i++):
            for(k = 0 k < n k++):
                if(A[i][k] != 0):
                    for(j = 0 j < nB j++):
                            if(B[k][j] != 0)
                            res[i][j] += A[i][k] * B[k][j]
        return res
```
------------------------------------------------------------------------------------------------
 Stack
=========
------------------------------------------------------------------------------------------------
 String
==========
------------------------------------------------------------------------------------------------
 247. Strobogrammatic Number II
==================================
 A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
 Find all strobogrammatic numbers that are of length = n.
 Example:
```
Input: n = 2
Output: ["11","69","88","96"]
```
 Thoughts:
1. Recursion: T(n) = append each string with ("1", "1") ("6","9") ("9","6") ("8","8") if not at the out-most recursion also add ("0","0") from returned element from T(n - 2) Base case: (n =0 => [''] n = 1=>['0', '1', '8'])
2. Without Recursion: reverse the order with for loop
 Code: Recursion
```python
class Solution(object):
    def findStrobogrammatic(self, n):
        """
 :type n: int
 :rtype: List[str]
 """
        def helper(cur_len, total_len):
            # base case 
            if cur_len == 0: return ['']
            if cur_len == 1: return ['0', '1', '8']
            ans = []
            sub = helper(cur_len - 2, total_len)
            for s in sub:
                if cur_len != total_len:
                    ans.append("0" + s + "0")
                ans.append("1" + s + "1")
                ans.append("6" + s + "9")
                ans.append("8" + s + "8")
                ans.append("9" + s + "6")
            return ans
        return helper(n, n)
```
 Code: Without Recursion
```python
class Solution(object):
    def findStrobogrammatic(self, n):
        """
 :type n: int
 :rtype: List[str]
 """
        one , two = ['0','1', '8'] , [''] # two base case
        ans = one if n % 2 == 1 else two
        i = n % 2 + 2
        while(i <= n):
            new = []
            for s in ans:
                if i != n: 
                    new.append("0" + s + "0")
                new.append("1" + s + "1")
                new.append("6" + s + "9")
                new.append("8" + s + "8")
                new.append("9" + s + "6")
            ans = new
            i += 2
        return ans
```
------------------------------------------------------------------------------------------------
 246. Strobogrammatic Number
===============================
 A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
 Write a function to determine if a number is strobogrammatic. The number is represented as a string.
 Example 1:
```
Input: "69"
Output: true
```
 Example 2:
```
Input:  "88"
Output: true
```
 Example 3:
```
Input:  "962"
Output: false
```
```python
class Solution :
    #  ask if 00 is a valid strobogrammatic number! Here is true!
    public boolean isStrobogrammatic(String num) :
        for(i = 0, j = num.length() -1 i <= j i++, j--):
            if(!"00 11 696 88".contains(num.charAt(i) + "" + num.charAt(j)))
                return false
        return true
```
```python
class Solution(object):
    def isStrobogrammatic(self, num):
        """
 :type num: str
 :rtype: bool
 """
        s = set(['00', '11', '69', '96', '88'])
        i , j  = 0, len(num) - 1
        while(i <= j):
            if '::'.format(num[i], num[j]) not in s:
                print('::'.format(num[i], num[j]))
                return False
            i+=1
            j-=1
        return True
```
------------------------------------------------------------------------------------------------
 560. Subarray Sum Equals K
==============================
 Given an array of integers and an integer
 k
 , you need to find the total number of continuous subarrays whose sum equals to
 k
 .
 Example 1:
```
Input:
A = [1,1,1], k = 2
Output: 2
```
 Note:
1. The length of the array is in range [1, 20,000].
2. The range of numbers in the array is [-1000, 1000] and the range of the integer
 k
 is [-1e7, 1e7].
 Thoughts:
1. Sum = k -> use hash table (hash map)
2. Find subarray #: record preSum , # if occurence with that preSum val
3. Initialization: (0, 1)
 Code
```python
class Solution :
    public subarraySum(int[] A, k) :
        sum = 0, result = 0
        Map<Integer, Integer> preS = new HashMap<Integer, Integer>()
        preS.put(0,1)
        for(num: A):
            sum += num
            if(preS.containsKey(sum-k)):
                result += preS.get(sum - k) #  find how many preSum has value sum - k so that the right part sum is k.
            #  put prefix sum for the future
            preS.put(sum, preS.getOrDefault(sum,0) + 1)
       return result 
```
 Python
```python
class Solution(object):
    def subarraySum(self, A, k):
        """
 :type A: List[int]
 :type k: int
 :rtype: int
 """
        count = collections.Counter()
        count[0] = 1
        ans = preS = 0
        for num in A:
            preS += num
            ans += count[preS - k]
            count[preS] +=1
        return ans
```
------------------------------------------------------------------------------------------------
 Subarray
============
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 Substring Search
====================
 Generalization: substring search problem Template:
* 76. Mininum Window Substring
* 159. Longest Substring with At Most Two Distinct Characters
```python
class Solution :
public:
    T minWindow(string s, string t) :
        if(t.length() > s.length()) return ""
        unordered_map <char, int> map
        for(i = 0 i < t.length() i++ ):
            ++map[t[i]]
        left = 0, right = 0, head = INT_MAX, len = INT_MAX, count = map.size()
        while(right < s.length()):
            char rightChar = s[right]
            if(map.find(rightChar) != map.end()):
                if(--map[rightChar] == 0) count -- #  here condition statement and -- or ++ depending on cases 
            right ++
            while(count == 0):     #  here condition statement depends on cases
                #  do 
                #  increment
                char leftChar = s[left]
                if (map.find(leftChar)!= map.end()):
                    if(++map[leftChar] > 0):
                        count++
                left ++
        return T # <answer to return>
```
 Original Java Code from the
 LeetCode Forum harrychaoyanghe
```python
public class Solution :
    public List<Integer> slidingWindowTemplateByHarryChaoyangHe(String s, String t) :
        # init a collection or value to save the result according the question.
        List<Integer> result = new LinkedList<>()
        if(t.length()> s.length()) return result
        # create a hashmap to save the Characters of the target substring.
        # (K, V) = (Character, Frequence of the Characters)
        Map<Character, Integer> map = new HashMap<>()
        for(char c : t.toCharArray()):
            map.put(c, map.getOrDefault(c, 0) + 1)
        # maintain a counter to check whether match the target string.
        counter = map.size()# must be the map size, NOT the string size because the char may be duplicate.
        # Two Pointers: begin - left pointer of the window end - right pointer of the window
        begin = 0, end = 0
        # the length of the substring which match the target string.
        len = Integer.MAX_VALUE 
        # loop at the begining of the source string
        while(end < s.length()):
            char c = s.charAt(end)# get a character
            if( map.containsKey(c) ):
                map.put(c, map.get(c)-1)#  plus or minus one
                if(map.get(c) == 0) counter--# modify the counter according the requirement(different condition).
            end++
            # increase begin pointer to make it invalid/valid again
            while(counter == 0 /* counter condition. different question may have different condition */):
                char tempc = s.charAt(begin)# ***be careful here: choose the char at begin pointer, NOT the end pointer
                if(map.containsKey(tempc)):
                    map.put(tempc, map.get(tempc) + 1)# plus or minus one
                    if(map.get(tempc) > 0) counter++# modify the counter according the requirement(different condition).
                /* save / update(min/max) the result if find a target*/
                #  result collections or result value
                begin++
        return result
```
 C++ Template:
 https:# leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
 Longest Substring with At Most Two Distinct Characters, Longest Substring with At Most K Distinct Characters,
 Minimum Window Substring, Longest Substring Without Repeating Characters
```
findSubstring(string s):
        vector<int> map(128,0)
        counter #  check whether the substring is valid
        begin=0, end=0 # two pointers, one point to tail and one head
        d # the length of substring
        for() : /* initialize the hash map here */ 
        while(end<s.size()):
            if(map[s[end++]]-- ?):  /* modify counter here */ 
            while(/* counter condition */): 
                 /* update d here if finding minimum*/
                # increase begin to make it invalid/valid again
                if(map[s[begin++]]++ ?): /*modify counter here*/ 
            /* update d here if finding maximum*/
        return d
```
 Minimum Window Substring
```
string minWindow(string s, string t) :
        vector<int> map(128,0)
        for(auto c: t) map[c]++
        counter=t.size(), begin=0, end=0, d=INT_MAX, head=0
        while(end<s.size()):
            if(map[s[end++]]-->0) counter-- # in t
            while(counter==0): # valid
                if(end-begin<d)  d=end-(head=begin)
                if(map[s[begin++]]++==0) counter++  # make it invalid
        return d==INT_MAX? "":s.substr(head, d)
```
 Longest Substring with At Most Two Distinct Characters:
```
lengthOfLongestSubstringTwoDistinct(string s) :
        vector<int> map(128, 0)
        counter=0, begin=0, end=0, d=0 
        while(end<s.size()):
            if(map[s[end++]]++==0) counter++
            while(counter>2) if(map[s[begin++]]--==1) counter--
            d=max(d, end-begin)
        return d
```
 Longest Substring Without Repeating Characters
```
lengthOfLongestSubstring(string s) :
        vector<int> map(128,0)
        counter=0, begin=0, end=0, d=0 
        while(end<s.size()):
            if(map[s[end++]]++>0) counter++ 
            while(counter>0) if(map[s[begin++]]-->1) counter--
            d=max(d, end-begin) # while valid, update d
        return d
```
 Special thanks:
 LeetCode Discussion Forum
 for the reference!
------------------------------------------------------------------------------------------------
 129. Sum Root to Leaf Numbers
=================================
 Given a binary tree containing digits from
 `0-9` 
 only, each root-to-leaf path could represent a number.
 An example is the root-to-leaf path
 `1->2->3` 
 which represents the number
 `123` 
 .
 Find the total sum of all root-to-leaf numbers.
 Note:
 A leaf is a node with no children.
 Example:
```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```
 Example 2:
```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```
 Thoughts:
1. Recusively: Having a current sum as parameter add detect whether current node is leaf node, if it is adds the sum to the total sum
2. Iteratively: Using Stack
 Code: Recursively:
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    sum 
    public sumNumbers(TreeNode root) :
        sum = 0
        if(root != null) sumNumbers(root, 0)
        return sum
    private void sumNumbers(TreeNode root, cur):
        cur = cur * 10 + root.val
        #  leaf node
        if(root.left == null && root.right == null) :
            sum += cur
            return
        if(root.left != null) sumNumbers(root.left,cur)
        if(root.right != null) sumNumbers(root.right,cur)
```
 Code: Iteratively
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public sumNumbers(TreeNode root) :
        if (root == null) return 0
        Stack<TreeNode> s = new Stack<>()
        s.push(root) sum = 0
        while(!s.empty()):
            TreeNode cur = s.pop()
            if(cur.left == null && cur.right == null):
                sum += cur.val
                continue
            if(cur.left != null):
                cur.left.val += cur.val *10
                s.push(cur.left)
            if(cur.right != null):
                cur.right.val += cur.val* 10
                s.push(cur.right)
        return sum
```
------------------------------------------------------------------------------------------------
 Sum
=======
 Given a string, find the length of the longest substring T that contains at mostkdistinct characters.
 Example 1:
```
Input: 
s = "eceba", k = 2
Output: 
3
Explanation: 
T is "ece" which its length is 3.
```
 Example 2:
```
Input: s = "aa", k = 1
Output: 
2
Explanation: 
T is "aa" which its length is 2.
```
 Thoughts:
1. d: a hash table to record distinct value (through (len(d)).
2. every iteration compare (i - low + 1) with max value (returned value in the end)
	1. when d is over k, delete the least value entry, set low = min(d.values()) + 1
 Code:
```python
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
 :type s: str
 :type k: int
 :rtype: int
 """
        d, low, ans = :, 0, 0
        for i,c in enumerate(s) :
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ans = max(i - low + 1, ans)
        return ans
```
------------------------------------------------------------------------------------------------
 101. Symmetric Tree
=======================
 Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
 For example, this binary tree
 `[1,2,2,3,4,4,3]` 
 is symmetric:
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
 But the following
 `[1,2,2,null,3,null,3]` 
 is not:
```
    1
   / \
  2   2
   \   \
   3    3
```
 Note:
 Bonus points if you could solve it both recursively and iteratively.
 Thoughts:
1. Recursively: each call needs to check the current two nodes value and need to recursively call two pairs: (left.left, right.right) and (left.right, right.left).
2. Iteratively: Same logic Using stack, each time check the and push the corresponding pairs of child node into the stack
 Code: Recursive
```python
public boolean isSymmetric(TreeNode root) :
    return root==null || isSymmetricHelp(root.left, root.right)
private boolean isSymmetricHelp(TreeNode left, TreeNode right):
    if(left==null || right==null)
        return left==right
    if(left.val!=right.val)
        return false
    return isSymmetricHelp(left.left, right.right) && isSymmetricHelp(left.right, right.left)
```
 Code: Iterative
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 *     val
 *     TreeNode left
 *     TreeNode right
 *     TreeNode(x) : val = x 
 * 
 */
class Solution :
    public boolean isSymmetric(TreeNode root) :
        if(root == null) return true
        Stack<TreeNode> s = new Stack<TreeNode>()
        s.push(root.left)
        s.push(root.right) #  relative ordering in the pair does not matter
        TreeNode l, r
        while(!s.empty()):
            l = s.pop() r = s.pop()
            if(l == null && r == null) continue
            if(l == null || r == null || l.val != r.val) return false
            s.push(l.left) s.push(r.right) #  relative ordering in the pair does not matter
            s.push(l.right) s.push(r.left)
        return true
```
------------------------------------------------------------------------------------------------
 621. Task Scheduler
=======================
 621. Task Scheduler
=====================
 Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
 However, there is a non-negative cooling interval
 n
 that means between two
 same tasks
 , there must be at least n intervals that CPU are doing different tasks or just be idle.
 You need to return the
 least
 number of intervals the CPU will take to finish all the given tasks.
 Example 1:
```
Input:
 tasks = ["A","A","A","B","B","B"], n = 2
Output:
 8
Explanation:
 A ->B -> idle -> A -> B ->idle -> A ->B.
```
 Note:
1. The number of tasks is in the range [1, 10000].
2. The integer n is in the range [0, 100].
 FB Followup:
1. Output the order as original task
 Thoughts:
1. count most frequent task, say k.
2. create k chunks, then fill less frequent chars into the gaps into each chunk
3. compare the length of the task vs (number of chunks) * (least length of each chunk) + last chunks size = ( k -1 ) * (n + 1) + (# of most frequent chars)
 Code:
```python
class Solution :
public:
    leastInterval(vector<char>& tasks, n) :
        count [26]  fill_n(count, 26, 0) #  need to fill each time since OJ seems to re-use the same 
        #  allocated space for running multiple tests
        for(char task : tasks):
            count[task - 'A']++
        sort(begin(count),end(count))
        #  count how many most frequent chars
        i = 25
        while(i >= 0 && count[i] == count[25])
             i--
        tasks_len = tasks.size()
        return max(tasks_len, (count[25] - 1)*(n + 1) + 25 - i)
```
 Code: C+
```python
class Solution :
public:
    leastInterval(vector<char>& tasks, n) :
        vector<int> counter (26)
        max_val = 0
        maxCount = 0
        for (auto c : tasks):
            counter[c - 'A']++
            if(max_val == counter[c - 'A']) maxCount ++
            else if(max_val < counter[c - 'A']):
                max_val = counter[c- 'A']
                maxCount = 1
        partCount = max_val - 1
        partLen = n - (maxCount - 1) #  could be negative
        emptySlots = partCount * partLen
        residualTasks = tasks.size() - max_val * maxCount
        idles = max(0, emptySlots - residualTasks)
        return tasks.size() + idles 
```
------------------------------------------------------------------------------------------------
 Topological Sort
====================
 210. Course Schedule II
=========================
 There are a total ofncourses you have to take, labeled from
 `0` 
 to
 `n - 1` 
 .
 Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair:
 `[0,1]` 
 Given the total number of courses and a list of prerequisite
 pairs
 , return the ordering of courses you should take to finish all courses.
 There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
 For example:
```
2, [[1,0]]
```
 There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is
 `[0,1]` 
```
4, [[1,0],[2,0],[3,1],[3,2]]
```
 There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is
 `[0,1,2,3]` 
 . Another correct ordering is
 `[0,2,1,3]` 
 .
 Note:
1. The input prerequisites is a graph represented by
 a list of edges
 , not adjacency matrices. Read more about
 how a graph is represented
 .
2. You may assume that there are no duplicate edges in the input prerequisites.
 click to show more hints.
 Hints:
1. This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2. Topological Sort via DFS
	* A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via
 BFS
 .
------------------------------------------------------------------------------------------------
 Traversal
=============
 103. Binary Tree Zigzag Level Order Traversal
===============================================
------------------------------------------------------------------------------------------------
 Tree
========
------------------------------------------------------------------------------------------------
 Trie
========
------------------------------------------------------------------------------------------------
 Twin String
===============
 Twin Strings
===============
 Given an array of lower case strings, the task is to find the number of strings that are distinct. Two strings are distinct if on applying the following operations on one string the second string cannot be formed.
* A character on odd index can be swapped with another character at odd index only.
* A character on even index can be swapped with another character on even index only.
 Examples:
```
Input  : arr[] = :"abcd", "cbad", "bacd"
Output : 2
The 2nd string can be converted to the 1st by swapping 
the first and third characters. So there are 2 distinct 
strings as the third string cannot be converted to the 
first.
Input  : arr[] = :"abc", "cba"
Output : 1
```
 Thoughts
 Use two maps/dictionaries (int[# of alphabets (assume string only consists of alphabet literals only)]), one for the even index char and one for the odd index char. Encode the string such that it contains all the key-value pair from odd and even maps/dictionaries. Use set (C++: unordered_set <string> , Java: Hashset<String>) to hash distinct twin strings.
 Code
```
#  C++ program to count distinct strings with even odd swapping
#  allowed.
#include<bits/stdc++.h>
using namespace std
const MAX_CHAR = 26
#  Returns encoding of string that can be used for hashing.
#  The idea is to return same encoding for strings which 
#  can become same after swapping a even positioned character
#  with other even characters OR swapping an odd character
#  with other odd characters.
string encodeString(string str)
:
    #  hashEven stores the count of even indexed character
    #  for each string hashOdd stores the count of odd
    #  indexed characters for each string
    hashEven[MAX_CHAR] = :0
    hashOdd[MAX_CHAR] = :0
    #  creating hash for each string
    for (i=0 i<str.length() i++)
    :
        char c = str[i]
        if (i&1) #  If index of current character is odd
           hashOdd[c-'a']++
        else
           hashEven[c-'a']++
    #  For every character from 'a' to 'z', we store its
    #  count at even position followed by a separator,
    #  followed by count at odd position.
    string encoding = ""
    for (i=0 i<MAX_CHAR i++)
    :
       encoding += to_string(hashEven[i])
       encoding += to_string('-')
       encoding += to_string(hashOdd[i])
       encoding += to_string('-')
    return encoding
#  This function basically uses a hashing based set to
#  store strings which are distinct according to accoding
#  to criteria given in question.
countDistinct(string input[], n)
:
    countDist = 0  #  Initialize result
    #  Create an empty set and store all distinct
    #  strings in it.
    unordered_set<string> s
    for (i=0 i<n i++)
    :
       #  If this encoding appears first time, increment
       #  count of distinct encodings.
       if (s.find(encodeString(input[i])) == s.end())
       :
           s.insert(encodeString(input[i]))
           countDist++
    return countDist
#  Driver code
main()
:
    string input[] = :"abcd", "acbd", "adcb", "cdba",
                      "bcda", "badc"
    n = sizeof(input)/sizeof(input[0])
    cout << countDistinct(input, n)
    return 0
```
 Special Thanks for GeeksforGeeks'
 detailed explanation
 of this problem.
------------------------------------------------------------------------------------------------
 Twitter
===========
------------------------------------------------------------------------------------------------
 170. Two Sum III - Data structure design
============================================
 Design and implement a TwoSum class. It should support the following operations:
 `add` 
 and
 `find` 
 .
`add` 
 - Add the number to an internal data structure.
`find` 
 - Find if there exists any pair of numbers which sum is equal to the value.
 Example 1:
```
add(1) add(3) add(5)
find(4) ->true
find(7) ->false
```
 Example 2:
```
add(3) add(1) add(2)
find(3) -> true
find(6) -> false
```
 Thoughts:
1. Find vs Add trade off
2. Find-favored algorithms
3. Add- favored algorithms
 Code:
 algorithms that are Find-favored algorithms (
 TLE
 )
```python
public class TwoSum :
        Set<Integer> sum
        Set<Integer> num
        TwoSum():
            sum = new HashSet<Integer>()
            num = new HashSet<Integer>()
        #  Add the number to an internal data structure.
        public void add(number) :
            if(num.contains(number)):
                sum.add(number * 2)
            else:
                Iterator<Integer> iter = num.iterator()
                while(iter.hasNext()):
                    sum.add(iter.next() + number)
                num.add(number)
        #  Find if there exists any pair of numbers which sum is equal to the value.
        public boolean find(value) :
            return sum.contains(value)
```
 Code: algorithms that are Add-favored algorithms (Add: O(1), Find: (O(n))
```python
class TwoSum :
    Map<Integer, Integer> map
    /** Initialize your data structure here. */
    public TwoSum() :
        map = new HashMap<>()
    /** Add the number to an internal data structure.. */
    public void add(number) :
        if(map.containsKey(number)):
            map.put(number, 2)
        else:
            map.put(number, 1)
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    public boolean find(value) :
            Iterator<Integer> iter = map.keySet().iterator()
            while(iter.hasNext()):
                n1 = iter.next()
                n2 = value - n1
                if (map.containsKey(n2) &&(map.get(n2) == 2 || n1!=n2)):
                    return true
            return false
/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum()
 * obj.add(number)
 * boolean param_2 = obj.find(value)
 */
```
------------------------------------------------------------------------------------------------
 1. Two Sum
==============
 1. Two Sum
============
 Given an array of integers, return
 indices
 of the two numbers such that they add up to a specific target.
 You may assume that each input would have
 exactly
 one solution, and you may not use thesameelement twice.
 Example:
```
Given A = [2, 7, 11, 15], target = 9,
Because A[0] + A[1] = 2 + 7 = 9,
return [0, 1].
```
 Thoughts:
 map key-value pair of component of the sum
```python
class Solution :
public:
    vector<int> twoSum(vector<int>& A, target) :
        unordered_map <int, int> map
        vector <int> ans 
        for (i = 0 i< A.size() i++):
            res = target - A[i]
            if (map.find(res) != map.end()):
                ans.push_back(map[res])
                ans.push_back(i)
                return ans
            map[A[i]] = i
        return ans
```
 Alternatively, I can first sort the vector _nums _and use
 two pointer
 (but the time complexity becomes sort dominant O(nlogn))
------------------------------------------------------------------------------------------------
 Union-Find
==============
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 242. Valid Anagram
======================
 Given two strings
 ---s_and_t--- 
 , write a function to determine if
 ---t_is an anagram of_s--- 
 .
 Example 1:
```
Input:
s = "anagram", 
t = "nagaram"
Output: true
```
 Example 2:
```
Input:
s = "rat", 
t = "car"
Output: false
```
 Note:
 You may assume the string contains only lowercase alphabets.
 Follow up:
 What if the inputs contain unicode characters? How would you adapt your solution to such case?
 Thoughts:
1. Give compare the canical sorted form
2. Compare the char count in the map
3. Follow-up: Method 1 would still work
 Code: Sort
```python
class Solution(object):
    def isAnagram(self, s, t):
        """
 :type s: str
 :type t: str
 :rtype: bool
 """
        return sorted(s) == sorted(t)
```
 Code: Counting Map (elements in s and t needs to be hashable)
```python
class Solution(object):
    def isAnagram(self, s, t):
        """
 :type s: str
 :type t: str
 :rtype: bool
 """
        d = collections.defaultdict(int)
        for c in s: d[c]+= 1
        for c in t: d[c]-= 1
        return all(d[v] == 0 for v in d)
```
------------------------------------------------------------------------------------------------
 678. Valid Parenthesis String
=================================
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
1. Any left parenthesis
 `'('` 
 must have a corresponding right parenthesis
 `')'` 
 .
2. Any right parenthesis
 `')'` 
 must have a corresponding left parenthesis
 `'('` 
 .
3. Left parenthesis
 `'('` 
 must go before the corresponding right parenthesis
 `')'` 
 .
4. `'*'` 
 could be treated as a single right parenthesis
 `')'` 
 or a single left parenthesis
 `'('` 
 or an empty string.
5. An empty string is also valid.
 Example 1:
```
Input: "()"
Output: True
```
 Example 2:
```
Input: "(*)"
Output: True
```
 Example 3:
```
Input: "(*))"
Output: True
```
 Thoughts:
1. DP
2. "two counter": min_op_left: how many open "(" if regarding all * to be ")" max_op_left: how many open "(" if regarding all * to be "("
	1. key idea: max_op_left should always be >= 0 in order to be considered legal, otherwise it will have unbalanced ")" and the parenthesis will never be balanced by further appending any char after it.
 Code: unordered DP with memoization Time: O(n^3) Space: O(n^2), Top-Down
```python
class Solution :
public:
    bool checkValidString(string s) :
        n = s.length()
        f = vector<vector<int>> (n, vector<int>(n, -1))
        return isValid(s, 0, n - 1)
private:
    vector<vector<int>> f
#  method checking substring s[start,...end] is valid
    bool isValid(const string &s, start, end):
        if(start > end) return true
        if(start == end) return f[start][end] = (s[start] == '*')
        if(f[start][end]>= 0) return f[start][end] #  is already memorized
        if((s[start] == '(' || s[start] == '*') 
           && (s[end] == ')'|| s[end] == '*') 
           && isValid(s, start + 1, end - 1))
            return f[start][end] = 1
        for(i = start i < end i++):
            if(isValid(s, start, i) && isValid(s, i + 1, end)) 
                return f[start][end] = 1
        return f[start][end] = 0
```
 Code: Ordered DP with memoization Time: O(n^3) Space: O(n^2), Bottom Up
```python
class Solution :
public:
    bool checkValidString(const string& s) :
        l = s.length()
        if (l == 0) return true
        vector<vector<int>> dp(l, vector<int>(l, 0))
        for (i = 0 i < l ++i)
            if (s[i] == '*') dp[i][i] = 1
        for (len = 2 len <= l ++len)
            for (i = 0 i <= l - len ++i) :
                j = i + len - 1
                #  (...), *...), (...*, *...*
                if ((s[i] == '(' || s[i] == '*')
                  &&(s[j] == ')' || s[j] == '*'))
                    if (len == 2 || dp[i + 1][j - 1]) :
                        dp[i][j] = 1
                        continue                    
                for (k = i k < j ++k)
                    if (dp[i][k] && dp[k + 1][j]) :
                        dp[i][j] = 1
                        break
        return dp[0][l - 1]
```
 Code Counting Time: O(n), Space: O(1)
```python
class Solution :
public:
    bool checkValidString(string s) :
        max_open_left = 0, min_open_left = 0
        for(char c: s):
            if(c == '(') min_open_left++ else min_open_left--
            if(c != ')') max_open_left++ else max_open_left--
            if(max_open_left < 0) return false
            min_open_left = max(0, min_open_left) #  we cannot use previous "*" to fullfill later '(": reset the min_open_left
        return min_open_left == 0
```
```python
class Solution :
public:
    bool checkValidString(string s) :
        max_open_left = 0, min_open_left = 0
        for(char c: s):
            if(c == '(') min_open_left++ else if(min_open_left > 0) min_open_left--
            if(c != ')') max_open_left++ 
            else if (max_open_left == 0) return false 
            else max_open_left--
        return min_open_left == 0
```
 Python
```python
class Solution(object):
    def checkValidString(self, s):
        """
 :type s: str
 :rtype: bool
 """
        max_open, min_open = 0, 0
        for c in s:
            # if c == '(': min_open += 1 
            # else: min_open -=1
            min_open = min_open + 1 if c == '(' else min_open - 1
            max_open = max_open + 1 if c != ')' else max_open - 1
            if max_open < 0: return False
            min_open = max(0, min_open)
        return min_open == 0
```
 Special Thanks to
 Huahua's blog
------------------------------------------------------------------------------------------------
 98. Validate Binary Search Tree
===================================
 98. Validate Binary Search Tree
=================================
 Given a binary tree, determine if it is a valid binary search tree (BST).
 Assume a BST is defined as follows:
* The left subtree of a node contains only nodes with keys
 less than
 the node's key.
* The right subtree of a node contains only nodes with keys
 greater than
 the node's key.
* Both the left and right subtrees must also be binary search trees.
 Example 1:
```
Input:
    2
   / \
  1   3
Output:
 true
```
 Example 2:
```
    5
   / \
  1   4
     / \
    3   6
Output:
 false
Explanation:
 The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
```
 Thoughts:
1. Inorder traversal + checking ascending property in serialized array
2. Improving 1 by only recording the prev node
3. Iteratively defining the left and right bound of the node
4. Iterative Traversal (Generic to solve other problems such as Binary Tree Inorder Traversal, Kth Smallest in BST and Validate BST
 Code 2:
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    bool isValidBST(TreeNode* root) :
        TreeNode * prev = NULL
        return isValidBST(root, prev)
private:
    bool isValidBST(TreeNode * root, TreeNode* & prev): #  !!important to add "&" since the prev will be changed
    #  as traversing down the BST 
        if(root == NULL) return true
        if(!isValidBST(root->left, prev)) return false
        if(prev != NULL && prev ->val >= root-> val) return false
        prev = root
        return isValidBST(root->right, prev)
```
 Code 3:
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public boolean isValidBST(TreeNode root) :
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE)
    public boolean isValidBST(TreeNode root, long min, long max):
        if(root == null) return true
        if(root.val >= max || root.val <= min) return false
        return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max)
```
 Code 4:
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    public boolean isValidBST(TreeNode root) :
        if(root == null) return true 
        Stack<TreeNode> stack = new Stack<>()
        TreeNode pre = null
        while (root != null || !stack.isEmpty()):
            #  left 
            while(root != null):
                stack.push(root)
                root = root.left
            root = stack.pop()
            #  do
            if (pre!= null && pre.val >= root.val) return false
            #  record predecessor
            pre = root
            #  right
            root = root.right
        return true
```
 Kth Smallest Element in a BST
```
 public kthSmallest(TreeNode root, k) :
     Stack<TreeNode> stack = new Stack<>()
     while(root != null || !stack.isEmpty()) :
         while(root != null) :
             stack.push(root)    
             root = root.left   
         root = stack.pop()
         if(--k == 0) break
         root = root.right
     return root.val
```
 Binary Tree Inorder Traversal
```python
public List<Integer> inorderTraversal(TreeNode root) :
    List<Integer> list = new ArrayList<>()
    if(root == null) return list
    Stack<TreeNode> stack = new Stack<>()
    while(root != null || !stack.empty()):
        while(root != null):
            stack.push(root)
            root = root.left
        root = stack.pop()
        list.add(root.val)
        root = root.right
    return list
```
------------------------------------------------------------------------------------------------
 255. Verify Preorder Sequence in Binary Search Tree
=======================================================
 255. Verify Preorder Sequence in Binary Search Tree
=====================================================
 Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
 You may assume each number in the sequence is unique.
 Follow up:
 Could you do it using only
 constant space complexity
 ?
 Thoughts
1. keep track of prev val in order to compare whether there is a new right branch
2. keep track of lower bound value of parent node for branching to the right
 Code: space complexity of O(n)
```python
class Solution :
public:
    bool verifyPreorder(vector<int>& preorder) :
        low = INT_MIN
        stack<int> nodes
        for(auto p : preorder):
            if(p < low) return false
            while(!nodes.empty() && p > nodes.top()):
                #  find the new lower bound 
                low = nodes.top() nodes.pop()
            #  new reference
            nodes.push(p)
        return true
```
 Code: space complexity of O(n) Python
```python
class Solution(object):
    def verifyPreorder(self, preorder):
        """
 :type preorder: List[int]
 :rtype: bool
 """
        stack = []
        low = float('-inf')
        for val in preorder:
            if val < low:
                return False
            while stack and val > stack[-1]:
                low = stack.pop()
            stack.append(val)
        return True
```
 Code: Use two stack (Java)
```python
class Solution :
    public boolean verifyPreorder(int[] preorder) :
        Stack<Integer> stack = new Stack<>()
        Stack<Integer> inOrder = new Stack<>() 
        for(val : preorder):
            if(!inOrder.isEmpty() && val < inOrder.peek()) return false
            while(!stack.isEmpty() && val > stack.peek()):
                #  new traced parent node
                inOrder.push(stack.pop())
            stack.push(val)
        return true
```
 Code: space complexity of O(1): MUST USE POINTER!
```python
class Solution :
public:
    bool verifyPreorder(vector<int>& preorder) :
        low = INT_MIN, branch_i = -1
        for(auto val : preorder):
            if(val < low) return false
            #  trace back to the parent node on which cur node based to the right
            while(branch_i >= 0 && val > preorder[branch_i]):
                low = preorder[branch_i--]
            #  update new branch compare value 
            preorder[++branch_i] = val
        return true
```
 Special Thanks
 stefanpochmann
 for the
 reference
------------------------------------------------------------------------------------------------
 286. Walls and Gates
========================
 You are given a m x n 2D grid initialized with these three possible values.
1. `-1` 
 - A wall or an obstacle.
2. `0` 
 - A gate.
3. `INF` 
 - Infinity means an empty room. We use the value
 `2^31- 1 = 2147483647` 
 to represent
 `INF` 
 as you may assume that the distance to a gate is less than
 `2147483647` 
 .
 Fill each empty room with the distance to itsnearestgate. If it is impossible to reach a gate, it should be filled with
 `INF` 
 .
 Example:
 Given the 2D grid:
```
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
```
 After running your function, the 2D grid should be:
```
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```
 Thoughts:
1. BFS and fill the empty rooms with current distance
 Code: T: O(mn) S:O(mn)
```python
class Solution :
    public void wallsAndGates(int[][] rooms) :
        if(rooms.length == 0|| rooms[0].length == 0) return
        Queue<int[]> queue = new LinkedList()
        [] d = :0,1,0,-1,0
        for(i = 0 i < rooms.length i++):
            for(j =0 j< rooms[0].length j++):
                if(rooms[i][j] == 0) queue.offer(new int[]:i,j)
        while(!queue.isEmpty()):
            [] pos  = queue.poll()
            row = pos[0], col = pos[1]
            for(i = 0 i < 4 i++):
                x = row + d[i]
                y = col + d[i+1]
                if(x >= 0 && x < rooms.length && y>=0 && y< rooms[0].length && rooms[x][y] == Integer.MAX_VALUE):
                    rooms[x][y] = rooms[row][col] + 1
                    queue.offer(new int[]:x,y)
```
------------------------------------------------------------------------------------------------
 Wildcard Matching
=====================
 Wildcard Matching
===================
 Implement wildcard pattern matching with support for
 `'?'` 
 and
 `'*'` 
 .
```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
The function prototype should be:
matchedIdx(const char *s, const char *p)
Some examples:
matchedIdx("aa","a") → 0
matchedIdx("juliadntdas","a*nt") → 4
```
 Thoughts:
1. Similar to LeetCode:
 44. Wildcard Matching
 ,
 Wildcard Pattern Matching
 @ GeeksforGeeks and
 String Matching with Wildcards @ Hackerrank
 problem except here it is required to output the index of the first occurrence.
2. Code
```
 bool isMatch(const char *s, const char *p) :
        const char* star=NULL
        const char* ss=s
        while (*s):
            # advancing both pointers when (both characters match) or ('?' found in pattern)
            # note that *p will not advance beyond its length 
            if ((*p=='?')||(*p==*s)):s++p++continue 
            #  * found in pattern, track index of *, only advancing pattern pointer 
            if (*p=='*'):star=p++ ss=scontinue 
            # current characters didn't match, last pattern pointer was *, current pattern pointer is not *
            # only advancing pattern pointer
            if (star): p = star+1 s=++sscontinue 
           # current pattern pointer is not star, last patter pointer was not *
           # characters do not match
            return false
       # check for remaining characters in pattern
        while (*p=='*'):p++
        return !*p  
```
------------------------------------------------------------------------------------------------
 Page not found
 Sorry, but the page you were looking for could not be found.
 Return to content
------------------------------------------------------------------------------------------------
 140. Word Break II
======================
 140. Word Break II
====================
 Given a
 non-empty
 strings and a dictionary
 ---wordDict
 containing a list of
 non-empty
 words, add spaces in--- 
 s
 to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.
 Return all such possible sentences.
 For example, given
 s=
 `"catsanddog"` 
 ,
 dict=
 `["cat", "cats", "and", "sand", "dog"]` 
 .
 A solution is
 `["cats and dog", "cat sand dog"]` 
 .
 UPDATE (2017/1/4):
 The
 wordDict
 parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
 Thoughts:
1. DP + Backtracking! but (TLE)
2. DFS
 Code : my TLE solution based on
 139
```python
class Solution :  
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) :
       n = s.length()
       if(n == 0) return vector<string>() 
       unordered_map<int, vector<string>> m
       m[0] = vector<string>(1,"")
        for(i = 1 i <= n i++):
           for(j = 0 j < i j++):
               string new2check = s.substr(j, i - j)
               if(m.find(j)!= m.end()&& find(wordDict.begin(), wordDict.end(), new2check)!=wordDict.end()):
                   auto tmp = m[j]
                   for(auto & str: tmp):
                       if(str == "") str+= new2check
                       else str+=" " + new2check
                   m[i].insert(m[i].end(),tmp.begin(),tmp.end())
        return m[n]
```
 Code: DFS + map table, TC:O(n^2) for worse , O(n) for best , SC:O(n^2) for worse, O(1) for best (k: num of words in the dictionary)
```python
class Solution :
    unordered_map <string, vector<string>> m
    vector<string> combine(string w, vector<string> prev):
        for(auto & str: prev):
            str += " " + w
        return prev
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) :
        if(m.find(s)!=m.end())return m[s]
        vector<string>ans
        # whole word
        if(find(wordDict.begin(),wordDict.end(),s)!=wordDict.end()) ans.push_back(s) #  or (wordDcict.count(s))
        # break up: i starts from 1
        for(i = 1 i < s.size() i++):
            string w = s.substr(i)
            if(find(wordDict.begin(),wordDict.end(),w)!=wordDict.end()) : #  or (wordDcict.count(w))
                string rest = s.substr(0,i)
                vector<string> prev_ans = combine(w, wordBreak(rest, wordDict))
                ans.insert(ans.end(), prev_ans.begin(), prev_ans.end())
        m[s] = ans
        return ans
```
 Code (Java) TC: O(k^2) for worse, O(n) for best, SC:O(k^2) for worse, O(1) for best (k: num of words in the dictionary)
```python
class Solution :
    public List<String> wordBreak(String s, List<String> wordDict) :
        return DFS(s, wordDict, new HashMap<String, List<String>>())
    List <String> DFS (String s, List<String> wordDict, Map<String, List<String>> map):
        if(map.containsKey(s)) return map.get(s)
        List<String> ans = new LinkedList<String>()
        if(s.length() == 0) :
            ans.add("")
            return ans
        for(String word: wordDict):
            if(s.startsWith(word)):
                List<String> restList = DFS(s.substring(word.length()), wordDict, map)
                #  System.out.println(restList.size())
               for(String rest: restList):
                   ans.add(word + (rest.isEmpty()?"": " ") + rest)
        map.put(s,ans)
        return ans
```
------------------------------------------------------------------------------------------------
 139. Word Break
===================
 139. Word Break
=================
 Given a
 non-empty
 stringsand a dictionarywordDictcontaining a list of
 non-empty
 words, determine ifscan be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
 For example, given
 s=
 `"leetcode"` 
 ,
 dict=
 `["leet", "code"]` 
 .
 Return true because
 `"leetcode"` 
 can be segmented as
 `"leet code"` 
 .
 UPDATE (2017/1/4):
 The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
 Thoughts:
1. f[i]: weather a there is a valid sequence ends at i.
2. f[i] is true only when there is a j from 0 to i -1 such that f[j] and dictionary contains (s.substr (j, i - j))
 Code: Time: O(n^2) (or O(n^3) depending on "contains" implementation) Space: O(n)
```python
class Solution :
public:
    bool wordBreak(string s, vector<string>& wordDict) :
        n = s.size()
        bool f [n + 1] fill_n(f, n + 1, false)
        #  initialize a vector: vector<bool> f (n + 1, false)
        f[0] = true
        for(i = 1 i <= n  i++):
            for(j = 0  j < i j++):
                string pre_word = s.substr(j, i - j)
                if(f[j] && find(wordDict.begin(), wordDict.end(),pre_word)!= wordDict.end()):
                    f[i] = true
                    break #  speed up
        return f[n]
```
------------------------------------------------------------------------------------------------
 126. Word Ladder II
=======================
 Given two words (
 ---beginWord_and_endWord--- 
 ), and a dictionary's word list, find all shortest transformation sequence(s) from
 ---beginWord_to_endWord--- 
 , such that:
1. Only one letter can be changed at a time
2. Each transformed word must exist in the word list. Note that _beginWord _is _not _a transformed word.
 Note:
* Return an empty list if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume _beginWord _and _endWord _are non-empty and are not the same.
 Example 1:
```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```
 Example 2:
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```
 Thoughts:
1. "Naive" Solution: Create a dictionary that maps <str word, List[List[str]]]> Solution lists. Initialize the layer[beginword] word as [[beginword]].
	1. Expanding the layer list as follows:
		1. Having a childLayer which maps the layer for the next step
		2. while current layer is not empty
			1. for each w in layers keys:
			2. if w is in the EndWord: res list record the results by taking all the elements of layer[w]
			3. else for every position, flop the word w as neww. check if neww is in the wordList: add neww after every path in layer[w], add this result into childLayer[neww]
			4. set layer to newLayer for the next iteration
			5. remvoe all the keys from wordList that is in newlayers
2. BFS + DFS:
	1. Shortest transformation: BFS to find the shortest path between start and end
	2. Find all the transformation: DFS with backtracking to find all the answer
 Code: T:O(L^3*l) ? (L as wordList length, l as word length). S:O(L^3*l)?
```python
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
 :type beginWord: str
 :type endWord: str
 :type wordList: List[str]
 :rtype: List[List[str]]
 """
        wordList = set(wordList)
        res,layer = [], :
        layer[beginWord] = [[beginWord]]
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res += [k for k in layer[w]]
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+= [j + [neww] for j in layer[w]]
            wordList -= set(newlayer.keys()) # for avoiding unsupported operation between sets and list
            layer = newlayer
        return res
```
 Code: BFS + DFS
```python
class Solution :
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) :
        HashSet<String> dict = new HashSet<>(wordList)
        List<List<String>> res = new ArrayList<>()
        Map<String, Integer> distance = new HashMap<>()
        Map<String, ArrayList<String>> neighbors = new HashMap<>()
        ArrayList<String> solution = new ArrayList<>()
        dict.add(beginWord)
        bfs(beginWord, endWord, dict, distance, neighbors)
        dfs(beginWord, endWord, dict, distance, neighbors, solution, res)
        return res
   private void bfs(String start, String end, Set<String> dict, Map<String, Integer> distance, Map<String, ArrayList<String>> nodeNeighbors) :
  for (String str : dict)
      nodeNeighbors.put(str, new ArrayList<String>())
  Queue<String> queue = new LinkedList<String>()
  queue.offer(start)
  distance.put(start, 0)
  while (!queue.isEmpty()) :
      count = queue.size()
      boolean foundEnd = false
      for (i = 0 i < count i++) :
          String cur = queue.poll()
          curDistance = distance.get(cur)                
          List<String> neighbors = getNeighbors(cur, dict)
          for (String neighbor : neighbors) :
              #  System.out.println(cur)
              nodeNeighbors.get(cur).add(neighbor)
              if (!distance.containsKey(neighbor)) :#  Check if visited
                  distance.put(neighbor, curDistance + 1)
                  if (end.equals(neighbor))#  Found the shortest path
                      foundEnd = true
                  else
                      queue.offer(neighbor)
          if (foundEnd)
              break
    private void dfs(String cur, String end, Set<String>dict , Map<String, Integer> distance, Map<String, ArrayList<String>> neighbors, List<String> solution, List<List<String>> res):
           solution.add(cur)
        #  found end: add
        if(end.equals(cur)) res.add(new ArrayList<String> (solution))
        #  not found yet: recursively calling dfs
        else:
            for(String next: neighbors.get(cur)):
                if(distance.get(next) == distance.get(cur) + 1)
                    dfs(next, end, dict, distance, neighbors, solution, res)
        solution.remove(solution.size() - 1)
    private List<String> getNeighbors(String node, Set<String> dict):
        List<String> res = new ArrayList<>()
        char chs []  = node.toCharArray()
        for(char ch = 'a' ch <= 'z' ch++):
            for(i = 0  i < chs.length i++):
                char old = chs[i]
                chs[i] = ch
                if(dict.contains(String.valueOf(chs))):
                    res.add(String.valueOf(chs))
                chs[i] = old
        return res
```
------------------------------------------------------------------------------------------------
 127. Word Ladder
====================
 Given two words (
 ---beginWord_and_endWord--- 
 ), and a dictionary's word list, find the length of shortest transformation sequence from
 ---beginWord_to_endWord--- 
 , such that:
1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that
 beginWord
 is
 not
 a transformed word.
 Note:
* Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume
 ---beginWord and endWord--- 
 are non-empty and are not the same.
 Example 1:
```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" ->"hot" -> "dot" -> "dog" -> "cog",return its length 5.
```
 Example 2:
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```
 Thoughts:
1. BFS: Generate the qualified permutation, add distance by 1, until find the answer or queue is empty
2. Optimizations:
	1. Python
	 :
		1. 1. Character flopping: flop (expanding the transformation candidate in the "front" set, then check whether it is in the word dictionary: T: O(M*26*L*L) O(L) . M: Dictionary Size, L: word length,
		2. 1. Dictionary Checking: Checking whether a word in current wordDictionary can be transformed into current word in the set: T:O(MNL). N: number of words in the dictionary.
		3. Removing entries in S from T vs Creating new entries from S if it is not in T.
	2. C++
 Code
```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
 :type beginWord: str
 :type endWord: str
 :type wordList: List[str]
 :rtype: int
 """
        def generateNeighbors(word, wordList):
            for i in range(len(word)):
                for letter in string.ascii_lowercase:
                    candidate = word[:i] + letter + word[i+1:]
                    if candidate in wordList:
                        yield candidate
        # We use q to keep track of the next nodes to process in the BFS.
        # Each item in the queue is a list with two items:
        # item[0] = word
        # item[1] = steps to reach word + 1 (i.e. number of nodes in list of nodes 
        # traversed to reach word - (format of Word Ladder I output)).
        q = collections.deque([ [beginWord,1] ])
        # We keep track of words we've processed to avoid getting stuck in a loop.
        seen = set([beginWord])
        # wordList is given as a list but we want O(1) lookup so we convert to a set.
        wordList = set(wordList)
        while q:
            q_item = q.popleft()
            for candidate in generateNeighbors(q_item[0], wordList):
                if candidate == endWord:
                    return q_item[1] + 1
                elif candidate in seen:
                    continue
                seen.add(candidate)
                q.append([candidate, q_item[1] + 1])
        return 0
```
```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
 :type beginWord: str
 :type endWord: str
 :type wordList: List[str]
 :rtype: int
 """
        dist = 2
        n = len(beginWord)
        wordDict = set(wordList)
        wordDict.discard(beginWord)
        # corner case: since we assume endWord is in wordDict when doing the swapping
        if endWord not in wordDict:
            return 0
        front, back = set([beginWord]), set([endWord])
        while front:
            # generate all valid permutations
            front = wordDict & set([word[:i] + c + word[i+1:]
                                    for word in front 
                                    for i in range(len(word))
                                    for c in string.ascii_lowercase
                                   ])
            if front & back:
                # there are common elements in front and back, done
                return dist
            dist += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front 
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
        return 0
```
 Code: Python Optimization
```python
class Solution:
    # @param :string beginWord
    # @param :string endWord
    # @param :set<string> wordDict
    # @return :integer
    def ladderLength(self, beginWord, endWord, wordDict):
        def generateNextSet1(current, wordDict, wordLen):
            nextSet = set()
            for word in current:
                for index in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:index] + ch + word[index+1:]
                        if nextWord in wordDict:
                            nextSet.add(nextWord)
            return nextSet
        def generateNextSet2(current, wordDict):
            nextSet = set()
            for word in current:
                for nextWord in wordDict:
                    index = 0
                    try:
                        while word[index] == nextWord[index]:
                            index += 1
                        if word[index+1:] == nextWord[index+1:]:
                            nextSet.add(nextWord)
                    except:
                        continue
            return nextSet
        steps, wordLen = 2, len(beginWord)
        front, back = set([beginWord]), set([endWord])
        wordDict.discard(beginWord)
        switchThreshold = 26*wordLen
        while front:
            # get all valid transformations
            if len(wordDict) >= switchThreshold:
                front = generateNextSet1(front, wordDict, wordLen)
            else:
                front = generateNextSet2(front, wordDict)
            if front & back:
                # there are common elements in front and back, done
                return steps
            steps += 1
            if len(front) >= len(back):
                # swap front and back for better performance (smaller nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycles
            if (len(wordDict)>>1) >= len(front):
                # s.difference_update(t): O(len(t))
                wordDict -= front
            else:
                # s.difference(t): O(len(s))
                wordDict = wordDict - front
        return 0
```
 Code: C++
 Optimization
 The above code can still be speeded up if we also begin from
 `end` 
 . Once we meet the same word from
 `start` 
 and
 `end` 
 , we know we are done.
 This link
 provides a nice two-end search solution. I rewrite the code below for better readability. Note that the use of two pointers
 `phead` 
 and
 `ptail` 
 save a lot of time. At each round of BFS, depending on the relative size of
 `head` 
 and
 `tail` 
 , we point
 `phead` 
 to the smaller set to reduce the running time.
```python
class Solution :
public:
    ladderLength(string beginWord, string endWord, vector<string>& wordList) :
        unordered_set<string> wordDict (wordList.begin(), wordList.end())
        if (wordDict.find(endWord) == wordDict.end()) return 0
        unordered_set<string> head, tail, *phead, *ptail
        head.insert(beginWord)
        tail.insert(endWord)
        dist = 2
        while (!head.empty() && !tail.empty()) :
            if (head.size() <= tail.size()) :
                phead = &head
                ptail = &tail
        else :
                phead = &tail
                ptail = &head
        unordered_set<string> temp
        for (auto itr = phead -> begin() itr != phead -> end() itr++) :
            string word = *itr
            for (p = 0 p < (int)word.length() p++) :
                char letter = word[p]
                for (k = 0 k < 26 k++) :
                    word[p] = 'a' + k
                    if (ptail -> find(word) != ptail -> end())
                        return dist
                    if (wordDict.find(word) != wordDict.end()) :
                        temp.insert(word)
                        wordDict.erase(word)
                word[p] = letter
        dist++ 
        #  throw away the expaned and add in new candidate into set
        *phead = temp
        return 0
```
------------------------------------------------------------------------------------------------
 212. Word Search II
=======================
 Given a 2D board and a list of words from the dictionary, find all words in the board.
 Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
 Example:
```
Input:
words = ["oath","pea","eat","rain"] and board =
[ 
 ['o','a','a','n'],
 ['e','t','a','e'],
 ['i','h','k','r'],
 ['i','f','l','v']
]
Output: ["eat","oath"]
```
 Note:
 You may assume that all inputs are consist of lowercase letters
 `a-z` 
 .
 Thoughts
1. How do we instantly know the current character is invalid? -> hashmap?
2. How do we instantly know what's the next valid character? -> LinkedList
3. But the next character can be chosen from a list of characters. -> "Multi-LinkedList?"
4. Combing them,
 `Trie` 
 is the natural choice. Notice that:
	1. No need to store character at TrieNode:
	 `c.next[i] != null` 
	 is enough.
	2. No need to use O(n^2) extra space visited[m][n]
	3. No need to use
	 `StringBuilder` 
	 . Storing
	 `word` 
	 itself at leaf node is enough
	4. No need to use
	 `Hashset` 
	 to de-duplicate. Set "cur.word = null" each time when found a character during DFS
5. Optimization:
	1. w.toCharArray() -> w.charAt(i)
	2. visited[m][n] -> board[i][j] = '#'
	3. checking index validity before calling dfs
	4. [c - ''a'] to i
6. Time Complexity
	1. O( l * wl) - Build the Tree
	2. O(min(m * n, wl) * l): worse case cenario. However, if words starting with the same characters and path sharing the cells, Trie can check multiple words when DFS from a certain cell, rather than check only one word when DFS from a certain cell like the naive way - Search
7. Space Complexity:
	1. O(l * wl) = max(O(wl), O(l * wl)) where:
		1. O(wl) recursive call
		2. O(l * wl) In the worst case when all words start with different characters, the trie has l * wl nodes. Also, since each word is stored in a leaf node, all the leaf nodes require l * wl memory (can be augmented by only store a boolean, but need to further discuss how to add found results in res), but the number of nodes stored in the tree is still l * wl
 Code:
```python
class Solution :
    public List<String> findWords(char[][] board, String[] words) :
        List<String> res = new ArrayList<>()
        TrieNode root = buildTrie(words)
        for(i = 0 i < board.length i++):
            for(j = 0 j < board[0].length j++):
                dfs(board,i,j ,root, res)
        return res
    private void dfs(char[][] board, i, j, TrieNode cur, List<String> res):
        char c = board[i][j]
        if(c == '#' || cur.next[c - 'a'] == null) return
        cur = cur.next[c-'a']
        if(cur.word != null):
            res.add(cur.word)
            cur.word = null #  de-duplicate
        board[i][j] = '#' #  visited
        if (i > 0) dfs(board, i - 1, j, cur, res)
        if (j > 0) dfs(board, i, j - 1, cur, res)
        if (i + 1< board.length) dfs(board, i + 1, j , cur, res)
        if (j + 1< board[0].length) dfs(board, i, j + 1, cur, res)
        board[i][j] = c
    private TrieNode buildTrie(String [] words):
        TrieNode root = new TrieNode()
        for(String word: words):
            TrieNode cur = root
            for (char c: word.toCharArray()):
                if(cur.next[c - 'a']== null) cur.next[c - 'a'] = new TrieNode()
                cur = cur.next[c - 'a']
            cur.word = word
        return root
class TrieNode:
    TrieNode [] next = new TrieNode[26]
    String word
```
 Reference to this
 post
------------------------------------------------------------------------------------------------
 79. Word Search
===================
 Given a 2D board and a word, find if the word exists in the grid.
 The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
 Example:
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```
 Thoughts:
1. Backtracking
 Code
```python
class Solution :
    public boolean exist(char[][] board, String word) :
        char[] w = word.toCharArray()
        for (i=0 i<board.length i++) :
            for (j=0 j<board[i].length j++) :
                if (exist(board, i, j, w, 0)) return true
        return false
    private boolean exist(char[][] board, x, y, char[] word, i) :
        if (i == word.length) return true
        if (y<0 || x<0 || x == board.length || y == board[x].length) return false
        if (board[x][y] != word[i]) return false
        board[x][y] ^= 256 #  flip every bit over
        boolean exist = exist(board, x, y+1, word, i+1) #  right
            || exist(board, x, y-1, word, i+1) #  left
            || exist(board, x+1, y, word, i+1) #  down
            || exist(board, x-1, y, word, i+1) #  up
        board[x][y] ^= 256 #  flip every bit over to recover the original value
        return exist
```
------------------------------------------------------------------------------------------------
 281. Zigzag Iterator
========================
 Given two 1d vectors, implement an iterator to return their elements alternately.
 Example:
```
Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling  next repeatedly until hasNext returns false, the order of elements returned by next
should be: [1,3,2,4,5,6].
```
 Follow up
 :
 What if you are given
 `k` 
 1d vectors? How well can your code be extended to such cases?
 Clarificationfor the follow up question:
 The "Zigzag" order is not clearly defined and is ambiguous for
 `k > 2` 
 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:
```
Input:
[1,2,3]
[4,5,6,7]
[8,9]
Output: [1,4,8,2,5,9,3,6,7].
```
 Code: Python Generator
```python
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
 Initialize your data structure here.
 :type v1: List[int]
 :type v2: List[int]
 """
        self.vals = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))
        self.n = len(v1) + len(v2)
    def next(self):
        """
 :rtype: int
 """
        self.n -= 1
        return next(self.vals)
    def hasNext(self):
        """
 :rtype: bool
 """
        return self.n > 0
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
```
 Code: Java k vectors
```python
public class ZigzagIterator :
    LinkedList<Iterator> queue
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) :
        queue = new LinkedList()
        if(!v1.isEmpty())
           queue.add(v1.iterator())
        if(!v2.isEmpty())
            queue.add(v2.iterator())
    public next() :
        Iterator iter = queue.remove() # 
        ret = (Integer)iter.next()
        if(iter.hasNext()) queue.add(iter)
        return ret
    public boolean hasNext() :
        return !queue.isEmpty()
/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2)
 * while (i.hasNext()) v[f()] = i.next()
 */
```
 C++ Iterator < start: end> pairs
```python
class ZigzagIterator :
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) :
       if(!v1.empty())  q.push(make_pair(v1.begin(), v1.end()))
       if(!v2.empty())  q.push(make_pair(v2.begin(), v2.end()))
    next() :
        auto i = q.front().first
        auto end = q.front().second 
        q.pop()
        if(i + 1 != end) q.push(make_pair(i + 1, end))
        return *i        
    bool hasNext() :
        return !q.empty()
private:
    queue<pair<vector<int>:: iterator, vector<int>:: iterator>> q
/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2)
 * while (i.hasNext()) cout << i.next()
 */
```
------------------------------------------------------------------------------------------------
 11. Container With Most Water
=================================
 Given n non-negative integers a1, a2, ...,an , where each represents a point at coordinate (i, ai).n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
 Note:
 You may not slant the container and n is at least 2.
![](../assets/water.png)
 The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
 Example:
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```
 Thoughts:
1. Two pointer: the shorter height need to move since the rest solution is guaranteed less optimal
```python
class Solution(object):
    def maxArea(self, height):
        """
 :type height: List[int]
 :rtype: int
 """
        left, right = 0, len(height) -1
        res = 0
        while left <= right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return res
```
```python
class Solution(object):
    def maxArea(self, height):
        """
 :type height: List[int]
 :rtype: int
 """
        res, i, j = 0 , 0, len(height) -1
        while i < j:
            h = min(height[i], height[j])
            res = max(res, (j - i)*h)
            while i < j and height[i] <= h: i+= 1
            while i < j and height[j] <= h: j-= 1
        return res
```
------------------------------------------------------------------------------------------------
 448. Find All Numbers Disappeared in an Array
=================================================
 Given an array of integers where 1 ≤ a[i] ≤n(n= size of array), some elements appear twice and others appear once.
 Find all the elements of [1,n] inclusive that do not appear in this array.
 Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
 Example:
```
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
```
 Thoughts:
1. mark the value indexed by current value as negative
2. add all index whose number is not negative (since originally 1 ≤ a[i] ≤n(n= size of array)
```python
class Solution(object):
    def findDisappearedNumbers(self, A):
        """
 :type A: List[int]
 :rtype: List[int]
 """
        # negating the number indexed by the value
        for i in range(len(A)):
            idx = abs(A[i]) - 1
            if(A[idx] > 0):
                A[idx] = -A[idx]
        res = []
        for i in range(len(A)):
            if(A[i] > 0):
                res.append(i + 1)
        return res
```
```python
class Solution(object):
    def findDisappearedNumbers(self, A):
        """
 :type A: List[int]
 :rtype: List[int]
 """
        for num in A:
            i = abs(num) - 1
            if A[i] > 0:
                A[i] = -A[i]
        return [i + 1 for i in range(len(A)) if A[i] > 0]
```
------------------------------------------------------------------------------------------------
 825. Friends of Appropriate Ages
====================================
 Some people will make friend requests. The list of their ages is given and
 `ages[i]` 
 is the age of the ith person.
 Person A will NOT friend request person B (B != A) if any of the following conditions are true:
* `age[B] <= 0.5 * age[A] + 7`
* `age[B] > age[A]`
* `age[B] > 100 && age[A] < 100`
 Otherwise, A will friend request B.
 Note that if A requests B, B does not necessarily request A. Also, people will not friend request themselves.
 How many total friend requests are made?
 Example 1:
```
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
```
 Example 2:
```
Input: 
[16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
```
 Example 3:
```
Input: 
[20,30,100,110,120]
Output: 
Explanation: 
Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
```
 Notes:
* `1 <= ages.length <= 200 00` 
 .
* `1 <= ages[i] <= 120` 
 .
 Thoughts:
1. 0.5 A + 7 < B <= A : so A >= 15 the three condition is redundant
 Code:
 O(n + r * r), r: age range
```python
class Solution :
public:
    numFriendRequests(vector<int>& ages) :
        a[121] = :, res = 0
        for (auto age : ages) a[age]++
        for (auto A = 15 A <= 120 A++)
            for(B = 0.5 * A + 8 B <= A B++):
                res += a[B] * (a[A] - (A == B))
        return res
```
 Code:
 O(n + m), r: age range
```python
class Solution :
public:
    numFriendRequests(vector<int>& ages) :
        a[121] =:, res = 0
        for (auto age : ages) a[age]++
        for (A = 15, lower = 15, acc = 0 A <= 120 acc += a[A], res+= a[A++] * (acc - 1))
            #  meet the first constraint by removing out those low ages that does not qualify
            while(lower <= 0.5 * A + 7) acc -=  a[lower++]
        return res
```
------------------------------------------------------------------------------------------------
 289. Game of Life
=====================
 According to the[Wikipedia's article]([[
 https:# en.wikipedia.org/wiki/Conway's_Game_of_Life](https:# en.wikipedia.org/wiki/Conway's_Game_of_Life)](https:# en.wikipedia.org/wiki/Conway's_Game_of_Life](https:# en.wikipedia.org/wiki/Conway's_Game_of_Life))\
 ): "The
 Game of Life
 , also known simply as
 Life
 , is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
 Given aboard with m by n cells, each cell has an initial state live(1) or dead(0). Each cell interacts with its
 eight neighbors
 (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
 Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
 Example:
```
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
```
 Follow up
 :
1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
 Thought:
1. In place algorithm: each time encode the board element 2bit state code [next state, current state] and transition by shifting the board element after encoding.
2. d
 Code
```python
class Solution(object):
    def gameOfLife(self, board):
        """
 :type board: List[List[int]]
 :rtype: void Do not return anything, modify board in-place instead.
 """
        m = len(board)
        n = len(board[0])
        def countLives(board, m , n , i, j):
            lives = 0
            for x in range (max(i - 1, 0), min(i + 1, m - 1) + 1):
                for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                    # print('x: : y:: i: : j:: board[i][j]::, lives::'.format(x,y,i,j,board[i][j], lives))
                    lives += (board[x][y] & 1)
            lives -= (board[i][j] & 1)
            print()
            return lives
        for i in range(m):
            for j in range(n):
                lives = countLives(board, m, n, i, j)
                if board[i][j] and (lives == 2 or lives == 3):
                    board[i][j] = 3 #encode 11 
                if not board[i][j] and (lives == 3):
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
```
 Code ( infinite case)
```python
class Solution(object):
    def gameOfLife(self, board):
        """
 :type board: List[List[int]]
 :rtype: void Do not return anything, modify board in-place instead.
 """
        # 1. find all the current alive cells
        # 2. update alive cells by counting the lives' neighbors appearance
        # 3. output results back to the board using alive cells
        live = :(i,j) for i, row in enumerate(board) for j, e in enumerate(row) if e
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i,j) in live) # a in-place solution for the board
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I,J)
                                 for i, j in live
                                 for I in range(i-1, i+2)
                                 for J in range(j-1, j+2)
                                 if I != i or J!= j)
        return :ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live
```
------------------------------------------------------------------------------------------------
 57. Insert Interval
=======================
 Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
 You may assume that the intervals were initially sorted according to their start times.
 Example 1:
```
Input:
 intervals = [[1,3],[6,9]], newInterval = [2,5]
Output:
 [[1,5],[6,9]]
```
 Example 2:
```
Input:
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```
 Thoughts:
1. Find the first and last interval index to merge(i,j) and merge them by creating a new interval with (min(
 ---firstInterval--- 
 .start,
 ---newInterval--- 
 .start), max(
 ---lastInterval--- 
 .end,
 ---newInterva--- 
 .end), and adding other intervals that is not merged.
	1. To find the first interval: incre i
	 until
	 intervals[i].end >
	 ---newInterval--- 
	 .start
	2. To find the last interval: incre j
	 until
	 intervals[j].start >
	 ---newInterval--- 
	 .end
	3. if i == j == 0 then only need to add _newinterval _in front
	4. if i == j == len, then only need to append _newinterval _in the end
2. One - Pass: Collect the intervals strictly left or right of the new interval, then merge the new one with the middle ones (if any) before inserting it between left and right ones.
 StefanPochmann
 's
 post
 Code
```
# Definition for an interval.
# class Interval(object):
# def __init__(self, s=0, e=0):
# self.start = s
# self.end = e
class Solution(object):
    def insert(self, intervals, newInterval):
        """
 :type intervals: List[Interval]
 :type newInterval: Interval
 :rtype: List[Interval]
 """
        res =[]
        i, j, n = 0, 0, len(intervals)
        while i < n:
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
                i +=1
            else: break
        while j < n:
            if intervals[j].start <= newInterval.end: j += 1
            else: break
        if i == j == 0:
            res.append(newInterval)
            res += intervals
            return res
        elif i == j == n:
            intervals.append(newInterval)
            return intervals
        merge = Interval(min(intervals[i].start, newInterval.start), max(intervals[j - 1].end, newInterval.end))
        res.append(merge)
        for k in range(j, n):
            res.append(intervals[k])
        return res
```
 Code
 : Python One pass
```
# Definition for an interval.
# class Interval(object):
# def __init__(self, s=0, e=0):
# self.start = s
# self.end = e
class Solution(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right
```
------------------------------------------------------------------------------------------------
 Interval
============
------------------------------------------------------------------------------------------------
 683. K Empty Slots
======================
 683. K Empty Slots
====================
 There is a garden with
 `N` 
 slots. In each slot, there is a flower. The
 `N` 
 flowers will bloom one by one in
 `N` 
 days. In each day, there will be
 `exactly` 
 one flower blooming and it will be in the status of blooming since then.
 Given an array
 `flowers` 
 consists of number from
 `1` 
 to
 `N` 
 . Each number in the array represents the place where the flower will open in that day.
 For example,
 `flowers[i] = x` 
 means that the unique flower that blooms at day
 `i` 
 will be at position
 `x` 
 , where
 `i` 
 and
 `x` 
 will be in the range from
 `1` 
 to
 `N` 
 .
 Also given an integer
 `k` 
 , you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is
 `k` 
 and these flowers are not blooming.
 If there isn't such day, output -1.
 Example 1:
```
Input:
flowers: [1,3,2]
k: 1
Output:
 2
Explanation:
 In the second day, the first and the third flower have become blooming.
```
 Example 2:
```
Input:
flowers: [1,2,3]
k: 1
Output:
 -1
```
 Note:
1. The given array will be in the range [1, 20000].
 Additional Notes:
`flowers[i] = x` 
1. should mean that the unique flower that blooms at day
 `i+1` 
 (not
 `i` 
 ) will be at position
 `x` 
 .
2. If you can get multiple possible results, then you need to return the minimum one.
 Thoughts:
1. construct a reverse index array: days[x] = i + 1 => the blooming day for place "x + 1" .
2. Find the subarray days[left, left + 1, ..., left + k - 1, right] which satisfies for and left + 1<= i <=left + k-1: days[left] < days[i] && days[right] < days[i] => result is max(days[left], day[right]).
 Code Time Complexity: O(n), Space Complexity O(n)
```python
class Solution :
public:
    kEmptySlots(vector<int>& flowers, k) :
        vector<int> days(flowers.size())
        for(i = 0 i < flowers.size() i++):
            days[flowers[i] - 1] = i + 1
        left = 0 , right = k + 1, ans = INT_MAX
        for (i = 0 right < days.size() i++):
            if(days[i] < days[left] || days[i] < days[right] || i == right):
                if(i == right) ans = min(ans, max(days[right], days[left]))
                left = i
                right = i + k + 1
        return (ans == INT_MAX) ?-1: ans
```
------------------------------------------------------------------------------------------------
 4. Median of Two Sorted Arrays
==================================
 4. Median of Two Sorted Arrays
================================
 There are two sorted arrays
 nums1
 and
 nums2
 of size m and n respectively.
 Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 Example 1:
```
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
```
 Example 2:
```
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
```
 Thoughts:
 use binary search to find the best partition i and j in nums1 and nums2 such that nums1[i] > A 2[j -1] && nums2[j] > nums1[i -1]. Also j = (m + n +1 )/ 2 - j (for n as the "longer" array length and m as the "shorter" array length, m >= n) to guarantee that i + j is the median position for odd number total length and left input of computing median for even total length.
 Code Time Complexity: O(min(m,n)), Space Complexity: O(1)
```python
class Solution :
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) :
         m = nums1.size(), n = nums2.size()
        if (m > n) return findMedianSortedArrays(nums2, nums1)
        i, j, imin = 0, imax = m, half = (m + n + 1) / 2
        #  bianry search to get optimal i
            while (imin <= imax) :
            i = (imin & imax) + ((imin ^ imax) >> 1) # (imin + imax)/2
            j = half - i
            if (i > 0 &&  nums1[i - 1] > nums2[j]) imax = i - 1 #  i too big, must decrease it.
            else if (i < m && nums2[j - 1] > nums1[i]) imin = i + 1 #  it too small, must increase it.
            else break
        max_left
        if(!i) max_left = nums2[j - 1] 
        else if(!j) max_left = nums1[i - 1]
        else max_left = max(nums1[i - 1], nums2[j - 1])
        if ((m + n) & 1) return max_left #  if m + n is odd
        min_right
        if(i == m) min_right = nums2[j]
        else if(j == n) min_right = nums1[i]
        else min_right = min(nums1[i],nums2[j])
        return (max_left + min_right)/ 2.0
```
 Special Thanks to
 missmary
 's
 solution& explanation
 and
 jianchao.li.fighter
 's code
------------------------------------------------------------------------------------------------
 56. Merge Interval
======================
 Given a collection of intervals, merge all overlapping intervals.
 Example 1:
```
Input:
 [[1,3],[2,6],[8,10],[15,18]]
Output:
 [[1,6],[8,10],[15,18]]
Explanation:
 Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```
 Example 2:
```
Input:
 [[1,4],[4,5]]
Output:
 [[1,5]]
Explanation:
 Intervals [1,4] and [4,5] are considered overlapping.
```
 Thoughts:
1. Sort the interval list according the start point
2. record end, for loop check whether the current interval's start time is after the record end if it is, merge the interval by maxing the end time if it is not, insert the interval of recorded start and end time and update them to start another interval to be merged with current start and end time.
 Code Java O(nlogn): Java8 lambda comparator
```
/**
 * Definition for an interval.
 * public class Interval :
 * start
 * end
 * Interval() : start = 0 end = 0 
 * Interval(s, e) : start = s end = e 
 * 
 */
class Solution :
    public List<Interval> merge(List<Interval> intervals) :
        if(intervals.size() <= 1) return intervals
        intervals.sort((i1, i2)->Integer.compare(i1.start, i2.start)) #  java8 lambda
        start = intervals.get(0).start, end =intervals.get(0).end
        List<Interval> results = new LinkedList <Interval>()
        for(Interval i: intervals):
            if(i.start <= end):
             end = Math.max(i.end, end)           #  merging 
            else:
              results.add(new Interval(start, end))   #  disjoint: first adding existing merged intervals, then update start, end
              start = i.start end = i.end #  update start, end
        results.add(new Interval(start, end))
        return results
```
 Code Python
```
# Definition for an interval.
# class Interval(object):
# def __init__(self, s=0, e=0):
# self.start = s
# self.end = e
class Solution(object):
    def merge(self, intervals):
        """
 :type intervals: List[Interval]
 :rtype: List[Interval]
 """
        intervals =sorted(intervals, key=lambda x:x.start)
        results = []
        l = len(intervals)
        i = 0
        while i < l:
            s = intervals[i].start
            e = intervals[i].end
            j = i + 1
            while j < l and e >= intervals[j].start:
                e = max(e, intervals[j].end)
                j += 1
            results.append(Interval(s,e))
            i = j
        return results
```
------------------------------------------------------------------------------------------------
 283. Move Zeros
===================
 283. Move Zeros
=================
 Given an array
 `A` 
 , write a function to move all
 `0` 
 's to the end of it while maintaining the relative order of the non-zero elements.
 For example, given
 `A = [0, 1, 0, 3, 12]` 
 , after calling your function,
 `A` 
 should be
 `[1, 3, 12, 0, 0]` 
 .
 Note
 :
1. You must do this
 in-place
 without making a copy of the array.
2. Minimize the total number of operations.
 Credits:
 Special thanks to
 @jianchao.li.fighter
 for adding this problem and creating all test cases.
 FB Followup: 输入是一个array, 有正数和负数，题目要求将正数移动到一侧，负数移动到另一侧。
 Thoughts:
 Having an pointer to keep track of non-zeros and replace the original value in the array then pad the rest of space with 0
 Code
```python
class Solution :
public:
    void moveZeroes(vector<int>& A) :
        j = 0
        for(i = 0  i < A.size() i++):
            if(A[i]!= 0) A[j++] = A[i] 
        for( j < A.size()j++):
            A[j] = 0
```
 FollowUp:
```
'''Ask if there is 0 in the array!'''
def move(arr): # with/ without 0
    i, j = 0, len(arr) - 1
    while True:
        while i <= j and arr[i] <= 0 : i+= 1
        while j >= i and arr[j] >= 0 : j-= 1
        if i > j: break
        arr[i], arr[j] = arr[j], arr[i]
    print(arr)
```
------------------------------------------------------------------------------------------------
 26. Remove Duplicates from Sorted Array
===========================================
 Given a sorted array
 ---A--- 
 , remove the duplicates
 in-place
 such that each element appear only _once _and return the new length.
 Do not allocate extra space for another array, you must do this by
 modifying the input array
 in-place
 with O(1) extra memory.
 Example 1:
```
Given 
A = [1,1,2],
Your function should return length = 2, with the first two elements of 
A being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
```
 Example 2:
```
Given A = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of A being modified to 0, 1, 2, 3, and  respectively.
It doesn't matter what values are set beyond the returned length.
```
```python
class Solution :
    public removeDuplicates(int[] A) :
        if(A == null || A.length == 0) return 0
        slow = 0 , fast = 0, len =1
        while(fast < A.length):
            if(A[slow] == A[fast]) fast++
            else:
                A[++slow] = A[fast++]
                len++
       return len 
```
------------------------------------------------------------------------------------------------
 54. Spiral Matrix
=====================
 Given a matrix of
 m
 x
 n
 elements (
 m
 rows,
 n
 columns), return all elements of the matrix in spiral order.
 Example 1:
```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:
 [1,2,3,6,9,8,7,4,5]
```
 Example 2:
```
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output:
 [1,2,3,4,8,12,11,10,9,5,6,7]
```
 Thoughts:
1. having four markers: rowBegin, rowEnd, colBegin, colEnd,
2. go right -> incre rowBegin go down -> decre colEnd go left -> check(rowBegin <= rowEnd), decre rowEnd go up ->check(colBegin <= colEnd), incre colBegin
 Code Java
```python
class Solution :
    public List<Integer> spiralOrder(int[][] matrix) :
        List<Integer> res = new LinkedList<Integer>()
        if(matrix.length == 0) return res
        rowBegin = 0, rowEnd = matrix.length - 1
        colBegin = 0, colEnd = matrix[0].length - 1
        while(rowBegin <= rowEnd && colBegin <= colEnd):
                #  go right
            for(j = colBegin j <= colEnd j++):
                res.add(matrix[rowBegin][j])
            rowBegin++
            #  go down
            for (i = rowBegin  i <= rowEnd i++):
                res.add(matrix[i][colEnd])
            colEnd--
            #  go left
            if(rowBegin <= rowEnd):
                for(j = colEnd j >= colBegin j --):
                    res.add(matrix[rowEnd][j])
            rowEnd--
            #  go up
            if(colBegin <= colEnd):
                for(i = rowEnd i >= rowBegin i--):
                    res.add(matrix[i][colBegin])
            colBegin++
        return res
```
```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
 :type matrix: List[List[int]]
 :rtype: List[int]
 """
        res = []
        if not matrix: return res
        rowS, colS, rowE, colE = 0, 0, len(matrix) - 1, len(matrix[0]) -1
        while rowS <= rowE and colS <= colE:
            # right
            for j in range(colS, colE + 1):
                res.append(matrix[rowS][j])
            rowS+= 1
            # down
            for i in range(rowS, rowE + 1):
                res.append(matrix[i][colE])
            colE-= 1
            # left
            if rowS <= rowE:
                for j in range(colE,colS - 1,-1):
                    res.append(matrix[rowE][j])
                rowE -= 1
            # up
            if colS <= colE:
                for i in range(rowE, rowS - 1, -1):
                    res.append(matrix[i][colS])
                colS+= 1
        return res
```
 from
 qwl5004
 's
 post
------------------------------------------------------------------------------------------------
 228. Summary Ranges
=======================
 Given a sorted integer array without duplicates, return the summary of its ranges.
 Example 1:
```
Input:
  [0,1,2,4,5,7]
Output:
 ["0->2","4->5","7"]
Explanation: 
0,1,2 form a continuous range 4,5 form a continuous range.
```
 Example 2:
```
Input:
  [0,2,3,4,6,8,9]
Output:
 ["0","2->4","6","8->9"]
Explanation: 
2,3,4 form a continuous range 8,9 form a continuous range.
```
 Thoughts:
1. record number a as A[i], if there is a next number and the next number is continuous update i.
2. check the A[i] with original if it is not equal (i was updated -> add string "a" + "->" + "A[i]")
 else (i was not updated ->only add string "a").
 Code
```python
class Solution(object):
    def summaryRanges(self, A):
        """
 :type A: List[int]
 :rtype: List[str]
 """
        n = len(A)
        i = 0
        ret = []
        while i < n:
            e = ':'.format(A[i])
            a = A[i]
            while i + 1 < n and A[i] + 1 == A[i+1]:
                i = i + 1
            if a != A[i]:
                ret.append(e + '->' + ":".format(A[i]))
            else:
                ret.append(e)
            i = i + 1
        return ret
```
------------------------------------------------------------------------------------------------
 Backpack II
===============
 Backpack IIProblem 单次选择+最大价值
==============================
 Given n items with size A[i] and value V[i], and a backpack with size m. What's the maximum value can you put into the backpack?
 You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.
 Example
---------
 Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.
 Challenge
-----------
 O(n x m) memory is acceptable, can you do it in O(m) memory?
 Note
------
 和BackPack I基本一致。依然是以背包空间为限制条件，所不同的是dp[j]取的是价值较大值，而非体积较大值。所以只要把dp[j-A[i]]+A[i]换成dp[j-A[i]]+V[i]就可以了。
 Solution
----------
```python
public class Solution :
    public backPackII(m, int[] A, V[]) :
        int[] dp = new int[m+1]
        for (i = 0 i < A.length i++) :
            for (j = m j > 0 j--) :
                if (j >= A[i]) dp[j] = Math.max(dp[j], dp[j-A[i]]+V[i])
        return dp[m]
```
------------------------------------------------------------------------------------------------
 Backpack I
==============
### 
 Description
 Given
 ---n _items with size _Ai--- 
 , an integer _m _denotes the size of a backpack. How full you can fill this backpack?
 You can not divide any item into small pieces.
 Have you met this question in a real interview?
 Yes
### 
 Example
 If we have
 `4` 
 items with size
 `[2, 3, 5, 7]` 
 , the backpack size is 11, we can select
 `[2, 3, 5]` 
 , so that the max size we can fill this backpack is
 `10` 
 . If the backpack size is
 `12` 
 . we can select
 `[2, 3, 7]` 
 so that we can fulfill the backpack.
 You function should return the max size we can fill in the given backpack.
### 
 Challenge
 O(n x m) time and O(m) memory.
 O(n x m) memory is also acceptable if you do not know how to optimize memory.
 Thoughts
 :
1. 0 - 1 backpack problem
2. Space-optimized Solution:
	1. dp[j] = for size j, there is a solution for current A[0, ... i] items
	2. dp[0] = True
	3. in
	 reverse order:
	 dp[j] |= dp[j - A[i]] # we can insert item A[i] into j
	4. solution : max i such that dp[i] == 1
3. Non-optimized Solution:
	1. dp[i][j]: for (i - 1) th item i, whether size j contain full bag (0th is for initial state)
	2. dp[.][0] = True
	3. in
	 left-right order:
	 dp[i][j] = dp[i - 1][j - A[i - 1]] for j >= A[i - 1]
4. real value Solution
 Code T:
 2614 ms
 O(m * n) S: O(m)
```python
class Solution:
    """
 @param m: An integer m denotes the size of a backpack
 @param A: Given n items with size A[i]
 @return: The maximum size
 """
    def backPack(self, m, A):
        # write your code here
        dp = [0 for _ in range(m + 1)]
        dp[0] = 1
        for i in range( len(A) ):
            for j in range(m, A[i ]-1, -1):
                dp[j] |= dp[j - A[i]]
        for i in range(m, -1, -1):
            if dp[i]:
                return i
        return 0
```
 Code T: O(m * n)
 6288 ms
  S: O(m * n)
```python
class Solution:
    """
 @param m: An integer m denotes the size of a backpack
 @param A: Given n items with size A[i]
 @return: The maximum size
 """
    def backPack(self, m, A):
        # write your code here
        dp = [[0 for j in range(m + 1)] for i in range(len(A) + 1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        # print('m + 1: : n + 1: :'.format(len(dp),len(dp[0])))
        for i in range(1, len(A) + 1):
            for j in range (m + 1):
                # print('i: : j: :'.format(i,j))
                dp[i][j] = dp[i-1][j]
                if j >= A[i-1] and dp[i - 1][j - A[i - 1]]:
                    dp[i][j] = 1
        for j in range(m, -1 , -1):
            if dp[len(A)][j]:
                return j
        return 0
```
 Code T: O(m * n)
 2397 ms
 S: O(m)
```python
public class Solution :
    public backPack(m, int[] A) :
        int[] dp = new int[m+1]
        for (i = 0 i < A.length i++) :
            for (j = m j > 0 j--) :
                if (j >= A[i]) :
                    dp[j] = Math.max(dp[j], dp[j-A[i]] + A[i])
        return dp[m]
```
------------------------------------------------------------------------------------------------
 Backpack III
==============
 Given n kind of items with size Ai and value Vi( each item has an infinite number available) and a backpack with size m. What's the maximum value can you put into the backpack?
 Notice
 You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.
 Example
---------
 Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.
```python
public class Solution :
    public backPackIII(int[] A, int[] V, m) :
        int[] dp = new int[m+1]
        for (i = 0 i < A.length i++) :
            for (j = 1 j <= m j++) :
                if (j >= A[i]) dp[j] = Math.max(dp[j], dp[j-A[i]]+V[i])
        return dp[m]
```
------------------------------------------------------------------------------------------------
 Backpack IV
===============
 Backpack IV
=============
 Given n items with size A[i] in an integer array with all positive numbers, no duplicates. An integer target denotes the size of a backpack. Find the
 number of possible ways to fill the backpack
 .
 Each item may be chosen unlimited number of times
 Example
---------
 Given candidate items [2,3,6,7] and target 7,
 A solution set is:
```
[7]
[2, 2, 3]
return 2
```
 Solution
----------
```python
public class Solution :
    public backPackIV(int[] A, target) :
        int[] dp = new int[target+1]
        dp[0] = 1
        for (i = 0 i < A.length i++) :
            for (j = 1 j <= target j++) :
                if (A[i] == j) dp[j]++
                else if (A[i] < j) dp[j] += dp[j-A[i]]
        return dp[target]
```
------------------------------------------------------------------------------------------------
 Backpack V
============
 Given n items with size A[i] which an integer array and all positive numbers. An integer target denotes the size of a backpack. Find the number of possible fill the backpack.
 Each item may only be used once
 Example
---------
 Given candidate items [1,2,3,3,7] and target 7,
 A solution set is:
```
[7]
[1, 3, 3]
return 2
```
 Solution
----------
```python
public class Solution :
    public backPackV(int[] A, target) :
        int[] dp = new int[target+1]
        dp[0] = 1
        for (i = 0 i < A.length i++) :
            for (j = target j >= 0 j--) :
                if (j >= A[i]) dp[j] += dp[j-A[i]]
        return dp[target]
```
------------------------------------------------------------------------------------------------
 Backpack VI aka: Combination Sum IV
=====================================
 Given an integer array A with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
 Notice
--------
 The different sequences are counted as different combinations.
 Example
---------
 Given A = [1, 2, 4], target = 4
 The possible combination ways are:
```
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
[4]
return 6
```
 Solution
----------
```python
public class Solution :
    public backPackVI(int[] A, target) :
        int[] dp = new int[target+1]
        dp[0] = 1
        for (i = 1 i <= target i++) :
            for (num: A) :
                if (num <= i) dp[i] += dp[i-num]
        return dp[target]
```
------------------------------------------------------------------------------------------------
 Coin Change 2
=================
 You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
 Note:
 You can assume that
* 0 <= amount <= 5000
* 1 <= coin <= 5000
* the number of coins is less than 500
* the answer is guaranteed to fit into signed 32-bit integer
 Thoughts:
1. `dp[i][j]` 
 : the number of combinations to make up amount
 `j` 
 by using the first
 `i` 
 types of coins
 `State transition` 
 :
	1. not using the
	 `i` 
	 th coin, only using the first
	 `i-1` 
	 coins to make up amount
	 `j` 
	 , then we have
	 `dp[i-1][j]` 
	 ways.
	2. using the
	 `i` 
	 th coin, since we can use unlimited same coin, we need to know how many way to make up amount
	 `j - coins[i]` 
	 by using first
	 `i` 
	 coins( including
	 `i` 
	 th), which is
	 `dp[i][j-coins[i]]`
	3. `Initialization` 
	 :
	 `dp[i][0] = 1`
2. `dp[i][j]` 
 only rely on
 `dp[i-1][j]` 
 and
 `dp[i][j-coins[i]]` 
 , then we can optimize the space by only using one-dimension array.
 Code: 2D DP: O(K * N), S: O(K * N)
```python
class Solution :
    public change(amount, int[] coins) :
        int[][] dp = new int[coins.length+1][amount+1]
        dp[0][0] = 1
        for (i = 1 i <= coins.length i++) :
            dp[i][0] = 1
            for (j = 1 j <= amount j++) :
                dp[i][j] = dp[i-1][j] + (j >= coins[i-1] ? dp[i][j-coins[i-1]] : 0)
        return dp[coins.length][amount]
```
 Code: 1D DP: O(K * N), S: O(N)
```python
class Solution :
    public change(amount, int[] coins) :
        if(amount < 0) return 0
        dp[] = new [amount + 1]
        dp[0] = 1
        for(coin: coins):
            for(i = coin i <= amount  i++):
                dp[i]+= dp[i - coin]
        return dp[amount]
```
------------------------------------------------------------------------------------------------
 231. Power of Two
=====================
 Given an integer, write a function to determine if it is a power of two.
 Example 1:
```
Input:1
Output:true 
Explanation: 2^0 = 1
```
 Example 2:
```
Input:16
Output:true
Explanation: 2^4 = 16
```
 Example 3:
```
Input:218
Output:false
```
 Thoughts:
 Power of 2 means only one bit of n is '1', so use the trick n& (n-1)==0 to judge whether that is the case
```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
 :type n: int
 :rtype: bool
 """
        return False if n<= 0 else (n & (n-1)) == 0
```
------------------------------------------------------------------------------------------------
 371. Sum of Two Integers
============================
 Calculate the sum of two integersaandb, but you are
 not allowed
 to use the operator
 `+` 
 and
 `-` 
 .
 Example 1:
```
Input: 
a = 1, b = 2
Output: 3
```
 Example 2:
```
Input: 
a = -2, b = 3
Output: 1
```
 Thoughts: (
 from Bit Manipulation Summary
 )
1. ##### 
 ^ tricks: Use ^to
 remove even exactly same numbers and save the odd, or save the distinct bits and remove the same. Sum of Two Integers Use^and&to add two integers
 Code
```python
class Solution :
public:
    getSum(a, b) :
        return b == 0? a: getSum(a^b, (a&b) << 1)
```
------------------------------------------------------------------------------------------------
 393. UTF-8 Validation
=========================
 A character in UTF8 can be from
 1 to 4 bytes
 long, subjected to the following rules:
1. For 1-byte character, the first bit is a 0, followed by its unicode code.
2. For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
 This is how the UTF-8 encoding would work:
```
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------------------------------------------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```
 Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
 Note:
 The input is an array of integers. Only the
 least significant 8 bits
 of each integer is used to store the data. This means each integer represents only 1 byte of data.
 Example 1:
```
data = [197, 130, 1], which represents the octet sequence: 
11000101 10000010 00000001
.
Return 
true
.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
```
 Example 2:
```
data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
```
```python
class Solution :
public:
    bool validUtf8(vector<int>& data) :
        count = 0
        for (auto d: data):
            if(count == 0):
                if(d >> 5 == 0b110) count = 1  #  follwing one bytes
                else if(d >> 4 == 0b1110) count = 2  #  follwing two bytes
                else if(d >> 3 == 0b11110) count = 3   #  follwing three bytes 
                else if(d >> 7) return false #  for chars more than 4 bytes, it will be returned here  for input [255], for 1 byte char: the first bit is 0
            else:
                if (d >> 6 != 0b10) return false
                count--
        return count == 0
```
```python
class Solution(object):
    def validUtf8(self, data):
        """
 :type data: List[int]
 :rtype: bool
 """
        cnt = 0
        for d in data:
            if cnt:
                if d > 191 or d < 128: return False # 0xxxxxxx or 11xxxxxx
                cnt -= 1
            else:
                if d > 247: return False # 11111xxx -> more than 4 bytes
                if d > 239: cnt = 3 #11110xxx
                elif d > 223: cnt = 2 #1110xxxx
                elif d > 191: cnt = 1 #110xxxxx
                elif 0 <= d < 128: continue #0xxxxxxx
                else: return False
        return not cnt
```
------------------------------------------------------------------------------------------------
 Count number of occurrences (or frequency) in a sorted array
==============================================================
 Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)
 Examples:
```
  Input: arr[] = :1, 1, 2, 2, 2, 2, 3,,   x = 2
  Output: 4 #  x (or 2) occurs 4 times in arr[]
  Input: arr[] = :1, 1, 2, 2, 2, 2, 3,,   x = 3
  Output: 1 
  Input: arr[] = :1, 1, 2, 2, 2, 2, 3,,   x = 1
  Output: 2 
  Input: arr[] = :1, 1, 2, 2, 2, 2, 3,,   x = 4
  Output: -1 #  4 doesn't occur in arr[]
```
 **Thoughts:
1. **Use conditional binary search to find the first and last occurrence of the target number. Then the length is right - left + 1
 Code
```python
class Solution:
    def number_of_occurance(self, arr, k):
        def first(arr, k):
            low, high  = 0 , len(arr) -1
            while (low <= high):
                mid = low + (high - low >> 1)
                if arr[mid] == k and (mid == 0 or k > arr[mid - 1]):
                    return mid
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        def last(arr, low, high, k):
            while ( low <= high):
                mid = low + ((high - low)>> 1)
                if arr[mid]==k and (mid == (len(arr) - 1) or k < arr[mid + 1]):
                    return mid
                elif arr[mid] > k:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        i = first(arr, k)
        if i < 0:
            return -1
        j = last(arr, i, len(arr) - 1, k)
        return j - i + 1
arr = [1,1,2,2,2,2,3]
s = Solution()
print(s.number_of_occurance(arr,4))
```
 Full Explanation on
 GeeksforGeeks
------------------------------------------------------------------------------------------------
 34. Find First and Last Position of Element in Sorted Array
===============================================================
 Given an array of integers
 `A` 
 sorted in ascending order, find the starting and ending position of a given
 `target` 
 value.
 Your algorithm's runtime complexity must be in the order of
 ---O--- 
 (log
 ---n--- 
 ).
 If the target is not found in the array, return
 `[-1, -1]` 
 .
 Example 1:
```
Input:
 A = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
 Example 2:
```
Input:
 A = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
 Thoughts:
1. Two binary searches: Search left as target - 0.5, right as target + 0.5
2. Two binary searches:
3. Divide and Conquer with early breaks
 a variety of ways to solve the problem
 Code: Solution 1: T O(logn)
```python
class Solution(object):
    def searchRange(self, A, target):
        """
 :type A: List[int]
 :type target: int
 :rtype: List[int]
 """
        def binarySearch(A, target):
            l, h = 0, len(A) -1
            while l <= h: # NEED this because of single input e.g: [1], 1
                mid = l + (h - l >>1)
                if A[mid] > target:
                    h = mid - 1
                elif A[mid] < target:
                    l = mid + 1
            return l # MUST BE L to slide over 
        left = target - 0.5
        right = target + 0.5
        l, r = binarySearch(A, left), binarySearch(A, right)
        if l == r: return [-1, -1]
        return [l, r - 1]
```
 Code: Solution 2: T O(logn)
```python
class Solution(object):
    def searchRange(self, A, target):
        def search(n):
            lo, hi = 0, len(A)
            while lo < hi:
                mid = (lo + hi) / 2
                if A[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        if not len(A):
            return [-1, -1]
        lo = search(target)
        return [lo, search(target+1)-1] if  lo < len(A) and A[lo] == target else [-1, -1] # in is to present index out of bounds. e.g: input = [] [2,2] 3
```
 C++
```python
class Solution :
public:
    vector<int> searchRange(vector<int>& A, target) :
        vector<int> ret(2, -1)
        if (A.size() == 0) return ret
        n = A.size()
        i = 0, j = n - 1
        #  Search for the left one
        while (i < j)
        :
            mid = (i + j) /2
            if (A[mid] < target) i = mid + 1
            #  else if (A[mid] > target) j = mid - 1
            else j = mid
        if (A[i]!=target) return ret
        else ret[0] = i
        #  Search for the right one
        j = n-1  #  We don't have to set i to 0 the second time.
        while (i < j)
        :
            mid = (i + j) /2 + 1    #  Make mid biased to the right
            if (A[mid] > target) j = mid - 1  
            #  else if (A[mid] < target) i = mid + 1
            else i = mid                #  So that this won't make the search range stuck.
        ret[1] = j
        return ret 
```
 Python
```python
class Solution(object):
    def searchRange(self, A, target):
        """
 :type A: List[int]
 :type target: int
 :rtype: List[int]
 """
        res = [-1,-1]
        if not A: return res
        i, j = 0, len(A) - 1
        while i < j:
            mid = i + (j - i >> 1)
            if A[mid] < target:
                i = mid + 1
            else:
                j = mid
        if A[i] != target: return res
        res[0], j = i, len(A) -1
        while i < j:
            mid = i + (j - i + 1)/2
            if A[mid] > target:
                j = mid - 1
            else:
                i = mid
        res[1] = j
        return res
```
 Code:
 Divide and Conquer with early breaks
```
def searchRange(self, A, target):
    def search(lo, hi):
        if A[lo] == target == A[hi]:
            return [lo, hi]
        if A[lo] <= target <= A[hi]:
            mid = (lo + hi) / 2
            l, r = search(lo, mid), search(mid+1, hi)
            return max(l, r) if -1 in l+r else [l[0], r[1]]
        return [-1, -1]
    return search(0, len(A)-1)
```
------------------------------------------------------------------------------------------------
 658. Find K Closest Elements
================================
 Given a sorted array, two integers
 `k` 
 and
 `x` 
 , find the
 `k` 
 closest elements to
 `x` 
 in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
 Example 1:
```
Input:
 [1,2,3,4,5], k=4, x=3
Output:
 [1,2,3,4]
```
 Example 2:
```
Input:
 [1,2,3,4,5], k=4, x=-1
Output:
 [1,2,3,4]
```
 Note:
1. The value k is positive and will always be smaller than the length of the sorted array.
2. Length of the given array is positive and will not exceed 10^4
3. Absolute value of elements in the array and x will not exceed 10^4
 Thoughts:
1. Binary -searching the first index i that arr[i] is closer or equally close to arr[i+k] (Original
 Post
 )
2. Binary-searching for
 `x` 
 and then expanding to the left and to the right: The idea is to find the first number which is equal to or greater than
 `x` 
 in
 `arr` 
 . Then, we determine the indices of the start and the end of a subarray in
 `arr` 
 , where the subarray is our result. The time complexity is
 `O(logn + k)` 
 .
 Code:
 Binary -searching for the first index i
 T: O(log(n-k))
```python
class Solution :
    public List<Integer> findClosestElements(int[] arr, k, x) :
        i = 0, j = arr.length - k
        while (i < j):
            mid = (i & j) + ((i ^ j) >> 1)
            #  mid = i + (j - i >> 1)
            if(x - arr[mid] > arr[mid + k] - x)
                i = mid + 1
            else
                j = mid
        List<Integer> res = new ArrayList<>()
        for (b = i b < i + k ++b) res.add(arr[b])
        return res
        #  return Arrays.stream(Arrays.copyOfRange(arr, i, i + k)).boxed().collect(Collectors.toList()) 
```
 Python: T: O(log(n-k))
```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
 :type arr: List[int]
 :type k: int
 :type x: int
 :rtype: List[int]
 """
        i, j = 0, len(arr) - k
        while i < j:
            mid = (i & j) + ((i^j)>> 1)
            if x - arr[mid] > arr[mid + k] - x: # arr is sorted
                i = mid + 1
            else:
                j = mid
        return arr[i:i+k]
```
 Code 2:
 Reference
 T: O(log(n)+k)
```
  public List<Integer> findClosestElements(List<Integer> arr, k, x) :
        index = Collections.binarySearch(arr, x)
        if(index < 0) index = -(index + 1)
        i = index - 1, j = index                                    
        while(k-- > 0):
            if(i < 0 || (j < arr.size() && Math.abs(arr.get(i) - x) > Math.abs(arr.get(j) - x)))j++
            else i--
        return arr.subList(i+1, j)
```
------------------------------------------------------------------------------------------------
 154. Find Minimum in Rotated Sorted Array II
================================================
 Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
 (i.e.,
 `[0,1,2,4,5,6,7]` 
 might become
 `[4,5,6,7,0,1,2]` 
 ).
 Find the minimum element.
 The array may contain duplicates.
 Example 1:
```
Input: [1,3,5]
Output: 1
```
 Example 2:
```
Input: [2,2,2,0,1]
Output: 0
```
 Note:
* This is a follow up problem to
 Find Minimum in Rotated Sorted Array
 .
* Would allow duplicates affect the run-time complexity? How and why? -This affects the worst case complexity to be O(n) since the each iteration the input size at worst only shrink one step (A[mid] == A[right])
 Thoughts:
1. Handle duplicates: if (A[mid] == A[right], then A[mid] maintains the value and right can only reduce one.
 Code
```python
class Solution(object):
    def findMin(self, A):
        """
 :type A: List[int]
 :rtype: int
 """
        left, right = 0, len(A) - 1
        while left < right:
            mid = (right - left >> 1) + left
            if  A[mid] < A[right]:
                right = mid
            elif A[mid] > A[right]:
                left = mid + 1
            else:
                right -= 1
        return A[left] # left = right
```
------------------------------------------------------------------------------------------------
 153. Find Minimum in Rotated Sorted Array
=============================================
 Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
 (i.e.,
 `[0,1,2,4,5,6,7]` 
 might become
 `[4,5,6,7,0,1,2]` 
 ).
 Find the minimum element.
 You may assume no duplicate exists in the array.
 Example 1:
```
Input:[3,4,5,1,2] 
Output:1
```
 Example 2:
```
Input:[4,5,6,7,0,1,2]
Output:0
```
 Thoughts:
1. Binary Search:
	1. 1st method : To find the minimum, use the A[mid] to compare with
	 A[right]:
	2. 2nd method: To compare with A[left] and at the end compare the found result with start and end value (since this method would "assume there is a pivot")
 Code1:
```python
class Solution :
    public findMin(int[] A) :
        left = 0, right = A.length - 1
        while (left < right):
            mid = left + (right - left >> 1)
            if (A[mid] > A[right]):
                left = mid + 1
            else 
                right = mid
        return A[left]
```
 Code2:
```python
class Solution :
   # binary search
    public findMin(int[] A):
        i =0
        j=A.length-1
        start=A[i]
        end=A[j]
        while(i+1<j) :
            mid = i + (j - i) / 2
            if (A[mid] > A[i])
                i = mid
            else 
                j = mid
         #  min in (A[i] , A[j], start)
         return Math.min(Math.min(A[i], A[j]),start)
```
------------------------------------------------------------------------------------------------
 162. Find Peak Element in O(logn)
=====================================
 A peak element is an element that is greater than its neighbors.
 Given an input array
 `A` 
 , where
 `A[i] ≠ A[i+1]` 
 , find a peak element and return its index.
 The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
 You may imagine that
 `A[-1] = A[n] = -∞` 
 .
 Example 1:
```
Input:
A = [1,2,3,1]
Output: 2
Explanation:
 3 is a peak element and your function should return the index number 2.
```
 Example 2:
```
Input:
A = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation:
 Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
```
 Thoughts:
1. Using binary search to compare two midpoints, the larger one being the new searching boundary
 Code: Iterative
```python
class Solution :
public:
    findPeakElement(vector<int>& A) :
        low = 0, high = A.size()-1
        while(low< high):
            mid1 = (low + high)/2
            mid2 = mid1 + 1
            if(A[mid1] < A[mid2]):
                low = mid2
            else:
                high = mid1
        return low
```
 Code: Recursive:
```python
class Solution :
public:
    findPeakElement(vector<int>& A) :
        return binarySearch(A, 0, A.size()-1)
    binarySearch (vector<int>& A, low, high):
        if(low == high) return low #  binary search converges low and high points together in the very end
        mid1 = (low + high) /2
        mid2 = mid1 + 1
        if (A[mid1] > A[mid2]):
            return binarySearch(A, low, mid1)
        else :
            return binarySearch(A, mid2, high)
```
 from
 gangan
 's
 post
------------------------------------------------------------------------------------------------
 278. First Bad Version
==========================
 You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
 Suppose you have
 `n` 
 versions
 `[1, 2, ..., n]` 
 and you want to find out the first bad one, which causes all the following ones to be bad.
 You are given an API
 `bool isBadVersion(version)` 
 which will return whether
 `version` 
 is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
 Example:
```
Given n = 5, and version = 4 is the first bad version.
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```
 Code
```
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
 :type n: int
 :rtype: int
 """
        i , j = 1, n 
        while i <= j:
            mid = i + (j - i >> 1)
            if isBadVersion(mid):
                j = mid - 1
            else:
                i = mid + 1
        return i
```
------------------------------------------------------------------------------------------------
 378. Kth Smallest Element in a Sorted Matrix
================================================
 Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
 Note that it is the kth smallest element in the sorted order, not the kth distinct element.
 Example:
```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
```
 Note:
 You may assume k is always valid, 1 ≤ k ≤ n^2.
 Thoughts:
1. Heap:
	1. Build a minHeap of elements from the first row.
	2. Repeat for k - 1 times: poll out the current element from the queue, get its row and col number. if row is not at the end (n-1), push a new element at the same column, next row into the queue
	3. return the kth smallest value by pop out of the queue
2. Binary Search:
	1. binary search the
	 value
	 in matrix to get its rank on the matrix:
	2. if rank < k: low = mid + 1
	3. hi = mid
	4. return lo(or hi) in the end
 Code: Heap T: O(k*logn) S: O(n)
```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
 :type matrix: List[List[int]]
 :type k: int
 :rtype: int
 """
        n = len(matrix)
        pq = []
        for j in range(n):
            heapq.heappush(pq, Element(0, j, matrix[0][j]))
        for i in range(k - 1):
            e = heapq.heappop(pq)
            if e.row == n - 1: continue
            heapq.heappush(pq, Element(e.row + 1, e.col, matrix[e.row + 1][e.col]))
        return heapq.heappop(pq).val
class Element(object):
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
    def __lt__(self, other):
            return self.val < other.val
    def __eq__(self, other):
            return self.val == other.val
```
 Code: Binary Search: T:O(n*log(max - min))S: O(1)
```python
class Solution :
    public kthSmallest(int[][] matrix, k) :
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0
        m = matrix.length, n = matrix[0].length
        l = matrix[0][0], h = matrix[m - 1][n-1]
        while(l < h):
            mid = l + (h - l >> 1)
            cnt = 0, j = n - 1
            #  rank mid value in matrix
            for(i = 0 i < m i++):
                while(j >=0 && matrix[i][j] > mid) j -- #  since column is ascending
                cnt+= (j + 1)                    #  so matrix[i + 1][j] >= matrix[i][j] -> do not have to
                                                        #  reset j here
            if(cnt < k) l = mid + 1
            else h = mid
        return l #  or h
```
 Good Reference:
 https:# leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
------------------------------------------------------------------------------------------------
 LintCode 183. Wood Cut
==========================
### 
 183.Wood Cut
 Given n pieces of wood with length
 `L[i]` 
 (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
### 
 Example
 For
 `L=[232, 124, 456]` 
 ,
 `k=7` 
 , return
 `114` 
 .
### 
 Challenge
 O(n log Len), where Len is the longest length of the wood.
### 
 Notice
 You couldn't cut wood into float length.
 If you couldn't get >=_k _pieces, return
 `0` 
 .
 Thoughts:
1. Binary Search on the length by testing the resulted cutting pieces
 Code: T: Nlog(max(L[i])), S: O(1)
```python
public class Solution :
    /**
 * @param L: Given n pieces of wood with length L[i]
 * @param k: An integer
 * @return: The maximum length of the small pieces
 */
    public woodCut(int[] L, k) :
        #  write your code here
        l = 1, r = 0
        for (len : L):
            r = Math.max(r, len)
        if(k == 0) return r
        while (l <= r):
            mid = l + ((r - l) >> 1)
            if (count(L, mid) >= k) l = mid + 1
            else r = mid - 1
        #  if (count(L,l) >= k) return l
        if (count(L,r) >= k) return r
        return 0
    private count(int[] L, query):
        sum = 0
        if (query == 0) return 0 #  in case of dividing with 0
        for (len : L):
            sum+= len/query
        return sum
```
```
出来之后看的标准的做法是用二分法加greedy去找, N * log max 
当场想的办法是用dp, K^2 * N, 具体的思路就是： 
dp[i][j] = 把前0 - i 根木头切 j段的最大长度 j < k 
dp[i][j] = max(min(dp[i - 1][a], wood[i] / (j - a)) for a < j)
```
------------------------------------------------------------------------------------------------
 88. Merge Sorted Array
==========================
 Given two sorted integer arrays
 ---nums1 _and _nums2--- 
 , merge _nums2 _into _nums1 _as one sorted array.
 Note:
* The number of elements initialized in _nums1 _and _nums2 _are _m _and _n _respectively.
* You may assume that
 ---nums1 _has enough space (size that is greater or equal to _m--- 
 +
 ---n--- 
 ) to hold additional elements from
 ---nums2--- 
 .
 Example:
```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
```
 Thoughts:
1. To fill the nums1 in place, should fill the array backwards: start with the last on both arrays and fill the larger one between A[i] and A[j]
2. Code
```python
class Solution :
public:
    void merge(vector<int>& nums1, m, vector<int>& nums2, n) :
        i = m - 1, j = n - 1, tar = m + n - 1
        while (j >= 0) :
            nums1[tar--] = i >= 0 && nums1[i] > nums2[j] ? nums1[i--] : nums2[j--]
```
 Alternate version:
```python
class Solution :
    public void merge(int[] nums1, m, int[] nums2, n) :
        i = m - 1, j = n - 1, merge = m + n - 1
        #  System.out.println("i: " + i + " j: " + j)
        while(i >= 0 && j >=0):
            nums1[merge--] = nums1[i] > nums2[j]?nums1[i--]:nums2[j--]
        if (i< 0):
            #  fill j
            while(j>=0) nums1[merge--] = nums2[j--]
        if (j < 0):
            # fill i
            while(i>=0) nums1[merge--] = nums1[i--]
        return
```
------------------------------------------------------------------------------------------------
 209. Minimum Size Subarray Sum
==================================
 Given an array of
 n
 positive integers and a positive integer
 s
 , find the minimal length of a
 contiguous
 subarray of which the sum ≥
 s
 . If there isn't one, return 0 instead.
 Example:
```
Input:
s = 7, A = [2,3,1,2,4,3]
Output:2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```
 Follow up:
 If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(nlogn).
 Thoughts:
1. O(n): Having a left and right pointer, Scan through the array, if record the sum if arr[i...j] >=s, then compare min with current sum, then try to move left pointer up, then compare with min again.
2. O(nlogn) Binary Search:
 Code: O(n):
```python
class Solution :
    public minSubArrayLen(s, int[] A) :
        if(A == null || A.length == 0 ) return 0
        i = 0, j = 0 , sum = 0 , min = Integer.MAX_VALUE
        while(j < A.length):
            sum += A[j++]
            while(sum >=s):
                min = Math.min(min, j - i) # (old j) - i + 1 = j - i
                sum -= A[i++]
        return min == Integer.MAX_VALUE ? 0 : min
```
 Code: Another C++
```python
public class Solution :
    public minSubArrayLen(s, int[] A) :
        i = 0, j = 0, sum = 0, min = Integer.MAX_VALUE
        while (j < A.length) :
            while (sum < s && j < A.length) sum += A[j++]
            if(sum>=s):
                while (sum >= s && i < j) sum -= A[i++]
                min = Math.min(min, j - i + 1)
        return min == Integer.MAX_VALUE ? 0 : min
```
 Python
```python
class Solution(object):
    def minSubArrayLen(self, s, A):
        """
 :type s: int
 :type A: List[int]
 :rtype: int
 """
        i, j, pres, res = 0 , 0 , 0, len(A) + 1
        while j < len(A):
            pres += A[j] j += 1
            while pres >= s:
                res = min(res, j - i)
                pres -= A[i] i+= 1
        return res if res != len(A) + 1 else 0
```
 Code: O(nlogn)
 - search if a window of size k that satisfies the condition
```python
public class Solution :
    public minSubArrayLen(s, int[] A) :
        i = 1, j = A.length, min = 0
        while (i <= j) :
            mid = (i + j) / 2
            if (windowExist(mid, A, s)) :
                j = mid - 1
                min = mid
             else i = mid + 1
        return min
    private boolean windowExist(size, int[] A, s) :
        sum = 0
        for (i = 0 i < A.length i++) :
            if (i >= size) sum -= A[i - size]
            sum += A[i]
            if (sum >= s) return true
        return false
```
 Python
```python
class Solution(object):
    def minSubArrayLen(self, s, A):
        """
 :type s: int
 :type A: List[int]
 :rtype: int
 """
        i,j, res = 1, len(A), 0
        def windowExists(size): # for a fixed window size "size": whether there is window sum >= s
            acc = 0
            for i in range(len(A)):
                acc += A[i]
                if i >= size: acc -= A[i - size]
                if acc >= s:
                    return True
            return False
        while i <= j:
            mid = (j - i >> 1) + i
            if windowExists(mid):
                j = mid - 1
            else:
                i = mid + 1
        return i if i <= len(A) else 0
```
------------------------------------------------------------------------------------------------
 50. Pow(x,n)
================
### 
 50.Pow(x, n)
 Implement
 pow(
 ---x--- 
 ,
 ---n--- 
 )
 , which calculates
 ---x _raised to the power _n--- 
 (x^n).
 Example 1:
```
Input:
 2.00000, 10
Output:
 1024.00000
```
 Example 2:
```
Input:
 2.10000, 3
Output:
 9.26100
```
 Example 3:
```
Input:
 2.00000, -2
Output:
 0.25000
Explanation:
 2^-2 = 1/2
1/2^2 = 1/4 = 0.25
```
 Note:
* -100.0 <
 ---x--- 
 < 100.0
* n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
 Thoughts:
1. halve the exponent, squae the input
2. flip the sign of exponent if negative, then inverse the base
	1. if the exponent == INT_MIN change it to INT_MAX,
		1. if x is negative, change x to -x before finally inverse it
 Sequential Search: T: O(n)
```python
class Solution :
    public findPeakElement(int[] A) :
             for(i = 1 i < A.length i ++)
                :
                    if(A[i] < A[i-1])
                    :#  <
                        return i-1
            return A.length-1
```
```python
class Solution :
    public double myPow(double x, n) :
        if(n == 0) return 1
        if(n == 1) return x
        if (n<0):
            if(n == Integer.MIN_VALUE):
                n = Integer.MAX_VALUE
                if(x<0) x = -x
            else:
                n = -n
            x = 1/x
        return n%2==0?myPow(x*x,n/2):x*myPow(x*x,n/2)
```
------------------------------------------------------------------------------------------------
 240. Search a 2D Matrix II
==============================
 Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.
 Example:
 Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
 Given target =
 `5` 
 , return
 `true` 
 .
 Given target =
 `20` 
 , return
 `false` 
 .
 Thoughts:
1. O(mlogn) : iteratively search each row using binary search
2. O(m + n): start at the
 top right corner.
 If current number is smaller than target, increase the row number, if it is larger than the target number, decrease the column number, otherwise return False.
 Code
 O(mlogn):
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
 :type matrix: List[List[int]]
 :type target: int
 :rtype: bool
 """
        def bins(v, target):
            low, high = 0, len(v) - 1
            while(low <= high):
                mid = low + (high - low)/2
                if v[mid] > target:
                    high = mid - 1
                elif v[mid] < target:
                    low = mid + 1
                else:
                    return True
            return False
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        for i in range(m):
            if bins(matrix[i], target):
                return True
        return False
```
 Code
 O(m + n):
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
 :type matrix: List[List[int]]
 :type target: int
 :rtype: bool
 """
        m = len(matrix)
        if m == 0: 
            return False
        n = len(matrix[0])
        row , col = 0, n - 1 # top right
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row = row + 1
            else:
                # matrix[row][col] > target:
                col = col - 1
        return False
```
------------------------------------------------------------------------------------------------
 81. Search in Rotated Sorted Array II
=========================================
 Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
 (i.e.,
 `[0,0,1,2,2,5,6]` 
 might become
 `[2,5,6,0,0,1,2]` 
 ).
 You are given a target value to search. If found in the array return
 `true` 
 , otherwise return
 `false` 
 .
 Example 1:
```
Input: A = [2,5,6,0,0,1,2], target = 0
Output: true
```
 Example 2:
```
Input: A = [2,5,6,0,0,1,2], target = 3
Output: false
```
 Follow up:
* This is a
 follow up
 problem to
 Search in Rotated Sorted Array
 , where
 `A` 
 may contain duplicates.
* Would this affect the run-time complexity? How and why?
 Thoughts:
1. only change is to consider case where both num[i] == num[j] == num[mid]: (i.e [3,1,2,3,3,3]), we should both update i and j by 1.
2. Selecting the pivot: then compare the mid value with the pivot to decide which side is monotuous
 Code: T:(O(n) ~ O(logn))
```python
class Solution :
public:
    bool search(vector<int>& A, target) :
        i = 0
        j = A.size()-1
        while(i <= j):
            mid = i + (j - i >> 1)
            if (A[mid] == target) return true
            if (A[i] == A[mid] && A[j] == A[mid]):i++ j--
            else if (A[i] == A[mid] && A[j] != A[mid]) i = mid + 1
            else if(A[i] < A[mid]):
                if(A[i] <= target and A[mid] > target):
                    j = mid - 1
                else:
                    i = mid + 1
            else if (A[i] > A[mid]):
                if (A[mid] < target and A[j] >= target):
                    i = mid + 1
                else:
                    j = mid - 1
            else : 
                # 
        return false
```
 Python: Pivot
```python
class Solution(object):
     def search(self, A, target):
        # the most annoying case is duplicate pivoting value in the array!!!
        # [4,5,4,4,4,4,4]
        # [4,4,4,4,4,5,4]
        # when A[mid] == pivot, it's impposible to decide whether you should move the 
        # lower bound or upper bound
        if not A: return False
        pivot = A[0]
        if target == pivot: return True
        # !!key!! 
        # we move lo and hi so pivot will never equal to lo or hi
        lo, hi = 0, len(A) - 1
        while hi >= 0 and A[hi] == pivot:
            hi -= 1
        while lo <= len(A) - 1 and A[lo] == pivot:
            lo += 1
        # now we can just blindly copy the code from search-in-rotated-sorted-array-i
        while lo <= hi:
            mid = (hi - lo) #  2 + lo
            if A[mid] == target:
                return True
            if A[mid] < pivot:
                # mid is on the upper side
                if A[mid] < target < pivot:
                    lo = mid + 1
                else:
                    hi = mid - 1
            if A[mid] > pivot:
                if pivot < target < A[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return False
```
------------------------------------------------------------------------------------------------
 33. Search in Rotated Sorted Array
======================================
 33. Search in Rotated Sorted Array
====================================
 Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
 (i.e.,
 `[0,1,2,4,5,6,7]` 
 might become
 `[4,5,6,7,0,1,2]` 
 ).
 You are given a target value to search. If found in the array return its index, otherwise return
 `-1` 
 .
 You may assume no duplicate exists in the array.
 Your algorithm's runtime complexity must be in the order of
 ---O--- 
 (log
 ---n--- 
 ).
 Example 1:
```
Input:
A = [4,5,6,7,0,1,2], target = 0
Output: 4
```
 Example 2:
```
Input:
A = [4,5,6,7,0,1,2], target = 3
Output: -1
```
 Thoguths:
1. Binary search, find the continuous parts by comparing A[i] with A[mid],
2. Doing binary search inside: if it does not work, return -1
 Code:
```python
class Solution :
public:
    search(vector<int>& A, target) :
        i = 0
        j = A.size()-1
        while(i <= j):
            mid = i + (j - i >> 1)
            if (A[mid] == target) return mid
            if(A[i] < A[mid]):
                if(A[i] <= target and A[mid] > target):
                    j = mid - 1
                else:
                    i = mid + 1
            else if (A[i] > A[mid]):
                if (A[mid] < target and A[j] >= target):
                    i = mid + 1
                else:
                    j = mid - 1
            else :
                i= mid + 1 # A[i] = A[mid]
        return -1 
```
 Code: Java
```python
public search(int[] A, target) :
    return binarySearch(A,0,A.length-1,target)
private binarySearch(int[] A, left, right, target):
    if(left > right) return -1
    mid = (left + right)/2
    if(target == A[mid]) return mid
    if(target > A[mid]) :
        if(A[mid] < A[left] && target > A[right]):
            return binarySearch(A,left,mid-1,target)
        else :
            return binarySearch(A,mid+1,right,target)
    else:
        if(A[mid] > A[right] && target < A[left]):
            return binarySearch(A,mid+1,right,target)
        else :
            return binarySearch(A,left,mid-1,target)
```
 Code: C++
```python
class Solution :
public:
    search(vector<int>& A, ele) :
        l = 0, h = A.size()-1
        if(!A.size())
            return -1
        while(l<h) :
            mid = (l+h)/2
            if(A[l] <= A[mid]) :
                if(ele >= A[l] && ele <= A[mid]) 
                    h = mid
                else 
                    l = mid+1
            else :
                if(ele>= A[mid] && ele<=A[h])
                    l = mid
                else
                    h = mid-1
        return A[l]==ele?l:-1
```
------------------------------------------------------------------------------------------------
 862. Shortest Subarray with Sum at Least K
==============================================
 Return the
 length
 of the shortest, non-empty, contiguous subarray of
 `A` 
 with sum at least
 `K` 
 .
 If there is no non-empty subarray with sum at least
 `K` 
 , return
 `-1.` 
 Example 1:
```
Input: 
A = [1], K = 1
Output: 1
```
 Example 2:
```
Input: 
A = [1,2], K = 4
Output: -1
```
 Example 3:
```
Input: 
A = [2,-1,2], K = 3
Output: 3
```
 Note:
1. `1 <= A.length <= 50000`
2. `-10 ^ 5 <= A[i] <= 10 ^ 5`
3. `1 <= K <= 10 ^ 9`
 Thoughts:
1. Using Deque + keeping increasing order: only larger index in the queue can have larger sum value. We use cumulative sum and priority queue that maintains minimal value within the window of a given length. We then iterate over all possible ends of windows and check, what is the maximal possible sum across all windows of length l <= L that end at this element.
2. Segment Tree:
3. TreeMap.submap
4. Binary Search
 https:# buptwc.github.io/2018/07/02/Leetcode-862-Shortest-Subarray-with-Sum-at-Least-K/
  https:# leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C++JavaPython-O(N)-Using-Deque
  https:# leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/151169/my-solution-O(nlgn)-use-segment-tree
  https:# leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/144291/Java-TreeMap.submap-Solution
  https:# leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143828/Java-binary-search-O(NlogN\
 Code: Deque. O(n)
```python
class Solution :
public:
    shortestSubarray(vector<int>& A, K) :
        N = A.size(), res = N + 1
        vector<int> S (N + 1, 0)
        for(i = 0 i < N i++) S[i + 1] = S[i] + A[i]
        deque<int> d
        for(i = 0 i < N + 1 i++):
            while(d.size() > 0 && S[i] - S[d.front()] >= K):
                res = min(res, i - d.front()) 
                d.pop_front()
            #  keep the INCREASING order to keep the optimal result (index larger should have larger(equal) value in the queue)
            while(d.size() > 0 && S[i] <= S[d.back()]):
                d.pop_back()
            d.push_back(i)
        return res == N + 1? -1: res
```
 Code: Python
```python
class Solution:
    def shortestSubarray(self, A, K):
        """
 :type A: List[int]
 :type K: int
 :rtype: int
 """
        dp = [0] * (len(A) + 1)
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + A[i - 1]
        res = len(A) + 1
        #
        Q = collections.deque()
        for i in range(len(dp)):
            while Q and dp[i] - dp[Q[0]] >= K:
                res = min(res, i - Q.popleft())
            while Q and dp[i] < dp[Q[-1]]:
                Q.pop() # pop right
            Q.append(i)
        return res if res != len(A)+1 else -1
```
 Code: Java
```python
class Solution :
    public shortestSubarray(int[] A, K) :
        N = A.length, res = N + 1
        int[] S  = new int[N+ 1]
        for(i = 0 i < N i++) S[i + 1] = S[i] + A[i]
        Deque<Integer> d = new LinkedList()
        for(i = 0 i < N + 1 i++):
            while(d.size() > 0 && S[i] - S[d.peekFirst()] >= K):
                res = Math.min(res, i - d.pollFirst()) 
            #  keep the INCREASING order to keep the optimal result (index larger should have larger(equal) value in the queue)
            while(d.size() > 0 && S[i] <= S[d.peekLast()]):
                d.pollLast()
            d.offerLast(i)
        return res == N + 1? -1: res
```
 Code: Segment Tree:
```python
class Solution :
    struct node:
        s,e
        long long m # min
        node *left, *right
        node(s, e, long long m): s(s), e(e), m(m), left(0), right(0):
        ~node():
            if(left) delete left
            if(right) delete right
    node* build(vector<long long> &sums, l, r):
        node *root = new node(l,r, sums[l])
        if(l == r) return root
        root->left = build(A, l, (l+r)/2)
        root->right = build(A, (l + r)/2 + 1, r)
        root-> m = min(root->left->m, root->right-> m)
        return root
    query(node* root, l, r, k):
        if(l > r) return -1
      # It is possible to make such a check in linear time.
      # We use cumulative sum and priority queue that maintains minimal value within 
      # the window of a given length. We then iterate over all possible ends of windows and check, 
      # what is the maximal possible sum across all windows of lenght <= L that end at this element. 
        if(root -> s > r || root-> e < l || root-> m >k) return -1
        if(root-> s == root ->e && root->m <=k) return root->s
        rr = query(root-> right, l, r, k)
        if(rr == -1) return query(root->left, l, r, k)
        return rr
public:
    shortestSubarray(vector<int>& A, K) :
        n = A.size()
        vector<long long> sum(n)
        sum[0] = A[0]
        for (i = 1 i < n i++) sum[i] = sum[i - 1] + A[i]
        node * root = build(sum, 0, n - 1)
        ans= n +1
        for (i = 0 i < n i++):
            if(sum[i] >=K) ans = min(ans, i + 1)
            p = query(root, 0, i - 1, sum[i] -K) #  find sum[p]
            if(p!= -1) ans = min(ans, i- p)
        return ans == n+ 1? -1: ans
```
 Code: Java subMap
```
   public shortestSubarray(int[] A, K) :
        if (A.length == 0) return -1
        TreeMap<Long, Integer> map = new TreeMap()
        map.put(0L, -1) #  pay attention to the initial state
        long cumSum = 0 #  sum of range[0-->i]
        minLen = Integer.MAX_VALUE
        for (i = 0 i < A.length i++) :
            #  get cur cumSum
            cumSum += A[i]
            #  find all candidates and update res (firstKey() will throw exception if map is empty)
            Long lowestKey = map.firstKey(), floorKey = map.floorKey(cumSum - K)
            if (lowestKey != null && floorKey != null) :
                Map<Long, Integer> subMap = new HashMap(map.subMap(lowestKey, true, floorKey, true))
                for (Long key: subMap.keySet()) :
                    curLen = i - subMap.get(key)
                    if (minLen > curLen) minLen = curLen  #  update res
                    else map.remove(key)                  #  prune bad candidate
            #  put new cumSum to tree
            map.put(cumSum, i)
        return minLen == Integer.MAX_VALUE ? -1 : minLen
```
 Code: Java Binary Search
```python
class Solution :
    public shortestSubarray(int[] A, K) :
        N = A.length
        #  Compute cumulative sum
        int[] cumSum = new int[N]
        for (i = 0 i < N ++i) :
            cumSum[i] = i > 0 ? cumSum[i-1] + A[i] : A[i]
        if (!existsSolution(cumSum, K, N)) return -1
        #  Binary search over all possible lengths
        l = 1, r = N
        while (l < r) :
            m = l + (r-l) / 2
            if (existsSolution(cumSum, K, m)) :
                r = m
             else :
                l = m+1
        return l
    boolean existsSolution(int[] cumSum, K, len) :
        #  Priority queue that maintains minimal value within the window of size 'len'
        PriorityQueue<VI> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val))
        pq.add(new VI(0, -1))
        for (i = 0 i < cumSum.length ++i) :
            #  Clean up minimal elements that are outside of the window
            while (!pq.isEmpty() && pq.peek().pos < i-len) :
                pq.poll()
            windowMin = !pq.isEmpty() ? pq.peek().val : 0
            if (cumSum[i] - windowMin >= K) :
                return true
            pq.add(new VI(cumSum[i], i))
        return false
    public static class VI :
        public val, pos
        public VI(val, pos) :
            this.val = val
            this.pos = pos
```
------------------------------------------------------------------------------------------------
 410. Split Array Largest Sum
================================
 Given an array which consists of non-negative integers and an integerm, you can split the array intomnon-empty continuous subarrays. Write an algorithm to minimize the largest sum among thesemsubarrays.
 Note:
 Ifnis the length of array, assume the following constraints are satisfied:
* 1 ≤ n ≤ 1000
* 1 ≤ m ≤ min(50, n)
 Examples:
```
Input:
A = [7,2,5,10,8]
m = 2
Output:18
Explanation:
There are four ways to split A into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```
 Thoughts:
1. Binary search to query the minimum value of partition until converge. As per each partition size, there is a number of partition calculated. (
 Original post
 )
2. DP: dp[i][j] = min:max:dp[k][j-1], subsum(k + 1, i), 0 <= k < i (
 Original post
 )
3. DP: 1D state array with appropriate initialization direction: r from 2 to m, k is shared for the same r (cuts), decreasing from n-1 to r, i (subarray boundary) is decreasing frm n to r
 Code:
 Binary search through ranges of values.
 T: O(nlogn)
```python
class Solution :
public:
    splitArray(vector<int>& A, m) :
        max_val = 0 long sum = 0
        for (num : A):
            max_val = max(max_val, num)
            sum += num
        #  if (m == 1) return (int)sum
        long l = max_val , r = sum
        while(l <= r):
            mid = l + (r - l >> 1)
            if(valid_partition(mid, A, m)):
                r = mid - 1
            else l = mid + 1
        return (int)l
    bool valid_partition(target, vector<int>& A, m):
        count = 1 long total = 0
        for (num: A):
            total += num
            if (total > target):
                count ++
                total = num
                if (count > m) return false
        return true
```
 Code: DP T: O(n^2m)
```python
class Solution(object):
    def splitArray(self, A, m):
        """
 :type A: List[int]
 :type m: int
 :rtype: int
 """
        n = len(A)
        if not n: 
            return 0
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + A[i]
        sub_sum = lambda i, j: pre_sum[j + 1] - pre_sum[i]
        sub_cand = lambda k, j, i: max(dp[k][j], sub_sum(k + 1, i))
        # dp = [[0] * m for _ in range(n)]
        dp = [[0 for _ in range(m + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = pre_sum[i + 1]
            k = 0 
            for j in range(2, m + 1): # assume j <= i + 1
                # while k + 1 < i and max(dp[k][j - 1], sub_sum(k+1, i)) > max(dp[k + 1][j - 1], sub_sum(k + 2, i)):
                min_val = pre_sum[-1]
                for k in range(i + 1):
                    min_val = min(min_val, sub_cand(k, j - 1, i))
                dp[i][j] = min_val
        return dp[n - 1][m]
```
 Code: DP T: O(nm), S: O(n)
```python
class Solution(object):
    def splitArray(self, A, m):
        '''
 O(n) space
 '''
        n = len(A)
        sums = [0]
        for v in A:
            sums+= [sums[-1]+v]
        dp = list(sums)
        dp_cal = lambda j: max(dp[j], sums[i]-sums[j])
        for r in range(2, m + 1):
            k = n - 1
            for i in range(n, r - 1, -1):
                while k >= r and dp_cal(k-1) <= dp_cal(k):
                    k -= 1
                dp[i] = dp_cal(k)
        return dp[n]
```
```
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
# def guess(self, word):
# """
# :type word: str
# :rtype int
# """
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
 :type wordlist: List[Str]
 :type master: Master
 :rtype: None
 """
        match = lambda w1, w2: sum(i == j for i, j in zip(w1, w2))
        n = 0 
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if match(w1, w2) == 0)
            guess = min(wordlist, key = lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == n]
```
------------------------------------------------------------------------------------------------
 Flatten Binary Tree to Linked List
======================================
 Given a binary tree, flatten it to a linked list in-place.
 For example, given the following tree:
```
    1
   / \
  2   5
 / \   \
3   4   6
```
 The flattened tree should look like:
```
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
```
 Thoughts:
1. Post order (right first) + record prev node
2. d
 Code: Recursive
```
/**
 * Definition for a binary tree node.
 * public class TreeNode :
 * val
 * TreeNode left
 * TreeNode right
 * TreeNode(x) : val = x 
 * 
 */
class Solution :
    private TreeNode prev = null
    public void flatten(TreeNode root) :
        if (root == null) return
        flatten(root.right)
        flatten(root.left)
        root.right = prev
        root.left = null
        prev = root
```
 Code: Iterative: Using stack
```
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def flatten(self, root):
        """
 :type root: TreeNode
 :rtype: void Do not return anything, modify root in-place instead.
 """
        if not root: return
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            if stack:
                cur.right = stack[-1]
            cur.left = None
```
 Code: Iterative Traversal C++:
```
/**
 * Definition for a binary tree node.
 * struct TreeNode :
 * val
 * TreeNode *left
 * TreeNode *right
 * TreeNode(x) : val(x), left(NULL), right(NULL) :
 * 
 */
class Solution :
public:
    void flatten(TreeNode* root) :
        TreeNode* top = root
        while(top):
            if(top->left):
                TreeNode* pre = top->left
                while(pre -> right):
                    pre = pre->right
                pre->right = top -> right
                top -> right = top -> left
                top -> left = NULL
            top = top -> right
```
------------------------------------------------------------------------------------------------
 373. Find K Pairs with Smallest Sums
========================================
 You are given two integer arrays
 nums1
 and
 nums2
 sorted in ascending order and an integer
 k
 .
 Define a pair
 (u,v)
 which consists of one element from the first array and one element from the second array.
 Find the k pairs
 (u1,v1),(u2,v2) ...(uk,vk)
 with the smallest sums.
 Example 1:
```
Input: 
nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```
 Example 2:
```
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```
 Example 3:
```
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
```
 Thoughts:
1. Min Sum: min element from num1 and nums2. Smallest is definitely nums1[0] + num2[0]
2. Selecting the next candidate needs extra comparison: nums1[i] + nums2[j + 1] vs nums1[i + 1] + nums2[j], and then it also needs to compare the candidate.
3. Thus, use priority queue to maintain the order of the sums. In order to add duplicates, first offer k sums with nums1[i] + nums2[0] for i = 0,...k.
![](../assets/k pair smallest.png)
 Code: T:O(klogk) S: O(k)
```python
class Solution :
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, k) :
        List<[]> res = new ArrayList<>()
        if(nums1.length == 0 || nums2.length == 0 || k == 0) return res
        PriorityQueue<[]> pq = new PriorityQueue<>((a, b) -> a[0] + a[1] - b[0] - b[1])
        for(i = 0 i < nums1.length && i < k i++) pq.offer(new []:nums1[i], nums2[0], 0) #  end of nums1
        while(k-- > 0 && !pq.isEmpty()):
            [] cur = pq.poll()
            res.add(new int[]:cur[0], cur[1])
            if(cur[2] == nums2.length - 1) continue #  end of nums2
            pq.offer(new int[] :cur[0], nums2[cur[2] + 1], cur[2] + 1)
        return res
```
------------------------------------------------------------------------------------------------
 215. Kth Largest Element in an Array
========================================
 215. Kth Largest Element in an Array
======================================
 Find the
 k
 th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
 Example 1:
```
Input:
[3,2,1,5,6,4] and k = 2
Output:
 5
```
 Example 2:
```
Input:
[3,2,3,1,2,4,5,5,6] and k = 4
Output:
 4
```
 Note:
 You may assume k is always valid, 1 ≤ k ≤ array's length.
 Thoughts:
1. naive: sort and get: O(N lg N) running time + O(1) memory
2. use min heap: O(N lg K) running time + O(K) memory
3. selection algorithm (partition method): O(NlogN) best case / O(N^2) worst case running time + O(1) memory
4. Code 1. Naive:
```python
public findKthLargest(int[] A, k) :
        final N = A.length
        Arrays.sort(A)
        return A[N - k]
```
 Code 2. Min Heap:
```python
public findKthLargest(int[] A, k) :
    final PriorityQueue<Integer> pq = new PriorityQueue<>()
    for(val : A) :
        pq.offer(val)
        if(pq.size() > k) :
            pq.poll()
    return pq.peek()
```
 Code 2.1 Min Heap C++ (implementation: multiset)
```python
class Solution :
public:
    findKthLargest(vector<int>& A, k) :
        multiset<int> min_heap # min heap implemetation
        for (num : A):
            min_heap.insert(num)
            if(min_heap.size() > k) min_heap.erase(min_heap.begin())
        return *min_heap.begin()
```
 Code 2.2 Min Heap: Python
```python
class Solution(object):
    def findKthLargest(self, A, k):
        """
 :type A: List[int]
 :type k: int
 :rtype: int
 """
        pq = []
        for val in A:
            heapq.heappush(pq, val)
            if len(pq) > k:
                heapq.heappop(pq)
        return heapq.heappop(pq)
```
 Code 2.3 Max Heap: C++
```python
class Solution :
public:
    findKthLargest(vector<int>& A, k) :
        priority_queue<int> pq(A.begin(), A.end())
        for (i = 0 i < k - 1 i++):
            pq.pop() #  pop k - 1 times
        return pq.top()
```
 Code 2.3 Max Heap C++ (implementation: max_heapify)
```python
class Solution :
public:
    findKthLargest(vector<int>& A, k) :
        build_max_heap(A)
        #  swap max element to the end k - 1 times, then kth max is A[0]
        for (i = 0 i < k - 1 i++):
            swap(A[0], A[heap_size - 1])
            heap_size--
            max_heapify(A, 0)
        return A[0]
private:
    heap_size
    inline left_child(idx):
        return (idx << 1) + 1
    inline right_child(idx):
        return (idx << 1) + 2
    void max_heapify(vector<int>& A, idx):
        largest = idx, l = left_child(idx), r = right_child(idx)
        if (l < heap_size && A[l] > A[largest]) largest = l 
        if (r < heap_size && A[r] > A[largest]) largest = r 
        if (idx != largest):
            swap(A[idx], A[largest])
            max_heapify(A, largest) # percolate it down
    void build_max_heap(vector<int>&A):
        heap_size = A.size()
        for(i = (heap_size >> 1) - 1 i>= 0 i--):
            max_heapify(A, i)
```
 Code 3. Partition, QuickSelect:
```python
class Solution :
    public findKthLargest(int[] A, k) :
        k = A.length - k #  we are finding N - k th smallest
        low = 0, high = A.length - 1
        while(low < high):
            i = quickSelect(A, low, high)
            if(i < k):
                low = i + 1
            else if (i > k):
                high = i - 1
            else:
                break
        return A[k]
    private quickSelect([] A, low, high):
        i = low
        j = high + 1
        while(true):
            while(i < high && A[++i] < A[low])
            while(j > low && A[low] < A[--j])
            if(i >= j) break
            #  swap A[i] and A[j]
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
        #  swap pivot to the position j and return
        tmp = A[low]
        A[low] = A[j]
        A[j] = tmp
        return j
```
```python
class Solution :
    public findKthLargest(int[] A, k) :
        k = A.length - k #  we are finding N - k + 1 th smallest: [N - (k - 1)] - 1
        low = 0, high = A.length - 1
        while(low < high):
            i = quickSelect(A, low, high)
            #  System.out.println(low + " "+ high + " " + i + " " + k)
            if(i < k):
                low = i + 1
            else if (i > k):
                high = i - 1
            else:
                break
        return A[k]
    private quickSelect([] A, low, high):
        i = low + 1
        j = high
        #  take low as the pivot
        while(true):
            while(i <= j && A[i] <= A[low]) i++
            while(i <= j && A[low] <= A[j]) j--
            if(i > j) break
            #  swap A[i] and A[j]
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
        #  swap pivot to the position j and return
        tmp = A[low]
        A[low] = A[j]
        A[j] = tmp
        return j
```
 Python:
```python
class Solution(object):
    def findKthLargest(self, A, k):
        """
 :type A: List[int]
 :type k: int
 :rtype: int
 """
        def quickselect(A, low, high):
            i, j = low + 1, high 
            while True:
                while i <= j and A[i] <= A[low]: i+= 1
                while j >= i and A[j] >= A[low]: j-= 1
                if i > j: break
                # swap A[i], A[j]
                A[i], A[j] = A[j], A[i]
            # swap A[low], A[j]
            A[low], A[j] = A[j], A[low]
            return j
        n, k = len(A), len(A) - k
        low, high = 0, n - 1
        while low < high:
            i = quickselect(A, low, high)
            if i < k:
                low = i + 1
            elif i > k:
                high = i - 1
            else: break
        return A[k]
```
 So how can we improve the above solution and make it
 O(N) guaranteed (practically speaking)
 ? The answer is quite simple, we can
 randomize the input
 , so that even when the worst case input would be provided the algorithm wouldn't be affected. (Blum-Floyd-Pratt-Rivest-Tarjan algorithm) In practice , when the array is long enough. The possibility is almost zero.
------------------------------------------------------------------------------------------------
 253. Meeting Rooms II
=========================
 Given an array of meeting time intervals consisting of start and end times
 `[[s1,e1],[s2,e2],...]` 
 (si< ei), find the minimum number of conference rooms required.
 Example 1:
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
```
 Example 2:
```
Input: [[7,10],[2,4]]
Output:1
```
 Thoughts:
1. Sort the interval by the start time
2. Using the priority queue to use the end time as the order to sort the used classroom
3. pop the earliest ending meeting room, check if the time ends earlier than the start time of current class being scheduled, if earlier, merge the interval by setting the poped intervals'end time as the current intervals' scheduled end time, push the current interval into pq as making a new room.
4. return the size of the pq as the result
 Code
```
/**
 * Definition for an interval.
 * public class Interval :
 * start
 * end
 * Interval() : start = 0 end = 0 
 * Interval(s, e) : start = s end = e 
 * 
 */
class Solution :
    public minMeetingRooms(Interval[] intervals) :
        if(intervals ==null || intervals.length == 0) return 0
        #  sort the arrays by start time
        Arrays.sort(intervals, new Comparator<Interval>():
           @Override
            public compare(Interval a, Interval b) :return a.start - b.start
        )
        #  sort the heap by end time (scheduled meeting)
        PriorityQueue<Interval> pq = new PriorityQueue<Interval>(intervals.length, new Comparator<Interval>():
           @Override 
            public compare (Interval a, Interval b) :return a.end - b.end
        )
        pq.offer(intervals[0])
        for(i = 1 i < intervals.length i++):
            Interval earliest = pq.poll()
            Interval curInterval = intervals[i]
            if(earliest.end <= curInterval.start):
                earliest.end = curInterval.end #  merge (use the same room)
            else :
                pq.offer(curInterval) #  schedule a new room
            pq.offer(earliest)
        return pq.size()
```
 Python
```
# Definition for an interval.
# class Interval(object):
# def __init__(self, s=0, e=0):
# self.start = s
# self.end = e
class Solution(object):  
    def minMeetingRooms(self, intervals):
        events = [(it.start, +1) for it in intervals] + [(it.end, -1) for it in intervals]
        events = sorted(events)
        rooms = 0
        max_concurrent = 0
        for t, inc in events:
            rooms += inc
            max_concurrent = max(max_concurrent, rooms)
        return max_concurrent
```
------------------------------------------------------------------------------------------------
 23. Merge k Sorted Lists
============================
 Merge_k_sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
 Example:
```
Input:
[1->4->5, 1->3->4,2->6]
Output:
 1->1->2->3->4->4->5->6
```
 Thoughts:
1. With minheap:
	1. Use minheap to add in head elements first
	2. While heap is not empty, pull the least element o out, then if the next element of the o is not null, add it to the heap.
2. Iterative merging:
 Code: Priority Queue T:O(NlogN) Space: O(N)
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 * val
 * ListNode next
 * ListNode(x) : val = x 
 * 
 */
class Solution :
    public ListNode mergeKLists(ListNode[] lists) :
        if(lists == null || lists.length ==0) return null
        PriorityQueue<ListNode> queue= new PriorityQueue<ListNode>(lists.length, (n1, n2)-> n1.val - n2.val)
        ListNode dummy = new ListNode(0)
        ListNode cur = dummy
        for(ListNode node : lists):
            if (node != null)
                queue.add(node)
        while(!queue.isEmpty()):
            cur.next = queue.poll() # link
            cur = cur.next
            if(cur.next != null):   #  put successor in the queue
                queue.add(cur.next)   
        return dummy.next
```
 Code: Iterative Merging T:(NlogN) Space: O(1)
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 * val
 * ListNode next
 * ListNode(x) : val = x 
 * 
 */
class Solution :
    public ListNode mergeKLists(ListNode[] lists) :
        if(lists ==null || lists.length ==0) return null
        final n = lists.length
        for (b = 1 b < n b<<=1):
            for(low = 0 low + b < n low+= b<<1):
                lists[low]=mergeTwoLists(lists[low], lists[low + b])
        return lists[0]
    private ListNode mergeTwoLists(ListNode l1, ListNode l2):
        if(l1 == null) return l2
        if(l2 == null) return l1
        if(l1.val < l2.val):
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2
```
------------------------------------------------------------------------------------------------
 218. The Skyline Problem
============================
 A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are
 given the locations and height of all the buildings
 as shown on a cityscape photo (Figure A), write a program to
 output the skyline
 formed by these buildings collectively (Figure B).
 ![](../assets/skyline1.jpg)
![](../assets/skyline2.jpg)
 The geometric information of each building is represented by a triplet of integers
 `[Li, Ri, Hi]` 
 , where
 `Li` 
 and
 `Ri` 
 are the x coordinates of the left and right edge of the ith building, respectively, and
 `Hi` 
 is its height. It is guaranteed that
 `0 ≤ Li, Ri ≤ INT_MAX` 
 ,
 `0 < Hi ≤ INT_MAX` 
 , and
 `Ri - Li > 0` 
 . You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
 For instance, the dimensions of all buildings in Figure A are recorded as:
 `[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]` 
 .
 The output is a list of "
 key points
 " (red dots in Figure B) in the format of
 `[ [x1,y1], [x2, y2], [x3, y3], ... ]` 
 that uniquely defines a skyline.
 A key point is the left endpoint of a horizontal line segment
 . Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.
 For instance, the skyline in Figure B should be represented as:
 `[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]` 
 .
 Notes:
* The number of buildings in any input list is guaranteed to be in the range
 `[0, 10000]` 
 .
* The input list is already sorted in ascending order by the left x position
 `Li` 
 .
* The output list must be sorted by the x position.
* There must be no consecutive horizontal lines of equal height in the output skyline. For instance,
 `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` 
 is not acceptable the three lines of height 5 should be merged into one in the final output as such:
 `[...[2 3], [4 5], [12 7], ...]`
 Thoughts:
1. Pseudo Algorithm:
 Our final solution, then, in O(nlogn) time, is as follows. First, sort the critical points. Then scan across the critical points from left to right. When we encounter the left edge of a rectangle, we add that rectangle to the heap with its height as the key. When we encounter the right edge of a rectangle, we remove that rectangle from the heap. (This requires keeping external pointers into the heap.) Finally, any time we encounter a critical point, after updating the heap we set the height of that critical point to the value peeked from the top of the heap. from
 Brian Gordon
 's
 blog
2. dong.wang.1694
 's solution: The idea is to do line sweep and just process the buildings only at the start and end points. The key is to use a priority queue to save all the buildings that are still "alive". The queue is sorted by its height and end time (the larger height first and if equal height, the one with a bigger end time first). For each iteration, we first find the current process time, which is either the next new building start time or the end time of the top entry of the live queue. If the new building start time is larger than the top one end time, then process the one in the queue first (pop them until it is empty or find the first one that ends after the new building) otherswise, if the new building starts before the top one ends, then process the new building (just put them in the queue). After processing, output it to the resulting vector if the height changes. Complexity is the worst case O(NlogN). Not sure why my algorithm is so slow considering others' Python solution can achieve 160ms, any commments?
 here's the probable explanation
 .
3. Detailed Implementation from the
 post
 by
 StefanPochmann
 : a Python version with modification from
 dong.wang.1694's brilliant C++ solution
 . It sweeps from left to right. But it doesn't only keep
 ---heights_of "alive buildings" in the priority queue and it doesn't remove them as soon as their building is left behind. Instead, (height, right)_pairs_are kept in the priority queue and they stay in there as long as there's a larger height in there, not just until their building is left behind. In each loop, we first check what has the smaller x-coordinate: adding the next building from the input, or removing the next building from the queue. In case of a tie, adding buildings wins, as that guarantees correctness (think about it :-). We then either add all input buildings starting at that x-coordinate or we remove all queued buildings ending at that x-coordinate_or earlier--- 
 (remember we keep buildings in the queue as long as they're "under the roof" of a larger actually alive building). And then, if the current maximum height in the queue differs from the last in the skyline, we add it to the skyline.
 Code Python from
 StefanPochmann
```
from heapq import *
class Solution:
    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline
```
 Fastest Python Solution:
```python
class Solution(object):
    def getSkyline(self, buildings):
        """
 :type buildings: List[List[int]]
 :rtype: List[List[int]]
 """
        if len(buildings) == 0:
            return []
        import heapq
        h = []
        arr = []
        lower = buildings[0][0]
        def get_height():
            return 0 if len(h) == 0 else -h[0][0]
        for x1, x2, y in buildings:
            if y == 0:
                continue
            while h and h[0][1] < x1:
                a, b = heapq.heappop(h)
                if b > lower:
                    arr.append([lower, -a])
                    lower = b
            if lower < x1 and get_height() < y:
                arr.append([lower, get_height()])
                lower = x1
            while get_height() == y:
                x2 = max(x2, heapq.heappop(h)[1])
            heapq.heappush(h, (-y, x2))
        while h:
            a, b = heapq.heappop(h)
            if b > lower:
                arr.append([lower, -a])
                lower = b
        arr.append([lower, 0])
        return arr
```
 Code from Java: using segments with Priority Queue to solve the problem:
```python
class Solution :
    public List<int[]> getSkyline(int[][] buildings) :
        List<int[]> heights = new ArrayList<>()
        for([]b : buildings):
            #  adding two tuples, one with negative (rising edge) height 
            #  and the other with positive (falling edge)
            heights.add(new [] :b[0], -b[2])
            heights.add(new [] :b[1], b[2])
        Collections.sort(heights, (a,b)-> a[0] != b[0]?
                        a[0] - b[0]:
                        a[1] - b[1]
                        )
        #  max heap for heights
        Queue<Integer> pq = new PriorityQueue<>((a,b)->(b-a))
        pq.offer(0) #  insert 0 to prevent later buildinga from being poped out before right edges come
        prev = 0
        List<int[]> result = new ArrayList<>()
        for ([]h : heights):
            if(h[1]< 0):
                pq.offer(-h[1])
            else:
                pq.remove(h[1])
            #  check if top value in the pq is the critical point by checking whether there is a height change 
            #  using prev and current value
            cur = pq.peek()
            if(prev!= cur):
                result.add(new int[]:h[0], cur)
                prev = cur
        return result
```
------------------------------------------------------------------------------------------------
 692. Top K Frequent Words
=============================
 Given a non-empty list of words, return the k most frequent elements.
 Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
 Example 1:
```
Input:
 ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output:
 ["i", "love"]
Explanation:
 "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```
 Example 2
```
Input:
 ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output:
 ["the", "is", "sunny", "day"]
Explanation:
 "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```
 Note:
1. You may assume k is always valid, 1 ≤k ≤ number of unique elements.
2. Input words contain only lowercase letters.
 Follow up:
1. Try to solve it in O(nlogk) time and O(n) extra space.
 Thoughts:
1. Custom the sorting: first sort the count in descending order, then sort the name in ascending order
2. O(nlogk) time and O(n) extra space: using a heap to keep top k words in the heap
 Code: Sorting: T: O(nlogn) S: O(n)
```
 class Solution(object):
    def topKFrequent(self, words, k):
        """
 :type words: List[str]
 :type k: int
 :rtype: List[str]
 """
        d = collections.defaultdict(int)
        for word in words:
            d[str(word)] += 1
        # alternative ways to do that
        # d = collections.Counter(words)
        return [i[0] for i in sorted(d.items(), key = lambda x : (-x[1], x[0]))[:k]] # top K
        # return [w for w, v in sorted(collections.Counter(words).items(), key = lambda x: (-x[1], x[0])) [:k]]
```
 Code: Heap
```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
 :type words: List[str]
 :type k: int
 :rtype: List[str]
 """
        d = collections.defaultdict(int)
        for word in words:
            d[word] +=1
        queue = []
        for word, count in d.items():
            heapq.heappush(queue, Element(count, word))
            if len(queue) > k:
                heapq.heappop(queue)
        return [heapq.heappop(queue).word for _ in range(k)][::-1]
class Element(object):
    def __init__(self, count, word):
        self.word = word
        self.count = count
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    def __eq__ (self, other):
        return self.count == other.count and self.word == other.word
```
 Code: Heap Java:
```python
class Solution :
    public List<String> topKFrequent(String[] words, k) :
        List<String> res = new LinkedList<>() #  add front from min heap
        Map<String, Integer> map = new HashMap<>()
        for(i = 0 i < words.length i++):
            if(map.containsKey(words[i])):
                map.put(words[i], map.get(words[i])+ 1)
            else:
                map.put(words[i], 1)
        #  max heap
        PriorityQueue<Map.Entry<String, Integer>>pq = new PriorityQueue<>(
            (a,b) -> a.getValue() == b.getValue() ? b.getKey().compareTo(a.getKey()) :a.getValue() - b.getValue()
        )
        for (Map.Entry<String, Integer> entry: map.entrySet()):
            pq.offer(entry)
            if(pq.size()> k) pq.poll()
        while(!pq.isEmpty()):
            res.add(0, pq.poll().getKey()) #  only record the name
        return res
```
 Code: Heap C++
```python
class Solution :
public:
    vector<string> topKFrequent(vector<string>& words, k) :
        unordered_map<string, int> freq
        for(auto w : words):
            freq[w]++
        auto comp = [&](const pair<string,int>& a, const pair<string,int>& b) :
            return a.second > b.second || (a.second == b.second && a.first < b.first)
        #  typedef priority_queue<pair<string,int>, vector<pair<string,int>>, decltype(comp)> my_pq_t 
        priority_queue<pair<string,int>, vector<pair<string,int>>, decltype(comp)> pq(comp) #  element, container, comparison
        for(auto w : freq ):
            pq.emplace(w.first, w.second)
            if(pq.size()>k) pq.pop()
        vector<string> res
        while(!pq.empty()):
            res.insert(res.begin(), pq.top().first)
            pq.pop()
        return res
```
------------------------------------------------------------------------------------------------
 537. Erect the Fence (Convex Hull Problem)
==============================================
 537. Erect the Fence
======================
 here are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the
 minimum length
 of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.
 Example 1:
```
Input:
 [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output:
 [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:
```
![](../assets/import.png)
 Example 2:
```
Input:
 [[1,2],[2,2],[4,2]]
Output:
 [[1,2],[2,2],[4,2]]
Explanation:
```
![](../assets/import2.png)
`Even you only have trees in a line, you need to use rope to enclose them.` 
 Note:
1. All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
2. All input integers will range from 0 to 100.
3. The garden has at least one tree.
4. All coordinates are distinct.
5. Input points have
 NO
 order. No order required for output.
 Thoughts:
1. Find the next convex "base" point, expand the co-linear points with it by using the
 Cross Product. (reason)
2. Repeat doing this until the graph traverses back to the original point.
3. This is essentially
 Jarvis'algorithm (or wrapping)
 with co-linear checks. (Other ways to solve convex Hull include
 Graham Scan
 ,
 Simple Divide and Conquer Algorithm
 , and )
4. Time Complexity of three Algorithm:
| Jarvis | Graham Scan | Andrew's Monotone Chain | Divide and Conquer |
| :--- | :--- | :--- | :--- |
| O(n^2) |
 O(nlogn)
 |
 O(nlogn)
 | O(n^3) |
 Note: Cross Product = 0 <=> 1. there is a zero vector (current point reaches the base point) 2. two vectors are parallel (or anti-parallel, the angle between is either 0 or 180 degree)
 Code Monotone Chain:
```
1. sort points based on the x value as first priority, then y value
2. build the lower hull: compare the cross product of second_last, last and current point, if negative, means the
previous vec made the clockwise turn, at which we should get rid of the last value as it is not a eligible vertex.
3. build the upper hull: repeat the step 2 with reversely traversing the vector.
```
```python
class Solution :
public:
    orientation(Point &p, Point &q, Point &r) :
        return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    vector<Point> outerTrees(vector<Point>& points) :
        if (points.size() <= 3)
            return points
        # sort lexicographically
        sort(points.begin(), points.end(), [](Point &p, Point &q) :
            return p.x < q.x || (p.x == q.x && p.y < q.y)
        )
        vector<Point> ans
        # lower hull 
        for (i = 0 i < points.size() ++i) :
            while (ans.size() >= 2 && orientation(ans[ans.size() - 2], ans[ans.size() - 1], points[i]) < 0)
                ans.pop_back()
            ans.push_back(points[i])
        #  remove the last point as it will be included in the upper hull
        ans.pop_back()
        #  upper hull
        for (i = points.size() - 1 i >= 0 --i) :
            while (ans.size() >= 2 && orientation(ans[ans.size() - 2], ans[ans.size() - 1], points[i]) < 0)
                ans.pop_back()
            ans.push_back(points[i])
        #  remove the last point as it was included as the first point explored
        ans.pop_back()
        return ans
```
 Other two comparable solutions:
 1
 ,
 2
 .
```python
class Solution :
public:
    vector<Point> outerTrees(vector<Point>& points) :
        #  Andrew's monotone chain method
        n = points.size()
        vector<Point> ans
        sort(points.begin(), points.end(), mycompare)
        #  left to right
        for (i = 0 i < n ++i) :
            while (ans.size() > 1 && orientation(ans[ans.size()-2], ans.back(), points[i]) < 0) 
                ans.pop_back()
            ans.push_back(points[i])
        #  if all points along a line, ans.size() is n after left to right procedure
        if (ans.size() == n) return ans
        #  right to left
        for (i = n-2 i >= 0 --i) :
            while (ans.size() > 1 && orientation(ans[ans.size()-2], ans.back(), points[i]) < 0) 
                ans.pop_back()
            ans.push_back(points[i])
        ans.pop_back()
        return ans
private:
    static bool mycompare(Point& a, Point& b) :
        return a.x < b.x || (a.x == b.x && a.y < b.y)
    orientation(Point& a, Point& b, Point& c) :
        return (b.x-a.x)*(c.y-b.y) - (b.y-a.y)*(c.x-b.x)
```
```
     vector<Point> outerTrees(vector<Point>& points) :
        if(points.size() < 3) return points
        auto cmp = [](Point& a, Point& b) -> bool :
            return a.x < b.x || (a.x == b.x && a.y < b.y)
        sort(points.begin(), points.end(), cmp)
        vector<Point> stack
        stack.push_back(points[0])
        stack.push_back(points[1])
        # left to right
        for(i = 2 i < points.size() ++i) :
            while(stack.size() > 1) :
                auto &t1 = stack.back()
                auto &t2 = stack[stack.size() - 2]
                if(isRightTurn(t2, t1, points[i])) break
                else stack.pop_back()
            stack.push_back(points[i])
        n = stack.size()
        if(n == points.size()) return stack # check if linear
        stack.push_back(points[points.size() - 2])
        # right to left
        for(i = points.size() - 3 i >= 0 --i) :
            while(stack.size() > n) :
                auto &t1 = stack.back()
                auto &t2 = stack[stack.size() - 2]
                if(isRightTurn(t2, t1, points[i])) break
                else stack.pop_back()
            stack.push_back(points[i])
        stack.pop_back()
        return stack
    bool isRightTurn(Point &a, Point &b, Point &c) :
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) <= 0
```
 Code Monotone Chain (Python):
```
def outerTrees(self, A):
    def sign(p, q, r):
        return cmp((p.x - r.x)*(q.y - r.y), (p.y - r.y)*(q.x - r.x))
    def drive(hull, r):
        hull.append(r)
        while len(hull) >= 3 and sign(*hull[-3:]) < 0:
            hull.pop(-2)
        return hull
    A.sort(key = lambda p: (p.x, p.y))
    lower = reduce(drive, A, [])
    upper = reduce(drive, A[::-1], [])
    return list(set(lower + upper))
```
 Code Graham Scan:
```
1)Find the bottom-most point by comparing y coordinate of all points. If there are two points with same y value, then the point with smaller x coordinate value is considered. Let the bottom-most point be P0. Put P0 at first position in output hull.
2)Consider the remaining n-1 points and sort them by polor angle in counterclockwise order around points[0]. If polor angle of two points is same, then put the nearest point first.
3After sorting, check if two or more points have same angle. If two more points have same angle, then remove all same angle points except the point farthest from P0. Let the size of new array be m.
4)If m is less than 3, return (Convex Hull not possible)
5)Create an empty stack ‘S’ and push points[0], points[1] and points[2] to S.
6)Process remaining m-3 points one by one. Do following for every point ‘points[i]’
4.1)Keep removing points from stack while
orientation
of following 3 points is not counterclockwise (or they don’t make a left turn).
            a) Point next to top in stack
            b) Point at the top of stack
            c) points[i]
4.2)Push points[i] to S
5)Print contents of S
```
```
/**
 * Definition for a point.
 * struct Point :
 *     x
 *     y
 *     Point() : x(0), y(0) :
 *     Point(a, b) : x(a), y(b) :
 * 
 */
class Solution :
    struct pointsComparator:
        Point p0
        bool operator() (const Point & p1, const Point& p2):
            o = orientation(p0, p1, p2)
            if(o == 0) return distSq(p0, p2)>= distSq(p0, p1)
            return o == 2
        pointsComparator(Point p): p0(p):
#      compare(const void *vp1, const void *vp2):
#          Point *p1 = (Point *) vp1
#          Point *p2 = (Point *) vp2
#      
    static distSq(Point p1, Point p2) :
        return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)
   static orientation(Point a, Point b, Point c):
        val = (b.x - a.x)*(c.y-b.y) - (b.y - a.y)*(c.x - b.x)
        if(val == 0) return 0
        return (val > 0)? 2:1
    #  Point nextTotop(stack<Point> &s):
    #      Point p = s.top()
    #      s.pop()
    #      Point res = s.top()
    #      s.push(p)
    #      return res
    #  
    #  void swap(Point &p1, Point& p2):
    #       Point temp = p1
    #       p1 = p2
    #       p2 = temp
    #  
public:
  vector<Point> outerTrees(vector<Point> points) :
        n = points.size()
        if (n <= 3) :
            return points
        #  Find the bottommost point
        ymin = points[0].y, min = 0
        for (i = 1 i < n i++) :
            y = points[i].y
            #  Pick the bottom-most or chose the left most point in case of tie
            if ((y < ymin) || (ymin == y && points[i].x < points[min].x)) :
                ymin = points[i].y, min = i
        #  Place the bottom-most point at first position
        Point temp = points[0]
        points[0] = points[min]
        points[min] = temp
        #  Sort n-1 points with respect to the first point.
        #  A point p1 comes before p2 in sorted ouput 
        #  if p2 has larger polar angle (in counterclockwise direction) than p1
        #  In the tied case, the one has smaller distance from p0 comes first
        Point p0 = points[0]
        sort(points.begin(), points.end(), pointsComparator(p0))
        # As we need to output all the vertices instead of extreme points
        # We need to sort the points with the same largest polar angle w.r.p. p0 in another way to break tie
        # Closer one comes last
        Point pn = points.back()        
        if (orientation(p0, points[1], pn) != 0) :
            idx = n-1
            while (orientation(p0, points[idx], pn) == 0) :
                idx--
            reverse(points.begin() + idx + 1, points.end())
        #  Create an empty stack and push first three points to it.
        vector<Point> vertices
        vertices.push_back(points[0])
        vertices.push_back(points[1])
        vertices.push_back(points[2])
        #  Process remaining n-3 points
        for (i = 3 i < n i++) :
            #  Keep removing top while the angle formed by
            #  points next-to-top, top, and points[i] makes a right (in clockwise) turn
            while (orientation(vertices[vertices.size() - 2], vertices.back(), points[i]) == 1) :
                vertices.pop_back()
            vertices.push_back(points[i])
        return vertices
```
 Code Javis's Algorithm
 (Java)
```python
public class Solution :
    public List<Point> outerTrees(Point[] points) :
        Set<Point> result = new HashSet<>()
        #  Find the leftmost point
        Point first = points[0]
        firstIndex = 0
        for (i = 1 i < points.length i++) :
            if (points[i].x < first.x) :
                first = points[i]
                firstIndex = i
        result.add(first)
        Point cur = first
        curIndex = firstIndex
        do :
            Point next = points[0]
            nextIndex = 0
            for (i = 1 i < points.length i++) :
                if (i == curIndex) continue
                cross = crossProductLength(cur, points[i], next)
                if (nextIndex == curIndex || cross > 0 ||
                        #  Handle collinear points
                        (cross == 0 && distance(points[i], cur) > distance(next, cur))) :
                    next = points[i]
                    nextIndex = i
            #  Handle collinear points
            for (i = 0 i < points.length i++) :
                if (i == curIndex) continue
                cross = crossProductLength(cur, points[i], next)
                if (cross == 0) :
                    result.add(points[i])
            cur = next
            curIndex = nextIndex
         while (curIndex != firstIndex)
        return new ArrayList<Point>(result)
    private crossProductLength(Point A, Point B, Point C) :
        #  Get the vectors' coordinates.
        BAx = A.x - B.x
        BAy = A.y - B.y
        BCx = C.x - B.x
        BCy = C.y - B.y
        #  Calculate the Z coordinate of the cross product.
        return (BAx * BCy - BAy * BCx)
    private distance(Point p1, Point p2) :
        return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)
```
 Special Thanks to
 shawngao
 's
 solution
 and
 solution
 by
 GeeksforGeeks
 ,
 lee215
 and
 aeonaxx
 for providing Monotone Chain
 Solution
 and equivalent
 Python solution
 by
 awice
 , along with alternative solution
 1
 by
 zestypanda
 , and
 2
 by
 hwf
 .
------------------------------------------------------------------------------------------------
 Sliding Window Median
=========================
 480. Sliding Window Median
============================
 Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
 Examples:
`[2,3,4]` 
 , the median is
 `3` 
`[2,3]` 
 , the median is
 `(2 + 3) / 2 = 2.5` 
 Given an array
 ---A--- 
 , there is a sliding window of size
 ---k _which is moving from the very left of the array to the very right. You can only see the k--- 
 numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.
 For example,
 Givennums=
 `[1,3,-1,-3,5,3,6,7]` 
 , andk= 3.
```
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
```
 Therefore, return the median sliding window as
 `[1,-1,-1,3,5,6]` 
 .
 Thoughts:
 Keep the window elements in a multiset and keep an iterator pointing to the middle value (to “index” k/2, to be precise).
 Code
```python
class Solution :
public:
    vector<double> medianSlidingWindow(vector<int>& A, k) :
        multiset<int> window(A.begin(), A.begin() + k)
        auto mid = next(window.begin(), k/2)
        vector<double> medians
        for(i = k  i++):
            #  push current median
            medians.push_back((double(*mid) + *prev(mid, 1 - k%2))/2)
            if(i == A.size()) return medians
            window.insert(A[i])
            if(A[i] < *mid) mid -- #  no equal here because if inserted value is equal to that of mid, the newly 
            #  inserted one actually comes AFTER the mid. 
            if(A[i-k] <= *mid) mid++
            window.erase(window.lower_bound(A[i-k]))
```
 Special Thanks to
 stefanpochmann
 's
 repost
 from
 @votrubac’s solution and comments
 .
------------------------------------------------------------------------------------------------
 445. Add Two Numbers II
===========================
 You are given two
 non-empty
 linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 Follow up:
 What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
 Example:
```
Input:(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```
 Thoughts:
1. Reversing the linkedList
2. Using a stack
 Code: Reversing the LinkedList
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 * val
 * ListNode next
 * ListNode(x) : val = x 
 * 
 */
class Solution :
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) :
        ListNode n1 = reverse(l1), n2 = reverse(l2)
        carry = 0
        ListNode temp = n1, pre = n1
        while((n1 != null) || (n2 != null) || (carry !=0)):
            v1 = n1 == null? 0 : n1.val
            v2 = n2 == null? 0 : n2.val
            if(n1 == null):
                n1 = new ListNode((v1 + v2 + carry)%10)
                pre.next = n1
            else :
                n1.val = (v1 + v2 + carry)%10
            carry = (v1 + v2 + carry) /10
            pre = n1
            n1 = n1 == null? null : n1.next
            n2 = n2 == null? null : n2.next
        return reverse(temp)
    private ListNode reverse(ListNode l1):
        ListNode cur = l1.next
        ListNode pre = l1
        pre.next = null
        while(cur!= null):
            ListNode next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
```
 Code: Using a stack
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 * val
 * ListNode next
 * ListNode(x) : val = x 
 * 
 */
class Solution :
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) :
        Stack<Integer> s1 = new Stack<>()
        Stack<Integer> s2 = new Stack<>()
        while(l1 != null):
            s1.push(l1.val)
            l1 = l1.next
        while(l2 != null):
            s2.push(l2.val)
            l2 = l2.next
        sum = 0
        ListNode cur = new ListNode(0)
        while(!s1.isEmpty() || !s2.isEmpty()):
            if(!s1.isEmpty()) sum += s1.pop()
            if(!s2.isEmpty()) sum += s2.pop()
            cur.val = sum%10
            ListNode head = new ListNode(sum/10)
            head.next = cur #  reconstruct
            cur = head#  moving on
            sum/=10
        return cur.val == 0? cur.next: cur
```
------------------------------------------------------------------------------------------------
 138. Copy List with Random Pointer
======================================
 138. Copy List with Random Pointer
====================================
 A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
 Return a deep copy of the list.
 Thoughts
 :
 O(n) time complexity, O(n) space Complexity
1. Make deep copy of each node by tying right after each node
2. Copy random pointer
3. Extract the copy list and restore the original list
 Code: without dummy node (copyHead at head->next)
```
/**
* Definition for singly-linked list with a random pointer.
* struct RandomListNode :
* label
* RandomListNode *next, *random
* RandomListNode(x) : label(x), next(NULL), random(NULL) :
* 
*/
class Solution :
public:
    RandomListNode *copyRandomList(RandomListNode *head) :
        if(!head) return nullptr
        RandomListNode* cur = head, *next
        #  copying each node right after the current node
        while(cur):
            next = cur->next
            RandomListNode* copyNode = new RandomListNode(cur->label)
            cur->next = copyNode
            copyNode -> next = next
            cur = next
        #  copying random pointer
        cur = head
        while(cur):
            next = cur -> next -> next
            if(cur->random)
            cur->next->random = cur->random->next #  cur->random->next is the copy of corresponding random node
            #  for the current node in original linked list
            cur = next
        #  extract copy list and restore original list
        cur = head
        RandomListNode *copyHead = head->next, *copyIter = copyHead
        while(cur):
            next = cur -> next -> next
            if(next) copyIter->next = next -> next
            copyIter = copyIter->next
            cur->next = next
            cur = next
        return copyHead
```
 Code: with dummy node (copyHead->next is the head->next): This one does not have to check null
 T: O(n) S: O(1)
 The algorithm is composed of the follow three steps which are also 3 iteration rounds.
1. Iterate the original list and duplicate each node. The duplicate of each node follows its original immediately.
2. Iterate the new list and assign the random pointer for each duplicated node.
3. Restore the original list and extract the duplicated nodes.
```
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode :
 * label
 * RandomListNode *next, *random
 * RandomListNode(x) : label(x), next(NULL), random(NULL) :
 * 
 */
class Solution :
public:
    RandomListNode *copyRandomList(RandomListNode *head) :
        RandomListNode* cur = head, *next
        #  copying each node right after the current node 
        while(cur):
            next = cur->next
            RandomListNode* copyNode = new RandomListNode(cur->label)
            cur->next = copyNode
            copyNode -> next = next
            cur = next
        #  copying random pointer
        cur = head
        while(cur):
            next = cur -> next -> next
            if(cur->random)
                cur->next->random = cur->random->next #  cur->random->next is the copy of corresponding random node 
                                                        #  for the current node in original linked list
            cur = next
        #  extract copy list and restore original list
        cur = head
        RandomListNode * dummyHead = new RandomListNode(0), *copyIter = dummyHead
        while(cur):
            next = cur -> next -> next
            copyIter->next = cur -> next
            copyIter = copyIter->next
            cur->next = next
            cur = next
        return dummyHead->next
```
 Code: Copy everything from the dictionary. Space O(n)
```
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
# def __init__(self, x):
# self.label = x
# self.next = None
# self.random = None
class Solution(object):
    def copyRandomList(self, head):
        """
 :type head: RandomListNode
 :rtype: RandomListNode
 """
        # set the default value to be changed later using collections.defaultdict ()
        mapping = collections.defaultdict(lambda: RandomListNode(0))
        # set the None identity mapping 
        mapping[None] = None
        cur = head
        while cur:
            mapping[cur].label = cur.label
            mapping[cur].next = mapping[cur.next]
            mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]
```
 Special Thanks to
 liaison
 's solution for the reference
------------------------------------------------------------------------------------------------
 237. Delete Node in a Linked List
=====================================
 237. Delete Node in a Linked List
===================================
 Write a function to delete a node (except the tail) in a singly linked list,
 given only access to that node
 .
 Supposed the linked list is
 `1 -> 2 -> 3 -> 4` 
 and you are given the third node with value
 `3` 
 , the linked list should become
 `1 -> 2 -> 4` 
 after calling your function.
 Thoughts:
1. Copy the
 node value
 of the next node to the
 current node
2. Optional: free the next node
 Code
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    void deleteNode(ListNode* node) :
        *node = *node->next
```
 Code (freeing space)
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    void deleteNode(ListNode* node) :
        auto next = node -> next
        *node = *next
        delete next
```
 Code (Java / C#)
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 *     val
 *     ListNode next
 *     ListNode(x) : val = x 
 * 
 */
class Solution :
    public void deleteNode(ListNode node) :
        node.val = node.next.val
        node.next = node.next.next
```
 Code (Python)
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next= node.next.next
```
 Code (JavaScript)
```
var deleteNode = function(node) :
    node.val = node.next.val
    node.next = node.next.next
```
 Code (Ruby)
```
# Definition for singly-linked list.
# class ListNode
# attr_accessor :val, :next
# def initialize(val)
# @val = val
# @next = nil
# end
# end
# @param :ListNode node
# @return :Void Do not return anything, modify node in-place instead.
def delete_node(node)
    node.val = node.next.val
    node.next = node.next.next
end
```
 Special Thanks to
 stefanpochmann
 's
 solution
 for the reference
------------------------------------------------------------------------------------------------
 708. Insert into a Cyclic Sorted List
=========================================
 Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to_any_single node in the list, and may not be necessarily the smallest value in the cyclic list.
 If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.
 If the list is empty (i.e., given node is
 `null` 
 ), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.
 The following example may help you understand the problem better:
![](https:# leetcode.com/static/images/problemset/InsertCyclicBefore.png)
 In the figure above, there is a cyclic sorted list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list.
![](https:# leetcode.com/static/images/problemset/InsertCyclicAfter.png)
 The new node should insert between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
 Thoughts:
1. No head:
2. prev.val <= val <= cur.val
3. prev.val > cur.val and (val < cur.val or prev.val < cur): cur is either the min or the max with
 not all nodes with the same value
4. val != every nodes's value in a cyclic linked list where every node has the same value
 Code
```
"""
# Definition for a Node.
class Node(object):
 def __init__(self, val, next):
 self.val = val
 self.next = next
"""
class Solution(object):
    def insert(self, head, val):
        """
 :type head: Node
 :type insertVal: int
 :rtype: Node
 """
        node = Node(val, head)
        # case 1 no head
        if not head:
            return node
        prev, cur = head, head.next
        while 1:
            # case 2: prev.val <= val <= cur.val
            if prev.val <= val <= cur.val:
                break
            # case 3: prev.val > cur.val and val < cur.val or prev.val < cur
            elif prev.val > cur.val and (val <= cur.val or prev.val <= val):
                break
            prev, cur = prev.next, cur.next
            # case 4: prev == head
            if prev == head: # in case of all nodes have same value that are > val 
                break
        # insert node between prev and cur
        prev.next = node
        node.next = cur
        return head
```
------------------------------------------------------------------------------------------------
 160. Intersection of Two Linked Lists
=========================================
 Write a program to find the node at which the intersection of two singly linked lists begins.
 For example, the following two linked lists:
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```
 begin to intersect at node c1.
 Notes:
* If the two linked lists have no intersection at all, return
 `null` 
 .
* The linked lists must retain their original structure after the function returns.
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.
 Credits:
 Special thanks to
 @stellari
 for adding this problem and creating all test cases.
 Thoughts:
1. Having two traversors traverse two lists separately, the total path they travel will be equal. And if a in the first round first gets the end, b will catch up with exactly shorter distance in the second round. So if there is a intersection and even two lists are not of the same length, swapping the end/ starting point in the second round will make sure they will have the same distance to the end point in the second round.
 Code
```
# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
 :type head1, head1: ListNode
 :rtype: ListNode
 """
        if not headA or not headB: return None
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```
------------------------------------------------------------------------------------------------
 142. Linked List Cycle II
=============================
 142. Linked List Cycle II
===========================
 Given a linked list, return the node where the cycle begins. If there is no cycle, return
 `null` 
 .
 Note:
 Do not modify the linked list.
 Follow up
 :
 Can you solve it without using extra space?
 Thoughts
1. Having two pointers: slow vs fast. When two first meets, note slow has gone
 k
 steps. So for the faster pointer, which is ahead of slow pointer exactly the length of cycle,
 r
 . Since faster at that moment can be counted as
 2k steps
 . Then 2k = k + r =>
 k = r.
 Also, note
 s
 as the distance between the start node of the list and the start node of the cycle,
 m
 as the distance between the start node of cycle and the first meeting node.
 k = s + m => s = k - m = r - m (the rest distance to finish the cycle, or the distance to REACH the start node of the cycle).
2. Solution: use
 hasCycle
 to detect whether there is an cycle. if there is an cycle, reset the slow pointer to the head then both move slow and fast one step each time until they first meet. The node they meet is the answer.
 Code
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
      ListNode *detectCycle(ListNode *head) :
        if (head == NULL || head->next == NULL) return NULL
        ListNode* slow = head
        ListNode* fast = head
        bool isCycle = false
        while(fast->next && fast->next->next):
            slow = slow ->next 
            fast = fast ->next -> next
            if(slow == fast) :isCycle =true break
        if(!isCycle) return NULL
        slow = head
        while( slow != fast) :
            slow = slow->next
            fast = fast->next
        return slow
```
 Special Thanks
 wall0p
 's
 Ideas + Solution
------------------------------------------------------------------------------------------------
 141. Linked List Cycle
==========================
 141. Linked List Cycle
========================
 Given a linked list, determine if it has a cycle in it.
 Follow up:
 Can you solve it without using extra space?
 Thoughts:
1. slow and fast pointer
2. Change the value of the node (mark)
 Code 1
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    bool hasCycle(ListNode *head) :
        if (!head) return false
        ListNode* slow = head, *fast = head
        while(fast->next && fast->next->next):
            slow = slow->next
            fast = fast->next->next
            if(slow == fast) return true
        return false
```
 Code 1 Using Exception (Python)
```
# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
 :type head: ListNode
 :rtype: bool
 """
        try:    
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
```
 Code 2 (Java)
```
/**
 * Definition for singly-linked list.
 * class ListNode :
 * val
 * ListNode next
 * ListNode(x) :
 * val = x
 * next = null
 * 
 * 
 */
public class Solution :
    public boolean hasCycle(ListNode head) :
    return head!=null && (head.val == (head.val = 0xcafebabe) || hasCycle(head.next))
```
------------------------------------------------------------------------------------------------
 23. Merge K Sorted Lists
============================
 23. Merge K Sorted Lists
==========================
 Merge k sorted linked lists and return it as one sorted list. Analyze and describe its
 complexity
 .
 Thoughts:
1. Recursively: Divide and Conquer idea: Top down: split K lists into K/2, K/4, ... 2 (or 1), and merge 2 lists, Bottom up:
 then merging two bigger lists until merging them all.
2. Iteratively:
	1. using Priority Queue, first pushing every listNode in the list, then everytime poping a node from the Priority Queue,
	 Checking weather it does have next node, if it does, pushing it into the queue otherwise, do nothing.
	2. make_heap: use vector as if it is a heap!
 Code1:
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) :
        if(lists.empty()) return nullptr
        len = lists.size()
        while(len > 1):
            for(i = 0  i < len / 2 i++):
                lists[i] = merge2Lists(lists[i], lists[len - 1 - i])
            len = (len + 1) / 2
        return lists.front()
    ListNode* merge2Lists(ListNode * l1, ListNode * l2):
        if(!l1) return l2
        if(!l2) return l1
        if(l1->val < l2->val):
            l1->next = merge2Lists(l1->next, l2)
            return l1
        else:
            l2->next = merge2Lists(l1, l2->next)
            return l2
```
 Code 2: using Priority Queue
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    struct compare:
        bool operator()(ListNode* l, ListNode* r):
            return l->val > r-> val
    ListNode* mergeKLists(vector<ListNode*>& lists) :
        priority_queue<ListNode*, vector<ListNode*>, compare> pq
        for(auto l : lists):
            if(l) pq.push(l)
        if(pq.empty()) return nullptr
        ListNode* answer = pq.top() pq.pop()
        ListNode* tail = answer
        if(tail->next) pq.push(tail->next)
        while(!pq.empty()):
            tail->next = pq.top() pq.pop()
            tail = tail->next
            if(tail->next) pq.push(tail->next)
        return answer
```
 Code 3: using make_heap
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    static bool heapComp (ListNode * l, ListNode* r):
        return l-> val > r->val
    ListNode* mergeKLists(vector<ListNode*>& lists) :
        ListNode head(0)
        ListNode* curNode = &head
        vector<ListNode*> pq
        for(i = 0 i < lists.size() i++):
            if(lists[i]) pq.push_back(lists[i])
        make_heap(pq.begin(), pq.end(), heapComp)
        while(!pq.empty()):
            curNode -> next = pq.front() 
            curNode = curNode -> next
            pop_heap(pq.begin(), pq.end(), heapComp)
            pq.pop_back() #  throw out the least? percolate down?
            if(curNode -> next):
                pq.push_back(curNode->next)
                push_heap(pq.begin(),pq.end(),heapComp) #  percolate up?
        return head.next
```
 Special Thanks to
 ericxiao
 's
 solution
 and
 mingjun
 's
 solution
 for the reference
------------------------------------------------------------------------------------------------
 21. Merge Two Sorted Lists
==============================
 21. Merge Two Sorted Lists
============================
 Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
 Example:
```
Input:1->2->4, 1->3->4
Output:1->1->2->3->4->4
```
 Thoughts:
1. Recursively find the current least value between two sorted lists and link the next node of the smallest among the rest.
 Code:
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) :
        if(!l1) return l2
        if(!l2) return l1
        if(l1->val < l2 -> val):
            l1 -> next = mergeTwoLists(l1->next, l2)
            return l1
        else:
            l2->next = mergeTwoLists(l1, l2->next)
            return l2
```
 Code: (Less intuitive way, Java)
```python
public class Solution :
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) :
        if (l1 == null) return l2
        if (l2 == null) return l1
        ListNode head=null
        ListNode former=null
        while (l1!=null&&l2!=null) :
            if (l1.val>l2.val) :
                if (former==null) former=l2 else former.next=l2
                if (head==null) head=former else former=former.next
                l2=l2.next
             else :
                if (former==null) former=l1 else former.next=l1
                if (head==null) head=former else former=former.next
                l1=l1.next
        if (l2!=null) l1=l2
        former.next=l1
        return head
```
------------------------------------------------------------------------------------------------
 19. Remove Nth Node From End of List
========================================
 Given a linked list, remove the
 ---n--- 
 -th node from the end of list and return its head.
 Example:
```
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
```
 Note:
 Given _n _will always be valid.
 Follow up:
 Could you do this in one pass?
 Thoughts:
1. dfs "backtracking": recursively determine the index, with
 Value-Shifting
2. Index and Remove: recursively determine the index, with "deleting" the nth node (selecting the next node)
3. Two pointer: Having fast node go n steps first then when fast reaches the end (fast.next == null) slow.next is the node to be deleted: (if after n step fast is null (means n == len(list)) then only move the head by returning head.next else slow and fast go until fast reaches the end, and assign slow.next = slow.next.next
 from:
 StefanPochmann
 's
 post
 Code: Value-Shifting
```python
class Solution:
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
```
 Code: Index and Remove
```
# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
 :type head: ListNode
 :type n: int
 :rtype: ListNode
 """
        def backRemove(node):
            if not node: return 0, node
            i, node.next = backRemove(node.next)
            return i + 1, (node, node.next)[i + 1==n]
        return backRemove(head)[1]
```
 Code: two pointer: slow.next is the node to be deleted
```
# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
 :type head: ListNode
 :type n: int
 :rtype: ListNode
 """
        slow = fast = head
        # Given n is valid
        for _ in range(n):
            fast = fast.next
        if not fast: return head.next # remove head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
```
------------------------------------------------------------------------------------------------
 143. Reorder List
=====================
 Given a singly linked list
 ---L--- 
 :
 ---L_0→_L_1→…→_Ln--- 
 -1→
 ---L_n,
 reorder it to:_L_0→_Ln--- 
 →
 ---L_1→_Ln--- 
 -1→
 ---L_2→_Ln--- 
 -2→…
 You may
 not
 modify the values in the list's nodes, only nodes itself may be changed.
 Example 1:
```
Given 1->2->3->4, reorder it to 1->4->2->3.
```
 Example 2:
```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```
 Thoughts:
 practice for linking the nodes in linked list. Always draw a example out before writing the code
```
# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None
class Solution(object):
    def reorderList(self, head):
        """
 :type head: ListNode
 :rtype: void Do not return anything, modify head in-place instead.
 """
        if not head or not head.next: return 
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        preM = slow
        preC = slow.next
        # reverse the second half of the node: 1->2->3->4->5->6: 1->2->3->6->5->4
        while preC.next:
            current = preC.next
            preC.next = current.next
            current.next = preM.next
            preM.next = current
        # insert right to left nodes one by one:
        p1 = head
        p2 = preM.next
        while p1 != preM:
            preM.next = p2.next
            p2.next =p1.next
            p1.next = p2
            p1 = p2.next
            p2 = preM.next
```
------------------------------------------------------------------------------------------------
 206. Reverse Linked List
============================
 206. Reverse Linked List
==========================
 Reverse a linked list
 Thoughts:
1. Using Stack (time limit exceed)
2. Recursively: Find the second from the last node (if it Linked List contains more than two nodes), then reverse current two nodes by first creating a
 cycle
 , then cut the forward links (set it to be NULL/nullptr)
3. Having three pointers
	1. first record next node and then set current node next to pre
	2. repeat for the next step: move pre to head and then move head to next
4. 1. having three pointers with dummy node:
	2. pre always inserts cur->next right next to itself
 Code 2
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* reverseList(ListNode* head) :
        if(!head || !head->next) return head
        ListNode* node = reverseList(head->next)
        head->next->next = head
        head->next = nullptr
        return node
```
 Code 3
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    ListNode* reverseList(ListNode* head) :
        ListNode * pre = nullptr
        while(head):
            ListNode *next = head->next
            head->next = pre
            pre = head
            head = next
        return pre
```
 Code 4
```python
class Solution :
public:
    ListNode* reverseList(ListNode* head) :
        ListNode* pre = new ListNode(0)
        pre -> next = head
        ListNode* cur = head 
        while (cur && cur -> next) :
            ListNode* temp = pre -> next
            pre -> next = cur -> next
            cur -> next = cur -> next -> next 
            pre -> next -> next = temp
        return pre -> next
```
 Special Thanks to
 jianchaolifighter
 's
 Solution
 and and
 redace85
 's
 Solution
------------------------------------------------------------------------------------------------
 148. Sort List
==================
 148. Sort List
================
 Sort a linked list in O(nlogn) time using
 constant
 space complexity
 Thoughts:
 Equivalent to write a merge-sort in LinkedList
1. Recursively (O(logn) stack space complexity): halve the list by setting fast-slow pointers
2. Iteratively: have two pointer slow, fast, moved by steps a, b to partition the merge list then merge list inside. Repeat the step and shift blocksize value left by 1-bit until no more element left to be merged.
 Code: Recursively (java)
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 * val
 * ListNode next
 * ListNode(x) : val = x 
 * 
 */
class Solution :
  public ListNode sortList(ListNode head) :
    if (head == null || head.next == null)
      return head
    #  step 1. cut the list to two halves
    ListNode prev = null, slow = head, fast = head
    while (fast != null && fast.next != null) :
      prev = slow
      slow = slow.next
      fast = fast.next.next
    prev.next = null
    #  step 2. sort each half
    ListNode l1 = sortList(head)
    ListNode l2 = sortList(slow)
    #  step 3. merge l1 and l2
    return merge(l1, l2)
    public ListNode merge (ListNode l1, ListNode l2):
        if(l1 == null) return l2
        if(l2 == null) return l1
        #  ListNode head = l1.val > l2.val? l2: l1
        ListNode head
        if(l1.val > l2.val):
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        ListNode cur = head
        while(l1!=null && l2!= null):
            if(l1.val > l2.val):
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
        #  deal with the rest nodes
        if(l1 != null) cur.next = l1
        if(l2 != null) cur.next = l2
        return head
```
 Code: Iterative
```
/**
 * Definition for singly-linked list.
 * struct ListNode :
 * val
 * ListNode *next
 * ListNode(x) : val(x), next(NULL) :
 * 
 */
class Solution :
public:
    count_size(ListNode * node):
        n = 0
        while(node!=NULL):
            n++
            node = node->next            
        return n
    ListNode* sortList(ListNode* head) :
        blockSize = 1, n = count_size(head), iter_len = 0 
        ListNode* dummyHead  = new ListNode (0)
        dummyHead -> next = head
        ListNode * next = NULL, *last = NULL, *it = NULL, *slow = NULL, *fast =NULL
        while(blockSize < n):
            iter_len = 0
            last = dummyHead
            it = dummyHead -> next
            while(iter_len < n):
                slow_len = min(n - iter_len, blockSize)
                fast_len = min(n - iter_len - slow_len, blockSize)
                slow = it
                if(fast_len!=0):
                    for(i = 0 i < slow_len - 1 i++) it = it->next
                    #  reach fast
                    fast = it -> next
                    it -> next = NULL
                    it = fast
                    #  next
                    for(i = 0 i < fast_len - 1 i++) it = it->next
                    next = it->next
                    it->next = NULL
                    it = next
                    while(slow || fast):
                        if(!fast || (slow && slow->val < fast->val)):
                            last->next = slow
                            last = slow
                            slow = slow->next
                        else:
                            last->next = fast
                            last = fast
                            fast = fast-> next
                    last->next = NULL
                    iter_len += slow_len + fast_len
            blockSize <<=1
        return dummyHead -> next
```
------------------------------------------------------------------------------------------------
 24. Swap Nodes in Pairs
===========================
 Given a linked list, swap every two adjacent nodes and return its head.
 Example:
```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```
 Note:
* Your algorithm should use only constant extra space.
* You may
 not
 modify the values in the list's nodes, only nodes itself may be changed.
 Thoughts:
1. Recusively solve the problem, but O(n) extra space
2. Iteratively: Here,
 `pre` 
 is the previous node. Since the head doesn't have a previous node, I just use
 `self` 
 instead. Again,
 `a` 
 is the current node and
 `b` 
 is the next node. To go from
 `pre -> a -> b -> b.next` 
 to
 `pre -> b -> a -> b.next` 
 , we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.(
 StefanPochmann
 's
 post
 )
 Code: Recursively swaping every pairs
```
# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None
class Solution(object):
    def swapPairs(self, head):
        """
 :type head: ListNode
 :rtype: ListNode
 """
        if not head or not head.next: return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n
```
 Code: Iteratively
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        pre, pre.next = dummy, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return dummy.next
```
 Code: Iteratively
```
/**
 * Definition for singly-linked list.
 * public class ListNode :
 * val
 * ListNode next
 * ListNode(x) : val = x 
 * 
 */
class Solution :
    public ListNode swapPairs(ListNode head) :
        ListNode dummy = new ListNode(0)
        dummy.next = head
        ListNode cur = dummy
        while (cur.next != null && cur.next.next != null) :
            ListNode first = cur.next
            ListNode second = cur.next.next
            first.next = second.next
            cur.next = second
            cur.next.next = first
            cur = cur.next.next
        return dummy.next
```
------------------------------------------------------------------------------------------------
 Ask For Cooling Time
========================
### 
 1467.Ask For Cooling Time
 You have a bunch of skills that need to be released. The release order is
 `arr` 
 . Must be released in order. Each skill has a cooldown of length
 `n` 
 . That is, there must be an interval of at least
 `n` 
 seconds between two similar skills. It takes 1 second to release each skill, return the time it takes to finish all skills.
### 
 Example
 Given
 `arr=[1,1,2,2]` 
 ,
 `n=2` 
 .Return
 `8` 
 .
```
The order is [1, _, _, 1, 2, _, _, 2].So return 8.
Skill 1 is released in the 1st second, in the 2nd second and the 3rd second enters the cooling time, and the 4th second releases the second time.
Skill 2 is released in the 5th second, in the 6th second and the 7th second enters the cooling time, and the 8th second releases the second time.
```
 Given
 `arr=[1,2,1,2]` 
 ,
 `n=2` 
 . Return
 `5` 
 .
```
The order is [1, 2, _, 1, 2].So return  5.
Skill 1 is released in the 1st second, in the 2nd second and the 3rd second enters the cooling time, and the 4th second releases the second time.
Skill 2 is released in the 2nd second, in the 3rd second and the 4th second enters the cooling time, and the 5th second releases the second time.
```
 Similar to 621. Task Scheduler + Akuna/Drone Delivery
```python
class Solution:
    """
 @param arr: The release order
 @param n: The cooldown
 @return: Return the time
 """
    def askForCoolingTime(self, arr, n):
        # Write your code here
        t = :
        T = 1
        if not len(arr):
            return 0
        # print('arr[0]:: t[arr[0]]::'.format(arr[0], t[arr[0]]))
        for i in range (1, len(arr)):
            t[arr[i]] = 0
        t[arr[0]] = T + n
        # print('t[arr[0]]: :'.format(t[arr[0]]))
        for i in range (1, len(arr)):
            # print('t[arr[1]]: :'.format(t[arr[1]]))
            if T < t[arr[i]]:
                T = t[arr[i]] + 1
                t[arr[i]] = T + n
                # print('in i:: T::  arr[i]: : t[arr[i]]: :'.format(i,T,arr[i],t[arr[i]]))
                continue
            T += 1
            t[arr[i]] = T + n
            # print('out i:: T::  arr[i]: : t[arr[i]]: :'.format(i,T,arr[i],t[arr[i]]))
        return T
```
------------------------------------------------------------------------------------------------
 Guess the Word
==================
 843. Guess the Word
=====================
 This problem is an
 ---interactive problem--- 
 new to the LeetCode platform.
 We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as
 secret
 .
 You may call
 `master.guess(word)` 
 to guess a word. The guessed word should have type
 `string` 
 and must be from the original list with 6 lowercase letters.
 This function returns an
 `integer` 
 type, representing the number of exact matches (value and position) of your guess to the
 secret word
 . Also, if your guess is not in the given wordlist, it will return
 `-1` 
 instead.
 For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to
 `master.guess` 
 and at least one of these guesses was the
 secret
 , you pass the testcase.
 Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list. The letters of each word in those testcases were chosen independently at random from
 `'a'` 
 to
 `'z'` 
 , such that every word in the given word lists is unique.
```
Example 1:
Input:
secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
Explanation:
master.guess("aaaaaa")
 returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") 
returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz")
 returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz")
 returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz")
 returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
```
 Note:
 Any solutions that attempt to circumvent the judge will result in disqualification.
 Thoughts:
 (
 Original Post
 )
1. Random:
	1. Randomly pick one word to query from wordlist, record the answer as x
	2. update wordlist only saving words
	 with exactly x matches
	 with the query words
2. Words with most non-zero matches (least 0 matches):
	1. for each word, record number of 0 matches
	2. find the word with least 0 matches, breaking ties using one with larger index
 Code: Random(80% success rate) O(N)
```python
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
 :type wordlist: List[Str]
 :type master: Master
 :rtype: None
 """
        n = 0 
        while n < 6:
            guess = random.choice(wordlist)
            n = master.guess(guess)
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(guess, w)) == n]
```
```
/**
 * #  This is the Master's API interface.
 * #  You should not implement it, or speculate about its implementation
 * class Master :
 * public:
 * guess(string word)
 * 
 */
class Solution :
public:
    match(string a, string b):
        matches = 0
        for(i = 0 i < a.length() ++i) if(a[i] == b[i]) matches ++
        return matches
    void findSecretWord(vector<string>& wordlist, Master& master) :
        for (i = 0, x = 0 i < 10 && x < 6 i++):
            string guess = wordlist[rand() % (wordlist.size())]
            x = master.guess(guess)
            vector<string> wordlist2
            for (string w: wordlist)
                if (match(guess, w) == x)
                    wordlist2.push_back(w)
            wordlist = wordlist2     
```
 Code: Least 0 matches: O(N^2)
```
/**
 * #  This is the Master's API interface.
 * #  You should not implement it, or speculate about its implementation
 * class Master :
 * public:
 * guess(string word)
 * 
 */
class Solution :
public:
    match(string a, string b):
        matches = 0
        for(i = 0 i < a.length() ++i) if(a[i] == b[i]) matches ++
        return matches
    void findSecretWord(vector<string>& wordlist, Master& master) :
        for (i = 0, x = 0 i < 10 && x < 6 i++):
            #  string guess = wordlist[rand() % (wordlist.size())]
            /* guess the words with the least 0 matches*/
            unordered_map<string, int> count
            for (string w1: wordlist)
                for (string w2: wordlist)
                    if (match(w1, w2) == 0)
                        count[w1]++
            /* search through wordlist to find words that has most non-zero matches (least mininum 0 matches) */
            pair<string, int> minimax = make_pair(wordlist[0], 1000)
            for (string w: wordlist)
                if (count[w] <= minimax.second)
                    minimax = make_pair(w, count[w])
            string guess = minimax.first
            x = master.guess(guess)
            vector<string> wordlist2
            for (string w: wordlist)
                if (match(guess, w) == x)
                    wordlist2.push_back(w)
            wordlist = wordlist2     
```
------------------------------------------------------------------------------------------------
 772. Basic Calculator III
=============================
 Implement a basic calculator to evaluate a simple expression string.
 The expression string may contain open
 `(` 
 and closing parentheses
 `)` 
 , the plus
 `+` 
 or minus sign
 `-` 
 ,
 non-negative
 integers and empty spaces.
 The expression string contains only non-negative integers,
 `+` 
 ,
 `-` 
 ,
 `*` 
 ,
 `/` 
 operators , open
 `(` 
 and closing parentheses
 `)` 
 and empty spaces. The integer division should truncate toward zero.
 You may assume that the given expression is always valid. All intermediate results will be in the range of
 `[-2147483648, 2147483647]` 
 .
 Some examples:
```
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
```
 Thoughts: Covered in
 Calculator Series
 :
 Code
 : Recursive: T: O(n^2) S:O(n)
```python
class Solution :
    public calculate(String s) :
        l1 = 0, o1 = 1
        l2 = 1, o2 = 1
        for (i = 0 i < s.length() i++) :
            char c = s.charAt(i)
            if (Character.isDigit(c)) :
                num = c - '0'
                while (i + 1 < s.length() && Character.isDigit(s.charAt(i + 1))) :
                    num = num * 10 + (s.charAt(++i) - '0')
                l2 = (o2 == 1 ? l2 * num : l2 / num)
             else if (c == '(') :
                j = i
                for (cnt = 0 i < s.length() i++) :
                    if (s.charAt(i) == '(') cnt++
                    if (s.charAt(i) == ')') cnt--
                    if (cnt == 0) break
                num = calculate(s.substring(j + 1, i))
                l2 = (o2 == 1 ? l2 * num : l2 / num)
             else if (c == '*' || c == '/') :
                o2 = (c == '*' ? 1 : -1)
             else if (c == '+' || c == '-') :
                l1 = l1 + o1 * l2
                o1 = (c == '+' ? 1 : -1)
                l2 = 1 o2 = 1
        return (l1 + o1 * l2)
```
 Code: Iterative:
 T: O(n) S: O(n)
```python
class Solution :
    public calculate(String s) :
        l1 = 0, o1 = 1
        l2 = 1, o2 = 1
        Deque<Integer> stack = new ArrayDeque()
        for(i = 0 i < s.length() i++):
            char c = s.charAt(i)
            if(Character.isDigit(c)):
                num = c - '0'
                while (i + 1 < s.length() && Character.isDigit(s.charAt(i + 1))) :
                    num = num *10 + (s.charAt(++i) - '0')
                l2 = (o2 == 1 ? l2 * num: l2 / num)
             else if (c == '('):
                #  First preserve current calculation status
                stack.offerFirst(l1) stack.offerFirst(o1)
                stack.offerFirst(l2) stack.offerFirst(o2)
                #  Reset them for the next calculation
                l1 = 0 o1 = 1
                l2 = 1 o2 = 1
             else if (c== ')'):
                 #  First preserve the result of current calculation
                num = l1 + o1 * l2
                #  Then restore previous calculation status
                o2 = stack.poll() l2 = stack.poll()
                o1 = stack.poll() l1 = stack.poll()
                #  Previous calculation status is now in effect
                l2 = (o2 == 1 ? l2 * num : l2 / num)
             else if (c == '*' || c == '/'):
                o2 = ( c == '*'? 1: -1)
             else if (c == '+' || c == '-'):
                l1 = l1 + o1 * l2
                o1 = (c == '+'? 1: -1)
                l2 = 1 o2 = 1
        return (l1 + o1 * l2)
```
------------------------------------------------------------------------------------------------
 227. Basic Calculator
=========================
 Implement a basic calculator to evaluate a simple expression string.
 The expression string contains only
 non-negative
 integers,
 `+` 
 ,
 `-` 
 ,
 `*` 
 ,
 `/` 
 operators and empty spaces. The integer division should truncate toward zero.
 Example 1:
```
Input: 
"3+2*2"
Output: 7
```
 Example 2:
```
Input: " 3/2 "
Output:1
```
 Example 3:
```
Input:" 3+5 / 2 "
Output: 5
```
 Note:
* You may assume that the given expression is always valid.
* Do not
 use the
 `eval` 
 built-in library function.
 Thoughts:
 need to look back to know what is the operand value when encountered an operator. Hence need two variable: operator and operand.
1. With stack: using a stack to keep track of numbers and do the operation based on operators.
2. Without stack: only add current operand to the accumulative sum when encountered '+' or '-' since '*' and '/' has prioirty
 Code: with a stack
```python
class Solution :
    public calculate(String s) :
        if(s == null || s.length() ==0) return 0
        len = s.length()
        Stack<Integer> stack = new Stack<Integer>()
        num = 0
        char sign= '+' #  equivalent to concatenate a '+' in front of s
        for(i = 0  i < len  i++):
            #  operand
            if (Character.isDigit(s.charAt(i)))
                num = 10 * num + s.charAt(i) - '0'
            if ((!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ') || i == len - 1):
                if(sign == '-'):
                    stack.push(-num)
                if(sign == '+'):
                    stack.push(num)
                if(sign == '*'):
                     stack.push(stack.pop()*num)
                if(sign == '/'):
                     stack.push(stack.pop()/num)
                sign = s.charAt(i)
                num = 0
        ans = 0
        for (i: stack) ans += i
        return ans
```
 Code: without a stack
```python
class Solution :
public:
    calculate(string s) :
        istringstream in('+' + s + '+')
        long long total = 0, term = 0, n
        char op
        while (in >> op) :
            if (op == '+' or op == '-') :
                total += term
                in >> term
                term *= op == '+' ? 1 : -1
             else :
                in >> n
                if (op == '*')
                    term *= n
                else
                    term /= n
        return total
```
------------------------------------------------------------------------------------------------
 Calculator Series
=====================
 So far, we have encountered the following series of calculator problems:
1. 224. Basic Calculator
2. 227. Basic Calculator II
3. 772. Basic Calculator III
4. 770. Basic Calculator IV
 Though each of them may be solved using different methodologies, in this post I'd like to sort out the complexities and develop one "generic" solution to help us approach these problems.
 Note that this post is
 NOT
 intended to deal with general calculator problems that involve complicated operands/operators. The analyses below are limited to the scope as specified by the problem descriptions of the above four problems.
`I -- Definitions and terminology` 
 In this section I will spell out some definitions to facilitate the explanation.
* `Expression` 
 : An expression is a string whose value is to be calculated. Every expression must be alternating between
 operand
 s and
 operator
 s.
* `Operand` 
 : An operand is a "generalized value" that can be the target of an operator. It must be one of the following three types --
 number
 ,
 variable
 ,
 subexpression
 .
* `Number` 
 : A number consists of digits only. The value of an operand of this type is given by the literal value of the number.
* `Variable` 
 : A variable consists of lowercase letters only. It can be either a free variable whose value is unknown, or a bound variable whose value is mapped to some number (can be looked up). Here we define the value of an operand of free variable type is given by the variable itself, while that of bound variable type is given by the value of the number to which the variable is mapped.
* `Subexpression` 
 : A subexpression is a valid expression enclosed in parentheses (which implies a recursive definition back to
 `Expression` 
 ). The value of an operand of this type is given by the calculated value of the subexpression itself.
* `Operator` 
 : An operator is some prescribed action to be taken on the target operands. It must be one of the following four types:
 `+` 
 ,
 `-` 
 ,
 `*` 
 ,
 `/` 
 , corresponding to addition, subtraction, multiplication and integer division, respectively. Operators have precedences, where
 `+` 
 and
 `-` 
 have
 level one
 precedence, while
 `*` 
 and
 `/` 
 have
 level two
 precedence (the higher the level is, the higher the precedence is).
`II -- Rules for calculations` 
 In this section, I will specify the general rules for carrying out the actual evaluations of the expression.
 Separation rule
 :
* We separate the calculations into two different levels corresponding to the two precedence levels.
* For each level of calculation, we maintain two pieces of information: the
 ---partial result_and the_operator in effect--- 
 .
* For level one, the partial result starts from
 `0` 
 and the initial operator in effect is
 `+` 
  for level two, the partial result starts from
 `1` 
 and the initial operator in effect is
 `*` 
 .
* We will use
 `l1` 
 and
 `o1` 
 to denote respectively the partial result and the operator in effect for level one
 `l2` 
 and
 `o2` 
 for level two. The operators have the following mapping:
`o1 == 1` 
 means
 `+` 
 `o1 == -1` 
 means
 `-` 
`o2 == 1` 
 means
 `*` 
 `o2 == -1` 
 means
 `/` 
 .
 By default we have
 `l1 = 0` 
 ,
 `o1 = 1` 
 , and
 `l2 = 1` 
 ,
 `o2 = 1` 
 .
 Precedence rule
 :
* Each operand in the expression will be associated with a precedence of level two by default, meaning they can only take part in calculations of precedence level two, not level one.
* The operand can be any of the aforementioned types (number, variable or subexpression), and will be evaluated together with
 `l2` 
 under the action prescribed by
 `o2` 
 .
 Demotion rule
 :
* The partial result
 `l2` 
 of precedence level two can be demoted to level one. Upon demotion,
 `l2` 
 becomes the operand for precedence level one and will be evaluated together with
 `l1` 
 under the action prescribed by
 `o1` 
 .
* The demotion happens when either a level one operator (i.e.,
 `+` 
 or
 `-` 
 ) is hit or the end of the expression is reached. After demotion,
 `l2` 
 and
 `o2` 
 will be reset for following calculations.
`III -- Algorithm implementations` 
 In this section, I will lay out the general structure of the algorithm using pseudo-codes. From section
 `I` 
 , we know there are at most five different types of structs contained in the expression: number, variable, subexpression, level one operators, level two operators. We will check each of them and proceed accordingly.
```python
public calculate(String s) :
    l1 = 0, o1 = 1 #  Initialization of level one
    l2 = 1, o2 = 1 #  Initialization of level two
    for (i = 0 i < s.length() i++) :
        char c = s.charAt(i)
        if (c is a digit) :
           --> we have an operand of type number, so find its value "num"
           --> then evaluate at level two: l2 = (o2 == 1 ? l2 * num : l2 / num)
         else if (c is a lowercase letter) :
           --> we have an operand of type variable, so find its name "var"
           --> then look up the variable mapping table to find its value "num"
           --> lastly evaluate at level two: l2 = (o2 == 1 ? l2 * num : l2 / num)
         else if (c is an opening parenthesis) :
           --> we have an operand of type subexpression, so find its string representation
           --> then recursively call the "calculate" function to find its value "num"
           --> lastly evaluate at level two: l2 = (o2 == 1 ? l2 * num : l2 / num)
         else if (c is a level two operator) :
            --> o2 needs to be updated: o2 = (c == '*' ? 1 : -1)
         else if (c is a level one operator) :
            --> demotion happens here: l1 = l1 + o1 * l2
            --> o1 needs to be updated: o1 = (c == '+' ? 1 : -1)
            --> l2, o2 need to be reset: l2 = 1, o2 = 1
       return (l1 + o1 * l2) #  end of expression reached, so demotion happens again
```
---
`IV -- List of solutions` 
 It is now straightforward to adapt the algorithm in section
 `III` 
 to tackle each of the calculator problems. Note that not all the checks are needed for a particular version of the calculator problems. More specifically,
* Basic Calculator I does not have variables and level two operators
* Basic Calculator II does not contain variables as well as subexpressions
* Basic Calculator III does not have variables
* Basic Calculator IV is the most general form but its level two operators do not include division (
 `/` 
 ).
 In this section, I will list two solutions for Basic Calculator III (recursive and iterative), and one solution for Basic Calculator IV (recursive).
 Basic Calculator III
 : Solutions for this version pretty much follow the general structure in section
 `III` 
 , except that we do not need to check for variables since the input expression does not contain any.
* Recursive solution:
 `O(n^2)` 
 time,
 `O(n)` 
 space
```python
public basicCalculatorIII(String s) :
    l1 = 0, o1 = 1
    l2 = 1, o2 = 1
    for (i = 0 i < s.length() i++) :
        char c = s.charAt(i)
        if (Character.isDigit(c)) :
            num = c - '0'
            while (i + 1 < s.length() && Character.isDigit(s.charAt(i + 1))) :
                num = num * 10 + (s.charAt(++i) - '0')
            l2 = (o2 == 1 ? l2 * num : l2 / num)
         else if (c == '(') :
            j = i
            for (cnt = 0 i < s.length() i++) :
                if (s.charAt(i) == '(') cnt++
                if (s.charAt(i) == ')') cnt--
                if (cnt == 0) break
            num = basicCalculatorIII(s.substring(j + 1, i))
            l2 = (o2 == 1 ? l2 * num : l2 / num)
         else if (c == '*' || c == '/') :
            o2 = (c == '*' ? 1 : -1)
         else if (c == '+' || c == '-') :
            l1 = l1 + o1 * l2
            o1 = (c == '+' ? 1 : -1)
            l2 = 1 o2 = 1
    return (l1 + o1 * l2)
```
* Iterative solution:
 `O(n)` 
 time,
 `O(n)` 
 space
```python
public basicCalculatorIII(String s) :
    l1 = 0, o1 = 1
    l2 = 1, o2 = 1
    Deque<Integer> stack = new ArrayDeque<>() #  stack to simulate recursion
    for (i = 0 i < s.length() i++) :
        char c = s.charAt(i)
        if (Character.isDigit(c)) :
            num = c - '0'
            while (i + 1 < s.length() && Character.isDigit(s.charAt(i + 1))) :
                num = num * 10 + (s.charAt(++i) - '0')
            l2 = (o2 == 1 ? l2 * num : l2 / num)
         else if (c == '(') :
            #  First preserve current calculation status
            stack.offerFirst(l1) stack.offerFirst(o1)
            stack.offerFirst(l2) stack.offerFirst(o2)
            #  Then reset it for next calculation
            l1 = 0 o1 = 1
            l2 = 1 o2 = 1
         else if (c == ')') :
            #  First preserve the result of current calculation
            num = l1 + o1 * l2
            #  Then restore previous calculation status
            o2 = stack.poll() l2 = stack.poll()
            o1 = stack.poll() l1 = stack.poll()
            #  Previous calculation status is now in effect
            l2 = (o2 == 1 ? l2 * num : l2 / num)
         else if (c == '*' || c == '/') :
            o2 = (c == '*' ? 1 : -1)
         else if (c == '+' || c == '-') :
            l1 = l1 + o1 * l2
            o1 = (c == '+' ? 1 : -1)
            l2 = 1 o2 = 1
    return (l1 + o1 * l2)
```
 Basic Calculator IV
 : Solutions for this version, however, require some extra effort apart from the general structure in section
 `III` 
 . Due to the presence of variables (free variables, to be exact), the partial results for each level of calculations may not be pure numbers, but instead expressions (simplified, of course). So we have to come up with some structure to represent these partial results.
 Though multiple options exist as to designing this structure, we do want it to support operations like addition, subtraction and multiplication with relative ease. Here I represent each expression as a collection of mappings from terms to coefficients, where each term is just a list of free variables sorted in lexicographic order. Some quick examples:
1. `"2 * a * b - d * c"` 
 : this expression contains two terms, where the first term is
 `["a", "b"]` 
 and the second is
 `["c", "d"]` 
 . The former has a coefficient of
 `2` 
 while the latter has a coefficient of
 `-1` 
 . So we represent the expression as two mappings:
 `["a", "b"] --> 2` 
 and
 `["c", "d"] --> -1` 
 .
2. "
 `4` 
 ": this expression contains a single term, where the term has
 zero
 free variables and thus will be written as
 `[]` 
 . The coefficient is
 `4` 
 so we have the mapping
 `[] --> 4` 
 . More generally, for any expression formed only by a pure number
 `num` 
 , we have
 `[] --> num` 
 .
 See below for a detailed definition of the
 `Term` 
 and
 `Expression` 
 classes.
 The
 `Term` 
 class will support operations for comparing two terms according to their degrees as well as for generating a customized string representation.
 The
 `Expression` 
 class will support operations for adding additional terms to the existing mapping.
 Addition
 of two expressions is done by adding all mappings in the second expression to those of the first one, and if possible, combine the coefficients of duplicate terms.
 Subtraction
 of two expressions is implemented by first negating the coefficients of terms in the second expression and then applying addition (and thus can be combined with addition).
 Multiplication
 of two expressions is done by collecting terms formed by merging every pair of terms from the two expressions (as well as their coefficients).
 Lastly to conform to the format of the output, we have a dedicated function to convert the mappings in the result expression to a list of strings, where each string consists of the coefficient and the term connected by the
 `*` 
 operator. Note that terms with
 `0` 
 coefficient are ignored and terms without free variables contains numbers only.
 As to complexity analysis, the nominal runtime complexity of this solution is similar to the recursive one for Basic Calculator III --
 `O(n^2)` 
 . It is also possible to use stacks to simulate the recursion process and cut the nominal time complexity down to
 `O(n)` 
 (I will leave this as an exercise for you).
 Here I used the word "nominal" because the above analyses assumed that the addition, subtraction and multiplication operations of two expressions take constant time, as is the case when the expressions are pure numbers. Apparently this assumption no longer stands true, since the number of terms may grow exponentially (think about this expression
 `(a + b) * (c + d) * (e + f) * ...` 
 ). Nevertheless, this solution should work against average/general test cases.
```
private static class Term implements Comparable<Term> :
    List<String> vars
    static final Term C = new Term(Arrays.asList()) #  this is the term for pure numbers
    Term(List<String> vars) :
        this.vars = vars
    public hashCode() :
        return vars.hashCode()
    public boolean equals(Object obj) :
        if (this == obj) return true
        if (!(obj instanceof Term)) return false
        Term other = (Term)obj
        return this.vars.equals(other.vars)
    public String toString() :
        return String.join("*", vars)
    public compareTo(Term other) :
        if (this.vars.size() != other.vars.size()) :
            return Integer.compare(other.vars.size(), this.vars.size())
         else :
            for (i = 0 i < this.vars.size() i++) :
                cmp = this.vars.get(i).compareTo(other.vars.get(i))
                if (cmp != 0) return cmp
        return 0
private static class Expression :
    Map<Term, Integer> terms
    Expression(Term term, coeff) :
        terms = new HashMap<>()
        terms.put(term, coeff)
    void addTerm(Term term, coeff) :
        terms.put(term, coeff + terms.getOrDefault(term, 0))
private Term merge(Term term1, Term term2) :
    List<String> vars = new ArrayList<>()
    vars.addAll(term1.vars)
    vars.addAll(term2.vars)
    Collections.sort(vars)
    return new Term(vars)
private Expression add(Expression expression1, Expression expression2, sign) :
    for (Map.Entry<Term, Integer> e : expression2.terms.entrySet()) :
        expression1.addTerm(e.getKey(), sign * e.getValue())
    return expression1
private Expression mult(Expression expression1, Expression expression2) :
    Expression res = new Expression(Term.C, 0)
    for (Map.Entry<Term, Integer> e1 : expression1.terms.entrySet()) :
        for (Map.Entry<Term, Integer> e2 : expression2.terms.entrySet()) :
            res.addTerm(merge(e1.getKey(), e2.getKey()), e1.getValue() * e2.getValue())
    return res
private Expression calculate(String s, Map<String, Integer> map) :
    Expression l1 = new Expression(Term.C, 0)
    o1 = 1
    Expression l2 = new Expression(Term.C, 1) 
    #  we don't need 'o2' because the precedence level two operators contain '*' only
    for (i = 0 i < s.length() i++) :
        char c = s.charAt(i)
        if (Character.isDigit(c)) :  #  this is a number
            num = c - '0'
            while (i + 1 < s.length() && Character.isDigit(s.charAt(i + 1))) :
                num = num * 10 + (s.charAt(++i) - '0')
            l2 = mult(l2, new Expression(Term.C, num))
         else if (Character.isLowerCase(c)) : #  this is a variable
            j = i
            while (i + 1 < s.length() && Character.isLowerCase(s.charAt(i + 1))) i++
            String var = s.substring(j, i + 1)
            Term term = map.containsKey(var) ? Term.C : new Term(Arrays.asList(var))
            num = map.getOrDefault(var, 1)
            l2 = mult(l2, new Expression(term, num))
         else if (c == '(') : #  this is a subexpression
            j = i
            for (cnt = 0 i < s.length() i++) :
                if (s.charAt(i) == '(') cnt++
                if (s.charAt(i) == ')') cnt--
                if (cnt == 0) break
            l2 = mult(l2, calculate(s.substring(j + 1, i), map))
         else if (c == '+' || c == '-') : #  level one operators
            l1 = add(l1, l2, o1)
            o1 = (c == '+' ? 1 : -1)
            l2 = new Expression(Term.C, 1)
    return add(l1, l2, o1)
private List<String> format(Expression expression) :
    List<Term> terms = new ArrayList<>(expression.terms.keySet())
    Collections.sort(terms)
    List<String> res = new ArrayList<>(terms.size())
    for (Term term : terms) :
        coeff = expression.terms.get(term)
        if (coeff == 0) continue
        res.add(coeff + (term.equals(Term.C) ? "" : "*" + term.toString()))
    return res
public List<String> basicCalculatorIV(String expression, String[] evalvars, int[] evalints) :
    Map<String, Integer> map = new HashMap<>()
    for (i = 0 i < evalvars.length i++) :
        map.put(evalvars[i], evalints[i])
    return format(calculate(expression, map))
```
------------------------------------------------------------------------------------------------
 Drone Delivery
==================
 Drone Delivery
================
 Drone delevery service is goint to be tested in a location.
 -The location has constructed homes on multiple identical grids throughout the town.
 -Each grid has 50 homes and each grid is assigned a unique number.
 -Each home within a grid has a unique number from 1 to 50.
 So each home can be uniquely identified by its grid number and home number pair.
 The simple algorithm for the initial rollout of the drone delivery service:
 -A swarm of delivery drones will be deployed for the delivery.
 -In each swarm there will be one drone for each unique housing grid that will receive deliveries.
 -Each drone will start at home number 1 in the grid and advance until all delivery for the grid is complete.
 -over the period of 1 minute each drone can move to the next house, can make a delivery or can stay at its current position.
 -All products must be delivered in exact order in which the order was made.
 Your task is to determine how long it will take a swarm of drones to complete a specified delivery.
 For example,
 1234-1, 1235-1, 1235-3, 1234-2
 from the above sequence there are two housing grids, 1234 and 1235, and two homes to deliver to on each grid.
 The swarm will perform the following tasks in order to deliver the products:
| 
 Time
  | 
 Drone - 1234
  | 
 Drone - 1235
  |
| --- | --- | --- |
| 
 1
  | 
 Deliver Product
  | 
 Wait at home 1
  |
| 
 2
  | 
 Move to Home 2
  | 
 Deliver Product
  |
| 
 3
  | 
 Wait at Home 2
  | 
 Move to Home 2
  |
| 
 4
  | 
 Wait at Home 2
  | 
 Move to Home 3
  |
| 
 5
  | 
 Wait at Home 2
  | 
 Deliver Product
  |
| 
 6
  | 
 Deliver Product
  | 
 Wait at Home 3
  |
 It will take 6 minutes to complete this delivery task.
 There can be
 at most two drones
 . For each test case you will be given the total number of packages and sequence of locations.
```
def time_to_deliver(num_package, delivery_sequence):
    record = : schedule = [] T = 0
    for input in delivery_sequence:
        a  = input.split("-")
        schedule.append(a)
        drone = a[0]
        if drone not in record.keys():
            record[drone] = [0, 1]
    # update time
    for s in schedule:
        drone = s[0]
        dest = int(s[1])
        # get Time , Location tuple
        travelTime = dest - record[drone][1]
        diff= max(T - record[drone][0], abs(travelTime)) + 1
        record[drone][0] += diff
        # update curloc
        record[drone][1] = dest
        T = record[drone][0]
    return T
```
------------------------------------------------------------------------------------------------
 636. Exclusive Time of Functions
====================================
 Given the running logs of
 n
 functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.
 Each function has a unique id, start from
 0
 to
 n-1
 . A function may be called recursively or by another function.
 A log is a string has this format :
 `function_id:start_or_end:timestamp` 
 . For example,
 `"0:start:0"` 
 means function 0 starts from the very beginning of time 0.
 `"0:end:0"` 
 means function 0 ends to the very end of time 0.
 Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.
 Example 1:
```
Input:
n = 2
logs = 
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:
[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
Now function 0 
calls function 1
, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
```
 Note:
1. Input logs will be sorted by timestamp, NOT log id.
2. Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
3. Two functions won't start or end at the same time.
4. Functions could be called recursively, and will always end.
5. 1 <= n <= 100
 Thoughts:
1. Recursive call: so using stack: record current functions by id
2. For each log, check the type of fuction:
	1. if it is a "start", increment the caller function execution time by querying the last element in the stack with time - prev_time
	2. if it is a "end", pop the function from stack and use it to index into returned function. The total execution for popped function is time +
	 1
	 - prev_time since the questions records the end of the time for "end"
 Code:
```python
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
 :type n: int
 :type logs: List[str]
 :rtype: List[int]
 """
        funcs = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            fid , typ, time = log.split(':')
            fid , time = int(fid), int(time)
            if typ == "start":
                if stack:
                    funcs[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:
                funcs[stack.pop()] += time + 1 -prev_time # end of time t so + 1
                prev_time = time + 1
        return funcs
```
 Code: use stack to record time (slow)
```python
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
 :type n: int
 :type logs: List[str]
 :rtype: List[int]
 """
        funcs , stack = [0] * n, []
        for log in logs:
            fid , typ, time = log.split(':')
            fid, time = int(fid), int(time)
            if typ == 'start':
                stack.append(time)
            else:
                d = time + 1 - stack.pop() 
                funcs[fid] += d
                stack = [t + d for t in stack]
        return funcs
```
 Code: Augmented solution for new stack class design
```python
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
 :type n: int
 :type logs: List[str]
 :rtype: List[int]
 """
        funcs , stack = [0] * n, AccStack()
        for log in logs:
            fid , typ, time = log.split(':')
            fid, time = int(fid), int(time)
            if typ == 'start':
                stack.append(time)
            else:
                d = time + 1 - stack.pop() 
                funcs[fid] += d # adds up for adjustments later
                stack.add_across(d)
        return funcs
class AccStack(object):
    def __init__ (self):
        self.s = []
    def append(self, x):
        self.s.append([x, 0]) #[time, time "waiting" in calling other methods]
    def pop(self):
        t1, t2 = self.s.pop()
        if self.s:
            self.s[-1][1] += t2
        return  t1 + t2
    def add_across(self, t):
        if self.s:
            self.s[-1][1] += t
```
------------------------------------------------------------------------------------------------
 388. Longest Absolute File Path
===================================
 Suppose we abstract our file system by a string in the following manner:
 The string
 `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` 
 represents:
```
dir
    subdir1
    subdir2
        file.ext
```
 The directory
 `dir` 
 contains an empty sub-directory
 `subdir1` 
 and a sub-directory
 `subdir2` 
 containing a file
 `file.ext` 
 .
 The string
 `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` 
 represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
 The directory
 `dir` 
 contains two sub-directories
 `subdir1` 
 and
 `subdir2` 
 .
 `subdir1` 
 contains a file
 `file1.ext` 
 and an empty second-level sub-directory
 `subsubdir1` 
 .
 `subdir2` 
 contains a second-level sub-directory
 `subsubdir2` 
 containing a file
 `file2.ext` 
 .
 We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is
 `"dir/subdir2/subsubdir2/file2.ext"` 
 , and its length is
 `32` 
 (not including the double quotes).
 Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return
 `0` 
 .
 Note:
* The name of a file contains at least a
 `.` 
 and an extension.
* The name of a directory or sub-directory will not contain a
 `.` 
 .
 Time complexity required:
 `O(n)` 
 where
 `n` 
 is the size of the input string.
 Notice that
 `a/aa/aaa/file1.txt` 
 is not the longest file path, if there is another path
 `aaaaaaaaaaaaaaaaaaaaa/sth.png` 
 .
 Thoughts:
 record the length of current explored folder in the stack and max length if it is has a file extension
```python
class Solution :
    public lengthLongestPath(String input) :
        Deque<Integer> stack = new ArrayDeque<>()
        stack.push(0) #  "dummy" length
        maxLen = 0
        for(String s:input.split("\n")):
            lev = s.lastIndexOf("\t")+1 #  number of "\t"
            #  System.out.println("s: "+ s + ", lev: " + lev + ", stack.size(): " + stack.size())
            while(lev+1<stack.size()) stack.pop() #  find parent
            len = stack.peek()+s.length()-lev+1 #  remove "/t", add"/"
            #  System.out.println("len: " + len)
            stack.push(len)
            #  check if it is file
            if(s.contains(".")) maxLen = Math.max(maxLen, len-1) 
        return maxLen
```
 using Array (DP):
```python
class Solution :
        public lengthLongestPath(String input) :
        String[] paths = input.split("\n")
        int[] stack = new int[paths.length+1]
        maxLen = 0
        for(String s:paths):
            lev = s.lastIndexOf("\t")+1, curLen = stack[lev+1] = stack[lev]+s.length()-lev+1
            if(s.contains(".")) maxLen = Math.max(maxLen, curLen-1)
        return maxLen
```
 Solution from
 sky-xu
 's
 post
------------------------------------------------------------------------------------------------
 716. Max Stack
==================
 Design a max stack that supports push, pop, top, peekMax and popMax.
1. push(x) -- Push element x onto stack.
2. pop() -- Remove the element on top of the stack and return it.
3. top() -- Get the element on the top.
4. peekMax() -- Retrieve the maximum element in the stack.
5. popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
 Example 1:
```
MaxStack stack = new MaxStack()
stack.push(5) 
stack.push(1)
stack.push(5)
stack.top() ->5
stack.popMax() ->5
stack.top() ->1
stack.peekMax() ->5
stack.pop() ->1
stack.top() ->5
```
 Note:
1. -1e7 <= x <= 1e7
2. Number of operations won't exceed 10000.
3. The last four operations won't be called when stack is empty.
 Thoughts:
 use a auxiliary map to record the index entry, and map can sort the order internally
 Code Write O(logn), read O(1):
```python
class MaxStack :
public:
    /** initialize your data structure here. */
    list<int> l
    map<int, vector<list<int>::iterator>> mp
    MaxStack() :
    void push(x) :
        l.insert(l.begin(),x)
        mp[x].push_back(l.begin())
    pop() :
        #  delete iterator in the map
        key = *l.begin()
        mp[key].pop_back()
        if(mp[key].empty()) mp.erase(key)
        l.erase(l.begin())
        return key
    top() :
        return *l.begin()
    peekMax() :
        return mp.rbegin()->first
    popMax() :
        key = mp.rbegin()->first
        #  get the iterator
        auto it = mp[key].back()
        mp[key].pop_back()
        if(mp[key].empty()) mp.erase(key)
        l.erase(it)
        return key
```
 solution from
 imrusty
 's
 post
------------------------------------------------------------------------------------------------
 phone
=========
 电面
 美国人，预定45分钟，实际52分钟。
 1, Python experience, relative project, may follow up quite a few questions about project, depends on whether he is interested
 2, Difference between List, Dict and Set follow up, time complexity of search in List and Dict
 3, Generator
 4, Decorator, give an example
 5, Why we need Multithread, why we prefer Multiprocess over Multithread
 6, How many numbers between 1 to 10,000 don't have 5 in it?
 7, Bank A has 10 tellers, each serving one customer at a time independently Bank B has 10 tellers, sharing a queue of customers to serve. Which bank you prefer? Why?
 8, Any questions you want to ask about Akuna?
------------------------------------------------------------------------------------------------
 Postfix to Infix
====================
 Convert an expression written in postfix notation to infix notation
 A postfix expression is one where each operator comes after it's operands, while in an infix expression the operator is in between the operands. For example, the postfix expression ab+c/ is equivalent to (a+b)/c in infix notation
 Your code should take a string of arbitrary length, convert it to postfix and return the equivalent infix expression
* Your Solution should detect invalid expressions and output "invalid" in that case.
* The only valid operators are +, -, *,/ and ^ (exponentiation operator)
* You can assume that all operands are single characters.
* Operands and operators may or may not be separated by spaces.
* Your solution must enclose expression in the minimal set of parentheses to appropriately preserve the order of operations.
```
def post_to_infix(expression):
    prec = :'+': 0, '-' : 0, '*' : 1, "/" : 1, '%' : 1, '^': 2
    stack = []
    for x in expression:
        if x == " ":
          continue 
        if x in prec.keys():
            #['+','-','*','/','%','^']:
            if len(stack) < 2:
              return "invalid"
            op2 = stack.pop()  # pop a wrapped list out
            op1 = stack.pop()
            if len(op2) > 1 and ((prec[op2[1]] < prec[x]) or (prec[op2[1]]== prec[x])):
                op2 = "(%s)" % op2[0]
            else:
                op2 = op2[0]
            if len(op1) > 1 and prec[op1[1]] < prec[x]:
                op1 = "(%s)" % op1[0]
            else:
                op1 = op1[0]
            stack.append(["%s%s%s" % (op1, x, op2), x])
        else:
            stack.append([x])
    if len(stack) != 1: 
      return "invalid"
    return stack.pop()[0]
s = post_to_infix("a b+cd--")
s = post_to_infix("")
print (s)
```
------------------------------------------------------------------------------------------------
 sup
=======
------------------------------------------------------------------------------------------------
 Bucket Sort
===============
------------------------------------------------------------------------------------------------
 252. Meeting Rooms
======================
 Given an array of meeting time intervals consisting of start and end times
 `[[s1,e1],[s2,e2],...]` 
 (si< ei), determine if a person could attend all meetings.
 Example 1:
```
Input:
[[0,30],[5,10],[15,20]]
Output: false
```
 Example 2:
```
Input:[[7,10],[2,4]]
Output:true
```
```
# Definition for an interval.
# class Interval(object):
# def __init__(self, s=0, e=0):
# self.start = s
# self.end = e
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
 :type intervals: List[Interval]
 :rtype: bool
 """
        if not intervals: return True
        intervals.sort(key=lambda x: x.start)
        for i, interval in enumerate(intervals[1:]):
            if interval.start < intervals[i].end:
                return False
        return True
```
```python
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
 :type intervals: List[Interval]
 :rtype: bool
 """
        return all([first.end <= second.start for first, second in 
                zip(sorted(intervals, key = lambda x: x.start), sorted(intervals, key = lambda x: x.start)[1:])
                   ]) if intervals else True
```
------------------------------------------------------------------------------------------------
 75. Sort Colors
===================
 Given an array with _n _objects colored red, white or blue, sort them
 in-place
 so that objects of the same color are adjacent, with the colors in the order red, white and blue.
 Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
 Note:
 You are not suppose to use the library's sort function for this problem.
 Example:
```
Input:
 [2,0,2,1,1,0]
Output:
 [0,0,1,1,2,2]
```
 Follow up:
* A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
* Could you come up with a one-pass algorithm using only constant space?
 Thoughts:
1. Counting Sort
2. Just like the Lomuto partition algorithm usually used in quick sort. We keep a loop invariant that [0,i) [i, j) [j, k) are 0s, 1s and 2s sorted in place for [0,k). Here ")" means exclusive. We don't need to swap because we know the values we want. (
 dietpepsi
 's
 post
 )
 Code: Counting Sort:
```python
class Solution(object):
    def sortColors(self, A):
        """
 :type A: List[int]
 :rtype: void Do not return anything, modify A in-place instead.
 """
        d = collections.defaultdict(int)
        for num in A: d[num]+=1
        i = 0
        for num in xrange(0,3):
            for t in xrange(d[num]):
                A[i] = num
                i+= 1
```
 Code: Partition: one pass
```python
class Solution(object):
    def sortColors(self, A):
        """
 :type A: List[int]
 :rtype: void Do not return anything, modify A in-place instead.
 """
        i = j = 0
        for k, v in enumerate(A):
            A[k] = 2
            if v < 2:
                A[j] = 1
                j+= 1
            if v == 0:
                A[i] = 0
                i+= 1
```
------------------------------------------------------------------------------------------------
 280. Wiggle Sort
====================
 Given an unsorted array
 `A` 
 , reorder it
 in-place
 such that
 `A[0] <= A[1] >= A[2] <= A[3]...` 
 .
 Example:
```
Input:
A = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
```
 Thoughts:
1. Naive: traverse through the element (sort each two element (from [i, i + 2) according to alternative order (ascending vs decending)
2. Window of 2: always ranking A[i-1] and num[i] with the alternating order: when i is odd, then A[i-1] should be <= A[i] when i is even (Excepet 0), A[i-1] should be >= A[i]
 Code
```python
class Solution(object):
    def wiggleSort(self, A):
        """
 :type A: List[int]
 :rtype: void Do not return anything, modify A in-place instead.
 """
        for i in range(len(A)):
            A[i: i+ 2] = sorted(A[i: i + 2], reverse = i%2)
```
 Code
```python
class Solution(object):
    def wiggleSort(self, A):
        """
 :type A: List[int]
 :rtype: void Do not return anything, modify A in-place instead.
 """
        for i in range(len(A)):
            if i%2 == 1:
                if A[i-1] > A[i]:
                    A[i-1], A[i] = A[i], A[i-1]
            elif i != 0 and A[i-1] < A[i]:
                A[i-1], A[i] = A[i], A[i-1]
```
------------------------------------------------------------------------------------------------
 152. Maximum Product Subarray
=================================
 152. Maximum Product Subarray
===============================
 Find the contiguous subarray within an array (containing at least one number) which has the largest product.
 For example, given the array
 `[2,3,-2,4]` 
 ,
 the contiguous subarray
 `[2,3]` 
 has the largest product =
 `6` 
 .
 Thoughts:
 Since two negative numbers multiply could result in positive, here we need to have two arrays, dmax, dmin to keep track of max product and min product so far
 Code
```python
class Solution :
public:
    maxProduct(vector<int>& A) :
        n = A.size()
        if(n == 0) return 0
        if(n == 1) return A[0]
        maxP = A[0]
        for(i  = 1, dmin = A[0], dmax = A[0] i < n i++):
            if(A[i] < 0)
                swap(dmin, dmax)
            dmin = min(A[i], dmin*A[i])
            dmax = max(A[i], dmax*A[i])
            maxP = maxP > dmax? maxP: dmax
        return maxP
```
```python
class Solution :
    public maxProduct(int[] A) :
        if(A == null && A.length == 0) return 0
        #  initial value
        max = A[0], min = A[0], ans = A[0]
        for (i = 1 i < A.length i++):
            prevMin = min, prevMax = max
            max = Math.max(A[i], Math.max(prevMin * A[i], prevMax * A[i]))
            min = Math.min(A[i], Math.min(prevMin * A[i], prevMax * A[i]))
            #  update results
            ans = Math.max(ans, max)
        return ans
```
------------------------------------------------------------------------------------------------
 53. Maximum Subarray
========================
 53. Maximum Subarray
======================
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
 For example, given the array
 `[-2,1,-3,4,-1,2,1,-5,4]` 
 ,
 the contiguous subarray
 `[4,-1,2,1]` 
 has the largest sum =
 `6` 
 .
 click to show more practice.
 More practice:
 If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 Thoughts:
1. Divide and Conquer: For each subarray, calculate four values:
	1. m (largest sum of this subarray),
	2. l (largest sum starting from the left most element),
	3. r (largest sum ending with the rightmost element),
	4. s (the sum of the whole subarray).
2. Greedy: find the largest difference between the sums summing from left to right. The largest difference corresponds to the sub-array with largest sum.
3. DP: dp[i] : max sum till i.
	1. dp[i] = max(dp[i-1], A[i] + dp[i-1])
	2. have a variable to record max dp[i] so far
 Code (DP) Time Complexity O(n), Space Complexity O(n)
```python
class Solution :
public:
    maxSubArray(vector<int>& A) :
        n = A.size()
        if( n == 0 ) return 0
        if(n == 1) return A[0]
        sum = A[0]
        dp [n]  fill_n(dp, n, 0) dp[0] = A[0]
        for ( i = 1 i < n i++):
            dp[i] = dp[i-1] > 0 ? dp[i-1] + A[i]: A[i]
            if(dp[i] > sum) sum = dp[i]
        return sum
```
 Code (Divide and Conquer) Time Complexity O(nlogn), Space Complexity O(nlogn)
```
struct val :
    l, m, r, s
    # m (largest sum of this subarray),
    # l (largest sum starting from the left most element),
    # r (largest sum ending with the rightmost element),
    # s (the sum of the whole subarray).
    val(l, m, r, s):l(l), m(m), r(r), s(s):
class Solution :
public:
    val dac(A[], n) :
        if(n == 1) return val(A[0], A[0], A[0], A[0])
        val v1 = dac(A, n / 2), v2 = dac(A + n / 2, n - n / 2)
        l, m, r, s
        l = max(v1.l, v1.s + v2.l)
        m = max(v1.r + v2.l, max(v1.m, v2.m))
        r = max(v2.r, v1.r + v2.s)
        s = v1.s + v2.s
        return val(l, m, r, s)
    maxSubArray(A[], n) :
        val v = dac(A, n)
        return v.m
```
 Code (Greedy) Time Complexity: O(n), Space Complexity: O(1)
```python
class Solution :
public:
    maxSubArray(A[], n) :
        sum = 0, min = 0, res = A[0]
        for(i = 0 i < n i++) :
            sum += A[i]
            if(sum - min > res) res = sum - min
            if(sum < min) min = sum
        return res
```
------------------------------------------------------------------------------------------------
 269. Alien Dictionary
=========================
 There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of
 non-empty
 words from the dictionary, where
 words are sorted lexicographically by the rules of this new language
 . Derive the order of letters in this language.
 Example 1:
```
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"
```
 Example 2:
```
Input:
[
  "z",
  "x"
]
Output: "zx"
```
 Example 3:
```
Input:
[
  "z",
  "x",
  "z"
] 
Output:""
Explanation: The order is invalid, so return "".
```
 Note:
1. You may assume all letters are in lowercase.
2. You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
3. If the order is invalid, return an empty string.
4. There may be multiple valid order of letters, return any one of them is fine.
 Thoughts:
1. BFS: construct the relative ordering between characters by observing the first
 difference of the character
 from the two consecutive inputs-> Then construct the relative ordering using BFS (with queue)
2. DFS: Check whether there is a cycle in the graph when building the return answer.
	1. state = -1, not exist
	2. 0: Exist. Non-visited.
	3. 1: Visiting
	4. 2: Visited
3. Topological Sort:
 Code: BFS
```python
class Solution :
    public String alienOrder(String[] words) :
        Map <Character, Set<Character>> map = new HashMap<Character, Set<Character>>()
        Map <Character, Integer> level = new HashMap <Character, Integer>()
        for(String word : words)
            for (char c : word.toCharArray())
                level.put(c, 0)
        #  find the dependency by pairwise comparason
        for(i = 0 i < words.length - 1 i++):
            String cur = words[i]
            String next = words[i + 1]
            len = Math.min(cur.length(), next.length())
            #  search for char difference to find the relative order
            for (j = 0 j < len j++):
                char c1 = cur.charAt(j)
                char c2 = next.charAt(j)
                if(c1 != c2):
                    #  put the order into the map
                    Set<Character> set = map.getOrDefault(c1, new HashSet<Character>())
                    if(!set.contains(c2)):
                        set.add(c2)
                        map.put(c1, set)
                        #  increasing the processing priority
                        level.put(c2, level.get(c2) + 1)
                    break
        #  BFS
        Queue<Character> q = new LinkedList<Character>()
        for(char c: level.keySet()) 
            if (level.get(c) == 0) q.add(c)
        String res = ""
        while(!q.isEmpty()):
            char c = q.remove()
            res += c
            #  propagate the dependency, increase its neighbors' priority
            if(map.containsKey(c)):
                for(char succ: map.get(c)):
                    level.put(succ, level.get(succ) - 1)
                    if (level.get(succ) == 0) q.add(succ)
        #  check whether all dependency has been meet: all the priority in level has become 0
        if(res.length() != level.size()) return ""
        return res
```
 Code: DFS
```python
class Solution :
    private final N = 26
    public String alienOrder(String[] words) :
        boolean [][] adj = new boolean [N][N]
        [] visited = new [N]
        StringBuilder sb = new StringBuilder()
        buildGraph(words, adj, visited)
        for(i = 0  i < N i++):
            if(visited[i]==0): #  unvisited
                if(!dfs(adj,visited,sb, i)) return ""
        return sb.reverse().toString()
    private boolean dfs( boolean [][] adj, int[] visited, StringBuilder sb, i):
        visited[i] = 1 #  mark as visiting
        #  checking its neightbor 
        for(j = 0 j < N j++):
            if(adj[i][j]):
                if(visited[j] == 1) return false #  cycle detection
                if (visited[j] == 0): #  only visit unvisited nodes that are "larger" in the ordering
                    if(!dfs(adj, visited, sb, j)) return false
        visited[i] = 2 #  mark as visited
        sb.append((char)(i + 'a'))
        return true
    private void buildGraph(String[] words, boolean[][] adj, int[] visited):
        Arrays.fill(visited, -1)
        for(i = 0 i < words.length i++):
            for(char c: words[i].toCharArray()) visited[c-'a'] = 0
            if(i > 0):
                String w1 = words[i - 1], w2 = words[i]
                len = Math.min(w1.length(), w2.length())
                for(j = 0 j < len j++):
                    char c1 = w1.charAt(j), c2 = w2.charAt(j)
                    if(c1 != c2):
                        #  imposing the ordering
                        adj[c1 - 'a'][c2 - 'a'] = true
                        break
```
 Code: Topological Sort
```
  class Solution(object):
    def alienOrder(self, words):
        """
 :type words: List[str]
 :rtype: str
 """
        # build the graph using greater and less default dict
        smaller = collections.defaultdict(set)
        larger = collections.defaultdict(set)
        for i in range(len(words) - 1):
            minlen = min(len(words[i]), len(words[i + 1]))
            j = 0 
            while j < minlen and words[i][j] == words[i + 1][j]:
                j += 1
            if j < minlen:
                smaller[words[i][j]].add(words[i + 1][j])
                larger[words[i + 1][j]].add(words[i][j])
        # adding free chars
        charset = set(''.join(words))
        res = []
        deque = collections.deque([x for x in charset if x not in larger])
        while deque:
            i = deque.popleft()
            if i in smaller:
                for j in smaller[i]:
                    larger[j].remove(i)
                    if len(larger[j]) == 0:
                        del larger[j]
                        # add into the queue
                        deque.append(j)
            res.append(i)
        # check whether there is still ordering constraints 
        if len(larger) > 0: return ""
        else: return "".join(res)
```
------------------------------------------------------------------------------------------------
 1.   Course Schedule II
=========================
 There are a total ofncourses you have to take, labeled from
 `0` 
 to
 `n - 1` 
 .
 Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair:
 `[0,1]` 
 Given the total number of courses and a list of prerequisite
 pairs
 , return the ordering of courses you should take to finish all courses.
 There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
 For example:
```
2, [[1,0]]
```
 There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is
 `[0,1]` 
```
4, [[1,0],[2,0],[3,1],[3,2]]
```
 There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is
 `[0,1,2,3]` 
 . Another correct ordering is
 `[0,2,1,3]` 
 .
 Note:
1. The input prerequisites is a graph represented by
 a list of edges
 , not adjacency matrices. Read more about
 how a graph is represented
 .
2. You may assume that there are no duplicate edges in the input prerequisites.
 click to show more hints.
 Hints:
1. This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2. Topological Sort via DFS
	* A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via
 BFS
 .
 Thoughts:
1. Similar two
 207. Course Schedule
 except here a vector of order number is expected to be returned
2. BFS (Kahn's Algorithm) vs DFS
 Code (BFS) Time: O(n^2)
```python
class Solution :
public:
    vector<int> findOrder(numCourses, vector<pair<int, int>>& prerequisites) :
        vector<unordered_set<int>> g(numCourses)
        vector<int> degree (numCourses,0)
        vector<int> ans
        #  outward record
        for(auto c: prerequisites):
            g[c.second].insert(c.first)
        #  in-degree record
        for(auto neighbors: g):
            for(neigh: neighbors):
                degree[neigh]++
        for(i = 0  i < numCourses i++):
            j = 0
            for( j < numCourses j++):
                if(!degree[j]) break
            if(j == numCourses):ans.clear() return ans
                degree[j] --
                for(auto neigh: g[j]):
                    degree[neigh]--
            ans.push_back(j)
        return ans
```
 Code (DFS + pruning) Time: O(n)
```python
class Solution :
    num = 0
    vector<int> ans
public:
    vector<int> findOrder(numCourses, vector<pair<int, int>>& prerequisites) :
       vector<unordered_set<int>> g(numCourses) vector <bool> path(numCourses, false)
       vector<int> ind (numCourses, 0) 
        vector<bool> visited (numCourses, false)
        for(auto p: prerequisites):
            g[p.second].insert(p.first)
        for(i = 0 i < numCourses i++):
            if(!visited[i] && dfs_cycle(g, i, path, visited)):
                ans.clear() 
                return ans
        reverse(ans.begin(), ans.end())
        return ans
private:
    bool dfs_cycle(vector<unordered_set<int>> & g, node, vector<bool> & path, vector<bool> & visited):
        if(visited[node]) return false
        path[node] = visited[node] = true
        for(auto neigh: g[node]):
            if(path[neigh] || dfs_cycle(g, neigh, path, visited)):
                return true
        path[node] = false
        cout<<node<<endl
        ans.push_back(node)
        return false
```
------------------------------------------------------------------------------------------------
 1.   Course Schedule
======================
 There are a total ofncourses you have to take, labeled from
 `0` 
 to
 `n - 1` 
 .
 Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair:
 `[0,1]` 
 Given the total number of courses and a list of prerequisite
 pairs
 , is it possible for you to finish all courses?
 For example:
```
2, [[1,0]]
```
 There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
```
2, [[1,0],[0,1]]
```
 There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 Note:
1. The input prerequisites is a graph represented by
 a list of edges
 , not adjacency matrices. Read more about
 how a graph is represented
 .
2. You may assume that there are no duplicate edges in the input prerequisites.
 Hints:
1. This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2. Topological Sort via DFS
	* A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via
 BFS
 .
 Thoughts:
 equivalent to cycle detection problem in topological sort (
 Kahn's algorithm
 vs DFS)
 Code (Kahn's algorithm)
```python
class Solution :
public:
bool canFinish(numCourses, vector<pair<int, int>>& prerequisites) :
        #  make graph outwards
        vector<unordered_set<int>> g(numCourses)
        vector<int> ind (numCourses, 0)
        for(auto p : prerequisites):
            g[p.second].insert(p.first)
        #  record in-degrees for each node
        for(auto p: prerequisites):
            ind[p.first]++
        for(i = 0  i < numCourses i++):
            j = 0
            for( j < numCourses j++):
                if(!ind[j]) break
            if(j== numCourses) return false
            ind[j]--
            for(neigh: g[j]):
                ind[neigh]--
        return true
```
 Code (DFS)
```python
class Solution :
public:
    bool canFinish(numCourses, vector<pair<int, int>>& prerequisites) :
        vector<unordered_set<int>> graph = make_graph(numCourses, prerequisites)
        vector<bool> onpath(numCourses, false), visited(numCourses, false)
        for (i = 0 i < numCourses i++)
            if (!visited[i] && dfs_cycle(graph, i, onpath, visited))
                return false
        return true
private:
    vector<unordered_set<int>> make_graph(numCourses, vector<pair<int, int>>& prerequisites) :
        vector<unordered_set<int>> graph(numCourses)
        for (auto pre : prerequisites)
            graph[pre.second].insert(pre.first)
        return graph
    bool dfs_cycle(vector<unordered_set<int>>& graph, node, vector<bool>& onpath, vector<bool>& visited) :
        onpath[node] = visited[node] = true 
        for (neigh : graph[node])
            #  current node and its child nodes
            if (onpath[neigh] || dfs_cycle(graph, neigh, onpath, visited))
                return true
        #  no neightbor case: leaf node, reset the onpath value so that this node can be re-visit 
        return onpath[node] = false
```
 Special Thanks to jianchaolifighter's solution for referenece
