import textwrap
s=raw_input("Enter your String : ")
w=int(raw_input("Enter width : "))
#The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.
print textwrap.fill(s,w)
#The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
#It returns a list of output lines.


print textwrap.wrap(s,w)