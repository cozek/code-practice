#include <iostream>
#include <string>
using namespace std;

class student {
  private:
    int age;
    string first_name;
    string last_name;
    int standard;

  public:
    void set_age(int a) {
      age = a;
    }
    int get_age(){
      return age;
    }

    void set_first_name(string s) {
      first_name = s;
    }
    string get_first_name(){
      return first_name;
    }

    void set_last_name(string s){
      last_name = s;
    }
    string get_last_name(){
      return last_name;
    }

    void set_standard(int i){
      standard = i;
    }
    int get_standard(){
      return standard;
    }

    string pprint(){
      string pretty = to_string(age) +',' \
                      + first_name + ',' \
                      +last_name + ','
                      +to_string(standard);
      return pretty;
    }
    string get_full_name (){
      string name = last_name + ', ' + first_name;
      return name;
    }



};
int main () {

  student satro;
  int age;
  cin >> age;
  satro.set_age(age);

  string first_name;
  cin >> first_name;
  satro.set_first_name(first_name);

  string last_name;
  cin >> last_name;
  satro.set_last_name(last_name);

  int standard;
  cin >> standard;
  satro.set_standard(standard);

  cout << satro.get_age() <<endl;
  cout << satro.get_full_name() << "\n";
  cout << satro.get_standard() << "\n\n";

  cout << satro.pprint();

}