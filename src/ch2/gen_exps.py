import array

symbols = '$¢£¥€¤'
tp = tuple(ord(symbol) for symbol in symbols)
print(tp)

ar = array.array('I', (ord(symbol) for symbol in symbols))
print(ar)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
