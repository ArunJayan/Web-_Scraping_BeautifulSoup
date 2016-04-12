#Example Web Scrapping using BeautifulSoap
#Its a popular library used for Web Scrapping 

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
print soup.html.title
print "============================================================="
print soup.body.p.next.next.string
print "============================================================="
print soup.get_text("|",strip=True)
print "============================================================="
print soup.body.p.next.string.strip()
print soup.body.p.next.next.string.strip()
print "============================================================="

