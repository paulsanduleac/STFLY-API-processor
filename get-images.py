from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import requests

auth_provider = PlainTextAuthProvider(username='root', password='')
cluster = Cluster(['127.0.0.1'],auth_provider=auth_provider, port=9042);
session = cluster.connect("vendorproject")

query="SELECT userid,Landingpagethumbnailurl FROM vendorcontent;"
result=session.execute(query)

for i in result:
    print(i[1])
    file = requests.get(i[1])
    with open("image"+i[0]+".jpeg", "wb") as f:
        f.write(file.content)