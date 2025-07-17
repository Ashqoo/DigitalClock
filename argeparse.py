import argparse

import requests

def DownloadFile(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
           for chunk in r.iter_content(chunk_size=8192): 
              #if chunk: # filter out keep-alive new chunks
             f.write(chunk)
    #f.close()
    return local_filename


parser = argparse.ArgumentParser()

#add command line arguments

parser.add_argument('Url', help='Url of the file you want to dowmload')
parser.add_argument('output',help='by which name you want to save your file')

#parse the arguments
args= parser.parse_args()

#use the arguments inyour code
print(args.url)
print(args.output)
DownloadFile(args.Url, args.output)

