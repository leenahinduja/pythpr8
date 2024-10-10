# Function to check even or odd numbers in a range
def check_even_odd():
    for number in range(1, 21):  # Checking numbers from 1 to 20
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

# Call the function
check_even_odd()
