
def get_password_strength(password):
    digits = [str(d) for d in range(0, 10)]
    lower_case_letters = [chr(d) for d in range(ord('a'), ord('z') + 1)]
    upper_case_letters = [chr(d) for d in range(ord('A'), ord('Z') + 1)]
    special_characters = ['~', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '_']
    
    # Анализ пароля
    
    password_strength = d_count = lcl_count = ucl_count = sch_count = 0
    
    for s in password:
        if s in digits:
            d_count += 1
        elif s in lower_case_letters:
            lcl_count += 1
        elif s in upper_case_letters:
            ucl_count += 1
        elif s in special_characters:
            sch_count += 1
    
    length = len(password)
            
    # Определение надежности пароля
    
    if length > 1:
        if d_count >= 1:
            password_strength += 1
    
        if lcl_count >= 1:
            password_strength += 1
        
        if ucl_count >= 1:
            password_strength += 1
    
        if sch_count >= 1:
            password_strength += 1 
        
    if length >= 16:
        password_strength += 6
    elif length >= 8  and length < 16:
        password_strength += 4
    elif length >= 4  and length < 8:
        password_strength += 2
    elif length > 0  and length < 4:
        password_strength += 1
    
    return password_strength

if __name__ == '__main__':
    pw = input('Enter password > ')
    print("Password strength [0-10] = %d" % get_password_strength(pw))