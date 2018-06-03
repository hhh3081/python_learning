import requests
from lxml import etree
import re
import time
import pymysql
#1. 打开数据库
con=pymysql.connect("localhost","root","root","huhuide",charset="utf8")
cursor=con.cursor()
###创建表ctrip
table = 'create table ctrip (id int auto_increment primary key,title varchar(255) not null,number varchar (255),price varchar(255),provider varchar(255),comment varchar(255),schedule longtext,route1 longtext,route2 longtext);'
cursor.execute(table)
con.commit()
#2. 利用循环获得多个主页面的url
def get_urllist(url_list):
    for i in range(1,33):
        url = "https://vacations.ctrip.com/tours/r-europe-120002/dc28p{}#_flta".format(i)
        ###把循环的得到的url添加到url_list
        url_list.append(url)
    return url_list
#3. 对每个主页面发送requests请求，并提取所有的url链接，再添加到列表
def tourism_url(url_list,all_url):
    for i in url_list:
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response=requests.get(i,headers=headers,timeout=60)
        response.encoding="utf-8"
        html_str=response.text
        ###用etree把html字符串转换成html对象
        html=etree.HTML(html_str)
        ###用xpath提取每个旅游团所对应的链接
        web =html.xpath('//*[@id="_prd"]//div[@class="product_main"]/h2/a/@href')
        ###补全web链接
        web_url = ["https:"+i for i in web]
        ###把web_url添加到列表
        all_url.append(web_url)
        time.sleep(8)
    return all_url
#4. 对上一步所得到的list做循环，拿到单个的url，并发送requests请求，再提取数据并保存到数据库
def extract_data(all_url,item,content_list):
    for list in all_url:
        for url in list:
            ###解析单个url，提取相关数据
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            response = requests.get(url, headers=headers, timeout=60)
            response.encoding = "utf-8"
            html_str = response.text
            html = etree.HTML(html_str)
            time.sleep(2)
            try:
                # 旅行团名称
                item["title"] = html.xpath('//*[@id="base_bd"]/div[1]/div[2]/div[2]/div[1]/h1/text()')[0].lstrip( "\r\n            ").rstrip("\r\n            ")
                time.sleep(2)
                # 出游人数
                item["number"] = html.xpath('//*[@id="js_main_price_wrap"]/div[1]/span/text()')
                time.sleep(2)
                # 旅游团的最低价列表
                pp = re.compile(r'\<span class=\"base\_price\"\>\<dfn\>\&yen\;\<\/dfn\>\<strong\>(\d*?)\<\/strong\>(.*?)\<\/span>')
                price = re.findall(pp, html_str)
                item["price"] = ["".join(i) for i in price]
                time.sleep(2)
                # 旅游团的供应商和旅游主题
                pr = re.compile(r'\<i class=\"other\_travel\"\>\<\/i\>\<span title=\"(.*?)\"\>(.*?)\<\/span\>\<\/dd\>')
                provider = re.findall(pr, html_str)
                item["provider"] = [":".join(i) for i in provider]
                time.sleep(2)
                # 评价
                item["comment"] = re.findall(r'<em>([\d.]+)</em>', html_str)
                time.sleep(2)
                # 行程
                item["schedule"] = re.findall(r'</i><span>(.*?)</span><i class', html_str)
                time.sleep(2)
                # 路线1
                item["route_1"] = html.xpath('//*[@id="js_detail"]/div/div/dl/dd/ul/li/p/em/text()')
                time.sleep(2)
                # 路线2
                item["route_2"] = html.xpath(
                    '//*[@id="js_detail"]/div[4]/div[1]/dl[1]/dd/text()|//*[@id="js_detail"]/div[4]/div[1]/dl[2]/dd/ul/li/p/em/text()')
                content_list.append(item)
                time.sleep(2)
                #保存到数据库
                cursor.execute("insert into ctrip(title,number,price,provider,comment,schedule,route1,route2) values(%s,%s,%s,%s,%s,%s,%s,%s)",[item["title"],item["number"][0],item["price"][0],item["provider"][0],item["comment"],item["schedule"][0],item["route_1"][0],item["route_2"][0]])
                con.commit()
            except:
                continue
    cursor.close()
    con.close()
    return


def main():
    item = {}
    all_url = []
    url_list = []
    content_list = []
    get_urllist(url_list)
    all_url = tourism_url(url_list, all_url)
    extract_data(all_url,item,content_list)

if __name__=="__main__":
    main()
print("OK")
