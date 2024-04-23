from pymilvus import connections, db

conn = connections.connect(host="127.0.0.1", port=19530)

print(db.list_database())


