import re
from pathlib import Path

file = 'emails.txt'

def write_to_file(data):
    out_file = file
    if Path(out_file).exists():
        with open(out_file, 'a') as f:
            for x in data: 
                f.write(f'{x}\n')
            f.write(f'--------------------------------\n')
    else:
        open(out_file, 'x')
        write_to_file(data)

def split_blob(blob, split=';'):
    return blob.split(split)

def get_emails(blob):
    emails = split_blob(blob)

    pattern_email_adres = "(?<=\<)(.*?)(?=\>)"
    pattern_email_name = "(.*?)(?<=\<)"
    
    names = []
    adresses = []
    no_email = []
    for email in emails:
        email = str(email.lstrip().rstrip())
        email_adres = re.search(pattern_email_adres, email)
        email_name = re.search(pattern_email_name, email)
        if email_adres != None:
            adresses.append(email_adres.group(0))
        if email_name != None:
            names.append(email_name.group(0).strip('<'))
        if '<' not in email or '>' not in email:
            no_email.append(email)

    write_to_file(names)
    write_to_file(adresses)
    write_to_file(no_email)



   
    return(names, adresses, no_email)


if __name__ == "__main__":
    email_blob = input('Paste emails here: ')
    cleaned = get_emails(email_blob)
    print(f'Names = {len(cleaned[0])}, Adresses = {len(cleaned[1])}, No email = {len(cleaned[2])}' )
    for x in cleaned[1]: print(x)
