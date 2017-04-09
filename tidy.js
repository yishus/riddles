const solve = require('code-jam').solve;

const transformArray = (array, pos) => {
	let arr = array.slice();
	arr[pos] = arr[pos] - 1;
	for (let i = pos + 1; i < arr.length; i++) {
		arr[i] = 9;
	}

	return arr;
};

solve(input => {
  const N = input.readWord();
	let digits = N.split("");
	let lastPosition = 0;
	while(lastPosition < digits.length - 1) {
		for (let i=0; i < digits.length; i++) {
			const left = digits[i];
			const right = digits[i + 1];
			lastPosition = i;
			if (left > right) {
				digits = transformArray(digits, i);
				break;
			}
		}
	}



	return digits.join('').replace(/^0+/, '');
});