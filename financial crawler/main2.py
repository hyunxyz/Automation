import OpenDartReader

api_key = '37761bd85d6d64273a3558903e46a2639fb620ae'
dart = OpenDartReader(api_key) 

# 식별 가능하게 지정 = formula 참고
ss_fs = dart.finstate('삼성전자', 2019)
ss_fs_all = dart.finstate_all('005930', 2019)
mult_fs = dart.finstate('005930, 000660, 005380', 2019)
shareholder = dart.report('005930', '최대주주', 2019)

# 엑셀 변환
ss_fs.to_excel("[삼전] 요약 재무제표.xlsx")
ss_fs_all.to_excel("[삼전] 연결 재무제표.xlsx")
mult_fs.to_excel("[3개사] 요약 재무제표.xlsx")
shareholder.to_excel("[삼전] 최대주주.xlsx")
