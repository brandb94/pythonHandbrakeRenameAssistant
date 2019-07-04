#-------------------------------------------------------
# Script to rename files generated from ripping a tv series via handbrake
# original delimiter format based on tv series dvd rip
#-------------------------------------------------------

import os

os.chdir('H:/tv show rips/The Simpsons Season 1')

diskDelimiters = []
seasonDelimiters = []

#Populate delimiter list. Typical dvd rip format
# for tv series is D1-1, D1-2, D2-1, D2-2, etc.
# so instead of implementing some smart logic I just hardcode the most common ones
for i in range(1,6):
    seasonDelimiters.append("S%s" % (str(i)))
    diskDelimiters.append("D%s-" % (str(i)))

# print(seasonDelimiters)
# print(diskDelimiters)
currentDirFiles = os.listdir()
episodeNumber = 1
renamedFileNameList = []

resultMap = {}

currentSeason = input("Please input season # ")
for f in currentDirFiles:
    #skip over directories
    if (os.path.isdir(f)):
        continue

    file_name, file_ext = os.path.splitext(f)

    finalFileName = ""
    finalDelim = ""
    for delim in diskDelimiters:
        splitFilename = file_name.split(delim)
        if (len(splitFilename) > 1):
            #print(splitFilename)
            finalDelim = delim
            #episodeNumber = splitFilename[1];

            finalFileName = splitFilename[0].strip() + " S" + currentSeason + "E" + str(episodeNumber) + file_ext
            #renamedFileNameList.append(finalFileName)
            resultMap[f] = finalFileName

    episodeNumber += 1

for fileName in resultMap.keys():
    print ("Renaming %s ----> %s" % (fileName, resultMap.get(fileName)))

userConsent = input("Your list of files will look like this. Is this okay? [y for yes] ")
if (userConsent.lower() == "y" or userConsent.lower() == "yes"):       
        for fileName in resultMap.keys():
            os.rename(fileName, resultMap.get(fileName))
            #print("hello")
