# Ecommerce Catalog API

## Authentication

To access the API endpoints is required a valid Token to be included in the header of the request:
```bash 
    'Authorization: Token a4f3ecdc0714a3b3b58cd80ca54e322512f77b63'
```

The Token can be acquired through the login with auth endpoints below:

###1. Registration:

**URL**
```bash
    POST localhost:8000/rest_auth/registration/
```
**Body**
```bash
{
    "username":"my_username", 
    "email": 'my_email@email.com',
    "password1":"my_password", 
    "password2":"my_password"
}  
```

**Success Response**

Code: ```200 OK```

Response: ```{"key":"a4f3ecdc0714a3b3b58cd80ca54e322512f77b63"}```

###2. Login:

**URL**
```bash
    POST localhost:8000/rest_auth/login/
```
**Body**
```bash
{
    "username": "my_username",
    "password": "my_password"
}   
```

**Success Response**

Code: ```200 OK```

Response: ```{"key":"a4f3ecdc0714a3b3b58cd80ca54e322512f77b63"}```

###3. Logout:

**URL**
```bash
    POST localhost:8000/rest_auth/logout/
```
**Header**
```bash
'Authorization: Token a4f3ecdc0714a3b3b58cd80ca54e322512f77b63'
```

**Success Response**

Code: ```200 OK```

Response: ```{"detail": "Successfully logged out."}```

###4. Request without Authentication Token:

Response:
   ```{"detail":"Authentication credentials were not provided."}```
   
    
## Catalog Endpoints

###Categoria:

* Get All: 
    URL: ```GET localhost:8000/api/v1/categorias/```

    Reponse:
    ```bash
    {
        "count": 0,
        "next": null,
        "previous": null,
        "results": []
    }
    ```

* Get By Id: 
    
    URL: ```GET localhost:8000/api/v1/categorias/<categoria_id>/```


* Create: 

    URL: ```POST localhost:8000/api/v1/categorias/```

    Body:
    ```bash
    {
        "nome": "Categoria Name"
    }  
    ```

* Update 

    URL: ```PUT localhost:8000/api/v1/categorias/<categoria_id>/```

    Body:
    ```bash
    {
        "nome": "Categoria Name Update"
    }  
    ```

* Delete: 

    URL: ```DELETE localhost:8000/api/v1/categorias/<categoria_id>/```
