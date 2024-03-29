#include "pch.h"
#include <iostream>
#include "Deck.h"
#include "Player.h"

using namespace std;

int main()
{
	string playerAName, playerBName;

	cout << "Enter the first players name: ";
	getline(cin, playerAName);
	cout << "Enter the second player's name: ";
	getline(cin, playerBName);

	vector<Card> a, b;
	Deck* deck = new Deck();
	for (int i = 0; i < 26; i++) {
		a.push_back(deck->getNext());
		b.push_back(deck->getNext());
	}

	Player* playerA = new Player(playerAName, a);
	Player* playerB = new Player(playerBName, b);

	cout << playerA->getCard().getValue() << endl;
	cout << playerB->getCard().getValue() << endl;

	vector<Card> potCards;
	int round = 1;

	while (!playerA->hasEmptyHand() && !playerB->hasEmptyHand()) {
		Card cardA = playerA->getCard();
		Card cardB = playerB->getCard();
		cout << "======================= ROUND " << round++ << " START =======================" << endl;
		cout << playerA->getName() << "'s card value is " << cardA.getValue() << endl;
		cout << playerB->getName() << "'s card value is " << cardB.getValue() << endl;

		if (cardA.getValue() > cardB.getValue()) {
			potCards.push_back(cardA);
			potCards.push_back(cardB);
			cout << playerA->getName() << " wins this round! Added " << potCards.size() << " cards to " << playerB->getName() << "'s hand." << endl;
			playerB->addCards(potCards);
			potCards.clear();
		}
		else if (cardB.getValue() > cardA.getValue()) {
			potCards.push_back(cardA);
			potCards.push_back(cardB);
			cout << playerB->getName() << " wins this round! Added " << potCards.size() << " cards to " << playerA->getName() << "'s hand." << endl;
			playerA->addCards(potCards);
			potCards.clear();
		}
		else {
			cout << "This round is a draw" << endl;
			potCards.push_back(cardA);
			potCards.push_back(cardB);
		}
		cout << "===========================================================" << endl;
		cout << "\n\n" << endl;
	}

	cout << playerA->getName() << " " << (playerA->hasEmptyHand() ? "Wins the game" :"Loses the game") << endl;
	cout << playerB->getName() << " " << ((playerB->hasEmptyHand() == 1) ? "Wins the game" : "Loses the game") << endl;

}

