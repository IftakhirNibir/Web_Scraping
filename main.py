from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    courses_cards = soup.find_all('div',class_='card')
    for i in courses_cards:
        courses_name = i.h5.text
        courses_price = i.a.text.split(' ')[-1]
        print(f"Course Name: {courses_name} and price is {courses_price}")


