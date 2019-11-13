#include "pch.h"
#include "Card.h"


Card::Card(int val)
{
	value = val;
}


Card::~Card()
{
}

int Card::getValue() {
	return value;
}
