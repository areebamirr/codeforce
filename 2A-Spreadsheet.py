
# Spreadsheet problem. 06/01/2026

# Excel to RXCY i.e. BC23 -> R23C55

def is_rxc_format(s):
    if len(s) < 4 or s[0] != 'R' or not s[1].isdigit():
        return False
    
    c_index = s.find('C')
    if c_index == -1:
        return False
    
    row_part = s[1:c_index]
    col_part = s[c_index + 1:]

    return row_part.isdigit() and col_part.isdigit() and row_part != "" and col_part != ""

def excel_to_rxc(s):
    col_letters = "" 
    row = "" 

    for char in s:
        if char.isalpha():
            col_letters += char
        else:
            row += char

    col_num = 0
    for letter in col_letters:
        col_num = col_num * 26 + (ord(letter) - ord('A') + 1)
    
    return f"R{row}C{col_num}"

def rxc_to_excel(s):
    c_index = s.find('C')

    row = s[1:c_index]
    col_num = int(s[c_index + 1:])

    col_letters = ""
    while col_num > 0:
        col_num -= 1
        remainder = col_num % 26
        col_letters = chr(ord('A') +remainder) + col_letters
        col_num //= 26

    return f"{col_letters}{row}"

def main():
    n = int(input().strip())

    convert = []
    for _ in range(n):
        s = input().strip()
        convert.append(s)

    for c in convert:
        if is_rxc_format(c):
            print(rxc_to_excel(c))
        else:
            print(excel_to_rxc(c))

if __name__ == "__main__":
    main()

