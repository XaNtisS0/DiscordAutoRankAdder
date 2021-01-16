**Users**

***Get   /{server}/users***
```css
GET /wrsftims/users
``````d
returns
{
    {
        "id": 0
        "name": "Roman Dmowski",
        "rank": "Sekcja IT"
    },
    {
        "id": 1
        "name": "Karol Wojtyła",
        "rank": "Sekcja duchowna"
    }
} , 200
```
***GET   /{server}/users/{id}***
```css
GET /wrsftims/users/1
``````d
returns
{
    {
        "id": 1
        "name": "Karol Wojtyła",
        "rank": "Sekcja duchowna"
    }
} , 200
```
***POST   /{server}/users***
```css
POST /wrsftims/users
{
    {
        "name": "Roman Dmowski",
        "rank": "Sekcja IT"
    }
}
``````d
returns "", 201
```
***PUT   /{server}/users/{id}***
```css
PUT /wrsftims/users/1
{
    {
        "name": "Karol Wojtyła",
        "rank": "GMD"
    }
}
``````d
returns
{
    {
        "name": "Karol Wojtyła",
        "rank": "Sekcja Księżąt ;P"
    }
}, 200
```
***DELETE   /{server}/users/{id}***
```css
DELETE /wrsftims/users/1``````d
returns "", 200
```

**Servers**

***Get   /servers***
```css
GET /servers
``````d
returns
{
    {
        "name": "WRS ftims",
        "picture": "{url}"
    },
    {
        "name": "Seria Turniejów WRS WFTIMS 2",
        "picture": "{url}"
    }
}, 200
```