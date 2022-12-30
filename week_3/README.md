Week3
=====
1. 문자열 내 p와 y의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/12916
2. 핸드폰 번호 가리기
https://school.programmers.co.kr/learn/courses/30/lessons/12948
3. 제일 작은 수 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12935
4. 콜라츠 추측
https://school.programmers.co.kr/learn/courses/30/lessons/12943
5. 수박수박수박수박수박수
https://school.programmers.co.kr/learn/courses/30/lessons/12922
6. 가운데 글자 가져오기
https://school.programmers.co.kr/learn/courses/30/lessons/12903
7. 올바른 괄호 - 스택/큐
https://school.programmers.co.kr/learn/courses/30/lessons/12909
8. H-index - 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/42747
9. 폰켓몬 - 해시
https://school.programmers.co.kr/learn/courses/30/lessons/1845
10. 다트 게임
https://school.programmers.co.kr/learn/courses/30/lessons/17682


***
### 1. 문자열 내 p와 y의 개수
count 함수를 써서 p와 y의 개수를 찾아줌

### 2. 핸드폰 번호 가리기
핸드폰 번호 뒤에서 4자리를 자른만큼 결과값에 * 개수를 넣어주고

남은 4자리의 번호를 붙여주었다

### 3. 제일 작은 수 제거하기
min 으로 최솟값을 찾은 후 remove로 제거, 리스트가 비어있다면 [-1] 반환

### 4. 콜라츠 추측
콜라츠 함수를 만들어 재귀를 이용했음

카운트가 500이되거나 num값이 1이될때 까지 함수를 반복

### 5. 수박수박수
answer에 수박을 n/2 만큼 넣어주고 홀수일땐 모자란 글자 하나를 넣어줌

### 6. 가운데 글자 가져오기
문자열의 길이를 2로 나눠 정수형으로 받아주면 slicing_number를 구할 수 있음

홀수일 땐 해당 인덱스 값을 가져오고 짝수면 slicing_num-1부터 slicing_num까지 두 문자를 가져옴

### 7. 올바른 괄호
for문 돌면서 '('를 만나면 count+1 ')'를 만나면 -1을 해줘서 짝이맞으면 count=0이 될것임

count에 따라 참거짓 판별

count가 한번이라도 -1로 떨어진다는 것은 닫는 괄호가 먼저 나온것이므로

짝이 맞을 수가 없음 이때는 for문 break되게 바로 false 반환

### 8. H-index
일단 큰수부터 앞으로 오도록 역순정렬

앞에서 부터 for문 돌면서 '해당 논문 인용된 숫자'보다 

'위치해 있는 인덱스번호+1(자신만큼 인용이 많이 된 논문의 수)'

가 같거나 크다면 그 숫자는 h-index가 될 수 있다.

-> 인덱스 번호로 하면 중복된 수 때문에 정확하지않음 (index를 쓰면 앞에있는 요소의 인덱스번호가 우선)

for문 한번에 count+1로 인덱스값을 대신함

### 9. 폰켓몬
얼마나 다양한 포켓몬을 가져오느냐 - 중복은 제거 set함수 사용

아무리 다양해도 가져올수 있는 마리수는 전체의 반이기때문에 set적용한 길이가 마리수를 초과하면

최대마리수를 반환, set적용해도 마리수보다 작다면 set한 리스트의 길이를 반환

### 10. 다트게임
계산할 수를 세 구역 x, y, z 로 나누어서

count값에따라 x, y, z를 계산함

숫자는 0부터 10까지 나올수 있는데 10인경우를 예외로두기위해

현재들어온 요소가 숫자 + 다음 들어올 요소가 0일 때 >> 값을 10으로 넣어준다.

문자가 들어올 경우 해당문자에 맞는 계산을 하고

문자뒤에 숫자가 오는 경우에만 count를 올려준다.