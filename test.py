from functools import partial

def iter():
    n=2
    while True:
        yield n
        n+=1

def isprime(n):
    it=iter()
    u=next(it)
    while u<n:
        yield u
        it=filter(partial(lambda x,p:x%p>0,p=u),it)
        u=next(it)

for i in isprime(10):
    print(i)
