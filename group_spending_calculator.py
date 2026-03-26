def split_expenses():
    n = int(input("Enter number of people: "))
    people = []

    print("Enter names:")
    for _ in range(n):
        name = input().strip().lower()
        people.append(name)

    # balance dictionary
    balance = {person: 0 for person in people}

    print("\nCommands:")
    print("Type 'next' to add next transaction")
    print("Type 'done' to finish and see result\n")

    while True:
        payer = input("\nWho paid? (or 'done'): ").strip().lower()

        if payer == "done":
            break

        if payer not in people:
            print("Invalid name")
            continue

        amount = float(input("Amount paid: "))

        split_type = input("Split among (all / specific): ").strip().lower()

        if split_type == "all":
            split_people = people
        else:
            print("Enter names separated by space:")
            split_people = input().strip().lower().split()

        share = amount / len(split_people)

        # update balances
        for person in split_people:
            balance[person] -= share

        balance[payer] += amount

        cmd = input("Type 'next' to continue or 'done': ").strip().lower()
        if cmd == "done":
            break

    return balance


def settle_balances(balance):
    creditors = []
    debtors = []

    for person, amt in balance.items():
        if amt > 0:
            creditors.append([person, amt])
        elif amt < 0:
            debtors.append([person, -amt])

    print("\n--- Final Settlement ---")

    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor, d_amt = debtors[i]
        creditor, c_amt = creditors[j]

        settle_amt = min(d_amt, c_amt)

        print(f"{debtor} pays {settle_amt:.2f} to {creditor}")

        debtors[i][1] -= settle_amt
        creditors[j][1] -= settle_amt

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1


# run
balances = split_expenses()
print("\nBalances:", balances)
settle_balances(balances)