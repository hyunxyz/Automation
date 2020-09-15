import os

directory = "personal_info/"
outfile_name = "merged_personal_info.csv"

out_file = open(outfile_name, 'w')
files = os.listdir(directory)

for filename in files:
    if ".txt" not in filename:
        continue
    file = open(directory + filename)
    for line in file:
        out_file.write(line)    
    out_file.write("\n\n") 
    file.close()
out_file.close()


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