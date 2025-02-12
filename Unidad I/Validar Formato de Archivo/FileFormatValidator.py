import re
import glob

class FileFormatValidator:
    def __init__ (self):
        # no incluye extension del archivo
        self.fileNamePattern = r"\w[\s\w\d_\-íó]*\." 
        self.pathPattern = r"[A-Z]:\\[\w\d_]+" 

    def showMatchingFiles(self, path, extension):
        if (re.match(self.pathPattern,path)):
            path = re.sub(r"\\+", "/",path)
            files = glob.glob(f"{path}/*.{extension}")
            print(path)
            for f in files:
                match = re.search(fr"{self.fileNamePattern}{extension}$",f)
                if match:
                    print(match.group())


