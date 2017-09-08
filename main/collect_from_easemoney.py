import urllib
import urllib.request
import re
import http.cookiejar
from http import cookiejar

test_url="http://www.baidu.com"

url_entry="http://fund.eastmoney.com/fund.html"

url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1^&lx=1^&letter=^&gsid=^&text=^&sort=zdf,desc^&page=1,9999^&feature=^|^&dt=1504853601803^&atfc=^&onlySale=0" 
#-H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-CN,zh;q=0.8" 
#-H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36" 
#-H "Accept: */*" 
#-H "Referer: http://fund.eastmoney.com/fund.html" 
#-H "Cookie: emstat_bc_emcount=17968619252306431716; st_pvi=89210540364576; Hm_lvt_557fb74c38569c2da66471446bbaea3f=1488341793,1488350457; qgqp_b_id=34812500607441202161; HAList=a-sz-002253-^%^u5DDD^%^u5927^%^u667A^%^u80DC^%^2Cp-sz-834255-^%^u4E0A^%^u8BAF^%^u4FE1^%^u606F^%^2Cg-0-AU1706-^%^u6CAA^%^u91D11706^%^2Cg-0-RU1705-^%^u6A61^%^u80F61705^%^2Cg-0-CU1702-^%^u6CAA^%^u94DC1702^%^2Cg-0-CUM-^%^u6CAA^%^u94DC^%^u4E3B^%^u529B^%^2Cg-0-AUM-^%^u6CAA^%^u91D1^%^u4E3B^%^u529B^%^2Ca-sz-300104-^%^u4E50^%^u89C6^%^u7F51^%^2Cg-0-RBM-^%^u87BA^%^u7EB9^%^u94A2^%^u4E3B^%^u529B^%^2Cg-0-jmm-^%^0A^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^20^%^u7126^%^u7164^%^u4E3B^%^u529B^%^2Cg-0-CM-^%^u7389^%^u7C73^%^u4E3B^%^u529B; em_hq_fls=old; _ga=GA1.2.283159655.1482490084; emstat_ss_emcount=0_1501667660_1814926519; st_si=69507833208416; ASP.NET_SessionId=cwtp5x455ado3ovjqtcd3paj" 
#-H "Connection: keep-alive" --compressed

cookie_filename="cookie.txt"


if __name__ == '__main__':
    
    print("*****************************")
    print("visit:"+url_entry)
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    handler=urllib.request.HTTPCookieProcessor(cookie)
    
    opener = urllib.request.build_opener(handler)
    
    headers={
        "Accept-Encoding":"gzip, deflate",
        'Accept-Language':"zh-CN,zh;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Accept":"*/*",
        "Referer":"http://fund.eastmoney.com/fund.html",
        "Connection":"keep-alive"
        }
   # opener.addheaders(headers)
    
    entry_response =opener.open(url)
    
    print("***************************")
    print("save cookie")
    for item in cookie:
        print("name="+item.name)
        print("value="+item.value)
    
    cookie.save(cookie_filename,True, True)
    
    
    
    result = opener.open(url)
    print(result.read())
    
    
    print()
    

