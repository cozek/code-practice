#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
  std::string numString = "1,2,3,4,5";
  std::stringstream ss(numString);
  std::vector<int> intVec;

  for (int i; ss>>i;) {
    intVec.push_back(i);
    if(ss.peek() == ','){
      ss.ignore();
    }
  }

  for (int i = 0; i<intVec.size(); i++){
    std::cout << intVec[i] <<std::endl;
  }
}
