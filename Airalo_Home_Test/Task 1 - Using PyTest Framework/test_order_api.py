import pprint
import requests
import pytest

'''
Authentication : Obtain OAuth2 tokens to access the Airalo Partner API, using the provided credentials
'''
@pytest.fixture()
def get_oauth_token():
    '''# Getting Oauth2 Token'''
    token_url = "https://sandbox-partners-api.airalo.com/v2/token"
    client_id = "7e29e2facf83359855f746fc490443e6"
    client_secret = "e5NNajm6jNAzrWsKoAdr41WfDiMeS1l6IcGdhmbb"
    # Request payload
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    # Headers
    headers = {
        "Accept": "application/json"
    }
    # Sending POST request
    response = requests.post(token_url, data=payload, headers=headers)
    assert response.status_code == 200, f"Token request failed: {response.text}"

    # Handling response
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['data']['access_token']
        assert access_token is not None
        #pprint.pprint(token_data)
        print("Access Token:", access_token)
        return access_token


'''
Endpoint 1 : Use endpoint to POST an order for 6 "merhaba-7days-1gb" eSIMs.
'''
def test_post_an_order(get_oauth_token):
    token_url = "https://sandbox-partners-api.airalo.com/v2/orders"
    package_id = "merhaba-7days-1gb"
    # Request payload
    payload = {
        "quantity": 6,
        "package_id": package_id,
    }
    # Headers
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {get_oauth_token}"
    }

    # Sending POST request
    response = requests.post(token_url, data=payload, headers=headers)
    assert response.status_code == 200, f"Order request failed: {response.text}"
    # Handling response
    sim_data = response.json()
    #pprint.pprint(sim_data)
    # Extract SIM IDs
    sim_ids = [sim["id"] for sim in sim_data["data"]["sims"]]
    pack_id = [sim_data["data"]["package_id"]]
    print("Post SIM IDs:", sim_ids)
    print("Package ID:" , pack_id)
    # validating that sim ids are present
    assert len(sim_ids) == 6, f"Expected 6 eSIMs, but got {len(sim_ids)}"
    # validating that package_ids are present
    assert package_id in pack_id, f"Error: '{package_id}' is not in the package_id configured list!"
    #return sim_ids

'''
Endpoint 2 : GET a list of eSIMs.
Ensure the list contains 6 eSIMs, and that all of them have the "merhaba-7days-1gb" package slug.
'''
def test_get_an_order(get_oauth_token):
    token_url = "https://sandbox-partners-api.airalo.com/v2/sims"
    # Request payload
    payload = {
        "include": "order"
    }
    # Headers
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {get_oauth_token}"
    }
    # Sending GET request
    response = requests.get(token_url, data=payload, headers=headers)
    assert response.status_code == 200, f"SIM retrieval failed: {response.text}"
    # Handling GET response
    sim_data = response.json()
    pprint.pprint(sim_data)
    # validating that sim ids are present
    sim_ids = [sim["id"] for sim in sim_data["data"]]
    assert len(sim_ids) >= 6, f"Expected 6 or more eSIMs, but got {len(sim_ids)}"
    print("Get SIM IDs:", sim_ids)
    # validating some other response body values
    assert sim_data["data"][0]['apn_type'] == 'manual'
    assert sim_data["data"][0]['apn_value'] == 'airalo2'
    assert sim_data["data"][0]['matching_id'] == 'TEST'
    #return sim_ids

'''
Ensure the list contains 6 eSIMs
'''
def test_post_sims_in_get_request(get_oauth_token):
    token_url1 = "https://sandbox-partners-api.airalo.com/v2/orders"
    token_url2 = "https://sandbox-partners-api.airalo.com/v2/sims"
    package_id = "merhaba-7days-1gb"
    # Request payload
    payload1 = {
        "quantity": 6,
        "package_id": package_id,
    }
    payload2 = {
        "include": "order"
    }
    # Headers
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {get_oauth_token}"
    }
    # Sending POST request
    response_post = requests.post(token_url1, data=payload1, headers=headers)
    assert response_post.status_code == 200, f"Order request failed: {response_post.text}"
    # Handling POST response
    sim_data_post = response_post.json()
    # Extract SIM IDs
    sim_ids_post = [sim["id"] for sim in sim_data_post["data"]["sims"]]

    # Sending GET request
    response_get = requests.get(token_url2, data=payload2, headers=headers)
    assert response_get.status_code == 200, f"SIM retrieval failed: {response_get.text}"
    # Handling GET response
    sim_data_get = response_get.json()
    # validating that sim ids are present
    sim_ids_get = [sim["id"] for sim in sim_data_get["data"]]
    # Check if all SIM IDs in sim_post exist in sim_get
    assert set(sim_ids_post).issubset(set(sim_ids_get)), f"Expected eSIM from Post request are not present in Get response"

    if set(sim_ids_post).issubset(set(sim_ids_get)):
        print("All SIM IDs in Posted SIM list are present in Get SIM list")
    else:
        print("Some SIM IDs from Post list are missing in Get list")


