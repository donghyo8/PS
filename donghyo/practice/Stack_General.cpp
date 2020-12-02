#include <iostream>
#include <stdio.h>

using namespace std;

#define STACK_SIZE 10
int arr[STACK_SIZE]; 
int top = 0; 

int push(int n) { 
    if (top >= STACK_SIZE) return -1; 
    arr[top++] = n; // 파라미터로 전달받는 element를 stack의 top에 추가
    return 0;
}
int pop() {
    if (top<=0) return -1; 
    return arr[--top]; 
}

int main(){
    push(1), push(2), push(3);
    printf("%d %d %d", pop(), pop(), pop());
}