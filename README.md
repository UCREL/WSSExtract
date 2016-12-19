# The Web Sentence Sentiment Extractor

Using web scraping tools extracts sentiment values from different sentence/Twitter
sentiment classifiers that are on the web.

This repository contains 11 different scraping scripts of which each one
is a Python module that contains the function sentiment. The sentiment function
when called will return a list of tuple(s) where the first value in the tuple
is the text being classified and the second value is the sentiment value
associated to that text e.g.
[('some text', 'Positive')]
Note that each classifier can output a different sentiment value e.g. 1, 'Pos'
etc therefore below you will see a list of outputs for each script.

**ALSO NOTE** that the [Christopher Potts](chris_potts.py) script is slightly different
and contains 5 sentiment classifiers in one therefore its sentiment function
output is slightly different.

## DISCLAIMER
Please respect the terms and conditions of each sentiment tools that is being
scraped I nor any contributor to this project take any liability for the way
this tool is used. Hence why there are timeouts in each script by default.

## Sentiment value outputs
1. [miopia](miopia.py) values: 'positive', 'neutral', 'negative'.
2. [Christopher Potts](chris_potts.py) values for each of the sentence classifiers
that are on his website are calculated like so: Each word has a sentiment value
e.g. 0.5, 1, -1, -0.6 and as the sentence is made up of normally many words each
sentiment values associated to each word in the sentence is summed.
