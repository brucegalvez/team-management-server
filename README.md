# RESTfull service for a Team Management App
RESTfull service built with Python, Flask, and Mongoose for managing student teams of Pachaqtec Coding School. Built as part of the final project of the backend specialization program from the same school.

## Service Endpoints

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
- Refer to postman file for the full documentation

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
- Rodrigo Bruce Galvez (team leader)
- Javier Cárdenas
