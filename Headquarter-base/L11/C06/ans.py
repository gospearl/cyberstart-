import requests

def post_message():
    # The URL of the API endpoint
    api_url = 'https://bondogge.com/createPost'

    # The message you want to post
    message = 'Hello'

    # The data to be sent in the POST request
    data = {'message': message}

    # Set the headers (if needed)
    headers = {'Content-Type': 'application/json'}

    try:
        # Make the POST request
        response = requests.post(api_url, json=data, headers=headers)

        # Check if the request was successful (status code 2xx)
        if response.ok:
            try:
                # Try to parse the response as JSON
                response_json = response.json()
                print('Message posted successfully. Response:', response_json)
            except ValueError:
                # Handle cases where the response is not JSON
                print('Received a non-JSON response. Status code:', response.status_code)
                print('Response Content:', response.text)
        else:
            # Handle non-successful HTTP status codes
            print('Failed to post message. Status code:', response.status_code)
            print('Response Content:', response.text)

    except requests.RequestException as e:
        # Handle general request exceptions
        print('An error occurred during the request:', e)

if __name__ == "__main__":
    post_message()
