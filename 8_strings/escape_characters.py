"""
Escape characters

\t \n \' \" \\  \b
"""



# Quotes. If you only have one type of quote, use the other type to create the string.
print("Macy's is a department store.")      # Single quote in double quoted string
print('He said "Code looks good!" to me.')  # Double quote in single quoted string



print("\"Where's my book?\", she said.")  # In a double quoted string, need to escape double quotes
print('"Where\'s my book?", she said.')   # Escape single quotes in a single quoted string


# Single quotes
print('Macy\'s is a department store.')

# Newlines
print('One line\nAnother line')

# Tabs
print('There is a tab \t here')

# Backslash
print('Your file is at C:\\Users\\document.doc')

# Example:
credits_per_day = {'Monday': 4, 'Tuesday': 0, 'Friday': 3}
for day, credits in credits_per_day.items():
    print(f'{day}\t{credits} credits')




# Backslash
print('To include a tab in a string, use the \\t escape code')


# Not all escape characters are converted to a printed character.
print('123\b456')  # What does this print? What's missing?

