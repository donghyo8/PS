#include <iostream>
#include <algorithm>


// return -> true or false

using namespace std;

int main(){
    int n = 100;
    int arr[]={0,};

    for(int i=0; i<n; i++){
        arr[i] = i;
    }

    cout << "exist : " <<binary_search(arr, arr+n, 70) << endl;


}