#include <iostream>
#include <algorithm>

using namespace std;

// C++ STL sort는 QuickSort 기반

void Print(int *arr){
    cout << "arr[i] : " ;
    for(int i=0; i<10; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(){
    int arr[10] = {3, 7, 2, 4, 1, 0, 9, 8, 5, 6};
    int len =sizeof(arr)/sizeof(int);

    Print(arr);
    sort(arr, arr+len);
    Print(arr);

    return 0;

}