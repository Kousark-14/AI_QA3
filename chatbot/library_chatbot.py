import re

def get_response(user_input: str) -> str:
    text = user_input.lower().strip()

    # Exit conditions
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for visiting the library. Goodbye!"

    # Greetings
    if re.search(r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b", text):
        return "Hello! How can I assist you with library services today?"

    # Library hours
    if re.search(r"\b(library hours|timings|open|closing time)\b", text):
        return (
            "The library is open from 9:00 AM to 6:00 PM, Monday to Saturday. "
            "It remains closed on Sundays and public holidays."
        )

    # Book availability
    if re.search(r"\b(book availability|available books|find a book|search book)\b", text):
        return (
            "You can check book availability using the library catalog at the help desk "
            "or through the library management system."
        )

    # Issue books
    if re.search(r"\b(issue book|borrow book|take book)\b", text):
        return (
            "To issue a book, please present your library ID at the circulation counter. "
            "Students can borrow up to 3 books for 14 days."
        )

    # Return books
    if re.search(r"\b(return book|book return|submit book)\b", text):
        return (
            "Books must be returned on or before the due date at the return counter "
            "to avoid late fees."
        )

    # Late fine
    if re.search(r"\b(late fine|penalty|fine amount)\b", text):
        return (
            "The late fine is ₹2 per day per book after the due date."
        )

    # Library membership
    if re.search(r"\b(membership|library card|library id)\b", text):
        return (
            "Library membership is available to all registered students and staff. "
            "Please contact the library office for registration."
        )

    # Reference section
    if re.search(r"\b(reference books|reference section)\b", text):
        return (
            "Reference books are available in the reference section and "
            "cannot be issued outside the library."
        )

    # Default response
    return (
        "Sorry, I couldn't understand that. You may ask about library timings, "
        "book availability, issuing books, fines, or membership."
    )


def library_chatbot():
    print("LibraryBot: Welcome! I am your rule-based library assistant.")
    print("LibraryBot: Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:
        user = input("You: ")
        response = get_response(user)
        print("LibraryBot:", response)

        if user.lower().strip() in ["bye", "exit", "quit", "goodbye"]:
            break


# Run the chatbot
library_chatbot()
