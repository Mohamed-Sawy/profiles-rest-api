# Profiles REST API
REST API providing basic functionality for manging user profiles.

## Functionality:
* Create new profile
  - Validate profile data
* List existing users
* Search for user
* Updating a profile
  - Update name / email
  - Change password
* Delete a profile

## URLs and HTTP Methods:
* /api/profiles/
  - `GET` : List all profiles
  - `POST` : Create profile
* /api/profiles/<profile_id>/
  - `GET` : Get details of this profile
  - `PUT` / `PATCH` : Update this profile
  - `DELETE` : Delete this profile