# Restaurant

## Contents
+ [List Restaurant](#list-restaurant)
+ [Retrive Restaurant](#retrive-restaurant)
+ [Delete Restaurant](#delete-restaurant)
+ [Create Restaurant](#create-restaurant)
+ [Update Restaurant](#update-restaurant)
+ [Statistics Restaurant](#statistics-restaurant)

## List Restaurant
    Retrive all Restaurant objects
#### - URL:
    GET: url/restaurant/
#### - Success response:
```json
{
    "count": 101,
    "next": "https://pure-temple-31104.herokuapp.com/restaurant/?page=2",
    "previous": null,
    "results": [
        {
            "id": "851f799f-0852-439e-b9b2-df92c43e7672",
            "rating": 1,
            "name": "Barajas, Bahena and Kano",
            "site": "https://federico.com",
            "email": "Anita_Mata71@hotmail.com",
            "phone": "534 814 204",
            "street": "82247 Mariano Entrada",
            "city": "Mérida Alfredotown",
            "state": "Durango",
            "lat": 19.4400570537131,
            "lng": -99.1270470974249
        },
        {
            "id": "4e17896d-a26f-44ae-a8a4-5fbd5cde79b0",
            "rating": 0,
            "name": "Hernández - Lira",
            "site": "http://graciela.com.mx",
            "email": "Brandon_Vigil@hotmail.com",
            "phone": "570 746 998",
            "street": "93725 Erick Arroyo",
            "city": "Mateofurt",
            "state": "Hidalgo",
            "lat": 19.437904276995,
            "lng": -99.1286576775023
        },
        {
            "id": "c0ffd058-e773-47f1-974b-42d41cb555bf",
            "rating": 3,
            "name": "Rendón - Elizondo",
            "site": "https://cristina.mx",
            "email": "Hugo.Casanova49@gmail.com",
            "phone": "5866-337-812",
            "street": "5518 Monserrat Explanada",
            "city": "Chignahuapan María",
            "state": "Sinaloa",
            "lat": 19.4360705910348,
            "lng": -99.1297865731994
        }, ...
        
    ]
}
```
 #### -Status Codes:
      - 200 is successful


## Retrive Restaurant
    Retrive one Restaurant object by ID
#### - URL:
    GET: url/restaurant/<ID_Restaurant>/
#### - Success response:
```json
{
    "id": "851f799f-0852-439e-b9b2-df92c43e7672",
    "rating": 1,
    "name": "Barajas, Bahena and Kano",
    "site": "https://federico.com",
    "email": "Anita_Mata71@hotmail.com",
    "phone": "534 814 204",
    "street": "82247 Mariano Entrada",
    "city": "Mérida Alfredotown",
    "state": "Durango",
    "lat": 19.4400570537131,
    "lng": -99.1270470974249
}
```

#### - Error response:
```json
{
    "detail": "Not found."
}
```

#### - Status Codes: 
    - 200 is successful 
    - 404 not found

## Delete Restaurant
    Delete one Restaurant object by ID
#### - URL:
    DELETE: url/restaurant/<ID_Restaurant>/
#### - Success response:
```json
    Empty
```

#### - Error response:
```json
{
    "detail": "Not found."
}
```

### Status Codes: 
    - 204 no content 
    - 404 not found

## Create Restaurant
    Create one Restaurant object
#### - URL:
    POST: url/restaurant/
    
#### - Request:
```json
{
    "id": "851f799f-0852-439e-b9b2-df92c43e5978",
    "rating": 5,
    "name": "Nuevo 2",
    "site": "https://test.com",
    "email": "q@q.com",
    "phone": "444 333 111",
    "street": "Av. blabla",
    "city": "own",
    "state": "No se",
    "lat": 19.4400570537555,
    "lng": -99.1270470974555
}
```
    
#### - Success response:
```json
{
    "id": "851f799f-0852-439e-b9b2-df92c43e5978",
    "rating": 5,
    "name": "Nuevo 2",
    "site": "https://test.com",
    "email": "q@q.com",
    "phone": "444 333 111",
    "street": "Av. blabla",
    "city": "own",
    "state": "No se",
    "lat": 19.4400570537555,
    "lng": -99.1270470974555
}
```

#### - Error response:
```json
{
    <Parameter>: [<Validation rule>]
}
```

#### - Validations
    - Id: unique
    - email: correct email form
    - site: correct URL form
    - rating: must be interger
    - lat: must be float
    - ing: must be float

#### - Status Codes: 
    - 200 is successful 
    - 400 bad request
    
## Update Restaurant
    Edit one Restaurant object by Id
#### - URL:
    POST: url/restaurant/<ID_Restaurant>
    
#### - Request:
```json
{
    "rating": 5,
    "name": "Nuevo 2",
    "site": "https://test.com",
    "email": "q@q.com",
    "phone": "444 333 111",
    "street": "Av. blabla",
    "city": "own",
    "state": "No se",
    "lat": 19.4400570537555,
    "lng": -99.1270470974555
}
```
>Note: the parameters could be one, all, or any combination 
    
#### - Success response:
```json
{
    "id": "851f799f-0852-439e-b9b2-df92c43e5978",
    "rating": 2,
    "name": "Nuevo 2.5",
    "site": "https://test.com",
    "email": "q@q.com",
    "phone": "444 333 111",
    "street": "Av. blabla",
    "city": "CDMX",
    "state": "No se",
    "lat": 19.4400570537555,
    "lng": -99.1270470974555
}
```

#### - Error response:
```json
{
    <Parameter>: [<Validation rule>]
}
```

#### OR

```json
{
    "detail": "Not found."
}
```


#### - Validations
    - email: correct email form
    - site: correct URL form
    - rating: must be interger
    - lat: must be float
    - ing: must be float

#### - Status Codes: 
    - 200 is successful
    - 400 bad request
    - 404 not found

## Statistics Restaurant
    Obtain statistics of restaurants by a geographical circle area
#### - URL:
    POST: url/restaurant/statistics?<Parameters>
    
#### -Parameters
    - latitude (float): obligatory field
    - longitude (float): obligatory field
    - radius (float): obligatory field

#### - Success response:
```json
{
    "count": 21,
    "avg": 1.47619,
    "std": 1.56905
}
```

#### - Error response:
```json
{
    <Parameter>: [<Validation rule>]
}
```

#### OR

```json
{
    "detail": "Not found."
}
```
#### - Validations
    - latitude: must be float, is required
    - longitude: must be float, is required
    - radius: must be float, is required

#### - Status Codes: 
    - 200 is successful
    - 400 bad request

