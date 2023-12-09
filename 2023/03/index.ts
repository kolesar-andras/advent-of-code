import { PartNumberParser, GearRatioParser, NumberFound, findNumbersAndSymbols } from "./lib"

let sumPartNumber: number = 0
let sumGearRatio: number = 0
const partNumberParser = new PartNumberParser(
    function(number: NumberFound) {
        sumPartNumber += parseInt(number.digits)
    }
)
const gearRatioParser = new GearRatioParser(
    function(numbers: NumberFound[]) {
        sumGearRatio += numbers.reduce((accumulator, number) => accumulator * parseInt(number.digits), 1)
    }
)
for await (const string of console) {
    const line = findNumbersAndSymbols(string)
    partNumberParser.parse(line)
    gearRatioParser.parse(line)
}
console.log(sumPartNumber)
console.log(sumGearRatio)
