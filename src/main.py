from pprint import pprint
import json

print('Hello, world!')

s = 'pusvwxvvwvwtwwwwxvwuxwwwxwxtwwwvwvxxwwxsuwwtxtwuvwxxsvxvxttwwrxwxwvvxwxttwxsxuuwtuwtuxuuwutwutxuvwtuwttxuuwttxuuw'
b = bytearray(s.encode())
result = list(b)

run = {
    'runid': 0,
    'cdIn': '00 11 22 33 44 55 66 77',
    'cdOut': '77 66 55 44 33 22 11',
    'samples': result
}

pprint(run)
with open('data_more.json', 'w') as fp:
    json.dump(run, fp)
