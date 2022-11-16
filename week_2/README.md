Week2
=====
1. 두 정수 사이의 합
https://school.programmers.co.kr/learn/courses/30/lessons/12912
2. 문자열을 정수로 바꾸기
https://school.programmers.co.kr/learn/courses/30/lessons/12925
3. 정수 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12933
4. 나머지가 1이 되는 수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/87389
5. 음양 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/76501
6. 예산
https://school.programmers.co.kr/learn/courses/30/lessons/12982
7. k번째수
https://school.programmers.co.kr/learn/courses/30/lessons/42748
8. 같은 숫자는 싫어
https://school.programmers.co.kr/learn/courses/30/lessons/12906
9. 실패율
https://school.programmers.co.kr/learn/courses/30/lessons/42889
10. 소수만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12977

***
### 1. 두 정수 사이의 합
그냥 더해주기 sum(range())

조건에 대소관계는 정해져있지 않다 문제잘읽기

### 2. 문자열을 정수로 바꾸기
부호만 따로빼서 if문으로 나눠줬는데

파이썬에서는 그냥 int(str)해줘도 되나보다 

### 3. 정수 내림차순으로 배치하기
정렬 sort, sorted

join

### 4. 나머지가 1이 되는 수 찾기
2부터 다넣어봄

### 5. 음양 더하기
zip 활용해보기

### 6. 예산
오름차순으로 정렬후 

한부서의 예산을 차례대로 전체예산에서 빼줌 더이상 뺄 수 없을때까지

### 7. k번째 수
리스트를 슬라이싱한 후 정렬

### 8. 같은 숫자는 싫어
리스트에서 요소 하나씩 꺼내서 리턴할 리스트의 마지막 요소와 다르면 넣어줌

### 9. 실패율
딕셔너리에 key = stage : value = 실패율 의 형태로 저장해줌

stage 값은 1부터 입력된 N까지의 값

실패율은 [스테이지에 머무는 사람] / [해당 스테이지에 도달한 총 도전자. len(stages)]

도전자는 스테이지가 올라갈때 마다 이전 스테이지에 머무르던 사람 수를 빼줘야한다

--> 런타임 에러

처음 고려하지 못한점 : 사람수가 0인경우 나눠줄 수 없음
 
-> 해결: 사람이 0일땐 실패율 0

생성된 딕셔너리를 value값 기준 내림차순으로 정렬
```
sorted_fail_dic = sorted(fail_dic, key=lambda x: fail_dic[x], reverse=True)
```

### 10. 소수만들기
주어진 배열에서 3개의 수를 뽑아 만들수있는 숫자들로 새로운 리스트를 만든다

그 리스트에서 소수가 몇개인지 판별한다.

배열에서 3개 뽑아 리스트만들기 -> 조합 combinations 사용

소수 판별할 때는 2부터 판별할 수의 제곱근까지만 판별해보면 된다.

약수는 제곱근 기준으로 대칭이기때문에





