# DiscordAutoRankAdder

***To Do***
- request adding to server
- admin approval of adding
- user authentication
- log in via discord


##  Users


**Get /{server}/users**
```
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
        "rank": ["Sekcja duchowna"
    }
} , 200
```
**GET /{server}/users/{id}**
```
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
{
    {
        "name": "Roman Dmowski",
        "rank": "Sekcja IT"
    }
}
``` ```
returns "", 201
```
**PATCH /{server}/users/{id}**
```
{
    {
        "name": "Karol Wojtyła",
        "rank": "GMD"
    }
}
``` ```
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
returns "", 200
```


## Servers


**Get /servers**
```
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

**POST /servers**
```
returns
"", 200
```

**PATCH /servers/{id}**
```
{
    {
        "name": "Karol Wojtyła",
    }
}
``` ```
returns
{
    {
        "name": "Karol Wojtyła",
    }
}, 200
```
**DELETE /servers/{id}**
```
returns "", 200
```
