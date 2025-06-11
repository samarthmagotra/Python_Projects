# Airalo API Test Automation

## Overview  
This project automates testing for the **Airalo API** using Python and `pytest`.  

### **Key Features**  
- **OAuth2 Authentication**: Secure token retrieval.  
- **Ordering eSIMs** (`POST /orders`): Validate eSIM purchases.  
- **Retrieving eSIMs** (`GET /sims`): Ensure correct package IDs and quantities.  
- **Cross-checking eSIM IDs**: Verify consistency between `POST` and `GET` responses.  
- **Validating number of eSIMs and package ID**: Verify num of `POST` eSIMs are subset of `GET` responses eSIMs, and package IDs are correct. 

## Prerequisites  
Before running the tests, ensure you have:  
- Python **3.x** installed.  
- Dependencies installed via:  
  ```sh
  pip install requests pytest 

## Execute all test cases via:

    ```sh 
    pytest -v test_airalo_api.py

## ** Test Breakdown **
## OAuth2 Token Retrieval
get_oauth_token() fetches a valid access token, ensuring API authentication.

## Ordering eSIMs (test_post_an_order)
Sends a POST request to order 6 "merhaba-7days-1gb" eSIMs.
Validates package ID and ensures quantity is correct.

## Retrieving eSIMs (test_get_an_order)
Fetches the list of eSIMs using GET /sims.
Checks for minimum 6 eSIMs.
Verifies APN settings ("airalo2"), matching_id, and other attributes.

## Verifying Posted SIMs Exist in GET Request (test_post_sims_in_get_request)
Ensures SIMs ordered via POST appear in the GET /sims response.
Uses set comparison to validate SIM ID presence in GET response.