#-*- coding:utf-8 -*-

# import geniatagger

from geniatagger import GeniaTagger

tagger=GeniaTagger('D:/Python-work/python2.7/Lib/site-packages/geniatagger')
# tagger = GeniaTagger('.../path_to_geniatagger/geniatagger')


print GeniaTagger.parse('This is a pen.')