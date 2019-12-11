from cassandra.cluster import Cluster
from cassandracsv import CassandraCsv
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='root', password='')
cluster = Cluster(['127.0.0.1'],auth_provider=auth_provider, port=9042);
session = cluster.connect("vendorproject")

result = session.execute("""SELECT * FROM vendorIDs;""")

CassandraCsv.export(result, output_dir="",filename="Data") # output_dir needs to be set