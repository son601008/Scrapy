from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "graph"))

'''def add_friend(tx, name, friend_name):
    #return tx.run(  "LOAD CSV WITH HEADERS FROM \"file:/n4jtest.csv\" AS line " 
     #               "MERGE (n:news {dataid: line.dataid, link: line.link, name: line.name})")
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)
def print_friends(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
                            print(record["friend.name"])'''


with driver.session() as session:
    session.run("LOAD CSV WITH HEADERS FROM \"file:/tiki.csv\" AS line " 
                "MERGE (n:products {dataid: line.dataid, title: line.title, link: line.link})")
    '''session.write_transaction(add_friend, "Arthur", "Guinevere")
    session.write_transaction(add_friend, "Arhur", "Lancelot")
    session.write_transaction(add_friend, "Arthur", "Merlin")
    session.read_transaction(print_friends, "Arthur")'''

