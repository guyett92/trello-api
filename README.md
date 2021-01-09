# Trello API Card Creation

A small application that allows you to create a card, categorize it, and add comments to it once it's been added. The code uses recursion, f strings, and a couple libraries. This took about 2 hours to create due to some issues with a pip update.

## Technology Used

* Python
* Requests
* JSON

## API
* [Trello](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)

## Getting Started

To get started you need to obtain your key and token from Trello which can be done by following the steps below.

1. Visit [Trello API](https://trello.com/app-key) and login or create an account. Your API key will be here.
2. On the same web page as before [Trello API](https://trello.com/app-key), you can access your token. Click "Token" underneath your API to get your token.
3. You need your board ID that you want to use as well. The board should have the lists you want to use on it. To get your board ID, visit your board and add a `.json` to the URL. For example, if your board URL is `https://trello.com/b/kjfsa01/test` you would use `https://trello.com/b/kjfsa01/test.json` as your new URL.
4. Once there, copy the `"id"` field. This is your board ID.
5. In `py-test.py`, add your key, token, and board ID to the appropriate variables.
6. Run the code!

## Example Board

* [Example](https://trello.com/b/kU1YjQA0/cpc-code-test)

## Future Plans

* Allow users to create and view boards and lists.
* Give users more choices throughout the process of creation.
* Add update features.
* Create a front-end to visualize the changes.
* Add user authentication.