> https://m.blog.naver.com/wpghks7/221598474816

## 5. DFS와 BFS 기초 1

### BFS와 DFS란?

* BFS(Breadth First Search) : 너비 우선 탐색
* DFS(Depth First Search) : 깊이 우선 탐색

BFS는 그래프를 탐색함에 있어 현재 점에서 갈 수 있는 점을 모두 방문하고 퍼지면서 방문하는 반면, DFS는 갈 수 있는 곳 중 한곳을 깊게 들어갔다가 나오며 탐색하는 방법.

**두 방법 모두 그래프를 탐색에 사용한다!**
---

### 중복 없는 순열 구현
* 중복 없는 순열
```
from itertools import permutations
permutations(iterable, r) # r = 몇 개 추출할 건지
```
* 중복 없는 조합
```
from itertools import combinations

```
* 중복 있는 순열 / 각 집단에서 추출
```
from itertools import product
product(iterables, repeat)
```
product 는 첫 인자로 여러 리스트를 받을 수 있다.
repeat만큼 첫 번째 인자를 반복해서 뽑아라.

* 중복 있는 조합
```
from itertools import combinations_with_replacement as com
```

순열은 문제의 사이즈를 유의해서 봐야한다!
순열은 모든 경우의 수를 다 보므로 O(n!) 시간이 걸린다.
1초에 1억번 정도 걸리기 때문에 12! 이상 정도 되면 1초 이상이 걸린다.