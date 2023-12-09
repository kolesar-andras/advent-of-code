export class NumberFound {
    digits: string
    start: number
    end: number
}

export class SymbolFound {
    char: string
    position: number
}

export class Line {
    numbers: NumberFound[] = []
    symbols: SymbolFound[] = []
}

export function findNumbersAndSymbols(string: string) {
    let line = new Line
    line.numbers = findNumbers(string)
    line.symbols = findSymbols(string)
    return line
}

export function findNumbers(string: string): NumberFound[] {
    let current: NumberFound | null = null
    let numbers: NumberFound[] = []
    let index = 0
    function closeCurrent() {
        if (current) {
            current.end = index-1
            numbers.push(current)
            current = null
        }
    }
    for (const char of string) {
        if (isDigit(char)) {
            if (!current) {
                current = new NumberFound
                current.start = index
            }
            current.digits = current.digits?.concat(char) ?? char
        } else {
            if (current) {
                closeCurrent()
            }
        }
        index++
    }
    closeCurrent()
    return numbers
}

function findSymbols(string: string): SymbolFound[] {
    let index = 0
    let symbols: SymbolFound[] = []
    for (const char of string) {
        if (!isDot(char) && !isDigit(char)) {
            const symbol = new SymbolFound
            symbol.char = char
            symbol.position = index
            symbols.push(symbol)
        }
        index++
    }
    return symbols
}

function isDigit(c: string) {
    return typeof c === 'string' && c.length == 1 && c >= '0' && c <= '9'
}

function isDot(c: string) {
    return c === '.'
}

export function isAdjacent(number: NumberFound, symbol: SymbolFound): boolean {
    return symbol.position >= number.start-1 && symbol.position <= number.end+1
}

export function isAdjacentToSymbols(number: NumberFound, symbols: SymbolFound[]): boolean {
    return symbols.some(symbol => isAdjacent(number, symbol))
}

export function getAdjacentNumbers(symbol: SymbolFound, numbers: NumberFound[]): NumberFound[] {
    return numbers.filter(number => isAdjacent(number, symbol))
}

export class PartNumberParser {
    last: Line | null = null
    callback: (number: NumberFound) => void

    constructor (callback: (number: NumberFound) => void) {
        this.callback = callback
    }

    parse(line: Line) {
        if (this.last) {
            this.last.numbers.forEach(number => {
                if (isAdjacentToSymbols(number, line.symbols)) {
                    this.callback(number)
                }
            })
        }
        line.numbers = line.numbers.filter(number => {
            return ![this.last?.symbols, line.symbols].some(symbols => {
                if (symbols && isAdjacentToSymbols(number, symbols)) {
                    this.callback(number)
                }
            })
        })
        this.last = line
    }
}

export class Window {
    lines: Line[] = []
    static readonly size: number = 3
    add(line: Line): void {
        this.lines.push(line)
        this.lines = this.lines.slice(-Window.size)
    }
    get filled(): boolean {
        return this.lines.length >= Window.size
    }
    get center(): Line {
        return this.lines[1]
    }
    numbers(): NumberFound[] {
        return this.lines.reduce((accumulator: NumberFound[], line: Line) => accumulator.concat(line.numbers), [])
    }
}

/**
 * part two
 *
 * make sure parse mathod is called with empty line at end
 * this is fulfilled if input file has trailing newline
 */
export class GearRatioParser {
    window: Window = new Window
    callback: (numbers: NumberFound[]) => void

    constructor (callback: (numbers: NumberFound[]) => void) {
        this.callback = callback
    }

    parse(line: Line) {
        this.window.add(line)
        if (!this.window.filled) return
        this.window.center.symbols
            .filter(symbol => symbol.char === '*')
            .map(symbol => getAdjacentNumbers(symbol, this.window.numbers()))
            .filter(numbers => numbers.length == 2)
            .forEach(numbers => this.callback(numbers))
    }
}
