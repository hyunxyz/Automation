from urllib.request import urlopen

crtfc_key = "37761bd85d6d64273a3558903e46a2639fb620ae"
corp_code = "00125530"
bsns_year = "2019"
reprt_code = "11011"   #사업보고서

url="https://opendart.fss.or.kr/api/alotMatter.json?crtfc_key={}" \
    "&corp_code={}&bsns_year={}&reprt_code={}".format(crtfc_key,corp_code,bsns_year,reprt_code)

req=urlopen(url)
result=req.read()