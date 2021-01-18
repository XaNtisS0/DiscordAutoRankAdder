# DiscordAutoRankAdder

***To Do***
- request adding to server
- admin approval of adding
- user authentication
- log in via discord
- set some ranks to be automaticly added to users added to the server (front-end)


# Run with Docker Compose

## Users


**Get /{server}/users**
```
returns
[
    {
        "id": 1,
        "server_id": 1,
        "username": "first user",
        "ranks": [
            "rank3",
            "rank2"
        ]
    },
    {
        "id": 2,
        "server_id": 1,
        "username": "second user",
        "ranks": [
            "rank1",
            "rank2"
        ]
    }
] , 200
```

**GET /{server}/users/{id}**
```
returns
[
   {
        "id": 1,
        "name": "User1",
        "ranks": [
            "name": "rank1",
            "name": "rank2"
        ]
    }
] , 200
```

**POST /{server}/users**
```
{
    "username": "first user",
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
    "ranks": [
        "name": "rank3",
        "name": "rank2"
    ]
}



returns
{
    "name": "User1",
    "ranks": [
        "name": "rank3",
        "name": "rank2"
    ]
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
{
    "name": "Test Server 1",
    "logging": false
}



returns
"", 201
```

**PATCH /servers/{id}**
```
{
    "name": "TestServer1"
}



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

**or**
```
{
    "name": "TestServer1"
}



returns "", 200
```