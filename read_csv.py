import csv
import os.path
import feedparser
import requests
from bs4 import BeautifulSoup
import re
from z_my_print import my_print

def read_file(file_name):
    content = []
    with open(file_name+'.csv' , newline='') as csvfile:
        f = csv.reader(csvfile, delimiter=',')
        for ea in f:
            content.append(ea)
    return content

##def clean_str(input_str):
##    allowed = str.digits + str.letters + './/
##    clean_str = ''
##    invalid_chars = []
##    for char in str(input_str):
##        if char in allowed:
##            clean_str = clean_str + char
##        elif char == ',':
##            clean_str = clean_str + ';'
##        else:
##            invalid_chars.append(char)
##    print('Invalid characters not added: {}'.format(invalid_chars))
##    return clean_str


def new_index(subscribed):
    #for each subscribed podcast
    for each in subscribed:
        #if the folder does not exist
        if not os.path.isdir(each[1]):
            #make it
            os.makedirs(each[1])
        #if the index does not exist
        if not os.path.isfile(each[1] + '//index.csv'):
            #create it
            with open(each[1] + '//index.csv','w') as csvfile:
                f_write = csv.writer(csvfile, delimiter=',')
                pass
    return None

#add new line in downloaded files
def add_download(folder,file_downloaded):
    with open(folder+'\\index.csv','a', newline='') as csvfile:
        f_write = csv.writer(csvfile, delimiter=',')
        f_write.writerow([file_downloaded])
    return file_downloaded

#input list of downloads for each subscribed
def index_contents(subscribed_list):
    folder_index = []
    for each in subscribed_list:
        r = read_file(str(each[1])+'\\index')
        #formatted as folder, previous downloads
        folder_index.append([each,r[1:]])
    #return the downloaded contents of each file
    return folder_index

#figure out what items are subscribed to
def sub_status(list_all):
    sub = []
    unsub = []
    for each in list_all:
        if len(each) > 0:
            if each[0] == '1':
                sub.append(each)
            elif each[0] == '0':
                unsub.append(each)
    return sub,unsub

#get download name
def name_grabber(input_string):
    i = len(input_string)-1
    name = ''
    while i > 0:
        temp_1 = input_string[i]
        if temp_1 == '/':
            i = 0
        else:
            name = temp_1 + name
        i = i - 1
    j = 0
    file_name = ''
    while j < len(name):
        temp_2 = name[j]
        if temp_2 == '.' or temp_2 =='?' or temp_2 == '&' or temp_2 == '=':
            i = len(name)
        else:
            file_name = file_name + temp_2
        j = j + 1
    if len(file_name) > 50:
        file_name = file_name[:50]
    return file_name


#get feed
def get_feed(urls):
    all_links = []
    for url in urls:
        each_podcast = []
        d = feedparser.parse(url[2])
        entries = d.entries
        for each_entry in entries:
            for each_link in each_entry.links:
                each_podcast.append(each_link.href)
                
##            each_podcast.append(ea.link)
            
##    for each_entry in e:
##        for each_link in each_entry.links:
##            #second link has the secure download
##            true_url = each_link.href
##            #append that link
##            urls.append(true_url)


        all_links.append([url,each_podcast])
    return all_links

#prepare next downloads
def prepare_next(all_links):
    next_dls = []
    for ea_1 in all_links:
        folder_name = ea_1[0][1]
        contents = read_file(folder_name + '\index')
        temp = []
        for ea in ea_1[1]:
            is_new = True
            for e in contents:
                if ea in e:
                    is_new = False
                    pass
            if is_new:
                temp.append(ea)
        next_dls.append([folder_name,temp])
    return next_dls

def get_them(next_dls):
    for ea in next_dls:
        folder = ea[0]
        urls = ea[1]
        if len(urls)>0:
            print('Folder: {}\nReceiving: {} files.\n\n'.format(folder,len(urls)))
        else:
            print('No new files for folder:\n  {}\n\n'.format(folder))
        for url in urls:
            r = requests.get(url)
            with requests.Session() as req:
                print('Attempting to download: {}'.format(url))
                download = req.get(url)
                if download.status_code == 200:
                    #if the download is > 0.25 MB
                    if len(download.content) > (0.25*1024*1024):
##                        print('Passed min file size')
                        name = name_grabber(url)+'.mp3'
                        with open(folder + '\\' + name,'wb') as f:
##                            print('Writting file: {}'.format(name))
                            f.write(download.content)
                            print('Done writing file')
                    else:
##                        print('Did not meet minimum file size')
                        pass
                    #if it was successfully downloaded
                    #but doesn't meet the min file size
                    #log it, so it doesn't try to dl again
                    add_download(folder,url)
##                    print('Added url to folder: {}'.format(folder))
                else:
##                    print('Download Failed for file: {}'.format(url))
                    pass
            print('')
    return None


def print_subscribed_list(subscribed_list):
    subscribed = []
    if len(subscribed_list) > 0:
        for ea in subscribed_list:
            subscribed.append(ea[1])
    print('Subscribed to:')
    if len(subscribed) > 0:
        for ea in subscribed:
            print(ea)
    else:
        print(None)
    return None


if __name__ == '__main__':
    temp = read_file('subscribed')
    s,u = sub_status(temp[1:])

    #ensure folder and index exist based on subscribed list
    new_index(s)

    #pair folders/downloads
    i = index_contents(s)

    #get list of available downloads based on subscribed list
    g = get_feed(s)

    #next [folder,items to download] pair to be downloaded
    n = prepare_next(g)

    get_them(n)



    pass
