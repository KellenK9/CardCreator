import csv


class QuickFunctions:
    def sum_csv(csv_path):
        # Read the CSV file and calculate the sum of the 3rd column
        with open(csv_path, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            sum_arr = [0, 0, 0, 0]

            # Skip the header if it exists
            for row in rows:
                if row[0] != "Card Name" and row[0] != "Deck Totals":
                    sum_arr[0] += float(row[2])

        # Append the sum as a new row and overwrite the file
        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Write the original data
            writer.writerows(rows)

            # Append the sum as a new row
            writer.writerow(["", "", f"Sum: {column_sum}"])


QuickFunctions.sum_csv("starter_decks.csv")
