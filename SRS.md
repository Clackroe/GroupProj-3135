# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Xander Cole](mailto:acole67@uncc.edu)
* [Walter Nguyen](mmailto:wnguyen4@uncc.edu)
* [Jacob Smith](mmailto:jsmit702@uncc.edu)
* [Nate Mirman](mmailto:nmirman@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.01 | 03/22/23 | Introduction | [Walter Nguyen](mmailto:wnguyen4@uncc.edu) | [Walter Nguyen](mmailto:wnguyen4@uncc.edu)
| 1.02 | 03/30/23 | Initial Content | Everyone | Everyone
| 1.03 | 04/06/23 | Updated Use Case | [Xander Cole](mailto:acole67@uncc.edu)| [Xander Cole](mailto:acole67@uncc.edu)

## Table of Contents

- [Software Requirements Specification Document](#software-requirements-specification-document)
  - [Group Members](#group-members)
  - [Revisions](#revisions)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Constraints](#constraints)
  - [Use Cases](#use-cases)
  - [User Stories](#user-stories)
  - [Glossary](#glossary)

## Introduction

Our software aims to be a website for a car dealership with two primary users, employees and customers, enabling cusutomers to have quick access to vehicle information and employees the ability to add new inventory or edit exsisting inventory. Employees/Admin users will have the ability to edit information about vehicles for sale and add new vehicles. Customers will be able to view all information, and contact the dealership for more information or to learn about purchase options.

## Requirements

* **ID:** REQ-1
  * **Description:** The system should be able to present information on a vehichle based on the image selected by the user.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** The primary purpose of the website is to advertise and atract buyers which requires the ability to select a vehichle and gain more information prior to the purchase.
  * **Testing:** We will use visual representation via SQL and test methods to check for any possible liablities.

* **ID:** REQ-2
  * **Description:** This feature will allow to user to enter different forms of contact information and store in a database for later  use by the car salesman.
  * **Type:** Non-Functional.
  * **Priority:** 3
  * **Rationale:** This feature is valued because it grants the customer the ability to speak with a salesperson one-on-one via cell phone or email.
  * **Testing:** We will develope false identities which include name, cell phone, and email to insert into our feature and see if the data is being stored properly via SQL.

* **ID:** REQ-3
  * **Description:** The system will allow and employee of the dealership to login via given credential, to add, remove, and change vehichle details.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** The ability to change vehichle information is vital to functionality of our systems as new cars will be coming and going and mileage on cars will change after test drives.
  * **Testing:** Test cases will be developed to ensure methods sending data to and from our data base, will be stored properly. 
## Constraints
* ### Development
  * Adequate comments must be written when not clearly understandable at first glancce.
  * Backend must be built using Flask & Python
  * Frontend must use a combination of HTML and CSS
* ### Developer Flow
  * Developers will make all functionality changes, updates, and additions in personal and seperate branches.
  * When a given change or feature is complete, one user will be assigned to merge and handle all conflicts.
* ### Planning
  * All features will be planned out via the [trello](https://trello.com/b/ybAmRdom/project)
  * All features and changes must be functionally complete **1-2 DAYS** before the subbmission is due on Canvas.
* ### Merging
  * Merging into main will be carried out on the [GitHub](https://github.com/Clackroe/School2022Spring) via a pull request.
  * Merging into main requires at least **1 ADDITIONAL** person to approve and review the pull request.
* ## Communication
  * Communication will be carried out via email, or discord.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

* **Use Case 1((User)Login as User):**
  * **Description:** Someone with an account will be able to login to the website in order to make a valid purchase.
  * **Actors:** Someone that is wishing to go through the website and is already a valid user.
  * **Preconditions:** The person must already have an account created through the website with their login details.
  * **Postconditions:** The user should be able to successfully sign in through the site and be able to access all of the website's functions.

* **Use Case 2((User and Admin)Purchase a Car):**
  * **Description:** Someone with an account should be able to purchase a car through the website.
  * **Actors:** A customer wishing to purchase a car through the website and has made an account.
  * **Preconditions:** Customer should already have an account, payment and insurance details, a car selected for purchasing, and the location for where they want to pick up their car.
  * **Postconditions:** An order is processed and the user should be expecting the car while the website should be expecting payment information on their end.

* **Use Case 3((User and Admin)Selling a Car):**
  * **Description:** Anyone with an account should be able to sell the car.
  * **Actors:** A person with an account whether that would be the average consumer or employee.
  * **Preconditions:** Someone should have an account, a car to sell, where the car is locally, the car details, and 
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

* **Use Case 4((Admin)Login as employee):**
  * **Description:** Any one working for this website should be able to sign in the website as an employee
  * **Actors:** Someone that is working in the company already should be able to login as an employee
  * **Preconditions:** Employee should already have an account made and ready to go through with their creditentials.
  * **Postconditions:** Employee should be able to access the website and have full management for the website.

* **Use Case 5((User and Admin)Create account):**
  * **Description:** Someone should be able to create an account from the website that keeps track of basic user data such as purchase and sale history, keep a record of what cars they have, interact with other users, and be able to get notified about any additional information.
  * **Actors:** A everyone that is the consumer and the employees should be able to create an account.
  * **Preconditions:** Valid Email account in order to register into the system
  * **Postconditions:** Consumer will result in having their account created.
  * **Postconditions:** Admins and employees will be able to create new admin accounts via an encrypted key

* **Use Case 6((User)Compare Car Specs):**
  * **Description:** A user should be able to take 2 cars on the website and compare specifications with each other. This also includes comparing features, what type of car it is, mileage(if used), etc.
  * **Actors:** Someone that is wishing to purchase a car or wants to compare cars. They do not need an account to do this.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

* **Use Case 7((User and Admin)See Purchase History):**
  * **Description:** A user should be able to see what cars they have purchased in the past, where they got it from, price, purchase date, warranty information, brand, and other additional information if needed.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format: 

//Example : "As a "person", I "want to", "so that" xyz."

* **US-1:** // Format for labeling user stories
  * **Customer** // Type of user
  * **Description: As a customer, I want to be able to view information about vehciles such as Year, Make, and Model, Mileage, Price, Color, and other items, so that I can make an informed decision when exploring vehicle options. ** // Description
* **US-2:** // Format for labeling user stories
  * **Employee/Admin** // Type of user
  * **Description: As a employee, I want to be able to add new vehicles to our inventory to be displayed on our webpage, so that customers can see the most recent/new vehicles in stock. ** // Description

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** The term that is being defined. This should be a single word or phrase that is being defined.
  * **Definition:** A definition of the term. This should be a short description of the term that is being defined. This should be a single sentence that describes the term.
