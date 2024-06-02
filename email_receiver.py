import imaplib
import getpass

# todo this needs a tonne of work todo with the parmaters and inputs

M = imaplib.IMAP4_SSL('imap.gmail.com')
email = getpass.getpass("To login enter your email: ")
uip = getpass.getpass("Enter your password: ")
print(M.login(email, uip))
print(M.list())
choice = input("Input an option from above: ")
M.select(choice)
parameter = input('Input parameter from above: ')
typ, data = M.search(None, parameter)
email_id = data
result, email_data = M.fetch(email_id, '(RFC822')
print(email_data)

# theres loads more coding to do here
# but it will be quite a big job for something you might not use
