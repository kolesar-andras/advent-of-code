import { expect, test } from "bun:test";
import { findNumbers, isAdjacentToSymbols } from "./lib.ts"

test("two numbers", () => {
  expect(findNumbers("467..114..")).toEqual([
    {
      digits: "467",
      start: 0,
      end: 2,
    },
    {
      digits: "114",
      start: 5,
      end: 7,
    }
  ])
})

test("numbers at end", () => {
  expect(findNumbers("467")).toEqual([
    {
      digits: "467",
      start: 0,
      end: 2,
    }
  ])
})

test("adjacent to symbol", () => {
  expect(isAdjacentToSymbols(
    {
      digits: "467",
      start: 0,
      end: 2
    },
    [
      {
        char: "*",
        position: 3
      }
    ]
  )).toBeTruthy()

  expect(isAdjacentToSymbols(
    {
      digits: "467",
      start: 0,
      end: 2
    },
    [
      {
        char: "*",
        position: 4
      }
    ]
  )).toBeFalsy()
})
