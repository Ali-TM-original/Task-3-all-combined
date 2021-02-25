"""
    Tabulate for Table formed data
    IMPORTED TIME TO MAKE IT REAL NOT GETTING PAID ENOUGH SO SKIPPED 
    Complete

    > Assuming Total money always starts with 0
    > Assuming up and down tickets always start from 480 or 640
"""

from tabulate import tabulate

UP_TIME = ['9:00', '11:00', '13:00', '15:00']
UP_TICKET = [480, 480, 480, 480]

DOWN_TIME = ['10:00', '12:00', '14:00', '16:00']
DOWN_TICKET = [480, 480, 480, 640]

UP_PASSENGERS = [0, 0, 0, 0]
DOWN_PASSENGERS = [0, 0, 0, 0]

TOTAL_MONEY = [0, 0, 0, 0]
TOTAL_PASSANGERS_ = [0, 0, 0, 0]


def main_tabel():
    headers = [
        "Up Time", "Down Time", "Up Tickets", "Down Tickets", "Up Passenger",
        "Down Passenger", "Money"
    ]

    MAIN_TABLE = list(
        zip(UP_TIME, DOWN_TIME, UP_TICKET, DOWN_TICKET, UP_PASSENGERS,
            DOWN_PASSENGERS, TOTAL_MONEY))

    print(tabulate(MAIN_TABLE, headers, tablefmt="fancy_grid"))


def final_table():
    headers = ["Total Passanger", "Total Money"]
    MAIN_TABLE = list(zip(TOTAL_PASSANGERS_, TOTAL_MONEY))
    print(tabulate(MAIN_TABLE, headers, tablefmt="fancy_grid"))


def free_ticket(num):
    if 10 <= num <= 80:
        ticket = round(num / 10)
        return int(ticket)
    else:
        return int(0)


y = True
X = True
while X:
    while y:
        try:
            Tickets = int(input('ENTER NUMBER OF TICKETS: '))
            y = False
        except ValueError:
            print("Please enter integre values only")
            y = True
    Departure = input('Enter departure time: ')
    if Departure == "dev":
        count = 0
        ttl_money = 0
        for i in range(0, 4):
            TOTAL_PASSANGERS_[i] = DOWN_PASSENGERS[i] + UP_PASSENGERS[i]
        for money in TOTAL_MONEY:
            ttl_money += int(money)

        journey = TOTAL_PASSANGERS_.index(max(TOTAL_PASSANGERS_))
        final_journey = journey + 1
        passangers = max(TOTAL_PASSANGERS_)

        final_table()
        print(
            f"Journey {final_journey} had the highest number of passangers: {passangers}"
        )
        print(f"Total Money taken for the day is {ttl_money}")

        X = False
        break
    else:
        pass
    count = 0
    if Departure in UP_TIME:
        index = UP_TIME.index(Departure)
        x_tickets = free_ticket(Tickets)
        total_tickets = Tickets + x_tickets
        if UP_TICKET[index] >= total_tickets:
            print(f'Ticket is available do you want to buy?\n'
                  f'You will get {x_tickets} for free')

            buy = input('Enter Y/N or Yes/No: ')
            if buy.lower() == 'y' or buy.lower() == 'yes':
                cost = int(Tickets) * 25
                if x_tickets != 0:
                    cost = int(Tickets) * 25
                    total_cost = int(cost)
                    TOTAL_MONEY[index] += total_cost
                    UP_PASSENGERS[index] += x_tickets + Tickets
                    UP_TICKET[index] -= UP_PASSENGERS[index]
                    print(
                        f'Please Pay {total_cost} at the counter to confirm your booking'
                    )
                    main_tabel()
                    y = True
                else:
                    total_cost = int(Tickets) * 25
                    TOTAL_MONEY[index] += total_cost
                    UP_PASSENGERS[index] += Tickets
                    UP_TICKET[index] -= UP_PASSENGERS[index]
                    print(
                        f'Please pay {total_cost} at the counter to confirm your booking'
                    )
                    main_tabel()
                    y = True
            elif buy.lower() == 'n' or buy.lower() == 'no':
                print('Thank you for using this service!')
                main_tabel()
                y = True

        else:
            print("The number of tickets are not available")
            main_tabel()
            y = True

    elif Departure in DOWN_TIME:
        index = DOWN_TIME.index(Departure)
        x_tickets = free_ticket(Tickets)
        total_tickets = Tickets + x_tickets
        if DOWN_TICKET[index] >= total_tickets:
            print(f'Tickets are available do you want to buy?\n'
                  f'You will get {x_tickets} Tickets for free')

            buy = input('Enter Y/N or Yes/No: ')
            if buy.lower() == 'y' or buy.lower() == 'yes':
                cost = int(Tickets) * 25
                if x_tickets != 0:
                    tik = free_ticket(Tickets) * 25
                    cost = int(Tickets) * 25
                    total_cost = int(tik) + int(cost)
                    TOTAL_MONEY[index] += total_cost
                    DOWN_PASSENGERS[index] += x_tickets + Tickets
                    DOWN_TICKET[index] -= DOWN_PASSENGERS[index]
                    print(
                        f'Please Pay {total_cost} at the counter to confirm your booking'
                    )
                    main_tabel()
                    y = True
                else:
                    total_cost = int(Tickets) * 25
                    TOTAL_MONEY[index] += total_cost
                    DOWN_PASSENGERS[index] += Tickets
                    DOWN_TICKET[index] -= DOWN_PASSENGERS[index]
                    print(
                        f'Please pay {total_cost} at the counter to confirm your booking'
                    )
                    main_tabel()
                    y = True

            elif buy.lower() == 'n' or buy.lower() == 'no':
                print('Thank you for using this service!')
                main_tabel()
                y = True

        else:
            print('The number of tickets are not available')
            main_tabel()
            y = True

    else:
        print('Train not avail at this time')
        main_tabel()
        y = True
"""
    ALI™ FINALIZE EVERYTHIN
    FIX DAT ISSUE IF YOU READ THIS
"""
