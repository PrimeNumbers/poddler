def validate_filename(file_name_to_check):
    new_name = ''

    assert(type(file_name_to_check)==type(str()))
    try:
        assert(len(new_name) < 75)
    except:
        #trim 75+ character titles for a file name
        new_name = new_name[0:75]

    valid_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'+'0123456789' + '- _'

    for each_letter in file_name_to_check:
        if each_letter in valid_char:
            new_name = new_name + each_letter

    return new_name



#function takes in a feed and validates the title for use as the file name
def clean_titles(title_episode_links):
    clean_title = []
    for each_episode in title_episode_links:
##        print('each_episode: {}'.format(each_episode[0:2]))
        clean = validate_filename(each_episode[0])
        clean_title.append([clean,each_episode[1],each_episode[2],each_episode[3]])
    return clean_title

if __name__ == '__main__':
    pass
##    valid = validate_filename('asdf1234_<>:"//\|?*_asdf1234')
