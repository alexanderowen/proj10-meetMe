"""
Just to test database functions,
outside of Flask.

We want to open our MongoDB database,
insert some proposals, and read them back
"""

# MongoDB Python module
from pymongo import MongoClient
import CONFIG
import sys

try: 
    dbclient = MongoClient(CONFIG.MONGO_URL)
    db = dbclient.meetings
    proposal_collection = db.proposals
    busy_collection = db.busy_times
except:
    print("Failure opening database.  Is Mongo running? Correct password?")
    sys.exit(1)
    
'''
proposal = {
	"type": "proposal",
	"start_date": '03/04/2016',
	"end_date": '03/06/2016',
	"start_time": '10:00',
	"end_time": '20:00',
	"proposer_name": 'Alex',
	"desc": 'This is a test meeting proposal',
	"title": 'Testing 1, 2, 3'
}

result = proposal_collection.insert_one(proposal)

busy = {
	"type": "busy_time",
	"proposal_ID": result.inserted_id,
	"start": '2016-03-04T12:00:00+00:00',
	"end": '2016-03-04T13:00:00+00:00',
	"name": 'Fox'
}

busy_result = busy_collection.insert_one(busy)
'''

records = []
for record in proposal_collection.find( {"type": "proposal"} ):
	records.append(
		{ "type": record['type'],
		  "sd": record['start_date'],
		  "desc": record["desc"]
		}
	)
	print(record)
	
#proposal_collection.delete_one( {'_id': record['_id'] } )

for record in busy_collection.find( {"type":"busy_time"} ):
	print(record)
	
	
#busy_collection.delete_one( {'_id': record['_id'] } )