Flight Management REST API (Django)

A simple Django REST Framework project for managing flights — includes CRUD operations and file upload.

Features

Create, view, update, delete flights

File upload endpoint

JSON-based REST API using DRF

JWT authentication (optional)

Tech Stack

Backend: Django + DRF

Database: SQLite / PostgreSQL

Auth: JWT (djangorestframework-simplejwt)

Setup
git clone <repo-url>
cd customapi
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

API Endpoints
Method	Endpoint	Description
GET	/api/flights/	List flights
POST	/api/flights/	Add flight
PUT	/api/flights/	Update flight
DELETE	/api/flights/<id>/	Delete flight
POST	/api/savefile/	Upload file
Example
curl -X POST http://127.0.0.1:8000/api/flights/ \
 -H "Content-Type: application/json" \
 -d '{"flight_name":"AirIndia","starting_from":"BOM","destination":"DEL"}'

Run Tests
python manage.py test

License

MIT © 2025
