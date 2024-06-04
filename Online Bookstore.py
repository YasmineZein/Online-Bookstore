from abc import abstractmethod
print("Welcome to Yasmine Zein's online Bookstore!")

class Item:
    def __init__(self, item_type,price):
        self.item_type = item_type
        self.__price = price
    
    def get_item_type(self):
        item = int(input(f"1.Book \n2.Magazine \n3.DVDs \nSelect(1/2/3): "))
        return item
    @abstractmethod
    def get_info(self):
        pass
    

class Book(Item):
    def __init__(self, item_type, title, author, price):
        super().__init__(item_type, price)
        self.title = title
        self.author = author
class Fiction(Book):
    
    def __init__(self, item_type, title, author, price, genre):
        super().__init__(item_type, title, author, price)
        self.genre = genre

    def get_info(self):
        return f"\nTitle: {self.title} \nAuthor: {self.author} \nPrice: {self._Item__price} \nGenre: {self.genre}\n --------------"
class NonFiction(Book):
    def __init__(self, item_type, title, author, price, topic):
        super().__init__(item_type, title, author, price)
        self.topic = topic

    def get_info(self):
        return f"\nTitle: {self.title} \nAuthor: {self.author} \nPrice: {self._Item__price} \nTopic: {self.topic}\n --------------"


class Magazine(Item):
    def __init__(self, item_type, price, author):
        super().__init__(item_type, price)
        self.author = author
    def get_info(self):
        return f"\nAuthor: {self.author} \nPrice: {self._Item__price}\n --------------"


class DVDs(Item):
    def __init__(self, item_type, price, type):
        super().__init__(item_type, price)
        self.type = type
class Games(DVDs):
    def __init__(self, item_type, price, type, title):
        super().__init__(item_type, price, type)
        self.title = title
    def get_info(self):
        return f"\nType: {self.type} \nTitle: {self.title} \nPrice: {self._Item__price}\n --------------"
class Movies(DVDs):
    def __init__(self, item_type, price, type, title, director, genre):
        super().__init__(item_type, price, type)
        self.title = title
        self.director = director
        self.genre = genre
    def get_info(self):
        return f"\nType: {self.type} \nTitle: {self.title} \nDirector: {self.director} \nPrice: {self._Item__price}\n --------------"

item1 = Item(None, None)


fiction_books = [Fiction('book', "Great Expectations", "Charles Dickens", 11, "Classic"),
                Fiction('book', "The Daughter of the Pirate King", "Tricia Levenseller", 10.50, "Fantasy"),
                Fiction('book', "After Anna", "Lisa Scottoline", 12, "Mystery"),
                Fiction('book', "The Secret Life of Bees", " Sue Monk Kidd", 8.50, "Historical Fiction")]
non_fiction_books = [NonFiction('book', "The Subtle Art of Not Giving a Fuck", "Mark Manson", 14.50, "Self-help"),
                    NonFiction('book', "Rich Dad Poor Dad", "Robert Kiyosaki", 15, "Business"),
                    NonFiction('book', "The 48 Laws of Power", "Robert Greene", 16, "Psychology"),
                    NonFiction('book', "Atomic Habits", "James Clear", 16.50, "Personal Development")]

news = [Magazine('magazine', 10, "The Daily Mail"),
        Magazine('magazine', 8.50, 'The New York Times'),
        Magazine('magazine', 11, 'The Wall Street Journal'),
        Magazine('magazine', 10, 'The Guardian')]

dvd_games = [Games('dvd', 79.50, "Gaming", "Game of Thrones"),
             Games('dvd', 32, "Gaming", "FIFA World Cup"),
             Games('dvd', 54.50, "Gaming", "Call Of Duty"),
             Games('dvd', 45, "Gaming", "GTA V")]
dvd_movies = [Movies('dvd', 79.50, "Movie", "The Godfather", 'Francis Ford Coppola', "Drama"),
             Movies('dvd', 54.50, "Movie", "The Godfather: Part II", 'Francis Ford Coppola', "Drama"), 
             Movies('dvd', 32, "Movie", "Maleficent", 'Joel Coen', "Fantasy"),
             Movies('dvd', 45, "Movie", "Titanic", 'James Cameron', "Romance")]
dvd_TV = [Movies('dvd', 65, "TV show", "Game Of Thrones", 'George R. R. Martin', "Drama"),
             Movies('dvd', 74.50, "TV show", "Breaking Bad", 'Vince Gilligan', "Crime"),
             Movies('dvd', 55, "TV show", "Rick and Morty", 'Dan Harmon', "Fantasy"),
             Movies('dvd', 45, "TV show", "Attack on Titan", 'Hajime Isayama', "Fantasy")]

cart = []
def add_to_cart(item):
    cart.append(item)
def calculate_total_price():
    total_price = sum(item._Item__price for item in cart)
    print(f"Total price: ${total_price:.2f}")

while True:
    print("\n1. Display Available Items")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            try:
                print("\nAvailable Items:")
                user_choice = item1.get_item_type()
                if user_choice == 1:
                    try:
                        fic_non = int(input("Fiction(1) or Non-Fiction(2): "))
                        try:
                            if fic_non == 1:
                                def display_books():
                                    for book in fiction_books:
                                        print(book.get_info())
                                display_books()
                                fic_choose = int(input("Select(1/2/3/4): "))
                                if fic_choose == 1:
                                    add_to_cart(fiction_books[0])
                                    calculate_total_price()
                                    print("Great Expectations was added to your cart!")
                                    continue
                                elif fic_choose == 2:
                                    add_to_cart(fiction_books[1])
                                    calculate_total_price()
                                    print("The Daughter of the Pirate King was added to your cart!")
                                    continue
                                elif fic_choose == 3:
                                    add_to_cart(fiction_books[2])
                                    calculate_total_price()
                                    print("After Anna was added to your cart!")
                                    continue
                                elif fic_choose == 4:
                                    add_to_cart(fiction_books[3])
                                    calculate_total_price()
                                    print("The Secret Life of Bees was added to your cart!")
                                    continue
                                else:
                                    print("Invalid choice. Please try again.")
                        except ValueError:
                            print("Invalid input! Please enter a number bet 1-4.")    
                    
                        try:
                            if fic_non == 2:
                                def display_books():
                                    for book in non_fiction_books:
                                        print(book.get_info())
                                display_books()
                                fic_choose = int(input("Select(1/2/3/4): "))
                                if fic_choose == 1:
                                    add_to_cart(non_fiction_books[0])
                                    calculate_total_price()
                                    print("The Subtle Art of Not Giving a Fuck was added to your cart!")
                                    continue
                                elif fic_choose == 2:
                                    add_to_cart(non_fiction_books[1])
                                    calculate_total_price()
                                    print("Rich Dad Poor Dad was added to your cart!")
                                    continue
                                elif fic_choose == 3:
                                    add_to_cart(non_fiction_books[2])
                                    calculate_total_price()
                                    print("The 48 Laws of Power was added to your cart!")
                                    continue
                                elif fic_choose == 4:
                                    add_to_cart(non_fiction_books[3])
                                    calculate_total_price()
                                    print("Atomic Habits was added to your cart!")
                                    continue
                                else:
                                    print("Invalid choice. Please try again.")
                        except ValueError:
                            print("Invalid input! Please enter a number bet 1-4.")    
                    except ValueError:
                        print("Invalid input! Please enter a number bet 1-2.")
                elif user_choice == 2:
                    def display_magazines():
                        for magazine in news:
                            print(magazine.get_info())
                    display_magazines()
                    try:
                        new_choose = int(input("Select(1/2/3/4): "))
                        if new_choose == 1:
                            add_to_cart(news[0])
                            calculate_total_price()
                            print("The Daily Mail was added to your cart!")
                            continue
                        elif new_choose == 2:
                            add_to_cart(news[1])
                            calculate_total_price()
                            print("The New York Times was added to your cart!")
                            continue
                        elif new_choose == 3:
                            add_to_cart(news[2])
                            calculate_total_price()
                            print("The Wall Street Journal was added to your cart!")
                            continue
                        elif new_choose == 4:
                            add_to_cart(news[3])
                            calculate_total_price()
                            print("The Guardian was added to your cart!")
                            continue
                        else:
                            print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Invalid input! Please enter a number bet 1-4.")
                elif user_choice == 3:
                    dvd_type = int(input("Games(1), Movies(2) or TV Shows(3): "))
                    try:
                        if dvd_type == 1:
                            def display_dvds():
                                for dvd in dvd_games:
                                    print(dvd.get_info())
                            display_dvds()
                            dvd_choose = int(input("Select(1/2/3/4): "))
                            if dvd_choose == 1:
                                add_to_cart(dvd_games[0])
                                calculate_total_price()
                                print("Game of Thrones was added to your cart!")
                                continue
                            elif dvd_choose == 2:
                                add_to_cart(dvd_games[1])
                                calculate_total_price()
                                print("FIFA World Cup was added to your cart!")
                                continue
                            elif dvd_choose == 3:
                                add_to_cart(dvd_games[2])
                                calculate_total_price()
                                print("Call Of Duty was added to your cart!")
                                continue
                            elif dvd_choose == 4:
                                add_to_cart(dvd_games[3])
                                calculate_total_price()
                                print("GTA V was added to your cart!")
                                continue
                            else:
                                print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Invalid input! Please enter a number bet 1-4.")
                    try:
                        if dvd_type == 2:
                            def display_movies():
                                for movie in dvd_movies:
                                    print(movie.get_info())
                            display_movies()
                            movie_choose = int(input("Select(1/2/3/4): "))
                            if movie_choose == 1:
                                add_to_cart(dvd_movies[0])
                                calculate_total_price()
                                print("The Godfather was added to your cart!")
                                continue
                            elif movie_choose == 2:
                                add_to_cart(dvd_movies[1])
                                calculate_total_price()
                                print("The Godfather: Part II was added to your cart!")
                                continue
                            elif movie_choose == 3:
                                add_to_cart(dvd_movies[2])
                                calculate_total_price()
                                print("Maleficent was added to your cart!")
                                continue
                            elif movie_choose == 4:
                                add_to_cart(dvd_movies[3])
                                calculate_total_price()
                                print("Titanic was added to your cart!")
                                continue
                            else:
                                print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Invalid input! Please enter a number bet 1-4.")
                    try:
                        if dvd_type == 3:
                            def display_tv():
                                for tv in dvd_TV:
                                    print(tv.get_info())
                            display_tv()
                            tv_choose = int(input("Select(1/2/3/4): "))
                            if tv_choose == 1:
                                add_to_cart(dvd_TV[0])
                                calculate_total_price()
                                print("Game Of Thrones was added to your cart!")
                                continue
                            elif tv_choose == 2:
                                add_to_cart(dvd_TV[1])
                                calculate_total_price()
                                print("Breaking Bad was added to your cart!")
                                continue
                            elif tv_choose == 3:
                                add_to_cart(dvd_TV[2])
                                calculate_total_price()
                                print("Rick and Morty was added to your cart!")
                                continue
                            elif tv_choose == 4:
                                add_to_cart(dvd_TV[3])
                                calculate_total_price()
                                print("Attack on Titan was added to your cart!")
                                continue
                            else:
                                print("Invalid choice. Please try again.")
                        else:
                            print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Invalid input! Please enter a number bet 1-4.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number bet 1-3.")
        elif choice == 2:
            print("Cart:")
            for item in cart:
                print(item.get_info())
        elif choice == 3:
            calculate_total_price()
            
            logout = input("Do you want to continue shopping? (y/n): ")
            if logout == 'n':
                print("Thank you for shopping with us!")
                raise SystemExit
            elif logout == 'y':
                continue
            else:
                print("Invalid input! Please enter y or n.")
            
        elif choice == 4:
            print("Thank you for shopping with us!")
            raise SystemExit
        else:
            print("Invalid input!")

    except ValueError:
        print("Invalid input! Please enter a number bet 1-4.")
