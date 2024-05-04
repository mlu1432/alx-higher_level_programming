#!/usr/bin/node

class Rectangle
{
	constructor(w, h)
	{
		// Check if width and height are positive integers greater than 0
		if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0)
		{
			this.width = w;
			this.height = h;
		}
	}
}

module.exports = Rectangle;
