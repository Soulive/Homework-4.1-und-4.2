import random, json, datetime

secret = random.randint(1, 30)
attempts = 0
name = input(str("Gamer: "))

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    for score_dict in score_list:
        print(score_dict["Gamer"], "had " + (str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date")),
              "The Secret number was:",score_dict["secret_number"], ". The wrong guesses were:",score_dict["wrong_guesses"])
        print("Top scores: " + str(score_list))

wrong_guesses = []

while True:
   guess = int(input("Guess the secret number (between 1 and 30): "))
   attempts += 1

   if guess == secret:

       score_data = {"Gamer": name,"attempts": attempts, "date": str(datetime.datetime.now()), "Gamer": name, "secret_number": secret,
                     "wrong_guesses": wrong_guesses}
       score_list.append(score_data)


       with open("score_list.txt", "w") as score_file:
           score_file.write(json.dumps(score_list))

       print("You've guessed it - congratulations! It's number " + str(secret))
       print("Attempts needed: " + str(attempts))
       break

   elif guess > secret:
       print("Your guess is not correct... try something smaller")
   elif guess < secret:
       print("Your guess is not correct... try something bigger")

   wrong_guesses.append(guess)