#include <bits/stdc++.h>
void print(std::vector<int> &v){
  for (auto i = 0; i<v.size(); i++){
    std::cout << v[i] <<' ';
  }
  std::cout << '\n';
}

class Solution {
// public:
//   std::vector<std::vector<int>> threeSum(std::vector<int>& v) {
//
//     std::vector<std::vector<int>> output;
//     if (v.empty()){
//       return output;
//     }
//     std::sort(v.begin(),v.end());
//
//     for (auto i=0; i<v.size()-2; i++) {
//       int low = i+1;
//       int high = v.size()-1;
//       printf("%i %i %i\n",i, low, high );
//
//       int diff = 0 - v[i];
//
//       while (low < high) {
//         int sum = v[low] + v[high];
//         if (sum == diff){
//           std::vector<int> set{v[i],v[low],v[high]};
//           output.emplace_back(set);
//         }
//         while (v[low] == v[low+1]) {low++;}
//         while (v[high] == v[high-1]) {high--;}
//         low++;
//         high--;
//       }
//     }
//     return output;
//   }
};

int main() {
  std::vector<std::vector<int>> output;
  // std::vector<int> v{-1, 0, 1, 2, -1, -4};
  std::vector<int> v{1,0,0,0,-1};

  if (v.empty()){exit(0);}
  if (v.size()<3){exit(0);}
  if (v.size() == 3){
    if (v[0]+v[1]+v[2] == 0){
      std::vector<int> b{v[0],v[1],v[2]};
      output.emplace_back(b);
    }

  }else{
    std::sort(v.begin(),v.end());
    int prev{-90909};

    for (auto i=0; i<v.size()-2; i++) {

      if (prev!=-90909 && v[i] == prev){
        continue;
      }
      int low = i+1;
      int high = v.size()-1;
      printf("%i %i %i\n",i, low, high );

      int diff = 0 - v[i];

      while (low < high) {
        int sum = v[low] + v[high];
        if (sum == diff){
          std::vector<int> set{v[i],v[low],v[high]};
          output.emplace_back(set);
          while (low < high && v[low] == v[low+1]) {low++;}
          while (low < high && v[high] == v[high-1]) {high--;}
          low++;
          high--;
        } else if(sum < diff){
          low++;
        } else{
          high--;
        }
      }
      prev = v[i];

    }
  }

  std::cout << "outputs:\n";
  for (auto j=0;j<output.size(); j++){
    print(output[j]);
  }
}