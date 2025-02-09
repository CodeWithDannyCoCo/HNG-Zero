# HNGx Stage Zero Task

This is a simple REST API built with Django that returns specific information in JSON format. The API is part of the HNGx internship program Stage Zero task.

## Description

This API provides a single endpoint that returns:

- The developer's email address
- Current UTC datetime in ISO 8601 format
- GitHub repository URL

## API Documentation

### Endpoint

- URL: `/api/`
- Method: `GET`
- No authentication required

### Response Format

```json
{
  "email": "simplytobs@gmail.com",
  "current_datetime": "2025-02-09T15:00:49.388802+00:00Z",
  "github_url": "https://github.com/CodeWithDannyCoCo/HNG-Zero.git"
}
```

### Status Codes

- 200: Successful request
- 404: Endpoint not found
- 500: Server error

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/CodeWithDannyCoCo/HNG-Zero.git
   cd HNG-Zero
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://localhost:8000/api/`

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `./build.sh`
   - Start Command: `gunicorn zero.wsgi:application`
4. Add the following environment variables:
   - `DEBUG`: false
   - `SECRET_KEY`: [your-secret-key]

## Technologies Used

- Python
- Django
- Django CORS Headers
- Gunicorn (Production Server)
- Whitenoise (Static Files)

## Related Resources

- [HNG Python Developers](https://hng.tech/hire/python-developers)

## Live Demo

The API is deployed at: [Your Render URL]
