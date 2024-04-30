import os


# reads all the files in the /negative folder and generates neg.txt from them.
# we'll run it manually like this:
# $ python
# Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from cascadeutils import generate_negative_description_file
# >>> generate_negative_description_file()
# >>> exit()
def generate_negative_description_file(path):
    # open the output file for writing. will overwrite all existing data in there
    with open(path + 'negative.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir(path + 'negative'):
            f.write(path + 'negative/' + filename + '\n')



# generate positive samples from the annotations to get a vector file using:
# $ C:/Users/Ben/learncodebygaming/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec
# $ C:/Users/fkr476/OneDrive\ -\ University\ of\ Copenhagen/PhD/Code/PhotonicDrivers/Code/MachineVision/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec

# train the cascade classifier model using:
# $ C:/Users/Ben/learncodebygaming/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 24 -h 24
# $ C:/Users/fkr476/OneDrive\ -\ University\ of\ Copenhagen/PhD/Code/PhotonicDrivers/Code/MachineVision/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 67 -numNeg 55 -numStages 10 -w 24 -h 24

# my final classifier training arguments:
# $ C:/Users/Ben/learncodebygaming/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 200 -numNeg 1000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999

