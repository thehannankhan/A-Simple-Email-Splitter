# Taking an input Email and using 'strip()' to split
email = input("Enter Email:").strip()

# Cut before the '@' Symbol
userName = email[:email.index("@")]
# Cut after the '@' Symbol
domainName = email[email.index("@")+1:]

#Using '.format()' for more effecient formatting
output = "Username: '{}'    Domain: '{}'".format(userName,domainName)

print(output)
