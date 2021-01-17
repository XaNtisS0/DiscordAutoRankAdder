# DiscordAutoRankAdder

***To Do***
- request adding to server
- admin approval of adding
- user authentication
- log in via discord
- set some ranks to be automaticly added to users added to the server (front-end)


##  Users


**Get /{server}/users**
```
returns
{
    {
        "id": 0
        "name": "User1",
        "ranks": [
            "name": "rank1",
            "name": "rank2"
        ]
    },
    {
        "id": 1
        "name": "User2",
        "ranks": [
            "name": "rank3",
            "name": "rank1"
        ]
    }
} , 200
```
**GET /{server}/users/{id}**
```
returns
{
   {
        "id": 1,
        "name": "User1",
        "ranks": [
            "name": "rank1",
            "name": "rank2"
        ]
    }
} , 200
```
**POST /{server}/users**
```
{
    "name": "User1",
    "ranks": [
        "rank1",
        "rank2"
    ]
}



returns "", 201
```
**PATCH /{server}/users/{id}**
```
{
    {
        "ranks": [
            "name": "rank3",
            "name": "rank2"
        ]
    }
}



returns
{
    {
        "name": "User1",
        "ranks": [
            "name": "rank3",
            "name": "rank2"
        ]
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
[
    {
        "id": 1,
        "name": "My new server",
        "logging": true
    },
    {
        "id": 2,
        "name": "TestServer2",
        "logging": false
    }
], 200
```

**POST /servers**
```
returns
"", 201
```

**PATCH /servers/{id}**
```
{
    "name": "TestServer1"
}
``` ```
returns
{
    "id": 1,
    "name": "TestServer1",
    "logging": true
}, 200
```
**DELETE /servers/{id}**
```
returns "", 200
```
