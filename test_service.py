import os

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, "input.txt")
    
    with open(file_path, 'a') as file:
        while True:
            user_input = input("Type something (press Enter to write to file, or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            file.write(user_input + '\n')
            file.flush()  # Flush the buffer to ensure immediate writing to the file

if __name__ == "__main__":
    main()
