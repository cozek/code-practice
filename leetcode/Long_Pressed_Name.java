class Long_Pressed_Name{

  public static boolean isLongPressedName(String name, String typed) {

  if (name.length() == typed.length()){return true;}

  int ptr1=0;
  int ptr2=0;
  int name_len = name.length()-1;
  int typed_len = typed.length()-1;

  while (ptr1 <= name_len && ptr2 <= typed_len){
    // n = name.charAt(ptr1);
    // t = name.charAt(ptr2);
    if (name.charAt(ptr1) == typed.charAt(ptr2)){
       ptr2++;
       ptr1++;
    }else{
        if (typed.charAt(ptr2) == name.charAt(ptr1-1)) {ptr2++;}
        else{return false;}
    }
  }
  if (name.charAt(name_len)!=typed.charAt(typed_len)){
      return false;
  }

  return true;
}
// "sxrmc"
// "sxxrrmmc"
// "pyplrz"
// "ppyypllr"
  public static void main(String[] args) {
    boolean a = isLongPressedName("sxrmc","sxxrrmmc");
    // boolean a = isLongPressedName("pyplrz","ppyypllr");
    // boolean a = isLongPressedName("saeed","ssaaedd");
    System.out.println(a);
  }
}