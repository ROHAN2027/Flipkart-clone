# Django Web Application

This is a Django-based web application that includes user authentication, profile management, and a contact form. The project is structured with two main app : `info` and `profileapp`.


## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Features

### User Authentication

- Users can sign up, log in, and log out.
- Email verification is required for account activation.

### Profile Management

- Users can update their profile information including name, bio, profile picture, date of birth, country, pincode, and address.
- Profile pictures are stored in the `media/profile_pics` directory.

### Contact Form

- Users can submit their name, email, and a message through the contact form.
- Submitted data is saved to the database and a success message is displayed.

## Apps

### [info](http://_vscodecontentref_/19)

- Manages the contact form and related views.
- Models: [info](http://_vscodecontentref_/20)
- Forms: [InfoForm](http://_vscodecontentref_/21)
- Views: [contact_view](http://_vscodecontentref_/22)

### [profileapp](http://_vscodecontentref_/23)

- Manages user profiles.
- Models: [profile](http://_vscodecontentref_/24)
- Forms: [ProfileForm](http://_vscodecontentref_/25)
- Views: [profile](http://_vscodecontentref_/26)

## Static Files

- CSS and JavaScript files are located in the [static](http://_vscodecontentref_/27) directory.
- Templates are located in the [templates](http://_vscodecontentref_/28) directory.

## Configuration

- The project settings are configured in [settings.py](http://_vscodecontentref_/29).
- Email settings for account verification are also configured in [settings.py](http://_vscodecontentref_/30).

## Running Tests

- To run tests, use the following command:
    ```sh
    python manage.py test
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
