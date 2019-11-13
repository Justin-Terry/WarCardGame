#include "pch.h"
#include "Player.h"
#include <iostream>

using namespace std;

Player::Player(string name, vector<Card> h)
{
	this->name = name;
	this->hand = Hand(h);

}

Player::~Player()
{
}

string Player::getName() {
	return this->name;
}

bool Player::hasEmptyHand() {
	return this->hand.isEmpty();
}

void Player::addCards(vector<Card> cards) {
	for (Card c : cards) {
		this->hand.addCard(c);
	}
}

Card Player::getCard() {
	return this->hand.getCard();
}
