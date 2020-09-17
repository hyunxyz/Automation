import datetime
import dart_fss as dart

api_key='37761bd85d6d64273a3558903e46a2639fb620ae'
dart.set_api_key(api_key=api_key)

# 현재 날짜 불러오기
now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d%H%M')
# 검색 시작 날짜
bgn_de = '20200101'
# 검색 종료 날짜
end_de = now.strftime('%Y%m%d')

# 모든 상장된 기업 리스트 불러오기
corp_list = dart.get_corp_list()

# 원하는 기업이름 입력
corp_name = '삼성전자'
corp_code = corp_list.find_by_corp_name(corp_name=corp_name)[0]
corp_code = corp_code._info['corp_code']

# 2019년 01월 01일에 올라온 연결재무제표부터 현재까지 검색
# 사업 보고서
fs = dart.fs.extract(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de, lang='ko', separator=False)
# 반기 보고서 [report_tp='half']
# fs = dart.fs.extract(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de, report_tp='half', lang='ko', separator=False)
# 분기 보고서 [report_tp='quarter']
# fs = dart.fs.extract(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de, report_tp='quarter', lang='ko', separator=False)

# 재무제표 일괄저장 (default: 실행폴더/fsdata/{corp_code}_{report_tp}.xlsx)
filename = corp_name + '_' + nowDate + '.xlsx'
# path = 'C:/Users/User/hb_jeong/Desktop/'
fs.save(filename=filename)