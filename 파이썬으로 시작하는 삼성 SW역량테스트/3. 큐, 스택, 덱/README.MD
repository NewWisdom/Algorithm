>https://blog.naver.com/wpghks7/221584442182

# 3. 큐, 스텍, 덱

## 큐 

> 공식 문서 : https://docs.python.org/ko/3/library/queue.html#module-queue

**First - In - First - Out**
* put() : 데이터를 큐의 가장 뒤에 넣는다.
* get() : 큐의 가장 앞에 있는 정수를 빼고 그 값을 반환한다.
* qsize() : 큐에 들어있는 정수의 개수를 반환한다.
* empty() : 큐가 비어있으면 True, 아니면 False를 반환한다.
 * front = q.queue[0]
 * back = q.queue[-1]
큐는 표준 모듈로 사용 가능하다!

* 큐 객체 선언
```
import queue
q = queue.Queue()
```

---
## 스택

**Last - In - First - Out**
* push(n) : n을 스택의 가장 뒤에 넣는다.
* pop() : 스택의 가장 마지막 데이터를 제거한다.
* top() : 스택의 가장 마지막 값을 확인한다.
* empty() : 스택이 비어있는지 확인한다.
* size() : 스택의 크기를 확인한다.


---
## 덱 (Deque)

**양방향 큐**
* append(n) : 덱의 가장 뒤에 n을 삽입한다.
* appendleft(n) : 덱의 가장 앞에 n을 삽입한다.
* pop() : 덱의 가장 마지막 원소를 제거하며 반환한다.
* popleft() : 덱의 가장 처음 원소를 저거하며 반환한다.
* len(dq) : 덱의 길이를 확인한다.

* 덱 객체 선언
```
from collections import deque
dq = deque()
```
