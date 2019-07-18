#coding=gbk
'''
    ������ȡbossֱƸ��
'''
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '+
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.'+
            '3626.109 Safari/537.36'}#��������ͷ
url = "https://www.zhipin.com/c101280100/?page=1&ka=page-1"
resp = requests.get(url,headers=headers)
print(resp.text)
#ץȡ���ݳ������й�����ְλ����ַ������ѧ��Ҫ�󡢹��ʷ�Χ����˾���Ƶȡ�

'''
��һ�γ��ԣ�������24Сʱ
�ڶ��γ��ԣ�����ϴ�1min����������ͷ,��ȡ��html����ʾδ��¼��
'''

#����ץȡһ�����ӡ�

soup = BeautifulSoup(resp.text, 'lxml')#����html

#ץȡְλ
all_jobs = soup.find_all('div', class_='job-title')
jobs = [j.get_text() for j in all_jobs]

# ~ print(jobs)
#ץȡн�ʷ�Χ
all_salarys = soup.find_all('span', class_='red')
salarys = [s.get_text() for s in all_salarys]

#ץȡ��ַ������Ҫ��ѧ��
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

#ץȡ��˾����
all_companys = soup.find_all('div',class_='company-text')
companys = [c.find('a').get_text() for c in all_companys]

#ץȡ��˾��ǩ�������������Ա��ģ
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

filename = 'bossְλ��ȡ.txt'
for job,salary,add,time,education,company,tag,financing,staff in zip(jobs,salarys,adds,times,educations,companys,tags,financings,staffs):
    job = 'ְλ:' + job + '\n'
    salary = 'н�ʷ�Χ��' + salary + '\n'
    add = '��˾��ַ' + add + '\n'
    time = '��������Ҫ��' + time + '\n'
    education = 'ѧ��Ҫ��' + education + '\n'
    company = '��˾���ƣ�' + company + '\n'
    tag = '��˾��ǩ��' + tag + '\n'
    financing = '���������' + financing + '\n'
    staff = '��Ա��ģ��' + staff + '\n'
    data = job + salary + add + time + education + company + tag + financing + staff
    with open(filename, 'a', encoding='UTF-8') as f_oj:
        f_oj.write(data + '*********************************' + '\n')
        
