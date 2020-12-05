import feedparser
import requests
from bs4 import BeautifulSoup
import re

def get_dl(url):
    r = requests.get(url)
    with requests.Session() as req:
        download = req.get(url)
        if download.status_code == 200:
            return download
    return 0

def get_new_dls_(path_pods,sub_folder,new_titles):
    success = []
    failure = []

    #iterate through each episode
    for ea in new_titles:
        title = ea[0]
        episode = ea[1]
        links = ea[2]

        dl = ''
        #as long as there is more than 1 link
        if type(links) == type(list()):
            #out of all the candidate links that are associated with the download
            candidates_dl = []
            for link in links:
##                print('link: {}'.format(link))
                candidates_dl.append(get_dl(link))
##            print('candidates_dl: {}'.format(candidates_dl))

            #get the lengths for each (as long as '0' was not returned for the download
            lengths_dl = []
            for each_dl in candidates_dl:
                if each_dl != 0:
                    lengths_dl.append(len(each_dl.content))
##            print('lengths_dl: {}'.format(lengths_dl))

            #find the largest file
            length = max(lengths_dl)
##            print('length: {}'.format(length))

            #and its corresponding index
            dl_index = lengths_dl.index(length)
##            print('dl_index: {}'.format(dl_index))
            #the file to download corresponds to this index
            dl = candidates_dl[dl_index]
        else:
            dl = get_dl(links)

        #save the file
        save_file = False
        file_name = path_pods + sub_folder + '//' + title + '.mp3'
        with open(file_name,'wb') as f:
            f.write(dl.content)
            save_file = True
            with open(path_pods + sub_folder + '//pod_log.txt','a') as f:
                f.write(title + '\n')
            

        #if the file failed to be downloaded
        if save_file:
            success.append(ea)
            print('Successful download: {}'.format(len(success)))
        else:
            failure.append(ea)
            print('Failure download: {}'.format(len(failure)))

    return success,failure


if __name__ == '__main__':
    pass
