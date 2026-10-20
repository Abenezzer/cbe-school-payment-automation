# CBE School Payment Automation System

An automated workflow built with Python and Selenium that integrates a Google AppSheet school management system with the CBE (Commercial Bank of Ethiopia) School Payment Portal.

## 📌 Business Problem
When registering new students, administrative staff must manually enter student and parent details into the school's internal management application (Google AppSheet) and then manually re-enter the same information into the bank's portal to generate payment codes. This duplicate entry process is time-consuming and prone to human error.

## 🚀 Solution Overview
This automation script bridges the two systems seamlessly:
1. **Fetch:** Accepts a unique `Student ID` as input and queries the Google AppSheet web interface to retrieve the required student and parent details.
2. **Process:** Log into the CBE School Payment portal securely.
3. **Generate:** Populates the student credentials into the CBE system and generates the specific fee structure/payment code.
4. **Output:** Extracts and returns the verified Student Name, Student ID, and the newly generated Payment Code for receipting.

## 🛠️ Tech Stack & Tools
- **Language:** Python 3.x
- **Browser Automation:** Selenium WebDriver
- **Target Applications:** Google AppSheet, Commercial Bank of Ethiopia (CBE) Henon School Payment Portal


