import os

class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def save_post(self):
        try:
            if self.user.name == "" or self.title == "" or self.content == "":
                raise ValueError("All fields are required!")

            filename = f"{self.user.name}_{self.title}.txt".replace(" ", "_")

            with open(filename, "w") as file:
                file.write(f"User: {self.user.name}\n")
                file.write(f"Title: {self.title}\n\n")
                file.write("Content:\n")
                file.write(self.content)

            print("Post saved successfully!")

        except Exception as e:
            print("Error:", e)

def create_post():
    try:
        name = input("Enter Username: ").strip()
        title = input("Enter Title: ").strip()
        content = input("Enter Content: ").strip()

        user = User(name)
        post = Post(user, title, content)

        post.save_post()

    except Exception as e:
        print("Error:", e)

def view_posts():
    try:
        files = [f for f in os.listdir() if f.endswith(".txt")]

        if len(files) == 0:
            print("No posts available!")
            return

        for i in range(len(files)):
            print(f"{i+1}. {files[i]}")

        choice = int(input("Select post number: "))

        if choice < 1 or choice > len(files):
            raise IndexError("Invalid selection!")

        filename = files[choice - 1]

        with open(filename, "r") as file:
            print(file.read())

    except ValueError:
        print("Enter a valid number!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\nMiniBlog")
        print("1. Create Post")
        print("2. View Posts")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_post()
        elif choice == "2":
            view_posts()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()