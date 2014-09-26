path = '/var/mobile/Applications/3BF38C99-0DEC-4F91-96FC-CA841E385928'
import os

snapchat_tmp = path + '/tmp/'
snapchat_doc = path + '/Documents/'

def remove_files(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)

        except Exception, e:
            print e

def main():
    remove_files(snapchat_tmp)
    remove_files(snapchat_doc)
    print "Finished!"

if __name__ == "__main__":
    main()