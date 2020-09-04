> https://m.blog.naver.com/wpghks7/221585604878

## 4. 순열과 조합

### 순열과 조합의 개념

* 순열 : 순서를 신경 쓰며 뽑는 방식
* 조합 : 순서에 상관없이 뽑는 방식

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