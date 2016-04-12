#Example Web Scrapping using BeautifulSoap
#Its a popular library used for Web Scrapping 
#Author : Arun Jayan


from bs4 import BeautifulSoup

soup = BeautifulSoup(open("sample.html"))

#print soup #print the html source 
print soup.html
#to aligned printing of source 
#sometimes the html code may not be aligned 
print "============================================================="
print soup.prettify()
print "============================================================="
print soup.html.body #prints the body
print "============================================================="
print soup.html.title #we wil get title 
print "============================================================="
print soup.body.p.next.next.string 
print "============================================================="
print soup.get_text("|",strip=True) #we will get all text in the webpage 
print "============================================================="
print soup.body.p.next.string.strip() #we will get first sentence 
print soup.body.p.next.next.string.strip()  # we willget socond
print "============================================================="
print soup.body.p.nextSibling.nextSibling.next.next.string.strip() #by using nextSibling we will get the next paragraph
print soup.body.p.nextSibling.nextSibling.next.next.next.next.string.strip() #
print "============================================================="
#To find all the tags with a name 
print soup.find_all("p") #it will give a list
print"##############################################################"
print soup.find_all("p")[0]
print "============================================================="
