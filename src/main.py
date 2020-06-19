from pprint import pprint
import json

s = 'pusvwxvvwvwtwwwwxvwuxwwwxwxtwwwvwvxxwwxsuwwtxtwuvwxxsvxvxttwwrxwxwvvxwxttwxsxuuwtuwtuxuuwutwutxuvwtuwttxuuwttxuuw'
b = bytearray(s.encode())
samples = list(b)

run = {
    'runid': 0,
    'cdIn': '00 11 22 33 44 55 66 77',
    'cdOut': '77 66 55 44 33 22 11',
    'samples': samples
}

pprint(run)
with open('data.json', 'w') as fp:
    json.dump(run, fp, sort_keys=True, indent=4, separators=(',', ': '))
