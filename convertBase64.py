import os
import base64
import re

def img_bs64(infile,outfile='', savefile =''):
    f=open(infile,'rb')
    pbs64=base64.b64encode(f.read()) 
    f.close()
    return pbs64.decode('utf-8')

if __name__ == '__main__':
    os.makedirs(os.path.dirname('./temp'), exist_ok=True)
    filenames = next(os.walk('./temp'), (None, None, []))[2]  # [] if no images
    if filenames and re.search('.*.md', filenames[0]):
        outputpath = './out/'+filenames[0].split('.')[0] + '.md'
        os.makedirs(os.path.dirname(outputpath), exist_ok=True)
        if os.path.exists(outputpath):
            os.remove(outputpath)
        with open(outputpath, 'a') as outfile:
            with open('./temp/' + filenames[0]) as file:
                while line := file.readline():
                    pattern = '!\[.*]\(.\/temp//media/image.*\)'
                    stringToReplace = re.findall(pattern, line)
                    if stringToReplace:
                        paths = re.findall('./temp//media/image.*\)', stringToReplace[0])
                        if paths: # PATH)
                            pbs64 = img_bs64(paths[0][:-1])
                            outfile.write(line.replace(stringToReplace[0], '![](data:image/png;base64,'+ pbs64 + ')'))
                        else:
                            outfile.write(line)
                    else:
                        outfile.write(line)
