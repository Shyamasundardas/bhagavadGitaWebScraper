import requests
from bs4 import BeautifulSoup

def link_grabber():
    html_text = requests.get('https://asitis.com/').text 

    soup = BeautifulSoup(html_text, 'lxml')
    concentrated_soup = soup.find('ul', class_='list-group')
    #separates two subsections of links^
    main_links = concentrated_soup.find_all('a', href=True)
    #print(main_links)
    link_list = [] 
    for link in main_links:
        if link.text == 'INDEX':
             link_list += [link['href']]
    #remove junk links \/
   # while True:
  #      link_suffix = link_list[0].split('/', -1)
   #     link_suffix = link_suffix[-1]
     #   while link_suffix != '1':
     #       del link_list[0]
     #   if link_suffix == '1':
     #       continue
    del link_list[0]
    del link_list[0]
    del link_list[0]
    return link_list


def chapterParser(link_list, chapterNumber):
    link = link_list[chapterNumber]
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    #make a list of verse annotations
    verse_annotation_condensed_soup = soup.find('div', class_='col-sm-6 col-md-7')
    verse_annotation_list_rough = verse_annotation_condensed_soup.find_all('h4')
   
    verse_annotation_list =[]
    i=0 #iterator for the verse extraction

    for annotations in verse_annotation_list_rough: 
        verse_annotation_list += annotations.a
        i += 1 
        
    #make a list of verses 
    verse_list_condensed_soup = soup.find('div', class_='col-sm-6 col-md-7')
    verse_list_rough = verse_list_condensed_soup.find_all('p')
    verse_list =[]

    for g in range(i):
        verse_list += verse_list_rough[g]

    f=0
    with open ("txt.txt", 'a') as out_file:
        for f in range(i):
            out_file.write(verse_annotation_list[f])
            out_file.write(': ')
            out_file.write(verse_list[f])
            out_file.write(';\n')
            f +=1
        

    
        








def main():
    i=0
    for i in range(17):
        chapterParser(link_grabber(), i)

        
main()