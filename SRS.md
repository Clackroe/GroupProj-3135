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

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

Our software aims to be a website for a car dealership with two primary users, employees and customers, enabling cusutomers to have quick access to vehicle information and employees the ability to add new inventory or edit exsisting inventory. Employees/Admin users will have the ability to edit information about vehicles for sale and add new vehicles. Customers will be able to view all information, and contact the dealership for more information or to learn about purchase options.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement. Do not replace the word `Description` with the actual description. Put the description in the space where these instructions are written. Maintain that practice for all future sections.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.
* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.

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
