#pragma once
#include "Card.h"
#include <vector>

using namespace std;

class Hand
{
public:
	Hand();
	Hand(vector<Card>&);
	~Hand();
	bool isEmpty();
	void addCard(Card&);
	Card getCard();
	vector<Card> getHand();

private:
	vector<Card> hand;
};

