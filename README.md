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
    {
        "name": "User1",
        "ranks": [
            "name": "rank1",
            "name": "rank2"
        ]
    }
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
{
    {
        "name": "Server1",
        "logging": True
    },
    {
        "name": "Server2",
        "logging": False
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
        "name": "Server1",
    }
}
``` ```
returns
{
    {
        "name": "Server1",
        "logging": True
    }
}, 200
```
**DELETE /servers/{id}**
```
returns "", 200
```
