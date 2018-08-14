import copy

class Application(object):


    #holds the application name, server name, and an array of instances
    def __init__(self, applicationName = "Not Set", serverName = "Not Set", instances = None):
        self.applicationName = applicationName
        self.serverName = serverName
        if instances == None:
            instances = []
        self.instances = instances
        
        
    def printInfo(self):
        print("Application Name: " + self.applicationName)
        print("Server Name: " + self.serverName)
        for instance in self.instances:
            instance.printInfo()
        
        
        
class Instance(object): #holds the instance name, an array of urls, and the expected results from these urls

    def __init__(self, name = "Not Set", expected = "Not Set"):
        self.name = name
        self.expected = expected #urls mapped to an array of expected responses
        self.actual = copy.deepcopy(expected)
        self.urls = []
        
        for url in self.actual:
            initList = []
            self.urls.append(url)
            for value in self.actual[url]:
                initList.append("Unable to connect")
            self.actual[url] = initList
                
                    
            
    def printInfo(self):
        print(self.name)
        print(self.expected)
        print(self.actual)
        
        
class CodeResponse(object): #container to hold a code attribute of response, and the acutal reponse
    def __init__(self, code, response):
        self.code = code
        self.response = response