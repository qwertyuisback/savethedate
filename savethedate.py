import pandas as pd
def save_the_data(file_path):
    try:
        event_list = pd.read_csv(file_path,delimiter=";",encoding="utf-8")
        print(f"Data loaded successfully from {file_path}")
        print(event_list)
        return event_list
    except pd.errors.EmptyDataError:
        print(f"No data found in the file: {file_path}")
        return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
save_the_data("dates.csv")

def create_ics(data, file_name):
    try:
        with open(file_name, 'w',encoding="utf-8") as f:
            f.write("BEGIN:VCALENDAR\n")
            f.write("VERSION:2.0\n")
            f.write(f"PRODID:-//Your Organization//Your Calendar//EN\n")
            f.write("CALSCALE:GREGORIAN\n")
            f.write("METHOD:PUBLISH\n")
            f.write("\n")

            for column in data.columns:
                if column not in ['Name', 'DTSTART', 'DTEND']:
                    raise ValueError(f"Invalid column name: {column}. Expected 'Name', 'DTSTART', and 'DTEND'.")
                else:
                    for index, row in data.iterrows():
                        f.write("BEGIN:VEVENT\n")
                        # f.write("UID:" + str(index) + "\n")
                        f.write("DTSTAMP:" + pd.Timestamp.now().strftime('%Y%m%dT'+'000000Z') + "\n")

                        f.write(f"SUMMARY:{row['Name']}\n")
                        f.write(f"DTSTART:{row['DTSTART']}\n")
                        f.write(f"DTEND:{row['DTEND']}\n")

                        # "reminder alerts for 1 day, 12 hours, 2 hours, and 5 minutes"
                        f.write(f"DESCRIPTION:\n")
                        f.write(f"BEGIN:VALARM\n")
                        f.write(f"ACTION:DISPLAY\n")
                        f.write(f"DESCRIPTION:Reminder\n")
                        f.write(f"TRIGGER:-PT5M\n")
                        f.write(f"END:VALARM\n")
                        f.write(f"BEGIN:VALARM\n")
                        f.write(f"ACTION:DISPLAY\n")
                        f.write(f"DESCRIPTION:Reminder\n")
                        f.write(f"TRIGGER:-PT2H\n")
                        f.write(f"END:VALARM\n")
                        f.write(f"BEGIN:VALARM\n")
                        f.write(f"ACTION:DISPLAY\n")
                        f.write(f"DESCRIPTION:Reminder\n")
                        f.write(f"TRIGGER:-PT12H\n")
                        f.write(f"END:VALARM\n")
                        f.write(f"BEGIN:VALARM\n")
                        f.write(f"ACTION:DISPLAY\n")
                        f.write(f"DESCRIPTION:Reminder\n")
                        f.write(f"TRIGGER:-P1D\n")
                        f.write(f"END:VALARM\n")
                        f.write("TRANSP:OPAQUE\n")
                        f.write("END:VEVENT\n")
                        f.write("\n")
                        print("Event ",row['Name']," is created successfully.")
                    f.write("END:VCALENDAR\n")
                    break
        print(f"ICS file '{file_name}' has been created successfully.")
    except Exception as e:
        print(f"Error creating ICS file: {e}")
    finally:
        print("Function create_ics finished execution.")


# save_the_data("dates.csv")
create_ics(save_the_data("dates.csv"), "savethedate.ics")
