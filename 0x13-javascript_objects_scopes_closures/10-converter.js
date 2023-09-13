#!/usr/bin/node

exports.converter = function (base) {
	return function to_string(number) {
		return number.toString(base);
	}
}
