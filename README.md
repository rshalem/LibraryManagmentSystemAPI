# Library Management System API

## Endpoints for Registration & Login

---
```
REGISTER : api/users/register/ - creates a new User & generates Token
LOGIN: api/users/login/ - obtains auth token on successful authentication
```
---
## Endpoints for Authors API
---
```
CREATE: api/authors/create/ - creates a new instance of Author
READ: api/authors/get/ - gets all instances of Author
```
---
## Endpoints for Books API
---
```
CREATE: api/books/create/ - creates a new instance of Books Class
READ: api/books/get/ - gets all instances of Books Class
```
---
## Endpoints for Categories API
---
```
CREATE: api/categories/create/ - creates a new instance of Category Class
READ: api/categories/get/ - gets all instances of Category Class
```
---
## Endpoints for Analytics API
---
```
GET/READ: api/analytics/authors/<str:category_id>/ - gets how many authors belongs to which categories via category id
GET/READ: api/analytics/books/<str:category_id>/ - gets how many books belongs to which categories via category id
```
---

## NOTE:
* db used is sqlite3 keeping in mind the non scalability of this API
* audioFileID (has to be unique and interger), kept it as it is as Primary key or ID of the instances
* please ensure participants field data is inserted in this format, {'participants':"['test1','test2]"}
* django-mysql's ListCharField field is used, which requires list to be passed of type CharField with max length validation
* api working validation are done both via DRF's template view and POSTMAN
---