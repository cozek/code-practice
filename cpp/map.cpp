#include <bits/stdc++.h>

int main() {
  std::unordered_map<std::string, int> m;
  std::unordered_map<std::string,int>::const_iterator it;
  m["hello"] = 1;
  m["world"] = 2;
  m["world"] = 10;
  m["bro"] = 3;

  for (it = m.begin(); it!=m.end(); it++) {
    std::cout << it->first
              << ':'
              << it->second
              << '\n' ;
  }
  return 0;
}
//
// for ( it = symbolTable.begin(); it != symbolTable.end(); it++ )
// {
//     std::cout << it->first  // string (key)
//               << ':'
//               << it->second   // string's value
//               << std::endl ;
// }