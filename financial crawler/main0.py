import dart_fss as dart

# Open DART API KEY 설정
api_key='37761bd85d6d64273a3558903e46a2639fb620ae'
dart.set_api_key(api_key=api_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자 검색
samlip = corp_list.find_by_corp_name('SPC삼립', exactly=True)[0]

# 2019년부터 연간 연결재무제표 불러오기
fs = samlip.extract_fs(bgn_de='20180101')

# 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
fs.save()
