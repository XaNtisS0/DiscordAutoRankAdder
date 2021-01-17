### DiscordAutoRankAdder

***To Do***
- request adding to server
- admin approval of adding
- user authentication
- log in via discord

***Users***

**Get /{server}/users**
```
GET /wrsftims/users
``````
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
**GET /{server}/users/{id}**
```
GET /wrsftims/users/1
``````
returns
{
    {
        "id": 1
        "name": "Karol Wojtyła",
        "rank": "Sekcja duchowna"
    }
} , 200
```
**POST /{server}/users**
```
POST /wrsftims/users
{
    {
        "name": "Roman Dmowski",
        "rank": "Sekcja IT"
    }
}
``````
returns "", 201
```
**PATCH /{server}/users/{id}**
```
PATCH /wrsftims/users/1
{
    {
        "name": "Karol Wojtyła",
        "rank": "GMD"
    }
}
``````
returns
{
    {
        "name": "Karol Wojtyła",
        "rank": "Sekcja Księżąt ;P"
    }
}, 200
```
**DELETE /{server}/users/{id}**
```
DELETE /wrsftims/users/1``````d
returns "", 200
```

***Servers***

**Get /servers**
```
GET /servers
``````
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

**POST   /servers**
```
POST /servers
``````
returns
"", 200
```

**PATCH   /servers/{id}**
```
PATCH /servers/1
{
    {
        "name": "Karol Wojtyła",
    }
}
``````
returns
{
    {
        "name": "Karol Wojtyła",
    }
}, 200
```
**DELETE   /servers/{id}**
```
DELETE /servers/1``````d
returns "", 200
```