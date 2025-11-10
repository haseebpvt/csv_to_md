#!/usr/bin/env python3

"""
Converts a CSV file into a structured Markdown file, where each
row is represented as a block of key-value pairs.

This script is an alternative to converting a CSV into a Markdown table.

Usage:
    python csv_to_structured_md.py <input_file.csv>
    python csv_to_structured_md.py <input_file.csv> -o ./output/directory
"""

import csv
import argparse
import sys
from pathlib import Path

def convert_csv_to_md(input_path: Path, output_path: Path):
    """
    Reads the CSV file from input_path and writes the structured
    Markdown file to output_path.
    """
    try:
        with input_path.open(mode='r', encoding='utf-8', newline='') as infile:
            # Use DictReader to automatically use the first row as keys
            # skipinitialspace=True handles potential spaces after commas
            reader = csv.DictReader(infile, skipinitialspace=True)
            
            # Get the header names from the reader
            headers = reader.fieldnames
            if not headers:
                print(f"Error: CSV file '{input_path}' is empty or has no header row.", file=sys.stderr)
                return False

            with output_path.open(mode='w', encoding='utf-8') as outfile:
                # Write a title (H3) based on the input filename (without extension)
                outfile.write(f"### {input_path.stem}\n\n")
                
                # Process each row in the CSV
                for i, row in enumerate(reader):
                    if i > 0:
                        # Add a horizontal rule to separate entries
                        outfile.write("\n---\n\n")
                    
                    # Write each key-value pair from the row
                    # We loop through `headers` to maintain the original column order
                    for header in headers:
                        # .strip() cleans up any leading/trailing whitespace
                        key = header.strip()
                        value = row[header].strip()
                        
                        outfile.write(f"{key}: {value}\n")
        
        return True

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied. Could not read '{input_path}' or write to '{output_path}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Parses command-line arguments and orchestrates the conversion.
    """
    parser = argparse.ArgumentParser(
        description="Convert a CSV file to a structured Markdown file (not a table).",
        epilog="Example: python %(prog)s my_data.csv -o ./docs"
    )
    
    # Required positional argument for the input file
    parser.add_argument(
        "input_file",
        type=str,
        help="The path to the input CSV file."
    )
    
    # Optional argument for the output directory
    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        help="Optional. The directory to save the output .md file. "
             "Defaults to the same directory as the input file."
    )
    
    args = parser.parse_args()
    
    # --- 1. Set up file paths ---
    input_path = Path(args.input_file)
    
    # Validate input file
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    if not input_path.is_file():
        print(f"Error: Input path is not a file: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
        # Create output directory if it doesn't exist
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            print(f"Error: Could not create output directory: {output_dir}. Permission denied.", file=sys.stderr)
            sys.exit(1)
    else:
        # Default to the input file's parent directory
        output_dir = input_path.parent
        
    # Create the final output path
    # output_filename will be, e.g., "my_data.md"
    output_filename = f"{input_path.stem}.md"
    output_path = output_dir / output_filename
    
    # --- 2. Run the conversion ---
    print(f"Converting '{input_path}'...")
    success = convert_csv_to_md(input_path, output_path)
    
    if success:
        print(f"Successfully saved to '{output_path}'")

if __name__ == "__main__":
    main()