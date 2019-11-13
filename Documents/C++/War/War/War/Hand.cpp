#include "pch.h"
#include "Hand.h"
#include <iostream>

using namespace std;

Hand::Hand(vector<Card>& hand)
{
	this->hand = hand;
}

Hand::Hand() {}

Hand::~Hand()
{
}

vector<Card> Hand::getHand() {
	return this->hand;
}

Card Hand::getCard() {
	Card c = hand.back();
	hand.pop_back();
	return c;
}

void Hand::addCard(Card& c) {
	hand.push_back(c);
}

bool Hand::isEmpty() {
	return hand.empty();
}
