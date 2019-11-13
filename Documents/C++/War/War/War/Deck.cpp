#include "pch.h"
#include "Deck.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <time.h>

using namespace std;

Deck::Deck()
{
	setupDeck(theDeck);
}


Deck::~Deck()
{
}

void Deck::setupDeck(stack<Card>& deck) {
	vector<int> values;
	for (int i = 1; i < 14; i++) {
		values.push_back(i);
		values.push_back(i);
		values.push_back(i);
		values.push_back(i);
	}
	srand(time(0));
	random_shuffle(values.begin(), values.end());

	for (int i : values) {
		deck.push(Card(i));
	}
}

Card Deck::getNext() {
	Card c = theDeck.top();
	theDeck.pop();
	return c;
}
