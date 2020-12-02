// 1. vector의 생성자와 연산자



// vector<[data type]> a;  : 비어있는 vector a를 만든다

// vector<[data type]> a(10);  : 기본값으로 초기화 된 10개의 원소를 가지는 vector a를 만든다

// vector<[data type]> a(10, 초기화값);  : 지정한 초기값으로 된 10개의 원소를 가지는 vector a를 만든다

// vector<[data type]> b(a); : vector b는 vector a를 복사해서 만든다

// vector들이 있을 때 내부의 인자들끼리 연산은 '==', '!=', '<', '>', '<=', '>=' 로 비교할 수 있다


// 2. vector 함수

// vector<int> v; 를 만들었다고 생각하고 함수를 사용해보겠다!



// v.assign(10, 1) : 1이라는 값으로 10개의 원소에 할당

// v.at(i) : i번째 원소를 return한다 vector의 범위를 체크하므로 []로 참조하는 것보다 느림

// v[i] : i번째 원소를 return한다 범위를 체크하지않으므로 at보다 빠름

// v.front() : 첫번째 원소를 return 한다

// v.back() : 마지막 원소를 return 한다

// v.clear() : 모든 원소를 제거한다(메모리공간은 남아있다) -> 빈컨테이너로 만든다

// v.push_back(5) : 마지막 원소 뒤에 5를 삽입한다

// v.pop_back() : 마지막 원소를 제거

// v.begin() : 첫번째 원소를 가리키는 반복자를 return

// v.end() : 마지막 원소를 가리키는 반복자를 return 

// v.rbegin(), b.rend() : reverse begin, reverse end


// v.reserve(n) : n개의 원소를 저장할 공간을 예약(미리 동적할당)

// v.resize(n) : vector의 크기를 n으로 변경, 더 커질경우 0으로 초기화

// v.resize(n, 1) : vector의 크기를 n으로 변경하고 더 커질경우 1로 초기화

// v.size() : vector 원소의 개수를 return

// v.capacity() : 할당된 공간의 크기를 return

// v2.swap(v1) : v1과 v2의 원소와 capacity를 바꿔줌

// v.insert(3, 4) : 3번위치에 값 4를 삽입, 삽입한 곳의 반복자 return

// v.insert(3, 4, 5) : 3번 위치에 4개의 값 5를 삽입

// v.erase(반복자) : 반복자가 가리키는 원소를 제거

// v.empty() : vector가 비어있는지를 본다 비어있으면 true

