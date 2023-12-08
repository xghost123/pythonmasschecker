# Function to extract and reformat the lines
def extract_and_reformat(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    smtp_config = []
    smtp_config_found = False

    with open(output_file_path, 'w') as output_file:
        for line in lines:
            if line.startswith("URL="):
                if smtp_config_found:
                    formatted_data = "|".join(smtp_config)
                    output_file.write(formatted_data + "\n")
                smtp_config = []
                smtp_config_found = False
            elif line.startswith("Server=") or line.startswith("Port=") or line.startswith("User=") or line.startswith("Password="):
                key, value = line.split("=")[0].strip(), line.split("=")[1].strip()
                if key in ["Server", "Port", "User", "Password"]:
                    smtp_config.append(value)
                    smtp_config_found = True

        if smtp_config_found:
            formatted_data = "|".join(smtp_config)
            output_file.write(formatted_data + "\n")

if __name__ == "__main__":
    input_file_path = "all_smtps.txt"
    output_file_path = "output.txt"
    extract_and_reformat(input_file_path, output_file_path)
