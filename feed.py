import feedparser

def feed_(url):
    feed = feedparser.parse(url)
    entries = feed.entries

    #debug purposes
##    keys = []
##    for each_entry in entries:
##        for each_key in each_entry.keys():
##            if each_key not in keys:
##                keys.append(each_key)
##    print('keys: \n{}'.format(each))

    episode_data = []
    for each_entry in entries:
        title = []
        try:
            title = each_entry.title
        except:
            pass
        if len(title) == 0:
            try:
                title = each_entry.itunes_title
            except:
                pass

        #episode_number
        episode_number = []
        try:
            episode_number = each_entry.itunes_episode
        except:
            pass

        #links
        links = []
        try:
            links.append(each_entry.link)
##            print('Links_1: {}'.format(links))
        except:
            pass

        #try to grab any alternative links
        try:
            #if the links are stored in an array
            if type(each_entry.links) == type(list()):
                for each_link in each_entry.links:
                    try:
                        #try to grab the hyperlinks from each
                        links.append(each_link.href)
##                        print('Links_1: {}'.format(links))
                    except:
                        pass
                #if the links are buried 2 deep
                for each_1 in each_entry.links:
                    for each_2 in each_1:
                        try:
                            #try to grab the hyperlinks from each
                            links.append(each_2.href)
##                            print('Links_1: {}'.format(links))
                        except:
                            pass
                #if the links are buried 3 deep... what are they doing with this format?
                for each_1 in each_entry.links:
                    for each_2 in each_1:
                        for each_3 in each_2:
                            try:
                                #try to grab the hyperlinks from each
                                links.append(each_3.href)
##                                print('Links_1: {}'.format(links))
                            except:
                                pass
            else:
                #otherwise try to add a single link
                temp_1 = each_entry.links
                links.append(temp_1.href)
##                print('Links_1: {}'.format(links))
        except:
            pass
        episode_data.append([title , episode_number , links , each_entry])
    return episode_data

##def missing_data(feed):
##    titles = []
##    episodes = []
##    links = []
##
##    for each_episode in feed:
##        if len(each_episode[0]) == 0:
##            titles.append(each_episode)
##        if len(each_episode[1]) == 0:
##            episodes.append(each_episode)
##        if len(each_episode[2]) == 0:
##            links.append(each_episode)
##
##    print('---Missing---')
##    print('  Titles:   {}'.format(len(titles)))
##    print('  Episodes: {}'.format(len(episodes)))
##    print('  Links:    {}'.format(len(links)))
##
##    return titles,episodes,links

if __name__ == '__main__':
    pass
