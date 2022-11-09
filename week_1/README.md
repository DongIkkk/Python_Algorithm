Week1
=====
1. 평균 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/12944
2. 짝수와 홀수
https://school.programmers.co.kr/learn/courses/30/lessons/12937
3. 자릿수 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/12931
4. 자연수 뒤집어 배열로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12932
5. 숫자 문자열과 영단어
https://school.programmers.co.kr/learn/courses/30/lessons/81301
6. 체육복
https://school.programmers.co.kr/learn/courses/30/lessons/42862
7. 비밀지도
https://school.programmers.co.kr/learn/courses/30/lessons/17681
8. 약수의 개수와 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/77884
9. 없는 숫자 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/86051
10. 완주하지 못한 선수
https://school.programmers.co.kr/learn/courses/30/lessons/42576

***
### 1. 평균 구하기
그냥 배열의 합을 배열의 길이로 나누어 줬음

변수의 자료형 같은거 고려하지 않는게 맞는건지 모르겠음

### 2. 짝수와 홀수
나머지 연산자 %

한줄로도 써봤음

### 3. 자릿수 더하기
자료형을 바꿔서 더하기

### 4. 자연수 뒤집어 배열로 만들기
map 함수로 요소가 int자료형인 list 만들기

reverse로 배열 뒤집기

### 5. 숫자 문자열과 영단어
영단어와 매칭되는 숫자를 딕셔너리에 넣어두고

입력받은 문자열을 훑으며

숫자라면 그대로 answer에 저장

문자라면 memory라는 변수에 저장

memory라는 변수는 매번 딕셔너리에 키로서 존재하는값인지 알아봄

키로서 존재해서 숫자로 바꿀수있다면 그때 answer에 저장

### 6. 체육복
탐욕법?

일단 reserve랑 lost랑 같은사람있으면 뺀다

reserve 양쪽번호 사람 값이 lost에 있으면 빼줌

다돌려보고 전체학생수 - lost 배열값

가장많은 사람에게 빌려주는게 아님

뒷사람 먼저주는게 유리할수도있으니 뒷사람 주는것도 돌려봄 더좋은결과를 리턴

그래도안됨



```
뒷사람 우선
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    l l   l       l     l  l
   /     /       /     /    \ 
  r     r   r   r    r        r
앞사람 우선
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    l l   l       l     l  l
   /   \   \     /     /    \ 
  r     r   r   r    r        r
```
해결 : 그냥 앞에꺼 부터 지우면 아무상관없음

테스트케이스 7번에서 항상 실패했는데

7번은 여벌의 체육복을 가진 사람이 모두 도난당한 케이스

겹치는 리스트 지울때 저렇게 지우면 index가 밀려서 안된다

겹치는거 지우면서 새로운 리스트를 만들어야함

### 7. 비밀지도
배열로 들어온 값을 이진수로 변환하고 

OR 연산

2진수 변환 bin쓰니까 접두사도붙고 

문제 입력마다 2진수 길이도 달라서(앞에 000~ 붙여야하는거)

문제에맞게 2진수 출력해주는 함수 dec_to_bin 만들어서 진행