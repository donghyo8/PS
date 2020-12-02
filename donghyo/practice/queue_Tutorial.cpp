#include <iostream>
using namespace std;
// FIFO(먼저 들어간 데이터 먼저 처리)

const int MAX = 1e5;

class Queue {
private:
    int data [MAX];
    int index_front;
    int index_back;
public:
    Queue();
    bool empty();
    void push(int x);
    void pop();
    int front();
    int back();
    int size();
};

Queue::Queue() {
    index_front = 0; // 가장 먼저 넣은 element index
    index_back = 0; // 가장 나중에 넣은 element index
}

bool Queue::empty() {
    return index_front == index_back; // 서로 같으면 element가 없음
}

void Queue::push(int x) {                // ex.) x : element
    index_back = (index_back + 1) % MAX; // back의 index를 증가시키고 큐가 꽉차있는지 확인(공간 계속 사용)
    data[index_back] = x;                // 파라미터로 전달받은 element를 해당 인덱스에 추가
}

void Queue::pop() {
    index_front = (index_front + 1) % MAX; // 가장 먼저 넣은 element를 꺼냄
}

int Queue::front() {
    return data[(index_front + 1) %MAX]; // 가장 먼저 넣은 element를 리턴하여 확인
}

int Queue::back() {
    return data[index_back]; // 가장 나중에 넣은 element를 리턴하여 확인
}

int Queue::size() {
    return (index_back - index_front + MAX) % MAX; // 큐의 element 개수 확인
}

int main(){

}