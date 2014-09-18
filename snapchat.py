import os

snapchat_tmp = '/var/mobile/Applications/8DBC5F17-336E-42B0-8E2A-EA184BD1C34C/tmp/'
snapchat_doc = '/var/mobile/Applications/8DBC5F17-336E-42B0-8E2A-EA184BD1C34C/Documents/'

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

if __name__ == "__main__":
    main()