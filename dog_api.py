"""
Assignment Overview:

You are building a Dog Image Browser using the Dog CEO REST API.

The app should allow users to:
- View a list of all available dog breeds
- Get a random image of a breed
- Get a random image of a sub-breed

You will be using the Dog CEO API: https://dog.ceo/dog-api/

Your app should display a main menu with the following options:
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

The system should handle the following errors:
- Handling errors when a user enters an invalid menu option
- Handling errors when a user enters a breed that does not exist
- Handling errors when a user enters a sub-breed that does not exist
- Handling connection errors when calling the API

If there is an error you should print your own custom error message to the user and allow them to try again.
- Hint: you can use a while loop + try / except blocks to handle this

You should use try / except blocks to handle these errors.

You can either use the should use the requests library or the http.client library to make your requests

"""


import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return {}

def get_random_image(breed):
    """GET request to fetch a random image from a breed."""
    # TOD0: Make a request to https://dog.ceo/api/breed/{breed}/images/random
    # TOD0: Return the image URL or handle errors
    try:
        response = requests.get("https://dog.ceo/api/breed/{breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return None

def get_random_sub_breed_image(breed, sub_breed):
    """GET request to fetch a random image from a sub-breed."""
    # TOD0: Make a request to https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random
    # TOD0: Return the image URL or handle errors
    try:
        response = requests.get("https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch random breed from API.")
        return None
   

def show_breeds(breeds_dict):
    """Prints all available breeds 5 per line."""
    # TOD0: Print all breeds (sorted), 5 per line
    if not breeds_dict:
        print("Error: No breeds available to display.")
        return
    
    breeds = sorted(breeds_dict.keys())
    print("\nAvailable breeds:")
    for i in range(0, len(breeds), 5):
        print("  " + ", ".join(breeds[i:i+5]))

def main():
    while True:
        print("\nDog Image Browser")
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        try:
            choice = input("Enter your choice (1-4): ").strip()
            choice_num = int(choice)
            if choice_num not in range(1, 5):
                raise ValueError("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Error: Invalid choice. Please select a number between 1 and 4.")
            continue
        
        if choice == "4":
            print("Goodbye!")
            break
        
        if choice_num == 1:
            breeds = get_all_breeds()
            if breeds is not None:
                show_breeds(breeds)
            else: 
                print("Please try again.")
                continue
            
        elif choice_num == 2:
            breeds = get_all_breeds()
            if breeds is None:
                print("please try again.")
                continue
            breed = input("Enter the breed name: ").strip().lower()
            if not breed:
                print("Error: Breed name cannot be empty.")
                continue
            if breed not in breeds:
                print(f"Error: Invalid breed '{breed}'. Please try again.")
                continue
            
            img_url = get_random_image(breed)
            if img_url:
                print(f"Random image of {breed}: {img_url}")
            else:
                print("Please try again.")
            
        elif choice_num == 3:
            breeds = get_all_breeds()
            if breeds is None:
                print("Please try again.")
                continue
            if breed not in breeds:
                print(f"Error: Invalid breed '{breed}'. Please choose a valid breed.")
                continue
            sub_breeds = breeds[breed]
            if not sub_breeds:
                print(f"Error: Breed '{breed}' has no sub-breeds.")
                continue
            print(f"Available sub-breeds for '{breed}': {', '.join(sub_breeds)}")
            sub_breed = input("Enter the sub-breed name: ").strip().lower()
            if not sub_breed:
                print("Error: Sub-breed name cannot be empty.")
                continue
            if sub_breed not in sub_breeds:
                print(f"Error: Invalid sub-breed '{sub_breed}' for breed '{breed}'")
                continue
            img_url = get_random_sub_breed_image(breed, sub_breed)
            if img_url:
                print(f"Random image of {sub_breed} from {breed}: {img_url}")
            else:
                print("Please try again.")
            continue
            

if __name__ == "__main__":
    main()
