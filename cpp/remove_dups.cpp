#include <bits/stdc++.h>

class Solution{
public:
  int removeDuplicates(std::vector<int>& nums) {
    //modifies the vector
    if (nums.size()==1){
      return 1;
    }
    auto i{1};
    while(i<nums.size()){
      if (nums[i]==nums[i-1]){
        nums.erase(nums.begin() + i);
        i--;
      }
      i++;
    }
    return nums.size();
  }
};

int main(){

  // std::vector<int> input{0,0,1,1,1,2,2,3,3,4};
  std::vector<int> input{0,0,0,0,0};

  auto sol = Solution();
  auto length = sol.removeDuplicates(input);
  std::cout<< length << std::endl;
  return 0;
}