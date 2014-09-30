import os, sys

path = "/var/mobile/Applications/"

print "Searching..."

for root, dirs, files in os.walk(path):
    for name in dirs:
        #print(os.path.join(root, name))
        if name == "Snapchat.app":
            #folder = root.replace(path, '')
            with open("snapchat.py", "r+") as snapchat:
                old = snapchat.read()
                snapchat.seek(0)
                snapchat.write("path = '" + root + "'\n" + old)

            print "Done!"
            sys.exit()

print "Directory 'Snapchat.app' not found. Install Snapchat from the App Store"