# Ecommerce Catalog API Documentation

## Summary

* [Authentication](#authentication)
* [API Status](#api-status)
* [Catalog Endpoints](#catalog-endpoints)
* [Pagination](#pagination)


## Authentication

To access the API endpoints is required a valid Token to be included in the header of the request:
```bash 
'Authorization: Token a4f3ecdc0714a3b3b58cd80ca54e322512f77b63'
```

The Token can be acquired through the login with auth endpoints below:

### 1. Registration:

**URL:**
```bash
localhost:8000/rest_auth/registration/
```

**Method:** ```POST```

**Body:**
```bash
{
    "username":"my_username", 
    "email": 'my_email@email.com',
    "password1":"my_password", 
    "password2":"my_password"
}  
```

**Response** ```200 OK``` 

```bash
{"key":"a4f3ecdc0714a3b3b58cd80ca54e322512f77b63"}
```

### 2. Login:

**URL:**
```bash
localhost:8000/rest_auth/login/
```

**Method:** ```POST```

**Body:**
```bash
{
    "username": "my_username",
    "password": "my_password"
}   
```

**Response:** ```200 OK```

```bash
{"key":"a4f3ecdc0714a3b3b58cd80ca54e322512f77b63"}
```

### 3. Logout:

**URL**
```bash
localhost:8000/rest_auth/logout/
```

**Method:** ```POST```

**Header**
```bash
'Authorization: Token a4f3ecdc0714a3b3b58cd80ca54e322512f77b63'
```

**Response:** ```200 OK```

```bash
{"detail": "Successfully logged out."}
```

### 4. Request without Authentication Token:

**Response:** ```401 Unauthorized```

```bash
{"detail":"Authentication credentials were not provided."}
```
   
### 4. Request with Invalid Authentication Token:

**Response:** ```401 Unauthorized```

```bash
{"detail":"Invalid token."}
```

## API Status

To check the API status just send a **GET** request to ```localhost:8000/api/```.
Response: ```200 OK```
```bash
{
    "message": "Welcome to the Ecommerce Catalog API!"
}
```
    
## Catalog Endpoints

### Categorias:

* Get All: 

    URL: ```localhost:8000/api/v1/categorias/```
    
    Method: ```GET```

    Response: ```200 OK```
    ```bash
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "nome": "Nome Categoria"
            }
        ]
    }
    ```

* Get By Id: 
    
    URL: ```localhost:8000/api/v1/categorias/<categoria_id>/```
    
    Method: ```GET```
    
    Response: ```200 OK```
    ```bash
    {
        "id": 1,
        "nome": "Nome Categoria"
    }
    ```


* Create: 

    URL: ```POST localhost:8000/api/v1/categorias/```
    
    Method: ```PUT```

    Body:
    ```bash
    {
        "nome": "Nome Categoria"
    }  
    ```
  
    Response: ```201 Created```
    ```bash
    {
        "id": 1,
        "nome": "Nome Categoria"
    }
    ```

* Update 

    URL: ```localhost:8000/api/v1/categorias/<categoria_id>/```
    
    Method: ```PUT```

    Body:
    ```bash
    {
        "nome": "Nome Categoria Update"
    }  
    ```
    Response: ```200 OK```
    ```bash
    {
        "id": 1,
        "nome": "Nome Categoria Update"
    }
    ```

* Delete: 

    URL: ```localhost:8000/api/v1/categorias/<categoria_id>/```
    
    Method: ```DELETE```
    
    Response: ```204 No Content```
    
* Filter by nome: 

    URL: ```localhost:8000/api/v1/categorias/nome__contains=<nome categoria>```
    
    Method: ```GET```

    Response: ```200 OK```
    ```bash
    {
        "count": 1,
        "next": "localhost:8000/api/v1/categorias/?limit=10&nome__contains=<nome categoria>&offset=10",
        "previous": null,
        "results": [
            {
                "id": 1,
                "nome": "Nome Categoria"
            }
        ]
    }
    ```

### Produtos:

* Get All: 

    URL: ```localhost:8000/api/v1/produtos/```
    
    Method: ```GET```

    Response: ```200 OK```
    ```bash
    {
        "count": 1,
        "next": "localhost:8000/api/v1/produtos/?limit=10&offset=10",
        "previous": null,
        "results": [
            {
                "id": 1,
                "nome": "Nome Produto",
                "descricao": "Descrição Produto",
                "preco": "180.00",
                "categoria": 1,
                "imagem": '<image_url>'
            }
        ]
    }
    ```

* Get By Id: 
    
    URL: ```localhost:8000/api/v1/produtos/<produto_id>/```
    
    Method: ```GET```
    
    Response: ```200 OK```
    ```bash
    {
        "id": 1,
        "nome": "Nome Produto",
        "descricao": "Descrição Produto",
        "preco": "180.00",
        "categoria": 1,
        "imagem": '<image_url>'
    }
    ```


* Create: 

    URL: ```POST localhost:8000/api/v1/produtos/```
    
    Method: ```PUT```

    Body:
    ```bash
    {
        "nome": "Nome Produto",
        "descricao": "Descrição Produto",
        "preco": "180.00",
        "categoria": 1
    } 
    ```
  
    Response: ```201 Created```
    ```bash
    {
        "id": 1,
        "nome": "Nome Produto",
        "descricao": "Descrição Produto",
        "preco": "180.00",
        "categoria": 1,
        "imagem": '<image_url>'
    }
    ```

* Update 

    URL: ```localhost:8000/api/v1/produtos/<produto_id>/```
    
    Method: ```PUT```

    Body:
    ```bash
    {
        "nome": "Nome Produto Update",
        "descricao": "Descrição Produto Update",
        "preco": "180.00",
        "categoria": 1
    }  
    ```
    Response: ```200 OK```
    ```bash
    {
        "id": 1,
        "nome": "Nome Produto Update",
        "descricao": "Descrição Produto Update",
        "preco": "180.00",
        "categoria": 1,
        "imagem": '<image_url>'
    }
    ```

* Delete: 

    URL: ```localhost:8000/api/v1/produtos/<produto_id>/```
    
    Method: ```DELETE```
    
    Response: ```204 No Content```

* Filter by nome: 

    URL: ```localhost:8000/api/v1/produtos/nome__contains=<nome produto>```
    
    Method: ```GET```

    Response: ```200 OK```
    ```bash
    {
        "count": 1,
        "next": "localhost:8000/api/v1/produtos/?limit=10&nome__contains=<nome produto>&offset=10",
        "previous": null,
        "results": [
            {
                "id": 1,
                "nome": "Nome Produto",
                "descricao": "Descrição Produto",
                "preco": "180.00",
                "categoria": 1,
                "imagem": '<image_url>'
            }
        ]
    }
    ```

* Filter by descricao: 

    URL: ```localhost:8000/api/v1/produtos/descricao__contains=<nome produto>```
    
    Method: ```GET```

    Response: ```200 OK```
    ```bash
    {
        "count": 1,
        "next": "localhost:8000/api/v1/produtos/?limit=10&descricao__contains=<nome produto>&offset=10",
        "previous": null,
        "results": [
            {
                "id": 1,
                "nome": "Nome Produto",
                "descricao": "Descrição Produto",
                "preco": "180.00",
                "categoria": 1,
                "imagem": '<image_url>'
            }
        ]
    }
    ```
  
### Pagination:
The default pagination page size is 10. However you can set the **page size** sending the **limit** as an **query params**

* Examples:
    
    URL: ```localhost:8000/api/v1/categorias/?limit=2```
    
    URL: ```localhost:8000/api/v1/produtos/?limit=2```