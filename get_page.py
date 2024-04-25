import requests
import csv 
import re


ACCESS_TOKEN = 'Bearer YNEOboMlOSofFS8fzZKOxbbGzoS3ZexBVUGA49tZuOlQAxmaMXf3lkI824AyCW1U'


def get_page_content(url):
    header = {'Authorization':ACCESS_TOKEN}
    response = requests.get(url,headers = header)
    if response.status_code == 200:
       
        page_content = response.json()
        matching(str(page_content))
    else:
        print('some_error')



def matching(page_content):
    pattern = r'"(https?:\/\/(www\.youtube\.com|wwww\.vimeo\.com)[^\s]+)"'
    links = re.findall(pattern , page_content)
    print(links)

def get_pages(filename : str):
    reader = csv.reader(open(filename , 'r'))
    for row in reader:
        course_name , sis_id , course_link , page_title , page_url = row
        url_split = page_url.split('/courses' , 1)
        if len(url_split) > 1:
            
            url = f'{url_split[0]}/api/v1/courses{url_split[1]}'
            get_page_content(url)

if __name__ == '__main__':
    doc = 'video_attachments.csv'
    get_pages(doc)