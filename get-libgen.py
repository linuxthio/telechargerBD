"""
auteur: djibril thiongane
email : djibthiongane@gmail.com
date: 14/03/2021

"""

import requests
from bs4 import BeautifulSoup as bs
import wget
from os import listdir
import sys
	
def get_cbr(url):
	pt=print
	rs=requests.get(url)
	soup=bs(rs.text,'html.parser')
	links=[]
	# __x=[]
	# __y=[]
	__tmp=[]
	for e in soup.find_all('td'):
		c=e.find('font')
		if c!=None:
			a=c.find('a')
			if a!=None:
				if a['href']!='../':
					__tmp.append(a.text+":"+a['href'])
					# __x.append(a.text)
					# __y.append(a['href'])
		# print("{} :: {}".format(a.text,a['href']))
	# netoyage 
	__tmp=list(set(__tmp))

	for c in range(len(__tmp)):
		
		__x=__tmp[c].split(":")[0]
		__y=__tmp[c].split(":")[1]
		links.append([__x,__y])
		pt(str(c)+"  "+__x+" : "+__y)
	return links

def create_url_output_dir():
	if sys.argv[2]==None:
		url=''
	else:
		url=sys.argv[2]
	#......................
	if sys.argv[1]==None:
		outputfiles='.'
	else:
		import os
		outputfiles=sys.argv[1]
		try:
			os.mkdir(outputfiles)
		except:
			pass
	return [url,outputfiles]

def launch_(url,outputfiles):
	pt=print
	if url!="":
		pt("Download is beginning now ......... GOOD LUCK BABY !!!")
		i=0
		for u in recup:
			pathss="http://libgen.lc/comics/"
			with open(outputfiles+"/bdd_files_downloads.txt","a") as g:
				try:
					test=g.readlines()
				except:
					test=[]
				pt(test)
			
			if  (u[1] not in test) ==True:
				pt(" - downloading of N {} size : {} format : {}".format(i,u[0].split('/')[1],u[0].split('/')[0]))
				fname=wget.download(pathss+u[1],outputfiles)
				i=i+1
				with open(outputfiles+"/files_downloads.txt","a") as f:
					f.write("{}\n".format(fname))

				with open(outputfiles+"/bdd_files_downloads.txt","a") as ff:
					ff.write("{}\n".format(u[1]))
			else:
				pt("!!!!!!!!! ce fichier est deja telecharger\n")
	else:
		pt("veuillez renseigne l'url ")
	pt("\n---------- END --------------\n")

def main():
	url,outputfiles=create_url_output_dir()
	recup=get_cbr(url)
	launch_(url,outputfiles)


if __name__=='__main__':
	main()

	
