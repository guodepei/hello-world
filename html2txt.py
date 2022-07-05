import os
import re

def get_chapter_dict():
    pattern = re.compile(r'<dd><a href="/TunShiXingKong/(.*)">(.*)</a></dd>')
    with open('index.txt', mode='r') as index:
        fstr = index.read()
        content = re.findall(pattern, fstr)
        return(dict(content))


def convert():
    files = os.listdir('.')
    files.sort()
    pattern1 = re.compile(r'(?<=<div)(.*)(?=</div>)')
    pattern2 = re.compile(r'<br />&nbsp;&nbsp;&nbsp;&nbsp;(.*)')
    pattern3 = re.compile(r'<p>.*')
    chapter_dict = get_chapter_dict()
    with open('ebook.txt', mode='w') as fbook:
        for fname in files:
            if os.path.splitext(fname)[1] == '.html':
                fbook.write('\n' + fname + ' ' + chapter_dict[fname] + '\n\n')
                f = open(fname, 'r')
                fstr = f.read()
                content = re.findall(pattern2, fstr)
                for line in content:
                    fbook.write(re.sub(pattern3, '', line) + '\n')

if __name__ == '__main__':
    # get_chapter_dict()
    convert()
