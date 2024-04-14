# Import packages - "requests"
# Install the "requests" package from pip - https://pypi.org/project/requests/
import requests

# Global variables
previous_word: str = None
bookmarked_words = []

# Function to take 1 string as an input and print the dictionary meaning fetched from the API as an output to the console
def get_dictionary_meaning(word: str):
    # Function logic goes here

    global previous_word
    previous_word = None

    # Dictionary API documentation - https://dictionaryapi.dev/
    # Make API request using the "requests" python pip module
    r = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)

    # If word is not found, API gives 404 status code
    if r.status_code == 404:
        print("\nError: Could not find the meaning of the given word. Try a different word.")
        return

    # If status code is not 200, then API response is not successful
    if r.status_code != 200:
        print("\nError: Could not retrieve the meaning of the given word. Please try again.")
        return

    # Parse the API response using json
    response = r.json()[0]

    previous_word = response["word"].capitalize()

    # Format and print the response to console
    print("\n======== Meaning of the word: '" + previous_word + "' ========")

    for meaning in response["meanings"]:
        print("\n")  # New Line
        print("Part of Speech: " + meaning["partOfSpeech"])

        for definition in meaning["definitions"]:
            print("-> " + definition["definition"])

        if len(meaning["synonyms"]) > 0:
            print("Synonyms: " + ", ".join(meaning["synonyms"]))

        if len(meaning["antonyms"]) > 0:
            print("Antonyms: " + ", ".join(meaning["antonyms"]))

    print("\n================ End of Meaning =================\n")


# Infinite Loop to take user input from the console. When the word 'exit' is read, quit the program
while True:
    print("\nInstructions:")
    print("Type a word and press enter to fetch it's meaning.")
    print("Type 'exit' to quit the program.")

    if previous_word is not None:
        print("Type '*' to bookmark the last input word.")

    print("Type '**' to view all bookmarked words.")
    print("Input:", end=" ")

    word = input()  # Here, we capture user input from console

    print("\n")

    # Check if word is 'exit'
    # If yes, exit loop
    if word == "exit":
        print("Exiting. Have a nice day!\n")
        break  # Exit the loop

    # If word is empty or just consisting of white space characters, show an error message and move to next iteration in the loop.
    if word.strip() == "":
        print("Error: Enter a non-empty word to get the dictionary meaning.")
        continue  # Skip current iteration of the loop

    # Bookmark the last word
    if word == "*":
        if previous_word is not None:
            bookmarked_words.append(previous_word)
            print("Successfully bookmarked the word '" + previous_word + "'.")
            previous_word = None
        else:
            print("Error: There is no previous word present to bookmark.")
        continue

    # Show all bookmarked words
    if word == "**":
        if len(bookmarked_words) > 0:
            print("Bookmarked words: " + ", ".join(bookmarked_words))
        else:
            print("There are no bookmarked words present.")
        continue

    # Call the meaning function
    get_dictionary_meaning(word)
