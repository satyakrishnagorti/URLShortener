"""
** program to convert a long url to a tiny one **
** working: for each long url stored in the database(here in a hash) get its 'id', named as count here **
** convert count in BASE 10 to the BASE of alphabet size here 63 **
** for each reaminder when divided by 63 add it to a list and then map contents of the list to the charachters at those indices of the alphabet**
** for getting back the long url, get the short url, convert back the code generated into base 10, and query database for that id **
"""


import sys
import random
import string
from constants import LETTERS,BASE,DOMAIN

count = 0
myhash = {}

#converts a given count to a code consisting of letters in LETTERS variable
def convert_url(count):
  r_list = []
  while count>0:
    remainder = count%BASE
    r_list.append(remainder)
    count/=BASE

  short_url = ""
  for i in range(len(r_list)):
    short_url+=LETTERS[r_list[i]]
  print r_list
  print short_url
  return short_url

#converts the code to count.
def convert_code(code):
  count = 0
  for i in range(len(code)):
    count = count*BASE+LETTERS.find(code[::-1][i])
  return count

if __name__ == '__main__':

  #generating random strings as urls to test.
  for i in range(100):
    url = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    print url
    count = i
    myhash[count]=url
    count+=1
    short_url = convert_url(count)
    print "Short URL:"+ DOMAIN + short_url

  short_url=str(raw_input("Short URL:"))
  code = short_url.rstrip().split('/')[-1]
  count = convert_code(code)

  print "calculated count:",count
  print "Long URL:"+myhash[count]