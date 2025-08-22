import csv


class QuickFunctions:

    def sum_csv(csv_path):
        # Read the CSV file and calculate the sum of the 3rd-6th columns, skipping headings
        with open(csv_path, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        sum_arr = [0, 0, 0, 0]
        new_rows = []
        deck_totals_found = False
        for row in rows:
            if not row or row[0].startswith("//") or row[0] == "Card Name":
                new_rows.append(row)
                continue
            if row[0] == "Deck Totals":
                deck_totals_found = True
                continue  # skip old Deck Totals row
            # Only sum if columns 2-5 are present and are numbers
            try:
                sum_arr[0] += int(row[2]) if row[2] else 0
                sum_arr[1] += int(row[3]) if row[3] else 0
                sum_arr[2] += int(row[4]) if row[4] else 0
                sum_arr[3] += int(row[5]) if row[5] else 0
            except (IndexError, ValueError):
                pass
            new_rows.append(row)

        # Write the new data and append Deck Totals row
        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
            writer.writerow(
                ["Deck Totals", "", sum_arr[0], sum_arr[1], sum_arr[2], sum_arr[3]]
            )


QuickFunctions.sum_csv("starter_decks.csv")
