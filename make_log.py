import os

#make: pod folder, sub folder, and pod log
def make_log_(path_pod,sub_folder):

    #check to make sure the path to the pod exists
    if not os.path.isdir(path_pod):
        os.makedirs(path_pod)

    #if the folder doesn't exist
    folder = path_pod + sub_folder
    if not os.path.isdir(folder):
        #make folder
        os.makedirs(folder)

    pod_log = folder + '//pod_log.txt'
    #if there is no log in that folder
    if not os.path.isfile(pod_log):
        #make log
        with open(pod_log,'w'):
            pass
    return None

if __name__ == '__main__':
    path_pods = 'pods'
    folder_name = 'zz_test_delete_me'

    #creates an example folder and log
    make_pod_logs_(path_pods,folder_name)

    #logs a bogus episode in the test folder
    log_episode(path_pods,'zz_test_delete_me','test from make_pod_logs.py')
    pass
