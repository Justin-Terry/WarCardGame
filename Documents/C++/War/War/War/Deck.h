#pragma once
#include <stack>
#include "Card.h"

using namespace std;

class Deck
{
public:
	Deck();
	~Deck();
	Card getNext();
	void setupDeck(stack<Card>&);
private:
	stack<Card> theDeck;
};

