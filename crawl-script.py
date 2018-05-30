'''
[] build function to open html file first and read a contant 
   -- in manner of link not a diroctary path !
[] build function to extract data links and hyper link in dictionay
   -- you need find() method 
   -- you need index() method
   -- you need dictionay
   -- 
[] build function to write a result in txt file
[] build a test function to test the result
   -- build comparison method with try and except using link-test.txt as 
      refrence  
good luck !!!
'''
import string
import urllib

links = []

def ex_link(y):
    result = []
    for i in y:
        if i != None and i.find("<h2>") != -1:
            result.append(i)
    for element in result:
        for i in range(len(result)):
           raw = result[result.index(element)].replace(" ","")
           first = raw.find("<ahref")
           end = raw.find(".html")
           links.append(raw[first+7:end+6])
           for i in links:
               i = 0
               try:
                   if links[i] == links[i+1]:
                       del links[i]
               except:
                   pass
    print links
    return links
def page(x):
    page = urllib.urlopen(x)
    result = []
    while True:
        page_line = page.readline()
        result.append(page_line)
        if not page_line : break
    return result
link_test =  page("file:///home/godzilla/crawler-project/test-1.html")

#extracted_link("file:///home/godzilla/crawler-project/test-1.html")
ex_link(link_test)

for i in links:
    print type(i)
print "============================under this is test table========="
def testing():
    links_list = []
    test_file = open("links-test.txt","r+")
    while True:
        test_line = test_file.readline()
        links_list.append(str(test_line))
        if not test_line: break
    test_file.close()
    for i in  links_list:
        print type(i)

    for link in links:
        if link in links_list:print link, "found !\n"
        else:print link, "not found !\n"
           
testing()
