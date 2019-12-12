# projectGuid#
# userId#
# userFirstName#
# userLastName#
# channel#
# platform#
# landingPageThumbnailUrl#
# previewTitle#
# previewSubtitle
# shareUrl#
# makeMyOwnUrl#
# editProjectUrl#

import re
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import tuple_factory

auth_provider = PlainTextAuthProvider(username='root', password='')
cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider, port=9042);
session = cluster.connect("vendorproject")
session.row_factory = tuple_factory
session.execute("TRUNCATE vendorcontent;")

pattern = []
pattern.append('(?<="projectGuid":")([-0-z]*)(?=")')
pattern.append('(?<="userId":")(\d*)(?=")')
pattern.append('(?<="userFirstName":")([0-z]*)(?=")')
pattern.append('(?<="userLastName":")([0-z]*)(?=")')
pattern.append('(?<="channel":")([-0-z]*)(?=")')
pattern.append('(?<="platform":")([-0-z]*)(?=")')
pattern.append('(?<="landingPageThumbnailUrl":")([a-zA-Z0-9\-\.\:\/]*)')
pattern.append('(?<="shareUrl":")([a-zA-Z0-9\-\.\:\/]*)')
pattern.append('(?<="makeMyOwnUrl":")([a-zA-Z0-9\-\.\:\/]*)')
pattern.append('(?<="editProjectUrl":")([a-zA-Z0-9\-\.\:\/]*)')
pattern.append('(?<="previewTitle":")([\(\) a-zA-Z0-9\-\.\:\/]*)')
pattern.append('(?<="previewSubtitle":")([\(\) a-zA-Z0-9\-\.\:\/]*)')


result = session.execute("SELECT id,api_response_content FROM VENDORIDS;")

for i in result:
    insert = []
    for regex in pattern:
        #print(regex)
        match = re.search(regex, i[1])
        if match:
            insert.append(match[0])
        else:
            insert.append('not found')
    session.execute(f"""INSERT INTO vendorcontent (id,projectGuid,userid,userFirstName, userLastName, channel, platform, landingPageThumbnailUrl, shareUrl, makeMyOwnUrl, editProjectUrl, previewTitle, previewSubtitle) VALUES ({i[0]},'{insert[0]}','{insert[1]}','{insert[2]}', '{insert[3]}', '{insert[4]}', '{insert[5]}', '{insert[6]}', '{insert[7]}', '{insert[8]}', '{insert[9]}', '{insert[10]}','{insert[11]}');""")
    #print(insert)

cluster.shutdown()
