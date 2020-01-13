#include <iostream>
#include <limits>
using namespace std;

class SelectionSort
{
    /* 
    Sorts an array in ascending order using selection sort
    */
public:
    void swap_elem(int *arr, int &idx1, int &idx2)
    {
        int temp = *(arr + idx1);
        *(arr + idx1) = *(arr + idx2);
        *(arr + idx2) = temp;
    }
    void print_arr(int *arr, int arr_len)
    {
        for (int i = 0; i < arr_len; i++)
        {
            cout << *(arr + i)
                 << " ";
        }
        cout << "\n";
    }
    void sort(int *arr, int &arr_len, bool verbose = false)
    {
        for (int i = 0; i < arr_len; i++)
        {
            int min_val = *(arr+i);
            int jmin = i;
            for (int j = i; j < arr_len; j++)
            {
                if (*(arr + j) < min_val)
                {
                    min_val = *(arr+j);
                    jmin = j;
                }
            }
            if (jmin!=i){
                swap_elem(arr, i, jmin);
            }

            if (verbose)
                print_arr(arr, arr_len);
        }
        print_arr(arr, arr_len);
    }
};



int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int arr_len = 5;
    SelectionSort s;
    s.sort(arr, arr_len);
    return 0;
}