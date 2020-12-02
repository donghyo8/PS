#include <iostream>
#include <algorithm>

using namespace std;



void BubbleSort(int arr[], int len){
    int i, j;
    for(i=1; i<=len; i++){
        for(j=0; j<=len-i; j++){
        if(arr[j] > arr[j+1]){
            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
        }
        }
        cout << arr[i] << endl;
        
    }
}

int main(){
    int arr[] = {10,9,8,7,6,5,4,3,2,1};
    int len =sizeof(arr)/sizeof(int);
    BubbleSort(arr, len);
}

