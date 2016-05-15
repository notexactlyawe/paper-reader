from __future__ import print_function
import requests

try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
    from urllib.parse import urlencode
except ImportError:
    from urlparse import urlparse
    from urllib2 import urlopen
    from urllib import urlencode

try:
    import json
except ImportError:
    # Older versions of Python (i.e. 2.4) require simplejson instead of json
    import simplejson as json


class AlchemyAPI:
    # Setup the endpoints
    ENDPOINTS = {}
    ENDPOINTS['sentiment'] = {}
    ENDPOINTS['sentiment']['url'] = '/url/URLGetTextSentiment'
    ENDPOINTS['sentiment']['text'] = '/text/TextGetTextSentiment'
    ENDPOINTS['sentiment']['html'] = '/html/HTMLGetTextSentiment'
    ENDPOINTS['sentiment_targeted'] = {}
    ENDPOINTS['sentiment_targeted']['url'] = '/url/URLGetTargetedSentiment'
    ENDPOINTS['sentiment_targeted']['text'] = '/text/TextGetTargetedSentiment'
    ENDPOINTS['sentiment_targeted']['html'] = '/html/HTMLGetTargetedSentiment'
    ENDPOINTS['author'] = {}
    ENDPOINTS['author']['url'] = '/url/URLGetAuthor'
    ENDPOINTS['author']['html'] = '/html/HTMLGetAuthor'
    ENDPOINTS['keywords'] = {}
    ENDPOINTS['keywords']['url'] = '/url/URLGetRankedKeywords'
    ENDPOINTS['keywords']['text'] = '/text/TextGetRankedKeywords'
    ENDPOINTS['keywords']['html'] = '/html/HTMLGetRankedKeywords'
    ENDPOINTS['concepts'] = {}
    ENDPOINTS['concepts']['url'] = '/url/URLGetRankedConcepts'
    ENDPOINTS['concepts']['text'] = '/text/TextGetRankedConcepts'
    ENDPOINTS['concepts']['html'] = '/html/HTMLGetRankedConcepts'
    ENDPOINTS['entities'] = {}
    ENDPOINTS['entities']['url'] = '/url/URLGetRankedNamedEntities'
    ENDPOINTS['entities']['text'] = '/text/TextGetRankedNamedEntities'
    ENDPOINTS['entities']['html'] = '/html/HTMLGetRankedNamedEntities'
    ENDPOINTS['category'] = {}
    ENDPOINTS['category']['url'] = '/url/URLGetCategory'
    ENDPOINTS['category']['text'] = '/text/TextGetCategory'
    ENDPOINTS['category']['html'] = '/html/HTMLGetCategory'
    ENDPOINTS['relations'] = {}
    ENDPOINTS['relations']['url'] = '/url/URLGetRelations'
    ENDPOINTS['relations']['text'] = '/text/TextGetRelations'
    ENDPOINTS['relations']['html'] = '/html/HTMLGetRelations'
    ENDPOINTS['language'] = {}
    ENDPOINTS['language']['url'] = '/url/URLGetLanguage'
    ENDPOINTS['language']['text'] = '/text/TextGetLanguage'
    ENDPOINTS['language']['html'] = '/html/HTMLGetLanguage'
    ENDPOINTS['text'] = {}
    ENDPOINTS['text']['url'] = '/url/URLGetText'
    ENDPOINTS['text']['html'] = '/html/HTMLGetText'
    ENDPOINTS['text_raw'] = {}
    ENDPOINTS['text_raw']['url'] = '/url/URLGetRawText'
    ENDPOINTS['text_raw']['html'] = '/html/HTMLGetRawText'
    ENDPOINTS['title'] = {}
    ENDPOINTS['title']['url'] = '/url/URLGetTitle'
    ENDPOINTS['title']['html'] = '/html/HTMLGetTitle'
    ENDPOINTS['feeds'] = {}
    ENDPOINTS['feeds']['url'] = '/url/URLGetFeedLinks'
    ENDPOINTS['feeds']['html'] = '/html/HTMLGetFeedLinks'
    ENDPOINTS['microformats'] = {}
    ENDPOINTS['microformats']['url'] = '/url/URLGetMicroformatData'
    ENDPOINTS['microformats']['html'] = '/html/HTMLGetMicroformatData'
    ENDPOINTS['combined'] = {}
    ENDPOINTS['combined']['url'] = '/url/URLGetCombinedData'
    ENDPOINTS['combined']['text'] = '/text/TextGetCombinedData'
    ENDPOINTS['image'] = {}
    ENDPOINTS['image']['url'] = '/url/URLGetImage'
    ENDPOINTS['imagetagging'] = {}
    ENDPOINTS['imagetagging']['url'] = '/url/URLGetRankedImageKeywords'
    ENDPOINTS['imagetagging']['image'] = '/image/ImageGetRankedImageKeywords'
    ENDPOINTS['facetagging'] = {}
    ENDPOINTS['facetagging']['url'] = '/url/URLGetRankedImageFaceTags'
    ENDPOINTS['facetagging']['image'] = '/image/ImageGetRankedImageFaceTags'
    ENDPOINTS['taxonomy'] = {}
    ENDPOINTS['taxonomy']['url'] = '/url/URLGetRankedTaxonomy'
    ENDPOINTS['taxonomy']['html'] = '/html/HTMLGetRankedTaxonomy'
    ENDPOINTS['taxonomy']['text'] = '/text/TextGetRankedTaxonomy'

    # The base URL for all endpoints
    BASE_URL = 'http://access.alchemyapi.com/calls'

    s = requests.Session()

    def __init__(self):
        import sys

        self.apikey = "72fcb566c0b4a99e821816b5324078d1f7e00a34"


    def entities(self, flavor, data, options={}):


        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['entities']:
            return {'status': 'ERROR', 'statusInfo': 'entity extraction for ' + flavor + ' not available'}

        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['entities'][flavor], {}, options)

    def keywords(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['keywords']:
            return {'status': 'ERROR', 'statusInfo': 'keyword extraction for ' + flavor + ' not available'}

        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['keywords'][flavor], {}, options)

    def concepts(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['concepts']:
            return {'status': 'ERROR', 'statusInfo': 'concept tagging for ' + flavor + ' not available'}

        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['concepts'][flavor], {}, options)

    def sentiment(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['sentiment']:
            return {'status': 'ERROR', 'statusInfo': 'sentiment analysis for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['sentiment'][flavor], {}, options)

    def sentiment_targeted(self, flavor, data, target, options={}):

        if target is None or target == '':
            return {'status': 'ERROR', 'statusInfo': 'targeted sentiment requires a non-null target'}

        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['sentiment_targeted']:
            return {'status': 'ERROR', 'statusInfo': 'targeted sentiment analysis for ' + flavor + ' not available'}

        # add the URL encoded data and target to the options and analyze
        options[flavor] = data
        options['target'] = target
        return self.__analyze(AlchemyAPI.ENDPOINTS['sentiment_targeted'][flavor], {}, options)

    def text(self, flavor, data, options={}):

        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['text']:
            return {'status': 'ERROR', 'statusInfo': 'clean text extraction for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['text'][flavor], options)

    def text_raw(self, flavor, data, options={}):

        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['text_raw']:
            return {'status': 'ERROR', 'statusInfo': 'raw text extraction for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['text_raw'][flavor], {}, options)

    def author(self, flavor, data, options={}):

        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['author']:
            return {'status': 'ERROR', 'statusInfo': 'author extraction for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['author'][flavor], {}, options)

    def language(self, flavor, data, options={}):
        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['language']:
            return {'status': 'ERROR', 'statusInfo': 'language detection for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['language'][flavor], {}, options)

    def title(self, flavor, data, options={}):

        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['title']:
            return {'status': 'ERROR', 'statusInfo': 'title extraction for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['title'][flavor], {}, options)

    def relations(self, flavor, data, options={}):
        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['relations']:
            return {'status': 'ERROR', 'statusInfo': 'relation extraction for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['relations'][flavor], {}, options)

    def category(self, flavor, data, options={}):

        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['category']:
            return {'status': 'ERROR', 'statusInfo': 'text categorization for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data

        return self.__analyze(AlchemyAPI.ENDPOINTS['category'][flavor], {}, options)

    def feeds(self, flavor, data, options={}):


        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['feeds']:
            return {'status': 'ERROR', 'statusInfo': 'feed detection for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['feeds'][flavor], {}, options)

    def microformats(self, flavor, data, options={}):


        # Make sure this request supports this flavor
        if flavor not in AlchemyAPI.ENDPOINTS['microformats']:
            return {'status': 'ERROR', 'statusInfo': 'microformat extraction for ' + flavor + ' not available'}

        # add the data to the options and analyze
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['microformats'][flavor], {}, options)

    def imageExtraction(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['image']:
            return {'status': 'ERROR', 'statusInfo': 'image extraction for ' + flavor + ' not available'}
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['image'][flavor], {}, options)

    def taxonomy(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['taxonomy']:
            return {'status': 'ERROR', 'statusInfo': 'taxonomy for ' + flavor + ' not available'}
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['taxonomy'][flavor], {}, options)

    def combined(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['combined']:
            return {'status': 'ERROR', 'statusInfo': 'combined for ' + flavor + ' not available'}
        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['combined'][flavor], {}, options)

    def imageTagging(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['imagetagging']:
            return {'status': 'ERROR', 'statusInfo': 'imagetagging for ' + flavor + ' not available'}
        elif 'image' == flavor:
            image = open(data, 'rb').read()
            options['imagePostMode'] = 'raw'
            return self.__analyze(AlchemyAPI.ENDPOINTS['imagetagging'][flavor], options, image)

        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['imagetagging'][flavor], {}, options)

    def faceTagging(self, flavor, data, options={}):

        if flavor not in AlchemyAPI.ENDPOINTS['facetagging']:
            return {'status': 'ERROR', 'statusInfo': 'facetagging for ' + flavor + ' not available'}
        elif 'image' == flavor:
            image = open(data, 'rb').read()
            options['imagePostMode'] = 'raw'
            return self.__analyze(AlchemyAPI.ENDPOINTS['facetagging'][flavor], options, image)

        options[flavor] = data
        return self.__analyze(AlchemyAPI.ENDPOINTS['facetagging'][flavor], {}, options)

    def __analyze(self, endpoint, params, post_data=bytearray()):

        params['apikey'] = self.apikey
        params['outputMode'] = 'json'


        post_url = ""
        try:
            post_url = AlchemyAPI.BASE_URL + endpoint + \
                '?' + urlencode(params).encode('utf-8')
        except TypeError:
            post_url = AlchemyAPI.BASE_URL + endpoint + '?' + urlencode(params)

        results = ""
        try:
            results = self.s.post(url=post_url, data=post_data)
        except Exception as e:
            print(e)
            return {'status': 'ERROR', 'statusInfo': 'network-error'}
        try:
            return results.json()
        except Exception as e:
            if results != "":
                print(results)
            print(e)
            return {'status': 'ERROR', 'statusInfo': 'parse-error'}