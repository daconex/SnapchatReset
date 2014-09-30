
import os, sys

if not 'path' in locals():
    print "Error: Run config.py before running this script"
    sys.exit()

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
    # Removes snapchat log also
    remove_files(snapchat_doc)
    print "Finished!"

if __name__ == "__main__":
    main()