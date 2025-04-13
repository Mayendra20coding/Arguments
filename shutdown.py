def shutdown():
    user_input = input("Do you want to shut down Yes No")
    normalized_input = user_input.strip().lower()
    if normalized_input == "yes":
        print("Shutting down...")
    elif normalized_input == "no":
        print("Shutdown aborted.")
    else:
        print(" sorry ")
shutdown()