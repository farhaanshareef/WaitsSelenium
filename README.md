# Understanding the Waits in Selenium
This repository provides explanations of the three different types of waits in Selenium with Python: explicit wait, implicit wait, and fluent wait.

# Types of Waits
# Explicit Wait
Explicit wait allows you to wait for a certain condition to occur before proceeding with the execution of your code. It provides a more precise control over waiting times and conditions compared to implicit wait. With explicit wait, you can wait for specific elements to be present, visible, clickable, or have specific attributes. This is particularly useful when dealing with dynamic web pages or when waiting for elements to load before interacting with them.

# Implicit Wait
Implicit wait sets a global timeout that will be applied to all subsequent web element searches. It tells the WebDriver to wait for a certain amount of time before throwing a NoSuchElementException if an element is not found immediately. Implicit wait is useful when you have a consistent page loading time across your application and want to avoid adding explicit wait statements for every element interaction.

# Fluent Wait
Fluent wait allows you to define more complex conditions for waiting, such as waiting for an element to be visible for a specific duration or polling an element at regular intervals until a condition is met. It provides a flexible way to handle dynamic elements and perform custom waiting logic.

# Setting Up and Using the Repository
To use the examples and code provided in this repository, follow these steps:

1. Clone the repository to your local machine using the following command:


git clone https://github.com/farhaanshareef/WaitsSelenium.git

2. Install the required dependencies by running the following command: 


pip install -r requirements.txt

3. Run the testcase by running the command  


python run <filename>
  
  
