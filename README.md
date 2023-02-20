# Profiles REST API
REST API providing basic functionality for managing user profiles.

## Development Tools:
* Python
* Django framework
* Django REST framework
* Vagrant
* VirtualBox

## Functionality:
* Create new profile
* List existing profiles
* Search for a profile by name or email
* Update **your** profile
  - Update name / email
  - Change password
* Delete **your** profile

## URLs and HTTP Methods:
* /api/profiles/
  - `GET` : List all profiles
  - `POST` : Create profile
* /api/profiles/<profile_id>/
  - `GET` : Get details of this profile
  - `PUT` / `PATCH` : Update this profile
  - `DELETE` : Delete this profile
* /api/login