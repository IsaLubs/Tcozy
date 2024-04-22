# Hotelmanagement-tcozy
[Visit the website here](https://hotelmanagement-tcozy-a5d15030424a.herokuapp.com/)

Welcome to our comprehensive Django Hotel Management System! We're thrilled to have you on board. Whether you're a hotel manager, staff member, or developer, this system is designed to streamline your operations and enhance guest experiences.

Welcome to Tcozy Hotel, where comfort meets elegance! Our app invites users to experience the epitome of relaxation and luxury at our boutique hotel. Inspired by our passion for hospitality and fueled by a desire to provide a haven for travelers, Tcozy Hotel offers a seamless booking experience for your perfect getaway.

Run by a team dedicated to ensuring every guest's stay is memorable, Tcozy Hotel was born out of a vision to create a tranquil retreat reminiscent of home. Utilizing Django for the first time, we've crafted a website that strikes the perfect balance between simplicity and functionality. With intuitive navigation, users can effortlessly explore our range of amenities and reserve their ideal accommodations with ease.

Just like the personal touch provided by a family-run business, Tcozy Hotel strives to deliver exceptional service tailored to each guest's needs. Whether you're seeking a peaceful weekend escape or a rejuvenating vacation, our cozy rooms and impeccable hospitality promise an unforgettable stay.

Indulge in the Tcozy Hotel experience and let us be your home away from home. Welcome, and enjoy your stay!

# User Experience (UX)

## For Hotel Staff:

- Efficient Workflow Management
  Hotel staff can navigate through daily tasks effortlessly with our user-friendly interface. From managing bookings to handling room assignments, each step of the workflow is streamlined for maximum efficiency.

- Personalized Guest Service
  Our system empowers staff to provide personalized experiences for guests. With easy access to guest preferences, special requests, and feedback history, staff members can anticipate needs and exceed expectations.
  
- Insightful Analytics
  Hotel managers gain valuable insights into performance metrics, occupancy rates, and revenue trends through comprehensive analytics tools. This data-driven approach enables informed decision-making and strategic planning.

## For Guests

- Seamless Booking Experience
  Guests enjoy a hassle-free booking process with our intuitive reservation system. Whether booking online or through the front desk, the process is quick, secure, and tailored to individual preferences.
  
- Exceptional Service
  From check-in to check-out, guests receive attentive and personalized service from hotel staff. Special requests and preferences are seamlessly integrated into the guest experience, ensuring a memorable stay.
  
- Convenient Access
  Our system offers guests convenient access to essential information and services, such as room availability, amenities, and local attractions. With a user-friendly interface, guests can easily navigate and make the most of their stay.

## Home Page
![Screenshot 2024-04-22 025143](https://github.com/KadDenuwara/HMS/assets/137709290/11954c3b-012f-4147-99da-80a75d6646f1)

## Login Page
![Screenshot 2024-04-22 025541](https://github.com/KadDenuwara/HMS/assets/137709290/19c89446-0944-4080-b265-a08ce8c769d8)

## SignUp Page
![Screenshot 2024-04-22 031459](https://github.com/KadDenuwara/HMS/assets/137709290/788aa311-5bbf-49ee-98de-b0c3a1061487)

## Hotel Details Page
![Screenshot 2024-04-22 025223](https://github.com/KadDenuwara/HMS/assets/137709290/f112604c-9e01-4f61-ad31-4cacabdebeff)

## User Dashboard
![Screenshot 2024-04-22 025339](https://github.com/KadDenuwara/HMS/assets/137709290/818f5701-fd2d-496a-ae1f-f27f1b80535b)

## AboutUs Page
![Screenshot 2024-04-22 025243](https://github.com/KadDenuwara/HMS/assets/137709290/dafa39cd-55b5-4c76-9028-4fc0192e0c59)

## Footer Links & Our Social Media Links
![Screenshot 2024-04-22 031533](https://github.com/KadDenuwara/HMS/assets/137709290/d20999a5-a78a-4667-a83e-01143393933a)

## Admin Panel
![Screenshot 2024-04-22 025402](https://github.com/KadDenuwara/HMS/assets/137709290/cda5922f-453e-4c91-beb5-b3204c89695a)

# Features

## 1. Booking Management
Effortlessly handle room reservations, check-ins, and check-outs with our intuitive booking management system. From single bookings to group reservations, streamline the entire process for maximum efficiency.

## 2. Inventory Control
Maintain full control over your hotel's inventory, including room availability, rates, and special packages. Easily adjust pricing, manage room allocations, and track inventory in real-time.

## 3. Guest Relations
Deliver exceptional guest service with personalized experiences tailored to individual preferences. Access guest profiles, manage special requests, and gather valuable feedback to enhance guest satisfaction.

## 4. Financial Tracking
Stay on top of your hotel's financial health with comprehensive financial tracking tools. Monitor revenue, expenses, and billing transactions to ensure accurate accounting and financial management.

## 5. Admin Dashboard
Access a centralized dashboard with insightful analytics, reports, and administrative tools. Gain valuable insights into occupancy rates, revenue trends, and guest demographics to inform strategic decision-making.

## 6. Customization Options
Tailor the system to your hotel's unique requirements with flexible customization options. From branding and theme customization to configuring user permissions, adapt the system to suit your specific needs.

## 7. Security Measures
Ensure the security of guest data and sensitive information with robust security measures. Implement encryption, access controls, and regular security audits to protect against potential threats.

## 8. Mobile Compatibility
Access key features of the system on the go with mobile compatibility. Whether on a smartphone or tablet, stay connected and manage hotel operations from anywhere, at any time.

# Testing

## Manual Testing:

### Functional Testing
 - Booking Process: Manually test the booking process to ensure that guests can make reservations smoothly, and staff can manage bookings effectively.
 - User Authentication: Verify that user authentication mechanisms, such as login and registration, function correctly and securely.
 - Room Management: Test the functionalities related to room management, including adding, editing, and deleting rooms.
 - Guest Services: Validate that guest services, such as room service requests and housekeeping, are working as expected.
### Usability Testing
 - User Interface: Evaluate the user interface for intuitiveness, clarity, and consistency, ensuring that users can navigate the system with ease.
 - Accessibility: Test the system's accessibility features to ensure compliance with accessibility standards and accommodate users with disabilities.
 - Error Handling: Assess how the system handles errors and edge cases, providing informative error messages and guiding users to resolve issues.

### Compatibility Testing
 - Browser Compatibility: Test the system across different web browsers (e.g., Chrome, Firefox, Safari) to ensure consistent functionality and appearance.
 - Device Compatibility: Validate the system's performance on various devices, including desktops, laptops, tablets, and smartphones, to accommodate users across different platforms.


# Deployment

## Steps taken to deploy on Heroku:

### Set up the workspace:

 - Install gunicorn: Gunicorn is a Python WSGI HTTP Server for UNIX, required for Heroku deployment. Install it in your workspace using pip install gunicorn.
 - Update requirements.txt and create Procfile: Ensure that gunicorn is added to your requirements.txt file. Create a Procfile in the root directory of your project and add the following line: web: gunicorn <hotel_management>.wsgi --log-file -.
 - Set DEBUG to False: In your Django project's settings.py, set DEBUG = False to ensure that your application runs in production mode.
 - Git add, commit and push changes to GitHub: Add any changes you've made, commit them, and push them to your GitHub repository.

### Deploy on Heroku:

 - Create the app on Heroku and connect to GitHub project: Log in to your Heroku account, navigate to the dashboard, and create a new app. Connect your Heroku app to your GitHub repository under the "Deploy" tab.
 - Set Config Vars in the "Settings" Tab: Go to the "Settings" tab of your Heroku app. Under the "Config Vars" section, set any necessary environment variables required for your Django application, such as SECRET_KEY, DATABASE_URL.
 - Deploy the app: Navigate to the "Deploy" tab on your Heroku dashboard. Scroll down to the "Manual deploy" section and click on "Deploy Branch". Heroku will then fetch the latest code from your GitHub repository and start the deployment process.
 - Verify deployment: Once the deployment process is complete, Heroku will provide you with a URL where your application is now live. You can visit this URL to verify that your Django application is running correctly on Heroku.


## Clone Repository

Cloning a repository allows you to create a local copy of it on your machine:

 - Within GitLab, navigate to the repository you want to clone.
 - Look for the "Clone" button, usually located on the right side of the repository page.
 - Click the "Clone" button and copy the HTTPS or SSH URL provided.
 - In your terminal or Git Bash, navigate to the directory where you want to clone the repository.
 - Type 'git clone' followed by the URL you copied from GitLab. For example:
    git clone https://gitlab.com/username/repository.git
 - If you're using SSH, you'd use an SSH URL instead.
 - Press Enter. Git will clone the repository onto your local machine.
 - You may be prompted to enter your GitLab credentials if you haven't authenticated previously.
 - Once the clone process is complete, you'll have a local copy of the repository in the directory you specified.

# Credits

### Code
 - To help me get started with the project and understand the basics, i followed Code Institute and Matt´s Walktrough on "I Think therefore i Blog", big thanks for getting me started.

 - Ed, Ger and Oisin, Tutors at Code Institute helped me solve some bugs in my code, big thanks.

### Bootstrap
 - Bootstrap has an amazing library and has helped me focus on the backend and save a lot of time with style, and layout on the frontend.

### Django
 - The generic views from Django made my life much easier, also great documentation.

### Issues with code
 - Most of the daily problems were solved thanks to Stackoverflow and W3Schools.

### Technologies Used
- [Figma = Wireframes](https://www.figma.com/file/k1vDI4pAx518tG6UAGlqEA/Figma-basics?type=design&node-id=511-10&mode=design&t=IzPyqkX3X6K3nHrF-0)
- Django = Framework
- HTML = mark up language
- CSS = styling
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/download/) = styling
- Python = functionality
- VS Code = IDE
- [Heroku = Deployment](https://dashboard.heroku.com/apps)
- GitHub = Used to store the project
- Git = version control
- [ElephantSQL](https://www.elephantsql.com/)
- [TinyPNG](https://tinypng.com/) used to compress images

# Acknowledgment
We would like to express our gratitude to the following individuals and organizations for their invaluable contributions to the development and success of our Django Hotel Management System:

 - Open Source Community: We are indebted to the vibrant open-source community for their continuous support, inspiration, and contributions to the Django framework and related technologies.
 - Django Developers: Our heartfelt thanks to the developers of Django for creating a powerful, flexible, and scalable web framework that serves as the foundation for our hotel management system.
 - Contributors: A special acknowledgment to all the contributors who have dedicated their time, expertise, and effort to enhance the functionality, usability, and reliability of our system through code contributions, bug reports, and feature suggestions.
 - Beta Testers: We extend our appreciation to the beta testers who volunteered to test early versions of the system, providing valuable feedback and insights that helped us identify and address issues before the official release.
 - Stack Overflow Community: We are grateful to the Stack Overflow community for providing invaluable assistance and solutions to technical challenges encountered during the development process.
 - Documentation Contributors: Our thanks to those who have contributed to the documentation efforts, helping to create clear, comprehensive, and user-friendly guides for installation, usage, and troubleshooting.

We deeply appreciate the collective effort and collaboration that have made our Django Hotel Management System possible. Your support and contributions are truly appreciated!
