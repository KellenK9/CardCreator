import csv


class QuickFunctions:
    def sum_csv(csv_path):
        # Read the CSV file and calculate the sum of the 3rd column
        with open(csv_path, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            # Skip the header if it exists
            for row in rows[1:]:
                column_sum += float(row[2])  # Convert the 3rd column value to float

        # Append the sum as a new row and overwrite the file
        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Write the original data
            writer.writerows(rows)

            # Append the sum as a new row
            writer.writerow(["", "", f"Sum: {column_sum}"])


QuickFunctions.sum_csv("starter_decks.csv")
