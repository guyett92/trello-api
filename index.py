import requests
import json


class TrelloBoard:

    def __init__(self, key, token, board_id):
        self.auth = {'key': key, 'token': token, 'idBoard': board_id}
        self.url = "https://api.trello.com/1"
        self.headers = {
            'type': "type",
            'content-type': "application.json"
        }

    def get_lists(self):
        data = self.auth.copy()
        board_url = self.url + '/boards/' + self.auth["idBoard"] + '/lists'
        response = requests.get(url=board_url, data=data)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(response.status_code)

    def choose_list(self):
        try:
            lists = self.get_lists()
            print('Which list would you like to add a card to? Choose a number below.')
            for i in range(len(lists)):
                print(f'{i + 1}. {lists[i]["name"]}')
            reply = int(input('\n')) - 1
            if reply not in range(len(lists)):
                print('Please enter an appropriate value.\n')
                return self.choose_list()
            else:
                return lists[reply]["id"]
        except ValueError:
            print('Please enter an integer.\n')
            return self.choose_list()

    def card_color(self):
        reply = input('What would you like to label this card as? Please choose a number. \n1. General\n2. Completed\n3. Current\n4. To-Do\n')
        if reply == '1':
            return 'blue'
        elif reply == '2':
            return 'green'
        elif reply == '3':
            return 'yellow'
        elif reply == '4':
            return 'red'
        else:
            print('Please choose only from the options below.\n')
            return self.card_color()

    def add_comment(self, card_id):
        reply = input('Would you like to add a comment (Y/N)?\n')
        if reply.lower() == 'y':
            text = input('Please enter your comment text:\n')
        if reply.lower() == 'n':
            print('Thank you!')
            return
        else:
            return self.add_comment(card_id)
        data = self.auth.copy()
        data['text'] = text
        url = self.url + "/cards/" + card_id + "/actions/comments"
        response = requests.post(url=url, data=data)
        if response.status_code == 200:
            print('success')
        else:
            print(response.status_code)


    def create_card(self):
        data = self.auth.copy()
        data['idList'] = self.choose_list()
        card_name = input('What would you like to call the card?\n')
        card_url = self.url + "/cards"
        data['name'] = card_name
        data['labels'] = [self.card_color()]
        response = requests.post(url=card_url, data=data)
        if response.status_code == 200:
            self.add_comment(json.loads(response.text)["id"])
        else:
            print(response.status_code)
