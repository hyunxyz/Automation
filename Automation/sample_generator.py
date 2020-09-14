"""
Author : Byunghyun Ban
Last Modification : 2018.12.24.
"""
import time
import random
import os

ALPHABET_SAMPLES = "abcdefghijklmnopqrstuvwxyz"

# number of samples
NUM_SAMPLES = 200

# a function to generate random string
def random_string(length): #def라는 함수 생성  #이름: random_string #함수에 length녀석을 입력
    result = ""            #result라는 곳에 지금부터 글자를 적을 것 
    for i in range(length): #for i in range=반복; length번만큼 아래 작업 반복해 
        result += random.choice(ALPHABET_SAMPLES) #임의 알파벳을 하나 골라 result에 이어붙여줘
    return result #반복이 끝났으면 result를 리턴해줘


# make a directory for sample files
os.mkdir("personal_info")   #라는 폴더 생성


# generating sample information
for i in range(NUM_SAMPLES):  #28~36 명령어 반복        
               #파일이 저장될 폴더   #랜덤알파벳3글자  #랜덤숫자;현재시각; 5글자   #확장자
    filename = "personal_info/" + random_string(3) + str(time.time())[-5:] + ".txt" 
    outfile = open(filename, 'w')  #파일생성 open(파일이름, 파일 w;쓰기모드)
    outfile.write("name : " + random_string(5) + "\n") #\n 줄바꾸는 escape code
    outfile.write("age : " + str(time.time())[-2:] + "\n")
    outfile.write("e-mail : " + random_string(8) + "@needle.worm\n")
    outfile.write("division : " + random_string(3) + "\n")
    outfile.write("telephone : 010-" + str(time.time())[-4:] + "-" + str(time.time())[-6:-2] + '\n')
    outfile.write("sex : " + random.choice(["male", "female", "others"]))
    outfile.close()
