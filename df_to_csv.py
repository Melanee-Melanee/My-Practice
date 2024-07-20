# import os
# import pandas as pd

# def list_files_in_directory(directory_path, output_csv):
#     # Get a list of files in the directory
#     files = os.listdir(directory_path)
    
#     # Create a DataFrame from the list of files
#     df = pd.DataFrame(files, columns=['Filename'])
    
#     # Save the DataFrame to a CSV file
#     df.to_csv(output_csv, index=False)
    
# # Define the directory path and output CSV file
# directory_path = '/home/melanee/Downloads/DPd/train'
# output_csv = 'labels.csv'

# # Run the function
# list_files_in_directory(directory_path, output_csv)



import os
import pandas as pd

def list_files_in_directory(directory_path, output_csv):
    # Get a list of files in the directory
    files = os.listdir(directory_path)
    
    # Filter out non-image files (optional, e.g., only include .jpg, .png, etc.)
    image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
    
    # Create a DataFrame with two columns: 'Filename' and 'Word'
    df = pd.DataFrame(image_files, columns=['filename'])
    df['words'] = df['filename'].apply(lambda x: os.path.splitext(x)[0] + ' :')
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)

# Define the directory path and output CSV file
directory_path = '/home/melanee/Downloads/DPd/train'
output_csv = 'labels.csv'

# Run the function
list_files_in_directory(directory_path, output_csv)

