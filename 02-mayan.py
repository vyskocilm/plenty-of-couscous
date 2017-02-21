#:: 0-.| .-| .|||-| ::-| .||-| ||
print "".join(("".join((y for y in x)) for x in 
( (chr (sum( (x if y != 0 else x*20 for y, x in
enumerate ( len(x)  if x != "0" else 0 for x in
(x.replace('|',':.:').replace(':','..')for x in
y))))) for y in x) for x in((x.split() for x in
y)for y in (x.split('-') for x in(x[1:] for x in
file(__file__, 'r') if x[0] == '#'))))))
#. :||-| ::||-| :|||-| .:|-| .-.| :-. .:||
