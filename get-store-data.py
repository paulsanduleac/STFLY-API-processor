from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import requests

auth_provider = PlainTextAuthProvider(username='root', password='')
cluster = Cluster(['127.0.0.1'],auth_provider=auth_provider, port=9042);
session = cluster.connect("vendorproject")

query="TRUNCATE VendorIDs;"
result=session.execute(query)

vendorURL=input("Enter vendor API URL \n")
with open("uuid-list","r") as f:
    data=f.read().split('\n')

n=1
for i in data:
    print(i)
    response = requests.get(vendorURL + i)
    response_content=response.text.replace("'", "''") #sanitize quote marks
    response_headers=str(response.headers).replace("'", "''")
    insert_query = session.execute(f"INSERT INTO vendorIDs (id, uuid, api_response_code, api_response_content, api_response_headers) VALUES({n},'{i}','{response.status_code}','{response_content}','{response_headers}');")
    print(insert_query.current_rows)
    n+=1

cluster.shutdown()
