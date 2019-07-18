#coding=gbk
'''
    尝试爬取boss直聘网
'''
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '+
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.'+
            '3626.109 Safari/537.36'}#设置请求头
url = "https://www.zhipin.com/c101280100/?page=1&ka=page-1"
resp = requests.get(url,headers=headers)
print(resp.text)
#抓取广州城市所有工作的职位、地址、区域、学历要求、工资范围、公司名称等。

'''
第一次尝试，被封了24小时
第二次尝试，间隔上次1min，加上请求头,获取到html，显示未登录。
'''

#尝试抓取一个例子。

soup = BeautifulSoup(resp.text, 'lxml')#解析html

#抓取职位
all_jobs = soup.find_all('div', class_='job-title')
jobs = [j.get_text() for j in all_jobs]

# ~ print(jobs)
#抓取薪资范围
all_salarys = soup.find_all('span', class_='red')
salarys = [s.get_text() for s in all_salarys]

#抓取地址、年限要求、学历
all_adds_times_educations = soup.find_all('div', class_='info-primary')
adds = []
times = []
educations = []
for alates in all_adds_times_educations:
    alate = alates.find('p')
    all_a_t_e2 = str(alate)
    all_a_t_e3 = all_a_t_e2.replace('<em class="vline"></em>',',').replace('<p>', '').replace('</p>','')
    all_a_t_e_list = all_a_t_e3.split(',')
    adds.append(all_a_t_e_list[0])
    times.append(all_a_t_e_list[1])
    educations.append(all_a_t_e_list[2])

#抓取公司名称
all_companys = soup.find_all('div',class_='company-text')
companys = [c.find('a').get_text() for c in all_companys]

#抓取公司标签、融资情况，人员规模
all_tags_financings_staffs = soup.find_all('div', class_='company-text')
tags = []
financings = []
staffs = []
for altfss in all_tags_financings_staffs:
    altfs = altfss.find('p')
    all_t_f_s2 = str(altfs)
    all_t_f_s3 = all_t_f_s2.replace('<em class="vline"></em>',',').replace('<p>', '').replace('</p>','')
    all_t_f_s_list = all_t_f_s3.split(',')
    tags.append(all_t_f_s_list[0])
    financings.append(all_t_f_s_list[1])
    staffs.append(all_t_f_s_list[-1])

filename = 'boss职位爬取.txt'
for job,salary,add,time,education,company,tag,financing,staff in zip(jobs,salarys,adds,times,educations,companys,tags,financings,staffs):
    job = '职位:' + job + '\n'
    salary = '薪资范围：' + salary + '\n'
    add = '公司地址' + add + '\n'
    time = '工作年限要求：' + time + '\n'
    education = '学历要求：' + education + '\n'
    company = '公司名称：' + company + '\n'
    tag = '公司标签：' + tag + '\n'
    financing = '融资情况：' + financing + '\n'
    staff = '人员规模：' + staff + '\n'
    data = job + salary + add + time + education + company + tag + financing + staff
    with open(filename, 'a', encoding='UTF-8') as f_oj:
        f_oj.write(data + '*********************************' + '\n')
        
