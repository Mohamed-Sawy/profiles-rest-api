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
* login
  * Update your profile
    - name - email - password
  * Delete your profile
  * View the **feed items** (**statuses**)
  * Create new feed item
  * Update feed item
  * Delete feed item

## URLs and HTTP Methods:
* /api/profiles/
  - `GET` : List all profiles
  - `POST` : Create profile
  - `/?search=<name_or_email>` : List all profiles that matches the string provided
* /api/profiles/<profile_id>/
  - `GET` : Get details of this profile
  - `PUT` / `PATCH` : Update this profile **_if authorized_**
  - `DELETE` : Delete this profile **_if authorized_**
* /api/login
  - `POST` : Get authentication token
* /api/feed/
  - `GET` : List all feed items **_if authenticated_**
  - `POST` : Create feed item **_if authenticated_**
* /api/feed/<feed_item_id>/
  - `GET` : Get details of this feed item **_if authenticated_**
  - `PUT` / `PATCH` : Update this feed item **_if authorized_**
  - `DELETE` : Delete this feed item **_if authorized_**