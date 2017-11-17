# -*- coding: utf-8 -*-
import ner
#有问题
tagger = ner.HttpNER(host='localhost', port=8080)
# tagger.get_entities("University of California is located in California, United States")
tagger.json_entities("Alice went to the Museum of Natural History.")
