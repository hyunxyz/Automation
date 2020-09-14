import os

directory = "personal_info/"
outfile_name = "merged_personal_info.csv"

out_file = open(outfile_name, 'w')

files = os.listdir(directory)

headers = []
outfile_has_header = False

for filename in files:                   #파일이름을 목록에서 하나씩 차례대로 불러옴 > filename 이름 붙임
    if ".txt" not in filename:           #파일명에 .txt가 없으면 
        continue                         #작업을 건너뛰고 for 루프의 다음 순서로 넘어감
    file = open(directory + filename)    #파일을 위에서부터 하나씩 불러옴 (파일1개 = 사람1명 정보)
                                         ##personal_info/라는 directory 내의 filename이라는 파일을 불러와 file이라는 이름의 변수로 만듬
    contents = []
    for line in file:
        if ":" in line:
            splits = line.split(":")
            contents.append(splits[-1].strip())
            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    if not outfile_has_header:
        header = ", ".join(headers)
        out_file.write(header)
        outfile_has_header = True

    new_line = ", ".join(contents)
    out_file.write("\n" + new_line)

    file.close()
out_file.close()