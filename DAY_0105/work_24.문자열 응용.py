# #-----------
# # 24.1.1 replace 함수(문자열 변경)
# s='Hello world!'
# s=s.replace('world!','python!')
# print(s)
#
# #24.1.2 문자 바꾸기
# table=str.maketrans('aeiou','12345')
# 'apple'.translate(table)
#
#
# #24.1.3 문자열 분리
#
# #split()은 공백을 기준으로 문자열을 분리하여 리스트로 만듦
# #split('기준문자열') 과 같이 기준 문자열을 지정하면 기준 문자열로 문자열을 분리합니다.
#
# 'apple pear grape pineapple orange'.split()
# 'apple,pear, grape, pineapple, orange'.split(', ')
# print('apple pear grape pineapple orange'.split(', '))
#
# #구 분자 문자열과 문자열 리스트 연결하기 - 문자열.join(리스트)
# ' '.join(['apple','pear', 'grape', 'pineapple', 'orange'])
# print(['apple','pear', 'grape', 'pineapple', 'orange'])
#
# # 특정문자 삭제
# 'football'.lstrip('fo')
#
# #문자열 왼쪽 정렬=> ljust
# #문자열 오른쪽 정렬=> rjust
# # 문자열 가운데 정렬=> center
# 'python'.rjust(10)
# 'python'.ljust(10)
# 'python'.center(10)
#
# # 메서드 체이닝:
# # 메서드를 계속 연결해서 호출하는 메서드 체이닝이 가능.
# 'python'.rjust(10).upper()
#
# #24.1.17  문자열 왼쪽에 0 채우기
# #zfill
# # '35'.zfill(4)=====>4자리
# # '3.5'.zfill(6) ====> 6자리
#
#
# # 24.4 연습문제: 파일 경로에서 파일명만 가져오기
#
# path='C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
# x=path.split('\\')  # 리스트로 나눠줌, 나눠준 부분의 인덱스를 찾으면 됨
# filename=x[-1]
# print(x)
# print(filename)


# 24.5 심사문제:특정 단어 개수 세기
#입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요.
# 모든 문자가 소문자인 the만 찾으면 되며 them,there,their
# 등은 포함하지 않음

# ('the grown-ups response, this time, was to advise me to lay aside '
# 'my drawings of boa constrictors, whether from the inside or the outside,'
# ' and devote myself instead to geography, history, arithmetic, and grammar.'
# ' That is why, at the, age of six, I gave up what might have been '
# 'a magnificent career as a painter. I had been disheartened by the failure '
# 'of my Drawing Number One and my Drawing Number Two. Grown-ups never understand'
# ' anything by themselves, and it is tiresome for children to be always and forever'
# ' explaining things to the.)


#24.6 심사문제 :높은 가격으로 출력하기

# 표준입력으로 물품가격 여러개가 문자열 한줄로 입력되고,각 가격은 ; (세미콜론)으로 구분되어 있습니다.
# price=list(map(int,input().split(';')))
#
# splitlist=price.sort(reverse=True)
# print(splitlist)
# gb h