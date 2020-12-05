def find_new_(path_pods,sub_folder,clean_titles,episodes):

    #[title,episode,links,entry_data]
    new_dl = []

    for each_episode in clean_titles:
        title = each_episode[0]
        if title not in episodes:
            new_dl.append(each_episode)
    return new_dl


if __name__ == '__main__':
    pass
