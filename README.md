# The Web Sentence Sentiment Extractor (WSSExtract)

## Install and requirements:
1. Python 3.6
2. pip install .

## General
Contains 4 working sentiment systems that all have a common API.

## Example

See the following Jupyter notebook for an [example](./notebooks/example.ipynb)

## DISCLAIMER
Please respect the terms and conditions of each sentiment tools that is being
scraped I nor any contributor to this project take any liability for the way
this tool is used. Hence why there are timeouts in each script by default.

### Text Processing
This has an explicit rate limit of 1000 calls per day see [here](http://text-processing.com/docs/index.html) for details. We have added timeouts to the calls but this is not enough to stop you from going over the rate limit. Therefore it is upon the users of this project to respect these rate limits.

## Sentiment value outputs for working APIs
1. [Repustate](./wss_extract/repustate.py). Real value between -1 and 1
2. [SentiStrength](./wss_extract/sentistrength.py). Binary value either -1 or 1.
3. [Text Analysis Online](./wss_extract/text_analysis_online.py). Real value between -1 and 1
4. [Text Processing](./wss_extract/text_processing.py). One of the following Strings: `pos`, `neg` or `neutral`

## Sentiment systems that do not work
1. [Christopher Potts](./wss_extract/chris_potts.py) - Contains 5 different sentiment systems
