import re

mess = '''22
+-------------+ One hundred and fifty quadrillion,
|             | seventy-two trillion, six hundred
| 150 072 626 | and twenty-six billion, eight hun-
| 840 312 999 | dred and fourty million, three
|             | hundred and thirteen thousand sub-
+-------------+ tract one is a rather large prime
                number which equals one to five if
calculated modulo two to six respectively.

However, one other rather more in- +-------------+
teresting number is two hundred    |             |
and twenty-one quadrillion, eight  | 221 806 434 |
hundred and six trillion, four     | 537 978 679 |
hundred and thirty-four billion,   |             |
five hundred and thirty-seven mil- +-------------+
million, nine hundred and seven-
                                ty-eight thousand,
+-----------------------------+ six hundred and
|                             | seventy nine,
| Subscribe for more Useless  | which isn't prime
|      Number Facts(tm)!      | but is the 83rd
+-----------------------------+ Lucas number.'''
def decolumnising(text):
	text =re.sub('\+\-+\+', '',text) # get rid of top box row
	text = re.sub('\|[^\n]+\|','', text) # get rid of double bar
	text = re.sub('-\n? ','', text) # remove hyphens from line-breaks
	text = re.sub('\n',' ',text)
	text = re.sub(' +', ' ', text) # remove extra spaces
	print(text)
	

print(decolumnising(mess))