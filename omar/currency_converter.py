import requests

# Function to get supported currencies from the API
def get_supported_currencies(api_key):
    url = "https://api.apilayer.com/fixer/symbols"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch supported currencies.")
        quit()
    data = response.json()
    if not data.get('success', False):
        print(f"Error: {data.get('error', {}).get('info', 'An unknown error occurred.')}")
        quit()
    return data.get('symbols', {})

# Function to get and validate the currency code input
def get_currency(prompt, supported_currencies):
    while True:
        currency = input(prompt).strip().upper()
        if currency in supported_currencies:
            return currency
        else:
            print("Please enter a valid 3-letter currency code from the supported list.")

# Function to get and validate the amount input
def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("The amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("The amount must be a number.")

# Main script
def main():
    api_key = "N7gQzdj78vSFntd3egAlg6vPrbDOtkzi"
    
    # Fetch supported currencies
    supported_currencies = get_supported_currencies(api_key)
    print("Supported currencies:", ", ".join(supported_currencies.keys()))

    # Get initial and target currency codes from user
    init_currency = get_currency("Enter an initial currency (e.g., USD): ", supported_currencies)
    target_currency = get_currency("Enter a target currency (e.g., EUR): ", supported_currencies)

    # Get the amount from user
    amount = get_amount("Enter an amount: ")

    # Debugging: Print currency codes
    print(f"Initial currency: {init_currency}")
    print(f"Target currency: {target_currency}")

    # Construct the URL for the API request
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    # Debugging: Print the URL
    print(f"Constructed URL: {url}")

    # Set up the headers with the API key
    headers = {"apikey": api_key}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        print("Sorry, there was a problem. Please try again later.")
        quit()

    # Parse the JSON response
    result = response.json()

    # Debugging: Print the full response
    print("Full API response:")
    print(result)

    # Check if the API response indicates success
    if not result.get('success', False):
        print(f"Error: {result.get('error', {}).get('info', 'An unknown error occurred.')}")
    else:
        print(result)

if __name__ == "__main__":
    main()
