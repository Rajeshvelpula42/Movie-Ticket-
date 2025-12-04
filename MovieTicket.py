# Simple Movie Ticket Booking System in Python

movies = {
    1: {"name": "Leo", "time": "10:00 AM", "total_seats": 10, "booked_seats": []},
    2: {"name": "Jailer", "time": "2:00 PM", "total_seats": 10, "booked_seats": []}
}


def show_movies():
    print("\nAvailable Movies:")
    for movie_id, movie in movies.items():
        print(f"{movie_id}. {movie['name']}  | Show Time: {movie['time']}")


def show_available_seats(movie_id):
    movie = movies[movie_id]
    total = movie["total_seats"]
    booked = movie["booked_seats"]
    available = [seat for seat in range(1, total + 1) if seat not in booked]

    print(f"\nMovie: {movie['name']} ({movie['time']})")
    print(f"Total Seats: {total}")
    print(f"Booked Seats: {booked if booked else 'None'}")
    print(f"Available Seats: {available if available else 'Housefull'}")


def book_ticket():
    show_movies()
    try:
        movie_id = int(input("\nEnter movie number to book ticket: "))
        if movie_id not in movies:
            print("Invalid movie selection!")
            return

        show_available_seats(movie_id)

        if len(movies[movie_id]["booked_seats"]) == movies[movie_id]["total_seats"]:
            print("Sorry, no seats available for this show.")
            return

        seat_no = int(input("Enter seat number to book: "))

        if seat_no < 1 or seat_no > movies[movie_id]["total_seats"]:
            print("Invalid seat number!")
            return

        if seat_no in movies[movie_id]["booked_seats"]:
            print("Seat already booked! Please choose another seat.")
            return

        # Book the seat
        movies[movie_id]["booked_seats"].append(seat_no)
        print(f"Ticket booked successfully for {movies[movie_id]['name']} at seat {seat_no}.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n=== Movie Ticket Booking System ===")
        print("1. View Movies")
        print("2. View Available Seats")
        print("3. Book Ticket")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_movies()

        elif choice == "2":
            show_movies()
            try:
                movie_id = int(input("\nEnter movie number to view seats: "))
                if movie_id in movies:
                    show_available_seats(movie_id)
                else:
                    print("Invalid movie selection!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            book_ticket()

        elif choice == "4":
            print("Thank you for using the Movie Ticket Booking System!")
            break

        else:
            print("Invalid choice! Please choose between 1-4.")


if __name__ == "__main__":
    main()
