#!/usr/bin/python

import argparse

def find_max_profit(prices):
  lowest_price = float('inf')
  lowest_price_index = 0
  max_price = float('-inf')

  for i in range(0,len(prices) - 1):
    if prices[i] < lowest_price:
      lowest_price = prices[i]
      lowest_price_index = i

  for j in range(lowest_price_index + 1, len(prices)):
    if prices[j] > max_price:
      max_price = prices[j]
      
  return max_price - lowest_price

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))