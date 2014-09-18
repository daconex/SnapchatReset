import os, sys

path = "/var/mobile/Applications/"

print "Searching files..."

for root, dirs, files in os.walk(path):
    #for name in files:
        #print(os.path.join(root, name))
    for name in dirs:
        #print(os.path.join(root, name))
        if name == "Snapchat.app":
            folder = root.replace(path, '')
            with open("snapchat.py", "r+") as snapchat:
                old = snapchat.read()
                snapchat.seek(0)
                snapchat.write("path = '" + root + "'\n" + old)

            print "Done!"
            sys.exit()