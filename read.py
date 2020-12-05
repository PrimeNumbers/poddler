import csv

def read_sub(file_name):
    sub = []
    ref = []
    ignore = []
    with open(file_name+'.csv' , newline='') as csvfile:
        f = csv.reader(csvfile, delimiter=',')
        for each_row in f:
            #ignore rows that are not correctly formatted
            if len(each_row) == 3:
                #ignore rows that begin as a comment
                if each_row[0][0] == '1':
                    #add it to the subscribed list
                    sub.append(each_row)
                elif each_row[0][0] == '0':
                    #add it to the reference list
                    ref.append(each_row)
                else:
                    #likely a comment row
                    #could be an improperly formatted row though
                    ignore.append(each_row)
            else:
                #likely a blank row or commented row
                #could be improperly formatted though
                ignore.append(each_row)
    return sub,ref,ignore

#grabs all episodes from a specific folder
def read_episodes(path_pods,folder):
    episodes = []
    log_path = path_pods + folder + '//pod_log.txt'
    with open(log_path ,'r', newline='') as f:
        for each_row in f:
            episodes.append(each_row.rstrip('\r\n'))
    return episodes

def show_list(input_list,values):
    print(input_list + ' contains: ')
    if len(values) == 0:
        print(None)
    else:
        for each_value in values:
            print(each_value)
    print()
    return None

if __name__ == '__main__':
    pass
##    sub , ref , ignore = read_sub('subscribed')
##    show('sub',sub)
##    show('ref',ref)
##    show('ignore',ignore)
##
##    all_pods_folder_location = 'pods'
##    test_folder = 'zz_test_delete_me'
##    episodes = read_episodes(all_pods_folder_location,test_folder)
##    show_list(test_folder,episodes)
