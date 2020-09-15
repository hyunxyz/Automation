import os

directory = "personal_info/"
outfile_name = "merged_personal_info.csv"

out_file = open(outfile_name, 'w')

files = os.listdir(directory)

headers = []
outfile_has_header = False

for filename in files:
    if ".txt" not in filename:
        continue
    file = open(directory + filename)

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


# [알고리즘]
# 1. 개인정보를 한 줄씩 불러옴. (그리고 이걸 line이라고 부름)
# 2. ":"라는 글자를 기준으로 line을 둘로 쪼갬. 그러면 첫 번째 줄을 기준으로 "name  ", "  ijfao\n" 두 개의 문자열로 쪼갤 수 있음 (우리 눈에 줄 바꿈으로 보이는 부분은 '\n'이라는 문자가 삽입되어 있음)
# 3. 두 개로 쪼개진 line의 좌측 부분은 모든 파일들이 공통으로 공유하는 양식임 이 데이터는 엑셀로 변환할 때 헤더 역할을 수행하도록 하면 될 것. line의 우측 부분은 각각의 사람들이 가진 고유한 특별한 값이다. 엑셀에서 한 칸씩 이 정보를 옆으로 나열하고, 사람이 바뀌면 엔터키를 한번 쳐 주는 식으로 데이터를 정리하면 됨
# 4. 수천 개의 파일을 순서대로 읽어와서 반복 작업을 수행할 것인데, 이 과정에서 line의 오른쪽 값은 반복해서 out_file에 적어줌
# 5. 단, 첫 번째로 불러온 파일을 읽을 때에는 line의 좌측 값을 header로 설정 (파일이 2000개면 총 2000번 name, sex, age 등의 문자가 등장하는데 이걸 엑셀에도 2000번 반복해 적을 필요는 없으므로 한 번만 작업을 수행하자는 뜻) 엑셀에서는 name, age 등의 값은 맨 윗줄에만 적어 두면 충분
