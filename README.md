# Backend-Team-Management-App
REST API made in Python for managing the teams of students of Pachaqtec Coding School, made as part of the final project for the specialization program in Backend 2019-2020 of the same school.

## Resources

### Home - Sign up and login
```http
POST /home/login
POST /home/signup
```

### Dashboard - Get all friends, one friend and edit my account
```http
GET /dashboard/friends
POST /dashboard/friends/{username}
PUT /dashboard/{username}/profile
PUT /dashboard/{username}/profile/tags
```

### Chat - Gets all conversations and one conversation
```http
GET /chat
PUT /chat/{username}
```

## Standards & full documentation
- Follows PEP8.
- Refer to postman file for full documentation

## Responses
Returns a JSON response in the following format:

```python
{
  "message" : string,
  "success" : bool,
  "content" : dict
}
```

## Status Codes
Returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

## Credits:
- Rodrigo Bruce Galvez (leader)
- Javier Cárdenas
