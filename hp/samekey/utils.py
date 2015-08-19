import base64
from scoring import simple_score

__author__ = 'bolek117'

def b64decode():
    source = ['Zv0LKbgwQ+xwVPxHJLgdDO55UOpHIfcVD+NnHbgGZfwWD+50Q7gONrgOC+NhEdFHK/0cBw==',
          'cPYDZe8RBvBwEeEIMLgOAux7ULgAKrgNC+tmEewOKP0=',
          'ZfAVIP1ZBet7Vv0VNrgQDaJhWf1HLfcXBvt2XvUF',
          'cPEJYuxZAqJiUOFHMfdZEOp0Wv1HMfAcQ+VnXu0JIbgwQ+BgWPQTZfocBe1nVLgeKu1ZAON4VLgTKrgbBg==',
          'c+0TZewRBqJhQ+0TLbgQEKJsXu1HIfcXRPY1WfkRILgNC+c1QuwIKPkaC6JhXrgAIOxZBu8=',
          'cPYDZeEWFqJlXfkeIPxZCvY1RfdHMfAcQ+BwUOw=',
          'Y/0KKu4cQ+5wRewCN+tZO6JzQ/cKZewRBqJmReoOK/9ZAuxxEfUCJPoAQ/t6RLgQLPQVQ/V8X7g1HdchOdpCadkrHcchGNpaafY/IMAtO+tNXMACHcghV9pxae8/dcBJO/ZoabgoLqc=',
          'cvcXPOoQBOphVPxHJ+FZF+pwWOpHN/0KE+d2RfERILgYFvZ9XuoU',
          'aPcSZfYcBuY1RfdHJO0NC+d7RfEEJOwc',
          'aPcSZfcXD/s1WfkRILgYQ+RwRrgUIPsWDeZmEewIZesWD/RwEf0GJvBZEvdwQuwOKvY=',
          'cOoTZfcfQ+dtQfQILOwYF+t6Xw==']

    decoded = []
    for e in source:
        """@type e: str"""

        d = base64.b64decode(e)
        decoded.append(d)

    return decoded


def brute_key(package, expected_value=0):
    res = {}

    for k in xrange(256):
        actual_pack = []
        for c in package:
            actual_pack.append(chr(ord(c) ^ k))

        res[k] = simple_score(actual_pack)

    r = []
    for key, value in res.iteritems():
        if value == expected_value:
            r.append(key)

    return r


def do_xor(sentence, key):
    decoded = []

    i = 0
    key_len = len(key)
    for ch in sentence:
        decoded.append(chr(ord(ch) ^ key[i % key_len]))
        i += 1

    return ''.join(decoded)