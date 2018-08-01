'''
Created on Jul 20, 2018

@author: y948467
'''
import requests
import webbrowser
from multiprocessing.dummy import Pool as ThreadPool 
from Application import Application
from Application import Instance
from Application import CodeResponse

#----------------------------------------------------------------------------------------------------------------------------------
CONFIGURATION_FILE = "info2.txt"
#----------------------------------------------------------------------------------------------------------------------------------
applications = []


def dataToHTML():
    #https://stackoverflow.com/questions/33920896/table-within-an-html-document-using-python-list
    f = open('helloworld.html','w')

    head = """<HTML>
    <head>
    <style>
        table {
    }
        table {
        border-collapse: collapse;
    }
        table {
        width: 100%;
    }
        th {
        height: 5px;
    }
        th, td {
        padding: 15px;
        text-align: left;
    }
        #content img {
            position: absolute;
            top: 0px;
            right: 0px;
            width: 15%;
            height: auto;
            
    }
    </style>
    </head>"""
    html = """
    <body>
        <div id="content">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Macys_logo.svg/1280px-Macys_logo.svg.png" class="ribbon"/>
        </div>
        <h1>Responses</h1>
        <table>
            <tr>
                <th>Application Name</th>
                <th>Server</th>
                <th>Instance</th>
                <th>URL</th>
                <th>Attribute</th>
                <th>Expected</th>
                <th>Actual</th>
                <th>Attribute</th>
                <th>Expected</th>
                <th>Actual</th>
                <th>Result</th>
            </tr>
            {0}
        </table>
    </body>
    </HTML>"""
    items = []
    for application in applications:
        instances = application.instances
        for instance in instances:
            expected = instance.expected
            actual = instance.actual
            urls = instance.urls
            for url in urls:
                result = "Pass"
                attributes = ["N/A", "N/A"]
                expectedResponses = ["N/A", "N/A"]
                actualResponses = ["N/A", "N/A"]
                
                for i in range(len(expected[url])):
                    expectedResponses[i] = str(expected[url][i].response)
                    actualResponses[i] = str(actual[url][i].response)
                    attributes[i] = str(expected[url][i].code)
                    if expectedResponses[i] != actualResponses[i]:
                        result = "Fail"
                row = []
                row.append(application.applicationName)
                row.append(application.serverName)
                row.append(instance.name)
                row.append(url)
                row.append(attributes[0])
                row.append(expectedResponses[0])
                row.append(actualResponses[0])
                row.append(attributes[1])
                row.append(expectedResponses[1])
                row.append(actualResponses[1])
                row.append(result)
                items.append(row)
    
    formatted = []
    for item in items:
        row = ["<tr>"]
        for a in item:
            if a == "Fail":
                row.append("<td bgcolor=\"#FF0000\">" + str(a) + "</td>")
            elif a == "Pass":
                row.append("<td bgcolor=\"#00FF00\">" + str(a) + "</td>")
            else:
                row.append("<td>" + str(a) + "</td>")
        row.append("</tr>")
        row = "".join(row)
        formatted.append(row)
    
    f.write(head)
    f.write(html.format("".join(formatted))) #replace with sub items
    f.close()

    webbrowser.open_new_tab('helloworld.html')

def processLine(line, x = 1, y = 1):
    info = line.split("-", x)[y]
    info = info.split()
    info = " ".join(info)
    return info

def requestApplication(application):
    print("processing")
    instances = application.instances
    for instance in instances:
        expected = instance.expected
        actual = instance.actual
        urls = instance.urls
        for url in urls:
            responses = []
            for i in range(len(expected[url])):
                code = expected[url][i].code
                try:
                    resp = requests.get(url)
                    currCodeResponse = CodeResponse(code, str(getattr(resp, code)))
                    responses.append(currCodeResponse)
                except requests.exceptions.RequestException as e:
                    currCodeResponse = CodeResponse(code, "Unable to Connect")
                    responses.append(currCodeResponse)
                    print(e)
            actual[url] = responses

with open(CONFIGURATION_FILE , 'r') as f:
    for line in f:
        while line.startswith("APPLICATIONNAME-"):
            currApplication = Application()
            applicationName = processLine(line)
            currApplication.applicationName = applicationName
            line = f.readline();
            while(line.startswith(applicationName + ".SERVERNAME")):
                serverName = processLine(line)
                currApplication.serverName = serverName
                line = f.readline()
                instances = []
                while(line.startswith(applicationName + ".INSTANCE")):
                    instanceName = processLine(line)
                    line = f.readline()
                    urls ={}
                    while(line.startswith(applicationName + ".URL")):
                        urlName = processLine(line)
                        line = f.readline()
                        responses = []
                        while(line.startswith(applicationName + ".RESPONSE")):
                            response = processLine(line, 2, 2)
                            currCodeResponse = CodeResponse(processLine(line,2,1), response) 
                            line = f.readline()
                            responses.append(currCodeResponse)
                        urls[urlName] = responses
                    currInstance = Instance(instanceName, urls)
                    instances.append(currInstance)
                currApplication.instances = instances
                applications.append(currApplication)
                        

pool = ThreadPool(4) 
pool.map(requestApplication, applications)
pool.close()
pool.join()

dataToHTML()