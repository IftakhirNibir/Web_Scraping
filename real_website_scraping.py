from bs4 import BeautifulSoup
import requests
import time
# requests is used for request the website to give their data
print("Put some skill that you are not familiar with")
unfamiliar_skill = input(">")
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        publish_date = job.find('span',class_='sim-posted').span.text
        if 'few' in publish_date:
            company_name = job.find('h3',class_="joblist-comp-name").text
            skills = job.find('span',class_="srp-skills").text.replace(' ','')
            publish_date = job.find('span',class_='sim-posted').span.text
            more_info = job.header.h2.a['href'] #for receive the value of that attribute 
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name:{company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'Publish Time: {publish_date.strip()} \n')
                    f.write(f'More Info: {more_info}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10 
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60) #10*60s = 10 minutes


