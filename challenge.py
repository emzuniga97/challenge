import requests, json, datetime, iso8601
from datetime import timedelta

github = 'https://github.com/emzuniga97/challenge.git'
token = '536f67e6a2d1286c789f2d3fb970d252'


def register():

    endpoint = 'http://challenge.code2040.org/api/register'
    r = requests.post(endpoint,{'github':github,'token':token})


def reverse():

    revurl = 'http://challenge.code2040.org/api/reverse'
    validate = 'http://challenge.code2040.org/api/reverse/validate'

    word = requests.post(revurl,{'token':token})
    mirror = word.text[::-1]
    r = requests.post(validate,{'token':token,'string':mirror})


def search():

    hayurl = 'http://challenge.code2040.org/api/haystack'
    validate = 'http://challenge.code2040.org/api/haystack/validate'

    bale = requests.post(hayurl,{'token':token})
    pybales = json.loads(bale.text)

    needle = pybales['needle']
    haystack = pybales['haystack']

    for i in range(len(haystack)):
        if haystack[i] == needle:
            r = requests.post(validate,{'token':token,'needle':i})
            break


def prefix():

    preurl = 'http://challenge.code2040.org/api/prefix'
    preval = 'http://challenge.code2040.org/api/prefix/validate'

    c2json = requests.post(preurl,{'token':token})

    strings = json.loads(c2json.text)

    prefix = strings['prefix']
    mess = strings['array']
    array = []

    for s in mess:
        if s[:(len(prefix))] != prefix:
            array.append(s)

    temp = {}
    temp['token'] = token
    temp['array'] = array

    r = requests.post(preval,json=temp)


def date():

    dateurl = 'http://challenge.code2040.org/api/dating'
    dateval = 'http://challenge.code2040.org/api/dating/validate'

    r = requests.post(dateurl,{'token':token})

    numbers = json.loads(r.text)

    datestamp = numbers['datestamp']
    interval = numbers['interval']

    start = iso8601.parse_date(datestamp)

    seconds = timedelta(seconds=int(float(interval)))

    finish = (start + seconds).isoformat()
    finish = finish[:-6]+'Z'

    a = requests.post(dateval,{'token':token,'datestamp':finish})



def main():

# Phase 1
#   register()
# Phase 2
#   reverse()
# Phase 3
#   search()
# Phase 4
#   prefix()
# Phase 5
#   date()

    print 'complete.'

if __name__ == '__main__':
  main()
