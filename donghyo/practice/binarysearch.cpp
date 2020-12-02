#include<iostream>
#include<algorithm>

using namespace std;


// 배열의 전체 길이를 반토막내어 중간 값을 선택하고 찾고자 하는 값(X)과 비교
// 값(X)이 중간 값보다 작으면 왼쪽으로 탐색
// 값(X)이 중간 값보다 크면 오른쪽으로 탐색
// 값을 찾을때 까지 반복


// ex.) len =10, searchValue = 5;

bool BinarySearch_Loop(int *arr, int len, int searchValue){
    int mid, count = 0;
    int start = 0; 
    int end = len -1; 

    while(end - start >= 1){

        mid = (start + end) / 2;

        if(arr[mid] == searchValue) {  // 검색 완료
            return true;
        }

        else if(arr[mid] > searchValue){ // 찾는 값이 mid의 값보다 작을 때 왼쪽으로
            end = mid - 1;
        }
        else { // 찾는 값이 mid의 값보다 작을 때 오른쪽으로
            start = mid + 1;
        }
    }
    return false;
}

bool BinarySearch_Recursive(int *arr, int start, int end, int searchValue){
    if(start > end) return false;

    int mid = (start + end) / 2;
    
    if(arr[mid] == searchValue){
        return true;
    }
    else if(arr[mid] > searchValue) {
        return BinarySearch_Recursive(arr, start, mid -1, searchValue);
    }
    else{
        return BinarySearch_Recursive(arr, mid + 1, end, searchValue);
    }

}

int main(){

    int arrTest1[] = {1, 2, 3, 4, 9, 6, 7, 8, 9, 10}; 
    int result1, result2;

    result1 = BinarySearch_Loop(arrTest1, 10, 9);
    cout << "count : " << result1 << endl; 

    result2 = BinarySearch_Recursive(arrTest1, 1, 10, 11);

    cout << "count : " << result2 << endl;

    


}