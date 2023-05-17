f= open("Lab11-1_data.txt","r") #읽기모드로 open

sum = 0
count = 0

for num in f:	#파일의 라인 수
    sum += float(num)  # 반복하여 덧셈
    count += 1  #카운트 증가
avg = sum/count		#합계 나누기 카운트를 하여 평균을 구함

sumstr = "합계=" + str(sum) + '\n'	#저장하기 좋게 정리
avgstr = "평균=" + str(avg) + '\n'	#저장하기 좋게 정리

f2 = open("datao.txt","w") #쓰기모드로 open
f2.write(sumstr)	#합계를 저장함
f2.write(avgstr)	#평균을 저장함

f.close()		#f 닫기
f2.close()		#f2 닫기