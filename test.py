from collections import OrderedDict
import traceback
import logging

import miopia
import repustate
import sentistrength
import sisa
import text_analysis_online
import text_processing
import text2data
import textsentiment
import tweenator
import werfamous_twitter
import chris_potts

sentiment_funcs = [sisa, sentistrength, miopia, repustate, text_analysis_online,
                   text_processing, text2data, werfamous_twitter]

logging.basicConfig(filename='test.log',level=logging.DEBUG)

input_file = 'input.txt'
sentiment_sentences = []
with open(input_file, 'r', encoding='utf-8') as fp:
    for sentiment_sentence in fp:
        sentiment_sentences.append(sentiment_sentence.strip())

no_sentences = len(sentiment_sentences)
sentiment_scores = {}
if no_sentences:
    for sentiment_func in sentiment_funcs:
        for sentiment_sentence in sentiment_sentences:
            try:
                logging.info('Processing this sentence {} with this classifier {}'.format(sentiment_sentence, sentiment_func.__name__))
                senti_score = getattr(sentiment_func, 'sentiment')(sentiment_sentence)
                if len(senti_score) != 1:
                    to_many_sents_err = ('The {} classifier think this sentence'
                                         ' is made up of more than one '
                                         'sentence {}. Therefore gets a score '
                                         'of unclassified'
                                         ).format(sentiment_func, senti_score)
                    print(to_many_sents_err)
                    senti_score = [(None, 'unclassified')]
                senti_score = str(senti_score[0][1])
                senti_func_name = sentiment_func.__name__
                if sentiment_sentence in sentiment_scores:
                    sentence_scores = sentiment_scores[sentiment_sentence]
                    if senti_func_name not in sentence_scores:
                        sentence_scores[senti_func_name] = senti_score

                    else:
                        logging.error('{} classifier is being applied to the sentence twice'.format(senti_func_name))
                else:
                    score_dict = OrderedDict([(senti_func_name, senti_score)])
                    sentiment_scores[sentiment_sentence] = score_dict
            except Exception as e:
                traceback_msg = traceback.extract_tb(e.__traceback__)
                traceback_msg = ''.join(traceback.format_list(traceback_msg))
                logging.error("Error {} TRACEBACK {}".format(e, traceback_msg))
                logging.error("Sentence and classifier it occured on: {} {}".format(sentiment_sentence, sentiment_func.__name__))
                continue

    logging.info('Number of sentiment sentences to process {}'.format(no_sentences))

else:
    logging.warning('No sentiment sentences to process')

chris_potts_clf = []
for sentiment_sentence in sentiment_sentences:
    senti_scores = chris_potts.sentiment(sentiment_sentence)
    for clf_info in senti_scores:
        senti_clf = clf_info[0]
        if senti_clf not in chris_potts_clf:
            chris_potts_clf.append(senti_clf)
        senti_score = str(clf_info[1][0][1])
        if sentiment_sentence in sentiment_scores:
            sentence_scores = sentiment_scores[sentiment_sentence]
            if senti_clf not in sentence_scores:
                sentence_scores[senti_clf] = senti_score

            else:
                logging.error('{} classifier is being applied to the sentence twice'.format(senti_func_name))
        else:
            score_dict = OrderedDict([(senti_clf, senti_score)])
            sentiment_scores[sentiment_sentence] = score_dict


result_file = 'results.tsv'
with open(result_file, 'w') as fp:
    senti_func_names = list(sentiment_scores[sentiment_sentences[0]].keys())
    senti_func_names.insert(0, '')
    top_line = '\t'.join(senti_func_names)
    fp.write(top_line + "\n")
    for sentence, func_score in sentiment_scores.items():
        sentence = sentence.replace('\t', '')
        fp.write(sentence + "\t")
        num_funcs = len(func_score)
        count = 0
        import code
        code.interact(local=locals())
        for func, score in func_score.items():
            count += 1
            # Handle end of lines
            if count == num_funcs:
                import code
                code.interact(local=locals())
                fp.write(score + "\n")
            else:
                fp.write(score + "\t")
