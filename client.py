import grpc
from game_grpc import game_pb2, game_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
difficulties = {1: "short", 2: "standard"}

stub = game_pb2_grpc.SpellingBeeGameStub(channel)


while True:
    # ===================================================
    # SET DIFFICULTY
    # ===================================================
    try:
        difficulty = int(input("Game Type:\n[1] Short\n[2] Standard\n"))
        if difficulty not in difficulties:
            continue
        else:
            difficulty = difficulties[difficulty]
    except ValueError:
        print("Invalid option")
        continue

    # ===================================================
    # INITIALIZE GAME
    # ===================================================
    difficulty_chosen = game_pb2.Difficulty(difficulty=difficulty)
    response = stub.SendDifficulty(difficulty_chosen)
    letters = response.game_letters
    main_letter = response.main_letter

    # ===================================================
    # INPUT WORDS
    # ===================================================
    while True:
        print("[1] View Words [2] Quit")
        print(f"[{main_letter}] {letters}")
        word = input("Word > ")
        # View Words
        if word == "1":
            print("\n"*20)
            get_words = stub.GetUserWords(game_pb2.Empty())
            print(f"You have found: {get_words.words}")
            continue
        # Quit
        elif word == "2":
            print("\n"*20)
            get_words = stub.GetUserWords(game_pb2.Empty())
            get_score = stub.GetUserScore(game_pb2.Empty())
            print("You have quit the game.")
            print(f"Your Words: {get_words.words}")
            print(f"Your Score: {get_score.score}")
            print("Thanks for playing!")
            break
        word = game_pb2.Word(word=word)
        response = stub.CheckWord(word)
        if response.outcome:
            print("Word is valid")
        else:
            print("Word is not valid")
        print("Current Score: ", response.score)
        print("")

    input("")




