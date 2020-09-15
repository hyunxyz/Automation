import os

directory = "personal_info/"
outfile_name = "merged_personal_info.csv"

out_file = open(outfile_name, 'w')

files = os.listdir(directory)

headers = []                             #header(카테고리;name,age..)를 담아줄 빈 list 생성
outfile_has_header = False               #  outfile_has_header라는 변수 선언 + 이 변수의 값을 false라고 설정
                                         #지금부터 이어질 코드에서는 outfile_has_header가 false이면 out_file에 header를 삽입 (start; 맨 위 카테고리 작성)
                                         #만약 outfile_has_header가 True일 경우 out_file에 header를 삽입하지 않고 넘어감 (컨텐츠 쌓기)

for filename in files:                   #파일이름을 목록에서 하나씩 차례대로 불러옴 > filename 이름 붙임
    if ".txt" not in filename:           #(거름) 파일명에 .txt가 없다면
        continue                         #작업을 건너뛰고 for 루프의 다음 순서로 넘어감
    file = open(directory + filename)    #파일을 위에서부터 하나씩 불러옴 (파일1개 = 사람1명 정보)
                                         ##personal_info/라는 directory 내의 filename이라는 파일을 불러와 file이라는 이름의 변수로 만듬
    contents = []                                   #각 사람들의 개인정보를 저장할 텅 빈 list를 새로 초기화 (contents라는 list는 새로운 파일을 불러올 때 마다 텅 빈 리스트로 정리됨)
    for line in file:                               
        if ":" in line:                             #조건문 (line 내부에 ":"라는 글자가 없으면 작업을 수행하지 않고 건너뜀
            splits = line.split(":")                #split(): 한 줄씩 불러온 string을 ()안에 있는 문자를 기준으로 여러개로 쪼갬 > 2개의 element를 갖는 리스트가 되어 split에 저장됨 
            contents.append(splits[-1].strip())     #splits[0]: header / splits[-1]: contents
                                                    #line의 우측 값에서 좌우 공백을 벗기는 strip 명령어 실행 > 벗은 글자는 contents라는 list에 삽입됨 (append)
            if len(contents) > len(headers):        #  contents와 headers 리스트 길이 비교; '과연 이 파일이 첫번째 순서로 불러온 파일인지 아닌지' 구분 가능
                headers.append(splits[0].strip())   #  for loop가 처음 돌아 첫번째 파일을 읽어오고 있다면 아직 headers는 빈 리스트일 것. 
                                                    #  순서상 한 줄씩 읽어온 데이터는 contents에 먼저 쌓이게 되므로 첫 번째 파일을 읽는 중에는 항상 contents의 길이가 headers의 길이보다 길어 저 조건문은 참이 되고, 두 번째 파일부터는 저 조건문은 항상 거짓이 됨
                                                    #조건문이 참일 경우, 그러니까 첫 번째 순서의 파일을 읽어 오는 동안에는 line의 왼쪽 부분을 strip 해 header에 넣어준다.

    if not outfile_has_header:          #outfile에 헤더가 있는지 검사 "outfile에 헤더를 삽입하는 작업을 이미 끝내 뒀나요?"
        header = ", ".join(headers)     #header 리스트 내의 내용물 사이사이에 "," string을 삽입하여 하나의 string으로 합침
        out_file.write(header)          #Ture (즉 outfile_has_header = false)이면 아래 headers 리스트의 내용물들을 하나의 큰 문자열로 합치며 outfile에 적어줌
        outfile_has_header = True       #outfile_has_header 값을 True로 변경 (이 작업 이미 끝냄)

    new_line = ", ".join(contents)      #contents 리스트 내의 내용물 사이사이에 "," string을 삽입하여 하나의 string으로 합침
    out_file.write("\n" + new_line)     #join()함수를 통해 완성된 new line을 out_file에 적어줌

    file.close()                        #파일 하나를 다 읽을 때마다 해당 파일 종료
out_file.close()                        #out_file 작성이 끝났으므로 파일 종료