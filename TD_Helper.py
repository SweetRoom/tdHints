class TD_App:
    def __init__(self):
        self.architecture=""
        self.binFolder=""
        self.build=""
        self.compileDate=(2018,4,15)
        self.configFolder=""
        self.installFolder=""
        self.osName="touchDesigner"
        self.osVersion="1"
        self.product="TouchDesigner"
        self.recentFiles=["file1","file2"]
        self.preferencesFolder=""
        self.userPaletteFolder=""
        self.version=1
        self.power=True

    def addNonCommercialLimit(self,password=""):
        pass

    def removeNonCommercialLimit(self,password=""):
        return False

    def addResolutionLimit(self,x=0,y=0,password=""):
        pass

    def removeResolutionLimit(self,password=""):
        return False

class TD_AbsTime:
    def __init__(self):
        self.frame=0
        self.seconds=0
        self.step=0
        self.stepSeconds=0

class TD_OP:
    def __init__(self):
        self.valid=False
        self.id=0
        self.name=""
        self.path=""
        self.digits=1.0
        self.base=""
        self.passive=True
        self.time=TD_timeCOMP()

class TD_timeCOMP:
    def __init__(self):
        pass

absTime=TD_AbsTime()
app=TD_App()
