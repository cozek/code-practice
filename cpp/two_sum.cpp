#include <bits/stdc++.h>

class Solution {
private:
  std::unordered_map<int, std::vector<int>> make_map(
    std::vector<int> & nums
  ){
    std::unordered_map<int, std::vector<int>> int_map;
    for (auto i=0; i<nums.size(); i++){
      if (int_map.find(nums[i]) == int_map.end()){
        //not present
        std::vector<int> v{i};
        int_map[nums[i]] = v;
      }
      else{
        //present
        int_map[nums[i]].emplace_back(i);
      }
    }
    return int_map;
  }

public:
  void print(std::unordered_map<int, std::vector<int>> my_map) {
    // std::unordered_map<int, std::vector<int>>::const_iterator it;
    for (auto it = my_map.begin(); it!=my_map.end() ; it++) {
      std::cout << it->first
                << ':';
      for (auto i =0; i<it->second.size(); i++){
        std:: cout << it->second[i]
                   << ',';
      }
      std::cout << '\n';
    }
  }
  std::vector<int> twoSum(std::vector<int>& nums, int target) {
      auto my_map = make_map(nums);
      std::vector<int> v;
      // print(my_map);

      for (auto i=0;i<nums.size();i++){
        int diff = target - nums[i];
        if (my_map.find(diff) != my_map.end()){
          if (my_map[diff][0]!= i){
            v = {i,my_map[diff][0]};
            break;
          }
          else if (my_map[diff][0]== i
            && my_map[diff].size() != 1){
            v = {my_map[diff][0],my_map[diff][1]};
            break;
          }
          else{
            continue;
          }
        }
      }
      return v;
    }
};
int main() {
  std::vector<int> v{2,7,11,15};
  int target{9};
  // std::vector<int> v{3,3};
  // int target{6};
  Solution a = Solution();
  std::vector<int> ans = a.twoSum(v,target);

  for (auto i=0;i<ans.size(); i++){
    printf("%d ", ans[i]);
  }
  return 0;
}