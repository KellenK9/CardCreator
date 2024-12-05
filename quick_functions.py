import csv


class QuickFunctions:
    def sum_csv(csv_path):
        # Read the CSV file and calculate the sum of the 3rd column
        with open(csv_path, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            sum_arr = [0, 0, 0, 0]
            for row in rows:
                if row[0] != "Card Name" and row[0] != "Deck Totals":
                    sum_arr[0] += float(row[2])
                    sum_arr[1] += float(row[3])
                    sum_arr[2] += float(row[4])
                    sum_arr[3] += float(row[5])

        # Append the sum as a new row and overwrite the file
        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Write the original data excluding the final row
            writer.writerows(rows[:-1])

            # Append the sum as a new row
            writer.writerow(
                ["Deck Totals", "", sum_arr[0], sum_arr[1], sum_arr[2], sum_arr[3]]
            )


QuickFunctions.sum_csv("starter_decks.csv")
