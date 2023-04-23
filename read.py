def read_config(ip,filename):
    ip_list=set()
    try:
        with open(filename, 'r') as file:
            data = []
            
            # Loop through each line in the file
            for line in file:
                # Split the line into a list of values
                values = line.strip().split(',')
                print(values[0])
                ip_list.add(values[0])
                if values[0] ==ip:
                # Append the list of values to the data list
                    data.append(values)
            print(data)
        return data,ip_list
    except FileNotFoundError:
        print(f"Error: file {filename} not found.")