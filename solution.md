**System Requirements**  
Python 3.6 or higher  
adhere to requirements.txt

**Build/Install**  
`python3 -m pip install -r requirements.txt`

**Run**  
`python3 main.py`

_All HTTP requests must be routed to server/item_

**Retrieve item values**  
To get specific item values, submit a GET that includes a list of 
the interesting items' IDs. If the list contains a value that does 
not appear in items, then that ID value will return a NULL value.  

To get all items and values, submit a GET with no query parameters.

**Add an item**  
Submit a POST where  
'id' is the item's id  
'val' is the value associated with the item

**Modify/Update an item**  
The same as 'Add an item', where the item with 'id' already exists

**Deleting an item**  
Submit a DELETE where  
'id' is the id of the item to be removed  

=============== NOTES ==================  
**NOT a RESTful API**  
Note that the URL doesn't change for any of the CRUD operations. 
A RESTful API would have URLs that look like  
`http://server/v1/items/<id>/delete`  
`http://server/v1/items/delete?<id0>,<id1> ... <idn>`  
`http://server/v1/items/all`  
`http://server/v1/items/<id>`  
et cetera. 

Other items:  
Missing OPTIONS.  
Pagination: limit, and offset for returned lists.  
Use PUT/PATCH to update an existing item.  
There are many other REST items that may be added, depending on requirements.

**This a POC**  
There are things that are missing.  
Error handling is a big one. Along with that comes informative error messages.
