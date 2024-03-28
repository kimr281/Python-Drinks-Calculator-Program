import valid as v
#******************************************************************************
# Author:           Kimberly Rodriguez
# Title:            Drinks Calculator Program
# Date:             03/27/2024
# Description:      This is a program to calculate the amount of cases
#                   of a drink you'll need to buy to serve people at a party.
#                   This program takes into account the amount of drinks you
#                   want each person to have.
#******************************************************************************
def main():
  drink = ''
  people = 0
  bottles_per_case = 0
  servings = 0
  num_boxes = 0
  
  print_welcome()

  #gets the user input
  drink = get_drink()
  people = get_num_people()
  bottles_per_case = get_bottles_per_case()
  servings = get_servings(drink)

  #calculates the number of boxes needed
  num_boxes = calc_num_boxes(people, servings, bottles_per_case)

  print_end(num_boxes, drink)


def print_welcome():
  """
  Prints a welcome message to the user
  :param: none
  :return: none
  """
  print("Welcome to the drink calculator program!\n")
  print("This program will help you determine"
        + " how many cases of drinks you need to buy for a party.\n")


def get_drink():
  """
  Prompts the user for the name of the drink
  :param: none
  :return: drink as a string
  """
  drink = ''
  drink = input("What drink are you planning on buying? ")
  while drink == '':
    print("Please enter a drink name.")
    drink = input("\nWhat drink are you planning on buying? ")
  return drink


def get_num_people():
  """
  Prompts the user for the number of people attending the party
  :param: none
  :return: people as an integer
  """
  people = 0
  people = v.get_integer("\nEnter the number of people attending the party: ")
  while people <= 0:
    print("Please enter a number greater than zero.")
    people = v.get_integer("\nEnter the number of people"
                           + " attending the party: ")
  return people


def get_bottles_per_case():
  """
  Prompts the user for the number of bottles per case
  :param: none
  :return: bottles_per_case as an integer
  """
  bottles_per_case = 0
  bottles_per_case = v.get_integer("Enter the number of bottles per case: ")
  while bottles_per_case < 1:
    print("Please enter a number greater than 0.")
    bottles_per_case = v.get_integer("\nEnter the number of bottles per case: ")
  return bottles_per_case


def get_servings(drink):
  """
  Prompts the user for the number of servings per bottle
  :param drink: string, name of drink
  :return: servings as an integer
  """
  servings = 0
  servings = v.get_integer("Enter the desired number"
                           + f" of {drink} per person: ")
  while servings < 1:
    print("Please enter a number greater than 0.")
    servings = v.get_integer("\nEnter the desired number"
                             + f" of {drink} per person: ")
  return servings


def calc_num_boxes(people, servings, bottles_per_case):
  """
  Calculates the number of boxes needed
  :param people: integer, number of people attending party
  :param servings: integer, number of servings per person
  :param bottles_per_case: integer, number of bottles per case
  :return: num_boxes as an integer
  """
  total_bottles_needed = people * servings
  num_boxes = total_bottles_needed // bottles_per_case
  #if there are any bottles left over, add an additional box
  if total_bottles_needed % bottles_per_case != 0:
     num_boxes += 1
  return num_boxes


def print_end(num_boxes, drink):
  """
  Prints the number of boxes needed
  :param num_boxes: integer, number of boxes needed
  :param drink: string, name of drink
  :return: none
  """
  print(f"\nYou will need {num_boxes} case(s) of {drink}."
        + " Thank you for using the drink calculator program!")
  

main()