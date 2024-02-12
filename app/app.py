import os

from neo4j import GraphDatabase

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASS")  # Replace with your password

# sleep for 5 seconds to wait for neo4j to start
import time
time.sleep(5)

driver = GraphDatabase.driver(uri, auth=(user, password))

# Function to create graph
def create_graph(driver):
    with driver.session() as session:
        query = (
            "MERGE (a:Person {name: 'Alice'}) "
            "MERGE (b:Person {name: 'Bob'}) "
            "MERGE (a)-[:KNOWS]->(b)"
        )
        session.run(query)
        print("Graph created.")

def query_graph(driver):
    with driver.session() as session:
        query = (
            "MATCH (a:Person {name: 'Alice'})-[:KNOWS]->(person) "
            "RETURN person.name AS name"
        )
        result = session.run(query)
        print("Alice knows:")
        for record in result:
            print(record["name"])

# Execute the function
create_graph(driver)
query_graph(driver)

# Close the connection
driver.close()
