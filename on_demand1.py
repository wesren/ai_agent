import requests

# Replace with your actual API key and user ID
api_key = '<replace_api_key>'
external_user_id = '<replace_external_user_id>'

# Create a new chat session
session_url = 'https://api.on-demand.io/chat/v1/sessions'
session_headers = {
    'apikey': api_key
}
session_body = {
    "pluginIds": [],
    "externalUserId": external_user_id
}

# Make the request to create a session
session_response = requests.post(session_url, headers=session_headers, json=session_body)

# Check if the session was created successfully
if session_response.status_code == 201:
    session_data = session_response.json()
    session_id = session_data['data']['id']  # Extract the session ID from the response

    # Define the query using the session ID
    query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
    query_headers = {
        'apikey': api_key
    }
    query_body = {
        "endpointId": "predefined-openai-gpt4o",
        "query": "Put your query here",
        "pluginIds": ["plugin-1730655786", "plugin-1716326559"],
        "responseMode": "sync"
    }

    # Make the request to submit a query
    query_response = requests.post(query_url, headers=query_headers, json=query_body)

    # Check if the query was submitted successfully
    if query_response.status_code == 200:
        query_data = query_response.json()
        # Process the query response as needed
        print(query_data)
    else:
        print("Failed to submit the query:", query_response.status_code, query_response.text)
else:
    print("Failed to create chat session:", session_response.status_code, session_response.text)
