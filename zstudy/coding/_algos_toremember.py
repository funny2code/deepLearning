
###################################################################################################### 
########### Strin problem ############################################################################

        Parenthesis problem:-

            1.https://leetcode.com/problems/generate-parentheses
            2.https://leetcode.com/problems/score-of-parentheses
            3.https://leetcode.com/problems/valid-parentheses
            4.https://leetcode.com/problems/valid-parentheses Easy
            5.https://leetcode.com/problems/remove-outermost-parentheses Easy
            6.https://leetcode.com/problems/different-ways-to-add-parentheses/ Medium
            7.https://leetcode.com/problems/remove-invalid-parentheses Hard
            8.https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses Medium
            9.https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses Easy

        Counting of substring based on some condition:-

            1.https://leetcode.com/problems/number-of-wonderful-substrings Medium
            2.https://leetcode.com/problems/sum-of-beauty-of-all-substrings/ Medium
            3.https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring Medium
            4.https://leetcode.com/problems/number-of-wonderful-substrings Medium

        Check types of string:-

            1.https://leetcode.com/problems/isomorphic-strings Easy
            2.https://leetcode.com/problems/valid-anagram Easy
            3. https://leetcode.com/problems/additive-number Medium
            4.https://leetcode.com/problems/buddy-strings Easy
            5.https://leetcode.com/problems/longest-happy-prefix Hard
            6.https://leetcode.com/problems/increasing-decreasing-string Easy
            7.https://leetcode.com/problems/check-if-a-string-can-break-another-string Medium
            8.https://leetcode.com/problems/determine-if-two-strings-are-close Medium
            9.https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent Easy
            10.https://leetcode.com/problems/check-if-word-equals-summation-of-two-words Easy
            11.https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal Easy

        **Palindromic string:- **

            1.https://leetcode.com/problems/palindrome-partitioning Medium
            2.https://leetcode.com/problems/palindrome-partitioning-ii Hard
            3.https://leetcode.com/problems/valid-palindrome Easy
            4.https://leetcode.com/problems/shortest-palindrome Hard
            5.https://leetcode.com/problems/palindrome-pairs Hard
            6.https://leetcode.com/problems/longest-palindrome Easy
            7.https://leetcode.com/problems/longest-palindromic-subsequence Medium
            8.https://leetcode.com/problems/find-the-closest-palindrome Hard
            9.https://leetcode.com/problems/palindromic-substrings Medium
            10.https://leetcode.com/problems/valid-palindrome-ii Easy
            11.https://leetcode.com/problems/longest-chunked-palindrome-decomposition Hard 12.https://leetcode.com/problems/break-a-palindrome Medium
            13. https://leetcode.com/problems/can-make-palindrome-from-substring Medium
            14.https://leetcode.com/problems/palindrome-partitioning-iii Hard
            15.https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome Hard
            16.https://leetcode.com/problems/remove-palindromic-subsequences Easy
            16.https://leetcode.com/problems/construct-k-palindrome-strings Medium
            17.https://leetcode.com/problems/split-two-strings-to-make-palindrome Medium

        Sorting on String:-
            1.https://leetcode.com/problems/sort-characters-by-frequency Medium
            2.https://leetcode.com/problems/custom-sort-string

        Longest and shortest kind of String Problem :-

            https://leetcode.com/problems/longest-duplicate-substring Hard
            2.https://leetcode.com/problems/longest-string-chain Medium
            3.https://leetcode.com/problems/longest-common-subsequence Medium
            4.https://leetcode.com/problems/longest-happy-string Medium
            5.https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters Medium
            6.https://leetcode.com/problems/find-longest-awesome-substring Hard
            7.https://leetcode.com/problems/largest-substring-between-two-equal-characters Easy
            8.https://leetcode.com/problems/largest-odd-number-in-string Easy





################################################################################################                                                
################################################################################################   
        #LIS: Longest increasing subsequence 
        #There is an algorithm for computing the LIS using dp, various implementations are found
        #### Srandard implementation of LIS using DP.
        def lenght_LIS(self, nums):
            ### Lenght of longest sub-array
            
            dp = [10**10] * (len(nums) + 1)
                        
            for elem in nums: 
              dp[bisect(dp, elem)] = elem  #### insert elent in correct order in Log(n)    , bisect(list, elt) : find index where to insert
                          
            return dp.index(10**10)  ####Location of the biggest numner == Length longest increasing sub-array







################################################################################################                                                
    k-largest in stream :  heap (ordered), 

        #### idea :
        heap : head[0] = min == k-largest element  , heap size k 
        build the heap to ensure heap[0] == k-largest
        heappushpop(heap1, val)  ## val > min




################################################################################################                                                
    k-largest in fixed array :
       Binary search  in Log(n)





Complexity: time complexity is O(n) in average, because on each time we reduce searching range approximately 2 times. This is not strict proof, for more details you can do some googling. Space complexity is O(n) as well.

class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]








