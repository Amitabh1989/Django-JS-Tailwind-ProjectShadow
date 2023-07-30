# Project Shadow

ProjectShadow is a custom website built using Django, Django Rest Framework (DRF), and Chart.js to generate custom JSON data. It provides a user-friendly interface for creating and managing test cases, while also offering powerful features for data visualization.

## Features

- **User Authentication with JWT**: ProjectShadow includes user registration, login, and password reset functionality using Django JSON Web Token (JWT) authentication. Users can securely create accounts, authenticate themselves, and reset their passwords if needed.

- **Django Rest Framework (DRF) APIs**: The project leverages DRF to create robust and scalable APIs that handle various operations, including user management, test case creation, and data retrieval. These APIs provide a seamless integration of frontend and backend components.

- **Test Case Creation**: Users can create test cases by selecting modules and submitting test steps. Each module represents a feature, and users can easily toggle values and submit steps using Django forms. The application ensures a smooth and intuitive experience for creating comprehensive test cases.

- **Cart Functionality**: ProjectShadow offers a cart feature that allows users to add test steps to a cart using JavaScript and Ajax. The cart enables users to gather multiple test steps before creating a test case. This dynamic interaction is facilitated by jQuery, ensuring a responsive and efficient workflow.

- **Data Visualization with Chart.js**: The project utilizes Chart.js, a powerful JavaScript library, for visualizing data. It enables users to generate custom JSON data and display it in various chart types, such as line charts, bar charts, and pie charts. Chart.js provides an interactive and visually appealing way to analyze and present data.

## Technologies Used

- Django: A Python web framework that provides a robust foundation for building web applications.

- Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs in Django.

- Chart.js: A JavaScript library for data visualization that allows the creation of dynamic and interactive charts.

- Django JSON Web Token (JWT): A secure authentication mechanism for Django applications.

- SQLite: A lightweight and reliable database management system used as the default database backend in Django.

- Tailwind CSS: A utility-first CSS framework for creating responsive and modern user interfaces.

- JavaScript: The programming language used to enhance interactivity and handle dynamic functionality.

- Ajax: A set of web development techniques that enable asynchronous communication between the client and server.

- jQuery: A JavaScript library that simplifies HTML document traversal, event handling, and AJAX interactions.

- React: A JavaScript library used to design responsive and reusable UI components.

- Docker: A containerization platform that provides an isolated and consistent environment for running applications.

## Installation and Usage

To run the ProjectShadow application locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/Amitabh1989/ProjectShadow.git

2. Install the required dependencies:
   pip install -r requirements.txt

3. Set up the database:
   python manage.py migrate

4. Start the development server:
   python manage.py runserver
  
5. Access the application in your browser at `http://localhost:8000`.

## Contributing

Contributions to ProjectShadow are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

ProjectShadow is licensed under the MIT License. You can find more information in the [LICENSE](https://github.com/Amitabh1989/ProjectShadow/blob/main/LICENSE) file.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Chart.js](https://www.chartjs.org/)
- [SQLite](https://www.sqlite.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Ajax](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX)
- [jQuery](https://jquery.com/)
- [React](https://reactjs.org/)
- [Docker](https://www.docker.com/)

## Contact

For any inquiries or questions, feel free to contact the project maintainers at [email protected]

We hope you find ProjectShadow helpful and enjoy using it for your custom JSON data generation and test case management needs!

