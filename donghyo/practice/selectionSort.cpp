#include <iostream>
#include <algorithm>

using namespace std;
void SelectionSort(int arr[], int MAX) {
    /* 입력 : A[0:n－1] , n : 정렬할 원소의 개수.
       출력 : A[0:n－1] : 정렬된 배열. */
       
    int i, j;
    int min, temp;
    for(i=0; i<MAX-1; i++) {
        min = i;
        for(j=i+1; j<MAX; j++) {
            if(arr[j] < arr[min]) min = j;
        }
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

int main(){

}

