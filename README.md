# FastAPI CRUD API
## Description

This is a REST API built with FastAPI that performs CRUD operations for items.
The project demonstrates basic API development with FastAPI, Pydantic, and Uvicorn.
It includes automatic Swagger documentation and supports creating, reading, updating, and deleting items.

## Installation

Clone the repository

Move into the project

cd fastapi-crud-api

Create a virtual environment

python -m venv venv

Activate it

Linux/macOS

source venv/bin/activate

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

## Run

uvicorn main:app --reload

The API will be available at

http://127.0.0.1:8000

Swagger UI

http://127.0.0.1:8000/docs

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| GET    | /           | Welcome message |
| GET    | /items      | Get all items   |
| GET    | /items/{id} | Get one item    |
| POST   | /items      | Create item     |
| PUT    | /items/{id} | Update item     |
| DELETE | /items/{id} | Delete item     |

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ba6c7d51-14b7-4edd-b7ea-f68d43f75863" />

<img width="1920" height="1080" alt="Screenshot_20260715_144908" src="https://github.com/user-attachments/assets/2112b816-23d7-41ea-9076-9c1a11affd2c" />
<img width="1920" height="1080" alt="Screenshot_20260715_144852" src="https://github.com/user-attachments/assets/ba49ea04-b72e-4121-b02d-66954ee277ba" />
<img width="1920" height="1080" alt="Screenshot_20260715_144822" src="https://github.com/user-attachments/assets/78e4500a-dfe9-46e8-a4e4-dfd38f694d56" />
<img width="1920" height="1080" alt="Screenshot_20260715_145225" src="https://github.com/user-attachments/assets/fedb0699-8543-45d1-8999-e2811dd9d26c" />
<img width="1920" height="1080" alt="Screenshot_20260715_145146" src="https://github.com/user-attachments/assets/809a41bc-7b24-4c8c-b44a-2fb851f726ce" />
<img width="1920" height="1080" alt="Screenshot_20260715_145125" src="https://github.com/user-attachments/assets/c073f02f-19b7-4bf0-998d-fb521f1ac99d" />
<img width="1920" height="1080" alt="Screenshot_20260715_145114" src="https://github.com/user-attachments/assets/2b1a692a-0c94-4981-ad83-2c90fc0964e6" />
<img width="1920" height="1080" alt="Screenshot_20260715_145029" src="https://github.com/user-attachments/assets/c4182ca2-abe4-4634-b4b6-235f077d5dcf" />

