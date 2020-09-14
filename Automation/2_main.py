"""
Author : Byunghyun Ban
Last Modification : 2018.12.24.
"""

import os

directory = "personal_info/"         #합칠 파일들이 든 폴더 /: 파일경로표시 (A/B; A폴더 내 B파일들)
outfile_name = "merged_personal_info.csv" #통합 파일의 이름 정하기 + .csv로 저장(.txt도 가능)

out_file = open(outfile_name, 'w')   #open 함수 이용, 통합 파일을 w쓰기모드로 열기
                                     #directory 폴더(personal_info/) 열기
files = os.listdir(directory)        #os.listdir(): 폴더 내 파일이름을 알려주는 함수 (자동화핵심***)
                                     #내용물 스캔 > 리스트 형태로 리턴

# 11~13: personal_inifo/라는 directory 폴더를 찾아가서 그 내용물을 하나하나 스캔 > 파일이름을 몽땅 모아서 리턴해줌
# 이렇게 불러온 리스트는 files라는 이름으로 메모리에 저장됨

for filename in files:                #반복 + os.listdir()로 불러왔던 files를 하나씩 filename이라는 이름을 붙이고 
                                      #files의 마지막 내용물까지 작업에 동원되면 반복 종료
    if ".txt" not in filename:        #검증: filename에 txt 문자가 포함되어 있는지 체크
        continue                      #당장 하던것을 중단하고 반복문의 다음 루프를 실행
    file = open(directory + filename) #personal_info/라는 directory 내의 filename이라는 파일을 불러와 file이라는 이름의 변수로 만듬
    for line in file:                 #반복문 이용, file을 위에서부터 한 줄씩 불러옴 > line이라 붙임
        out_file.write(line)          #불러온 파일을 한 줄씩 out_file에 옮겨 적음 (out_file에 write()함수 이용해서 line입력)
    out_file.write("\n\n")            #엔터 두개
    file.close()                      #불러온 file 닫기
out_file.close()                      #out_file 닫기

#(1) personal_info에 어떤 파일들이 있는지 확인하고
#(2) out_file을 하나 만든 다음
#(3) personal_info에 있는 파일을 하나씩 불러와
#(4) 내용물을 한 줄씩 out_file에 베껴 적는다.
#(5) 모든 파일에 대해서 위 작업을 마쳤으면 out_file도 종료해 준다.

#(1) personal_info 폴더를 열고
#(2) 합쳐진 데이터를 저장할 파일을 하나 만든 다음
#(3) personal_info에 있는 파일을 하나씩 실행해서
#(4) 내용물을 out_file에 베껴 적는다.
#(5) 모든 파일에 대해서 위 작업이 끝나면 out_file을 저장한다.

