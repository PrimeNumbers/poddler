from read import read_sub
from make_log import make_log_ as make_log
from read import read_episodes
from valid import clean_titles
from feed import feed_ as feed
from find_new import find_new_ as find_new
from get_new_dls import get_new_dls_ as get_new_dls

from z_my_print import my_print

if __name__ == '__main__':
    #name of the folder that holds all the subscription folders
    path_pods = 'pods//'

    #gather info from subscribed csv file
    sub , ref , ignore = read_sub('subscribed') #read subscribed.txt
    # sub contains [[sub_status,folder_name,feed_url],[sub_status_2,folder_name_2,feed_url_2],[etc,etc,etc]]

    #as long as there is a subscription
    assert(len(sub) != 0)

    for each_sub in sub:
        sub_folder = each_sub[1]
        feed_url = each_sub[2]
        make_log(path_pods,sub_folder)
        episodes = read_episodes(path_pods,sub_folder)
##        print('episodes: {}'.format(len(episodes)))

        title_episode_links = feed(feed_url)
##        print('first episode title: {}'.format(title_episode_links[0][0]))

        clean_title = clean_titles(title_episode_links)
        new_titles = find_new(path_pods,sub_folder,clean_title,episodes)
        print('For: {}\n New: {}'.format(sub_folder,len(new_titles)))

        download_backlog = True

        if len(new_titles) > 1:
            get = input('Download {} episodes? (y or n): '.format(len(new_titles)))
            if get.lower() == 'y':
                download_backlog = True
            else:
                download_backlog = False

        if download_backlog:
            success , failure = get_new_dls(path_pods,sub_folder,new_titles)
            if len(success) > 0 or len(failure) > 0:
                print(' Success: {}\n Failure: {}'.format(len(success),len(failure)))
            print('')
        else:
            for each_episode in new_titles:
                with open(path_pods + sub_folder + '//pod_log.txt','a') as f:
                    f.write(each_episode[0] + '\n')
