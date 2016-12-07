## Links that do not work
1. http://www.meaningcloud.com/demo
2. http://dtminredis.housing.salle.url.edu:8080/EmoLib/en/index.html
3. http://onlinesentiment.com/
4. https://twitter.25trends.me/services/twitter/public This needs to be a non https link like this:
http://twitter.25trends.me/services/twitter/public/
5. http://www.nactem.ac.uk/opminpackage/opinion_analysis

## Accurarcy note:
On tool 14 using sentence a which is the only one I tested I got a different accurarcy rating to the one stated in the paper.

## Has an API and is a company are we allowed to scrape?
1. http://apidemo.theysay.io/
2. https://www.repustate.com/api-demo/
3. http://www.opinioncrawl.com/OpinionCrawlTOS.htm in terms of use:
(i) automate the use of the website and the services, or in any way increase the volume of access to an unreasonably high level that interferes with the ability of Semantic Engines LLC to provide the service;
They do have an API but it is a free trail one see here:
http://www.sensebot.net/sentimentapi.aspx
4. http://twitter.25trends.me/terms.php In the terms and conditions: (b) use any automated tool (e.g., robots, spiders) in connection with the Service; shown here: http://twitter.25trends.me/terms.php
5. http://test.umigon.com/ has an API with a pricing guide:
https://dev.exploreyourdata.com/pricing.html
6. Do not think you can use http://liwc.wpengine.com/ due to this term and condition in their API http://www.receptiviti.ai/terms/ : (i) you may not store Receptiviti profiles and associated data, insights, results, scores or outputs (collectively, “Receptiviti Content”) in any medium of any kind, whether or electronic or physical, for more than 30 calendar days after receiving it; for clarity, Receptiviti Content held by you or by a third party on your behalf must be purged or destroyed at the end of such 30 calendar day period;
7. http://text2data.org/Pricing
8. has an API http://textanalysisonline.com/ at https://market.mashape.com/textanalysis/textanalysis which I believe is free but I think it would require a Card to make sure you get charged if over a limit.

## Copyright problems and paper referecning:
1. http://www.sentaero.com/terms.php

## Difficult or problems
1. http://textsentiment.com/twitter-sentiment-analyzer has an API but not sure if it is the correct one as their is no link between the two companies websites. https://market.mashape.com/fyhao/text-sentiment-analysis-method
2. http://sentiment.christopherpotts.net/lexicon/textscores_results/ - This is most likely to be difficult

## Has an API but not a company -- Note this is not a problem just somewhere to write the notes and let you know as well:
1. https://miopia.grupolys.org/docs
2. http://www.socialmention.com/api/
3. http://text-processing.com/docs/
4. http://www.sentimentanalysisonline.com/page/api-request/

## Has a ruby GEM/CMD interface
1. http://www.opener-project.eu/documentation/sentiment-scores.html

## Problems
http://www.sentaero.com/textsearch.php sentiment text search does not work
unless it has 5 unique words as input and all sentences that are tested
in the paper are 4 unique words long.
LIWC -- cannot find a way to evaluate it I'm guessing they have removed the
web front end that was orginally used.
sentimentanalysisonline - requires a topic and comment therefore I do not
know how to test this without having to sign up for a free API.
http://demo2-opener.rhcloud.com/welcome.action does not appear to be working
and nor does their ruby gem.

## Websites that do not support multi sentences
1. Repustate
2. miopia
3. text_processing

## Dryscrape jobs
1. theysay
2. werfamous
3. opinioncrawl - Very difficult the result is on an image and I can't find a
 way of reading it yet so skipping it til last. Also they have an API.
4. twitter.25trends.me - too difficult the sentiment is shown to you as a pie
chart.
5. umigon
6. http://www.danielsoper.com/sentimentanalysis/# the sentiment is shown as a
image therefore very difficult to collect the data.
