from game_type.game_factory import GameFactory
from eng_dictionary.dictionary import Dictionary
import grpc
from game_grpc import game_pb2, game_pb2_grpc
from concurrent import futures
import time


dic = Dictionary()
factory = GameFactory()


class SpellingBeeServer(game_pb2_grpc.SpellingBeeGameServicer):

    def __init__(self):
        self.game = None
        self.difficulty = ""

    def SendDifficulty(self, request, context):
        self.difficulty = request.difficulty
        self.game = factory.create_game(request.difficulty, dic)
        print(self.game.letters)
        print(self.game.main_letter)
        response = game_pb2.Letters()
        response.game_letters = self.game.letters_to_string()
        response.main_letter = self.game.main_letter
        return response

    def CheckWord(self, request, context):
        res_score, res_outcome = self.game.check_word(request.word)
        response = game_pb2.Score()
        if res_outcome:
            response.outcome = True
        else:
            response.outcome = False
        response.score = res_score
        return response

    def GetUserWords(self, request, context):
        response = game_pb2.Words()
        response.words = self.game.user_words_to_string()
        return response

    def GetUserScore(self, request, context):
        response = game_pb2.Score()
        response.score = self.game.score
        return response









server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
game_pb2_grpc.add_SpellingBeeGameServicer_to_server(SpellingBeeServer(), server)

print("Starting server")
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(60000)
except KeyboardInterrupt:
    server.stop(0)