import requests, datetime, random, time

def unixMillis():
        return datetime.datetime.now().timestamp() * 1000

token = ""

class LanguageNut:
    
    class loginController:
        def attemptlogin(username, password):
            headers = {
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.languagenut.com',
                'Referer': 'https://www.languagenut.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            params = {
                'cacheBreaker': str(unixMillis()),
            }

            data = {
                'username': username,
                'pass': password,
                'loginType': 'browserLogin',
                'languagenutTimeMarker': str(unixMillis()),
                'lastLanguagenutTimeMarker': str(unixMillis()),
                'apiVersion': '9',
            }

            return requests.post('https://api.languagenut.com/loginController/attemptlogin', params=params, headers=headers,
                                 data=data).json()

    class assignmentController: 
        def getViewableAll(token):
            headers = {
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.languagenut.com',
                'Referer': 'https://www.languagenut.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            params = {
                'cacheBreaker': str(unixMillis()),
            }

            data = {
                'newPageTrigger': 'true',
                'newPage': 'Homework',
                'languagenutTimeMarker': str(unixMillis()),
                'lastLanguagenutTimeMarker': str(unixMillis() - 3000),
                'languagenutStatistics[]': 'curriculumHomework',
                'apiVersion': '9',
                'token': token,
            }

            response = requests.post(
                'https://api.languagenut.com/assignmentController/getViewableAll',
                params=params,
                headers=headers,
                data=data,
            ).json()
            token = response.get("newToken")
            return response

    class recentActivity:
        def getAllStudentActivity(token, id):
            headers = {
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.languagenut.com',
                'Referer': 'https://www.languagenut.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            params = {
                'cacheBreaker': str(int(time.time())),
            }

            data = {
                'studentID': str(id),
                'languageID': 'all',
                'to': str(int(time.time())),
                'from': '0',
                'seperateHomework': 'false',
                'limiter': '500',
                'languagenutTimeMarker': str(int(time.time())),
                'lastLanguagenutTimeMarker': str(int(time.time())),
                'apiVersion': '9',
                'token': token,
            }

            response = requests.post(
                'https://api.languagenut.com/recentActivity/getAllStudentActivity',
                params=params,
                headers=headers,
                data=data,
            ).json()
            token = response.get("newToken")
            return response

    class sentenceTranslationController:
        def getSentenceTranslations(game_uid, catalogUid):
            headers = {
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.languagenut.com',
                'Referer': 'https://www.languagenut.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            data = {
                'gameUid': game_uid,
                'catalogUid': catalogUid,
                'toLanguage': 'de',
                'fromLanguage': 'en-GB',
                'languagenutTimeMarker': str(unixMillis()),
                'lastLanguagenutTimeMarker': str(unixMillis() - 3000),
                'apiVersion': '9',
                'token': token,
            }

            response = requests.post(
                'https://api.languagenut.com/sentenceTranslationController/getSentenceTranslations',
                headers=headers,
                data=data,
            )
    
    class vocabTranslationController:
        def getVocabTranslations(token, catalogUid, homeworkUid):
            headers = {
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.languagenut.com',
                'Referer': 'https://www.languagenut.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            params = {
                'cacheBreaker': str(unixMillis()),
            }

            data = {
                'catalogUid[]': catalogUid,
                'toLanguage': 'de',
                'fromLanguage': 'en-GB',
                'homeworkUid': homeworkUid,
                'languagenutTimeMarker': str(unixMillis()),
                'lastLanguagenutTimeMarker': str(unixMillis() - 3000),
                'apiVersion': '9',
                'token': token,
            }

            response = requests.post(
                'https://api.languagenut.com/vocabTranslationController/getVocabTranslations',
                params=params,
                headers=headers,
                data=data,
            ).json()
            token = response.get("newToken")
            return response

    class gameDataController:
        def addGameScore(token, moduleUid, gameType, homeworkUid, gameUid, isTest, correctVocabs, incorrectVocabs, isSentence, featureUid,
                 isALevel, isVerb, isGrammar, isExam, timeStamp, vocabNumber, correctStudentAns, languagenutTimeMarker,
                 lastLanguagenutTimeMarker):
            headers = {
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.languagenut.com',
                'Referer': 'https://www.languagenut.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            params = {
                'cacheBreaker': str(unixMillis()),
            }

            #print(moduleUid, gameType, homeworkUid, gameUid, isTest, correctVocabs, incorrectVocabs, isSentence, featureUid,
            #        isALevel, isVerb, isGrammar, isExam, timeStamp, vocabNumber, correctStudentAns, languagenutTimeMarker,
            #        lastLanguagenutTimeMarker)

            data = "moduleUid=" + moduleUid + "&gameUid=" + gameUid + "&gameType=" + gameType + "&isTest=" + isTest + "&toietf=de&fromietf=en-GB&score=2000&correctVocabs=" \
                + correctVocabs + "&incorrectVocabs=" + incorrectVocabs + "&homeworkUid=" + homeworkUid + "&featureUid=" + featureUid + "&isSentence=" + isSentence \
                + "&isALevel=" + isALevel + "&isVerb=" + isVerb + "&grammarCatalogUid=" + moduleUid + "&isGrammar=" + isGrammar + "&isExam=" + isExam + "&timeStamp=" \
                + timeStamp + "&vocabNumber=" + vocabNumber + "&rel_module_uid=" + moduleUid + "&dontStoreStats=true&correctStudentAns=&incorrectStudentAns=&product=secondary\
              &languagenutTimeMarker=" + languagenutTimeMarker + "&lastLanguagenutTimeMarker=" + lastLanguagenutTimeMarker + "&apiVersion=9&token=" + token

            response = requests.post('https://api.languagenut.com/gameDataController/addGameScore', params=params,
                                     headers=headers, data=data).json()
            token = response.get("newToken")
            return response

