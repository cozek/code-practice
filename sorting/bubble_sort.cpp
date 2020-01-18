#include <iostream>
using namespace std;

class BubbleSort
{
    private:
        void swap(int *arr, int i, int j){
            *(arr+i) = *(arr+i) + *(arr+j);
            *(arr+j) = *(arr+i) - *(arr+j);
            *(arr+i) = *(arr+i) - *(arr+j);
        }
    
    public:
        int arr_size = 0;

        void sort(int *arr, int arr_len, bool verbose=false)
        {
            bool is_swap = false;
            
            for (int i = 0; i<arr_len-1; i++)
            {
                if (*(arr+i) > *(arr+i+1))
                {
                    swap(arr, i, i+1);
                    is_swap = true;
                }
            }
            if (verbose){
                print(arr);
            }
            if (is_swap){
                sort(arr, arr_len-1, verbose);
            }
        }
        void print(int *arr)
        {
            for (int i=0; i<arr_size; i++){
                printf("%d | ", *(arr+i));
            }
            printf("\n");
        }
};

int main()
{
    // int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int arr[] = {1, 1, 9, 1, 1, 1, 1};

    int arr_len = sizeof(arr) / sizeof(arr[0]);

    BubbleSort s;
    s.arr_size = arr_len;
    s.sort(arr,arr_len,true);

    return 0;
}