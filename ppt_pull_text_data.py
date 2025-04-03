import os

# Output file to store combined data
combined_file = "combined_text_data.txt"

# Open the combined file in append mode
with open(combined_file, "a", encoding="utf-8") as combined:
    # Loop through all .txt files that don't start with "done_"
    for txt_file in [f for f in os.listdir('.') if f.endswith('.txt') and not f.startswith('done_') and f != combined_file]:
        try:
            print(f"Appending contents from: {txt_file}")
            # Read content from the current file
            with open(txt_file, "r", encoding="utf-8") as current_file:
                combined.write(current_file.read())
                combined.write("\n")  # Add a newline between files

            # Rename the original file to indicate it has been processed
            os.rename(txt_file, "done_" + txt_file)
            print(f"Renamed '{txt_file}' to 'done_{txt_file}'")

        except Exception as e:
            print(f"Failed to process {txt_file}: {e}")
