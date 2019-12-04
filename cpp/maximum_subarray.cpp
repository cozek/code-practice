#include <bits/stdc++.h>
/*
Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/
class Solution{
private:
  int lowest = std::numeric_limits<int>::lowest();
public:
  int maxSubArray(std::vector<int>& nums){
    if (nums.empty()){return 0;}
    if (nums.size()==1){return nums[0];}
    int best = nums[0];
    int current = nums[0];
    for (int x:nums){
      current = std::max(x,current+x);
      best = std::max(best,current);
    }
    return best;
  }

  int maxSubArray2(std::vector<int>& nums){
    if (nums.empty()){return 0;}
    if (nums.size()==1){return nums[0];}
    int best = 0;
    int current = 0;
    bool all_negative = true;
    int min = std::numeric_limits<int>::lowest();
    for (int i=0; i<nums.size(); i++){
      if (nums[i] > 0) {all_negative = false;}
      if (all_negative) {
        if (nums[i]>min) {
          min = nums[i];
        }
      }
      std::cout << nums[i] << "+"<<current<<'=';
      current = std::max(0,current+nums[i]);
      std::cout << current<<'\n';
      best = std::max(best,current);
    }
    if (all_negative){return min;}
    return best;
  }
};

int main(){
  // std::vector<int> nums{-2,1,-3,4,-1,2,1,-5,4};
  std::vector<int> nums{-1,-1,0};

  auto sol = Solution();

  int a = std::numeric_limits<int>::lowest();
  // std::cout << a;
  std::cout << sol.maxSubArray2(nums)
            << '\n';
  return 0;
}