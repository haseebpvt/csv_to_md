#!/usr/bin/env python3

"""
Streamlit web interface for CSV to Markdown converter.
Allows users to upload a CSV file and view/download the markdown output.
"""

import streamlit as st
import csv
import io
from pathlib import Path

def convert_csv_to_markdown(csv_file, filename: str) -> str:
    """
    Converts uploaded CSV file to structured Markdown format.
    
    Args:
        csv_file: The uploaded file object (BytesIO from Streamlit)
        filename: Original filename (for the title)
    
    Returns:
        str: The markdown formatted string
    """
    try:
        # Read the CSV content
        content = csv_file.read().decode('utf-8')
        csv_reader = csv.DictReader(io.StringIO(content), skipinitialspace=True)
        
        # Get headers
        headers = csv_reader.fieldnames
        if not headers:
            return "Error: CSV file is empty or has no header row."
        
        # Build markdown string
        markdown_lines = []
        
        # Add title based on filename (without extension)
        file_stem = Path(filename).stem
        markdown_lines.append(f"### {file_stem}\n")
        
        # Process each row
        for i, row in enumerate(csv_reader):
            if i > 0:
                # Add horizontal rule to separate entries
                markdown_lines.append("\n---\n")
            
            # Write each key-value pair with markdown line breaks (two spaces at end)
            for header in headers:
                key = header.strip()
                value = row[header].strip()
                markdown_lines.append(f"{key}: {value}  ")  # Two spaces for markdown line break
        
        return "\n".join(markdown_lines)
    
    except Exception as e:
        return f"Error processing CSV file: {str(e)}"

def main():
    """
    Main Streamlit application.
    """
    # Page configuration
    st.set_page_config(
        page_title="CSV to Markdown Converter",
        page_icon="📄",
        layout="centered"
    )
    
    # Header
    st.title("📄 CSV to Markdown Converter")
    st.markdown("""
    Upload your CSV file and instantly convert it to structured Markdown format.
    Each row becomes a block of key-value pairs.
    """)
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Drop your CSV file here or click to browse",
        type=["csv"],
        help="Upload a CSV file to convert it to Markdown format"
    )
    
    if uploaded_file is not None:
        # Show file details
        st.success(f"✅ File uploaded: **{uploaded_file.name}**")
        
        # Auto-convert when file is uploaded or changed
        current_filename = Path(uploaded_file.name).stem
        
        # Check if this is a new file or if we need to reconvert
        if 'filename' not in st.session_state or st.session_state['filename'] != current_filename:
            with st.spinner("Converting..."):
                # Convert CSV to Markdown
                markdown_content = convert_csv_to_markdown(uploaded_file, uploaded_file.name)
                
                # Store in session state
                st.session_state['markdown_content'] = markdown_content
                st.session_state['filename'] = current_filename
        
        # Display results
        if 'markdown_content' in st.session_state:
            st.markdown("---")
            
            # Create columns for preview title and action buttons
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📋 Markdown Preview")
            
            with col2:
                # Download button
                st.download_button(
                    label="⬇️ Download",
                    data=st.session_state['markdown_content'],
                    file_name=f"{st.session_state['filename']}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            
            # Copyable code block with built-in copy button
            st.markdown("**📋 Click the copy icon to copy markdown:**")
            st.code(st.session_state['markdown_content'], language=None, line_numbers=False)
            
            # Show the rendered markdown preview
            st.markdown("**👁️ Rendered Preview:**")
            with st.container(border=True):
                st.markdown(st.session_state['markdown_content'])
    
    else:
        # Instructions when no file is uploaded
        st.info("👆 Please upload a CSV file to get started")
        
        # Example format
        with st.expander("ℹ️ See Expected CSV Format"):
            st.markdown("""
            Your CSV should have a header row with column names. For example:
            
            ```
            Name,Email,Age,City
            John Doe,john@example.com,30,New York
            Jane Smith,jane@example.com,25,Los Angeles
            ```
            
            Will be converted to:
            
            ```markdown
            ### filename
            
            Name: John Doe
            Email: john@example.com
            Age: 30
            City: New York
            
            ---
            
            Name: Jane Smith
            Email: jane@example.com
            Age: 25
            City: Los Angeles
            ```
            """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

