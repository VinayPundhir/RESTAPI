# FastAPI Project

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

This is a FastAPI project that provides a REST API for managing user information and skills.

![Screenshot from 2023-07-03 13-44-16](https://github.com/VinayPundhir/RESTAPI/assets/51248042/c46891b8-0356-4351-a650-73c4b0c54d00)




## Models

The following models are used in this project:

- `User`: Represents a user with attributes `id`, `name`, `age`, `email`, `password`, and a relationship to `Skill` entities.

- `Skill`: Represents a skill with attributes `id`, `name`, and a relationship to `User` entities.

## Endpoints

### Authentication

- **POST /login**: Endpoint to authenticate a user and generate an access token.

### Skills

- **POST /create_skill**: Endpoint to create a new skill.

- **GET /skill_info_by_name/{name}**: Endpoint to retrieve skill information by name.

### Users

- **GET /user_info/{id}**: Endpoint to retrieve user information by ID.

- **DELETE /delete_usr/{id}**: Endpoint to delete user information by ID.

- **PUT /update/{id}**: Endpoint to update user information by ID.

- **GET /all_usrs**: Endpoint to retrieve information of all users.

- **POST /create_usr**: Endpoint to create a new user.

### Default

- **GET /**: Index endpoint to welcome users.

## Getting Started

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Running the Project
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload

