
const solve = require('code-jam').solve;

const fromLeft = (sequence) => {
	for (let i = 0; i < sequence.length; i++) {
		if (sequence[i] == "-") {
			return i;
		}
	}
	return -1;
}

const fromRight = (sequence) => {
	for (let i = sequence.length - 1; i >= 0; i--) {
		if (sequence[i] == "-") {
			return sequence.length - 1 - i;
		}
	}
	return -1;
}

const flipLeft = (sequence, pos, k) => {
	let s = sequence.slice();
	for (let i = 0; i < k; i++) {
		if (s[pos + i] == "+") {
			s = s.substr(0, pos + i) + "-" + s.substr(pos + i + 1);
		} else {
			s = s.substr(0, pos + i) + "+" + s.substr(pos + i + 1);
		}
	}

	return s;
}

const flipRight = (sequence, pos, k) => {
	let s = sequence.slice();
	for (let i = 0; i < k; i++) {
		const index = sequence.length - 1 - pos - i;
		if (s[index] == "+") {
			s = s.substr(0, index) + "-" + s.substr(index + 1);
		} else {
			s = s.substr(0, index) + "+" + s.substr(index + 1);
		}
	}

	return s;
}

solve(input => {
  let sequence = input.readWord();
	const k = input.readNumber();

	let count = 0;

	while (count < 1000) {
		const left = fromLeft(sequence);
		const right = fromRight(sequence);

		if (left == -1 && right == -1) {
			return count;
		}

		if (left <= right) {
			sequence = flipLeft(sequence, left, k);
		} else {
			sequence = flipRight(sequence, right, k);
		}

		count++;
	}

	return "IMPOSSIBLE";
});