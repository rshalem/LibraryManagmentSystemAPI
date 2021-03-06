# Library Management System API

# Changing this line to change something and make a pull request

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
CREATE: api/books/create/ - creates a new instance of Book (adding Authors & Categories to Book instance)

READ: api/books/get/ - gets all instances of Book
```
---
## Endpoints for Categories API
---
```
CREATE: api/categories/create/ - creates a new instance of Category

READ: api/categories/get/ - gets all instances of Category
```
---
## Endpoints for Analytics API
---
```
GET/READ: api/analytics/authors/<str:category_name>/ - gets how many authors belongs to which categories via category name

GET/READ: api/analytics/books/<str:category_name>/ - gets how many books belongs to which categories via category name
```
---

## NOTE:
* db used is sqlite3 keeping in mind the non scalability of this API
* Make sure to add Token inside header as **KEY**: Authorization & **VALUE**: Token c776ec417e7ef27c29e20134bf7ec0d2b0425
* category name used while fetching analytics should be unique in the db
* please ensure authors & categories m2m field data is inserted in this format, {'authors': ['test1','test2], 'categories': ['thriller','fiction'] }
* API Testing is done via POSTMAN & Rest Framework's APITestCase Class
* Endpoints are all mentioned above.
---