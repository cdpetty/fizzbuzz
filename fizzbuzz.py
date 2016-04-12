def fb1():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print 'fizzbuzz'
        elif x % 3 == 0:
            print 'fizz'
        elif x % 5 == 0:
            print 'buzz'
        else:
            print x

def fb2():
    for x in range(1, 101):
        special = True
        output = ''
        if x % 3 == 0:
            output += 'fizz'
            special = False
        if x % 5 == 0:
            output += 'buzz'
            special = False
        if special:
            output += str(x)
        print output

def fb3():
    for x in range(1, 101):
        output = ''
        output += 'fizz' if x % 3 == 0 else ''
        output += 'buzz' if x % 5 == 0 else '' 
        print (x if output == '' else output)
        print output
        
def fb4():
    for x in range(1, 101):
        print 'fizz'*(1 if x % 3 == 0 else 0) + 'buzz'*(1 if x%5 == 0 else 0) + str(x)*(1 if x % 5 != 0 and x % 3 != 0 else 0)
    # map(lambda x: [x for x in range(1, 101)]

def fb5():
    print '\n'.join(map(lambda x: 'fizz'*(1 if x % 3 == 0 else 0) + 'buzz'*(1 if x%5 == 0 else 0) + str(x)*(1 if x % 5 != 0 and x % 3 != 0 else 0), xrange(1, 101)))

def fb6():
    print '\n'.join(map(lambda x: 'fizz'*(1 if x % 3 == 0 else 0) + 'buzz'*(1 if x%5 == 0 else 0) or str(x), xrange(1, 101)))

def fb7():
    print '\n'.join('fizz'*(x % 3 == 0) + 'buzz'*(x%5 == 0) or str(x) for x in xrange(1, 101))

def fb7():
    for i in range(1,101): 
        print "FizzBuzz"[i*i%3*4:8--i**4%5] or i

if __name__=='__main__':
    fb7()
