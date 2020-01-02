// https://leetcode.com/problems/valid-parentheses/

#include<iostream>
#include<vector>
#include<string.h>

using namespace std;

class Solution{
    public:
        bool isValid(string s){
            // '(', ')', '{', '}', '[' , ']'

            std::vector<char> stack;

            for (char c:s){
                if (stack.empty()){
                    stack.emplace_back(c);
                }
                else{
                    if (stack.back() == '(')
                    {
                        if (c == ')') 
                        {
                            stack.pop_back();
                        }
                        else
                        {
                            stack.emplace_back(c);
                        }
                    }
                    else if (stack.back() == '[')
                    {
                        if (c == ']')
                        {
                            stack.pop_back();
                        }
                        else
                        {
                            stack.emplace_back(c);
                        }
                    }
                    else if (stack.back() == '{')
                    {
                        if (c == '}')
                        {
                            stack.pop_back();
                        }
                        else
                        {
                            stack.emplace_back(c);
                        }
                    }
                    
                    // cout << stack.back();
                }
            }

            if (stack.empty()){
                return true;
            }else{
                return false;
            }
            
        }
};
int main(){
    std::vector<string> test_cases{"[]", "([])", "([)"};

    Solution sol = Solution();
    for (string s:test_cases){
        cout << sol.isValid(s)<< "\n";
    }

    return 0;

}



