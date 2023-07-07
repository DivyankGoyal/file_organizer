#File Sorter by DJ

import os, shutil

import argument_parser 
from datetime import datetime

class typeOrganizer:

    def __init__(self):
        self.images=[".jpeg",".png",".jpg",".gif"]                              #extensions for images
        self.text=[".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"]          #extensions for text files
        self.videos=[".mp4",".mkv"]                                             #extensions for videos
        self.sounds=[".mp3",".wav",".m4a"]                                      #extensions for sounds
        self.applications=[".exe",".lnk",".bat",".app",".dmg"]                  #extensions for applications
        self.codes = [".c",".py",".java",".cpp",".js",".html",".css",".php"]    #extensions for codes

    def getDestination(self, file, PATH):
        dest = ""
        for ex in self.images:
            if file.endswith(ex) or file.endswith(ex.upper()):
                dest = PATH + '/Image_Folder'
                return dest

        for ex in self.text:
            if file.endswith(ex) or file.endswith(ex.upper()):
                dest = PATH + '/Text_Folder'
                return dest

        for ex in self.sounds:
            if file.endswith(ex) or file.endswith(ex.upper()):
                dest = PATH + '/Sound_Folder'
                return dest

        for ex in self.videos:
            if file.endswith(ex) or file.endswith(ex.upper()):
                dest = PATH + '/Video_Folder'
                return dest

        for ex in self.applications:
            if file.endswith(ex) or file.endswith(ex.upper()):
                dest = PATH + '/Application_Folder'
                return dest

        for ex in self.codes:
            if file.endswith(ex) or file.endswith(ex.upper()):
                dest = PATH + '/Code_Folder'
                return dest
        dest = PATH + '/Other_Folder'
        return dest

    def updateName(self, file):
        file_wihtout_extension = os.path.splitext(file)[0]
        file_extension = os.path.splitext(file)[1]
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        new_file_path = file_wihtout_extension + '_' + str(current_datetime) + file_extension
        os.rename(file, new_file_path)
        return new_file_path
    
    def createDirectory(self, files, dest):
        if os.path.exists(dest):    
            if os.path.isdir(dest):                 # if dest is a directory
                pass
            else:                                   # if dest is a file then change the name of that file and then create that a directory
                newName = self.updateName(dest)
                files.append(newName)
                os.mkdir(dest)
        else:
            os.mkdir(dest)

    def main(self):
        args = argument_parser.argParser()
        PATH = args.path
        files = [os.path.join(PATH, file) for file in os.listdir(PATH)]
        for file in files:
            if not os.path.exists(file):   # file not exist as it may get renamed because of same name as of folder
                continue
            if os.path.isdir(file) and not file.endswith('.app') and not file.endswith('.APP'):   # if file is a directory skip that filr and .app is also a directory but we are taking it as a file
                continue
            dest = self.getDestination(file, PATH) # get final destination of the file
            self.createDirectory(files, dest) # create directory if not present
            file_name = os.path.basename(file)
            if os.path.exists(dest + '/' + file_name):
                file = self.updateName(file)
            shutil.move(file, dest)

        print("Sorting Completed...")

if __name__ == "__main__":
    organizer = typeOrganizer()
    organizer.main()
