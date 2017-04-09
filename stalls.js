/* Large test case failed */

const solve = require('code-jam').solve;
const BigNumber = require('bignumber.js');

solve(input => {
    const stalls = new BigNumber(input.readWord());
    const people = new BigNumber(input.readWord());

    const log = Math.floor(Math.log2(people));
    const maxAtK = Math.floor(stalls/Math.pow(2, log));

    let prev = stalls;
    let lastMax = stalls;

    let prevOddCount = new BigNumber(0);
    let prevEvenCount = new BigNumber(0);
    if (stalls.modulo(2) == 0) {
        prevEvenCount = new BigNumber(1);
    } else {
        prevOddCount = new BigNumber(1);
    }

    while(lastMax.greaterThan(maxAtK)) {
        let oddCount, evenCount;

        const max = prev.dividedBy(2).floor();
        const min = max.minus(1);

        if (lastMax.modulo(2) == 0) {
            if (max.modulo(2) == 0) {
                evenCount = prevEvenCount;
                oddCount = prevEvenCount.plus(prevOddCount.times(2));
            } else {
                oddCount = prevEvenCount;
                evenCount = prevEvenCount.plus(prevOddCount.times(2));
            }
        } else {
            if (max.modulo(2) == 0) {
                evenCount = prevOddCount.times(2).plus(prevEvenCount);
                oddCount = prevEvenCount;
            } else {
                oddCount = prevOddCount.times(2).plus(prevEvenCount);
                evenCount = prevEvenCount;
            }
        }

        prevEvenCount = evenCount;
        prevOddCount = oddCount;

        lastMax = max;
        prev = prev.dividedBy(2);
    }

    let currentMax = prev.dividedBy(2).floor();
    let currentMin = currentMax.minus(1);

    if (currentMax.isZero()) {
        currentMin = 0;
    }
    
    let firstK = stalls.dividedBy(prev);
    let diff = people.minus(firstK);

    console.log(currentMax.toString(), currentMin.toString(), lastMax.toString());

    if (lastMax.modulo(2) == 0) {
        if (diff.lessThan(prevEvenCount)) {
            return (currentMax.toString() + " " + currentMin.toString());
        } else {
            return (currentMin.toString() + " " + currentMin.toString());
        }
    } else {
        if (diff.lessThan(prevOddCount)) {
            return (currentMax.toString() + " " + currentMax.toString());
        } else {
            return (currentMax.toString() + " " + currentMin.toString());
        }
    }
});