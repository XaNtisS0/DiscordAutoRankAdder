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
***PATH   /{server}/users/{id}***
```css
PATH /wrsftims/users/1
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
        "picture": "{url}",
        "users": [
            
        ]
    },
    {
        "name": "Seria Turniejów WRS WFTIMS 2",
        "picture": "{url}"
    }
}, 200
```

***POST   /servers***
```css
POST /servers
``````d
returns
"", 200
```