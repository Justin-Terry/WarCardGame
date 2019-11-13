#pragma once
#include "Hand.h"
#include "Card.h"
#include <string>
#include <vector>

using namespace std;
class Player
{
public:
	Player(string, vector<Card>);
	~Player();
	Card getCard();
	string getName();
	bool hasEmptyHand();
	void addCards(vector<Card>);
private:
	string name;
	Hand hand;
};

