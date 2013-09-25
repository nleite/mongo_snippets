import random
import string
from datetime import datetime
from pymongo import MongoClient
import gridfs

def genvalue(size):
    return "".join(random.sample( string.ascii_letters, size))

def genint(size):
    return "".join(random.sample( string.digits*4, size))

def build():
    d = {}
    d['nif'] = genvalue(10)
    d['date'] = datetime.today()
    d['value'] = genint(10)
    d['zip'] = genint(4)
    d['client_id'] = genvalue(10)
    return d


def run(host, ndocs):
    mc = MongoClient(host)
    db = mc.example
    gfs = gridfs.GridFS(db)

    for i in range(ndocs):
        name = genvalue(12)
        with open("example.pdf") as pdf:
            oid = gfs.put(pdf, content_type="application/pdf", filename=name)
            doc = build()
            doc['file_id'] = oid
            db.metadata.insert(doc)


if __name__ == "__main__":
    import timeit
    timeit.timeit(run("nair.local", 10000))



